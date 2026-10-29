"""Receive explicitly prepared mathematical units at one fixed source revision."""
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
from urllib.parse import quote
import uuid

from ..core import repository as r
from ..core import identity as humans
from ..core import links, source_refs, external
from ..core.publication import Preparation as _Preparation, Batch
from ..materials import documents, identity as names
from . import bibliography as bib

KINDS = {'C', 'T', 'R', 'U', 'L', 'J'}
SOURCE_KINDS = KINDS | {'S', 'D'}
HOMES = {'C': 'claims', 'T': 'tasks', 'R': 'audits/reviews', 'L': 'ledger', 'J': 'computations/programs'}


class GitSource:
    def __init__(self, root, revision):
        from ..core.git_views import Tree, git
        r.require(re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', revision or ''), 'Intake requires a full fixed source commit.')
        resolved = git(root, 'rev-parse', '--verify', revision + '^{commit}').decode().strip()
        r.require(resolved == revision, 'Source revision differs from the requested commit.')
        self.tree = Tree(root, revision)
        self.root, self.revision = Path(root).resolve(), revision
        self.names = self.tree.names
        self.config = self.tree.json('repository/config.json')
        r.require(isinstance(self.config, dict), 'Repository configuration must be an object.')
        humans.repository_name(self.config.get('repository'), required=True)
        self._entries = None

    @property
    def entries(self):
        """Load bibliography only when a selected U actually requests its fields."""
        if self._entries is None:
            self._entries = bib.parse(self.read(bib.BIB).decode('utf-8-sig')) if bib.BIB in self.names else {}
        return self._entries

    def read(self, path):
        return self.tree.bytes(path)

    def close(self):
        self.tree.close()

    def source_view(self):
        return self.tree.research_view()


def operations(repo):
    tree = getattr(repo, 'selected_tree', None)
    if tree is None:
        paths = [path.relative_to(repo.root).as_posix() for path in (repo.root/'intake').glob('*/*.json')]
    else:
        paths = sorted(path for path in tree.names if re.fullmatch(r'intake/[^/]+/[^/]+\.json', path))
    for path in paths:
        try: value = json.loads(r.read_from(repo, path))
        except json.JSONDecodeError: continue
        if not isinstance(value, dict) or not isinstance(value.get('items'), list): continue
        yield path, value


def check_selection(doc, anchor, *, receiving_kind=None, prepared=False):
    """A selected independent historical L finding needs its prepared R home."""
    if doc.identity.kind == 'L' and anchor:
        from ..materials import review
        selected = documents.Locator(doc.path, anchor)
        relationship = review.relationships(doc, finding=selected).get(selected)
        r.require(relationship != 'independently reviewed' or (prepared and receiving_kind == 'R'),
                  'Prepare an actual independent L finding in fixed receiving R with its true scope and limits: '
                  + doc.path + '#' + anchor)


def _reviewed_targets(targets, repository, revision):
    r.require(isinstance(targets, list), 'Supply the actual original reviewed_targets list, including any real undeclared scope.')
    for target in targets:
        r.require(isinstance(target, dict) and set(target) == {'path', 'anchor', 'scope'}
                  and all(isinstance(target[field], str) for field in target) and target['scope'].strip(),
                  'Retain each actual original review target and inspected scope.')
        if source_refs.parse(target['path']) is None:
            source_refs.make(repository, revision, target['path'], target['anchor'])
        else:
            r.require('#' not in target['path'],
                      'Original reviewed target URI path must omit the fragment separator; use the separate anchor field.')


def _recorded_material_path(repo, path):
    """Recorded local keys belong to their selected view, not always this disk."""
    from ..core.git_views import Tree
    tree = getattr(repo, 'selected_tree', None)
    if isinstance(tree, Tree) and tree.ref not in (None, 'WORKTREE'):
        r.require(isinstance(path, str) and path and '\\' not in path
                  and not PurePosixPath(path).is_absolute(), 'Use a repository-relative POSIX path.')
        key = r.relative(repo, path)
        r.require(not r.paths.in_pdf_store(key), 'Private local literature is outside intake.')
    else:
        # Preparation and Batch postimages still describe actual local writes.
        r.safe_path(repo.root, path)


def validate_operation(repo, path, value, *, read=None, new_selection=False):
    """Validate recorded facts and original identity, not old scopes in mutable J."""
    parts = PurePosixPath(path).parts
    r.require(len(parts) == 3 and parts[0] == 'intake' and parts[1] == value['initiator'], 'Intake belongs to its actual initiating human.')
    humans.person(repo, value['initiator']); humans.person(repo, value['recorded_by'])
    r.valid_stamp(value['at'])
    r.require(value.get('instruction') and value.get('items'), 'Acquisition needs its actual instruction and selected scope.')
    read = read or (lambda name:r.read_from(repo, name))
    for item in value['items']:
        r.require(item['kind'] in KINDS, 'Select an eligible adapted mathematical home.')
        origin = item['source']
        external.repository(repo, origin['repository'])
        external.repository(repo, value['transport']['repository'])
        if item['kind'] in 'CTRLJ':
            external.person(repo, origin['author'], origin['repository'], origin['author_name'])
        source_refs.parse(source_refs.make(origin['repository'], origin['revision'], origin['path'], origin.get('anchor', '')))
        _reviewed_targets(origin.get('reviewed_targets', []), origin['repository'], origin['revision'])
        local = item['local']
        _recorded_material_path(repo, local['path'])
        raw = read(local['path'])
        doc = documents.parse(local['path'], raw.decode('utf-8-sig') if isinstance(raw,bytes) else raw)
        r.require(doc.identity.kind == item['kind'], 'Acquisition kind disagrees with its receiving material.')
        if 'source_material' in doc.header:
            r.require((doc.header.get('source_repository'), doc.header['source_material']) ==
                      (origin['repository'], origin['path']), 'Acquisition metadata disagrees with the obtained original.')
        else:
            r.require(bool(doc.identity.source_repository) and item['kind'] in 'CTRLJ',
                      'A combined original needs an external single-author receiving identity.')
            external.person(repo, doc.identity.author, doc.identity.source_repository)
        if item['kind'] in 'CTRLJ':
            r.require(doc.identity.author == origin['author'], 'Acquired author differs from its adopted local source record.')
        r.require(item.get('scope') and (item['kind'] == 'J' or not local.get('anchor')
                  or links.anchor_occurrences(doc.text)[local['anchor']] == 1),
                  'Acquired scope needs one actual local anchor and its description.')
        if item['kind'] == 'C': r.require(local.get('anchor') in doc.decisions, 'Acquired Claim needs its exact decision.')
        if item['kind'] == 'U': r.require(local.get('anchor') == doc.identity.anchor, 'Acquired U needs its exact unit.')
        if item['kind'] == 'R': _require_review_finding(doc, local.get('anchor', ''))
        if new_selection: check_selection(doc, local.get('anchor', ''))
        for pair in item['files']:
            source_refs.make(value['transport']['repository'],value['transport']['revision'],pair['source'])
            _recorded_material_path(repo, pair['local'])
            r.require(pair['local']==local['path'] or (item['kind']=='J' and pair['local'].startswith(posixpath.dirname(local['path'])+'/')),
                      'Acquired files must belong to the selected typed material or its J group.')
            if item['kind'] != 'J':
                read(pair['local'])
            else:
                original = _file_key(item, pair)
                external.repository(repo, original[0])
        for artifact in item.get('source_artifacts', []):
            r.require(item['kind'] == 'U' and isinstance(artifact, dict)
                      and set(artifact) == {'source','local','available'}
                      and isinstance(artifact['available'], bool)
                      and r.paths.valid_source_name(artifact['source']),
                      'Selected source artifacts need their explicit original/local paths and availability.')
            prefix = r.paths.PDF_ROOT.as_posix()+'/'
            r.require(isinstance(artifact['local'], str) and artifact['local'].startswith(prefix)
                      and r.paths.valid_source_name(artifact['local'][len(prefix):]),
                      'Selected source artifact local path must identify a retained source file.')
    return value


def material_info(repo, document, *, read=None, seen=()):
    r.require(document.identity.kind in KINDS, 'Use the actual adapted receiving mathematical home.')
    r.require(document.path not in seen, 'Cyclic explicit receiving input: ' + document.path)
    read = read or (lambda path: r.read_from(repo, path))
    found = []
    for path, operation in operations(repo):
        for item in operation['items']:
            if not isinstance(item, dict) or not isinstance(item.get('local'), dict) or item['local'].get('path') != document.path:
                continue
            # A requested original validates its own acquired item, not all
            # unrelated objects acquired in the same historical operation.
            validate_operation(repo, path, {**operation, 'items': [item]}, read=read)
            origin = item['source']
            if 'source_material' in document.header:
                r.require((origin['repository'], origin['path']) ==
                          (document.header['source_repository'], document.header['source_material']),
                          'Acquisition original identity disagrees with material header.')
            found.append({'operation': path, 'source': origin, 'scope': item['scope'], 'local': item['local'],
                          'source_artifacts': item.get('source_artifacts', []),
                          'unmapped_references': item.get('unmapped_references', item.get('missing_inputs', []))})
    if not found:
        inputs = documents.revision_inputs(document, read)
        r.require(inputs, 'A local revision needs its explicit acquired receiving input and scope: ' + document.path)
        from ..materials.validation import validate_locator_targets
        validate_locator_targets(inputs, read)
        resolved = []
        for entry in inputs:
            raw = read(entry['path'])
            earlier = documents.parse(entry['path'], raw.decode('utf-8-sig') if isinstance(raw, bytes) else raw)
            r.require((earlier.header.get('source_repository'), earlier.header.get('source_material')) ==
                      (document.header.get('source_repository'), document.header.get('source_material')),
                      'The explicit receiving input contradicts the revision\'s original binding.')
            info = material_info(repo, earlier, read=read, seen=(*seen, document.path))
            resolved.append({**entry, 'acquisitions': info['acquisitions']})
            for row in info['acquisitions']:
                if row not in found:
                    found.append(row)
        return {'origin': document.header, 'inputs': resolved, 'acquisitions': found}
    if 'source_material' not in document.header:
        r.require(len({(row['source']['repository'], row['source']['path']) for row in found}) > 1,
                  'A combined original needs its distinct per-unit source accounts in the existing intake records.')
    return {'origin': document.header, 'acquisitions': found}


def finding_evidence(repo, locator):
    doc = documents.parse(locator.path, r.read_from(repo, locator.path).decode('utf-8-sig'))
    info = material_info(repo, doc)
    local_revision = bool(info.get('inputs'))
    if not local_revision:
        selected = any(row['local'].get('anchor', '') in ('', locator.anchor) for row in info['acquisitions'])
        r.require(selected, 'The selected review finding was not acquired.')
    relationships, bindings = _require_review_finding(doc, locator.anchor)
    if local_revision:
        from ..materials import review
        # The operation describes the input. Compare only the selected current
        # declarations with that explicitly designated fixed finding, preserving
        # retained declarations while checking new/changed findings strictly.
        relationships, bindings = review.check_findings(doc, finding=locator,
            read=lambda path: r.read_from(repo, path))
    available = {(target.path, target.anchor) for finding, target, scope in bindings
                 if finding == locator and not source_refs.external(target.path)}
    from ..materials.validation import validate_locator_targets
    validate_locator_targets([{'path': path, 'anchor': anchor} for path, anchor in available],
                             lambda path: r.read_from(repo, path))
    return relationships.get(locator, 'unknown'), available


def _source_items(source, doc, record=None):
    for path in sorted(source.names):
        if record is not None and path != record: continue
        if re.fullmatch(r'intake/[^/]+/[^/]+\.json', path):
            try: operation = json.loads(source.read(path))
            except json.JSONDecodeError: continue
            if not isinstance(operation, dict) or not isinstance(operation.get('items'), list): continue
            for item in operation.get('items', []):
                if isinstance(item, dict) and isinstance(item.get('local'), dict) and item['local'].get('path') == doc.path:
                    yield path, item


def _correspondence(rows, context, record=None):
    if record is not None: rows = [row for row in rows if row[0] == record]
    r.require(rows, 'No acquired file/scope correspondence: ' + context)
    values = [row[1] for row in rows]
    r.require(all(value == values[0] for value in values),
              'Ambiguous acquisition correspondence: ' + context + '; select an existing acquisition record or explicit mapping.')
    return values[0]


def _file_key(item, pair):
    source, local = item['source'], item['local']
    entrances = [row['source'] for row in item['files']
                 if isinstance(row, dict) and row.get('local') == local['path'] and isinstance(row.get('source'), str)]
    r.require(len(entrances) == 1, 'Acquired J file correspondence lacks its exact group entrance: ' + local['path'])
    entrance = entrances[0]
    for path in (source['path'], entrance, pair['source']):
        source_refs.make(source['repository'], source['revision'], path)
    original = posixpath.join(posixpath.dirname(source['path']),
                             posixpath.relpath(pair['source'], posixpath.dirname(entrance)))
    recorded = pair.get('original', {'repository': source['repository'], 'path': original, 'revision': source['revision']})
    r.require(isinstance(recorded, dict) and set(recorded) == {'repository', 'path', 'revision'},
              'A per-file original needs its repository, path and revision.')
    source_refs.make(recorded['repository'], recorded['revision'], recorded['path'])
    r.require(recorded['repository'] == source['repository']
              and recorded['path'].startswith(posixpath.dirname(source['path']) + '/'),
              'Selected file belongs to another original J: ' + str(recorded))
    return recorded['repository'], recorded['path'], recorded['revision'], ''


def _mapped_author(source, repository, name):
    matches = [row['author'] for row in source.author_mapping
               if row['repository'] == repository and row['name'] == name]
    r.require(len(matches) == 1, 'Supply one adopted original author correspondence: ' + repository + '/' + name)
    external.person(source.receiver, matches[0], repository, name)
    return matches[0]


def _origin(source, doc, anchor='', record=None, choice=None):
    if not doc.identity.source_repository:
        r.require(choice in (None, 'current'), 'An ordinary original has its current source context.')
        repository, name = source.transport, doc.identity.author
        origin = {'repository': repository, 'revision': source.revision, 'path': doc.path, 'anchor': anchor}
    else:
        matches = []
        for operation, item in _source_items(source, doc, record):
            if 'source_material' in doc.header:
                r.require((item['source']['repository'], item['source']['path']) ==
                          (doc.header['source_repository'], doc.header['source_material']),
                          'Onward provenance conflicts with the original header.')
            local_anchor = item['local'].get('anchor', '')
            original = item['source']
            if doc.identity.kind == 'J':
                entrance = [pair for pair in item['files'] if isinstance(pair, dict) and pair.get('local') == doc.path]
                if not entrance: continue
                r.require(len(entrance) == 1, 'Ambiguous acquired J entrance: ' + doc.path)
                original = {**original, 'revision': _file_key(item, entrance[0])[2]}
            if local_anchor in ('', anchor): matches.append((operation, original))
            elif doc.identity.kind == 'C' and local_anchor in doc.decisions:
                if any(role == 'statement' and loc == documents.Locator(doc.path, anchor)
                       for role, loc, scope in doc.decisions[local_anchor].relations):
                    matches.append((operation, original))
        if not matches:
            # An explicit local revision is supplied by this fixed sender
            # version. Its Inputs references retain the earlier acquired facts;
            # newly authored content must not be attributed to that old source.
            r.require(record is None, 'The selected acquisition record does not name this local revision.')
            info = material_info(source.source_view(), doc)
            r.require(info.get('inputs'), 'Onward transfer lacks its actual acquired input: ' + doc.path)
            if doc.identity.kind == 'R':
                r.require(choice is not None,
                          'Choose current origin or an exact acquired input for the selected revised-R finding.')
                if choice != 'current':
                    r.require(isinstance(choice, dict) and set(choice) <= {'input', 'acquisition'} and 'input' in choice,
                              'A selected inherited origin needs one exact input locator and optional acquisition selector.')
                    selected = choice['input']
                    r.require(isinstance(selected, dict) and set(selected) == {'path', 'anchor'}
                              and all(isinstance(selected[key], str) and selected[key] for key in selected),
                              'Supply the exact fixed input path and finding anchor.')
                    r.require(any(entry['path'] == selected['path'] and entry['anchor'] in ('', selected['anchor'])
                                  for entry in info['inputs']), 'The chosen origin is not a declared fixed revision input.')
                    earlier = documents.parse(selected['path'], source.read(selected['path']).decode('utf-8-sig'))
                    _require_review_finding(earlier, selected['anchor'])
                    selected_record = choice.get('acquisition')
                    r.require(selected_record is None or isinstance(selected_record, str), 'Select an existing acquisition record path.')
                    r.require(any(item['local'].get('anchor', '') in ('', selected['anchor'])
                                  for _path, item in _source_items(source, earlier, selected_record)),
                              'The chosen existing acquisition does not cover this input finding.')
                    return _origin(source, earlier, selected['anchor'], selected_record)
            return {'repository': source.transport, 'revision': source.revision,
                    'path': doc.path, 'anchor': anchor, 'author_name': doc.identity.author,
                    'author': _mapped_author(source, source.transport, doc.identity.author)}
        r.require(choice is None, 'This directly acquired finding already has its recorded original context.')
        origin = _correspondence(matches, doc.path, record).copy()
        foreign = origin['repository']
        external.repository(source.source_view(), foreign)
        r.require(foreign in source.repository_mapping, 'Map the selected original repository from its sender namespace: ' + foreign)
        repository = source.repository_mapping[foreign]
        external.repository(source.receiver, repository)
        name = origin['author_name']
        if doc.identity.kind in 'CTRLJSD':
            r.require(origin['author'] == doc.identity.author, 'Onward original author conflicts with the material header.')
            external.person(source.source_view(), origin['author'], foreign, name)
        origin['repository'] = repository
    origin['author_name'] = name
    if doc.identity.kind in 'CTRLJSD': origin['author'] = _mapped_author(source, repository, name)
    return origin


def _require_review_finding(doc, anchor):
    from ..materials import review
    selected = documents.Locator(doc.path, anchor)
    r.require(anchor and links.anchor_occurrences(doc.text)[anchor] == 1,
              'Select one actual review finding anchor.')
    # Target kinds and acquisition need are agent judgments. Source-only or
    # historically undeclared targets retain their actual evidence limitation.
    relationships = review.relationships(doc, finding=selected)
    bindings = review.bindings(doc, finding=selected)
    return relationships, bindings


def manifest(source, selections, *, files=()):
    r.require(selections, 'Select at least one mathematical unit and its actual scope.')
    result = []
    for selection in selections:
        path, anchor = selection['path'], selection.get('anchor', '')
        r.require(not r.paths.in_computation_outputs(path), 'J intake selects fixed programs and inputs, not local outputs.')
        item = names.parse(path)
        r.require(item.kind in SOURCE_KINDS, 'Select a mathematical unit; personal files use personal import.')
        r.require(path in source.names, 'Selected source file is unavailable: ' + path)
        raw = source.read(path).decode('utf-8-sig')
        original_header = None
        if raw.startswith(('---\n', '---\r\n')):
            original_header, _ = documents.header_values(raw, known=False)
            r.require(original_header['author'] == item.author, 'Source path and actual single author disagree.')
        raw_source = bool(selection.get('prepared')) and selection.get('source_author') is not None
        if raw_source:
            from types import SimpleNamespace
            r.require(not item.source_repository and selection['source_author'] == item.author,
                      'Raw source preparation needs its explicit original source_author.')
            r.require(original_header is None or not {'source_repository', 'source_material'} & original_header.keys(),
                      'Raw source preparation cannot replace declared original-source bindings.')
            # Explicit preparation selects source text as content, without
            # interpreting its old declarations as valid current decisions.
            from ..materials import tasks
            task_type = tasks.declarations(path, documents.MarkdownInput(raw))[0] if item.kind == 'T' else 'ordinary'
            doc = SimpleNamespace(path=path, identity=item, header={'author': item.author}, text=raw,
                                  decisions={}, task_type=task_type)
        else:
            doc = documents.parse(path, raw)
        local_kind = selection.get('local', {}).get('kind', item.kind)
        r.require(local_kind in KINDS and (item.kind == 'U') == (local_kind == 'U'),
                  'Adapt selected S/D content into its actual fixed mathematical home; U keeps its own contract.')
        r.require(item.kind != 'T' or doc.task_type == 'joint', 'Intake receives only a necessary common joint T contract.')
        r.require(local_kind != 'T' or (item.kind == 'T' and doc.task_type == 'joint'),
                  'Intake does not manufacture another human\'s ordinary Task or a joint contract from other content.')
        r.require(not anchor or links.anchor_occurrences(raw)[anchor] == 1, 'Selected source anchor is absent or ambiguous.')
        source_finding = documents.Locator(doc.path, anchor) if anchor else None
        selected_bindings = []
        raw_review = raw_source and (item.kind == 'R' or (item.kind == 'L' and (
            anchor or local_kind == 'R' or 'source_review' in selection)))
        source_review = selection.get('source_review') if raw_review else None
        r.require('source_review' not in selection or raw_review,
                  'Explicit source_review facts belong only to a raw original R/L preparation.')
        if raw_review:
            r.require(isinstance(source_review, dict) and 'reviewed_targets' in source_review
                      and set(source_review) <= {'reviewed_targets', 'relationship'},
                      'Raw R/L preparation needs explicit original source_review facts and reviewed_targets.')
            r.require('relationship' not in source_review or (isinstance(source_review['relationship'], str)
                      and source_review['relationship'] in {'self-reviewed', 'independently reviewed', 'unknown'}),
                      'Unknown original finding review relationship.')
            _reviewed_targets(source_review['reviewed_targets'], source.transport, source.revision)
            r.require(source_review.get('relationship') != 'independently reviewed' or local_kind == 'R',
                      'Prepare an actual independent L/R finding in fixed receiving R with its true scope and limits.')
        elif item.kind in {'R', 'L'} and not raw_source:
            from ..materials import review
            # An explicit finding is read before unrelated old row targets.
            # A whole-container selection retains its complete validation scope.
            review.relationships(doc, finding=source_finding)
            selected_bindings = review.bindings(doc, finding=source_finding)
        r.require(item.kind != 'C' or anchor in doc.decisions or selection.get('prepared'), 'Select the Claim decision or explicitly prepare the selected mathematical unit.')
        r.require(item.kind != 'U' or anchor == item.anchor or selection.get('prepared'),
                  'Select the source unit anchor or explicitly adapt its actual older unit scope.')
        if not raw_source:
            check_selection(doc, anchor, receiving_kind=local_kind, prepared=bool(selection.get('prepared')))
        r.require(selection.get('scope'), 'Describe the actual selected mathematical scope.')
        r.require(item.kind != 'J' or PurePosixPath(path).name == 'readme.md', 'Select the J group README and explicit indispensable files.')
        owned = [path]
        if item.kind == 'J':
            prefix = posixpath.dirname(path) + '/'
            owned += [name for name in files if name.startswith(prefix) and name != path]
        for field in ('file_map', 'file_preparations'):
            choices = selection.get(field, {})
            r.require(isinstance(choices, dict) and set(choices) <= set(owned) - {path},
                      field + ' names only explicitly selected native children of this J.')
        records = selection.get('acquisition', {})
        r.require(isinstance(records, dict), 'Choose existing acquisition records by their selected source file path.')
        r.require(set(records) <= set(owned) and all(isinstance(value, str) for value in records.values()),
                  'Choose an existing acquisition record only for an actually selected file.')
        origin = _origin(source, doc, anchor, records.get(path), selection.get('origin'))
        if ((item.kind == 'R' or (item.kind == 'L' and local_kind == 'R') or raw_review)
                and (origin['repository'], origin['revision'], origin['path']) ==
                    (source.transport, source.revision, doc.path)):
            # These are the inspected input locators declared in the original
            # review's namespace, before receiving text/reference adaptation.
            # Onward transfer retains them with that original review account.
            origin['reviewed_targets'] = [dict(target) for target in source_review['reviewed_targets']] if raw_review else [
                {'path': target.path, 'anchor': target.anchor, 'scope': scope}
                for finding, target, scope in selected_bindings]
        file_origins = {}
        if item.kind == 'J' and doc.identity.source_repository:
            # Omitted inputs keep their prior acquisition; a group refresh does
            # not attribute every file still present to the newer revision.
            for name in owned:
                candidates = [(operation, _file_key(acquired, pair))
                              for operation, acquired in _source_items(source, doc, records.get(name))
                              for pair in acquired['files'] if isinstance(pair, dict) and pair.get('local') == name]
                original = _correspondence(candidates, name, records.get(name))
                r.require(source.repository_mapping.get(original[0]) == origin['repository'],
                          'Selected file belongs to another original J: ' + name)
                file_origins[name] = (origin['repository'], *original[1:])
        elif item.kind == 'J':
            file_origins = {name: (origin['repository'], name, source.revision, '') for name in owned}
        result.append({'doc': doc, 'kind': local_kind, 'source': origin, 'scope': selection['scope'],
                       'anchor': anchor, 'files': owned, 'file_origins': file_origins, 'selection': selection,
                       'source_review': source_review})
    owned = {path for item in result for path in item['files']}
    r.require(set(files) <= owned, 'Explicit files must belong to a selected J group; select C/R/U/L separately.')
    for path in owned:
        r.require(path in source.names, 'Required J input is absent: ' + path)
        source_refs.make(source.transport, source.revision, path)
        r.require(not r.paths.in_pdf_store(path), 'Private local literature is outside intake.')
    return sorted(result, key=lambda item: item['doc'].identity.kind == 'R')


def _available(repo, requested):
    result = {}
    files = {}
    for operation_path, operation in operations(repo):
        for item in operation['items']:
            if (not isinstance(item, dict) or item.get('kind') not in KINDS or
                    not isinstance(item.get('source'), dict) or not isinstance(item.get('local'), dict) or
                    not isinstance(item.get('files'), list)): continue
            source, local = item['source'], item['local']
            if not all(isinstance(source.get(field), str) for field in ('repository','path','revision')) or not isinstance(local.get('path'), str): continue
            if not any(repository == source['repository'] for repository, path in requested): continue
            if item.get('kind') == 'J':
                entrances = [row['source'] for row in item['files'] if isinstance(row, dict)
                             and row.get('local') == local['path'] and isinstance(row.get('source'), str)]
                for pair in item['files']:
                    if not isinstance(pair, dict) or not isinstance(pair.get('source'), str): continue
                    recorded = pair.get('original')
                    if isinstance(recorded, dict): original_path = recorded.get('path')
                    elif len(entrances) == 1:
                        original_path = posixpath.join(posixpath.dirname(source['path']),
                            posixpath.relpath(pair['source'], posixpath.dirname(entrances[0])))
                    else: continue
                    if (source['repository'], original_path) not in requested: continue
                    key = _file_key(item, pair)
                    destination = pair['local']
                    r.safe_path(repo.root, destination)
                    files.setdefault(destination, []).append((operation_path, key))
                continue
            if (source['repository'], source['path']) not in requested: continue
            key = source['repository'], source['path'], source['revision'], source.get('anchor', '')
            r.safe_path(repo.root, local['path'])
            destination = (local['path'], local.get('anchor', ''))
            r.require(key not in result or result[key] == destination,
                      'Ambiguous original scope correspondence; supply an exact selected mapping.')
            result[key] = destination
    for path, candidates in files.items():
        key = _correspondence(candidates, path)
        if r.safe_path(repo.root, path).is_file(): result[key] = (path, '')
    return result


def _check_j_refresh(repo, item, path, original):
    """Protect the occupied original group and its recorded native correspondence."""
    entrance, incoming = item['target'], item['source']
    try:
        raw = r.read_from(repo, entrance).decode('utf-8-sig')
    except FileNotFoundError as error:
        raise r.ResearchError('Cannot replace occupied J bytes without their original group entrance: ' + path) from error
    doc = documents.parse(entrance, raw)
    occupied = doc.header.get('source_repository'), doc.identity.author, doc.header.get('source_material')
    expected = incoming['repository'], incoming['author'], incoming['path']
    r.require(occupied == expected,
              'Occupied J original identity conflict at ' + entrance + ': '
              + str(occupied) + '; incoming ' + str(expected))
    material_info(repo, doc)
    if path != entrance:
        recorded = [_file_key(acquired, pair) for _, operation in operations(repo)
                    for acquired in operation['items']
                    if isinstance(acquired, dict) and isinstance(acquired.get('local'), dict)
                    and acquired['local'].get('path') == entrance
                    for pair in acquired['files'] if pair['local'] == path]
        r.require(recorded and all(key[:2] == original[:2] for key in recorded),
                  'Occupied J native file lacks its acquired original correspondence: ' + path)


def _unit_text(raw, choice):
    """Apply only agent-designated original offsets, or supplied final local text."""
    r.require(isinstance(choice, dict) and not set(choice)-{'number','version','edits','text'},
              'Supply the explicit receiving unit number and designated edits or final text.')
    r.require(type(choice.get('number')) is int and choice['number'] > 0,
              'Supply a positive explicit receiving unit number.')
    return links.edit_text(raw, {key:value for key,value in choice.items() if key not in {'number', 'version'}}, context='unit')


def acquire(repo, source_root, selections, *, revision, instruction, source_repository, correspondence,
            initiator=None, files=(), timeout=30, refresh_j=False, mapping=(), batch=None):
    """Receive prepared authored content after the caller's U acquisition duties.

    Original-source acquisition and its actual failure report are agent actions
    completed before U receipt; this helper neither fetches private originals
    nor infers their edition, availability or the adequacy of source evidence.
    """
    nonempty = lambda value: isinstance(value, str) and bool(value.strip())
    r.require(nonempty(instruction), 'Record the actual intake instruction.')
    for selection in selections:
        r.require(not selection.get('returning_original'), 'This repository does not reacquire its own returning originals.')
        retired = {'source_artifacts', 'source_bibliography', 'holding', 'source_updates'} & selection.keys()
        r.require(not retired, 'Private local literature is outside intake; retired inputs: ' + ', '.join(sorted(retired)))
        r.require('output_attachments' not in selection, 'Unsupported intake input: output_attachments; select fixed J programs and inputs.')
    for path in files:
        r.require(not r.paths.in_pdf_store(path), 'Private local literature is outside intake.')
        r.require(not r.paths.in_computation_outputs(path), 'J intake selects fixed programs and inputs, not local outputs.')
    recorder = repo.actor(); initiator = initiator or recorder
    coordinated = batch is not None
    batch = batch or Batch(repo)
    humans.person(repo, initiator)
    source = GitSource(source_root, revision)
    try:
        external.repository(repo, source_repository)
        r.require(isinstance(correspondence, dict) and not set(correspondence) - {'repositories', 'authors'},
                  'Supply prepared repository and author correspondence.')
        source.receiver, source.transport = repo, source_repository
        source.repository_mapping = dict(correspondence.get('repositories', {}))
        source.author_mapping = list(correspondence.get('authors', []))
        for foreign, local in source.repository_mapping.items():
            external.token(foreign, 'repo'); external.repository(repo, local)
        identity_before = {path: r.read_from(repo, path) for path in (external.REPOSITORIES, external.PEOPLE)}
        plan = manifest(source, selections, files=files)
        prepared = {path: source.read(path) for item in plan for path in item['files']}
        from . import literature
        chosen_works, choices = {}, {}
        for item in plan:
            if item['doc'].identity.kind != 'U': continue
            key = item['doc'].identity.source_key
            choice = item['selection'].get('bibliography')
            r.require(isinstance(choice, dict), 'Supply the chosen existing/new bibliography for each U.')
            r.require(choice.get('existing_key') or key in source.entries,
                      'A new bibliography work needs its actual supplied entry; otherwise choose an adequate existing work explicitly.')
            unit_choice = item['selection'].get('unit')
            r.require(isinstance(unit_choice, dict), 'Choose the actual receiving U position.')
            unit_choice = {**unit_choice, **item['selection'].get('prepared', {})}
            item['unit_text'] = _unit_text(prepared[item['doc'].path].decode('utf-8-sig'), unit_choice)
            unit_header, _ = documents.header_values(item['unit_text'])
            r.require(unit_header['author'] == item['doc'].identity.author,
                      'Prepared U content retains its actual single original human author.')
            r.require(key not in choices or choices[key] == choice, 'Conflicting bibliography choices for '+key)
            choices[key] = choice
        bibliography_file = repo.root/bib.BIB
        bibliography_before = bibliography_file.read_bytes() if choices and bibliography_file.exists() else None
        entries = bib.parse(bibliography_before.decode('utf-8-sig')) if bibliography_before is not None else {}
        for original, choice in choices.items():
            r.require(not set(choice)-{'existing_key','new_work','chosen_key','field_updates'}, 'Invalid explicit bibliography choice.')
            current = entries.get(choice.get('existing_key'))
            chosen_works[original] = literature._choose(entries,source.entries[original] if choice.get('new_work') else None,
                existing_key=choice.get('existing_key'),new_work=choice.get('new_work',False),chosen_key=choice.get('chosen_key'),
                field_updates=choice.get('field_updates'),snapshot=(current.kind,current.fields.copy()) if current else None)
        bibliography_pending = {}
        if choices and (bibliography_before is None or bib.parse(bibliography_before.decode('utf-8-sig')) != entries):
            bibliography_pending[bib.BIB] = bib.render(entries).encode('utf8')
        supplied_mapping, qualified_mapping = {}, {}
        for row in mapping:
            r.require(isinstance(row, dict) and set(row) in ({'source','local'}, {'source','local','sender'}),
                      'Supply source/local mapping, with its sender for a foreign-number source context.')
            original = source_refs.parse(row['source'])
            r.require(original is not None, 'Mapping source must be an exact acme-source locator.')
            r.require(not r.paths.in_pdf_store(original['path']), 'Private local literature is outside intake.')
            r.require(not r.paths.in_computation_outputs(original['path']), 'Source outputs have no intake correspondence.')
            local = links.destination('', row['local'])
            r.require(local is not None, 'Mapping destination must be a relative local locator.')
            local_path, local_anchor = local
            r.require(not r.paths.in_computation_outputs(local_path), 'Intake mappings do not install local outputs.')
            r.paths.check_public_target(local_path)
            original_id = names.parse(original['path'])
            # The final target is structurally validated below. Its mathematical
            # correspondence is supplied by the agent; local adaptation has its
            # own kind and physical version, separate from this exact source.
            key = original['repository'], original['path'], original['revision'], original.get('anchor','')
            selected_mapping = qualified_mapping if 'sender' in row else supplied_mapping
            if 'sender' in row: r.require(row['sender'] == source.transport, 'Foreign mapping belongs to this selected sender.')
            else: external.repository(repo, original['repository'])
            destination = local_path, local_anchor
            r.require(key not in selected_mapping or selected_mapping[key] == destination,
                      'Conflicting explicit original mappings.')
            selected_mapping[key] = destination
        for key, local in qualified_mapping.items():
            repository = source.repository_mapping.get(key[0])
            if repository is not None:
                r.require(supplied_mapping.get((repository, *key[1:]), local) == local,
                          'Conflicting explicit original mappings.')
        # Prepare the explicit selections before taking the shared lock;
        # only rechecking and atomic installation hold it.
        import copy
        repo = copy.copy(repo)
        snapshot = _Preparation(repo.root,
                                [chosen_works[item['doc'].identity.source_key] for item in plan if item['doc'].identity.kind == 'U'],
                                metadata=True)
        repo.selected_tree = snapshot
        snapshot.watch('repository/config.json'); snapshot.watch('repository/people.json')
        snapshot.data.update(identity_before)
        snapshot.names.update(identity_before)
        if chosen_works:
            snapshot.data[bib.BIB] = bibliography_before
            if bibliography_before is not None: snapshot.names.add(bib.BIB)
        r.require(snapshot.unchanged(),'Shared intake inputs changed during preparation; retry with current inputs.')
        available = dict(supplied_mapping)
        from ..materials import discovery
        unit_paths = sorted(p for p in snapshot.names if re.fullmatch(
            r'mathematics/audits/literature/[^/]+/[^/]+_U[0-9]+_v[0-9]+\.md', p))
        positions, correspondence = discovery.unit_positions(unit_paths,snapshot.header)
        mapping, pending, metadata = {}, dict(bibliography_pending), []
        planned_families, planned_positions = {}, {}
        for item in plan:
            doc, origin = item['doc'], item['source']
            ident = names.parse(origin['path'])
            established = False
            if ident.kind == 'U':
                source_key = doc.identity.source_key
                key = chosen_works[source_key]
                r.require(key in entries, 'Chosen bibliography changed after preparation; retry with fresh inputs.')
                choice = item['selection'].get('unit')
                number = choice['number']
                prefix = 'mathematics/audits/literature/' + key + '/'
                family = origin['repository'], ident.family
                established = (key, family) in correspondence
                for _, prior in operations(repo):
                    for acquired in prior['items']:
                        if (isinstance(acquired, dict) and acquired.get('kind') == 'U'
                                and isinstance(acquired.get('source'), dict)
                                and acquired['source'].get('repository') == origin['repository']
                                and isinstance(acquired['source'].get('path'), str)
                                and names.parse(acquired['source']['path']).family == ident.family
                                and names.parse(acquired['local']['path']).source_key == key):
                            r.require(names.parse(acquired['local']['path']).number == number,
                                      'Reuse the established receiving position of this original U family.')
                            established = True
                r.require((key, family) not in correspondence or correspondence[(key, family)] == number,
                          'Keep the existing local position of this original U family.')
                r.require((key, number) not in positions or positions[(key, number)] == family,
                          'Conflicting local U position: '+key+f'-U{number:03d}; choose a free explicit position.')
                positions[(key, number)] = family
                correspondence[(key, family)] = number
                exact = (origin['repository'], origin['path'], origin['revision'], origin.get('anchor',''))
                if exact not in available:
                    for acquired, local in _available(repo, {exact[:2]}).items(): available.setdefault(acquired, local)
                known = [(k, v) for k, v in available.items() if k == (origin['repository'], origin['path'], origin['revision'], origin.get('anchor',''))]
                if known:
                    target = known[-1][1][0]
                    r.require(names.parse(target).source_key == key and names.parse(target).number == number,
                              'Explicit U placement conflicts with its exact existing acquisition.')
                else:
                    basename = ident.author + '_' + origin['repository'] + '_U'
                    version = choice.get('version', ident.version)
                    r.require(type(version) is int and version > 0, 'Use a positive receiving U version.')
                    target = prefix + basename + f'{number:03d}_v{version}.md'
                local_anchor = names.parse(target).anchor
            else:
                choice = item['selection'].get('local', {})
                position = choice.get('number')
                r.require(type(position) is int and position > 0, 'Prepare a positive receiving family number for C/T/R/L/J.')
                receiving_repository = choice.get('source_repository', origin['repository'])
                external.person(repo, origin['author'], receiving_repository)
                for _, prior in operations(repo):
                    for acquired in prior['items']:
                        if (isinstance(acquired, dict) and acquired.get('kind') == item['kind']
                                and isinstance(acquired.get('source'), dict)
                                and acquired['source'].get('repository') == origin['repository']
                                and acquired['source'].get('author') == origin['author']
                                and isinstance(acquired['source'].get('path'), str)
                                and names.in_namespace(acquired['source'].get('path', ''), family=ident)
                                and names.parse(acquired['source']['path']).family == ident.family):
                            prior_local = names.parse(acquired['local']['path'])
                            same_scope = acquired['source'].get('anchor', '') == origin.get('anchor', '')
                            same_position = (prior_local.number == position
                                             and prior_local.line == choice.get('line', getattr(ident, 'line', 'A'))
                                             and prior_local.source_repository == receiving_repository)
                            r.require(not same_scope or same_position,
                                      'Reuse the established receiving family for this exact original scope.')
                            established = established or same_position
                version = choice.get('version', ident.version or 1) if item['kind'] in 'CTRL' else ident.version
                r.require(version is None or type(version) is int and version > 0,
                          'Use an actual positive local physical version.')
                local = names.Identity(origin['author'], receiving_repository, item['kind'],
                                       choice.get('line', getattr(ident, 'line', 'A')), position, version)
                target = 'mathematics/' + HOMES[item['kind']] + '/' + local.name + ('/readme.md' if item['kind'] == 'J' else '.md')
                local_anchor = choice.get('anchor', item['anchor'])
            local_ident = names.parse(target)
            family_key = names.namespace(local_ident), origin['repository'], ident.family, origin.get('anchor', '')
            position_key = names.namespace(local_ident), local_ident.number
            r.require(family_key not in planned_families or planned_families[family_key] == local_ident.number,
                      'One original family must retain one receiving position across selected versions.')
            if position_key in planned_positions and planned_positions[position_key] != family_key:
                peers = [other for other in plan if other.get('target') == target]
                r.require(item['selection'].get('prepared') and peers
                          and all(other['source']['author'] == origin['author']
                                  and other['selection'].get('prepared') for other in peers),
                          'A combination needs the same single author and complete prepared receiving text.')
            item['established'] = established or family_key in planned_families
            planned_families[family_key] = local_ident.number
            planned_positions[position_key] = family_key
            item['target'], item['local_anchor'] = target, local_anchor
            mapping[(doc.path, item['anchor'])] = (target, local_anchor)
            if ident.kind == 'C' and item['anchor'] in doc.decisions:
                for role, loc, scope in doc.decisions[item['anchor']].relations:
                    if role == 'statement' and loc.path == doc.path:
                        mapping[(doc.path, loc.anchor)] = (target, loc.anchor)
            # Prepared receiving units retain their actual local anchors;
            # unchanged whole text remains an explicit available choice.
            item['self_anchors'] = links.anchors_text(doc.text)
            if item['selection'].get('prepared'):
                item['prepared_text'] = links.edit_text(doc.text, item['selection']['prepared'], context='intake')
                prepared_header, _ = documents.header_values(item['prepared_text'])
                receiving_author = origin['author'] if item['kind'] in 'CTRLJ' else doc.identity.author
                r.require(prepared_header['author'] in {doc.identity.author, receiving_author},
                          'Prepared intake content must retain its original single human author.')
                r.require(prepared_header.get('source_repository', origin['repository']) in
                          {origin['repository'], local_ident.source_repository},
                          'Prepared intake source association conflicts with the selected original.')
                r.require(prepared_header.get('source_material', origin['path']) == origin['path'],
                          'Prepared intake original path conflicts with the actual selected input.')
            for path in item['files']:
                destination = (target if path == doc.path else item['selection'].get('file_map', {}).get(path,
                               posixpath.dirname(target) + '/' + posixpath.relpath(path, posixpath.dirname(doc.path))))
                r.safe_path(repo.root, destination)
                if path != doc.path:
                    r.require(item['kind'] == 'J' and destination.startswith(posixpath.dirname(target) + '/')
                              and names.parse(destination) == local_ident,
                              'A native-file arrangement stays within its actual receiving J group.')
                mapping[(path, '')] = (destination, '') if ident.kind == 'J' or not item['anchor'] else mapping.get((path, ''), (None, ''))
        planned_paths = {local[0] for local in mapping.values() if local[0]}
        planned_paths.update(item['target'] for item in plan)
        planned_paths.update(batch.pending)
        combined = {target for target in planned_paths if len({(item['source']['repository'], item['source']['path'])
                    for item in plan if item['target'] == target}) > 1}
        navigation_targets = {}
        for item in plan:
            doc, origin, target = item['doc'], item['source'], item['target']
            missing = []
            def rewrite(owner, new_owner, raw, *, local_text=False):
                replacements = []
                for first, last, label, start, end, href in links.markdown_link_details(raw):
                    original_reference = source_refs.parse(href.strip().strip('<>'))
                    destination = links.destination(owner, href)
                    if destination is None and original_reference is None: continue
                    path, anchor = destination if destination is not None else ('', '')
                    if local_text and destination is not None:
                        # Prepared ordinary links already name receiving objects;
                        # only explicit source locators enter source mapping.
                        r.paths.check_public_target(path)
                        navigation_targets.setdefault(new_owner, []).append({'path': path, 'anchor': anchor})
                        relative = posixpath.relpath(path, posixpath.dirname(new_owner)) if path != new_owner else ''
                        value = quote(relative, safe='/._-') + ('#' + quote(anchor, safe='._-') if anchor else '')
                        replacements.append((start, end, value))
                        continue
                    output = original_reference if original_reference is not None else (
                        {'path': path, 'anchor': anchor} if destination is not None else None)
                    if output is not None and r.paths.in_computation_outputs(output['path']):
                        locator = output['path'] + ('#' + output['anchor'] if output['anchor'] else '')
                        context = ('; raw locator `' + href + '`') if original_reference is not None else ''
                        value = (label + ' (source-only output; not acquired; reference in sending repository named `'
                                 + source.config['repository'] + '` at material revision `' + source.revision
                                 + '`; source path `' + locator + '`' + context + ')')
                        replacements.append((first, last, value))
                        continue
                    if destination is not None and path == owner:
                        local_anchor = (item['local_anchor'] if owner == doc.path and anchor == item['anchor'] else anchor)
                        navigation_targets.setdefault(new_owner, []).append({'path': new_owner, 'anchor': local_anchor})
                        replacements.append((start, end, '#' + quote(local_anchor, safe='._-') if local_anchor else ''))
                        continue
                    selected = None
                    explicit = []
                    if original_reference is not None:
                        key = tuple(original_reference[field] for field in ('repository', 'path', 'revision', 'anchor'))
                        if key in qualified_mapping: explicit.append(qualified_mapping[key])
                        if not explicit:
                            whole = qualified_mapping.get((*key[:3], ''))
                            if whole and not whole[1]: selected = (whole[0], key[3])
                        local_repository = source.repository_mapping.get(original_reference['repository'])
                        if local_repository is None:
                            if not explicit and selected is None:
                                value = (label + ' (unacquired foreign source context; raw locator `' + href
                                         + '`; numbering context is the sending repository named `'
                                         + source.config['repository'] + '` at fixed sending revision `'
                                         + source.revision + '`)')
                                replacements.append((first, last, value))
                                missing.append(value)
                                continue
                        else:
                            original_reference = {**original_reference, 'repository': local_repository}
                    reference_origin = original_reference or {'repository': source.transport, 'revision': source.revision, 'path': path, 'anchor': anchor}
                    key = tuple(reference_origin[field] for field in ('repository', 'path', 'revision', 'anchor'))
                    if original_reference is None or local_repository is not None:
                        if key in supplied_mapping:
                            explicit.append(supplied_mapping[key])
                        elif original_reference is not None:
                            whole = supplied_mapping.get((*key[:3], ''))
                            if whole and not whole[1]: selected = (whole[0], key[3])
                    if destination is not None:
                        for chosen in plan:
                            if path == chosen['doc'].path:
                                original = chosen['source']
                                chosen_key = original['repository'], original['path'], original['revision'], anchor
                            elif path in chosen['file_origins']:
                                chosen_key = (*chosen['file_origins'][path][:3], anchor)
                            else: continue
                            if chosen_key in supplied_mapping: explicit.append(supplied_mapping[chosen_key])
                    r.require(not explicit or all(value == explicit[0] for value in explicit),
                              'Conflicting explicit original mappings: ' + href)
                    if explicit: selected = explicit[0]
                    elif destination is not None and selected is None:
                        selected = mapping.get((path, anchor))
                        if selected is None:
                            whole = supplied_mapping.get((*key[:3], ''))
                            if whole and not whole[1]: selected = (whole[0], anchor)
                        if selected is None:
                            whole = mapping.get((path, ''))
                            if whole and whole[0]: selected = (whole[0], anchor)
                    if selected and selected[0]:
                        r.paths.check_public_target(selected[0])
                    private = (original_reference if original_reference is not None and r.paths.in_pdf_store(original_reference['path'])
                               else {'repository': source.transport, 'path': path, 'anchor': anchor}
                               if not local_text and destination is not None and r.paths.in_pdf_store(path) else None)
                    if private:
                        locator = private['path'] + ('#' + private.get('anchor', '') if private.get('anchor') else '')
                        value = (label + ' (source-only local literature; not acquired; reference in sending repository named `'
                                 + source.config['repository'] + '` at material revision `' + source.revision
                                 + '`; source path `' + locator + '`)')
                        replacements.append((first, last, value))
                        missing.append('Unacquired local literature in ' + private['repository'] + ': ' + locator)
                        continue
                    if selected and selected[0]:
                        local_path, local_anchor = selected
                        navigation_targets.setdefault(new_owner, []).append({'path': local_path, 'anchor': local_anchor})
                        relative = posixpath.relpath(local_path, posixpath.dirname(new_owner)) if local_path != new_owner else ''
                        value = quote(relative, safe='/._-') + ('#' + quote(local_anchor, safe='._-') if local_anchor else '')
                    elif destination is not None and path not in source.names:
                        # A material's commit supplies reference context, not
                        # versioned bytes for a file absent from that Git tree.
                        # Do not infer an output role or another source layout.
                        locator = path + ('#' + anchor if anchor else '')
                        value = (label + ' (source-only reference; not acquired; absent from the selected sending Git tree; '
                                 'reference in sending repository named `' + source.config['repository']
                                 + '` at material revision `' + source.revision + '`; source path `' + locator + '`)')
                        replacements.append((first, last, value))
                        missing.append('Source reference absent from selected Git tree; prepare any necessary input or correspondence: '
                                       + source.transport + ': ' + locator)
                        continue
                    else:
                        value = source_refs.make(reference_origin['repository'], reference_origin['revision'], reference_origin['path'], reference_origin.get('anchor', ''))
                        missing.append(value)
                    replacements.append((start, end, value))
                for start, end, value in reversed(replacements): raw = raw[:start] + value + raw[end:]
                return raw
            pairs = []
            for path in item['files']:
                destination = target if path == doc.path else mapping[(path, '')][0]
                raw = prepared[path]
                native_preparation = item['selection'].get('file_preparations', {}).get(path)
                if native_preparation is not None:
                    raw = links.edit_text(raw.decode('utf-8-sig'), native_preparation,
                                          context='selected native input').encode('utf8')
                if path.endswith('.md'):
                    prepared_main = path == doc.path and 'prepared_text' in item
                    prepared_unit = (path == doc.path and doc.identity.kind == 'U'
                                     and any(field in item['selection']['unit'] for field in ('text', 'edits')))
                    final_text = prepared_main or prepared_unit or native_preparation is not None
                    content = (item['prepared_text'] if prepared_main else
                               item['unit_text'] if path == doc.path and doc.identity.kind == 'U'
                               else raw.decode('utf-8-sig'))
                    if path == doc.path and item['kind'] == 'T':
                        from ..materials import tasks
                        tasks.validate_links(destination if final_text else path, content)
                    text = rewrite(destination if final_text else path, destination, content, local_text=final_text)
                    if path == doc.path:
                        body = text.replace('\r\n', '\n').split('\n---\n', 1)[1]
                        header = {'author': origin['author'] if item['kind'] in 'CTRLJ' else doc.identity.author}
                        header['source_repository'] = names.parse(target).source_repository
                        if target not in combined:
                            header['source_material'] = origin['path']
                        text = '---\n' + ''.join(key + ': ' + value + '\n' for key, value in header.items()) + '---\n' + body
                        if item['kind'] == 'T':
                            tasks.validate_links(destination, text)
                    raw = text.encode('utf-8')
                r.require(destination not in pending or pending[destination] == raw, 'Conflicting selected inputs install to one path.')
                pending[destination] = raw
                pair = {'source': path, 'local': destination}
                if doc.identity.kind == 'J':
                    original = item['file_origins'][path]
                    default_path = posixpath.join(posixpath.dirname(origin['path']),
                                                 posixpath.relpath(path, posixpath.dirname(doc.path)))
                    default = origin['repository'], default_path, origin['revision'], ''
                    if original != default:
                        pair['original'] = {'repository': original[0], 'path': original[1], 'revision': original[2]}
                    _file_key({'source': origin, 'local': {'path': target},
                               'files': [{'source': doc.path, 'local': target}]}, pair)
                pairs.append(pair)
            metadata.append({'kind': item['kind'], 'source': origin, 'local': {'path': target, 'anchor': item['local_anchor']},
                             'scope': item['scope'], 'files': pairs,
                             'unmapped_references': sorted(set(missing))})
        # Explicit mappings keep their physical-path checks after Task's
        # prohibition, including when rewriting introduced the forbidden link.
        for local_path, _anchor in (*supplied_mapping.values(), *qualified_mapping.values()):
            if not r.paths.in_pdf_store(local_path):
                r.paths.ordinary_path(repo.root, local_path)
        # Every staged branch is validated against the complete final selected
        # postimage. Batch.commit runs these checks before taking the lock, then
        # rechecks all captured inputs under that lock before any publication.
        def validate(read, view):
            from ..materials.validation import validate_navigation_targets
            for item, planned in zip(metadata, plan):
                document = documents.parse(item['local']['path'], read(item['local']['path']))
                relatives = snapshot.family(document.identity) if document.identity.kind == 'T' else ()
                documents.check(document, read, paths=set(relatives) | set(batch.pending),
                                source_info=lambda doc: material_info(view, doc, read=read))
                check_selection(document, item['local'].get('anchor', ''))
                if item['kind'] == 'J':
                    r.require(not item['local']['anchor'] or links.anchor_occurrences(document.text)[item['local']['anchor']] == 1,
                              'Selected current J scope has no actual local anchor: ' + document.path)
                if item['kind'] == 'R':
                    _require_review_finding(document, item['local']['anchor'])
                if planned['source_review'] is not None:
                    relationships, bindings = _require_review_finding(document, item['local']['anchor'])
                    chosen = documents.Locator(document.path, item['local']['anchor'])
                    r.require(relationships.get(chosen) == planned['source_review'].get('relationship'),
                              'Prepared finding must retain its actual original review relationship, including an undeclared relationship.')
                    r.require(not planned['source_review']['reviewed_targets'] or bindings,
                              'Prepare the actual receiving target bindings for the selected original review scope.')
            for owner, locators in navigation_targets.items():
                batch.guards.append(validate_navigation_targets(repo.root, owner, locators, read, planned=batch.pending))
            validate_operation(view, operation_path, operation, read=read, new_selection=True)
        for path, raw in pending.items():
            if path in bibliography_pending: continue
            target = r.safe_path(repo.root, path)
            original = snapshot.watch(path)
            if original is not None and original != raw:
                owner = next((item for item in plan if path in {pair['local'] for row in metadata if row['local']['path']==item['target'] for pair in row['files']}),None)
                r.require(refresh_j and owner is not None and owner['doc'].identity.kind=='J',
                          'Acquired original collision; fixed U/C/R/L versions cannot be overwritten, and J refresh must be explicit: ' + path)
                humans.require_author(repo, owner['source']['author'], owner['source']['repository'])
                entry, pair = next((row, pair) for row in metadata if row['local']['path'] == owner['target']
                                   for pair in row['files'] if pair['local'] == path)
                _check_j_refresh(repo, owner, path, _file_key(entry, pair))
        operation = {'initiator': initiator, 'recorded_by': recorder,
                     'at': repo.now(), 'instruction': instruction,
                     'transport': {'repository':source.transport, 'revision': revision},
                     'items': metadata, 'outcome': 'obtained selected scope'}
        operation_path = 'intake/' + initiator + '/' + repo.now().replace(':', '').replace('+', 'p') + '-' + uuid.uuid4().hex[:12] + '.json'
        pending[operation_path] = r.encoded(operation)
        for path in pending:
            snapshot.watch(path)
        batch.add(pending, snapshot,
                  reservations=[(names.parse(item['target']), item['established']) for item in plan],
                  validate=validate)
        if not coordinated:
            batch.commit(timeout=timeout)
        return {'operation': operation_path, 'materials': [row['local'] for row in metadata],
                'notices': ['Unmapped original reference: ' + value for row in metadata for value in row['unmapped_references']]}
    finally:
        source.close()
