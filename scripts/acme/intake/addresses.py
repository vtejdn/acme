"""Exact bibliography keys, prepared local text and explicit reversible file moves.

Original source and transport locators remain provenance.
Prepare choices outside publication; the caller holds the existing shared lock
while this interface checks current inputs and publishes its selected plan.
"""
from pathlib import Path, PurePosixPath
import copy
import json
from ..core import repository as r, paths, links
from . import bibliography as bib

TEXT = {'.md', '.tex', '.bib', '.json'}


def rename_keys(text, mapping):
    """Change complete parsed keys and the defined single-key reference fields."""
    spans = []
    entries = bib.parse(text, spans=spans)
    edits = []
    for key, field, start, end in spans:
        if field is None:
            old = key
        elif field in {'crossref', 'xref'}:
            old = entries[key].fields[field]
        else:
            continue
        new = mapping.get(old, old)
        if new != old:
            edits.append((start, end, new if field is None else '{'+new+'}'))
    for start, end, value in reversed(edits): text = text[:start]+value+text[end:]
    bib.parse(text)
    return text


def _location(root, name):
    r.require(isinstance(name, str) and PurePosixPath(name).as_posix() == name,
              'Use an exact repository-relative POSIX file path: '+repr(name))
    if paths.in_pdf_store(Path(name)):
        return paths.source_path(root, name)
    return r.safe_path(root, name)


def prepared_text(raw, choice):
    r.require(isinstance(choice, dict) and set(choice) in ({'edits'}, {'expected','text'}),
              'Maintenance needs expected-text edits or expected original text with prepared final text.')
    return links.edit_text(raw, choice)


def plan(root, *, files=(), moves=None, updates=None):
    root = Path(root).resolve()
    moves, updates = moves or {}, updates or {}
    files = tuple(dict.fromkeys((*files, *moves, *updates)))
    changes, relocations = {}, {}
    for name in files:
        file = _location(root, name)
        r.require(file.is_file(), 'Selected file is unavailable: '+name)
        if name in moves or name in updates:
            from ..materials import identity, documents
            from ..core import identity as humans
            try:
                candidate = identity.parse(name)
            except ValueError:
                candidate = None
            if candidate:
                entrance = name
                if candidate.kind == 'J':
                    parts = PurePosixPath(name).parts
                    entrance = PurePosixPath(*parts[:parts.index(candidate.name) + 1], 'readme.md').as_posix()
                ident, _header, _body = documents.author_header(entrance, _location(root, entrance).read_text(encoding='utf-8-sig'))
                humans.require_author(r.Repository(root), ident.author, ident.source_repository)
        if name in moves:
            destination = _location(root, moves[name])
            r.require(paths.in_pdf_store(Path(name)) == paths.in_pdf_store(Path(moves[name])),
                      'A source-store move must keep both exact paths in source storage.')
            if destination != file: relocations[file] = destination
        if name in updates:
            r.require(file.suffix.lower() in TEXT and not paths.in_pdf_store(Path(name)),
                      'Prepared text updates require a selected local text or operation file.')
            before = file.read_bytes()
            original = before.decode('utf-8-sig')
            after = prepared_text(original, updates[name])
            if after != original: changes[file] = after.encode('utf8')
    destinations = set()
    for source, destination in relocations.items():
        folded = str(destination).casefold()
        r.require(folded not in destinations, 'Two artifacts would acquire the same address: '+str(destination))
        destinations.add(folded)
        r.require(not destination.exists() or destination in relocations,
                  'A destination is already occupied: '+str(destination))
    return changes, relocations


def _provenance(value):
    """Exclude only existing local correspondence fields, without changing JSON."""
    original = copy.deepcopy(value)
    for item in original['items']:
        for field in ('path','anchor'): item['local'].pop(field, None)
        for group in ('files','source_artifacts'):
            for pair in item.get(group, []): pair.pop('local', None)
    return original


