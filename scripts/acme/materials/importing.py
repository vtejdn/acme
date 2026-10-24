"""Explicit own-content import with agent-chosen forward dependencies.

Preparation inputs and source correspondence are transient. Ordinary local
contents are the only own-content result; foreign branches use actual intake.
"""
from pathlib import Path, PurePosixPath

from . import documents, identity as names, discovery, tasks
from ..core import repository as r, identity as humans, links
from ..core.publication import Batch, Preparation


def material_identity(path):
    try:
        return names.parse(path)
    except ValueError:
        return None


def selected(plan):
    """Traverse only explicit necessary edges; never discover textual links."""
    r.require(isinstance(plan, dict) and isinstance(plan.get('entries'), list)
              and isinstance(plan.get('roots'), list) and plan['roots'],
              'Supply explicitly selected roots and prepared entries.')
    entries = {}
    for entry in plan['entries']:
        r.require(isinstance(entry, dict) and isinstance(entry.get('id'), str)
                  and entry['id'] and entry['id'] not in entries, 'Each selected entry needs one unique id.')
        entries[entry['id']] = entry
    seen, ordered = set(), []
    def visit(key):
        if key in seen:
            return
        r.require(key in entries, 'A required dependency needs an explicit entry or unavailable limitation: ' + str(key))
        seen.add(key)
        entry = entries[key]
        dependencies = entry.get('dependencies', [])
        r.require(isinstance(dependencies, list) and all(isinstance(item, str) for item in dependencies),
                  'Dependencies are an explicit list of necessary entry ids.')
        ordered.append(entry)
        for dependency in dependencies:
            visit(dependency)
    for root in plan['roots']:
        visit(root)
    return ordered


def _destination(repo, path, author):
    r.require(isinstance(path, str) and PurePosixPath(path).as_posix() == path,
              'Use a canonical explicit receiving file path.')
    target = r.safe_path(repo.root, path)
    # The selected file must belong to the actual human's responsible home.
    ident = material_identity(path)
    if ident:
        r.require(ident.author == author and ident.source_repository is None,
                  'Own import uses the actual local author, without an acquired identity.')
        if ident.kind not in 'UJ':
            from .write import HOMES
            r.require(PurePosixPath(path).parent.as_posix() == 'mathematics/' + HOMES[ident.kind],
                      'Use the selected kind\'s actual typed mathematical home.')
        elif ident.kind == 'J':
            r.require(path.startswith('mathematics/computations/programs/' + ident.name + '/')
                      or path.startswith('mathematics/computation/outputs/' + ident.name + '/'),
                      'Native J files use their actual program or output home.')
    else:
        allowed = (path.startswith('profiles/' + author + '/')
                   or any(path.startswith('mathematics/' + home + '/')
                          for home in ('manuscripts', 'presentations', 'talks')))
        r.require(allowed, 'Select the actual author\'s profile, document or typed mathematical home.')
        for person in humans.registry(repo)['people']:
            if person['id'] == author:
                continue
            r.require(not any(path.startswith('mathematics/' + home + '/' + person['id'] + '_')
                              for home in ('manuscripts', 'presentations', 'talks')),
                      'Do not place own imported content in another registered human\'s document home.')
    return target


def _source_author(path, raw, author, correspondence):
    ident = material_identity(path)
    if ident:
        r.require(ident.source_repository is None,
                  'Already-intaken content keeps its existing acquired identity; reuse its actual local counterpart.')
        # A J child inherits its source entrance's author; it has no new author.
        source_name = ident.author
        if path.endswith('.md') and (ident.kind != 'J' or PurePosixPath(path).name == 'readme.md'):
            header, _body = documents.header_values(raw.decode('utf-8-sig'), known=False)
            r.require(header['author'] == ident.author, 'Source path and actual single author disagree.')
            r.require(not {'source_repository', 'source_material'} & header.keys(),
                      'Already-intaken content keeps its existing acquired identity; reuse its actual local counterpart.')
            source_name = header['author']
        r.require(source_name == author or correspondence.get(source_name) == author,
                  'Establish the selected source author as the actual importing human; another author uses intake.')


def _source_task_type(path, raw):
    # Only the necessary coordination declaration is a source-format input;
    # old contracts and decisions need not pass the receiving document parser.
    _header, body = documents.header_values(raw.decode('utf-8-sig'), known=False)
    return tasks.declarations(path, documents.MarkdownInput(body))[0]


