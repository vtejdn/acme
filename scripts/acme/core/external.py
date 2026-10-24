"""Explicit repository-local external source records and selected correspondence."""
import copy
import re
from . import repository as r

REPOSITORIES = 'repository/repositories.json'
PEOPLE = 'repository/intake-people.json'


def token(value, kind):
    r.require(isinstance(value, str) and re.fullmatch(kind + r'[1-9][0-9]*', value),
              'Use a canonical external ' + kind + ' number beginning at 1.')
    return value


def table(repo, kind):
    path, field = (REPOSITORIES, 'repositories') if kind == 'repo' else (PEOPLE, 'people')
    data = r.json_from(repo, path)
    r.require(isinstance(data, dict) and isinstance(data.get(field), list)
              and type(data.get('next')) is int and data['next'] > 0,
              'Invalid external registration table: ' + path)
    ids = []
    for index, row in enumerate(data[field]):
        r.require(isinstance(row, dict), path + '.' + field + '[' + str(index) + '] needs a record.')
        try:
            ids.append(token(row.get('id'), kind))
        except ValueError as error:
            raise ValueError(path + '.' + field + '[' + str(index) + '].id: ' + str(error)) from error
    r.require(len(ids) == len(set(ids)) and all(int(value[len(kind):]) < data['next'] for value in ids),
              'External numbers collide or allocation would reuse a number: ' + path)
    return data


def references(values, kind, field):
    r.require(isinstance(values, list), field + ' needs a list.')
    for index, value in enumerate(values):
        try: token(value, kind)
        except ValueError as error: raise ValueError(field + '[' + str(index) + ']: ' + str(error)) from error
    r.require(len(values) == len(set(values)), field + ' contains duplicate numbers.')
    return values


def repository(repo, value):
    token(value, 'repo')
    rows = [row for row in table(repo, 'repo')['repositories'] if row['id'] == value]
    r.require(len(rows) == 1, 'Register the selected external repository: ' + value)
    row = rows[0]
    field = REPOSITORIES + '[' + value + ']'
    for key in ('name', 'facts'):
        r.require(isinstance(row.get(key), str) and row[key].strip(), field + '.' + key + ' needs a nonempty string.')
    r.require(row.get('url') is None or isinstance(row['url'], str), field + '.url needs a string or null.')
    references(row.get('authors'), 'author', field + '.authors')
    return row


def person(repo, value, source=None, name=None):
    token(value, 'author')
    rows = [row for row in table(repo, 'author')['people'] if row['id'] == value]
    r.require(len(rows) == 1, 'Register the selected external author: ' + value)
    row = rows[0]
    if 'local_human' in row:
        from . import identity
        r.require(identity.person(repo, row['local_human'])['id'] == row['local_human'],
                  'Use an adopted canonical local_human correspondence.')
    sources = references(row.get('source_repositories'), 'repo', PEOPLE + '[' + value + '].source_repositories')
    r.require(isinstance(row.get('names'), list), PEOPLE + '[' + value + '].names needs qualified source-name rows.')
    r.require(isinstance(row.get('facts'), str) and row['facts'].strip(),
              PEOPLE + '[' + value + '].facts needs a nonempty string.')
    qualified = []
    for index, item in enumerate(row['names']):
        field = PEOPLE + '[' + value + '].names[' + str(index) + ']'
        r.require(isinstance(item, dict) and isinstance(item.get('name'), str) and item['name'].strip(),
                  field + ' needs an original source-local name.')
        try: reference = token(item.get('repository'), 'repo')
        except ValueError as error: raise ValueError(field + '.repository: ' + str(error)) from error
        r.require(reference in sources, field + '.repository is outside source_repositories: ' + reference)
        qualified.append((reference, item['name']))
    r.require(len(qualified) == len(set(qualified)), PEOPLE + '[' + value + '].names contains duplicates.')
    if source is not None:
        owner = repository(repo, source)
        r.require(source in row['source_repositories'] and value in owner['authors'],
                  'The selected author/repository association must agree at both entrances: ' + value + '/' + source)
        if name is not None:
            r.require({'repository': source, 'name': name} in row['names'],
                      'Supply the adopted qualified original author correspondence: ' + value + '/' + source + '/' + name)
    return row


