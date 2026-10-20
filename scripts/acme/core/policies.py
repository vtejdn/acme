"""Locate applicable policy sources without inventing or activating a policy."""
from . import identity
from . import repository as r


def sources(repo, topic, *, author=None, subfield=None, document=None):
    r.require(topic in {'execution', 'writing'}, 'Unknown policy topic.')
    operator = repo.actor()
    person = identity.person(repo, author or operator)['id'] if topic == 'writing' else operator
    values = ['framework/rules/' + ('writing' if topic == 'writing' else 'execution') + '.md']
    base = 'profiles/' + person + '/'
    if topic == 'writing':
        values.append(base + 'writing/readme.md')
        if subfield:
            r.require(subfield.replace('_', '').isalnum(), 'Use a named subfield, not a path.')
            values.append(base + 'writing/' + subfield + '.md')
    else:
        values.append(base + 'execution.md')
    if document:
        r.safe_path(repo.root, document)
        values.append(document)
    return {'operator': operator, 'responsible_human': person,
            'sources_low_to_high': [value for value in values if (repo.root / value).is_file()],
            'interpretation': 'Read the actual scope, active/default clauses and end conditions. This locator does not activate policy, authorize resumption or reset an E allowance.'}
