"""Human identity registration and checkout-local attribution, without account authentication."""
import json
from pathlib import Path
import re
import subprocess
from . import repository as r

KEY = re.compile(r'[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*')


def key(value):
    r.require(isinstance(value, str) and KEY.fullmatch(value),
              'Identity keys use letters, digits and internal hyphens; underscores separate identifier fields.')
    return value


def repository_name(value, *, required=False):
    """Validate the chosen repository name; personal folders may remain unnamed."""
    if value is None:
        r.require(not required,
                  'Register the human-chosen repository name in repository/config.json before Git research writing or delivery; keep existing materials and use identity-bind for this checkout.')
        return None
    r.require(isinstance(value, str) and KEY.fullmatch(value),
              'Repository names use letters, digits and internal hyphens; ask the human for a valid choice without deriving it from the author key or folder.')
    return value


def attribution_name(value):
    r.require(isinstance(value, str) and value.strip() and '\n' not in value and '\r' not in value,
              'Supply a nonempty single-line display_name for License attribution, separately from the author key.')
    return value


def git(root, *args, optional=False):
    result = subprocess.run(['git', *args], cwd=root, capture_output=True, text=True, encoding='utf-8')
    if optional and result.returncode == 1:
        return ''
    r.require(result.returncode == 0, 'Local Git operation failed: ' + result.stderr.strip())
    return result.stdout.strip()


def checkout(root):
    actual = git(root, 'rev-parse', '--show-toplevel')
    r.require(Path(actual).resolve() == Path(root).resolve(), 'Local identity must belong to this exact Git checkout.')


def git_managed(root):
    """An existing marker retains Git requirements, including broken markers."""
    try: (Path(root) / '.git').lstat()
    except FileNotFoundError: return False
    return True


def registry(repo):
    return validate_registry_value(repo.identity_registry if hasattr(repo, 'identity_registry') else r.read_json(repo.home / 'people.json', root=repo.root))


def validate_registry_value(data):
    r.require(isinstance(data.get('people'), list), 'Invalid human identity registry.')
    seen, identities, accounts = set(), set(), set()
    for person in data['people']:
        name = key(person['id'])
        r.require(not re.fullmatch(r'author[1-9][0-9]*', name, re.I),
                  'External author numbers cannot register or bind a local operator; choose a readable local name.')
        r.require(name.casefold() not in seen, 'Human identity collision ignoring case: ' + name)
        seen.add(name.casefold())
        r.require(isinstance(person.get('display_name'), str) and person['display_name'].strip(), 'Human display name is required.')
        if 'registered_at' in person: r.require(False, 'Administrative registration timestamps are retired.')
        for item in person.get('git_identities', []):
            r.require(all(isinstance(item.get(k), str) and item[k].strip() for k in ('name', 'email')), 'Incomplete Git identity.')
            pair = (item['name'], item['email'].casefold())
            r.require(pair not in identities, 'Git identity assigned more than once.')
            identities.add(pair)
        for account in person.get('github_accounts', []):
            key(account)
            r.require(account.casefold() not in accounts, 'GitHub account assigned more than once.')
            accounts.add(account.casefold())
    return data


def person(repo, value):
    key(value)
    matches = [p for p in registry(repo)['people'] if p['id'].casefold() == value.casefold()]
    r.require(len(matches) == 1, 'Register the human identity before use: ' + value)
    return matches[0]


def source_author(repo, author, source):
    """Resolve the actual qualified source author in this supplied view."""
    from . import external
    if re.fullmatch(r'author[1-9][0-9]*', author):
        return external.person(repo, author, source)
    else:
        # U keeps its readable original author and qualified source name.
        matches = [item for item in external.table(repo, 'author')['people']
                   if {'repository': source, 'name': author} in item.get('names', [])]
        r.require(len(matches) == 1, 'Direct revision needs one adopted same-human source-author correspondence.')
        return external.person(repo, matches[0]['id'], source, author)


def require_author(repo, author, source=None):
    """Use adopted human correspondence, never a caller's author argument."""
    actual = actor(repo)
    if source is None:
        r.require(person(repo, author)['id'] == author == actual,
                  'Correct another human\'s authored content in your own document with an exact reference.')
    else:
        row = source_author(repo, author, source)
        r.require(row.get('local_human') == actual,
                  'Direct revision needs adopted same-human correspondence in the external person record.')
    return actual


def worktree_enabled(root, runner=None):
    run = runner or git
    return run(root, 'config', '--local', '--bool', '--get',
               'extensions.worktreeConfig', optional=True) == 'true'


def enable_worktree_config(root):
    if worktree_enabled(root):
        return
    common = Path(git(root, 'rev-parse', '--path-format=absolute', '--git-common-dir'))
    config = common / 'config'
    main = common / 'config.worktree'
    # These settings formerly applied only to the main checkout. Keep that scope
    # before the extension makes the ordinary config common to all worktrees.
    settings = {}
    for key_name in ('core.worktree', 'core.bare'):
        value = git(root, 'config', '--local', '--get', key_name, optional=True)
        if value and (key_name != 'core.bare' or
                      git(root, 'config', '--local', '--bool', '--get', key_name) == 'true'):
            settings[key_name] = value
    for key_name, value in settings.items():
        existing = git(root, 'config', '--file', str(main), '--get', key_name, optional=True) if main.exists() else ''
        r.require(not existing or existing == value,
                  'Resolve the existing main worktree configuration before enabling worktree bindings.')
    before = {path: path.read_bytes() if path.exists() else None for path in (config, main)}
    try:
        for key_name, value in settings.items():
            git(root, 'config', '--file', str(main), '--replace-all', key_name, value)
            git(root, 'config', '--file', str(config), '--unset-all', key_name)
        git(root, 'config', '--file', str(config), 'extensions.worktreeConfig', 'true')
    except Exception:
        for path, data in before.items():
            if data is not None:
                r.write_bytes(path, data)
            elif path.exists():
                path.unlink()
        raise