def _check_operations(root, files, changes, moves):
    from . import acquire
    repo = r.Repository(root)
    destinations = {destination:source for source,destination in moves.items()}
    def read(name):
        target = _location(root, name)
        if target in destinations: source = destinations[target]
        else:
            if target in moves: raise FileNotFoundError('Selected local path was moved: '+name)
            source = target
        return changes[source] if source in changes else source.read_bytes()
    check_unit_layout(root,changes,moves,read)
    for name in files:
        if not (name.startswith('intake/') and name.endswith('.json')): continue
        source = _location(root, name)
        before = json.loads(source.read_bytes())
        after = json.loads(changes.get(source, source.read_bytes()))
        r.require(_provenance(before) == _provenance(after),
                  'Prepared operation must preserve original/transport facts, scope, availability and unselected content.')
        selected = [new for old,new in zip(before['items'], after['items'])
                    if old != new or _location(root,old['local']['path']) in moves
                    or _location(root,old['local']['path']) in changes]
        if selected:
            destination = moves.get(source, source).relative_to(root).as_posix()
            acquire.validate_operation(repo, destination, {**after,'items':selected}, read=read)


def check_unit_layout(root, changes, moves, read):
    """Validate the affected final U namespaces, including unmoved siblings."""
    from ..materials import discovery, identity
    affected = set()
    for path in set(changes) | set(moves) | set(moves.values()):
        # Explicit source-store moves resolve through the permitted external
        # mount; they do not occupy a local U namespace.
        if not path.is_relative_to(root): continue
        name = path.relative_to(root).as_posix()
        candidate = identity.candidate(name)
        if candidate and candidate['kind'] == 'U': affected.add(PurePosixPath(name).parent)
    final = set()
    for folder in affected:
        directory = _location(root,folder.as_posix())
        if directory.exists():
            final.update(path for path in directory.iterdir() if path.is_file() and identity.candidate(path.relative_to(root).as_posix()))
    final.difference_update(moves)
    final.update(destination for destination in moves.values() if destination.is_relative_to(root)
                 and PurePosixPath(destination.relative_to(root).as_posix()).parent in affected)
    def header(name):
        file = _location(root,name)
        if file in changes or file in moves.values():
            return read(name).decode('utf-8-sig')
        return discovery.unit_header(root,name)
    discovery.unit_positions(sorted(path.relative_to(root).as_posix() for path in final),header)


def publish(changes, moves):
    """Publish the selected plan exclusively and roll back only our own writes."""
    before = {path:path.read_bytes() for path in changes}
    staged, installed, written = {}, [], []
    import uuid
    try:
        for source in moves:
            temporary = source.with_name('.rename-'+uuid.uuid4().hex)
            source.rename(temporary); staged[source] = temporary
        for source,destination in moves.items():
            r.write_bytes(destination, staged[source].read_bytes(), exclusive=True)
            installed.append(source)
        for source,raw in changes.items():
            r.write_bytes(moves.get(source,source), raw); written.append(source)
    except BaseException:
        for source in reversed(written):
            if source not in moves: r.write_bytes(source,before[source])
        for source in reversed(installed): moves[source].unlink()
        for source,temporary in staged.items():
            if temporary.exists(): temporary.rename(source)
        raise
    for temporary in staged.values(): temporary.unlink()
    for directory in sorted({source.parent for source in moves},key=lambda path:len(path.parts),reverse=True):
        if directory.exists() and not any(directory.iterdir()): directory.rmdir()
    return {'rewritten':len(changes),'relocated':len(moves)}


