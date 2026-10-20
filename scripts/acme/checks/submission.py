"""Check explicit attribution, fields and references in a requested Git view."""
import json
from pathlib import Path
import re
import subprocess
from types import SimpleNamespace
from ..core import repository as r
from ..core import identity as identity


def git(root, *args):
    result = subprocess.run(['git', *args], cwd=root, capture_output=True)
    r.require(result.returncode == 0, 'Git inspection failed: ' + result.stderr.decode('utf-8', errors='replace').strip())
    return result.stdout


class Tree:
    def __init__(self, root, ref):
        self.root, self.ref = Path(root).resolve(), ref
        self.modes = {}
        self.object_ids, self.cache, self.json_cache, self.anchor_cache = {}, {}, {}, {}
        self.batch = None
        if ref == 'WORKTREE':
            names = git(root, 'ls-files', '--cached', '--others', '--exclude-standard', '-z')
            self.names = {n for n in names.decode().split('\0') if n and (self.root / n).is_file()}
        elif ref == 'INDEX':
            r.require(not git(root, 'ls-files', '--unmerged'), 'Resolve Git index conflicts before submission.')
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
        r.require(path in self.names, 'Required file is absent from the submitted tree: ' + path)
        r.require(self.modes.get(path) not in {'120000', '160000'}, 'Submitted evidence must be an ordinary file: ' + path)
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

    def anchors(self, path):
        if path not in self.anchor_cache:
            from ..core.links import anchors_text
            self.anchor_cache[path] = anchors_text(self.bytes(path).decode('utf-8-sig'))
        return self.anchor_cache[path]

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
        config = self.json('repository/config.json')
        view = SimpleNamespace(root=self.root, home=self.root/'repository', config=config,
                               identity_registry=self.json('repository/people.json'), selected_tree=self)
        identity.key(config['repository']); identity.registry(view)
        return view


def git_person(view, name, email):
    found = [p['id'] for p in identity.registry(view)['people'] if
             any(i['name'] == name and i['email'].casefold() == email.casefold() for i in p.get('git_identities', []))]
    r.require(len(found) == 1, 'Git signature does not uniquely match a registered human: ' + name + ' <' + email + '>')
    return found[0]


def effective_person(repo, variable):
    ident = git(repo.root, 'var', variable).decode().strip()
    match = re.fullmatch(r'(.*) <([^<>]+)> [0-9]+ [+-][0-9]{4}', ident)
    r.require(match, 'Unrecognized effective Git identity.')
    return git_person(repo, match[1], match[2])


def check_tree(tree, before, author, other_parents=(), *, authors_by_path=None):
    from . import scoped as research_scoped
    return research_scoped.validate(tree, (before, *other_parents), author,
                                    authors_by_path)


def check(root, *, working_tree=False, commits=None, github_account=None, push=False):
    opened = []
    def open_tree(ref):
        tree = Tree(root, ref); opened.append(tree); return tree
    try:
        root = Path(root).resolve()
        identity.checkout(root)
        repo = open_tree('HEAD' if commits is not None else ('WORKTREE' if working_tree else 'INDEX')).research_view()
        actor = identity.actor(repo)
        r.require(effective_person(repo, 'GIT_AUTHOR_IDENT') == actor, 'Local actor and effective Git author do not match.')
        r.require(effective_person(repo, 'GIT_COMMITTER_IDENT') == actor, 'Local actor and effective Git committer do not match.')
        if push:
            r.require(github_account, 'Supply the authenticated GitHub login established by the authorized connectivity check.')
        if github_account:
            r.require(github_account.casefold() in [x.casefold() for x in identity.person(repo, actor).get('github_accounts', [])],
                      'GitHub login does not match the locally bound human identity.')
        head_result = subprocess.run(['git', 'rev-parse', '--verify', 'HEAD'], cwd=root, capture_output=True, text=True)
        head = head_result.stdout.strip() if head_result.returncode == 0 else None
        count, checked = 0, 0
        if commits is not None:
            r.require(head, 'No commits to check.')
            base = git(root, 'rev-parse', '--verify', commits + '^{commit}').decode().strip()
            if push:
                ancestor = subprocess.run(['git', 'merge-base', '--is-ancestor', base, head], cwd=root, capture_output=True)
                r.require(ancestor.returncode == 0, 'Push base is not an ancestor of HEAD; resolve remote divergence before pushing.')
            revisions = git(root, 'rev-list', '--reverse', base + '..HEAD').decode().splitlines()
            tree = open_tree(head)
            view = tree.research_view()
            authors_by_path = {}
            headers = git(root, 'log', '--reverse', '-m', '--format=%x1e%H%x00%an%x00%ae%x00%cn%x00%ce%x00',
                          '--name-only', '-z', base + '..HEAD').decode('utf-8')
            for block in headers.split('\x1e'):
                if not block.strip('\x00\n'): continue
                values = block.split('\x00')
                contributor = git_person(view, values[1], values[2])
                git_person(view, values[3], values[4])
                for path in values[5:]:
                    path = path.strip('\n')
                    if path: authors_by_path.setdefault(path, set()).add(contributor)
            count = check_tree(tree, open_tree(base), actor, authors_by_path=authors_by_path)
            checked = len(revisions)
    
        else:
            tree = open_tree('WORKTREE' if working_tree else 'INDEX')
            view = tree.research_view()
            r.require(identity.person(view, actor)['id'] == actor, 'Local actor is absent from the submitted registry.')
            # The submitted registry, not an unstaged registry edit, must authorize the signature.
            ident = git(root, 'var', 'GIT_AUTHOR_IDENT').decode().strip()
            match = re.fullmatch(r'(.*) <([^<>]+)> [0-9]+ [+-][0-9]{4}', ident)
            r.require(git_person(view, match[1], match[2]) == actor, 'Submitted identity mapping differs from the local actor.')
            merge_path = Path(git(root, 'rev-parse', '--git-path', 'MERGE_HEAD').decode().strip())
            if not merge_path.is_absolute():
                merge_path = root / merge_path
            merges = []
            if merge_path.exists():
                for value in merge_path.read_text(encoding='ascii').splitlines():
                    commit = git(root, 'rev-parse', '--verify', value + '^{commit}').decode().strip()
                    merges.append(open_tree(commit))
            count = check_tree(tree, open_tree(head), actor, tuple(merges))
        return {'actor': actor, **count, 'commits': checked,
                'scope': 'final base-to-HEAD changes' if commits is not None else ('working-tree preparation' if working_tree else 'staged changes')}
    finally:
        for tree in opened: tree.close()


def report(result):
    return f"Checked {result['changed_paths']} paths in {result['scope']}; structural checks passed." + ''.join('\nNotice: ' + note for note in result.get('notices', []))
