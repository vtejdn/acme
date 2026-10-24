"""Exclusive single-material writes without a C/T record or snapshot store.

Callers supply authored Markdown and explicit mathematical decisions. These
operations validate declared fields, registered names and locators; they do not perform a
mathematical review or infer a review's applicability from its mere existence.
"""
from dataclasses import replace
from pathlib import PurePosixPath
import posixpath
import re

from . import documents as documents
from . import discovery
from . import identity as names
from ..core import repository as shared
from ..core import identity as humans
from ..core import paths as paths

require = names.require
HOMES = {'C': 'claims', 'T': 'tasks', 'S': 'strategies', 'R': 'audits/reviews',
         'D': 'drafts', 'L': 'ledger', 'J': 'computations/programs'}


def _path(repo, value):
    require(isinstance(value, str) and value and '\\' not in value,
            'Use a repository-relative POSIX material path.')
    relative = PurePosixPath(value)
    require(relative.as_posix() == value and not relative.is_absolute()
            and '..' not in relative.parts and ':' not in value,
            'Unsafe or noncanonical material path.')
    require(relative.parts[0] == 'mathematics', 'Authored materials belong under mathematics/.')
    candidate = paths.ordinary_path(repo.root, relative)
    # Windows cannot distinguish these names, and a Linux-authored checkout must
    # not introduce a different identity when subsequently opened on Windows.
    parent = repo.root
    for part in relative.parts:
        if parent.is_dir():
            matches = [child.name for child in parent.iterdir() if child.name.casefold() == part.casefold()]
            require(not matches or matches == [part], 'Material path collision ignoring case: ' + value)
        parent /= part
    return candidate


def _read(repo, path):
    data = (shared.read_from(repo, path) if path.startswith('execution/')
            else _path(repo, path).read_bytes())
    return data.decode('utf-8-sig') if path.lower().endswith('.md') else data


def _actor(repo, author=None):
    actor = humans.actor(repo)
    author = actor if author is None else author
    require(humans.person(repo, author)['id'] == author, 'Use the registered author spelling.')
    humans.require_author(repo, author)
    return author


def _inventory(repo, **scope):
    """Read addresses only, including an existing J directory without a README."""
    found = []
    registered = {person['id'].casefold(): person['id'] for person in humans.registry(repo)['people']}
    for path in discovery.selected(discovery.candidates(repo.root, include_empty_j=True), **scope):
        _path(repo, path)
        ident = names.parse(path)
        if ident.source_repository is None:
            require(registered.get(ident.author.casefold(), ident.author) == ident.author,
                    'Existing local material has noncanonical author spelling: ' + path)
        found.append((ident, path))
    ledger = {}
    for ident, path in found:
        if ident.kind != 'L': continue
        key = (ident.family.casefold(), ident.version)
        require(key not in ledger, 'Duplicate L identity at ' + path + ' and ' + ledger.get(key, '') + '; reconcile the actual material before allocation.')
        ledger[key] = path
        require(path.startswith('mathematics/ledger/'), 'L belongs in mathematics/ledger/: ' + path)
    return found


def _owned_current(repo, path, expected_current):
    _path(repo, path)
    doc = documents.parse(path, _read(repo, path))
    require(doc.identity.kind not in 'CT' or (doc.current is not None and not getattr(doc, 'archival', False)),
            'An archival material is not a current authoring entrance.')
    humans.require_author(repo, doc.identity.author, doc.identity.source_repository)
    family = _inventory(repo, family=doc.identity)
    require(all(ident.family == doc.identity.family for ident, _ in family), 'Material family collision ignoring case.')
    if doc.identity.version is not None:
        latest = documents.current([candidate for _, candidate in family], doc.identity.family)
        require(path == latest, 'Only the current main-material entry may be changed; refresh the family entrance.')
    else:
        require(len(family) == 1, 'More than one path owns this rolling material family.')
    actual = vars(doc.current) if doc.current else None
    expected = vars(expected_current) if isinstance(expected_current, documents.Locator) else expected_current
    require(expected == actual, 'Stale expected current decision; read the current material again.')
    documents.check(doc, lambda target: _read(repo, target),
                    paths=discovery.candidates(repo.root) if doc.identity.kind in 'ST' else ())
    return doc