def _boundary(path, doc, source_path, source, existing, prepared=None):
    from ..execution import records
    original = None
    if names.candidate(source_path) and names.parse(source_path).kind == 'T':
        source_ident = names.parse(source_path)
        if source_ident.source_repository is None:
            source_e = records.address(source_path)
            raw = source.watch(source_e)
            if raw is not None:
                original = raw.decode('utf-8-sig')
                # Read only the actual source assignment/state facts. Unknown
                # old fields and unrelated prose are not receiving E content.
                tables = [rows for header, rows in documents.MarkdownInput(original).tables()
                          if tuple(header) == ('Field', 'Value')
                          and {'task', 'state'} <= {cells[0] for cells, _ in rows}]
                r.require(len(tables) == 1, 'Identify one actual source Task execution boundary.')
                rows = [cells for cells, _ in tables[0]]
                r.require(all(len(row) == 2 and all(row) for row in rows)
                          and len(dict(rows)) == len(rows), 'Source E has ambiguous execution fields.')
                fields = dict(rows)
                r.require(fields['state'] != 'running',
                          'Stop the former Task writer before moving its assignment; import grants no parallel allowance.')
                old_task = fields['task']
                r.require(names.parse(old_task.partition('#')[0]).family == source_ident.family,
                          'The source E must belong to the selected source Task family.')
    if existing is not None:
        # Existing effective state and limits remain byte-for-byte owned here.
        return None
    if prepared is not None:
        text = links.edit_text(original or '', prepared, context='execution boundary')
        fields = records.parse(path, text)
        r.require(fields['state'] != 'running', 'Import prepares only a non-running execution boundary.')
        return text.encode('utf8')
    r.require(original is None,
              'Supply explicitly chosen execution text or exact edits for the moved Task; source E is not copied automatically.')
    return ('# Current execution boundary\n\n| Field | Value |\n| --- | --- |\n'
            '| task | ' + doc.current.path + '#' + doc.current.anchor + ' |\n'
            '| state | not-running |\n\nImport grants no execution authority or allowance.\n').encode('utf8')


