"""Exact text edits, bounded declaration structure and explicit locator decoding."""
import posixpath
import re
from bisect import bisect_right
from urllib.parse import unquote


def edit_text(raw, choice, *, context='text'):
    """Apply supplied final text or exact original character spans, without inference."""
    def require(condition, message):
        if not condition: raise ValueError(message)
    require(isinstance(choice, dict) and set(choice) in ({'edits'}, {'text'}, {'expected','text'}),
            'Supply designated edits or complete final text, not both.')
    if 'text' in choice:
        if 'expected' in choice:
            require(raw == choice['expected'], 'Stale designated '+context+' edit; prepare from the selected original text again.')
        require(isinstance(choice['text'], str), 'Final text must be explicit text.')
        return choice['text']
    require(isinstance(choice['edits'], list), 'Edits must be an explicit list.')
    changes, previous = [], 0
    for edit in choice['edits']:
        require(isinstance(edit, dict) and set(edit) == {'start','end','expected','replacement'},
                'Each edit needs original start/end offsets, expected text and replacement.')
        start, end = edit['start'], edit['end']
        require(type(start) is int and type(end) is int and previous <= start < end <= len(raw)
                and isinstance(edit['expected'], str) and isinstance(edit['replacement'], str),
                'Edits must be ordered, disjoint original character spans.')
        require(raw[start:end] == edit['expected'], 'Stale designated '+context+' edit; prepare from the selected original text again.')
        changes.append((start, end, edit['replacement']))
        previous = end
    for start, end, value in reversed(changes): raw = raw[:start] + value + raw[end:]
    return raw


_CODE = re.compile(r'(?<!`)(`+)(?!`)(.*?)(?<!`)\1(?!`)', re.S)
_HTML_BLOCK = re.compile(r' {0,3}<(pre|script|style|textarea)(?=[ \t>]|$)', re.I)
_HTML_OPEN = re.compile(r'<(pre|code|script|style|textarea)\b[^>]*>', re.I)
_HTML_BLOCK_END = re.compile(r'</(?:pre|script|style|textarea)\s*>', re.I)
_INLINE = re.compile(r'(?<!`)(`+)(?!`)|<!--|<(?:pre|code|script|style|textarea)\b', re.I)
_HEADING = re.compile(r' {0,3}#{1,6}(?:[ \t]|$)')


def _fence_start(line):
    opened = re.fullmatch(r' {0,3}(`{3,}|~{3,})(.*)', line.expandtabs(4))
    return opened if opened and not (opened[1][0] == '`' and '`' in opened[2]) else None


def _paragraph_boundary(line):
    return (not line.strip() or _HEADING.match(line) or _fence_start(line) or
            _HTML_BLOCK.match(line) or re.match(r' {0,3}<!--', line))


def _escaped(text, position):
    start = position
    while start and text[start - 1] == '\\':
        start -= 1
    return (position - start) % 2


