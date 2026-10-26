"""Create a clean, self-exportable research checkout from an explicit file manifest."""
from __future__ import annotations

import argparse
import json
import os
import re
from pathlib import Path, PurePosixPath
import shutil
import shlex
import stat
import subprocess
import sys
import tempfile
import uuid

from ..core import repository as r
from ..core import identity as identity
from . import version as version

MANIFEST = version.MANIFEST
HUMAN_FILES = ('user-manual/ai-disclosure-example.md',)
DISPLAY_TOKENS = re.compile(r'\{\{(?:REPOSITORY_ABBREVIATION|REPOSITORY_NAME)\}\}')


def display_value(value, label):
    """Accept an independent reader-facing display value, preserving its text."""
    r.require(type(value) is str, label + ' must be text.')
    r.require(value != '' and '\n' not in value and '\r' not in value,
              label + ' must be nonempty single-line text.')
    return value


def command_environment():
    # Keep the caller's trust-file policy; discard repository/index/author
    # overrides. Rebuild only safe.directory from inline Git config carriers.
    trust_files = {'GIT_CONFIG_GLOBAL', 'GIT_CONFIG_SYSTEM', 'GIT_CONFIG_NOSYSTEM'}
    env = {k: v for k, v in os.environ.items()
           if not k.upper().startswith('GIT_') or k.upper() in trust_files}
    trusted = []
    try:
        count = int(os.environ.get('GIT_CONFIG_COUNT', '0'))
        r.require(0 <= count <= len(os.environ), 'Invalid inline Git configuration count.')
        for index in range(count):
            key_name = os.environ['GIT_CONFIG_KEY_' + str(index)]
            value = os.environ['GIT_CONFIG_VALUE_' + str(index)]
            if key_name.casefold() == 'safe.directory':
                trusted.append(value)
        # Git's older -c carrier uses shell-quoted key=value tokens. It is parsed
        # as data only, never passed to a shell.
        for item in shlex.split(os.environ.get('GIT_CONFIG_PARAMETERS', ''), posix=True):
            key_name, separator, value = item.partition('=')
            if separator and key_name.casefold() == 'safe.directory':
                trusted.append(value)
    except (ValueError, KeyError) as error:
        raise r.ResearchError('Invalid inline Git trust configuration.') from error
    if trusted:
        env['GIT_CONFIG_COUNT'] = str(len(trusted))
        for index, value in enumerate(trusted):
            env['GIT_CONFIG_KEY_' + str(index)] = 'safe.directory'
            env['GIT_CONFIG_VALUE_' + str(index)] = value
    env['PYTHONDONTWRITEBYTECODE'] = '1'
    env['GIT_OPTIONAL_LOCKS'] = '0'
    return env


def command(root, *args, optional=False):
    result = subprocess.run(args, cwd=root, env=command_environment(), capture_output=True)
    if optional and result.returncode == 1:
        return ''
    # A missing HEAD is expected in a new checkout; ownership/config failures
    # from every other optional read must remain visible.
    if optional and result.returncode and tuple(args[-3:]) == ('rev-parse', '--verify', 'HEAD'):
        if b'dubious ownership' not in result.stderr.lower():
            return None
    r.require(result.returncode == 0, 'Export command failed: ' + result.stderr.decode('utf-8', 'replace').strip()
              + result.stdout.decode('utf-8', 'replace').strip())
    return result.stdout.decode('utf-8', 'replace').strip()


def linked(path):
    info = path.lstat()
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, 'st_file_attributes', 0) & 0x400)


def ordinary_chain(path):
    path = Path(os.path.abspath(path))
    for item in [path, *path.parents]:
        if os.path.lexists(item):
            r.require(not linked(item), 'Links/junctions are not export paths: ' + str(item))
    return path


def relative(value):
    r.require(isinstance(value, str) and '\\' not in value, 'Manifest paths use forward slashes.')
    path = PurePosixPath(value)
    r.require(value and not path.is_absolute() and path.as_posix() == value and
              all(p not in ('', '.', '..') for p in path.parts) and ':' not in value,
              'Unsafe export manifest path: ' + repr(value))
    r.require(all(part.casefold() not in ('.git', '.codex', '.agents') for part in path.parts),
              'Protected metadata cannot enter a framework export.')
    r.require(all(part == part.rstrip('. ') for part in path.parts), 'Ambiguous Windows path component.')
    return path