def _validated(repo, path, body):
    require(isinstance(body, str), 'Material body must be explicit Markdown text.')
    # New writes have a uniform newline convention; previous fixed files remain
    # untouched. Decision edits preserve existing text except the chosen section.
    doc = documents.parse(path, body)
    humans.require_author(repo, doc.identity.author, doc.identity.source_repository)
    documents.check(doc, lambda target: body if target == path else _read(repo, target),
                    paths=discovery.candidates(repo.root) if doc.identity.kind in 'ST' else ())
    return doc


def _check_new_decisions(repo, doc, anchors, *, previous=None, new_date_anchors=None):
    anchors = list(anchors)
    new_date_anchors = set(anchors if new_date_anchors is None else new_date_anchors)
    from . import review as material_review
    if doc.identity.kind == 'R':
        material_review.check_findings(doc, previous=previous, read=lambda target: _read(repo, target))
    # A canonical-looking filename is not the evidence's authorship/provenance.
    # J children locate their program entrance, including native reports without
    # individual headers. This does not attribute output bytes to its generator
    # or to the program's Git revision. Other Markdown inputs own their header.
    # Do not traverse selected decisions or rejudge historical evidence.
    loaded = {doc.path}
    for anchor in anchors:
        documents.new_decision(doc, doc.decisions[anchor])
        if anchor in new_date_anchors:
            shared.valid_stamp(doc.decisions[anchor].fields['date'])
        for role, loc, _scope in doc.decisions[anchor].relations:
            if role not in {'argument', 'support', 'dependency', 'review'}:
                continue
            ident = names.parse(loc.path)
            evidence = loc.path
            if ident.kind == 'J':
                if paths.in_computation_outputs(loc.path):
                    evidence = 'mathematics/computations/programs/' + ident.name + '/readme.md'
                else:
                    parts = PurePosixPath(loc.path).parts
                    group = parts.index(ident.name)
                    evidence = PurePosixPath(*parts[:group + 1], 'readme.md').as_posix()
            if evidence not in loaded and evidence.lower().endswith('.md'):
                documents.parse(evidence, _read(repo, evidence))
            loaded.add(evidence)
    # The explicit review bindings are a structural input/target contract,
    # never a rerun or a new mathematical verdict on existing historical data.
    accepted = [anchor for anchor in anchors if
                (doc.identity.kind == 'C' and doc.decisions[anchor].fields['status'].startswith(('proved', 'refuted')))
                or (doc.identity.kind == 'T' and doc.decisions[anchor].fields['status'] == 'completed')]
    if not accepted:
        return
    from . import runtime as runtime
    for anchor in accepted:
        read = lambda target: doc.text if target == doc.path else _read(repo, target)
        material_review.check_decision(doc, doc.decisions[anchor],
                                       read, repo=repo,
                                       previous=previous, previous_read=lambda target: _read(repo, target))
        runtime.validate_inputs(repo, replace(doc, current=documents.Locator(doc.path, anchor)), read)


def _publish(repo, path, body, *, exclusive, new_decisions=(), previous=None):
    doc = _validated(repo, path, body)
    if doc.identity.source_repository:
        from ..intake.acquire import material_info
        material_info(repo, doc, read=lambda source: body if source == path else _read(repo, source))
    if new_decisions:
        require(not getattr(doc, 'archival', False) and not getattr(doc, 'historical_assessments', {}),
                'New authoring cannot create archival material or historical-only assessments.')
        require(set(new_decisions) <= doc.decisions.keys(), 'Choose actual new decision anchors explicitly.')
        _check_new_decisions(repo, doc, new_decisions, previous=previous)
    if doc.identity.kind == 'T' and previous is not None:
        from . import tasks
        tasks.validate(doc, lambda source: body if source == path else _read(repo, source),
                       paths=discovery.candidates(repo.root), previous=[previous])
    if doc.identity.kind == 'R':
        from . import review as material_review
        material_review.check_findings(doc, previous=previous, read=lambda source: _read(repo, source))
    if doc.identity.kind in 'CT' and doc.current is not None:
        from . import runtime as runtime
        runtime.validate_inputs(repo, doc,
            lambda source: doc.text if source == doc.path else _read(repo, source))
    target = _path(repo, path)
    if doc.identity.kind == 'T' and doc.task_type == 'ordinary' and doc.identity.version == 1 and exclusive:
        from ..execution.records import address
        from ..core.publication import publish_files
        execution = address(path)
        boundary = ('# Current execution boundary\n\n| Field | Value |\n| --- | --- |\n'
                    '| task | ' + doc.current.path + '#' + doc.current.anchor + ' |\n'
                    '| state | not-running |\n\nSetup grants no execution authority or allowance.\n')
        publish_files(repo, {path: body.encode('utf8'), execution: boundary.encode('utf8')},
                      {path: None, execution: None})
        return doc
    shared.write_bytes(target, body.encode('utf-8'), exclusive=exclusive, root=repo.root)
    return doc


