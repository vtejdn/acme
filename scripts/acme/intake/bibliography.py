"""BibTeX parsing, explicit fields and unoccupied alpha-style addresses.

Keys use simplified ASCII name/year abbreviations, not exact alpha.bst labels.
Bibliographic names remain unchanged; character-aware identity is separate
from the address's lossy transliteration.
"""
from dataclasses import dataclass
from pathlib import Path
import re
import unicodedata

BIB = 'mathematics/literature/references.bib'


@dataclass
class Entry:
    kind: str
    key: str
    fields: dict


def parse(text, *, spans=None):
    """Read balanced BibTeX values, strings and concatenations without executing TeX."""
    entries, strings = {}, {}
    strings.update(dict(zip(('jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'),
                            ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'))))
    i, size = 0, len(text)

    def skip():
        nonlocal i
        while i < size:
            if text[i].isspace() or text[i] == ',':
                i += 1
            elif text[i] == '%':
                end = text.find('\n', i)
                i = size if end < 0 else end + 1
            else:
                break

    def value():
        nonlocal i
        skip()
        if i >= size:
            raise ValueError('Missing BibTeX value.')
        start = i
        if text[i] == '{':
            i += 1
            start, depth = i, 1
            while i < size and depth:
                if text[i] == '\\':
                    i += 2
                    continue
                depth += (text[i] == '{') - (text[i] == '}')
                i += 1
            if depth:
                raise ValueError('Unterminated BibTeX brace value.')
            return text[start:i-1]
        if text[i] == '"':
            i += 1
            start, depth = i, 0
            while i < size:
                if text[i] == '\\':
                    i += 2
                    continue
                if text[i] == '"' and depth == 0:
                    result = text[start:i]; i += 1
                    return result
                depth += (text[i] == '{') - (text[i] == '}')
                i += 1
            raise ValueError('Unterminated quoted BibTeX value.')
        while i < size and text[i] not in ',#})\r\n\t ':
            i += 1
        token = text[start:i]
        if token.isdigit():
            return token
        if token.casefold() not in strings:
            raise ValueError('Undefined BibTeX string: ' + token)
        return strings[token.casefold()]

    while i < size:
        skip()
        if i >= size:
            break
        if text[i] != '@':
            # BibTeX permits explanatory text outside entries.
            found = text.find('@', i)
            if found < 0: break
            i = found
        match = re.match(r'@(\w+)\s*([({])', text[i:])
        if not match:
            raise ValueError('Malformed BibTeX entry.')
        kind, opening = match.groups(); kind = kind.casefold()
        i += match.end()
        closing = '}' if opening == '{' else ')'
        if kind in {'comment', 'preamble'}:
            depth = 1
            while i < size and depth:
                if text[i] == '\\': i += 2; continue
                depth += (text[i] == opening) - (text[i] == closing)
                i += 1
            if depth: raise ValueError('Unterminated BibTeX comment/preamble.')
            continue
        fields = {}
        if kind != 'string':
            match = re.match(r'\s*([^\s,{}()]+)\s*,', text[i:])
            if not match: raise ValueError('Missing BibTeX citation key.')
            if spans is not None:
                spans.append((match[1], None, i + match.start(1), i + match.end(1)))
            key = match[1]; i += match.end()
            if any(existing.casefold() == key.casefold() for existing in entries):
                raise ValueError('Duplicate bibliography key ignoring case: ' + key)
        while True:
            skip()
            if i >= size: raise ValueError('Unterminated BibTeX entry.')
            if text[i] == closing:
                i += 1; break
            match = re.match(r'([A-Za-z][A-Za-z0-9_-]*)\s*=\s*', text[i:])
            if not match: raise ValueError('Invalid BibTeX field near ' + text[i:i+60])
            field = match[1].casefold(); i += match.end()
            start = i
            item = value(); end = i; skip()
            while i < size and text[i] == '#':
                i += 1; item += value(); end = i; skip()
            if field in fields: raise ValueError('Repeated BibTeX field: ' + field)
            fields[field] = item
            if spans is not None and kind != 'string':
                spans.append((key, field, start, end))
        if kind == 'string': strings.update(fields)
        else: entries[key] = Entry(kind, key, fields)
    return entries


def render(entries):
    return '\n\n'.join('@' + entry.kind + '{' + entry.key + ',\n' + '\n'.join(
        '  ' + field + ' = {' + value + '},' for field, value in entry.fields.items()) + '\n}'
        for entry in entries.values()) + ('\n' if entries else '')


def split_top(value, separator):
    depth, start, result, i = 0, 0, [], 0
    while i < len(value):
        if value[i] == '\\': i += 2; continue
        depth += (value[i] == '{') - (value[i] == '}')
        if not depth and value.startswith(separator, i):
            result.append(value[start:i].strip()); i += len(separator); start = i
        else: i += 1
    result.append(value[start:].strip())
    return result


def _unicode_name(value):
    """Interpret known TeX name characters, without evaluating TeX or macros."""
    accents = {"'": '\u0301', '`': '\u0300', '"': '\u0308', '^': '\u0302',
               '~': '\u0303', '=': '\u0304', '.': '\u0307', 'u': '\u0306',
               'v': '\u030c', 'H': '\u030b', 'c': '\u0327', 'k': '\u0328',
               'b': '\u0331', 'd': '\u0323', 'r': '\u030a'}
    letters = {'aa': 'å', 'AA': 'Å', 'ae': 'æ', 'AE': 'Æ', 'oe': 'œ', 'OE': 'Œ',
               'ss': 'ß', 'SS': 'ẞ', 'o': 'ø', 'O': 'Ø', 'l': 'ł', 'L': 'Ł',
               'i': 'ı', 'j': 'ȷ', 'dh': 'ð', 'DH': 'Ð', 'th': 'þ', 'TH': 'Þ',
               'ng': 'ŋ', 'NG': 'Ŋ'}

    def atom(at):
        start = at
        char = value[at]; at += 1
        if char == '{':
            parts = []
            while at < len(value) and value[at] != '}':
                part, at = atom(at); parts.append(part)
            return ''.join(parts), at + (at < len(value))
        if char != '\\' or at == len(value): return char, at
        match = re.match(r'[A-Za-z]+|.', value[at:])
        if not match: return value[start:at], at
        command = match[0]; at += len(command)
        if command in accents:
            while at < len(value) and value[at].isspace(): at += 1
            if at == len(value): return value[start:at], at
            part, end = atom(at)
            # Dotless i/j are the TeX bases of accented i/j, not aliases when
            # used by themselves. Combining marks survive identity comparison.
            base = unicodedata.normalize('NFD', part.replace('ı', 'i').replace('ȷ', 'j'))
            if base and base[0].isalpha() and all(unicodedata.combining(c) for c in base[1:]):
                return unicodedata.normalize('NFC', base + accents[command]), end
            return value[start:end], end
        if command in letters:
            while at < len(value) and value[at].isspace(): at += 1
            return letters[command], at
        # Unknown controls remain opaque; their letters are not ordinary name
        # text. In particular, no command is executed or expanded speculatively.
        return value[start:at], at

    parts, at = [], 0
    while at < len(value):
        part, at = atom(at); parts.append(part)
    return unicodedata.normalize('NFC', ''.join(parts))


def _name_text(value):
    value = re.sub(r'\\(?:[\'"`^~=.uvHckbdr])\s*\{?([A-Za-z])\}?', r'\1', value)
    for source, target in {'\\ss': 'ss', '\\ae': 'ae', '\\AE': 'AE', '\\oe': 'oe', '\\OE': 'OE',
                           '\\o': 'o', '\\O': 'O', '\\l': 'l', '\\L': 'L', 'ß': 'ss', 'æ': 'ae', 'ø': 'o', 'ł': 'l'}.items():
        value = value.replace(source, target)
    value = ''.join(c for c in unicodedata.normalize('NFKD', value) if not unicodedata.combining(c))
    value = value.replace('{', '').replace('}', '').replace('~', ' ')
    return value


def ascii_text(value):
    value = _name_text(value)
    if any(ord(c) > 127 for c in value):
        raise ValueError('An established Latin transliteration is required for the address: ' + value)
    return value


def _tokens(value):
    # Keep braced corporate/special-character tokens together.
    return [part for part in split_top(re.sub(r'(?:\s|(?<!\\)~)+', ' ', value.strip()), ' ') if part]


def name_parts(name):
    """BibTeX First/von/Last/Jr components, retaining full name tokens."""
    if name.startswith('{') and name.endswith('}') and len(split_top(name, ' ')) == 1:
        return [], [], [name], []
    parts = split_top(name, ',')
    if len(parts) > 3: raise ValueError('Invalid BibTeX personal name: ' + name)
    tokens = _tokens(parts[0])
    if not tokens: raise ValueError('Empty bibliographic name.')
    lower = lambda token: next((c for c in _unicode_name(token) if c.isalpha()), 'A').islower()
    if len(parts) > 1:
        last_lower = max((i for i, token in enumerate(tokens[:-1]) if lower(token)), default=-1)
        return (_tokens(parts[-1]), tokens[:last_lower+1], tokens[last_lower+1:],
                _tokens(parts[1]) if len(parts) == 3 else [])
    first_lower = next((i for i, token in enumerate(tokens[:-1]) if lower(token)), None)
    if first_lower is None: return tokens[:-1], [], tokens[-1:], []
    last_lower = max(i for i, token in enumerate(tokens[:-1]) if lower(token))
    return tokens[:first_lower], tokens[first_lower:last_lower+1], tokens[last_lower+1:], []


def surname(name):
    _, von, last, _ = name_parts(name)
    return von, last


def _initials(tokens):
    return ''.join(next((c for c in ascii_text(part) if c.isalpha()), '')
                   for token in tokens for part in split_top(token, '-'))


def alpha_label(entry):
    """Simplified ASCII alpha-style base; collision suffixes are persisted."""
    fields = entry.fields
    name = fields.get('author')
    if entry.kind in {'book', 'inbook'}: name = name or fields.get('editor')
    if entry.kind == 'proceedings': name = fields.get('editor')
    if name:
        people = split_top(name, ' and ')
        if any(person.casefold() == 'others' for person in people):
            raise ValueError('Retain the complete author list; and others is not an alpha-key shortcut.')
        # Transliteration affects the address only; the original field survives.
        address_names = split_top(fields.get('alpha-names', name), ' and ')
        if len(address_names) != len(people): raise ValueError('Transliterated names must retain every author in order.')
        pieces = []
        for person in address_names[:3] if len(people) > 4 else address_names:
            von, last = surname(person)
            abbreviation = _initials(von + last)
            if len(people) == 1 and len(abbreviation) < 2:
                abbreviation = ''.join(c for c in ascii_text(' '.join(last)) if c.isalnum())[:3]
            pieces.append(abbreviation)
        prefix = ''.join(pieces) + ('+' if len(people) > 4 else '')
    else:
        fallback = fields.get('key')
        if not fallback and entry.kind in {'manual', 'proceedings'}:
            fallback = re.sub(r'^The ', '', fields.get('organization', ''))
        fallback = fallback or entry.key
        prefix = ''.join(c for c in ascii_text(fallback) if c.isalnum())[:3]
    year = fields.get('alpha-year', fields.get('year', ''))
    if not re.fullmatch(r'[0-9]{4}', year):
        raise ValueError('Record a supported publication/first-public/private year or an explicit provisional basis.')
    label = prefix + year[-2:]
    if not re.fullmatch(r'[A-Za-z][A-Za-z0-9+]*', label): raise ValueError('Invalid portable alpha label: ' + label)
    return label


def suffix(number):
    result = ''
    while True:
        number, digit = divmod(number, 26); result = chr(97 + digit) + result
        if not number: return result
        number -= 1


def allocate(entries, entry):
    """Allocate an unused key after the caller explicitly chose a new work."""
    base = alpha_label(entry)
    used = {key.casefold() for key in entries}
    if base.casefold() not in used and not any(re.fullmatch(re.escape(base) + '[a-z]+', key, re.I) for key in entries):
        return base
    # Never fill an earlier hole in a persisted group when later suffixes exist.
    def ordinal(value):
        total = 0
        for char in value: total = total * 26 + ord(char) - 96
        return total - 1
    existing_suffixes = [key[len(base):].lower() for key in used if re.fullmatch(re.escape(base) + '[a-z]+', key, re.I)]
    index = max([ordinal(value) for value in existing_suffixes], default=0) + 1
    while (base + suffix(index)).casefold() in used: index += 1
    return base + suffix(index)


def field_differences(current, supplied):
    """Display exact supplied/current fields without choosing a correction."""
    return {field: {'current': current.fields.get(field), 'supplied': value}
            for field, value in supplied.fields.items() if current.fields.get(field) != value}


def search(entries, text):
    """Return literal case-insensitive candidates, without deciding work identity."""
    text = text.casefold()
    return [key for key, entry in entries.items()
            if text in key.casefold() or any(text in value.casefold() for value in entry.fields.values())]


def check(entries):
    errors = []
    for key, entry in entries.items():
        if not re.fullmatch(r'[A-Za-z][A-Za-z0-9+_-]*', key): errors.append('Invalid source key: ' + key)
        for field in ('title', 'year'):
            if not entry.fields.get(field): errors.append(key + ': missing known bibliographic field ' + field)
        if re.search(r'\band others\b', entry.fields.get('author', ''), re.I): errors.append(key + ': incomplete author list')
        # Structural host locators, not a classifier for the meaning of notes.
        # Multi-component drive/UNC paths and explicit home/file locators are
        # distinct from public URLs, DOI strings and TeX such as C:\to D.
        host = r'(?<![\w])(?:[A-Za-z]:[\\/][^\s{}<>"`$^]+[\\/]|\\\\[A-Za-z0-9_.-]+\\[A-Za-z0-9_.-]+|file:///|/(?:home|Users)/[^/\s]+/)'
        if any(re.search(host, value) for value in entry.fields.values()):
            errors.append(key + ': machine-local locator is not bibliographic content')
    return errors
