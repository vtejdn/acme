"""Explicit review input and target structure for newly authored decisions.

These bindings express an author's review-scope assertion. They neither infer a
verdict from prose nor rejudge the mathematics of an existing historical review.
"""
from . import documents as documents
from . import navigation as navigation
from ..core import links as links
from ..core import paths as storage_paths
from pathlib import PurePosixPath

require = documents.require


def _selected_label(review, label, finding):
    """Locate only an explicit selected link before validating its whole cell."""
    parsed = documents.SIMPLE_LINK.match(label.strip())
    if parsed is not None:
        try:
            target = links.destination(review.path, parsed[2])
        except ValueError:
            # An invalid unrelated path supplies no selected finding locator.
            return False
        if target == (finding.path, finding.anchor):
            return True
    return False


def _rows(review, heading, columns, finding):
    if finding is None:
        return navigation.table(review, heading, columns, with_lines=True)
    sections = documents.MarkdownInput(review.text.replace('\r\n', '\n')).sections(heading)
    require(len(sections) <= 1, 'Repeated navigation section: ' + heading)
    if not sections:
        return []
    content, first_line = sections[0]

    def selected_row(line, mask):
        pipes = links.table_pipes(mask)
        label = line[pipes[0] + 1:pipes[1] if len(pipes) > 1 else len(line)]
        return _selected_label(review, label, finding)

    tables = list(content.tables(select_row=selected_row))
    require(len(tables) <= 1, 'Expected one contiguous material table. Section: ' + heading)
    if not tables:
        return []
    header, rows = tables[0]
    require(header == list(columns), 'Unexpected material table header. Section: ' + heading)
    result, seen = [], set()
    for cells, number in rows:
        if not cells or not _selected_label(review, cells[0], finding):
            continue
        require(len(cells) == len(columns) and all(cells), 'Material relationships need all declared fields.')
        require(tuple(cells) not in seen, 'Repeated material relationship.')
        seen.add(tuple(cells))
        result.append((cells, first_line + number))
    return result


def binding_at(review, offset):
    """Identify the actual target cell, not another link to the same address."""
    text = links.declaration_markdown(review.text, preserve_offsets=True)
    start = text.rfind('\n', 0, offset) + 1
    end = text.find('\n', offset)
    line = text[start:end if end >= 0 else len(text)]
    pipes = links.table_pipes(line)
    if len(pipes) != 4 or not start + pipes[1] + 1 <= offset < start + pipes[2]:
        return None
    # Offset masks locate cells only. Evidence text comes from the same parsed
    # binding as ordinary review coverage, including comment/pipe semantics.
    line_number = text[:start].count('\n')
    for (finding, target, scope), number in bindings(review, with_lines=True):
        if number == line_number:
            return finding, {'path': target.path, 'anchor': target.anchor, 'scope': scope}
    return None


def bindings(review, *, with_lines=False, finding=None, validate_anchors=True):
    require(review.identity.kind in 'RL', 'Review bindings belong to fixed R/L material.')
    relationships(review, finding=finding, validate_anchors=validate_anchors)
    result = []
    for (label, target, scope), number in _rows(review, 'Review bindings', ('Review', 'Target', 'Scope'), finding):
        selected = documents.locator(review.path, label)
        if finding is not None and selected != finding: continue
        require(selected.path == review.path, 'A review binding must belong to its own fixed R/L material.')
        require(not validate_anchors or not selected.anchor or links.anchor_occurrences(review.text)[selected.anchor] == 1,
                'Review binding names a missing finding anchor.')
        binding = (selected, documents.locator(review.path, target), scope)
        result.append((binding, number) if with_lines else binding)
    return result


def relationships(review, *, finding=None, validate_anchors=True):
    """Explicit finding facts; consumer assessments never classify findings."""
    result = {}
    for (label, relationship), _number in _rows(review, 'Review relationships', ('Review', 'Relationship'), finding):
        loc = documents.locator(review.path, label)
        if finding is not None and loc != finding: continue
        require(loc.path == review.path and (not validate_anchors or links.anchor_occurrences(review.text)[loc.anchor] == 1),
                'Review relationship needs an actual local finding anchor.')
        require(relationship in {'self-reviewed', 'independently reviewed', 'unknown'},
                'Unknown finding review relationship.')
        require(loc not in result, 'Duplicate finding review relationship.')
        result[loc] = relationship
    return result