def worktree_scope(root, runner=None):
    run = runner or git
    locations = run(root, 'rev-parse', '--path-format=absolute', '--git-dir', '--git-common-dir').splitlines()
    r.require(len(locations) == 2, 'Cannot determine this worktree configuration identity.')
    directory, common = (Path(value).resolve() for value in locations)
    r.require(directory.is_relative_to(common), 'Unsupported external worktree administration directory.')
    return 'main' if directory == common else directory.relative_to(common).as_posix()


def actor(repo, *, runner=None):
    if runner is None and not git_managed(repo.root):
        people = registry(repo)['people']
        r.require(len(people) == 1, 'Personal use without Git requires one explicitly registered local human.')
        return people[0]['id']
    repository_name(repo.config.get('repository'), required=True)
    run = runner or git
    actual = run(repo.root, 'rev-parse', '--show-toplevel')
    r.require(Path(actual).resolve() == repo.root.resolve(),
              'Local identity must belong to this exact Git checkout.')
    r.require(worktree_enabled(repo.root, run),
              'Bind this checkout once with identity-bind to migrate its shared legacy actor.')
    value = run(repo.root, 'config', '--worktree', '--get', 'research.actor', optional=True)
    scope = run(repo.root, 'config', '--worktree', '--get', 'research.actorWorktree', optional=True)
    # Git may copy config.worktree when adding a worktree. A copied actor is not
    # confirmation that the new checkout belongs to that operator.
    r.require(value and scope == worktree_scope(repo.root, run),
              'Bind this checkout once with identity-bind; no shared or copied default actor is used.')
    return person(repo, value)['id']


def bind(repo, value):
    r.check_storage(repo.root)
    checkout(repo.root)
    canonical = person(repo, value)['id']
    enable_worktree_config(repo.root)
    git(repo.root, 'config', '--worktree', 'research.actor', canonical)
    git(repo.root, 'config', '--worktree', 'research.actorWorktree', worktree_scope(repo.root))
    # Explicit binding confirms this checkout only. Other worktrees without their
    # own binding must ask for one instead of inheriting the last shared operator.
    if git(repo.root, 'config', '--local', '--get', 'research.actor', optional=True):
        git(repo.root, 'config', '--local', '--unset-all', 'research.actor')
    location = git(repo.root, 'rev-parse', '--git-path', 'config.worktree')
    return {'actor': canonical, 'storage': location + ': research.actor'}


def register(repo, value, display_name, git_name=None, git_email=None, github_account=None, *, timeout=30):
    key(value); attribution_name(display_name)
    with r.locked(repo.root, timeout=timeout):
        r.check_storage(repo.root)
        key(value)
        r.require(bool(git_name) == bool(git_email), 'Provide Git name and email together.')
        data = registry(repo)
        r.require(not any(p['id'].casefold() == value.casefold() for p in data['people']), 'Human identity is already registered.')
        if not git_managed(repo.root):
            r.require(not data['people'], 'Personal use without Git supports one local human; retain original authors as external identities.')
            registrar = value
        elif not data['people']:
            checkout(repo.root)
            r.require(not git(repo.root, 'config', '--get', 'research.actor', optional=True)
                      and not git(repo.root, 'config', '--get', 'research.actorWorktree', optional=True),
                      'Empty registry conflicts with an existing research binding.')
            registrar = value
        else:
            registrar = actor(repo)
        entry = {'id': value, 'display_name': display_name,
                 'git_identities': [{'name': git_name, 'email': git_email}] if git_name else [],
                 'github_accounts': [github_account] if github_account else [], 'registered_by': registrar}
        # Validate the proposed complete registry before publishing it.
        proposed = {**data, 'people': data['people'] + [entry]}
        validate_registry_value(proposed)
        r.write_json(repo.home / 'people.json', proposed, root=repo.root)
        return entry


def initialize(root, username, repository, url=None, git_name=None, git_email=None, github_account=None, *, display_name):
    root = Path(root).resolve()
    r.check_storage(root)
    key(username); repository_name(repository, required=True); attribution_name(display_name)
    r.require(bool(git_name) == bool(git_email), 'Provide Git name and email together.')
    r.require(not (root / 'repository/config.json').exists(), 'Repository is already initialized.')
    config = {'repository': repository, 'layout_format': 2,
              'repository_url': url, 'material_next': {}, 'framework_update_check': True}
    people = {'people': [{'id': username, 'display_name': display_name,
              'registered_by': username,
              'git_identities': [{'name': git_name, 'email': git_email}] if git_name else [],
              'github_accounts': [github_account] if github_account else []}]}
    validate_registry_value(people)
    for name in ('people.json', 'config.json', 'repositories.json', 'intake-people.json'):
        r.require(not (root / 'repository' / name).exists(), 'Initialization target already has identity/configuration: ' + name)
    root.mkdir(parents=True, exist_ok=True)
    if not (root / '.git').exists():
        git(root, 'init', '--quiet')
    checkout(root)
    r.write_json(root / 'repository/people.json', people, exclusive=True, root=root)
    r.write_json(root / 'repository/config.json', config, exclusive=True, root=root)
    r.write_json(root / 'repository/repositories.json', {'next': 1, 'repositories': []}, exclusive=True, root=root)
    r.write_json(root / 'repository/intake-people.json', {'next': 1, 'people': []}, exclusive=True, root=root)
    repo = r.Repository(root)
    bind(repo, username)
    return repo