def _reserve_unit_moves(root, changes, moves, key_mapping):
    """Reserve U positions and carry bounds of explicitly mapped key corrections."""
    from ..materials import identity, discovery, documents
    selected, retiring = [], []
    for source, destination in moves.items():
        if not source.is_relative_to(root) or not destination.is_relative_to(root): continue
        old_name, new_name = source.relative_to(root).as_posix(), destination.relative_to(root).as_posix()
        old_candidate, new_candidate = identity.candidate(old_name), identity.candidate(new_name)
        if not old_candidate or old_candidate['kind'] != 'U' or not new_candidate or new_candidate['kind'] != 'U': continue
        old, new = identity.parse(old_name), identity.parse(new_name)
        retiring.append(old)
        if (identity.namespace(old), old.number) == (identity.namespace(new), new.number): continue
        same_unit = (key_mapping.get(old.source_key) == new.source_key
                     and (old.author, old.source_repository, old.number, old.version) ==
                         (new.author, new.source_repository, new.number, new.version))
        selected.append((source,new,old if same_unit else None))
    if not retiring: return
    config_path = root/'repository/config.json'
    config = r.read_json(config_path,root=root)
    state = identity.material_next(config)
    for old in retiring:
        key = identity.namespace(old)
        r.require(state.get(key,0) > old.number,
                  'Initialize the retiring U namespace from an agent-confirmed issued upper bound: ' + key)
    prepared = json.loads(changes[config_path]) if config_path in changes else config
    identity.material_next(prepared,config)
    reserved, positions = prepared, set()
    for source,ident,old in sorted(selected,key=lambda item:(identity.namespace(item[1]),item[1].number)):
        position = identity.namespace(ident), ident.number
        if position in positions: continue
        folder = root/'mathematics/audits/literature'/ident.source_key
        existing_paths = [path.relative_to(root).as_posix() for path in folder.glob('*.md')
                    if identity.candidate(path.relative_to(root).as_posix())
                    and identity.candidate(path.relative_to(root).as_posix())['kind'] == 'U']
        existing = [identity.parse(path) for path in existing_paths]
        occupied, _ = discovery.unit_positions(existing_paths,lambda name:discovery.unit_header(root,name))
        raw = changes.get(source,source.read_bytes()).decode('utf-8-sig')
        _, header, _ = documents.author_header(moves[source].relative_to(root).as_posix(),raw)
        established = occupied.get((ident.source_key,ident.number)) == discovery.unit_origin(ident,header)
        if old is not None:
            _, prior_header, _ = documents.author_header(source.relative_to(root).as_posix(), source.read_text(encoding='utf-8-sig'))
            r.require((header.get('source_repository'), header.get('source_material')) ==
                      (prior_header.get('source_repository'), prior_header.get('source_material')),
                      'A chosen source-key correction preserves the original unit binding.')
            state_now = identity.material_next(reserved)
            state_now[identity.namespace(ident)] = max(state_now.get(identity.namespace(ident), 1), state[identity.namespace(old)])
            reserved = {**reserved, 'material_next': state_now}
            established = True
        reserved = identity.reserve(reserved,ident,existing,established=established)
        positions.add(position)
    if reserved['material_next'] != state:
        # The caller holds the shared lock; publish rollback never owns this state.
        r.write_json(config_path,{**config,'material_next':reserved['material_next']},root=root)
    if config_path in changes:
        changes[config_path] = r.encoded(reserved)


def rename(root, entries, mapping, *, files=(), moves=None, updates=None):
    root = Path(root).resolve()
    moves, updates = moves or {}, updates or {}
    original = (root/bib.BIB).read_bytes()
    text = original.decode('utf-8-sig')
    r.require(bib.parse(text) == entries, 'Supplied bibliography changed; prepare from the current entries again.')
    for old,new in mapping.items():
        r.require(old in entries, 'Selected bibliography key is absent: '+old)
        r.require(isinstance(new,str) and new and not any(key.casefold() == new.casefold() and key not in mapping for key in entries),
                  'A bibliography destination is already occupied: '+str(new))
    selected = tuple(dict.fromkeys((*files, *moves, *updates)))
    changes, relocations = plan(root,files=selected,moves=moves,updates=updates)
    text = changes.get(root/bib.BIB,original).decode('utf-8-sig')
    updated = rename_keys(text,mapping)
    chosen = bib.parse(updated)
    if updated != original.decode('utf-8-sig'): changes[root/bib.BIB] = updated.encode('utf8')
    _check_operations(root,selected,changes,relocations)
    _reserve_unit_moves(root,changes,relocations,mapping)
    result = publish(changes,relocations)
    entries.clear(); entries.update(chosen)
    return result