def _literal_regions(text, *, block_positions=False):
    """Read bounded blocks before their inlines; yield disjoint source spans.

    An active fence, indented block, comment, HTML literal or code span owns its
    contents. Its apparent inner openers cannot alter the outer parser state.
    At block positions, only a line's first nonspace token can start a region;
    unrelated prose cannot carry inline state into a later declaration.
    Inline backticks look ahead only to the next actual block boundary, never
    through a raw HTML block. This is not a general Markdown/HTML renderer.
    """
    lines, position = [], 0
    for line in text.splitlines(keepends=True):
        content = line.rstrip('\r\n')
        lines.append((position, position + len(content), position + len(line), content))
        position += len(line)
    starts = [line[0] for line in lines]
    limits, boundary = {}, len(text)
    for index in range(len(lines) - 1, -1, -1):
        start, end, _next, content = lines[index]
        limits[index] = boundary
        if _paragraph_boundary(content):
            boundary = start

    fence, paragraph, indented = None, False, False
    active_end, active_kind, active_block = 0, None, False
    for index, (start, end, following, content) in enumerate(lines):
        cursor, parts = start, []
        if active_end > start:
            cursor = min(active_end, end)
            if active_kind != 'hidden':
                # Literal contents count as text, but their inner heading or
                # setext markers cannot determine the next line's paragraph state.
                parts.append('x')
            if active_block or cursor == end:
                paragraph = bool(parts) and not active_block
                continue
        else:
            expanded = content.expandtabs(4)
            if fence is not None:
                marker, width = fence
                if re.fullmatch(r' {0,3}' + re.escape(marker) + '{' + str(width) + r',}[ \t]*', expanded):
                    fence = None
                yield 'hidden', start, following, None
                continue
            if (indented or not paragraph) and expanded.startswith('    '):
                indented, paragraph = True, False
                yield 'hidden', start, following, None
                continue
            if not content.strip():
                paragraph = False
                yield 'hidden', start, following, None
                continue
            indented = False
            block = _HTML_BLOCK.match(content)
            # Keep the established bounded <code> literal extension; unlike
            # rawtext HTML, it does not interrupt an existing paragraph.
            code_block = re.match(r' {0,3}<code\b[^>]*>', content, re.I) if not paragraph else None
            if code_block:
                closing = re.compile(r'</code\s*>', re.I).search(text, start + code_block.end())
                # Establish the code's containing span before looking for an
                # outside continuation. Raw-line limits can contain apparent
                # block openers owned by this code, including on its closing line.
                if closing and not re.search(r'\r?\n[ \t]*\r?\n', text[start + code_block.end():closing.start()]):
                    closing_line = bisect_right(starts, closing.end() - 1) - 1
                    tail = text[closing.end():lines[closing_line][1]]
                    continues = closing_line + 1 < len(lines) and not _paragraph_boundary(lines[closing_line + 1][3])
                    if tail.strip() or continues:
                        code_block = None
            if block or code_block:
                closing = (_HTML_BLOCK_END.search(text, start + block.end()) if block else
                           re.search(r'</code\s*>', text[start + code_block.end():], re.I))
                close_end = (closing.end() if block else start + code_block.end() + closing.end()) if closing else len(text)
                active_end = lines[bisect_right(starts, max(start, close_end - 1)) - 1][2] if closing else len(text)
                active_kind, active_block, paragraph = 'html', True, False
                yield 'html', start, active_end, None
                continue
            opened = _fence_start(content)
            if opened:
                fence, paragraph = (opened[1][0], len(opened[1])), False
                yield 'hidden', start, following, None
                continue

        # A heading-shaped prefix inside the active region does not make its
        # closing line a heading. Only a heading recognized outside that region
        # bounds subsequent backticks to this physical line.
        inline_limit = end if cursor == start and _HEADING.match(content) else limits[index]
        while cursor < end:
            if block_positions:
                first = start + len(content) - len(content.lstrip(' \t'))
                token = _INLINE.match(text, first, end) if cursor <= first else None
            else:
                token = _INLINE.search(text, cursor, end)
            if token is None:
                parts.append(text[cursor:end])
                break
            parts.append(text[cursor:token.start()])
            if _escaped(text, token.start()):
                parts.append(token[0])
                cursor = token.end()
                continue
            match, kind, stop = None, None, None
            if token[1]:
                match = _CODE.match(text, token.start(), inline_limit)
                if match:
                    kind, stop = 'code', match.end()
            elif token[0] == '<!--':
                closing = text.find('-->', token.end())
                kind, stop = 'hidden', closing + 3 if closing >= 0 else len(text)
            else:
                opened = _HTML_OPEN.match(text, token.start())
                if opened:
                    closing = re.compile(r'</' + opened[1] + r'\s*>', re.I).search(text, opened.end())
                    kind, stop = 'html', closing.end() if closing else len(text)
            if kind is None:
                parts.append(token[0])
                cursor = token.end()
                continue
            yield kind, token.start(), stop, match
            active_end, active_kind, active_block = stop, kind, False
            if kind != 'hidden':
                parts.append('x')
            cursor = stop
        visible = ''.join(parts)
        paragraph = bool(visible.strip()) and not (_HEADING.match(visible) or re.fullmatch(r' {0,3}(?:=+|-+)[ \t]*', visible))


def code_spans(text):
    """Matched inline backticks in their containing block, with source offsets."""
    for kind, _start, _end, match in _literal_regions(text):
        if kind == 'code':
            yield match


