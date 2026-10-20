"""Pure route and feedback views for material-owned documents.

The navigation writer uses these pure views. Callers supply the relevant
parsed documents and a read-only material loader; this module writes no source
material, acquisition record, registry or generated file.
"""
from dataclasses import dataclass
from html import escape
import posixpath
import re
from urllib.parse import quote

from . import documents as materials
from . import identity as identity
from . import discovery
from ..core import links as links
from ..core import source_refs

require = identity.require
INDEX = 'mathematics/strategies/index.md'
DISPOSITIONS = {'proposed', 'active', 'paused', 'blocked', 'completed', 'refuted', 'superseded'}


@dataclass(frozen=True)
class Association:
    target: materials.Locator
    scope: str


@dataclass(frozen=True)
class Route:
    document: materials.Document
    tasks: tuple
    disposition: str | None
    priority: str | None
    parent: materials.Locator | None = None
    parent_line: int | None = None


@dataclass(frozen=True)
class Feedback:
    document: materials.Document
    relation: str
    source: materials.Locator
    scope: str


def table(document, heading, columns, *, with_lines=False):
    """Read eligible structures, then decode their original visible cells."""
    sections = materials.MarkdownInput(document.text.replace('\r\n', '\n')).sections(heading)
    require(len(sections) <= 1, 'Repeated navigation section: ' + heading)
    if not sections:
        return []
    content, first_line = sections[0]
    try:
        rows = content.table(columns)
    except ValueError as error:
        raise ValueError(str(error) + ' Section: ' + heading) from error
    return [(cells, first_line + number) for cells, number in rows] if with_lines else [cells for cells, _ in rows]


def route(document):
    require(document.identity.kind == 'S', 'Only a Strategy owns a route.')
    associations = []
    require(not document.identity.source_repository, 'Public source Strategies are referenced, not acquired.')
    for target, scope in table(document, 'Task associations', ('Task', 'Scope')):
        loc = materials.locator(document.path, target)
        require(identity.parse(loc.path).kind == 'T', 'A route association must name a fixed Task material.')
        associations.append(Association(loc, scope))
    fields = {}
    parent, parent_line = None, None
    try:
        rows = table(document, 'Route', ('Field', 'Value'), with_lines=True)
        for (key, value), line in rows:
            require(key in {'disposition', 'priority', 'parent'} and key not in fields,
                    'Unknown or repeated route field: ' + key)
            fields[key] = value
            if key == 'parent':
                parent_line = line + 1
                parent = materials.locator(document.path, value)
                require(identity.parse(parent.path).kind == 'S', 'Route parent must name a Strategy.')
                require(parent.anchor, 'Route parent needs an exact stable anchor.')
                require(identity.parse(parent.path).family.casefold() != document.identity.family.casefold(),
                        'A route cannot be its own parent.')
    except ValueError as error:
        raise ValueError(document.path + (':' + str(parent_line) if parent_line else '') +
                         ': Route: ' + str(error)) from error
    require('disposition' not in fields or fields['disposition'] in DISPOSITIONS, 'Undefined route disposition.')
    return Route(document, tuple(associations), fields.get('disposition'), fields.get('priority'), parent, parent_line)


def validate_routes(documents, read, *, paths=()):
    """Validate supplied local routes and their actual selected-view ancestors."""
    loaded, families, done, visiting = {}, {}, set(), []
    paths = list(paths)

    def register(document):
        if not document.identity.source_repository:
            candidates = set(discovery.selected(paths, family=document.identity)) | {document.path}
            for candidate in candidates: identity.parse(candidate)
            require(len(candidates) == 1, 'Ambiguous route identity: ' + ', '.join(sorted(candidates)))
        key = (document.identity.family.casefold(), document.header.get('source_repository'),
               posixpath.dirname(document.path) if document.identity.source_repository else None)
        require(key not in families or families[key] == document.path,
                'Ambiguous route identity: ' + document.path)
        families[key] = document.path
        loaded[document.path] = route(document)

    for document in documents:
        if document.identity.kind == 'S':
            register(document)

    def visit(path):
        if path in done:
            return
        require(path not in visiting, 'Route parent cycle: ' + ' -> '.join(visiting + [path]))
        visiting.append(path)
        item = loaded[path]
        if item.parent:
            parent = item.parent
            place = path + ':' + str(item.parent_line) + ': parent ' + parent.path + '#' + parent.anchor
            try:
                parent_ident = identity.parse(parent.path)
                require(not parent_ident.source_repository, 'Route parents must be local Strategies.')
                if parent.path not in loaded:
                    try:
                        register(materials.parse(parent.path, read(parent.path)))
                    except (FileNotFoundError, KeyError):
                        raise ValueError('Unresolved route parent.')
                target = loaded[parent.path].document
                require(target.identity.kind == 'S', 'Route parent must name a Strategy.')
                require(parent.anchor in links.anchors_text(target.text), 'Route parent anchor missing.')
                visit(parent.path)
            except ValueError as error:
                raise ValueError(place + ': ' + str(error)) from error
        visiting.pop()
        done.add(path)

    for path in tuple(loaded):
        visit(path)
    return loaded