def _newlines(body):
    require(isinstance(body, str), 'Material body must be explicit Markdown text.')
    return body.replace('\r\n', '\n').replace('\r', '\n').rstrip('\n') + '\n'


def _task_entrance(path, body):
    from ..execution.records import address
    from ..core import links
    entrances = [target for _, _, href in links.markdown_link_spans(body)
                 if (target := links.destination(path, href)) is not None and target[0].startswith('execution/')]
    doc = documents.parse(path, body)
    if doc.task_type == 'joint':
        require(not entrances, 'A joint Task has no E link.')
        return body
    expected = address(path)
    require(not entrances or entrances == [(expected, '')], 'A Task may have one unanchored entrance to its family E.')
    return body if entrances else body.rstrip() + '\n\n## Execution boundary\n\n[Current execution boundary](../../' + expected + ').\n'


def create(repo, *, kind, body, line=None, task=None, author=None, new_decisions=()):
    """Allocate one local family and create its first authored Markdown file.

    ``body`` includes its explicit author header, title and (for C/T) decisions.
    A J creation installs its sole README; native children are separate bundle
    content, never allocated as extra mathematical identities.
    """
    actor = _actor(repo, author)
    if task is not None:
        parent = documents.parse(task, _read(repo, task))
        require(parent.identity.kind == 'T', 'The selected parent must be a Task.')
        require(kind != 'S' or parent.task_type == 'ordinary', 'Strategies belong to individual Tasks, not joint Tasks.')
        documents.check(parent, lambda target: _read(repo, target))
    sequence = names.allocate([], author=actor, kind=kind, line=line, task=task)
    with shared.locked(repo.root):
        existing = [item for item, _ in _inventory(repo, kind=kind, author=actor, line=sequence.line, local=True)]
        if kind == 'D':
            ident = names.allocate(existing, author=actor, kind=kind, line=sequence.line)
        else:
            config = shared.read_json(repo.home / 'config.json', root=repo.root)
            bound = names.allocation_bound(config, sequence, existing)
            ident = names.allocate(existing, author=actor, kind=kind, line=sequence.line, next_number=bound)
            config = names.reserve(config, ident, existing)
            shared.write_json(repo.home / 'config.json', config, root=repo.root)
            repo.config = config
    if kind in 'CTRL':
        ident = replace(ident, version=1)
    name = ident.name + ('/readme.md' if kind == 'J' else '.md')
    home = HOMES[kind]
    path = 'mathematics/' + home + '/' + name
    if kind == 'T': body = _task_entrance(path, body)
    try:
        return _publish(repo, path, _newlines(body), exclusive=True, new_decisions=new_decisions)
    except FileExistsError as error:
        raise ValueError('Material allocation collided; refresh this sequence and retry the explicit authored body.') from error


def revise(repo, path, *, body, expected_current, new_decisions=()):
    """Create the next fixed vN without rewriting any earlier mathematical file.

    A revised C/T explicitly selects a new decision bound to its new statement or
    contract. Deliberately adopting an older fixed decision is a separate
    ``select_decision`` operation, retaining that decision's historical scope.
    """
    with shared.locked(repo.root):
        old, doc = _revise(repo, path, body, expected_current, new_decisions)
    return doc


def _revise(repo, path, body, expected_current, new_decisions=()):
    body = _newlines(body)
    previous = documents.parse(path, _read(repo, path))
    old = _owned_current(repo, path, expected_current)
    require(old.identity.kind in 'CTRL', 'Only fixed C/T/R/L materials receive a new mathematical version.')
    ident = replace(old.identity, version=old.identity.version + 1)
    target = str(PurePosixPath(path).with_name(ident.name + '.md'))
    body = _newlines(body)
    if ident.kind == 'T': body = _task_entrance(target, body)
    doc = _validated(repo, target, body)
    if doc.current:
        require(doc.current.path == target and doc.current.anchor in doc.decisions,
                'A revised statement/contract needs an explicit new local decision; reopen or adopt applicable evidence.')
        decision = doc.decisions[doc.current.anchor]
        primary = 'statement' if ident.kind == 'C' else 'contract'
        require(next(loc for role, loc, _ in decision.relations if role == primary).path == target,
                'The revision decision must bind its revised statement/contract, not silently carry an old disposition.')
    doc = _publish(repo, target, body, exclusive=True, new_decisions=new_decisions, previous=old)
    return old, doc