def refuse_history(value):
    parts = tuple(part.casefold() for part in relative(value).parts)
    r.require(parts[:3] != ('mathematics', 'computation', 'outputs'),
              'Local computation output cannot enter a clean framework export: ' + value)
    r.require(parts[:1] != ('history',) and
              parts[:2] not in {('project', 'history'), ('framework', 'history')},
              'Repository history cannot be exported: ' + value)


def source_file(root, value):
    rel = relative(value)
    path = ordinary_chain(root.joinpath(*rel.parts))
    r.require(path.resolve().is_relative_to(root.resolve()) and path.is_file(),
              'Missing or unsafe allowlisted framework file: ' + value)
    return path


def destination_kind(destination, author):
    """Read-only bootstrap eligibility of the exact target checkout."""
    ordinary_chain(destination)
    if not os.path.lexists(destination):
        return 'new'
    r.require(destination.is_dir(), 'Destination must be a blank directory.')
    r.require(not any(p.name != '.git' for p in destination.iterdir()),
              'Destination contains non-Git content; clean export cannot overlay it.')
    if not (destination/'.git').exists():
        return 'blank-directory'
    actual = command(destination, 'git', 'rev-parse', '--show-toplevel')
    r.require(Path(actual).resolve() == destination.resolve(), 'Target must be the exact Git checkout.')
    r.require(not command(destination, 'git', 'ls-files', '--stage'), 'Target index must be empty.')
    head = command(destination, 'git', 'rev-parse', '--verify', 'HEAD', optional=True)
    r.require(not head or not command(destination, 'git', 'ls-tree', '-r', '--name-only', head),
              'Target HEAD contains tracked content.')
    for name in ('MERGE_HEAD', 'CHERRY_PICK_HEAD', 'REVERT_HEAD', 'rebase-merge', 'rebase-apply', 'sequencer'):
        path = Path(command(destination, 'git', 'rev-parse', '--path-format=absolute', '--git-path', name))
        r.require(not path.exists(), 'Target has an unfinished Git operation: ' + name)
    if author is None:
        for key in ('research.actor', 'research.actorWorktree'):
            r.require(not command(destination, 'git', 'config', '--get', key, optional=True),
                      'Authorless target has an existing research binding: ' + key)
    return 'blank-git-worktree'


def install(stage, destination, plan):
    """Install only owned entries; never merge or replace target Git metadata."""
    kind = destination_kind(destination, plan['actor'])
    r.require(kind == plan['destination_kind'], 'Destination changed during export.')
    if kind == 'new':
        stage.rename(destination)
        (destination/'.framework-export-owner').unlink()
        return
    owned_files, owned_dirs, git_created = [], [], False
    configs = {}
    if kind == 'blank-git-worktree' and plan['actor'] is not None:
        common = Path(command(destination, 'git', 'rev-parse', '--path-format=absolute', '--git-common-dir'))
        local = Path(command(destination, 'git', 'rev-parse', '--path-format=absolute', '--git-path', 'config.worktree'))
        configs = {p: p.read_bytes() if p.exists() else None for p in {common/'config', common/'config.worktree', local}}
    try:
        # Exclusive creation records ownership at file granularity. A foreign
        # file appearing during installation is preserved, including on failure.
        for source in sorted(stage.rglob('*'), key=lambda p: (len(p.parts), str(p))):
            rel = source.relative_to(stage)
            if rel.parts[0] in ('.git', '.framework-export-owner'):
                continue
            target = destination/rel
            if source.is_dir():
                target.mkdir()
                owned_dirs.append(target)
            else:
                data = source.read_bytes()
                with target.open('xb') as output:
                    owned_files.append((target, data))
                    output.write(data)
        if kind == 'blank-directory':
            # Transfer this operation's initialized Git once; no second init.
            (stage/'.git').rename(destination/'.git')
            git_created = True
        if plan['actor'] is not None:
            command(destination, sys.executable, '-B', 'scripts/research.py', 'identity-bind', plan['actor'])
    except BaseException as error:
        problems = []
        for path, data in configs.items():
            try:
                restore_binding_config(path, data)
            except OSError as failure:
                problems.append(str(failure))
        if git_created:
            # Return only the Git directory installed by this operation to its
            # owned staging area for the ordinary bounded cleanup.
            try:
                (destination/'.git').rename(stage/'.git')
            except OSError as failure:
                problems.append(str(failure))
        for path, data in reversed(owned_files):
            try:
                if path.exists() and not linked(path) and path.read_bytes() == data:
                    path.unlink()
                elif path.exists():
                    problems.append('Changed installed file retained: ' + str(path))
            except OSError as failure:
                problems.append(str(failure))
        for path in reversed(owned_dirs):
            try:
                path.rmdir()
            except OSError:
                if path.exists():
                    problems.append('Nonempty installed directory retained: ' + str(path))
        if problems:
            raise r.ResearchError(str(error) + '; incomplete cleanup: ' + '; '.join(problems)) from error
        raise


