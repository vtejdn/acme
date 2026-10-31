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
    version: None = field(default=None, init=False)
    kind: str = field(default='U', init=False)

    @property
    def unit(self):
        return self.family

    @property
    def anchor(self):
        return f'{self.source_key}-u{self.number:03d}'.lower()

    @property
    def family(self):
        origin = '_' + self.source_repository if self.source_repository else ''
        return f'{self.source_key}/{self.author}{origin}_U{self.number:03d}'

    @property
    def name(self):
        return self.family.split('/')[-1]


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
    unit = re.fullmatch(r'([A-Za-z0-9-]+)(?:_([A-Za-z0-9-]+))?_U([0-9]+)', name, re.I)
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
    unit = re.fullmatch(r'([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)(?:_([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*))?_U([0-9]{3,})\.md', path.name)
    if unit:
        require(len(path.parts) == 5 and path.parts[:3] == ('mathematics', 'audits', 'literature'),
                'A source unit belongs in its source-specific literature audit.')
        source_key = path.parts[3]
        validate_source_key(source_key)
        author, origin, number = unit.groups()
        require(origin is None or re.fullmatch(r'repo[1-9][0-9]*', origin), 'A received U uses its registered local repository token.')
        require(int(number) > 0 and number == f'{int(number):03d}', 'Noncanonical source unit number.')
        return SourceUnitIdentity(author, origin, source_key, int(number))
    # A J group owns its standard children, including its readme, rather than
    # allocating a mathematical identity to each output file.
    group = next((p for p in path.parts if re.search(r'_J_[A-Z][0-9]+(?:_v[0-9]+)?$', p)), None)
    name = group or path.stem
    match = re.fullmatch(r'([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*)(?:_([A-Za-z0-9]+(?:-[A-Za-z0-9]+)*))?_([CTSRDJL])_([A-Z][0-9]+)(?:_v([1-9][0-9]*))?', name)
    require(match is not None, 'Noncanonical material name: ' + str(path))
    author, origin, kind, suffix, revision = match.groups()
    if origin is not None:
        require(kind in 'CTRLJ' and re.fullmatch(r'author[1-9][0-9]*', author)
                and re.fullmatch(r'repo[1-9][0-9]*', origin),
                'External C/T/R/L/J prefixes use receiving authorN_repoN records.')
    else:
        require(not re.fullmatch(r'author[1-9][0-9]*', author, re.I), 'Local material uses a registered readable local author name.')
    require(kind == 'J' or path.suffix == '.md', 'Authored text material uses Markdown.')
    line, number = serial(suffix)
    require(kind not in 'CTRL' or revision is not None, 'Fixed material needs an explicit version.')
    require(kind not in 'SD' or revision is None, 'Rolling S/D material has no version suffix.')
    require(kind != 'J' or group is not None, 'A computation must own a J directory.')
    return Identity(author, origin, kind, line, number, int(revision) if revision else None)


def namespace(ident):
    """The permanent family counter, independent of a physical version."""
    if ident.kind == 'D':
        return None
    if ident.kind == 'U':
        origin = '_' + ident.source_repository if ident.source_repository else ''
        return 'U/' + validate_source_key(ident.source_key) + '/' + ident.author + origin
    require(ident.kind in {'C', 'T', 'R', 'L', 'J', 'S'}, 'Unknown permanent material family.')
    origin = '_' + ident.source_repository if ident.source_repository else ''
    return f'{ident.author}{origin}_{ident.kind}_{ident.line}'