def _section(text, name):
    """Locate visible structural lines, retaining original prose and examples."""
    lines = text.splitlines(keepends=True)
    visible = documents.links.declaration_markdown(text).splitlines(keepends=True)
    require(len(lines) == len(visible), 'Cannot safely locate material sections.')
    starts = [index for index, line in enumerate(visible)
              if re.fullmatch(r' {0,3}' + re.escape('## ' + name) + r'[ \t]*', line.rstrip('\r\n'))]
    require(len(starts) <= 1, 'Repeated section: ' + name)
    if not starts:
        return None
    start = starts[0]
    end = next((index for index in range(start + 1, len(lines)) if re.match(r'^ {0,3}#{1,2}(?:[ \t]|$)', visible[index])), len(lines))
    offsets = [0]
    for line in lines:
        offsets.append(offsets[-1] + len(line))
    return offsets[start + 1], offsets[end]


def _locator(value):
    if isinstance(value, documents.Locator):
        return value
    require(isinstance(value, dict) and set(value) == {'path', 'anchor'}, 'Supply an exact {path, anchor} decision locator.')
    require(all(isinstance(value[key], str) and value[key] for key in value), 'Decision locators need path and anchor.')
    return documents.Locator(**value)


def _select_text(doc, target):
    target = _locator(target)
    name = 'Current assessment' if doc.identity.kind == 'C' else 'Current decision'
    start, end = _section(doc.text, name)
    relative = '' if target.path == doc.path else posixpath.relpath(target.path, posixpath.dirname(doc.path))
    require(not any(char in relative + target.anchor for char in '\r\n()'), 'Unsafe decision locator.')
    return doc.text[:start] + '[Selected decision](' + relative + '#' + target.anchor + ')\n\n' + doc.text[end:]


def append_decision(repo, path, *, decision, expected_current, select=True):
    """Append one explicit decision, preserving all preceding sections verbatim."""
    with shared.locked(repo.root):
        return _append_decision(repo, path, decision, expected_current, select)


def _append_decision(repo, path, decision, expected_current, select):
    doc = _owned_current(repo, path, expected_current)
    require(doc.identity.kind in 'CT', 'Only Claims and Tasks own decision histories.')
    decision = _newlines(decision)
    require(re.match(r'\A### Decision [A-Za-z0-9-]+\n', decision), 'Provide one explicit Decision section.')
    require(not re.search(r'^ {0,3}#{1,2}(?:[ \t]|$)', documents.links.declaration_markdown(decision), re.M),
            'Decision input cannot replace material sections.')
    sentinel = '## Material write boundary\n'
    require(documents.links.declaration_markdown(decision + '\n\n' + sentinel).endswith(sentinel),
            'Close decision literal regions and comments before appending; preserve following material prose.')
    name = 'Assessment history' if doc.identity.kind == 'C' else 'Lifecycle and completion'
    section = _section(doc.text, name)
    if section is None:
        body = doc.text + '\n## ' + name + '\n\n' + decision
    else:
        end = section[1]
        body = doc.text[:end] + '\n' + decision + '\n' + doc.text[end:]
    proposed = _validated(repo, path, body)
    added = proposed.decisions.keys() - doc.decisions.keys()
    require(len(added) == 1 and len(proposed.decisions) == len(doc.decisions) + 1,
            'Append exactly one new decision without replacing a historical decision.')
    _check_new_decisions(repo, proposed, added, previous=doc)
    if select:
        body = _select_text(proposed, documents.Locator(path, next(iter(added))))
    return _publish(repo, path, body, exclusive=False)


def select_decision(repo, path, *, target, expected_current):
    """Explicitly adopt one fixed same-family decision, including an older one."""
    with shared.locked(repo.root):
        doc = _owned_current(repo, path, expected_current)
        require(doc.identity.kind in 'CT', 'Only Claims and Tasks select decisions.')
        target = _locator(target)
        _path(repo, target.path)
        body = _select_text(doc, target)
        proposed = documents.parse(path, body)
        owner, chosen = documents.selection(proposed, lambda name: _read(repo, name))
        documents.new_decision(owner, chosen)
        return _publish(repo, path, body, exclusive=False)
