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
        self.stages = {}
        self.object_ids, self.cache, self.json_cache = {}, {}, {}
        self.batch = None
        if ref == 'WORKTREE':
            names = git(root, 'ls-files', '--cached', '--others', '--exclude-standard', '-z')
            # Names are candidates, not availability or ordinary-file facts.
            # Keep lexical exclusions ahead of any actual selected access.
            self.names = {name for name in names.decode().split('\0')
                          if name and not paths.local_runtime(name) and not paths.in_pdf_store(name)}
        elif ref == 'INDEX':
            entries = [n.split('\t', 1) for n in git(root, 'ls-files', '--stage', '-z').decode().split('\0') if n]
            for info, name in entries:
                mode, object_id, stage = info.split()
                self.stages.setdefault(name, {})[stage] = (mode, object_id)
            self.names = set(self.stages)
            for name, stages in self.stages.items():
                if set(stages) == {'0'}:
                    self.modes[name], self.object_ids[name] = stages['0']
        elif ref is None:
            self.names = set()
        else:
            entries = [n.split('\t', 1) for n in git(root, 'ls-tree', '-r', '-z', ref).decode().split('\0') if n]
            self.modes = {name: info.split()[0] for info, name in entries}
            self.object_ids = {name: info.split()[2] for info, name in entries}
            self.names = set(self.modes)

    def bytes(self, path):
        r.require(path in self.names, 'Required file is absent from the selected Git view: ' + path)
        r.require(self.ref != 'INDEX' or set(self.stages[path]) == {'0'},
                  'Selected Git index path is unmerged: ' + path)
        r.require(self.modes.get(path) not in {'120000', '160000'}, 'Selected evidence must be an ordinary file: ' + path)
        if path not in self.cache:
            if self.ref == 'WORKTREE':
                self.cache[path] = self._worktree_path(path).read_bytes()
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

    def _worktree_path(self, path):
        selected = r.safe_path(self.root, path)
        r.require(stat.S_ISREG(selected.stat().st_mode), 'Selected evidence must be an ordinary file: ' + path)
        return selected

    def existing(self, candidates):
        """Qualify only the caller's explicitly scoped context candidates."""
        for path in candidates:
            r.require(path in self.names, 'Context candidate is absent from the selected Git view: ' + path)
            if self.ref == 'WORKTREE':
                try:
                    self._worktree_path(path)
                except FileNotFoundError:
                    continue
            yield path

    def json(self, path):
        if path not in self.json_cache:
            self.json_cache[path] = json.loads(self.bytes(path))
        return self.json_cache[path]

    def header(self, path):
        """Read a selected sibling's header without requesting its whole body."""
        from ..materials import documents
        r.require(path in self.names, 'Required file is absent from the selected Git view: ' + path)
        r.require(self.ref != 'INDEX' or set(self.stages[path]) == {'0'},
                  'Selected Git index path is unmerged: ' + path)
        r.require(self.modes.get(path) not in {'120000', '160000'}, 'Selected evidence must be an ordinary file: ' + path)
        if self.ref == 'WORKTREE':
            with self._worktree_path(path).open('rb') as stream:
                return documents.header_stream(stream)
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
