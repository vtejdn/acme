"""Bounded derived navigation retaining fixed history and original source scope."""
import posixpath
from pathlib import PurePosixPath
from urllib.parse import quote
from . import discovery, documents, identity, validation, review
from .navigation import cell
from ..core import source_refs, paths as storage_paths

INDEXES = {'C': 'mathematics/claims/index.md', 'T': 'mathematics/tasks/index.md'}
require = identity.require

def link(index, label, locator):
    path, anchor = locator['path'], locator.get('anchor', '')
    if source_refs.external(path):
        href = path + ('#' + quote(anchor, safe='._-') if anchor else '')
    else:
        href = quote(posixpath.relpath(path, posixpath.dirname(index)), safe='/._-')
        if anchor:
            href += '#' + quote(anchor, safe='._-')
    return '[' + cell(label) + '](' + href + ')'


def native_target(locator):
    """Classify a declared J child without probing or loading its payload."""
    path = locator['path']
    storage_paths.check_local_role(path)
    storage_paths.check_public_target(path)
    try:
        ident = identity.parse(path)
    except ValueError:
        return False
    if ident.kind != 'J':
        return False
    entrance = 'mathematics/computations/programs/' + ident.name + '/readme.md'
    parts = PurePosixPath(path).parts
    require(len(parts) >= 5 and parts[3] == ident.name
            and parts[:3] in {('mathematics', 'computations', 'programs'),
                             ('mathematics', 'computations', 'outputs')},
            'A declared computation target needs its actual J storage identity.')
    return path != entrance


def target_link(index, label, locator):
    if not source_refs.external(locator['path']) and native_target(locator):
        # A code locator preserves a native fragment without promising a
        # currently available local data link or treating it as a source URI.
        address = locator['path'] + ('#' + locator['anchor'] if locator.get('anchor') else '')
        fence = '`'
        while fence in address:
            fence += '`'
        return fence + ' ' + address.replace('|', '\\|') + ' ' + fence
    return link(index, label, locator)


def check_target(locator, read):
    if not native_target(locator):
        validation.validate_locator_targets([locator], read)

