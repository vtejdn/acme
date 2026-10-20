"""Bounded derived navigation retaining fixed history and original source scope."""
import posixpath
from urllib.parse import quote
from . import discovery, documents, identity, validation
from .navigation import cell
from ..core import source_refs

INDEXES = {'C': 'mathematics/claims/index.md', 'T': 'mathematics/tasks/index.md'}
require = identity.require

def link(index, label, locator):
    path, anchor = locator['path'], locator.get('anchor', '')
    if source_refs.external(path):
        href = path
    else:
        href = quote(posixpath.relpath(path, posixpath.dirname(index)), safe='/._-')
        if anchor:
            href += '#' + quote(anchor, safe='._-')
    return '[' + cell(label) + '](' + href + ')'

def views(paths, read, *, source_info=None):
    paths = tuple(paths)
    require(all(identity.parse(path).kind in 'CT' for path in paths), 'Claim/Task indexes accept only explicit C/T material paths.')
    cache = {}
    def source(path):
        if source_refs.external(path):
            raise FileNotFoundError('Original reference outside local acquisition: ' + path)
        if path not in cache:
            raw = read(path)
            cache[path] = raw.decode('utf-8-sig') if isinstance(raw, bytes) and path.endswith('.md') else raw
        return cache[path]
    def document(path):
        return documents.parse(path, source(path))
    rows = discovery.families(paths, source, source_info=source_info)
    rows.sort(key=lambda row: (identity.parse(row['path']).author, identity.parse(row['path']).source_repository or '',
                              identity.parse(row['path']).line, identity.parse(row['path']).number))
    output = {}
    for kind, index in INDEXES.items():
        title = 'Claim' if kind == 'C' else 'Task'
        lines = ['# ' + title + ' Navigation', '',
                 'Derived from supplied material revisions and their explicit selections.',
                 'Source assessments belong to their original authors; acquisition does not establish a recipient judgment.', '',
                 '| Family and entrance | Title | Author | Original repository | Selected decision | Status | Role | Statement or contract | Current argument | Review evidence | Review classification |',
                 '| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |']
        chosen = [row for row in rows if row['kind'] == kind]
        outside = []
        for row in chosen:
            doc = document(row['path'])
            imported = bool(doc.identity.source_repository)
            if source_refs.external(doc.current.path):
                require(imported, 'Local decisions must select locally available evidence.')
                owner, selected = None, None
            else:
                owner, selected = documents.selection(doc, source)
            refs = {role: [] for role in ('statement', 'contract', 'argument', 'review')}
            if selected:
                for role, loc, scope in selected.relations:
                    external = source_refs.external(loc.path)
                    if external:
                        require(imported, 'Required input is outside acquired scope: ' + loc.path)
                        outside.append((row['family'], role, loc, scope))
                    else:
                        validation.validate_locator_targets([vars(loc)], source)
                        if role in {'statement', 'contract'}:
                            primary = document(loc.path)
                            require(primary.identity.family == owner.identity.family
                                    and documents.original_family(primary) == documents.original_family(owner),
                                    'Selected primary material has another family or original family identity.')
                    if role in refs:
                        refs[role].append(('Source only: ' if external else '') + link(index, scope, vars(loc)))
            origin = doc.identity.source_repository if imported else 'Local original'
            status = selected.fields['status'] if selected else 'Source decision outside acquired scope'
            values = [link(index, row['family'], {'path': row['path']}), cell(row['title']), cell(row['author']), cell(origin),
                      link(index, doc.current.anchor or 'Original decision', vars(doc.current)), ('Source: ' if imported else '') + cell(status),
                      cell(selected.fields.get('role', 'Not stated') if selected else 'Unavailable'),
                      '; '.join(refs['statement' if kind == 'C' else 'contract']) or 'Unavailable',
                      '; '.join(refs['argument']) or 'Not selected', '; '.join(refs['review']) or 'Not selected',
                      ('Source: ' if imported else '') + cell(selected.fields.get('review-status', 'Not stated') if selected else 'Unavailable')]
            lines.append('| ' + ' | '.join(values) + ' |')
        if not chosen:
            lines.extend(['', 'No ' + title.lower() + ' materials were supplied.'])
        lines.extend(['', '## Fixed History', '', 'Retained decisions and historical-only assessments keep their exact scope; history is navigation, not a new selection.', '',
                      '| Family | Material version | Decisions | Historical-only assessments |', '| --- | --- | --- | --- |'])
        for row in chosen:
            for old in row['versions']:
                refs = lambda field: '; '.join(link(index, anchor, {'path': old['path'], 'anchor': anchor}) for anchor in old[field]) or 'None'
                label = 'v' + str(old['version']) + (' (archival material)' if old['archival'] else '')
                lines.append('| ' + ' | '.join([cell(row['family']), link(index, label, {'path': old['path']}), refs('decisions'), refs('historical_assessments')]) + ' |')
        if outside:
            lines.extend(['', '## Unacquired Source Inputs', '', '| Family | Role | Original input | Scope |', '| --- | --- | --- | --- |'])
            for family, role, loc, scope in outside:
                lines.append('| ' + ' | '.join([cell(family), cell(role), link(index, 'Original source', vars(loc)), cell(scope)]) + ' |')
        output[index] = '\n'.join(lines) + '\n'
    return output
