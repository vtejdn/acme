"""Selected-view readers; acquisition records carry no mathematical adoption."""
from pathlib import PurePosixPath
import re
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
        for _start, _end, href in links.markdown_link_spans(doc.text):
            original = source_refs.parse(href.strip().strip('<>'))
            if original is not None: external.repository(self.repo, original['repository'])
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
                           for p in (self.repo.root / prefix).glob('*_U*_v*.md')))
            discovery.unit_positions([p for p in candidates if p.startswith(prefix)
                                      and PurePosixPath(p).parent == PurePosixPath(path).parent
                                      and re.fullmatch(r'.+_U[0-9]+_v[0-9]+\.md', PurePosixPath(p).name)], self.read)
            documents.source_unit_scope(doc)
        return doc

    def show(self, path):
        """Enrich an explicitly displayed U with its local holding facts."""
        doc = self.check(path)
        if doc.identity.kind == 'U':
            from ..checks import literature
            try:
                registry = self.read(literature.REGISTRY.as_posix())
            except FileNotFoundError:
                registry = None
            doc.source_holding = None
            if registry is not None:
                # Only this receiver's independently recorded local holding is relevant.
                catalog = literature.source_catalog(registry, holding_keys=(doc.identity.source_key,))
                doc.source_holding = literature.holding_status(self.repo.root, registry, doc.identity.source_key,
                                                               catalog=catalog)
                if doc.source_holding:
                    doc.notices = list(dict.fromkeys(getattr(doc, 'notices', []) + doc.source_holding['notices']))
        return doc

    def destination(self, document, href):
        original = source_refs.parse(href)
        if original is not None: external.repository(self.repo, original['repository'])
        return links.destination(document, href)

    def destinations(self, document, body):
        for _, _, href in links.markdown_link_spans(body):
            target = self.destination(document, href)
            if target is not None:
                yield target

    def unavailable(self, document, target, anchor, *, offset=None):
        # Unacquired originals are explicit source URLs; broken local links fail.
        return False