def restore_binding_config(path, before):
    """Rollback binding keys while preserving concurrent unrelated settings."""
    owned = {'research.actor', 'research.actorworktree', 'extensions.worktreeconfig',
             'core.worktree', 'core.bare'}
    def settings(data):
        result = subprocess.run(['git', 'config', '--null', '--list', '--file', '-'],
                                input=data or b'', capture_output=True, env=command_environment())
        r.require(result.returncode == 0, 'Cannot inspect configuration rollback: ' + str(path))
        values = {}
        for field in result.stdout.decode('utf8').split('\0'):
            if field:
                key, _, value = field.partition('\n')
                values.setdefault(key.lower(), []).append(value)
        return values
    current = path.read_bytes() if path.exists() else None
    old, new = settings(before), settings(current)
    if {k:v for k,v in old.items() if k not in owned} == {k:v for k,v in new.items() if k not in owned}:
        if before is None:
            path.unlink(missing_ok=True)
        else:
            path.write_bytes(before)
        return
    for key in owned:
        if old.get(key) == new.get(key):
            continue
        if key in new:
            command(path.parent, 'git', 'config', '--file', str(path), '--unset-all', key)
        for value in old.get(key, []):
            command(path.parent, 'git', 'config', '--file', str(path), '--add', key, value)