def import_content(repo, source_root, plan, *, author=None, timeout=30):
    author = author or repo.actor()
    humans.require_author(repo, author)
    source = Preparation(Path(source_root).resolve())
    batch = Batch(repo)
    batch.snapshots.append(source)
    for path in ('repository/config.json', 'repository/people.json'):
        batch.snapshot.watch(path)
    entries = selected(plan)
    correspondence = plan.get('author_correspondence', {})
    r.require(isinstance(correspondence, dict) and all(value == author for value in correspondence.values()),
              'Prepared same-human source correspondence belongs only to this importing human.')
    own, foreign, notices, reservations = [], [], [], []
    for entry in entries:
        if 'unavailable' in entry:
            r.require(isinstance(entry['unavailable'], str) and entry['unavailable'].strip(),
                      'Describe the actual unavailable dependency at its consumer.')
            notices.append(entry['unavailable'])
            continue
        if 'intake' in entry:
            foreign.append(entry['intake'])
            continue
        path = entry['local']
        if entry.get('reuse'):
            raw = batch.snapshot.bytes(path)
            # Reuse may name already-local foreign or already-intaken own
            # evidence. It writes neither a conversion nor a shadow original.
            if names.candidate(path):
                doc = documents.parse(path, raw.decode('utf-8-sig'))
                if doc.identity.source_repository:
                    from ..intake.acquire import material_info
                    material_info(repo, doc)
            own.append(path)
            continue
        target = _destination(repo, path, author)
        original = source.bytes(entry['source'])
        _source_author(entry['source'], original, author, correspondence)
        source_ident = material_identity(entry['source'])
        if source_ident and source_ident.kind == 'J' and PurePosixPath(entry['source']).name != 'readme.md':
            entrance = 'mathematics/computations/programs/' + source_ident.name + '/readme.md'
            _source_author(entrance, source.bytes(entrance), author, correspondence)
        if 'prepared' in entry:
            raw = links.edit_text(original.decode('utf-8-sig'), entry['prepared'], context='personal import').encode('utf8')
        else:
            raw = original
        before = batch.snapshot.watch(path)
        candidate = material_identity(path)
        if before is not None and before != raw:
            fixed = candidate and candidate.kind in 'CTRLU'
            r.require(not fixed, 'Preserve the occupied fixed version; reuse it or prepare the appropriate next physical version.')
            r.require(entry.get('expected') == before.decode('utf-8-sig'),
                      'A rolling/profile/document replacement needs its exact expected receiving text.')
        if candidate:
            ident = candidate
            relatives = batch.snapshot.family(ident)
            established = bool(relatives)
            if ident.kind != 'J' or PurePosixPath(path).name == 'readme.md':
                doc = documents.parse(path, raw.decode('utf-8-sig'))
                if ident.kind == 'T':
                    source_ident = material_identity(entry['source'])
                    if source_ident and source_ident.kind == 'T':
                        original_type = _source_task_type(entry['source'], original)
                        for relative in source.family(source_ident):
                            sibling = source.bytes(relative)
                            _source_author(relative, sibling, author, correspondence)
                            r.require(_source_task_type(relative, sibling) == original_type,
                                      'Source Task family type is invariant across its actual versions.')
                        r.require(doc.task_type == original_type,
                                  'Task family type is invariant across prepared import; preserve its explicit joint declaration.')
                    from ..execution import records
                    if doc.task_type == 'ordinary':
                        execution = records.address(path)
                        boundary = _boundary(execution, doc, entry['source'], source,
                                             batch.snapshot.watch(execution), entry.get('execution'))
                        if boundary is not None:
                            batch.add({execution: boundary})
                if ident.kind == 'U':
                    units = Preparation(repo.root, [ident.source_key])
                    batch.snapshots.append(units)
            reservations.append((ident, established))
        batch.add({path: raw})
        own.append(path)

    def validate(read, view):
        from .validation import validate_locator_targets
        from ..execution import records
        from ..core import source_refs, external
        entrances = set(discovery.candidates(repo.root)) | set(batch.pending)
        units = []
        for path in own:
            raw = read(path)
            ident = material_identity(path)
            if ident and ident.kind == 'J' and PurePosixPath(path).name != 'readme.md':
                if r.paths.in_computation_outputs(path):
                    entrance = 'mathematics/computations/programs/' + ident.name + '/readme.md'
                else:
                    parts = PurePosixPath(path).parts
                    entrance = PurePosixPath(*parts[:parts.index(ident.name) + 1], 'readme.md').as_posix()
                owner = documents.parse(entrance, read(entrance))
                r.require(owner.identity == ident, 'A native J input needs its actual same-group authored entrance.')
            if ident and (ident.kind != 'J' or PurePosixPath(path).name == 'readme.md'):
                doc = documents.parse(path, raw)
                documents.check(doc, read, paths=entrances)
                if ident.kind == 'T' and doc.task_type == 'ordinary':
                    boundary = records.address(path)
                    records.validate(view, records.parse(boundary, read(boundary)), boundary)
                if ident.kind == 'U':
                    units.extend(candidate for candidate in entrances if (item := names.candidate(candidate))
                                 and item['kind'] == 'U' and item['source_key'] == ident.source_key)
            if isinstance(raw, str):
                locators = []
                for _, _, href in links.markdown_link_spans(raw):
                    original = source_refs.parse(href.strip().strip('<>'))
                    if original is not None:
                        external.repository(view, original['repository'])
                    destination = links.destination(path, href)
                    if destination is not None and not r.paths.in_pdf_store(destination[0]):
                        locators.append({'path': destination[0], 'anchor': destination[1]})
                validate_locator_targets(locators, read)
        if units:
            discovery.unit_positions(sorted(set(units)), read)
        for boundary in (path for path in batch.pending if path.startswith('execution/')):
            records.validate(view, records.parse(boundary, read(boundary)), boundary)

    batch.add({}, reservations=reservations, validate=validate)
    # Import does not use intake for any own-content branch. Only explicitly
    # reached foreign nodes invoke it, with their own provenance and operation.
    operations = []
    if foreign:
        from ..intake.acquire import acquire
        for options in foreign:
            options = dict(options)
            foreign_root = options.pop('source_root')
            selections = options.pop('selections')
            result = acquire(repo, foreign_root, selections, batch=batch, **options)
            operations.append(result['operation'])
            notices.extend(result['notices'])
    installed = batch.commit(timeout=timeout)
    return {'materials': own, 'installed': installed, 'foreign_operations': operations, 'notices': notices}