def check_rows(repo, repositories, authors):
    """Check selected rows and their explicit counterparts, without identity inference."""
    sources = {row['id']: row for row in table(repo, 'repo')['repositories']}
    people = {row['id']: row for row in table(repo, 'author')['people']}
    selected_people = set(authors) & people.keys()
    selected_sources = set(repositories) & sources.keys()
    # Include unchanged rows that still point to a changed or removed number.
    selected_sources.update(key for key, row in sources.items()
                            if isinstance(row.get('authors'), list) and set(authors).intersection(
                                item for item in row['authors'] if isinstance(item, str)))
    selected_people.update(key for key, row in people.items()
                           if (isinstance(row.get('source_repositories'), list) and set(repositories).intersection(
                               item for item in row['source_repositories'] if isinstance(item, str)))
                           or (isinstance(row.get('names'), list) and any(
                               isinstance(item, dict) and isinstance(item.get('repository'), str)
                               and item['repository'] in repositories for item in row['names'])))
    for value in sorted(selected_sources):
        try:
            row = repository(repo, value)
            for author in row['authors']:
                person(repo, author, value)
                selected_people.add(author)
        except ValueError as error:
            raise ValueError(REPOSITORIES + '[' + value + '].authors: ' + str(error)) from error
    for value in sorted(selected_people):
        try:
            row = person(repo, value)
            for source in row['source_repositories']: person(repo, value, source)
            for name in row['names']:
                person(repo, value, name['repository'], name['name'])
                r.require(not any(other['id'] != value and any(isinstance(item, dict)
                                  and (item.get('repository'), item.get('name')) == (name['repository'], name['name'])
                                  for item in other['names'])
                                  for other in people.values() if isinstance(other.get('names'), list)),
                          'Qualified name belongs to more than one author: ' + name['repository'] + '/' + name['name'])
        except ValueError as error:
            raise ValueError(PEOPLE + '[' + value + ']: ' + str(error)) from error


def register_repository(repo, name, facts, url=None, *, timeout=30):
    r.require(isinstance(name, str) and name.strip() and isinstance(facts, str) and facts.strip(),
              'Supply the actual external name and chosen identification facts.')
    with r.locked(repo.root, timeout=timeout):
        data = table(repo, 'repo')
        value = 'repo' + str(data['next'])
        row = {'id': value, 'name': name, 'url': url, 'facts': facts, 'authors': []}
        updated = {**data, 'next': data['next'] + 1, 'repositories': [*data['repositories'], row]}
        r.write_json(repo.root / REPOSITORIES, updated, root=repo.root)
        return row


def register_person(repo, source, name, facts, author=None, *, local_human=None, timeout=30):
    r.require(isinstance(name, str) and name.strip() and isinstance(facts, str) and facts.strip(),
              'Supply the original source-local name and adopted identification facts.')
    with r.locked(repo.root, timeout=timeout):
        repository(repo, source)
        sources, people = copy.deepcopy(table(repo, 'repo')), copy.deepcopy(table(repo, 'author'))
        qualified = {'repository': source, 'name': name}
        occupied = [row['id'] for row in people['people'] if qualified in row['names']]
        r.require(not occupied or occupied == [author],
                  'The qualified source name already belongs to another external author.')
        if author is None:
            author = 'author' + str(people['next'])
            people['next'] += 1
            row = {'id': author, 'names': [], 'source_repositories': [], 'facts': facts}
            people['people'].append(row)
        else:
            person(repo, author)
            row = next(row for row in people['people'] if row['id'] == author)
        owner = next(row for row in sources['repositories'] if row['id'] == source)
        if local_human is not None:
            from . import identity
            r.require(identity.person(repo, local_human)['id'] == local_human,
                      'Register the actual local human before adopting correspondence.')
            r.require(row.get('local_human', local_human) == local_human,
                      'Conflicting adopted same-human correspondence.')
            row['local_human'] = local_human
        if source not in row['source_repositories']: row['source_repositories'].append(source)
        if author not in owner['authors']: owner['authors'].append(author)
        qualified = {'repository': source, 'name': name}
        if qualified not in row['names']: row['names'].append(qualified)
        from .publication import publish_files
        pending = {REPOSITORIES: r.encoded(sources), PEOPLE: r.encoded(people)}
        expected = {path: r.read_from(repo, path) for path in pending}
        publish_files(repo, pending, expected)
        return row
