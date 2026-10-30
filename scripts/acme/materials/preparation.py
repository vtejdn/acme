"""Explicit public-file checks and fresh reference preparation, without installation."""
import json
from pathlib import Path, PurePosixPath
import posixpath
from types import SimpleNamespace
from urllib.parse import quote

from ..core import git_views, links, paths, publication, repository as r
from . import discovery, identity, runtime, validation


def parse_json(text):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            r.require(key not in result, 'Duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(text, object_pairs_hook=unique)


def parse_file_list(text):
    value = parse_json(text)
    r.require(isinstance(value, list), 'A file list is a JSON array of explicit relative paths.')
    return value


def public_name(value, *, concrete=True):
    if value == '.' and not concrete:
        return value
    r.require(isinstance(value, str) and value and '\\' not in value and ':' not in value
              and not PurePosixPath(value).is_absolute() and PurePosixPath(value).as_posix() == value
              and all(part not in {'.', '..'} and part.rstrip(' .') == part for part in value.split('/')),
              'Use a canonical repository-relative POSIX path: ' + repr(value))
    paths.check_local_role(value)
    paths.check_public_target(value)
    r.require(value.split('/')[0].casefold() not in {'execution', '.venv'},
              'The public-file helper excludes execution and local environments.')
    r.require(not concrete or not paths.in_pdf_store(value),
              'Concrete source-store reads are outside public-file preparation.')
    return value


def selected_files(positional=(), extra=None, *, required=True):
    r.require(extra is None or isinstance(extra, list), 'A file list must be an array of paths.')
    values = list(positional) + (extra or [])
    r.require(values or not required, 'Select explicit files; there is no implicit whole-library check.')
    selected, seen = [], set()
    for value in values:
        name = public_name(value)
        r.require(name.casefold() not in seen, 'Duplicate or case-conflicting selected path: ' + name)
        seen.add(name.casefold())
        selected.append(name)
    return selected


def ordinary_root(value):
    return paths.ordinary_directory(value)


def public_root(value, receiving_root):
    absolute = Path(value).absolute()
    if absolute != receiving_root and absolute.is_relative_to(receiving_root):
        public_name(absolute.relative_to(receiving_root).as_posix())
    return ordinary_root(value)


def file_path(root, name, *, receiving_root=None):
    name = public_name(name)
    root = public_root(root, receiving_root) if receiving_root is not None else ordinary_root(root)
    if receiving_root is not None and (root / name).is_relative_to(receiving_root):
        public_name((root / name).relative_to(receiving_root).as_posix())
    target = r.safe_path(root, name)
    paths.check_case_spelling(root, name)
    return target


def file_bytes(root, name, *, receiving_root=None):
    return file_path(root, name, receiving_root=receiving_root).read_bytes()


def check_files(root, selected=(), *, files=None, prepared=None, installed=False, context=None):
    selected = selected_files(selected, files)
    context = selected_files(context or (), required=False)
    r.require(not installed or prepared is not None, '--installed requires --prepared.')
    root = ordinary_root(root)
    prepared = public_root(prepared, root) if prepared is not None else None
    pending = set(selected) if prepared is not None and not installed else set()
    captured = {}

    def raw(name):
        if name not in captured:
            captured[name] = file_bytes(prepared if name in pending else root, name, receiving_root=root)
        return captured[name]

    def read(name):
        data = raw(name)
        return data.decode('utf-8-sig') if name.endswith('.md') else data

    errors, notices = [], set()
    for name in selected:
        try:
            data = raw(name)
            if installed:
                r.require(data == file_bytes(prepared, name, receiving_root=root),
                          'Installed bytes differ from the selected prepared file.')
        except (OSError, ValueError) as error:
            errors.append({'path': name, 'kind': 'bytes', 'error': str(error)})
    if errors:
        return {'operation': 'check-files', 'files': len(selected), 'errors': errors, 'notices': []}

    typed = set(runtime.entrances(selected, strict=False))
    reader = None
    if typed:
        names = set(context) | set(selected) | {'repository/config.json', 'repository/people.json'}
        if any(identity.candidate(name)['kind'] in 'STU' for name in typed):
            names.update(discovery.candidates(root))
        tree = SimpleNamespace(root=root, names=names, bytes=raw, json=lambda name: json.loads(raw(name)))
        view = git_views.research_view(tree, require_name=False)
        reader = runtime.Reader(view)
        reader.read = read
    for name in selected:
        if name.endswith('.md'):
            try:
                locators = [{'path': public_name(path, concrete=False), 'anchor': anchor}
                            for path, anchor in (reader.destinations(name, read(name)) if name in typed
                                                 else links.destinations(name, read(name)))]
                validation.validate_navigation_targets(root, name, locators, read, planned=pending)
            except (OSError, ValueError) as error:
                errors.append({'path': name, 'kind': 'navigation', 'error': str(error)})
        if name in typed:
            try:
                doc = reader.check(name)
                notices.update(getattr(doc, 'notices', ()))
            except (OSError, ValueError, KeyError, TypeError) as error:
                errors.append({'path': name, 'kind': 'material', 'error': str(error)})
    return {'operation': 'check-files', 'files': len(selected), 'errors': errors, 'notices': sorted(notices)}


def address(value):
    r.require(isinstance(value, str), 'A locator must be PATH or PATH#ANCHOR.')
    path, separator, anchor = value.partition('#')
    r.require(not separator or anchor, 'An explicit locator fragment must be nonempty.')
    return public_name(path, concrete=False), anchor


def rewrite_text(owner, text, path_map, locator_map):
    new_owner = path_map.get(owner, owner)
    replacements = []
    for start, end, href in links.markdown_link_spans(text):
        destination = links.destination(owner, href)
        if destination is None:
            continue
        path, anchor = destination
        public_name(path, concrete=False)
        locator = path + ('#' + anchor if anchor else '')
        if locator in locator_map:
            path, anchor = address(locator_map[locator])
        else:
            path = path_map.get(path, path)
        public_name(path, concrete=False)
        relative = '' if path == new_owner and anchor else posixpath.relpath(path, posixpath.dirname(new_owner) or '.')
        value = quote(relative, safe='/-._~') + ('#' + quote(anchor, safe='-._~') if anchor else '')
        if href.strip().startswith('<'):
            value = '<' + value + '>'
        if value != href:
            replacements.append((start, end, value))
    for start, end, value in reversed(replacements):
        text = text[:start] + value + text[end:]
    return text, len(replacements)


def prepare_references(root, source, output, mapping, selected=(), *, files=None):
    selected = selected_files(selected, files)
    r.require(source is not None and output is not None, 'Supply --source and --output.')
    r.require(isinstance(mapping, dict) and not set(mapping) - {'paths', 'locators', 'edits'},
              'A mapping object accepts only paths, locators and explicit edits.')
    path_map, locator_map, edits = (mapping.get(key, {}) for key in ('paths', 'locators', 'edits'))
    r.require(all(isinstance(part, dict) for part in (path_map, locator_map, edits)),
              'paths, locators and edits must be objects.')
    for before, after in path_map.items():
        public_name(before, concrete=False)
        public_name(after, concrete=False)
    for before, after in locator_map.items():
        address(before)
        address(after)
    r.require(not set(edits) - set(selected), 'Explicit edits must name selected owners.')
    root = ordinary_root(root)
    source, output = public_root(source, root), public_root(output, root)
    origins = {file_path(source, name, receiving_root=root) for name in selected}
    destinations = {}

    def boundary(target):
        if source != root:
            r.require(not target.is_relative_to(source), 'Prepared output must not enter the external source tree.')
        if target.is_relative_to(root):
            r.require(target.is_relative_to(root / '.tmp') and target != root / '.tmp',
                      'Prepared output in the receiving repository must stay in root .tmp/.')
        r.require(target not in origins, 'Prepared output must not replace a selected source file.')

    def locate(base, name):
        base = public_root(base, root)
        boundary(base / name)
        target = r.safe_path(base, public_name(name))
        boundary(target)
        paths.check_case_spelling(base, name)
        return target

    for owner in selected:
        destination = public_name(path_map.get(owner, owner))
        r.require(owner.endswith('.md') and destination.endswith('.md'),
                  'Reference preparation needs canonical lowercase .md owners and destinations.')
        target = locate(output, destination)
        key = target.as_posix().casefold()
        r.require(key not in destinations, 'Case-conflicting prepared destinations: ' + destination)
        destinations[key] = target
    for target in destinations.values():
        r.require(not any(parent.as_posix().casefold() in destinations for parent in target.parents),
                  'A prepared file conflicts with another output directory: ' + str(target))

    pending, count = {}, 0
    for owner in selected:
        text = file_bytes(source, owner, receiving_root=root).decode('utf-8')
        if owner in edits:
            text = links.edit_text(text, edits[owner], context=owner)
        text, changed = rewrite_text(owner, text, path_map, locator_map)
        pending[path_map.get(owner, owner)] = text.encode('utf-8')
        count += changed
    publication.publish_files(SimpleNamespace(root=output), pending, dict.fromkeys(pending),
                              locate=locate, ordinary_root=output)
    return {'operation': 'prepare-references', 'files': len(pending), 'rewritten_links': count,
            'output': str(output), 'errors': []}