def feedback(document):
    if document.identity.kind not in 'SL':
        return []
    result = []
    for relation, source, scope in table(document, 'Feedback and lineage', ('Relation', 'Source', 'Scope')):
        require(relation in {'feedback', 'predecessor'}, 'Unknown feedback or lineage relation: ' + relation)
        loc = materials.locator(document.path, source)
        origin = source_refs.parse(loc.path)
        source_kind = identity.parse(origin['path'] if origin else loc.path).kind
        require(source_kind in 'SL', 'Feedback source must be a Strategy or fixed ledger material.')
        require(relation != 'predecessor' or (source_kind == 'S' and document.identity.kind == 'S'),
                'Route predecessors require a source and successor Strategy.')
        result.append(Feedback(document, relation, loc, scope))
    return result


def task_anchor(task):
    ident = identity.parse(task) if isinstance(task, str) else task
    require(ident.kind == 'T', 'A Task-specific entrance needs a Task identity.')
    return 'task-' + ident.family.lower()


def continuation_link(task, documents):
    """Suggest an entrance only for explicitly associated routes; write nothing."""
    ident = identity.parse(task)
    require(ident.kind == 'T', 'A continuation entrance belongs to a Task.')
    found = any(identity.parse(item.target.path).family == ident.family
                for document in documents if document.identity.kind == 'S'
                for item in route(document).tasks)
    if not found:
        return None
    target = posixpath.relpath(INDEX, posixpath.dirname(task))
    return '[Related routes](' + quote(target, safe='/._-') + '#' + task_anchor(ident) + ')'


def cell(value):
    return (escape(str(value), quote=False).replace('|', '&#124;')
            .replace('[', '&#91;').replace(']', '&#93;').replace('\r', ' ').replace('\n', ' '))


def link(label, loc):
    if source_refs.external(loc.path):
        destination = loc.path + ('#' + quote(loc.anchor, safe='._-') if loc.anchor else '')
        return '[' + cell(label) + '](' + destination + ')'
    target = posixpath.relpath(loc.path, posixpath.dirname(INDEX))
    destination = quote(target, safe='/._-') + ('#' + quote(loc.anchor, safe='._-') if loc.anchor else '')
    return '[' + cell(label) + '](' + destination + ')'