def markdown_views(text, *, preserve_offsets=False, block_positions=False):
    """Decode semantic content and mask structures from the same source spans."""
    visible, structure, position = [], [], 0
    for kind, start, end, _match in _literal_regions(text, block_positions=block_positions):
        preceding, value = text[position:start], text[start:end]
        visible.append(preceding)
        structure.append(preceding)
        if kind == 'hidden':
            value = re.sub(r'[^\r\n]', ' ' if preserve_offsets else '', value)
            visible.append(value)
            structure.append(value)
        else:
            visible.append(value)
            structure.append(re.sub(r'[^\r\n]', ' ', value))
        position = end
    visible.append(text[position:])
    structure.append(text[position:])
    return ''.join(visible), ''.join(structure)


def visible_markdown(text, *, preserve_offsets=False):
    """Remove code blocks/comments, retaining literal cell and heading text."""
    return markdown_views(text, preserve_offsets=preserve_offsets)[0]


def declaration_views(text, *, preserve_offsets=False):
    """Block positions and bounded table contents, independent of free prose."""
    visible, structure = markdown_views(text, preserve_offsets=preserve_offsets, block_positions=True)
    runs, opened, offset = [], None, 0
    for line in structure.splitlines(keepends=True):
        if re.match(r'^[ \t]*\|', line):
            if opened is None:
                opened = offset
        elif opened is not None:
            runs.append((opened, offset))
            opened = None
        offset += len(line)
    if opened is not None:
        runs.append((opened, offset))
    # Inline code and comments belong to this actual contiguous table only.
    # Process both views together, and never interpret preceding prose first.
    for start, end in reversed(runs):
        cells, mask = markdown_views(visible[start:end], preserve_offsets=preserve_offsets)
        visible = visible[:start] + cells + visible[end:]
        structure = structure[:start] + mask + structure[end:]
    return visible, structure


def anchor_occurrences(text):
    from collections import Counter
    # Markdown treats CRLF and CR as line endings, not heading content.
    visible, structure = declaration_views(text.replace('\r\n', '\n').replace('\r', '\n'), preserve_offsets=True)
    explicit = re.compile(r'''^ {0,3}<a[ \t]+id=(?P<quote>["']?)(?P<anchor>[^\s"'<>=`]+)(?P=quote)[ \t]*>[ \t]*</a>[ \t]*$''', re.M)
    values = Counter(item['anchor'] for item in explicit.finditer(structure))
    # A heading must start outside literals, while inline code contributes its
    # visible text to the established heading slug.
    for heading in re.finditer(r'^ {0,3}#{1,6}(?=[ \t])', structure, re.M):
        end = visible.find('\n', heading.end())
        line = visible[heading.end():end if end >= 0 else len(visible)]
        title = visible_markdown(line).strip()
        if not title: continue
        title = re.sub(r'[ \t]+#+[ \t]*$', '', title)
        values[re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')] += 1
    return values


def anchors_text(text):
    return set(anchor_occurrences(text))


def declaration_markdown(raw, *, preserve_offsets=False):
    """Responsible block/table structure, retaining selected source offsets."""
    return declaration_views(raw, preserve_offsets=preserve_offsets)[1]


def table_pipes(line):
    """Offsets of unescaped, eligible delimiters in a table structure view."""
    return [item.start() for item in re.finditer(r'(?<!\\)\|', line)]


def destination_text(link):
    """Remove Markdown address delimiters/escapes, leaving URL decoding separate."""
    link = link.strip()
    if link.startswith('<') and link.endswith('>'):
        link = link[1:-1]
    return re.sub(r'\\([!"#$%&\'()*+,\-./:;<=>?@\[\\\]^_`{|}~])', r'\1', link)


def destination(document, link):
    link = destination_text(link)
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link):
        return None
    path, _, anchor = link.partition('#')
    path, anchor = unquote(path), unquote(anchor)
    # Filesystem separators constrain the path, not the resource's fragment.
    if '\\' in path:
        raise ValueError('Local links must use relative POSIX paths, not backslashes.')
    if path.startswith('/'):
        raise ValueError('Absolute local link: ' + link)
    target = posixpath.normpath(posixpath.join(posixpath.dirname(document), path)) if path else document
    if target == '..' or target.startswith('../') or any(p.casefold() in {'.git', '.codex', '.agents'} for p in target.split('/')):
        raise ValueError('Unsafe local link: ' + link)
    return target, anchor