def views(paths, read, *, source_info=None, strategy_paths=()):
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
                 'Status belongs to the exact selected decision; original lineage and acquisition remain separate facts.', '',
                 '| Family and entrance | Title | Author | Original repository | Selected decision | Status | Statement or contract | Current argument | Review evidence |',
                 '| --- | --- | --- | --- | --- | --- | --- | --- | --- |']
        chosen = [row for row in rows if row['kind'] == kind]
        outside = []
        findings = []
        for row in chosen:
            doc = document(row['path'])
            imported = bool(doc.identity.source_repository)
            owner, selected = None, None
            if doc.current is not None:
                try:
                    owner, selected = documents.selection(doc, source, source_info=source_info)
                except FileNotFoundError:
                    if not source_refs.external(doc.current.path):
                        raise
            refs = {role: [] for role in ('statement', 'contract', 'argument', 'review')}
            if selected:
                for role, loc, scope in selected.relations:
                    external = source_refs.external(loc.path)
                    if external:
                        require(imported, 'Required input is outside acquired scope: ' + loc.path)
                        outside.append((row['family'], role, loc, scope))
                    else:
                        if role in {'statement', 'contract'}:
                            require(identity.parse(loc.path).family == owner.identity.family,
                                    'Selected primary material has another family or original family identity.')
                        if role == 'review':
                            require(identity.parse(loc.path).kind in 'RL', 'Selected review needs its actual R/L finding entrance.')
                        check_target(vars(loc), source)
                        if role in {'statement', 'contract'}:
                            primary = document(loc.path)
                            require(primary.identity.family == owner.identity.family
                                    and documents.original_family(primary) == documents.original_family(owner),
                                    'Selected primary material has another family or original family identity.')
                    if role in refs:
                        refs[role].append(('Source only: ' if external else '') + target_link(index, scope, vars(loc)))
                    if role == 'review' and kind == 'C':
                        claim = link(index, row['family'], {'path': row['path']})
                        decision_link = link(index, doc.current.anchor, vars(doc.current))
                        finding_link = ('Source only: ' if external else '') + link(index, loc.anchor or 'Whole account', vars(loc))
                        if external:
                            findings.append([claim, decision_link, finding_link, 'Unavailable source finding', 'Unavailable', 'Unavailable'])
                            continue
                        account = document(loc.path)
                        relationship = review.relationships(account, finding=loc).get(loc, 'Not declared')
                        bound = review.bindings(account, finding=loc)
                        if not bound:
                            findings.append([claim, decision_link, finding_link, cell(relationship), 'Not declared', 'Not declared'])
                        for _finding, target, checked_scope in bound:
                            unavailable = source_refs.external(target.path)
                            if not unavailable: check_target(vars(target), source)
                            inspected = ('Source only: ' if unavailable else '') + target_link(index, target.path + ('#' + target.anchor if target.anchor else ''), vars(target))
                            findings.append([claim, decision_link, finding_link, cell(relationship), inspected, cell(checked_scope)])
            origin = doc.identity.source_repository if imported else 'Local original'
            status = selected.fields['status'] if selected else ('Not selected' if doc.current is None else 'Source decision outside acquired scope')
            values = [link(index, row['family'], {'path': row['path']}), cell(row['title']), cell(row['author']), cell(origin),
                      link(index, doc.current.anchor or 'Original decision', vars(doc.current)) if doc.current else 'Not selected', cell(status),
                      '; '.join(refs['statement' if kind == 'C' else 'contract']) or 'Unavailable',
                      '; '.join(refs['argument']) or 'Not selected', '; '.join(refs['review']) or 'Not selected']
            lines.append('| ' + ' | '.join(values) + ' |')
        if not chosen:
            lines.extend(['', 'No ' + title.lower() + ' materials were supplied.'])
        if kind == 'T':
            lines.extend(['', '## Joint Tasks and Participation', '',
                          'Derived from the supplied individual Tasks\' exact joint-task declarations.',
                          'Omitted participants are not asserted absent; no lifecycle or execution state propagates.', '',
                          '| Adopted joint contract | Individual Task | Human | Strategy entrance |',
                          '| --- | --- | --- | --- |'])
            participants = []
            from . import tasks
            from .navigation import route
            strategies = [(candidate, route(document(candidate))) for candidate in strategy_paths]
            for row in chosen:
                doc = document(row['path'])
                tasks.validate(doc, source, paths=paths)
                if doc.joint_task:
                    parent = document(doc.joint_task.path)
                    participants.append('| ' + ' | '.join([
                        link(index, parent.identity.name, vars(doc.joint_task)),
                        link(index, doc.identity.name, {'path': doc.path}), cell(doc.identity.author),
                        '; '.join(link(index, identity.parse(candidate).name, {'path': candidate})
                                  for candidate, strategy in strategies if any(
                                      identity.parse(association.target.path).family == doc.identity.family
                                      for association in strategy.tasks)) or 'No strategies supplied in this view']) + ' |')
            lines.extend(participants or ['', 'No participation declarations in the supplied Tasks.'])
        if kind == 'C':
            lines.extend(['', '## Selected Review Findings', '',
                          'Relationships and checked scopes are declared by each selected finding; no aggregate review grade or proof verdict is inferred.', '',
                          '| Claim | Current decision | Selected finding | Declared relationship | Reviewed input | Declared scope |',
                          '| --- | --- | --- | --- | --- | --- |'])
            lines.extend('| ' + ' | '.join(finding) + ' |' for finding in findings)
            if not findings: lines.extend(['', 'No review evidence is selected in the supplied Claim decisions.'])
        lines.extend(['', '## Fixed History', '', 'Retained fixed decisions keep their exact scope; history is navigation, not a new selection.', '',
                      '| Family | Material version | Decisions |', '| --- | --- | --- |'])
        for row in chosen:
            for old in row['versions']:
                refs = '; '.join(link(index, anchor, {'path': old['path'], 'anchor': anchor}) for anchor in old['decisions']) or 'None'
                label = 'v' + str(old['version'])
                lines.append('| ' + ' | '.join([cell(row['family']), link(index, label, {'path': old['path']}), refs]) + ' |')
        if outside:
            lines.extend(['', '## Unacquired Source Inputs', '', '| Family | Role | Original input | Scope |', '| --- | --- | --- | --- |'])
            for family, role, loc, scope in outside:
                lines.append('| ' + ' | '.join([cell(family), cell(role), link(index, 'Original source', vars(loc)), cell(scope)]) + ' |')
        output[index] = '\n'.join(lines) + '\n'
    return output
