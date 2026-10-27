"""Local Markdown destinations and checks of explicitly supplied public files."""
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


def _literal_regions(text):
    """Read bounded blocks before their inlines; yield disjoint source spans.

    An active fence, indented block, comment, HTML literal or code span owns its
    contents. Its apparent inner openers cannot alter the outer parser state.
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


def markdown_views(text, *, preserve_offsets=False):
    """Decode semantic content and mask structures from the same source spans."""
    visible, structure, position = [], [], 0
    for kind, start, end, _match in _literal_regions(text):
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


def anchor_occurrences(text):
    from collections import Counter
    # Markdown treats CRLF and CR as line endings, not heading content.
    visible, structure = markdown_views(text.replace('\r\n', '\n').replace('\r', '\n'), preserve_offsets=True)
    values = Counter(re.findall(r'(?<!\\)<a\s+id=[\"\']?([^\"\'>\s]+)', structure))
    # A heading must start outside literals, while inline code contributes its
    # visible text to the established heading slug.
    for heading in re.finditer(r'^ {0,3}#{1,6}(?=[ \t])', structure, re.M):
        end = visible.find('\n', heading.end())
        title = visible[heading.end():end if end >= 0 else len(visible)].strip()
        if not title: continue
        title = re.sub(r'[ \t]+#+[ \t]*$', '', title)
        values[re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')] += 1
    return values


def anchors_text(text):
    return set(anchor_occurrences(text))


def _inline_link_spans(text):
    """Scan inline links without rescanning long unmatched bracket sequences."""
    offset = 0
    for line in text.splitlines(keepends=True):
        opened, consumed = None, 0
        for bracket in re.finditer(r'[\[\]]', line):
            position = bracket.start()
            if position < consumed:
                continue
            if bracket[0] == '[':
                if opened is None and (not position or line[position-1] != '^'):
                    opened = position
            else:
                if opened is not None and position > opened+1 and line[position+1:position+2] == '(':
                    end = line.find(')', position+2)
                    if end == -1:
                        break
                    if end > position+2:
                        yield offset+opened, offset+position+2, offset+end
                        consumed = end+1
                opened = None
        offset += len(line)


def markdown_link_details(raw):
    """Return whole-link and destination spans, label and href in source order.

    This uses the shared block semantics but keeps every source character's
    position. Literal code, comments, escaped math and TeX math remain intact
    even when they contain the same address as a real link elsewhere. Like the
    existing destination reader, this covers inline links, not reference-style
    definitions or arbitrary HTML attributes.
    """
    text = declaration_markdown(raw, preserve_offsets=True)

    def mask(matches):
        nonlocal text
        pieces, cursor = [], 0
        for start, end in matches:
            pieces.extend((text[cursor:start], re.sub(r'[^\r\n]', ' ', text[start:end])))
            cursor = end
        text = ''.join(pieces) + text[cursor:]

    mask((item.start(), item.end()) for item in re.finditer(
        r'\\\[.*?\\\]|\\\(.*?\\\)|(?<!\\)\$\$.*?(?<!\\)\$\$|(?<!\\)\$[^$\n]*?(?<!\\)\$', text, re.S))
    result = []
    for position, start, end in _inline_link_spans(text):
        cursor = position
        while cursor and raw[cursor-1] == '\\':
            cursor -= 1
        escapes = position - cursor
        if escapes % 2:
            continue
        # Visible masking can cross a literal segment within a would-be link;
        # only a wholly visible destination is eligible for rewriting.
        if raw[start:end] == text[start:end]:
            link_start = position
            if position and raw[position-1] == '!' and not _escaped(raw, position-1):
                link_start -= 1
            result.append((link_start, end+1, raw[position+1:start-2], start, end, raw[start:end]))
    return result


def markdown_link_spans(raw):
    """Return actual inline-link destination spans in the original Markdown."""
    return [(start, end, href) for _first, _last, _label, start, end, href
            in markdown_link_details(raw)]


def declaration_markdown(raw, *, preserve_offsets=False):
    """Structure-only view: examples cannot supply headings or table pipes.

    Cell text must still come from visible_markdown, not this mask. With the
    default comment decoding both views have identical positions; callers that
    address original link offsets use preserve_offsets on both views instead.
    Heading/anchor interpretation intentionally remains independent of this view.
    """
    return markdown_views(raw, preserve_offsets=preserve_offsets)[1]


def table_pipes(line):
    """Offsets of unescaped, eligible delimiters in a table structure view."""
    return [item.start() for item in re.finditer(r'(?<!\\)\|', line)]


def destination(document, link):
    link = link.strip().strip('<>')
    if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', link):
        return None
    path, _, anchor = link.partition('#')
    path, anchor = unquote(path), unquote(anchor)
    path = path.replace('\\', '/')
    if path.startswith('/'):
        raise ValueError('Absolute local link: ' + link)
    target = posixpath.normpath(posixpath.join(posixpath.dirname(document), path)) if path else document
    if target == '..' or target.startswith('../') or any(p.casefold() in {'.git', '.codex', '.agents'} for p in target.split('/')):
        raise ValueError('Unsafe local link: ' + link)
    return target, anchor


def destinations(document, text):
    return {d for _, _, href in markdown_link_spans(text) if (d := destination(document, href)) is not None}


def check_files(root, names):
    """Check local links in these files; do not inventory materials or source bytes.

    Source-store targets receive path-containment checks only. Selected source
    presence, hashes and native anchors belong to an explicitly scoped source read.
    """
    from pathlib import Path
    from . import paths
    root = Path(root).resolve()
    texts, targets, anchors, errors = {}, {}, {}, []

    def text(path):
        if path not in texts: texts[path] = path.read_bytes().decode('utf-8-sig')
        return texts[path]

    for value in dict.fromkeys(names):
        name = Path(value).as_posix()
        try:
            if Path(value).is_absolute(): raise ValueError('Choose repository-relative public files.')
            paths.check_public_target(name)
            raw = text(paths.ordinary_path(root, name))
            for _offset, _label, href in markdown_link_spans(raw):
                selected = destination(name, href)
                if selected is None: continue
                target, anchor = selected
                paths.check_public_target(target)
                if paths.in_pdf_store(Path(target)):
                    continue
                if target not in targets:
                    located = paths.ordinary_path(root, target)
                    targets[target] = located, located.exists()
                located, exists = targets[target]
                if not exists:
                    errors.append(name + ': missing local target ' + href)
                elif located.is_dir():
                    continue
                elif anchor and located.suffix.lower() == '.md':
                    if target not in anchors: anchors[target] = anchor_occurrences(text(located))
                    count = anchors[target][anchor]
                    if count != 1: errors.append(name + (': missing anchor ' if not count else ': ambiguous anchor ') + href)
        except (OSError, ValueError, UnicodeError) as error:
            errors.append(name + ': ' + str(error))
    return errors