def load_plan(source, destination, repository, repository_name, repository_abbreviation, author=None, display_name=None):
    repository = identity.key(repository)
    repository_name = display_value(repository_name, 'Repository display name')
    repository_abbreviation = display_value(repository_abbreviation, 'Repository abbreviation')
    source = ordinary_chain(source).resolve()
    r.require(source.is_dir(), 'Source checkout does not exist.')
    destination = ordinary_chain(destination)
    r.require(destination.parent.is_dir(), 'Create the destination parent directory first.')
    resolved = destination.resolve()
    r.require(not resolved.is_relative_to(source) and not source.is_relative_to(resolved),
              'A framework destination must be outside the source checkout.')
    actual = command(source, 'git', 'rev-parse', '--show-toplevel')
    r.require(Path(actual).resolve() == source, 'Export identity must belong to the exact source checkout.')
    actor = identity.key(author) if author is not None else None
    r.require(actor is not None or display_name is None, 'A display name needs an explicitly selected author key.')
    if actor is not None:
        identity.attribution_name(display_name)
        identity.validate_registry_value({'people': [{'id': actor, 'display_name': display_name}]})
    target_kind = destination_kind(destination, actor)
    manifest_bytes = source_file(source, MANIFEST).read_bytes()
    manifest = json.loads(manifest_bytes)
    version.validate_manifest(manifest)
    r.require('preferences' not in manifest, 'Clean-framework manifest must not contain personal preference entries.')
    copies = list(manifest['copy'])
    for item in copies:
        relative(item)
    ordinary_roots = {*HUMAN_FILES, '.gitignore', '.gitattributes', 'AGENTS.md', 'LICENSE',
                      'user-manual/user-manual.md', 'user-manual/用户手册.md',
                      'user-manual/Benutzerhandbuch.md', 'user-manual/Manuel d’utilisation.md',
                      'user-manual/ユーザーマニュアル.md',
                      'user-manual/agent-harness.md', 'user-manual/git-repository.md',
                      'user-manual/git-repo.png',
                      'user-manual/collaboration.jpg', 'user-manual/workflow.jpg',
                      'user-manual/user-instructions/user-instructions.md', 'user-manual/user-instructions/用户指令.md',
                      'user-manual/user-instructions/Anweisungsbeispiele.md',
                      'user-manual/user-instructions/Exemples de consignes.md',
                      'user-manual/user-instructions/指示例.md'}
    r.require(all(p in ordinary_roots or p.startswith('framework/') or p.startswith('scripts/')
                  for p in copies), 'Direct copies may contain only framework files, tools and declared human documents.')
    r.require(MANIFEST in copies and all(f in copies for f in HUMAN_FILES),
              'The manifest and declared human documents must be direct-copy entries.')
    templates = manifest['templates']
    r.require(isinstance(templates, dict), 'Template destinations must be explicit.')
    generated = manifest['generated']
    r.require(set(generated) == {'repository/config.json', 'repository/people.json',
              'repository/repositories.json', 'repository/intake-people.json',
              'mathematics/claims/index.md', 'mathematics/tasks/index.md',
              'mathematics/strategies/index.md'},
              'Unexpected generated paths in the framework manifest.')
    targets = copies + list(templates) + generated
    folded = [p.casefold() for p in targets]
    r.require(len(folded) == len(set(folded)), 'Export destination paths collide ignoring case.')
    for value in targets:
        relative(value)
        refuse_history(value)
        r.require(PurePosixPath(value).parts[0].casefold() != 'profiles', 'Personal profiles cannot be export targets.')
        r.require(not any(value.casefold().startswith(prefix) for prefix in
                  ('intake/', 'execution/', 'blueprint/')),
                  'Research evidence and development materials cannot be exported: ' + value)
    inputs = set(copies) | set(templates.values()) | {MANIFEST}
    for value in inputs | set(manifest['empty_directories']):
        refuse_history(value)
        r.require(not value.casefold().startswith('execution/'),
                  'Execution history cannot be an export input or initialized child: ' + value)
        r.require(value not in inputs or value.casefold() != 'execution',
                  'Execution storage cannot be an export input.')
        r.require(PurePosixPath(value).parts[0].casefold() != 'profiles', 'Personal profiles cannot be export inputs or target structures.')
    r.require(all(value.startswith('framework/export-templates/') for value in templates.values()),
              'Clean export template sources must be generic framework/export-templates files.')
    # The plan owns captured bytes, not a later traversal of mutable source directories.
    data = {p: source_file(source, p).read_bytes() for p in sorted(inputs)}
    r.require(data[MANIFEST] == manifest_bytes, 'Export manifest changed while planning.')
    return {'source': source, 'destination': destination, 'repository': repository,
            'repository_name': repository_name, 'repository_abbreviation': repository_abbreviation,
            'actor': actor, 'display_name': display_name, 'destination_kind': target_kind,
            'manifest': manifest, 'data': data,
            'copies': copies, 'templates': templates}


