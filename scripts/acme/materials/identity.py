"""Canonical material names; author-selected lines never overflow into letters."""
from dataclasses import dataclass, field
from pathlib import PurePosixPath
import re


def require(condition, message):
    if not condition:
        raise ValueError(message)


def serial(value):
    match = re.fullmatch(r'([A-Z])([0-9]{4,})', value)
    require(match is not None, 'Expected one research-line letter and a numeric serial: ' + value)
    number = int(match[2])
    require(number > 0 and match[2] == f'{number:04d}', 'Noncanonical serial: ' + value)
    return match[1], number


@dataclass(frozen=True)
class Identity:
    author: str
    source_repository: str | None
    kind: str
    line: str
    number: int
    version: int | None = None

    @property
    def family(self):
        origin = '_' + self.source_repository if self.source_repository else ''
        return f'{self.author}{origin}_{self.kind}_{self.line}{self.number:04d}'

    @property
    def name(self):
        return self.family + (f'_v{self.version}' if self.version is not None else '')


@dataclass(frozen=True)
class SourceUnitIdentity:
    """An existing source-key unit, not a research-line material counter."""
    author: str
    source_repository: str | None
    source_key: str
    number: int
    version: int
    kind: str = field(default='U', init=False)

    @property
    def unit(self):
        return f'{self.source_key}-U{self.number:03d}'

    @property
    def anchor(self):
        return self.unit.lower()

    @property
    def family(self):
        origin = '_' + self.source_repository if self.source_repository else ''
        return f'{self.source_key}/{self.author}{origin}_U{self.number:03d}'

    @property
    def name(self):
        return self.family.split('/')[-1] + f'_v{self.version}'


def validate_source_key(value):
    require(isinstance(value, str) and re.fullmatch(r'[A-Za-z][A-Za-z0-9+_-]*', value), 'Invalid source citation key.')
    return value


def candidate(path):
    """Locate a possible namespace; this does not validate its address."""
    path = PurePosixPath(path)
    group = next((part for part in path.parts[:-1]
                  if re.fullmatch(r'[A-Za-z0-9-]+(?:_[A-Za-z0-9-]+)?_J_[A-Za-z][0-9]+(?:_v[0-9]+)?', part, re.I)), None)
    if group is not None and (path.parent.name != group or path.name != 'readme.md'):
        return None
    if path.name.casefold() == 'readme.md' and group is None:
        return None
    name = path.parent.name if path.name.casefold() == 'readme.md' else path.name
    name = re.sub(r'\.md$', '', name, flags=re.I)
    match = re.fullmatch(r'([A-Za-z0-9-]+)(?:_([A-Za-z0-9-]+))?_([CTSRDJL])_([A-Za-z])([0-9]+)(?:_v[0-9]+)?', name, re.I)
    if match:
        author, origin, kind, line, number = match.groups()
        return {'author':author, 'origin':origin, 'kind':kind.upper(), 'line':line.upper(), 'number':int(number)}
    unit = re.fullmatch(r'([A-Za-z0-9-]+)(?:_([A-Za-z0-9-]+))?_U([0-9]+)(?:_v[0-9]+)?', name, re.I)
    if unit:
        author, origin, number = unit.groups()
        return {'author':author, 'origin':origin, 'kind':'U', 'source_key':path.parent.name, 'number':int(number)}
    return None


def in_namespace(path, *, kind=None, author=None, line=None, local=False, family=None):
    item = candidate(path)
    if item is None: return False
    if family is not None:
        if item['kind'] != family.kind or item['number'] != family.number: return False
        if family.kind == 'U':
            if item['source_key'].casefold() != family.source_key.casefold(): return False
        elif item['line'] != family.line: return False
        author, local = family.author, family.source_repository is None
        if (item['origin'] or '').casefold() != (family.source_repository or '').casefold(): return False
    return ((kind is None or item['kind'] == kind)
            and (author is None or item['author'].casefold() == author.casefold())
            and (line is None or item.get('line') == line)
            and (not local or item['origin'] is None))


def parse(path):
    path = PurePosixPath(path)
    require(not path.is_absolute() and '..' not in path.parts and '\\' not in str(path) and ':' not in str(path), 'Unsafe material path.')
    unit = re.fullmatch(r'([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)(?:_([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*))?_U([0-9]{3,})_v([1-9][0-9]*)\.md', path.name)
    if unit:
        require(len(path.parts) == 5 and path.parts[:3] == ('mathematics', 'audits', 'literature'),
                'A source unit belongs in its source-specific literature audit.')
        source_key = path.parts[3]
        validate_source_key(source_key)
        author, origin, number, revision = unit.groups()
        require(origin is None or re.fullmatch(r'repo[1-9][0-9]*', origin), 'A received U uses its registered local repository token.')
        require(int(number) > 0 and number == f'{int(number):03d}', 'Noncanonical source unit number.')
        return SourceUnitIdentity(author, origin, source_key, int(number), int(revision))
    # A J group owns its standard children, including its readme, rather than
    # allocating a mathematical identity to each output file.
    group = next((p for p in path.parts if re.search(r'_J_[A-Z][0-9]+(?:_v[0-9]+)?$', p)), None)
    name = group or path.stem
    match = re.fullmatch(r'([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)(?:_([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*))?_([CTSRDJL])_([A-Z][0-9]+)(?:_v([1-9][0-9]*))?', name)
    require(match is not None, 'Noncanonical material name: ' + str(path))
    author, origin, kind, suffix, revision = match.groups()
    if origin is not None:
        require(kind in 'CRLJ' and re.fullmatch(r'author[1-9][0-9]*', author)
                and re.fullmatch(r'repo[1-9][0-9]*', origin),
                'External C/R/L/J prefixes use receiving authorN_repoN records.')
    else:
        require(not re.fullmatch(r'author[1-9][0-9]*', author, re.I), 'Local material uses a registered readable local author name.')
    require(kind == 'J' or path.suffix == '.md', 'Authored text material uses Markdown.')
    line, number = serial(suffix)
    require(kind not in 'CTRL' or revision is not None, 'Fixed material needs an explicit version.')
    require(kind not in 'SD' or revision is None, 'Rolling S/D material has no version suffix.')
    require(kind != 'J' or group is not None, 'A computation must own a J directory.')
    return Identity(author, origin, kind, line, number, int(revision) if revision else None)


def allocate(existing, *, author, kind, line=None, task=None, source_repository=None):
    """Return the next address; callers lock and recheck before creating files."""
    if task is not None:
        parent = parse(task)
        require(parent.kind == 'T', 'Parent must be a Task.')
        require(line is None or line == parent.line, 'Explicit line conflicts with the selected Task.')
        line = parent.line
    require(line is not None and re.fullmatch('[A-Z]', line), 'A new independent line needs its author designation.')
    require(kind in {'C', 'T', 'S', 'R', 'D', 'J', 'L'}, 'Unknown material family.')
    require(re.fullmatch(r'[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*', author), 'Invalid author key.')
    require(source_repository is None, 'Imported originals keep their source identity; do not allocate a replacement.')
    numbers = [x.number for x in existing if
               x.kind != 'U' and
               (x.author, x.source_repository, x.kind, x.line) == (author, None, kind, line)]
    return Identity(author, None, kind, line, max(numbers, default=0) + 1)
