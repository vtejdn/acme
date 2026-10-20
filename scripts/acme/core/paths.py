"""Repository traversal and explicit, contained access to retained sources."""
import os
from pathlib import Path
import re
import stat
from urllib.parse import unquote

PDF_ROOT = Path('mathematics/literature/pdf')
LEGACY_PDF_ROOT = Path('literature/pdf')
COMPUTATION_OUTPUT_ROOT = Path('mathematics/computation/outputs')
PROTECTED = {'.git', '.codex', '.agents'}
# Shared environments and generated test caches contain no authored materials.
EXCLUDED = PROTECTED | {'.tmp', '.generated', '.venv', '.pytest_cache', '__pycache__', 'build', 'output'}
PDF_NAME = re.compile(r'[A-Za-z0-9][A-Za-z0-9+_.-]*\.pdf', re.I | re.ASCII)


class PathError(ValueError):
    pass


def resolved_path(path):
    """Normalize equivalent Windows final-path spellings after resolution.

    A concurrent exclusive create can make GetFinalPathNameByHandle retain the
    extended prefix. Compare the same drive/UNC spelling on both sides; linked
    components and the resolved repository boundary are still checked below.
    """
    resolved = Path(path).resolve()
    value = str(resolved)
    if os.name == 'nt':
        if value.startswith('\\\\?\\UNC\\'):
            return Path('\\\\' + value[8:])
        if re.match(r'^\\\\\?\\[A-Za-z]:\\', value):
            return Path(value[4:])
    return resolved


def is_reparse(path):
    """Include Windows junctions, which are not ordinary symbolic links."""
    try:
        info = path.lstat()
    except FileNotFoundError:
        return False
    return stat.S_ISLNK(info.st_mode) or bool(getattr(info, 'st_file_attributes', 0) & 0x400)


def protected_path(relative):
    return any(part.casefold() in PROTECTED for part in relative.parts)


def private_file(relative):
    parts = tuple((part.rstrip(' .') if os.name == 'nt' else part).casefold()
                  for part in Path(relative).parts)
    return len(parts) == 3 and parts[0] == 'profiles' and parts[2] == 'secrets.md'


def check_public_target(relative):
    """Reject a private link by its normalized role, without opening the file."""
    if private_file(relative):
        raise PathError('Public links must not target private profile secrets; use inline-code lookup instructions instead.')


def in_pdf_store(relative):
    parts = tuple(part.casefold() for part in Path(relative).parts)
    return any(parts[:len(prefix.parts)] == tuple(prefix.parts)
               for prefix in (PDF_ROOT, LEGACY_PDF_ROOT))


def in_computation_outputs(relative):
    parts = tuple(part.casefold() for part in Path(relative).parts)
    return parts[:len(COMPUTATION_OUTPUT_ROOT.parts)] == tuple(COMPUTATION_OUTPUT_ROOT.parts)


def valid_pdf_name(name):
    return bool(PDF_NAME.fullmatch(name))


def valid_source_name(name):
    """PDFs stay flat; original HTML/resources have one canonical work group."""
    if valid_pdf_name(name): return True
    if '\\' in name or ':' in name: return False
    parts = name.split('/')
    if len(parts) < 2 or not re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9+_.-]*', parts[0], re.ASCII): return False
    if any(part in {'', '.', '..'} or part.rstrip(' .') != part or
           re.search(r'[\x00-\x1f<>:"\\|?*]', part) or part.casefold() in PROTECTED
           for part in parts[1:]): return False
    return not name.lower().endswith('.pdf')


def ordinary_path(root, relative):
    """Resolve an ordinary repository path without accepting any linked component."""
    root, relative = resolved_path(root), Path(relative)
    if relative.is_absolute() or '..' in relative.parts or ':' in str(relative):
        raise PathError('Local path must stay inside the repository.')
    if protected_path(relative):
        raise PathError('Protected path: repository metadata.')
    candidate = root
    for part in relative.parts:
        candidate /= part
        if is_reparse(candidate):
            raise PathError('Local path follows an undeclared directory/file link.')
    resolved = resolved_path(candidate)
    if not resolved.is_relative_to(root):
        raise PathError('Local path escapes the repository: ' + str(candidate) + ' resolved to ' + str(resolved) + '; root ' + str(root))
    if protected_path(resolved.relative_to(root)):
        raise PathError('Protected path: resolved repository metadata.')
    return resolved


def material_path(root, relative):
    """Source-store aliases must not become publication material."""
    root, relative = resolved_path(root), Path(relative)
    if in_pdf_store(relative):
        raise PathError('Local literature PDF storage is source access, not publishable research material.')
    resolved = ordinary_path(root, relative)
    targets = [resolved_path(root / entrance) for entrance in (PDF_ROOT, LEGACY_PDF_ROOT)]
    if in_pdf_store(resolved.relative_to(root)) or any(resolved.is_relative_to(target) for target in targets):
        raise PathError('Local literature PDF storage is source access, not publishable research material.')
    return resolved


def repository_files(root, suffix='.md'):
    root = resolved_path(root)
    files, errors = [], []
    pending = [root]
    while pending:
        folder = pending.pop()
        try:
            children = sorted(folder.iterdir())
        except OSError as error:
            errors.append(f'Cannot inspect repository directory {folder}: {error}')
            continue
        for child in children:
            relative = child.relative_to(root)
            if (child.name.casefold() in EXCLUDED or in_pdf_store(relative)
                    or in_computation_outputs(relative) or private_file(relative)):
                continue
            if is_reparse(child):
                errors.append(f'Repository traversal refuses an undeclared directory/file link: {relative}')
                continue
            if child.is_dir():
                pending.append(child)
            elif suffix is None or child.suffix.lower() == suffix:
                files.append(child)
    return sorted(files), errors


