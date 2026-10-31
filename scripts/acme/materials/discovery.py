"""Derived material-family discovery; no independent record or pointer store."""
from pathlib import Path, PurePosixPath
import os

from . import documents as documents
from . import identity as identity
from ..core import paths as paths
from ..core import source_refs

require = identity.require


def unit_origin(ident, header):
    """Actual original unit, independent of its receiving spelling."""
    if ident.source_repository:
        return header['source_repository'], header['source_material']
    return None, ident.family


def unit_positions(paths_to_read, read):
    """Check explicitly selected author namespaces and original correspondence."""
    positions, correspondence, spellings = {}, {}, {}
    for path in paths_to_read:
        ident = identity.parse(path)
        if ident.kind != 'U': continue
        ident, header, _ = documents.author_header(path, read(path))
        namespace = identity.namespace(ident)
        require(spellings.get(namespace.casefold(), namespace) == namespace,
                'Conflicting local U namespace spelling: ' + namespace)
        spellings[namespace.casefold()] = namespace
        position, origin = (identity.namespace(ident), ident.number), unit_origin(ident, header)
        require(position not in positions or positions[position] == origin,
                'Conflicting local U position: '+ident.unit+'; choose a free position for the different original family.')
        family = identity.namespace(ident), origin
        require(family not in correspondence or correspondence[family] == ident.number,
                'Original U family has conflicting local positions: '+ident.source_key)
        positions[position] = origin
        correspondence[family] = ident.number
    return positions, correspondence


def unit_header(root, path):
    """Read only the physical identity header of a namespace sibling."""
    with paths.ordinary_path(root,path).open('rb') as stream:
        return documents.header_stream(stream)


def unit_namespace(path, ident):
    """Select the actual source/author/origin before any sibling body read."""
    item = identity.candidate(path)
    return (item is not None and item['kind'] == 'U'
            and item['source_key'].casefold() == ident.source_key.casefold()
            and item['author'].casefold() == ident.author.casefold()
            and (item['origin'] or '').casefold() == (ident.source_repository or '').casefold())


def candidates(root, *, include_empty_j=False):
    """Enumerate possible entrances without validating unrelated namespaces."""
    base = paths.ordinary_path(root, 'mathematics')
    result = set()
    if not base.exists():
        return result
    def failed(error):
        raise ValueError('Cannot enumerate material entrances: ' + str(error)) from error
    pending = [base]
    while pending:
        directory = pending.pop()
        relative = PurePosixPath(os.path.relpath(directory, root).replace(os.sep, '/'))
        try:
            with os.scandir(directory) as entries:
                for entry in entries:
                    name, target = entry.name, relative / entry.name
                    # Classify before even asking whether a private path
                    # is a file or a directory. os.walk classifies too early.
                    if (name.casefold() in paths.EXCLUDED or paths.private_file(target)
                            or paths.in_pdf_store(target) or paths.in_computation_outputs(target)):
                        continue
                    if paths.is_reparse(Path(entry.path)):
                        continue
                    directory_entry = entry.is_dir()
                    if directory_entry:
                        pending.append(entry.path)
                        if not include_empty_j: continue
                    path = target.as_posix()
                    item = identity.candidate(path)
                    if item is None: continue
                    if directory_entry:
                        if item['kind'] != 'J': continue
                        path += '/readme.md'
                    elif not name.lower().endswith('.md'):
                        continue
                    if item['kind'] == 'J' and PurePosixPath(path).name != 'readme.md': continue
                    result.add(path)
        except OSError as error:
            failed(error)
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
            row.pop('versions')
            row.update(unit=entry.identity.unit)
        if entry.identity.kind == 'T':
            row.update(task_type=entry.task_type,
                       joint_task=vars(entry.joint_task) if entry.joint_task else None)
        result.append(row)
    return result
