"""Derived material-family discovery; no independent record or pointer store."""
from pathlib import PurePosixPath
import os

from . import documents as documents
from . import identity as identity
from ..core import paths as paths
from ..core import source_refs

require = identity.require


def unit_origin(ident, header):
    """Actual original family, independent of its recipient spelling/version."""
    if ident.source_repository:
        return header['source_repository'], identity.parse(header['source_material']).family
    return None, ident.family


def unit_positions(paths_to_read, read):
    """Check source-key positions and original-family continuity in this scope."""
    positions, correspondence, versions = {}, {}, {}
    for path in paths_to_read:
        ident = identity.parse(path)
        if ident.kind != 'U': continue
        ident, header, _ = documents.author_header(path, read(path))
        position, origin = (ident.source_key, ident.number), unit_origin(ident, header)
        require(position not in positions or positions[position] == origin,
                'Conflicting local U position: '+ident.unit+'; choose a free position for the different original family.')
        family = ident.source_key, origin
        require(family not in correspondence or correspondence[family] == ident.number,
                'Original U family has conflicting local positions: '+ident.source_key)
        version = position, ident.version
        require(version not in versions or versions[version] == path,
                'Multiple entrances own the same local U version: '+ident.unit)
        positions[position] = origin
        correspondence[family] = ident.number
        versions[version] = path
    return positions, correspondence


def unit_header(root, path):
    """Read only the physical identity header of a namespace sibling."""
    with paths.ordinary_path(root,path).open(encoding='utf-8-sig',newline='') as stream:
        lines = [stream.readline()]
        for line in stream:
            lines.append(line)
            if line.strip() == '---': break
    return ''.join(lines)


def candidates(root, *, include_empty_j=False):
    """Enumerate possible entrances without validating unrelated namespaces."""
    base = paths.ordinary_path(root, 'mathematics')
    result = set()
    if not base.exists():
        return result
    def failed(error):
        raise ValueError('Cannot enumerate material entrances: ' + str(error)) from error
    for directory, children, files in os.walk(base, followlinks=False, onerror=failed):
        relative = PurePosixPath(os.path.relpath(directory, root).replace(os.sep, '/'))
        children[:] = [name for name in children if name.casefold() not in paths.EXCLUDED
                       and not paths.in_pdf_store(relative / name)
                       and not paths.in_computation_outputs(relative / name)]
        for name in files + (children if include_empty_j else []):
            path = (relative / name).as_posix()
            item = identity.candidate(path)
            if item is None: continue
            if name in children:
                if item['kind'] != 'J': continue
                path += '/readme.md'
            elif not name.lower().endswith('.md'):
                continue
            if item['kind'] == 'J' and PurePosixPath(path).name != 'readme.md': continue
            result.add(path)
    return sorted(result)


def selected(candidates, **scope):
    return [path for path in candidates if identity.in_namespace(path, **scope)]


def inventory(root, kind=None):
    """Strict discovery of the requested kind, or the explicit complete scope."""
    require(kind is None or kind in set('CTSRDJLU'), 'Unknown material kind.')
    result, spellings = [], {}
    for path in selected(candidates(root), kind=kind):
        identity.parse(path)
        paths.ordinary_path(root, path)
        require(spellings.get(path.casefold(), path) == path, 'Material path collision ignoring case.')
        spellings[path.casefold()] = path
        result.append(path)
    return result


def families(paths_to_read, read, *, source_info=None):
    """Derive family entrances and the status of their exact selected decisions."""
    paths_to_read = list(paths_to_read)
    unit_positions(paths_to_read, read)
    grouped, spellings = {}, {}
    for path in paths_to_read:
        doc = documents.parse(path, read(path))
        family = doc.identity.family
        require(spellings.get(family.casefold(), family) == family, 'Family spelling collision.')
        spellings[family.casefold()] = family
        grouped.setdefault(family, []).append(doc)
    result = []
    for family, entries in sorted(grouped.items()):
        require(len({documents.original_family(doc) for doc in entries}) == 1, 'Conflicting original families.')
        revisions = [doc.identity.version for doc in entries]
        require(len(set(revisions)) == len(revisions), 'Multiple entrances own the same version: ' + family)
        ordered = sorted(entries, key=lambda doc: doc.identity.version or 0)
        entry = ordered[-1]
        if entry.identity.kind == 'T':
            from . import tasks
            tasks.validate(entry, read, previous=ordered[:-1])
        selected = None
        if entry.current:
            try:
                selected = documents.selection(entry, read, source_info=source_info)[1]
            except FileNotFoundError:
                require(bool(entry.identity.source_repository) and source_refs.external(entry.current.path),
                        'Missing selected local decision.')
        row = {'family': family, 'path': entry.path, 'title': entry.title, 'author': entry.identity.author,
               'kind': entry.identity.kind, 'source_repository': entry.identity.source_repository,
               'selected_decision': vars(entry.current) if entry.current else None,
               'status': selected.fields['status'] if selected else None,
               'versions': [{'path': doc.path, 'version': doc.identity.version, 'decisions': list(doc.decisions)} for doc in ordered]}
        if entry.identity.source_repository:
            row['acquisition'] = source_info(entry) if source_info else {'origin': entry.header}
        if entry.identity.kind == 'U':
            row.update(unit=entry.identity.unit, source_inspection=documents.source_unit_scope(entry))
        if entry.identity.kind == 'T':
            row.update(task_type=entry.task_type,
                       joint_task=vars(entry.joint_task) if entry.joint_task else None)
        result.append(row)
    return result
