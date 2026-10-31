"""Captured inputs and short, reversible publication of explicitly prepared files.

This module has no intake, import-history or mathematical-decision semantics.
Callers judge the contents and supply validation and allocation scope explicitly.
"""
import copy
from . import repository as r


def publish_files(repo, pending, expected, *, locate=None, ordinary_root=None):
    # The default locator enforces ordinary repository storage. A caller with
    # a declared source mount supplies its own checked locator for every I/O.
    # A bounded ordinary locator can retain atomic-write guards with ordinary_root.
    storage_root = ordinary_root if ordinary_root is not None else repo.root if locate is None else None
    locate = locate or r.safe_path
    targets, locations = {}, {}
    for name in pending:
        target = r.paths.resolved_path(locate(repo.root, name))
        key = target.as_posix().casefold()
        r.require(key not in targets, 'Conflicting publication destinations: '
                  + targets.get(key, '') + ' and ' + name)
        targets[key] = name
        locations[name] = target
    if storage_root is not None:
        root = r.paths.resolved_path(storage_root)
        selected = [target.relative_to(root) for target in locations.values()]
        for relative in selected:
            r.paths.check_required_directories(root, relative, planned=selected,
                                               context='Required output directory')
    for name, old in expected.items():
        target = locate(repo.root, name)
        r.require((target.read_bytes() if target.exists() else None) == old,
                  'Selected input changed during preparation: ' + name)
    attempts = []
    try:
        for name, raw in pending.items():
            target = locate(repo.root, name)
            old = expected[name]
            if old == raw:
                continue
            ownership = {}
            attempts.append((name, ownership))
            r.write_bytes(target, raw, exclusive=old is None, root=storage_root, ownership=ownership)
            ownership['installed'] = True
    except BaseException as error:
        competing, failed = [], []
        for name, ownership in reversed(attempts):
            try:
                target = locate(repo.root, name)
                info = target.stat() if target.exists() else None
                same_file = info is not None and (info.st_dev, info.st_ino) == ownership.get('file_id')
                # A non-returning writer may already have installed its temporary
                # file. Equal bytes from a failed exclusive create are not ours.
                if not ownership.get('installed') and not same_file:
                    continue
                if not same_file or target.read_bytes() != pending[name]:
                    competing.append(name)
                    continue
                if expected[name] is None:
                    r.unlink(target, root=storage_root)
                else:
                    r.write_bytes(target, expected[name], root=storage_root)
            except BaseException as rollback_error:
                try:
                    target = locate(repo.root, name)
                    current = target.read_bytes() if target.exists() else None
                    if current == expected[name]:
                        continue
                    state = ('missing' if current is None else 'published content remains'
                             if current == pending[name] else 'other content present')
                except BaseException as inspection_error:
                    state = 'state unavailable: ' + type(inspection_error).__name__
                failed.append(name + ' (' + state + '; ' + str(rollback_error) + ')')
        problems = []
        if competing:
            problems.append('competing content preserved during rollback: ' + ', '.join(competing))
        if failed:
            problems.append('rollback failed for: ' + ', '.join(failed))
        if problems:
            raise r.ResearchError('Publication failed; ' + '; '.join(problems)) from error
        raise


class Preparation:
    """Watch actual inputs and explicitly selected allocation namespaces."""
    def __init__(self, root, units=(), *, metadata=False):
        self.root, self.data, self.headers = root, {}, {}
        self.metadata = metadata
        self.units = tuple(units)
        self.names = self.inventory()
        self.shared_names = set(self.names)
        self.families = {}

    def inventory(self):
        selected = set()
        if self.metadata:
            folder = r.safe_path(self.root, 'intake')
            if folder.is_dir():
                files, errors = r.paths.repository_files(folder, suffix=None)
                r.require(not errors, '; '.join(errors))
                selected.update(path.relative_to(self.root).as_posix() for path in files)
        from ..materials import discovery
        for ident in self.units:
            relative = 'mathematics/audits/literature/' + ident.source_key
            folder = r.safe_path(self.root, relative)
            if not folder.is_dir():
                continue
            selected.update(path.relative_to(self.root).as_posix() for path in folder.glob('*.md')
                            if discovery.unit_namespace(path.relative_to(self.root).as_posix(), ident))
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
            def header(self, path):
                if path not in batch.pending:
                    return batch.snapshot.header(path)
                from io import BytesIO
                from ..materials import documents
                return documents.header_stream(BytesIO(batch.pending[path]))
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
            for path in self.pending:
                target = r.safe_path(self.repo.root, path)
                r.paths.check_required_directories(self.repo.root, target.relative_to(self.repo.root),
                                                   planned=self.pending, context='Required output directory')
            config = r.read_json(self.repo.home / 'config.json', root=self.repo.root)
            reserved, issued = config, set()
            for ident, established in sorted(self.reservations,
                    key=lambda row: (names.namespace(row[0]) or '', row[0].number)):
                position = names.namespace(ident), ident.number
                if position[0] is None or position in issued:
                    continue
                candidates = discovery.candidates(self.repo.root, include_empty_j=True)
                if ident.kind == 'U':
                    selected = [path for path in candidates if discovery.unit_namespace(path, ident)]
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
