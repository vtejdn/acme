"""Captured inputs and short, reversible publication of explicitly prepared files.

This module has no intake, import-history or mathematical-decision semantics.
Callers judge the contents and supply validation and allocation scope explicitly.
"""
import copy
from . import repository as r


def publish_files(repo, pending, expected, *, locate=None):
    # The default locator enforces ordinary repository storage. A caller with
    # a declared source mount supplies its own checked locator for every I/O.
    storage_root = repo.root if locate is None else None
    locate = locate or r.safe_path
    for name, old in expected.items():
        target = locate(repo.root, name)
        r.require((target.read_bytes() if target.exists() else None) == old,
                  'Selected input changed during preparation: ' + name)
    written = []
    try:
        for name, raw in pending.items():
            target = locate(repo.root, name)
            old = expected[name]
            if old == raw:
                continue
            r.write_bytes(target, raw, exclusive=old is None, root=storage_root)
            written.append(name)
    except BaseException as error:
        competing = []
        for name in reversed(written):
            target = locate(repo.root, name)
            # A competing replacement is not owned by this publication.
            if not target.exists() or target.read_bytes() != pending[name]:
                competing.append(name)
                continue
            if expected[name] is None:
                r.unlink(target, root=storage_root)
            else:
                r.write_bytes(target, expected[name], root=storage_root)
        if competing:
            raise r.ResearchError('Publication failed; competing content preserved during rollback: '
                                  + ', '.join(competing)) from error
        raise


class Preparation:
    """Watch actual inputs and explicitly selected allocation namespaces."""
    def __init__(self, root, unit_keys=(), *, metadata=False):
        self.root, self.data, self.headers = root, {}, {}
        self.metadata = metadata
        self.unit_keys = tuple(unit_keys)
        self.names = self.inventory()
        self.shared_names = set(self.names)
        self.families = {}

    def inventory(self):
        selected = set()
        for relative in (['intake'] if self.metadata else []) + ['mathematics/audits/literature/' + key for key in self.unit_keys]:
            folder = r.safe_path(self.root, relative)
            if not folder.is_dir():
                continue
            files, errors = r.paths.repository_files(folder, suffix=None)
            r.require(not errors, '; '.join(errors))
            selected.update(path.relative_to(self.root).as_posix() for path in files)
        return selected

    def watch(self, path):
        if path not in self.data:
            target = r.safe_path(self.root, path)
            self.data[path] = target.read_bytes() if target.exists() else None
            if self.data[path] is not None:
                self.names.add(path)
        return self.data[path]

    def bytes(self, path):
        raw = self.watch(path)
        if raw is None:
            raise FileNotFoundError(path)
        return raw

    def header(self, path):
        from ..materials import discovery
        if path not in self.headers:
            self.headers[path] = discovery.unit_header(self.root, path)
        return self.headers[path]

    def family(self, ident):
        from ..materials import discovery
        selected = set(discovery.selected(discovery.candidates(self.root), family=ident))
        self.families[ident] = selected
        for path in selected:
            self.watch(path)
        return selected

    def unchanged(self):
        from ..materials import discovery
        if self.inventory() != self.shared_names:
            return False
        return (all(set(discovery.selected(discovery.candidates(self.root), family=ident)) == paths
                    for ident, paths in self.families.items())
                and all(discovery.unit_header(self.root, path) == raw for path, raw in self.headers.items())
                and all((r.safe_path(self.root, path).read_bytes() if r.safe_path(self.root, path).exists() else None) == raw
                        for path, raw in self.data.items()))


class Batch:
    """A disposable selected postimage shared by otherwise independent entrances."""
    def __init__(self, repo):
        self.repo, self.pending, self.snapshots = repo, {}, []
        self.reservations, self.validators, self.guards = [], [], []
        self.snapshot = Preparation(repo.root)
        self.snapshots.append(self.snapshot)

    def add(self, pending, snapshot=None, *, reservations=(), validate=None, guard=None):
        for path, raw in pending.items():
            r.require(path not in self.pending or self.pending[path] == raw,
                      'Contradictory prepared destinations: ' + path)
            self.snapshot.watch(path)
            self.pending[path] = raw
        if snapshot is not None and snapshot not in self.snapshots:
            self.snapshots.append(snapshot)
        self.reservations.extend(reservations)
        if validate:
            self.validators.append(validate)
        if guard:
            self.guards.append(guard)

    def read(self, path):
        raw = self.pending[path] if path in self.pending else self.snapshot.bytes(path)
        return raw.decode('utf-8-sig') if path.endswith('.md') else raw

    def view(self):
        from ..materials import discovery
        batch = self
        class Postimage:
            @property
            def names(self):
                return (set(discovery.candidates(batch.repo.root)) | set(batch.pending)
                        | set().union(*(snapshot.names for snapshot in batch.snapshots)))
            def bytes(self, path):
                raw = batch.read(path)
                return raw.encode('utf8') if isinstance(raw, str) else raw
        view = copy.copy(self.repo)
        view.selected_tree = Postimage()
        return view

    def commit(self, *, timeout=30):
        from ..materials import identity as names, discovery
        # Reading and potentially expensive validation stay outside the lock.
        view = self.view()
        for validate in self.validators:
            validate(self.read, view)
        with r.locked(self.repo.root, timeout=timeout):
            r.require(all(snapshot.unchanged() for snapshot in self.snapshots),
                      'Selected inputs changed during preparation; read and prepare again.')
            for guard in self.guards:
                guard()
            config = r.read_json(self.repo.home / 'config.json', root=self.repo.root)
            reserved, issued = config, set()
            for ident, established in sorted(self.reservations,
                    key=lambda row: (names.namespace(row[0]) or '', row[0].number)):
                position = names.namespace(ident), ident.number
                if position[0] is None or position in issued:
                    continue
                candidates = discovery.candidates(self.repo.root, include_empty_j=True)
                if ident.kind == 'U':
                    selected = [path for path in candidates if (item := names.candidate(path))
                                and item['kind'] == 'U' and item['source_key'] == ident.source_key]
                else:
                    selected = [path for path in discovery.selected(candidates, kind=ident.kind,
                                author=ident.author, line=ident.line)
                                if (names.candidate(path)['origin'] or '').casefold()
                                == (ident.source_repository or '').casefold()]
                existing = [names.parse(path) for path in selected]
                r.require(all(names.namespace(item) == names.namespace(ident) for item in existing),
                          'Receiving material namespace has a noncanonical case collision.')
                reserved = names.reserve(reserved, ident, existing, established=established)
                issued.add(position)
            if reserved != config:
                r.write_json(self.repo.home / 'config.json', reserved, root=self.repo.root)
            # Issued numbers remain issued even if subsequent publication fails.
            expected = {path: self.snapshot.data[path] for path in self.pending}
            publish_files(self.repo, self.pending, expected)
            self.repo.config = reserved
        return list(self.pending)