def views(documents, read, *, source_info=None, unavailable=None, paths=()):
    """Return derived index text, retaining exact source and Task formulations.

    This view never resolves a Claim/Task assessment, promotes imported source
    status, or selects a newer argument. Acquisition metadata never supplies a recipient judgment.
    """
    documents = tuple(documents)
    by_path = {document.path: document for document in documents}
    require(len(by_path) == len(documents), 'Duplicate material navigation input.')
    loaded = dict(by_path)
    task_origins = {}

    def register_task(document):
        if document.identity.kind == 'T':
            family = document.identity.family
            source = document.header.get('source_repository')
            require(family not in task_origins or task_origins[family] == source,
                    'Conflicting original repository identities for Task family: ' + family)
            task_origins[family] = source

    for document in documents:
        register_task(document)

    def target(loc):
        if loc.path not in loaded:
            loaded[loc.path] = materials.parse(loc.path, read(loc.path))
        document = loaded[loc.path]
        register_task(document)
        require(not loc.anchor or loc.anchor in links.anchors_text(document.text),
                'Navigation target anchor missing: ' + loc.path + '#' + loc.anchor)
        return document

    hierarchy = validate_routes(documents, read, paths=paths)
    routes = [hierarchy[document.path] for document in documents if document.identity.kind == 'S']

    def ancestry(item):
        chain = [item.document.path]
        while item.parent:
            chain.append(item.parent.path)
            if item.parent.path not in hierarchy:
                break
            item = hierarchy[item.parent.path]
        return tuple(reversed(chain))

    def context(item, scope):
        if not item.parent:
            return 'Source root' if item.document.identity.source_repository else 'Root'
        if item.parent.path not in hierarchy:
            return 'Unavailable source context: ' + cell(item.parent.path + '#' + item.parent.anchor)
        label = hierarchy[item.parent.path].document.identity.name
        prefix = 'Source parent: ' if item.document.identity.source_repository else 'Parent: '
        if item.parent.path not in scope:
            prefix += 'outside this view; '
        return prefix + link(label, item.parent)

    def route_link(item):
        return ('&#8627; ' * (len(ancestry(item)) - 1) +
                link(item.document.identity.name, materials.Locator(item.document.path, '')))
    groups = {}
    for item in routes:
        for association in item.tasks:
            task = target(association.target)
            groups.setdefault(task.identity.family, []).append((item, association, task))
    anchors = [task_anchor(entries[0][2].identity) for entries in groups.values()]
    require(len(set(anchors)) == len(anchors), 'Conflicting Task entrance anchors.')
    output = ['# Strategy Navigation', '',
              'Derived from explicit material relationships.',
              'Route materials own their disposition and priority.',
              'An association to a historical Task contract does not establish applicability to a changed contract.',
              'Navigation does not authorize execution, select evidence or reopen a Task.',
              'Hierarchy and reverse child listings include only the supplied routes; omitted children are not '
              'asserted absent.',
              'Each Task entrance includes only that route\'s explicit Task associations.', '']
    if not groups:
        output.extend(['No explicit Task-to-route associations in the supplied materials.', ''])
    for family, entries in sorted(groups.items()):
        display_use = False
        use_column = ''
        output.extend(['<a id="' + task_anchor(entries[0][2].identity) + '"></a>',
                       '## ' + cell(family), '',
                       '| Route | Title | Author | Disposition | Priority | Exact Task contract | Association scope | Organization |' + use_column,
                       '| --- | --- | --- | --- | --- | --- | --- | --- |' + (' --- |' if display_use else '')])
        scope = {entry[0].document.path for entry in entries}
        for item, association, task in sorted(entries, key=lambda entry: (ancestry(entry[0]), entry[1].target.path, entry[1].target.anchor)):
            document = item.document
            source_prefix = 'Source: ' if document.identity.source_repository else ''
            values = [route_link(item),
                      cell(document.title), cell(document.header['author']),
                      cell(source_prefix + (item.disposition or 'Not stated')),
                      cell(source_prefix + (item.priority or 'Not stated')),
                      link(task.identity.name + ': ' + task.title, association.target), cell(association.scope), context(item, scope)]
            output.append('| ' + ' | '.join(values) + ' |')
        output.append('')

    unassociated = [item for item in routes if not item.tasks]
    if unassociated:
        output.extend(['## Other Supplied Routes and Source Context', '',
                       'No local Task association is inferred from a parent or from a captured source assertion.', '',
                       '| Route | Title | Author | Disposition | Priority | Organization |',
                       '| --- | --- | --- | --- | --- | --- |'])
        scope = {item.document.path for item in unassociated}
        for item in sorted(unassociated, key=ancestry):
            document = item.document
            prefix = 'Source: ' if document.identity.source_repository else ''
            output.append('| ' + ' | '.join([route_link(item), cell(document.title),
                cell(document.header['author']), cell(prefix + (item.disposition or 'Not stated')),
                cell(prefix + (item.priority or 'Not stated')), context(item, scope)]) + ' |')
        output.append('')

    contributions = [item for document in documents if not document.identity.source_repository
                     for item in feedback(document)]
    if contributions:
        output.extend(['## Feedback and Derived Routes', '',
                       'These are the contributor\'s stated relationships and scopes.',
                       'They do not indicate source-author endorsement, adoption, or a change to the source route\'s disposition.',
                       'A received original remains distinct even when its author matches the local operator.', '',
                       '| Contribution | Title | Author | Relation | Exact source formulation | Source author | Scope |',
                       '| --- | --- | --- | --- | --- | --- | --- |'])
        for item in sorted(contributions, key=lambda item: (item.source.path, item.source.anchor, item.document.path, item.relation)):
            origin = source_refs.parse(item.source.path)
            source = None if origin else target(item.source)
            source_identity = identity.parse(origin['path']) if origin else source.identity
            document = item.document
            values = [link(document.identity.name, materials.Locator(document.path, '')),
                      cell(document.title), cell(document.header['author']), cell(item.relation),
                      link(source_identity.name + (': ' + source.title if source else ' (external source)'), item.source),
                      cell(source_identity.author), cell(item.scope)]
            output.append('| ' + ' | '.join(values) + ' |')
        output.append('')
    return {INDEX: '\n'.join(output).rstrip() + '\n'}