def check_findings(review, *, previous=None, read=None, finding=None):
    """Require declarations for new/changed explicit finding scopes only.

    Bindings, relationship rows and an explicit selected locator identify the
    declaration scope. Plain prose does not identify an inspection or establish
    whether its mathematics changed.
    """
    require(review.identity.kind == 'R', 'Formal project findings belong to fixed R material.')

    def declared(document, *, selected=None, validate_anchors=True):
        relations = relationships(document, finding=selected, validate_anchors=validate_anchors)
        by_anchor = {loc.anchor: value for loc, value in relations.items()}
        scopes = {}
        bound = bindings(document, finding=selected, validate_anchors=validate_anchors)
        for loc, target, scope in bound:
            scopes.setdefault(loc.anchor, set()).add((target.path, target.anchor, scope))
        if selected is not None and links.anchor_occurrences(document.text)[selected.anchor] == 1:
            scopes.setdefault(selected.anchor, set())
        return relations, bound, {anchor: (by_anchor.get(anchor), frozenset(scopes.get(anchor, ())))
                                  for anchor in scopes.keys() | by_anchor.keys()}

    relations, bound, current = declared(review, selected=finding)
    # A new address can retain an old performed review. Only actual declared
    # finding scopes are structural inputs; file addition dates no inspection.
    # The preimage supplies declaration scope, not a fresh locator validation.
    # Otherwise repairing an old duplicate anchor would be blocked by that old
    # defect even though the postimage passed the strict shared readers above.
    earlier = []
    inputs = documents.revision_inputs(review, read) if read is not None and review.identity.source_repository else []
    for entry in inputs:
        # Only the agent's explicit fixed input and selected scope supply prior
        # declarations. An unrelated old finding is not an input for this use.
        if finding is not None and entry['anchor'] not in ('', finding.anchor):
            continue
        raw = read(entry['path'])
        document = documents.parse(entry['path'], raw.decode('utf-8-sig') if isinstance(raw, bytes) else raw)
        anchor = finding.anchor if finding is not None else entry['anchor']
        selected = documents.Locator(document.path, anchor) if anchor else None
        earlier.append(declared(document, selected=selected)[2])
    if not inputs and previous is not None:
        selected = documents.Locator(previous.path, finding.anchor) if finding is not None else None
        earlier.append(declared(previous, selected=selected, validate_anchors=False)[2])
    for anchor, scope in current.items():
        if not any(scope == old.get(anchor) for old in earlier):
            selected = documents.Locator(review.path, anchor)
            # Both retained and changed declarations use one target per row;
            # declaration equality does not judge mathematical reuse.
            bindings(review, finding=selected)
            require(selected in relationships(review, finding=selected),
                    'New or revised finding needs an explicit review relationship: ' + review.path + '#' + anchor)
    return relations, bound