def write(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    r.require(not os.path.lexists(path), 'Refusing to overwrite an export file: ' + str(path))
    path.write_bytes(data)


def initialize(stage, plan):
    command(stage, 'git', '-c', 'init.templateDir=', 'init', '--quiet', '--template=')
    write(stage/'repository/config.json', r.encoded({
        'repository': plan['repository'],
        'layout_format': 2, 'repository_url': None, 'material_next': {},
        'framework_update_check': True}))
    people = [] if plan['actor'] is None else [{
        'id': plan['actor'], 'display_name': plan['display_name'],
        'registered_by': plan['actor'], 'git_identities': [], 'github_accounts': []}]
    write(stage/'repository/people.json', r.encoded({'people': people}))
    write(stage/'repository/repositories.json', r.encoded({'next': 1, 'repositories': []}))
    write(stage/'repository/intake-people.json', r.encoded({'next': 1, 'people': []}))
    if plan['actor'] is not None:
        command(stage, sys.executable, '-B', 'scripts/research.py', 'identity-bind', plan['actor'])
    command(stage, sys.executable, '-B', 'scripts/render-research-navigation.py')


def validate_export(stage):
    # Validate the actual portable output, without a research/material audit.
    output = command(stage, sys.executable, '-B', '-c', '''import json,sys
from pathlib import Path
sys.path.insert(0,str(Path.cwd()/'scripts'))
from acme.core import links
from acme.framework import version
root=Path.cwd()
manifest=json.loads((root/'framework/export-manifest.json').read_text(encoding='utf8'))
names=manifest['copy']+list(manifest['templates'])+manifest['generated']
errors=version.check(root)+links.check_files(root,[name for name in names if name.endswith('.md')])
if errors: raise ValueError('\\n'.join(errors))
print('Checked portable output links and framework manifest.')
''')
    for script in ('research.py', 'material.py', 'execution.py', 'render-research-navigation.py',
                   'check-literature-storage.py', 'export-framework.py'):
        command(stage, sys.executable, '-B', 'scripts/'+script, '--help')
    r.require(not (stage / 'repository/records').exists() and not (stage / 'repository/versions').exists(),
              'Export recreated retired C/T storage.')
    r.require(command(stage, 'git', 'rev-parse', '--verify', 'HEAD', optional=True) is None,
              'A clean export must not create a Git commit.')
    r.require(not command(stage, 'git', 'remote'), 'A clean export must not configure a remote.')
    return output + ' Installed public entrances are usable.'


def cleanup(stage, parent, token):
    # Only our verified sibling staging directory may be removed recursively.
    r.require(stage.parent.resolve() == parent.resolve() and stage.name.startswith('.framework-export-')
              and stage.resolve().parent == parent.resolve() and not linked(stage),
              'Unsafe export cleanup target.')
    marker = stage / '.framework-export-owner'
    r.require(marker.is_file() and marker.read_text(encoding='ascii') == token, 'Export cleanup ownership mismatch.')
    for root, dirs, files in os.walk(stage, followlinks=False):
        for name in dirs + files:
            r.require(not linked(Path(root) / name), 'Unexpected link in temporary export; preserving it for inspection.')
    shutil.rmtree(stage)


def export(source, destination, *, repository, repository_name, repository_abbreviation,
           author=None, display_name=None, dry_run=False):
    plan = load_plan(source, destination, repository, repository_name, repository_abbreviation, author, display_name)
    result = {'destination': str(plan['destination']), 'repository': plan['repository'],
              'actor': plan['actor'], 'framework_version': plan['manifest']['framework_version'],
              'copied_files': len(plan['copies']), 'templates': len(plan['templates']),
              'destination_kind': plan['destination_kind']}
    if dry_run:
        return {**result, 'dry_run': True}
    parent = plan['destination'].parent
    stage = Path(tempfile.mkdtemp(prefix='.framework-export-', dir=parent))
    token = uuid.uuid4().hex
    (stage / '.framework-export-owner').write_text(token, encoding='ascii')
    try:
        for target in plan['copies']:
            write(stage / target, plan['data'][target])
        values = {'{{REPOSITORY_ABBREVIATION}}': plan['repository_abbreviation'],
                  '{{REPOSITORY_NAME}}': plan['repository_name']}
        for target, template in plan['templates'].items():
            body = plan['data'][template].decode('utf-8')
            # Substitute only original template occurrences; inserted display text is literal data.
            body = DISPLAY_TOKENS.sub(lambda match: values[match.group(0)], body)
            write(stage / target, body.encode('utf-8'))
        for directory in plan['manifest']['empty_directories']:
            relative(directory)
            (stage / directory).mkdir(parents=True, exist_ok=True)
        initialize(stage, plan)
        result['validation'] = validate_export(stage)
        ordinary_chain(parent)
        install(stage, plan['destination'], plan)
        return result
    finally:
        if stage.exists():
            cleanup(stage, parent, token)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('destination', type=Path)
    parser.add_argument('--source', type=Path, default=Path(__file__).resolve().parents[3])
    parser.add_argument('--repository', required=True, help='Explicit destination repository identity key.')
    parser.add_argument('--repository-name', required=True,
                        help='Explicit full human-facing repository name for the exported README.')
    parser.add_argument('--repository-abbreviation', required=True,
                        help='Explicit short human-facing repository abbreviation for the exported README.')
    parser.add_argument('--author', help='Explicit initial human to register and bind; omission leaves an empty, unbound registry.')
    parser.add_argument('--display-name', help='Independent License attribution name; required with --author.')
    parser.add_argument('--dry-run', action='store_true', help='Check source, identity and destination without creating files.')
    args = parser.parse_args()
    try:
        print(json.dumps(export(args.source, args.destination, repository=args.repository,
                                repository_name=args.repository_name,
                                repository_abbreviation=args.repository_abbreviation,
                                author=args.author, display_name=args.display_name, dry_run=args.dry_run),
                         ensure_ascii=False, indent=2))
    except (OSError, ValueError, KeyError, TypeError) as error:
        print('Framework export refused: ' + str(error), file=sys.stderr)
        return 1
    return 0
