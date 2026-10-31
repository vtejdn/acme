"""Selected-view readers; acquisition records carry no mathematical adoption."""
from pathlib import PurePosixPath
from . import documents
from . import identity
from ..core import repository as shared
from ..core import identity as humans
from ..core import links
from ..core import paths
from ..core import source_refs, external


def entrances(names, *, strict=True):
    result = []
    for path in sorted(names):
        if paths.in_computation_outputs(path):
            continue
        if not path.startswith('mathematics/') or not path.lower().endswith('.md'):
            continue
        item = identity.candidate(path)
        if item is None: continue
        if item['kind'] == 'J' and PurePosixPath(path).name != 'readme.md': continue
        if strict: identity.parse(path)
        result.append(path)
    return result


def validate_inputs(repo, doc, read):
    if doc.identity.kind not in 'CT' or doc.current is None:
        return
    selected = documents.selected(doc, read)
    for role, loc, scope in selected.relations:
        if source_refs.external(loc.path):
            shared.require(bool(doc.identity.source_repository), 'Required input has not been acquired: ' + loc.path)
            continue
        from .validation import validate_locator_targets
        validate_locator_targets([vars(loc)], read)


class Reader:
    def __init__(self, repo, *, parents=None):
        self.repo = repo
        self.loaded = {}
        self.cache = {}

    def read(self, path):
        if source_refs.external(path):
            raise FileNotFoundError('Source reference is outside acquired local scope: ' + path)
        if path not in self.cache:
            tree = getattr(self.repo, 'selected_tree', None)
            if paths.in_computation_outputs(path) and tree is not None:
                if getattr(tree, 'ref', None) == 'WORKTREE':
                    data = shared.safe_path(self.repo.root, path).read_bytes()
                elif path not in tree.names:
                    raise FileNotFoundError('Local computation output is absent from the selected Git view: ' + path)
                else:
                    data = shared.read_from(self.repo, path)
            else:
                data = shared.read_from(self.repo, path)
            self.cache[path] = data.decode('utf-8-sig') if path.lower().endswith('.md') else data
        return self.cache[path]

    def document(self, path):
        paths.check_public_target(path)
        if path not in self.loaded:
            self.loaded[path] = documents.parse(path, self.read(path))
        return self.loaded[path]

    def source_info(self, document):
        from ..intake import acquire
        return acquire.material_info(self.repo, document)

    def check(self, path):
        doc = self.document(path)
        shared.require(doc.identity.kind != 'L' or PurePosixPath(path).parts[:2] == ('mathematics', 'ledger'), 'All L material belongs in mathematics/ledger/.')
        acquired = None
        if doc.identity.source_repository:
            acquired = self.source_info(doc)
        else:
            humans.person(self.repo, doc.identity.author)
        route_paths = ()
        if doc.identity.kind in 'ST':
            tree = getattr(self.repo, 'selected_tree', None)
            if tree is None:
                from . import discovery
                route_paths = discovery.candidates(self.repo.root)
            else:
                route_paths = entrances(tree.names, strict=False)
        documents.check(doc, self.read, paths=route_paths, source_info=self.source_info)
        if doc.identity.kind == 'U':
            from . import discovery
            prefix = str(PurePosixPath(path).parent) + '/'
            tree = getattr(self.repo, 'selected_tree', None)
            candidates = (tree.names if tree is not None else
                          (p.relative_to(self.repo.root).as_posix()
                           for p in (self.repo.root / prefix).glob('*.md')))
            def header(name):
                if name == path: return doc.text
                if tree is None:
                    return discovery.unit_header(self.repo.root, name)
                return tree.header(name)
            discovery.unit_positions([p for p in candidates if discovery.unit_namespace(p, doc.identity)], header)
        return doc

    def show(self, path):
        """Display selected shared material without querying local originals."""
        return self.check(path)

    def destination(self, document, href, *, mapping=()):
        """Decode one supplied address, optionally applying its exact correspondence."""
        original = source_refs.parse(links.destination_text(href))
        chosen = []
        if original is not None:
            external.repository(self.repo, original['repository'])
            for row in mapping:
                shared.require(isinstance(row, dict) and set(row) == {'source', 'local'},
                               'Use explicit source/local address correspondence.')
                shared.require(all(isinstance(row[key], str) and row[key] for key in row),
                               'Address correspondence needs nonempty source and local strings.')
                candidate = source_refs.parse(row['source'])
                shared.require(candidate is not None, 'Correspondence source needs an exact acme-source address.')
                if candidate == original:
                    chosen.append(row['local'])
            shared.require(not chosen or all(value == chosen[0] for value in chosen),
                           'Conflicting explicit address correspondence.')
            if chosen:
                href = chosen[0]
        target = links.destination(document, href)
        shared.require(not chosen or target is not None, 'Correspondence destination needs a relative local locator.')
        if target is not None:
            paths.check_local_role(target[0])
            paths.check_public_target(target[0])
        return target