def pdf_storage(root):
    root = resolved_path(root)
    # Neither mathematics nor literature may itself be an undeclared link.
    ordinary_path(root, PDF_ROOT.parent)
    mount = root / PDF_ROOT
    if is_reparse(mount) and getattr(mount.lstat(), 'st_reparse_tag', None) != getattr(stat, 'IO_REPARSE_TAG_MOUNT_POINT', 0xA0000003):
        raise PathError('The local literature entrance must be an ordinary directory or top-level directory junction.')
    target = resolved_path(mount)
    if root.is_relative_to(target):
        raise PathError('PDF storage cannot point to the repository or one of its parent directories.')
    if mount.exists() and not mount.is_dir():
        raise PathError(f'{PDF_ROOT.as_posix()} must be an ordinary directory or top-level directory junction.')
    return mount, target


def pdf_path(root, relative):
    """Resolve one named flat PDF through the sole local source entrance."""
    root, relative = resolved_path(root), Path(relative)
    prefix = tuple(part.casefold() for part in relative.parts[:len(PDF_ROOT.parts)])
    if prefix != tuple(PDF_ROOT.parts):
        raise PathError(f'Only {PDF_ROOT.as_posix()} is a permitted external source mount.')
    if len(relative.parts) != len(PDF_ROOT.parts) + 1:
        raise PathError(f'Unsupported PDF path: subdirectories are not permitted in {PDF_ROOT.as_posix()}.')
    name = relative.parts[-1]
    if not valid_pdf_name(name):
        raise PathError(f'Unsupported PDF filename: {name}')
    mount, target = pdf_storage(root)
    candidate = mount / name
    if is_reparse(candidate):
        raise PathError('Nested junctions or file links are not permitted in PDF source locators.')
    resolved = resolved_path(candidate)
    if not resolved.is_relative_to(target):
        raise PathError('PDF locator escapes its storage target.')
    return resolved


def source_path(root, relative, *, work_key=None):
    """Resolve one explicitly named local file without registry interpretation or traversal."""
    relative = Path(relative)
    if not in_pdf_store(relative) or tuple(part.casefold() for part in relative.parts[:len(PDF_ROOT.parts)]) != tuple(PDF_ROOT.parts):
        raise PathError('Only the declared literature source mount is supported.')
    name = relative.relative_to(PDF_ROOT).as_posix()
    if name.lower().endswith('.pdf'): return pdf_path(root, relative)
    if not valid_source_name(name): raise PathError('Unsupported grouped source path: ' + name)
    group = name.split('/', 1)[0]
    if work_key is not None and group != work_key:
        raise PathError('Source group differs from the selected canonical work key.')
    mount, target = pdf_storage(root)
    candidate = mount
    for part in name.split('/'):
        candidate /= part
        if is_reparse(candidate): raise PathError('Nested junctions or file links are not permitted in source groups.')
    resolved = resolved_path(candidate)
    if not resolved.is_relative_to(target / group): raise PathError('Source locator escapes its declared work group.')
    return resolved


def link_path(root, document, destination):
    """Normalize a relative link lexically before following any filesystem link."""
    root = resolved_path(root)
    destination = unquote(destination)
    if '\\' in destination or Path(destination).is_absolute() or ':' in destination:
        raise PathError('Local links must use relative POSIX paths.')
    lexical = Path(os.path.abspath(Path(document) if not destination else Path(document).parent / destination))
    if not lexical.is_relative_to(root):
        raise PathError('Local link escapes the repository.')
    relative = lexical.relative_to(root)
    if protected_path(relative):
        raise PathError('Local link targets protected repository metadata.')
    if in_pdf_store(relative):
        return source_path(root, relative), True
    return ordinary_path(root, relative), False


def internal_path(root, path):
    """An internal path has one ordinary entrance under this checkout's repository/."""
    root = resolved_path(root)
    path = Path(path)
    if path.is_absolute():
        try:
            path = path.relative_to(root)
        except ValueError as error:
            raise PathError('Internal storage path escapes the repository.') from error
    if not path.parts or path.parts[0].casefold() != 'repository':
        raise PathError('Internal storage paths must start with repository/.')
    return ordinary_path(root, path)


def execution_path(root, path='execution'):
    """Execution storage is an ordinary, flat directory at execution/."""
    root = resolved_path(root)
    path = Path(path)
    if path.is_absolute():
        try:
            path = path.relative_to(root)
        except ValueError as error:
            raise PathError('Execution storage path escapes the repository.') from error
    if not path.parts or path.parts[0].casefold() != 'execution':
        raise PathError('Execution storage paths must start with execution/.')
    return ordinary_path(root, path)


def check_internal_storage(root):
    """Inspect links before mutation; never descend through an internal reparse point."""
    root = resolved_path(root)
    home = internal_path(root, 'repository')
    if not home.exists():
        return
    if not home.is_dir():
        raise PathError('Internal storage repository/ must be an ordinary directory.')
    pending = [home]
    while pending:
        directory = internal_path(root, pending.pop())
        for child in directory.iterdir():
            if is_reparse(child):
                raise PathError('Internal storage refuses a directory/file link: ' +
                                child.relative_to(root).as_posix())
            if child.is_dir():
                pending.append(child)
    execution = execution_path(root)
    if execution.exists() and not execution.is_dir():
        raise PathError('Execution storage execution/ must be an ordinary directory.')
    return None
