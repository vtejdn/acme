"""Direct fixed-revision C/R/U/L/J acquisition; operation metadata only."""
from dataclasses import replace
from datetime import datetime
import json
from pathlib import Path, PurePosixPath
import posixpath
import re
from urllib.parse import quote
import uuid

from ..core import repository as r
from ..core import identity as humans
from ..core import links, source_refs, external
from ..materials import documents, identity as names
from . import bibliography as bib

KINDS = {'C', 'R', 'U', 'L', 'J'}
HOMES = {'C': 'claims', 'R': 'audits/reviews', 'L': 'ledger', 'J': 'computations/programs'}


class GitSource:
    def __init__(self, root, revision):
        from ..checks.submission import Tree, git
        r.require(re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', revision or ''), 'Intake requires a full fixed source commit.')
        resolved = git(root, 'rev-parse', '--verify', revision + '^{commit}').decode().strip()
        r.require(resolved == revision, 'Source revision differs from the requested commit.')
        self.tree = Tree(root, revision)
        self.root, self.revision = Path(root).resolve(), revision
        self.names = self.tree.names
        self.config = self.tree.json('repository/config.json')
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
        from types import SimpleNamespace
        return SimpleNamespace(root=self.root, home=self.root/'repository', selected_tree=self.tree)


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


def validate_operation(repo, path, value, *, read=None):
    """Validate recorded facts and original identity, not old scopes in mutable J."""
    parts = PurePosixPath(path).parts
    r.require(len(parts) == 3 and parts[0] == 'intake' and parts[1] == value['initiator'], 'Intake belongs to its actual initiating human.')
    humans.person(repo, value['initiator']); humans.person(repo, value['recorded_by'])
    r.require(datetime.fromisoformat(value['at']).utcoffset() is not None, 'Record an offset-aware acquisition time.')
    r.require(value.get('instruction') and value.get('items'), 'Acquisition needs its actual instruction and selected scope.')
    read = read or (lambda name:r.read_from(repo, name))
    for item in value['items']:
        r.require(item['kind'] in KINDS, 'Only C/R/U/L/J can be acquired.')
        origin = item['source']
        external.repository(repo, origin['repository'])
        external.repository(repo, value['transport']['repository'])
        if item['kind'] in 'CRLJ':
            external.person(repo, origin['author'], origin['repository'], origin['author_name'])
        source_refs.parse(source_refs.make(origin['repository'], origin['revision'], origin['path'], origin.get('anchor', '')))
        local = item['local']
        r.safe_path(repo.root, local['path'])
        raw = read(local['path'])
        doc = documents.parse(local['path'], raw.decode('utf-8-sig') if isinstance(raw,bytes) else raw)
        r.require(doc.identity.kind == item['kind'] and doc.header.get('source_repository') == origin['repository']
                  and doc.header.get('source_material') == origin['path'], 'Acquisition metadata disagrees with the obtained original.')
        if item['kind'] in 'CRLJ':
            r.require(doc.identity.author == origin['author'], 'Acquired author differs from its adopted local source record.')
        r.require(item.get('scope') and (item['kind'] == 'J' or not local.get('anchor')
                  or local['anchor'] in links.anchors_text(doc.text)),
                  'Acquired scope has no actual local anchor or description.')
        if item['kind'] == 'C': r.require(local.get('anchor') in doc.decisions, 'Acquired Claim needs its exact decision.')
        if item['kind'] == 'U': r.require(local.get('anchor') == doc.identity.anchor, 'Acquired U needs its exact unit.')
        if item['kind'] == 'R': _require_review_claim(doc, local.get('anchor', ''))
        for pair in item['files']:
            source_refs.make(value['transport']['repository'],value['transport']['revision'],pair['source'])
            r.safe_path(repo.root,pair['local'])
            r.require(pair['local']==local['path'] or (item['kind']=='J' and pair['local'].startswith(posixpath.dirname(local['path'])+'/')),
                      'Acquired files must belong to the selected typed material or its J group.')
            if item['kind'] != 'J':
                read(pair['local'])
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
        for attachment in item.get('output_attachments', []):
            r.require(item['kind'] == 'J', 'Output attachments belong to an explicitly selected J.')
            _output_path(repo.root, attachment['local'], doc.identity.name)
            r.require(attachment['scope'] and isinstance(attachment['provenance'], dict),
                      'Retain the supplied attachment scope and provenance.')
            r.require('revision' not in attachment['transport'],
                      'An unversioned output attachment has no transport Git revision.')
            r.require(isinstance(attachment['available'], bool), 'Record actual attachment availability.')
    return value


def material_info(repo, document):
    r.require(document.identity.kind in KINDS, 'T/S/D are ordinary original source references, not acquired objects.')
    found = []
    for path, operation in operations(repo):
        for item in operation['items']:
            if not isinstance(item, dict) or not isinstance(item.get('local'), dict) or item['local'].get('path') != document.path:
                continue
            # A requested original validates its own acquired item, not all
            # unrelated objects acquired in the same historical operation.
            validate_operation(repo, path, {**operation, 'items': [item]})
            origin = item['source']
            r.require((origin['repository'], origin['path']) ==
                      (document.header['source_repository'], document.header['source_material']), 'Acquisition original identity disagrees with material header.')
            tree = getattr(repo, 'selected_tree', None)
            attachments = []
            for attachment in item.get('output_attachments', []):
                location = r.safe_path(repo.root, attachment['local'])
                present = (location.is_file() if tree is None or getattr(tree, 'ref', None) == 'WORKTREE'
                           else attachment['local'] in tree.names)
                attachments.append({**attachment, 'present_in_selected_view': present})
            found.append({'operation': path, 'source': origin, 'scope': item['scope'], 'local': item['local'],
                          'source_artifacts': item.get('source_artifacts', []),
                          'output_attachments': attachments,
                          'unmapped_references': item.get('unmapped_references', item.get('missing_inputs', []))})
    r.require(found, 'Imported original lacks its operation provenance: ' + document.path)
    return {'origin': document.header, 'acquisitions': found}


def finding_evidence(repo, locator):
    from ..materials import review
    doc = documents.parse(locator.path, r.read_from(repo, locator.path).decode('utf-8-sig'))
    info = material_info(repo, doc)
    selected = any(row['local'].get('anchor', '') in ('', locator.anchor) for row in info['acquisitions'])
    r.require(selected, 'The selected review finding was not acquired.')
    _require_review_claim(doc, locator.anchor)
    available = {(target.path, target.anchor) for finding, target, scope in review.bindings(doc)
                 if finding == locator and not source_refs.external(target.path)}
    from ..materials.validation import validate_locator_targets
    validate_locator_targets([{'path': path, 'anchor': anchor} for path, anchor in available],
                             lambda path: r.read_from(repo, path))
    return review.relationships(doc).get(locator, 'unknown'), available


def _source_items(source, doc):
    for path in sorted(source.names):
        if re.fullmatch(r'intake/[^/]+/[^/]+\.json', path):
            try: operation = json.loads(source.read(path))
            except json.JSONDecodeError: continue
            if not isinstance(operation, dict) or not isinstance(operation.get('items'), list): continue
            for item in operation.get('items', []):
                if isinstance(item, dict) and isinstance(item.get('local'), dict) and item['local'].get('path') == doc.path:
                    yield datetime.fromisoformat(operation['at']), item


def _file_key(item, pair):
    source, local = item['source'], item['local']
    entrances = [row['source'] for row in item['files'] if row['local'] == local['path']]
    r.require(len(entrances) == 1, 'Acquired J file correspondence lacks its exact group entrance: ' + local['path'])
    entrance = entrances[0]
    original = posixpath.join(posixpath.dirname(source['path']),
                             posixpath.relpath(pair['source'], posixpath.dirname(entrance)))
    return source['repository'], original, source['revision'], ''


def _mapped_author(source, repository, name):
    matches = [row['author'] for row in source.author_mapping
               if row['repository'] == repository and row['name'] == name]
    r.require(len(matches) == 1, 'Supply one adopted original author correspondence: ' + repository + '/' + name)
    external.person(source.receiver, matches[0], repository, name)
    return matches[0]


def _origin(source, doc, anchor=''):
    if not doc.identity.source_repository:
        repository, name = source.transport, doc.identity.author
        origin = {'repository': repository, 'revision': source.revision, 'path': doc.path, 'anchor': anchor}
    else:
        matches = []
        for at, item in _source_items(source, doc):
            r.require((item['source']['repository'], item['source']['path']) ==
                      (doc.header['source_repository'], doc.header['source_material']),
                      'Onward provenance conflicts with the original header.')
            local_anchor = item['local'].get('anchor', '')
            if local_anchor in ('', anchor): matches.append((at, item['source']))
            elif doc.identity.kind == 'C' and local_anchor in doc.decisions:
                if any(role == 'statement' and loc == documents.Locator(doc.path, anchor)
                       for role, loc, scope in doc.decisions[local_anchor].relations):
                    matches.append((at, {**item['source'], 'anchor': anchor}))
        r.require(matches, 'Onward transfer lacks the original acquired revision/scope: ' + doc.path)
        origin = max(matches, key=lambda row: row[0])[1].copy()
        foreign = origin['repository']
        external.repository(source.source_view(), foreign)
        r.require(foreign in source.repository_mapping, 'Map the selected original repository from its sender namespace: ' + foreign)
        repository = source.repository_mapping[foreign]
        external.repository(source.receiver, repository)
        name = origin['author_name']
        if doc.identity.kind in 'CRLJ':
            r.require(origin['author'] == doc.identity.author, 'Onward original author conflicts with the material header.')
            external.person(source.source_view(), origin['author'], foreign, name)
        origin['repository'] = repository
    origin['author_name'] = name
    if doc.identity.kind in 'CRLJ': origin['author'] = _mapped_author(source, repository, name)
    if anchor and not origin.get('anchor'): origin['anchor'] = anchor
    return origin


def _require_review_claim(doc, anchor):
    from ..materials import review
    targets = []
    for finding, target, _ in review.bindings(doc):
        if finding.anchor != anchor: continue
        origin = source_refs.parse(target.path)
        path = origin['path'] if origin else target.path
        if names.parse(path).kind == 'C': targets.append(target)
    r.require(targets and all(not source_refs.external(target.path) for target in targets),
              'Selected R finding requires its exact fixed C target acquired first or in this operation.')


def manifest(source, selections, *, files=()):
    r.require(selections, 'Select at least one C/R/U/L/J object and its actual scope.')
    result = []
    for selection in selections:
        path, anchor = selection['path'], selection.get('anchor', '')
        item = names.parse(path)
        r.require(item.kind in KINDS, 'T/S/D and manuscript projects are outside intake, including related inputs.')
        r.require(path in source.names, 'Selected source file is unavailable: ' + path)
        raw = source.read(path).decode('utf-8-sig')
        doc = documents.parse(path, raw)
        if item.kind in {'R', 'L'}:
            from ..materials import review
            review.relationships(doc)
            review.bindings(doc)
        r.require(not anchor or anchor in links.anchors_text(raw), 'Selected source anchor is absent.')
        r.require(item.kind != 'C' or anchor in doc.decisions, 'Select the exact Claim assessment decision.')
        r.require(item.kind != 'U' or anchor == item.anchor, 'Select the exact source unit anchor.')
        r.require(selection.get('scope'), 'Describe the actual selected mathematical scope.')
        r.require(item.kind == 'J' or not selection.get('output_attachments'),
                  'Select output attachments with their actual J object.')
        r.require(item.kind != 'J' or PurePosixPath(path).name == 'readme.md', 'Select the J group README and explicit indispensable files.')
        owned = [path]
        if item.kind == 'J':
            prefix = posixpath.dirname(path) + '/'
            owned += [name for name in files if name.startswith(prefix) and name != path]
        origin = _origin(source, doc, anchor)
        if item.kind == 'J' and doc.identity.source_repository:
            # Omitted inputs keep their prior acquisition; a group refresh does
            # not attribute every file still present to the newer revision.
            acquired_files = {}
            for at, acquired in sorted(_source_items(source, doc), key=lambda row: row[0]):
                for pair in acquired['files']:
                    acquired_files[pair['local']] = _file_key(acquired, pair)
            for name in owned:
                original = acquired_files.get(name)
                r.require(original is not None and source.repository_mapping.get(original[0]) == origin['repository']
                          and original[2] == origin['revision'],
                          'J file was not acquired at the selected original revision '
                          + origin['revision'] + ': ' + name)
        result.append({'doc': doc, 'source': origin, 'scope': selection['scope'],
                       'anchor': anchor, 'files': owned, 'selection': selection})
    owned = {path for item in result for path in item['files']}
    r.require(set(files) <= owned, 'Explicit files must belong to a selected J group; select C/R/U/L separately.')
    for path in owned:
        r.require(path in source.names, 'Required J input is absent: ' + path)
        r.safe_path(source.root, path)
    return sorted(result, key=lambda item: item['doc'].identity.kind == 'R')


def _output_path(root, path, group):
    """Check one explicitly associated output, without discovering siblings."""
    target = r.safe_path(root, path)
    prefix = r.paths.COMPUTATION_OUTPUT_ROOT.as_posix() + '/' + group + '/'
    r.require(path.startswith(prefix) and len(path) > len(prefix),
              'Select an actual file under the associated J output home: ' + prefix)
    r.require(not target.exists() or target.is_file(), 'Output attachment must be a file: ' + path)
    return target


def _prepare_outputs(source, plan):
    """Read supplied local files; no commit, filename or prior intake authenticates them."""
    prepared = []
    for item in plan:
        item['output_attachments'] = []
        for selection in item['selection'].get('output_attachments', []):
            r.require(isinstance(selection, dict) and
                      set(selection) == {'source', 'local', 'scope', 'provenance'},
                      'Supply source/local output paths, actual scope and provenance.')
            r.require(isinstance(selection['scope'], str) and selection['scope'].strip(),
                      'Describe the selected output scope.')
            provenance = selection['provenance']
            r.require(isinstance(provenance, dict) and isinstance(provenance.get('generation'), str)
                      and provenance['generation'].strip(),
                      'State the known generation facts or explicitly unknown generation.')
            candidate = _output_path(source.root, selection['source'], item['doc'].identity.name)
            raw = candidate.read_bytes() if candidate.is_file() else None
            attachment = {'transport': {'repository': source.transport, 'path': selection['source']},
                          'local': selection['local'], 'scope': selection['scope'],
                          'provenance': provenance, 'available': raw is not None}
            item['output_attachments'].append(attachment)
            prepared.append((candidate, raw))
            attachment['_raw'] = raw
    return prepared


def _available(repo):
    result = {}
    ordered = []
    for _, operation in operations(repo):
        try:
            at = datetime.fromisoformat(operation['at'])
            if at.utcoffset() is not None: ordered.append((at, operation))
        except (KeyError, TypeError, ValueError): continue
    for _, operation in sorted(ordered,key=lambda row:row[0]):
        for item in operation['items']:
            if (not isinstance(item, dict) or item.get('kind') not in KINDS or
                    not isinstance(item.get('source'), dict) or not isinstance(item.get('local'), dict) or
                    not isinstance(item.get('files'), list)): continue
            source, local = item['source'], item['local']
            if not all(isinstance(source.get(field), str) for field in ('repository','path','revision')) or not isinstance(local.get('path'), str): continue
            if not all(isinstance(pair, dict) and isinstance(pair.get('source'), str) and isinstance(pair.get('local'), str)
                       for pair in item['files']): continue
            if not any(pair['local'] == local['path'] for pair in item['files']): continue
            if item.get('kind') == 'J':
                # Replace provenance only for files actually acquired again.
                # Retained inputs keep their old revision, never the group's new one.
                for pair in item['files']:
                    key = _file_key(item, pair)
                    result = {old:value for old,value in result.items() if old[:2] != key[:2]}
                    if not r.safe_path(repo.root, pair['local']).is_file(): continue
                    result[key] = (pair['local'], '')
            key = source['repository'], source['path'], source['revision'], source.get('anchor', '')
            result[key] = (local['path'], local.get('anchor', ''))
    return result


def _declared_input(repo, original, available):
    """Resolve exact provenance or an explicit statement of that same C decision."""
    key = original['repository'], original['path'], original['revision'], original.get('anchor', '')
    if key in available: return available[key]
    for acquired, local in available.items():
        if acquired[:3] != key[:3]: continue
        path, anchor = local
        if not path or names.parse(path).kind != 'C': continue
        tree = getattr(repo, 'selected_tree', None)
        if hasattr(tree, 'watch'): tree.watch(path)
        try: doc = documents.parse(path, r.read_from(repo, path).decode('utf-8-sig'))
        except FileNotFoundError: continue
        decision = doc.decisions.get(anchor)
        if decision and any(role == 'statement' and locator == documents.Locator(path,key[3])
                            for role, locator, scope in decision.relations):
            material_info(repo, doc)
            return path, key[3]
    return None


def _check_j_refresh(repo, item, path):
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
        original_path = posixpath.join(posixpath.dirname(incoming['path']),
                                      posixpath.relpath(path, posixpath.dirname(entrance)))
        r.require(any(_file_key(acquired, pair)[:2] == (incoming['repository'], original_path)
                      for _, operation in operations(repo) for acquired in operation['items']
                      if isinstance(acquired, dict) and isinstance(acquired.get('local'), dict)
                      and acquired['local'].get('path') == entrance
                      for pair in acquired['files'] if pair['local'] == path),
                  'Occupied J native file lacks its acquired original correspondence: ' + path)


def _unit_text(raw, choice):
    """Apply only agent-designated original offsets, or supplied final local text."""
    r.require(isinstance(choice, dict) and not set(choice)-{'number','edits','text'},
              'Supply the explicit receiving unit number and designated edits or final text.')
    r.require(type(choice.get('number')) is int and choice['number'] > 0,
              'Supply a positive explicit receiving unit number.')
    return links.edit_text(raw, {key:value for key,value in choice.items() if key != 'number'}, context='unit')


class _Preparation:
    """Capture only read inputs; recheck them at shared publication."""
    def __init__(self, root, unit_keys=()):
        self.root, self.data, self.headers = root, {}, {}
        self.unit_keys = tuple(unit_keys)
        self.names = self.inventory()
        self.shared_names = set(self.names)

    def inventory(self):
        # Only metadata and selected U allocation directories participate in
        # this short publication snapshot; unrelated repository paths are not
        # traversed or validated as intake prerequisites.
        selected = set()
        for relative in ['intake'] + ['mathematics/audits/literature/'+key for key in self.unit_keys]:
            folder = r.safe_path(self.root, relative)
            if not folder.is_dir(): continue
            files, errors = r.paths.repository_files(folder, suffix=None)
            r.require(not errors, '; '.join(errors))
            selected.update(path.relative_to(self.root).as_posix() for path in files)
        return selected

    def watch(self, path):
        if path not in self.data:
            from .literature import target_path
            target = target_path(self.root,path)
            self.data[path] = target.read_bytes() if target.exists() else None
            if self.data[path] is not None: self.names.add(path)
        return self.data[path]

    def bytes(self, path):
        raw = self.watch(path)
        if raw is None: raise FileNotFoundError(path)
        return raw

    def unchanged(self):
        if self.inventory() != self.shared_names: return False
        from .literature import target_path
        from ..materials import discovery
        return all(discovery.unit_header(self.root,p) == raw for p,raw in self.headers.items()) and all((target_path(self.root,p).read_bytes() if target_path(self.root,p).exists() else None) == raw
                   for p, raw in self.data.items())

    def header(self, path):
        from ..materials import discovery
        if path not in self.headers: self.headers[path] = discovery.unit_header(self.root,path)
        return self.headers[path]


def acquire(repo, source_root, selections, *, revision, instruction, source_repository, correspondence,
            initiator=None, files=(), timeout=30, refresh_j=False, mapping=()):
    nonempty = lambda value: isinstance(value, str) and bool(value.strip())
    r.require(nonempty(instruction), 'Record the actual intake instruction.')
    for selection in selections:
        r.require(not selection.get('returning_original'), 'This repository does not reacquire its own returning originals.')
        retired = {'source_artifacts', 'source_bibliography', 'holding', 'source_updates'} & selection.keys()
        r.require(not retired, 'Private local literature is outside intake; retired inputs: ' + ', '.join(sorted(retired)))
    for path in files:
        r.require(not r.paths.in_pdf_store(path), 'Private local literature is outside intake.')
    recorder = repo.actor(); initiator = initiator or recorder
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
        output_inputs = _prepare_outputs(source, plan)
        from . import literature
        chosen_works, choices = {}, {}
        for item in plan:
            if item['doc'].identity.kind != 'U': continue
            key = item['doc'].identity.source_key
            r.require(key in source.entries, 'A source unit needs its supplied bibliography entry.')
            choice = item['selection'].get('bibliography')
            r.require(isinstance(choice, dict), 'Supply the chosen existing/new bibliography for each U.')
            item['unit_text'] = _unit_text(prepared[item['doc'].path].decode('utf-8-sig'), item['selection'].get('unit'))
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
            local_path, separator, local_anchor = row['local'].partition('#')
            r.safe_path(repo.root, local_path)
            key = original['repository'], original['path'], original['revision'], original.get('anchor','')
            selected_mapping = qualified_mapping if 'sender' in row else supplied_mapping
            if 'sender' in row: r.require(row['sender'] == source.transport, 'Foreign mapping belongs to this selected sender.')
            else: external.repository(repo, original['repository'])
            r.require(key not in selected_mapping, 'Duplicate explicit original mapping.')
            selected_mapping[key] = (local_path, local_anchor if separator else '')
        # Prepare the explicit selections before taking the shared lock;
        # only rechecking and atomic installation hold it.
        import copy
        repo = copy.copy(repo)
        snapshot = _Preparation(repo.root,
                                [chosen_works[item['doc'].identity.source_key] for item in plan if item['doc'].identity.kind == 'U'])
        repo.selected_tree = snapshot
        snapshot.watch('repository/config.json'); snapshot.watch('repository/people.json')
        snapshot.data.update(identity_before)
        snapshot.names.update(identity_before)
        if chosen_works:
            snapshot.data[bib.BIB] = bibliography_before
            if bibliography_before is not None: snapshot.names.add(bib.BIB)
        r.require(snapshot.unchanged(),'Shared intake inputs changed during preparation; retry with current inputs.')
        available = _available(repo)
        available.update(supplied_mapping)
        from ..materials import discovery
        unit_paths = sorted(p for p in snapshot.names if re.fullmatch(
            r'mathematics/audits/literature/[^/]+/[^/]+_U[0-9]+_v[0-9]+\.md', p))
        positions, correspondence = discovery.unit_positions(unit_paths,snapshot.header)
        mapping, pending, metadata = {}, dict(bibliography_pending), []
        for item in plan:
            doc, origin = item['doc'], item['source']
            ident = names.parse(origin['path'])
            if ident.kind == 'U':
                source_key = doc.identity.source_key
                r.require(source_key in source.entries, 'A source unit needs its complete canonical bibliography entry.')
                key = chosen_works[source_key]
                r.require(key in entries, 'Chosen bibliography changed after preparation; retry with fresh inputs.')
                choice = item['selection'].get('unit')
                number = choice['number']
                prefix = 'mathematics/audits/literature/' + key + '/'
                family = origin['repository'], ident.family
                r.require((key, family) not in correspondence or correspondence[(key, family)] == number,
                          'Keep the existing local position of this original U family.')
                r.require((key, number) not in positions or positions[(key, number)] == family,
                          'Conflicting local U position: '+key+f'-U{number:03d}; choose a free explicit position.')
                positions[(key, number)] = family
                correspondence[(key, family)] = number
                known = [(k, v) for k, v in available.items() if k == (origin['repository'], origin['path'], origin['revision'], origin.get('anchor',''))]
                if known:
                    target = known[-1][1][0]
                    r.require(names.parse(target).source_key == key and names.parse(target).number == number,
                              'Explicit U placement conflicts with its exact existing acquisition.')
                else:
                    basename = ident.author + '_' + origin['repository'] + '_U'
                    target = prefix + basename + f'{number:03d}_v{ident.version}.md'
                local_anchor = names.parse(target).anchor
            else:
                position = item['selection'].get('local', {}).get('number')
                r.require(type(position) is int and position > 0, 'Prepare a positive receiving family number for C/R/L/J.')
                for _, prior in operations(repo):
                    for acquired in prior['items']:
                        if (isinstance(acquired, dict) and acquired.get('kind') == ident.kind
                                and acquired['source']['repository'] == origin['repository']
                                and acquired['source'].get('author') == origin['author']
                                and names.parse(acquired['source']['path']).family == ident.family):
                            r.require(names.parse(acquired['local']['path']).number == position,
                                      'Reuse the established receiving family number for this original.')
                local = replace(ident, author=origin['author'], source_repository=origin['repository'], number=position)
                target = 'mathematics/' + HOMES[ident.kind] + '/' + local.name + ('/readme.md' if ident.kind == 'J' else '.md')
                local_anchor = item['anchor']
            item['target'], item['local_anchor'] = target, local_anchor
            mapping[(doc.path, item['anchor'])] = (target, local_anchor)
            if ident.kind == 'C':
                for role, loc, scope in doc.decisions[item['anchor']].relations:
                    if role == 'statement' and loc.path == doc.path:
                        mapping[(doc.path, loc.anchor)] = (target, loc.anchor)
            # A selected fixed document is authentic and whole; same-document
            # internal references keep their actual retained anchors.
            item['self_anchors'] = links.anchors_text(doc.text)
            for path in item['files']:
                destination = target if path == doc.path else posixpath.dirname(target) + '/' + posixpath.relpath(path, posixpath.dirname(doc.path))
                mapping[(path, '')] = (destination, '') if ident.kind == 'J' or not item['anchor'] else mapping.get((path, ''), (None, ''))
            for attachment in item['output_attachments']:
                destination = attachment['local']
                _output_path(repo.root, destination, names.parse(target).name)
                source_path = attachment['transport']['path']
                r.require((source_path, '') not in mapping or mapping[(source_path, '')] == (destination, ''),
                          'Conflicting output destinations for the same selected source file.')
                mapping[(source_path, '')] = (destination, '')
        for item in plan:
            origin, doc = item['source'], item['doc']
            for (path, anchor), local in mapping.items():
                if path == doc.path and local[0]:
                    available[(origin['repository'], origin['path'], origin['revision'], anchor)] = local
        prepared_targets = {item['target'] for item in plan}
        planned_paths = {local[0] for local in mapping.values() if local[0]}
        for item in plan:
            doc, origin, target = item['doc'], item['source'], item['target']
            missing = []
            def rewrite(owner, new_owner, raw):
                replacements = []
                for first, last, label, start, end, href in links.markdown_link_details(raw):
                    original_reference = source_refs.parse(href.strip().strip('<>'))
                    destination = links.destination(owner, href)
                    if destination is None and original_reference is None: continue
                    path, anchor = destination if destination is not None else ('', '')
                    selected = (mapping.get((path, anchor)) or mapping.get((path, ''))) if destination is not None else None
                    if original_reference is not None:
                        key = tuple(original_reference[field] for field in ('repository', 'path', 'revision', 'anchor'))
                        selected = qualified_mapping.get(key)
                        if selected is None:
                            local_repository = source.repository_mapping.get(original_reference['repository'])
                            if local_repository is None:
                                value = (label + ' (unacquired foreign source context; raw locator `' + href
                                         + '`; numbering context is the sending repository named `'
                                         + source.config['repository'] + '` at fixed sending revision `'
                                         + source.revision + '`)')
                                replacements.append((first, last, value))
                                missing.append(value)
                                continue
                            original_reference = {**original_reference, 'repository': local_repository}
                    private = (original_reference if original_reference is not None and r.paths.in_pdf_store(original_reference['path'])
                               else {'repository': source.transport, 'path': path, 'anchor': anchor}
                               if destination is not None and r.paths.in_pdf_store(path) else None)
                    if private:
                        locator = private['path'] + ('#' + private.get('anchor', '') if private.get('anchor') else '')
                        value = (label + ' (source-only local literature; not acquired; reference in sending repository named `'
                                 + source.config['repository'] + '` at material revision `' + source.revision
                                 + '`; source path `' + locator + '`)')
                        replacements.append((first, last, value))
                        missing.append('Unacquired local literature in ' + private['repository'] + ': ' + locator)
                        continue
                    if destination is not None and owner == doc.path and path == owner:
                        selected = (target, item['local_anchor'] if anchor == item['anchor'] else anchor)
                    if selected and selected[0]:
                        local_path, local_anchor = selected
                        if local_path not in planned_paths:
                            snapshot.watch(local_path)
                            data = r.read_from(repo, local_path)
                            r.require(not local_anchor or local_anchor in links.anchors_text(data.decode('utf-8-sig')),
                                      'Explicit mapped current anchor is missing: ' + local_path)
                        relative = posixpath.relpath(local_path, posixpath.dirname(new_owner)) if local_path != new_owner else ''
                        value = quote(relative, safe='/._-') + ('#' + quote(local_anchor, safe='._-') if local_anchor else '')
                    elif destination is not None and r.paths.in_computation_outputs(path):
                        # The reference context identifies a locator, not acquired
                        # bytes or a correspondence with any receiver-local slot.
                        locator = path + ('#' + anchor if anchor else '')
                        value = (label + ' (source-only unversioned output; not acquired; '
                                 'reference in sending repository named `' + source.config['repository']
                                 + '` at material revision `' + source.revision + '`; source path `' + locator + '`)')
                        replacements.append((first, last, value))
                        missing.append('Unselected unversioned output in ' + source.transport + ': ' + locator)
                        continue
                    else:
                        reference_origin = original_reference or {'repository': source.transport, 'revision': source.revision, 'path': path, 'anchor': anchor}
                        acquired = _declared_input(repo, reference_origin, available)
                        if acquired:
                            local_path, local_anchor = acquired
                            if local_path not in prepared_targets:
                                snapshot.watch(local_path)
                                r.require((repo.root/local_path).is_file(), 'Previously acquired local input is missing: ' + local_path)
                                r.require(not local_anchor or local_anchor in links.anchors_text(r.read_from(repo, local_path).decode('utf-8-sig')),
                                          'Previously acquired exact scope is missing: ' + local_path + '#' + local_anchor)
                            value = quote(posixpath.relpath(local_path, posixpath.dirname(new_owner)), safe='/._-') + ('#' + quote(local_anchor, safe='._-') if local_anchor else '')
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
                if path.endswith('.md'):
                    text = rewrite(path, destination, item['unit_text'] if path == doc.path and doc.identity.kind == 'U'
                                   else raw.decode('utf-8-sig'))
                    if path == doc.path:
                        body = text.replace('\r\n', '\n').split('\n---\n', 1)[1]
                        header = {'author': origin['author'] if doc.identity.kind in 'CRLJ' else doc.identity.author}
                        if doc.header.get('framework'): header['framework'] = doc.header['framework']
                        header.update(source_repository=origin['repository'], source_material=origin['path'])
                        text = '---\n' + ''.join(key + ': ' + value + '\n' for key, value in header.items()) + '---\n' + body
                    raw = text.encode('utf-8')
                r.require(destination not in pending or pending[destination] == raw, 'Conflicting selected inputs install to one path.')
                pending[destination] = raw
                pairs.append({'source': path, 'local': destination})
            for attachment in item['output_attachments']:
                destination, raw = attachment['local'], attachment.pop('_raw')
                existing = snapshot.watch(destination)
                r.require(existing is None or (raw is not None and existing == raw),
                          'Output attachment destination is occupied by different or unavailable source bytes: ' + destination)
                r.require(destination not in pending or pending[destination] == raw,
                          'Conflicting output attachments install to one destination.')
                if raw is not None: pending[destination] = raw
            metadata.append({'kind': doc.identity.kind, 'source': origin, 'local': {'path': target, 'anchor': item['local_anchor']},
                             'scope': item['scope'], 'files': pairs,
                             'output_attachments': item['output_attachments'],
                             'unmapped_references': sorted(set(missing))})
        # Validate every prepared document against the final selected local bytes.
        def read(path):
            raw = pending[path] if path in pending else r.read_from(repo, path)
            return raw.decode('utf-8-sig') if path.endswith('.md') else raw
        for item in metadata:
            document = documents.parse(item['local']['path'], read(item['local']['path']))
            documents.check(document, read)
            if item['kind'] == 'J':
                r.require(not item['local']['anchor'] or item['local']['anchor'] in links.anchors_text(document.text),
                          'Selected current J scope has no actual local anchor: ' + document.path)
            if item['kind'] == 'R': _require_review_claim(document, item['local']['anchor'])
        for path, raw in pending.items():
            if path in bibliography_pending: continue
            target = r.safe_path(repo.root, path)
            original = snapshot.watch(path)
            if original is not None and original != raw:
                owner = next((item for item in plan if path in {pair['local'] for row in metadata if row['local']['path']==item['target'] for pair in row['files']}),None)
                r.require(refresh_j and owner is not None and owner['doc'].identity.kind=='J',
                          'Acquired original collision; fixed U/C/R/L versions cannot be overwritten, and J refresh must be explicit: ' + path)
                _check_j_refresh(repo, owner, path)
        operation = {'initiator': initiator, 'recorded_by': recorder,
                     'at': datetime.now(r.zone(repo.config['timezone'])).isoformat(timespec='microseconds'), 'instruction': instruction,
                     'transport': {'repository':source.transport, 'revision': revision},
                     'items': metadata, 'outcome': ('obtained available scope; selected output unavailable'
                         if any(not output['available'] for item in metadata for output in item['output_attachments'])
                         else 'obtained selected scope')}
        operation_path = 'intake/' + initiator + '/' + repo.now().replace(':', '').replace('+', 'p') + '-' + uuid.uuid4().hex[:12] + '.json'
        validate_operation(repo, operation_path, operation, read=read)
        with r.locked(repo.root, timeout=timeout):
            r.require(snapshot.unchanged(), 'Shared intake inputs changed during preparation; retry with current inputs.')
            for candidate, raw in output_inputs:
                # Recheck only the actual explicit source file and its containment.
                r.safe_path(source.root, candidate.relative_to(source.root).as_posix())
                r.require((candidate.read_bytes() if candidate.is_file() else None) == raw,
                          'Selected output attachment changed during preparation; retry with current facts.')
            pending[operation_path] = r.encoded(operation)
            for path in pending: snapshot.watch(path)
            literature.publish_files(repo,pending,{path:snapshot.data[path] for path in pending})
            return {'operation': operation_path, 'materials': [row['local'] for row in metadata],
                    'notices': ['Unmapped original reference: ' + value for row in metadata for value in row['unmapped_references']] +
                               ['Selected output unavailable: ' + output['transport']['path']
                                for row in metadata for output in row['output_attachments'] if not output['available']]}
    finally:
        source.close()