def _counter_key(value):
    require(isinstance(value, str), 'Material counter namespace must be text.')
    if value.startswith('U/'):
        parts = value.split('/')
        require(len(parts) == 3, 'A U counter belongs to a source key and author namespace.')
        validate_source_key(parts[1])
        ident = parse('mathematics/audits/literature/' + parts[1] + '/' + parts[2] + '_U001.md')
        require(namespace(ident) == value, 'Noncanonical U counter namespace: ' + value)
        return
    match = re.fullmatch(r'(.+)_([CTRLJS])_([A-Z])', value)
    require(match is not None, 'Invalid permanent material counter namespace: ' + value)
    prefix, kind, line = match.groups()
    name = f'{prefix}_{kind}_{line}0001' + ('_v1' if kind in 'CTRL' else '')
    path = 'mathematics/' + (name + '/readme.md' if kind == 'J' else name + '.md')
    require(namespace(parse(path)) == value, 'Noncanonical material counter namespace: ' + value)


def material_next(config, previous=None):
    """Validate compact next-unissued state and an explicitly supplied preimage."""
    require(isinstance(config, dict) and isinstance(config.get('material_next'), dict),
            'Initialize material_next from agent-confirmed issued upper bounds before allocation.')
    state = config['material_next']
    for key, value in state.items():
        _counter_key(key)
        require(type(value) is int and value > 0, 'Material next number must be a positive integer: ' + key)
    if previous is not None:
        old = material_next(previous) if 'material_next' in previous else {}
        require(all(key in state and state[key] >= value for key, value in old.items()),
                'Permanent material counters cannot be removed or decreased.')
    return dict(state)


def check_issued(ident, config, *, previous=None, established=False):
    """Check a selected newly installed family against its authored counter."""
    key = namespace(ident)
    if key is not None:
        require(material_next(config).get(key, 0) > ident.number,
                'Advance material_next for the selected installed family: ' + key)
        if previous is not None and 'material_next' in previous and not established:
            require(ident.number >= material_next(previous).get(key, 1),
                    'Fresh material position is below the previous next-unissued bound: ' + key)


def allocation_bound(config, ident, existing=()):
    """Read occupation as a lower bound; never infer an issued upper bound."""
    key = namespace(ident)
    state = material_next(config)
    occupied = [item.number for item in existing if namespace(item) == key]
    require(key in state or not occupied,
            'Initialize the existing namespace from an agent-confirmed issued upper bound: ' + str(key))
    return max(state.get(key, 1), max(occupied, default=0) + 1)


def reserve(config, ident, existing=(), *, established=False):
    """Prepare monotone state for a fresh family or established correspondence.

    The caller holds the shared mutation lock and persists this state before
    publishing material bytes; a later publication failure does not undo it.
    """
    key = namespace(ident)
    if key is None:
        return config
    require(type(ident.number) is int and ident.number > 0, 'Reserve a positive family number.')
    bound = allocation_bound(config, ident, existing)
    require(established or ident.number >= bound,
            'Fresh material position is below the next-unissued bound: ' + key)
    state = material_next(config)
    state[key] = max(bound, ident.number + 1)
    return {**config, 'material_next': state}


def allocate(existing, *, author, kind, line=None, task=None, source_repository=None, next_number=1):
    """Compute a candidate address; the writer reserves it under the shared lock."""
    if task is not None:
        parent = parse(task)
        require(parent.kind == 'T', 'Parent must be a Task.')
        require(line is None or line == parent.line, 'Explicit line conflicts with the selected Task.')
        line = parent.line
    if line is None: line = 'A'
    require(re.fullmatch('[A-Z]', line), 'Use one uppercase research-line letter.')
    require(kind in {'C', 'T', 'S', 'R', 'D', 'J', 'L'}, 'Unknown material family.')
    require(re.fullmatch(r'[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*', author), 'Invalid author key.')
    require(source_repository is None, 'Imported originals keep their source identity; do not allocate a replacement.')
    numbers = [x.number for x in existing if
               x.kind != 'U' and
               (x.author, x.source_repository, x.kind, x.line) == (author, None, kind, line)]
    require(type(next_number) is int and next_number > 0, 'Next family number must be a positive integer.')
    return Identity(author, None, kind, line, max(next_number, max(numbers, default=0) + 1))