def original_locator(loc, read, origins=(), *, repo=None):
    """Keep physical targets unless actual acquisition supplies correspondence."""
    if storage_paths.in_computation_outputs(loc.path):
        # Output locators never inherit the program README's acquired origin.
        # Local output facts remain separate from acquired fixed program files.
        return None, loc.path, loc.anchor
    recorded = [row['origin'] for row in origins if row['target'] == loc.path]
    require(not recorded or all(row == recorded[0] for row in recorded), 'Conflicting original input identity.')
    origin = recorded[0] if recorded else None
    owner = loc.path
    ident = documents.identity.parse(loc.path)
    if ident.source_repository is None and origin is None:
        # A local material keeps its exact local path identity. Imported
        # originals require an external prefix and actual source headers.
        return None, loc.path, loc.anchor
    if ident.kind == 'J':
        parts = PurePosixPath(loc.path).parts
        owner = '/'.join(parts[:parts.index(ident.name) + 1]) + '/readme.md'
        if origin and owner != loc.path and PurePosixPath(origin['source_material']).name == 'readme.md':
            origin = {**origin, 'source_material': (PurePosixPath(origin['source_material']).parent /
                      PurePosixPath(loc.path).relative_to(PurePosixPath(owner).parent)).as_posix()}
    try:
        raw = read(owner)
        doc = documents.parse(owner, raw.decode('utf-8-sig') if isinstance(raw, bytes) else raw)
    except FileNotFoundError:
        require(origin is not None, 'Missing original-identity evidence: ' + loc.path)
    else:
        actual = (doc.header['source_repository'], doc.header.get('source_material', loc.path)) if doc.identity.source_repository else (None, loc.path)
        if doc.identity.source_repository and owner != loc.path:
            actual = (actual[0], (PurePosixPath(actual[1]).parent / PurePosixPath(loc.path).relative_to(PurePosixPath(owner).parent)).as_posix())
        require(origin is None or actual == (origin['source_repository'], origin['source_material']), 'Conflicting original input identity.')
        if not doc.identity.source_repository:
            return None, loc.path, loc.anchor
        if repo is not None:
            from ..intake.acquire import material_info
            info = material_info(repo, doc, read=read)
            if info.get('inputs'):
                return None, loc.path, loc.anchor
            # An acquired container does not supply correspondence for every
            # possible anchor or constituent. Use only its recorded exact scope.
            originals = {(row['source']['repository'], row['source']['path'],
                          row['source'].get('anchor', '') or loc.anchor)
                         for row in info['acquisitions']
                         if row['local']['path'] == loc.path
                         and (row['local'].get('anchor', '') == loc.anchor
                              or not row['local'].get('anchor') and not row['source'].get('anchor'))}
            require(len(originals) <= 1, 'Conflicting original input scope: ' + loc.path)
            if originals:
                return next(iter(originals))
        elif origin is not None and not documents.revision_inputs(doc, read):
            return (*actual, loc.anchor)
        return None, loc.path, loc.anchor
    return origin['source_repository'], origin['source_material'], loc.anchor


def check_decision(owner, decision, read, *, repo=None):
    """Check selected R bindings name the declared accepted inputs.

Call only for newly authored decisions. Old adopted decisions keep their actual
historical evidence; this function does not fabricate retrospective bindings.
"""
    kind, status = owner.identity.kind, decision.fields['status']
    accepted = (kind == 'T' and status == 'completed') or (
        kind == 'C' and status.startswith(('proved', 'refuted')))
    if not accepted:
        return
    needed_roles = {'contract', 'support', 'dependency'} if kind == 'T' else {'statement', 'argument'}
    needed = {original_locator(loc, read, repo=repo) for role, loc, _ in decision.relations if role in needed_roles}
    selected = [loc for role, loc, _ in decision.relations if role == 'review']
    require(needed and selected, 'An accepted decision needs its explicit inputs and adopted review.')
    covered, loaded, unavailable = set(), {}, False
    for loc in selected:
        if loc.path not in loaded:
            loaded[loc.path] = documents.parse(loc.path, read(loc.path))
        review = loaded[loc.path]
        require(review.identity.kind == 'R', 'New local formal review evidence must belong to fixed R material.')
        require(not loc.anchor or links.anchor_occurrences(review.text)[loc.anchor] == 1,
                'Selected review anchor is missing: ' + loc.path + '#' + loc.anchor)
        declared = relationships(review, finding=loc)
        require(loc in declared, 'Selected finding needs an explicit review relationship: ' + loc.path + '#' + loc.anchor)
        if review.identity.source_repository:
            if repo is None:
                unavailable = True
                targets = set()
            else:
                from ..intake.acquire import finding_evidence
                _relationship, available = finding_evidence(repo, loc)
                targets = {documents.Locator(path, anchor) for path, anchor in available}
        else:
            targets = {target for finding, target, _scope in bindings(review, finding=loc) if finding == loc}
        for target in targets:
            covered.add(original_locator(target, read, repo=repo))
    missing = sorted(needed - covered, key=str)
    require(not missing, 'Selected review bindings do not cover the exact new accepted inputs: ' +
            ', '.join(str(item) for item in missing) + '; selected findings: ' +
            ', '.join(loc.path + '#' + loc.anchor for loc in selected) +
            ('; required acquired review inputs are unavailable.' if unavailable else ''))
