"""Read-only bytes and fields from an explicitly selected Git view."""
import json
from pathlib import Path
import stat
import subprocess
from types import SimpleNamespace
from . import repository as r
from . import identity, paths


def git(root, *args):
    result = subprocess.run(['git', *args], cwd=root, capture_output=True)
    r.require(result.returncode == 0, 'Git inspection failed: ' + result.stderr.decode('utf-8', errors='replace').strip())
    return result.stdout


def research_view(tree, *, require_name=True):
    """Use the metadata and bytes of one explicitly supplied reading view."""
    config = tree.json('repository/config.json')
    r.require(isinstance(config, dict), 'Repository configuration must be an object.')
    view = SimpleNamespace(root=tree.root, home=tree.root/'repository', config=config,
                           identity_registry=tree.json('repository/people.json'), selected_tree=tree)
    identity.repository_name(config.get('repository'), required=require_name)
    identity.registry(view)
    return view


class Tree:
    def __init__(self, root, ref):
        self.root, self.ref = Path(root).resolve(), ref
        self.modes = {}
        self.object_ids, self.cache, self.json_cache = {}, {}, {}
        self.batch = None
        if ref == 'WORKTREE':
            names = git(root, 'ls-files', '--cached', '--others', '--exclude-standard', '-z')
            # Exclude local notes and source stores before shape
            # queries, even while indexed. Explicit profile selection stays.
            self.names = set()
            for name in names.decode().split('\0'):
                if not name or paths.local_runtime(name) or paths.in_pdf_store(name):
                    continue
                try:
                    mode = (self.root / name).stat().st_mode
                except FileNotFoundError:
                    continue
                if stat.S_ISREG(mode):
                    self.names.add(name)
        elif ref == 'INDEX':
            r.require(not git(root, 'ls-files', '--unmerged'), 'Resolve Git index conflicts before reading this selected view.')
            entries = [n.split('\t', 1) for n in git(root, 'ls-files', '--stage', '-z').decode().split('\0') if n]
            self.modes = {name: info.split()[0] for info, name in entries}
            self.object_ids = {name: info.split()[1] for info, name in entries}
            self.names = set(self.modes)
        elif ref is None:
            self.names = set()
        else:
            entries = [n.split('\t', 1) for n in git(root, 'ls-tree', '-r', '-z', ref).decode().split('\0') if n]
            self.modes = {name: info.split()[0] for info, name in entries}
            self.object_ids = {name: info.split()[2] for info, name in entries}
            self.names = set(self.modes)

    def bytes(self, path):
        r.require(path in self.names, 'Required file is absent from the selected Git view: ' + path)
        r.require(self.modes.get(path) not in {'120000', '160000'}, 'Selected evidence must be an ordinary file: ' + path)
        if path not in self.cache:
            if self.ref == 'WORKTREE':
                self.cache[path] = r.safe_path(self.root, path).read_bytes()
            else:
                if self.batch is None:
                    self.batch = subprocess.Popen(['git', 'cat-file', '--batch'], cwd=self.root,
                                                  stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                self.batch.stdin.write((self.object_ids[path] + '\n').encode('ascii'))
                self.batch.stdin.flush()
                header = self.batch.stdout.readline().split()
                r.require(len(header) == 3 and header[1] == b'blob', 'Cannot read selected Git object: ' + path)
                size = int(header[2])
                self.cache[path] = self.batch.stdout.read(size)
                r.require(len(self.cache[path]) == size and self.batch.stdout.read(1) == b'\n', 'Incomplete selected Git object.')
        return self.cache[path]

    def json(self, path):
        if path not in self.json_cache:
            self.json_cache[path] = json.loads(self.bytes(path))
        return self.json_cache[path]

    def header(self, path):
        """Read a selected sibling's header without requesting its whole body."""
        from ..materials import documents, discovery
        r.require(path in self.names, 'Required file is absent from the selected Git view: ' + path)
        r.require(self.modes.get(path) not in {'120000', '160000'}, 'Selected evidence must be an ordinary file: ' + path)
        if self.ref == 'WORKTREE':
            return discovery.unit_header(self.root, path)
        process = subprocess.Popen(['git', 'cat-file', 'blob', self.object_ids[path]], cwd=self.root,
                                   stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
        try:
            return documents.header_stream(process.stdout)
        finally:
            process.stdout.close()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill(); process.wait()

    def close(self):
        if self.batch is not None:
            process, self.batch = self.batch, None
            process.stdin.close()
            process.stdout.close()
            try:
                process.wait(timeout=2)
            except subprocess.TimeoutExpired:
                process.kill(); process.wait()

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()

    def __del__(self):
        self.close()

    def research_view(self):
        return research_view(self)
