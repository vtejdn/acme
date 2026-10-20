"""Explicit review input and target structure for newly authored decisions.

These bindings express an author's review-scope assertion. They neither infer a
verdict from prose nor rejudge the mathematics of an existing historical review.
"""
from . import documents as documents
from . import navigation as navigation
from ..core import links as links
from ..core import paths as storage_paths
from pathlib import PurePosixPath
import re

require = documents.require


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


def bindings(review, *, with_lines=False, legacy=False):
    require(review.identity.kind in 'RL', 'Review bindings belong to fixed R/L material.')
    relationships(review, legacy=legacy)
    result = []
    for (finding, target, scope), number in navigation.table(review, 'Review bindings', ('Review', 'Target', 'Scope'), with_lines=True):
        selected = documents.locator(review.path, finding)
        require(selected.path == review.path, 'A review binding must belong to its own fixed R/L material.')
        require(not selected.anchor or selected.anchor in links.anchors_text(review.text),
                'Review binding names a missing finding anchor.')
        targets = [target]
        if legacy:
            explicit = re.findall(r'\[[^\]\n]+\]\([^\)\n]+\)', target)
            if len(explicit) > 1 and re.sub(r'\[[^\]\n]+\]\([^\)\n]+\)', '', target).strip() == 'and':
                targets = explicit
        for value in targets:
            binding = (selected, documents.locator(review.path, value), scope)
            result.append((binding, number) if with_lines else binding)
    return result


def relationships(review, *, legacy=False):
    """Explicit finding facts; consumer assessments never classify findings."""
    result = {}
    for finding, relationship in navigation.table(review, 'Review relationships', ('Review', 'Relationship')):
        loc = documents.locator(review.path, finding)
        require(loc.path == review.path and loc.anchor in links.anchors_text(review.text),
                'Review relationship needs an actual local finding anchor.')
        require(relationship in {'self-reviewed', 'independently reviewed', 'unknown'},
                'Unknown finding review relationship.')
        require(legacy or relationship != 'independently reviewed' or review.identity.kind == 'R',
                'An independently reviewed finding must belong to fixed R material.')
        require(loc not in result, 'Duplicate finding review relationship.')
        result[loc] = relationship
    return result


def original_locator(loc, read, origins=()):
    """Compare exact originals, never display names or author spelling alone."""
    if storage_paths.in_computation_outputs(loc.path):
        # Output locators never inherit the program README's acquired origin.
        # Actual attachment provenance is supplied in its intake operation.
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
        actual = (doc.header['source_repository'], doc.header['source_material']) if doc.identity.source_repository else (None, loc.path)
        if doc.identity.source_repository and owner != loc.path:
            actual = (actual[0], (PurePosixPath(actual[1]).parent / PurePosixPath(loc.path).relative_to(PurePosixPath(owner).parent)).as_posix())
        require(origin is None or actual == (origin['source_repository'], origin['source_material']), 'Conflicting original input identity.')
        return (*actual, loc.anchor)
    return origin['source_repository'], origin['source_material'], loc.anchor


def role_maintenance(owner, decision, previous, read_previous):
    """Compare role actions to the actual prior selection, without judging prose."""
    if (owner.identity.kind != 'C' or previous is None or previous.current is None
            or owner.path != previous.path):
        return False
    _material, selected = documents.selection(previous, read_previous)
    metadata = {'role', 'date', 'reason', 'authority'}
    fields = lambda item: {key: value for key, value in item.fields.items() if key not in metadata}
    relations = lambda item: {(role, loc.path, loc.anchor, scope) for role, loc, scope in item.relations}
    # Several role actions can cancel within one selected Git diff. Their net
    # role need not differ from that view's baseline; no assessment/input changed.
    return fields(decision) == fields(selected) and relations(decision) == relations(selected)


def check_decision(owner, decision, read, *, repo=None,
                   previous=None, previous_read=None):
    """Check selected R/L bindings name the declared accepted inputs.

Call only for newly authored decisions. Old adopted decisions keep their actual
historical evidence; this function does not fabricate retrospective bindings.
"""
    kind, status = owner.identity.kind, decision.fields['status']
    accepted = (kind == 'T' and status == 'completed') or (
        kind == 'C' and status.startswith(('proved', 'refuted')))
    if not accepted or role_maintenance(owner, decision, previous, previous_read or read):
        return
    needed_roles = {'contract', 'support', 'dependency'} if kind == 'T' else {'statement', 'argument'}
    needed = {original_locator(loc, read) for role, loc, _ in decision.relations if role in needed_roles}
    selected = [loc for role, loc, _ in decision.relations if role == 'review']
    independent = decision.fields.get('review-status') == 'independently reviewed'
    require(needed and selected, 'An accepted decision needs its explicit inputs and adopted review.')
    covered, loaded, unavailable, inconsistent = set(), {}, False, []
    for loc in selected:
        if loc.path not in loaded:
            loaded[loc.path] = documents.parse(loc.path, read(loc.path))
        review = loaded[loc.path]
        require(not loc.anchor or loc.anchor in links.anchors_text(review.text),
                'Selected review anchor is missing: ' + loc.path + '#' + loc.anchor)
        relationship = relationships(review).get(loc, 'unknown')
        acquired_inputs = None
        if review.identity.source_repository:
            if repo is None:
                relationship = 'unknown'
                acquired_inputs = set()
            else:
                from ..intake.acquire import finding_evidence
                relationship, acquired_inputs = finding_evidence(repo, loc)
        if independent and (review.identity.kind != 'R' or relationship != 'independently reviewed'):
            inconsistent.append(loc.path + '#' + loc.anchor + ': ' + review.identity.kind + ', ' + relationship)
            continue
        for finding, target, _scope in bindings(review):
            if finding == loc and acquired_inputs is not None and (target.path, target.anchor) not in acquired_inputs:
                unavailable = True
            elif finding == loc:
                covered.add(original_locator(target, read))
    missing = sorted(needed - covered, key=str)
    require(not missing, 'Selected review bindings do not cover the exact new accepted inputs: ' +
            ', '.join(str(item) for item in missing) + '; selected findings: ' +
            ', '.join(loc.path + '#' + loc.anchor for loc in selected) +
            ('; independent coverage needs explicitly independent fixed R findings: ' + '; '.join(inconsistent) if inconsistent else '') +
            ('; required acquired review inputs are unavailable.' if unavailable else ''))
