"""Derived material navigation; authored materials and intake keep authority."""
from pathlib import Path
import os
from . import discovery as discovery
from . import documents as documents
from . import indexes as indexes
from . import navigation as navigation
from . import runtime as runtime
from ..core import repository as shared


def views(repo):
    reader = runtime.Reader(repo)
    tree = getattr(repo, 'selected_tree', None)
    if isinstance(tree, _Snapshot):
        reader.read = tree.read
    selected = runtime.entrances(tree.names) if tree is not None else discovery.inventory(repo.root)
    # Validate discovery collisions, registered original sources and numeric revision ordering.
    discovery.families(selected, reader.read, source_info=reader.source_info)
    fixed = [p for p in selected if reader.document(p).identity.kind in 'CT']
    outputs = indexes.views(fixed, reader.read, source_info=reader.source_info,
                            strategy_paths=[path for path in selected if reader.document(path).identity.kind == 'S'])
    routes = [reader.document(p) for p in selected if reader.document(p).identity.kind in 'SL']
    outputs.update(navigation.views(routes, reader.read, source_info=reader.source_info,
                                    unavailable=reader.unavailable, paths=selected))
    return {path: text.encode('utf-8') for path, text in outputs.items()}


def _inputs(root):
    selected = set(discovery.inventory(root))
    selected.update(('repository/config.json', 'repository/people.json',
                     'repository/repositories.json', 'repository/intake-people.json'))
    selected.update(shared.safe_path(root, p.relative_to(root).as_posix()).relative_to(root).as_posix()
                    for p in shared.safe_path(root, 'intake').glob('*/*.json'))
    return selected


class _Snapshot:
    def __init__(self, root, names):
        self.root = root
        self.names = names
        self.data = {p: shared.read_bytes(root/p, root=root) for p in names}

    def read(self, path):
        # Capture only additional targets actually read by the derived views.
        # The publication guard rechecks these bytes along with the entrances.
        if path not in self.data:
            self.data[path] = shared.read_bytes(shared.safe_path(self.root, path), root=self.root)
        data = self.data[path]
        return data.decode('utf-8-sig') if path.endswith('.md') else data

    def bytes(self, path):
        if path not in self.data:
            raise FileNotFoundError(path)
        return self.data[path]


def render(repo, *, timeout=30):
    # Parse and render outside the shared publication lock. Recheck the exact
    # captured inputs before installing; ordinary material writers stay unlocked.
    root = repo.root
    for attempt in range(3):
        snapshot = _Snapshot(root, _inputs(root))
        selected = shared.Repository(root)
        selected.selected_tree = snapshot
        outputs = views(selected)
        with shared.locked(root, timeout=timeout):
            if (_inputs(root) != snapshot.names or any(
                    shared.read_bytes(root/p, root=root) != raw
                    for p, raw in snapshot.data.items())):
                continue
            return _publish(repo, outputs)
    raise ValueError('Navigation inputs changed during preparation; retry against the current materials.')


def _publish(repo, outputs):
        changed = shared.generated_changes(repo.root, outputs)
        before = {path: shared.read_bytes(repo.root / path, root=repo.root)
                  if (repo.root / path).exists() else None for path in changed}
        written = []
        try:
            for path, data in changed.items():
                shared.write_bytes(repo.root / path, data, root=repo.root)
                written.append(path)
        except Exception:
            for path in reversed(written):
                if before[path] is None:
                    shared.unlink(repo.root / path, root=repo.root)
                else:
                    shared.write_bytes(repo.root / path, before[path], root=repo.root)
            raise
        return {'outputs': len(outputs), 'changed': len(changed)}
