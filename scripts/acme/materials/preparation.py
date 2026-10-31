"""Explicit selected-file byte, view and material-declaration checks."""
import json
from io import BytesIO
from pathlib import Path, PurePosixPath
from types import SimpleNamespace

from ..core import git_views, paths, repository as r
from . import discovery, documents, identity, runtime


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

    def header(name):
        if name in captured:
            return documents.header_stream(BytesIO(captured[name]))
        with file_path(root, name, receiving_root=root).open('rb') as stream:
            return documents.header_stream(stream)

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
        tree = SimpleNamespace(root=root, names=names, bytes=raw, header=header, json=lambda name: json.loads(raw(name)))
        view = git_views.research_view(tree, require_name=False)
        reader = runtime.Reader(view)
        reader.read = read
    for name in selected:
        if name in typed:
            try:
                doc = reader.check(name)
                notices.update(getattr(doc, 'notices', ()))
            except (OSError, ValueError, KeyError, TypeError) as error:
                errors.append({'path': name, 'kind': 'material', 'error': str(error)})
    return {'operation': 'check-files', 'files': len(selected), 'errors': errors, 'notices': sorted(notices)}
