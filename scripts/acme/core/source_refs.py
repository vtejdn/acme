"""Explicit original-repository locators for references outside acquired scope."""
from urllib.parse import quote, unquote, urlsplit
from pathlib import PurePosixPath
import re
    

def make(repository, revision, path, anchor=''):
    value = 'acme-source://' + repository + '/' + revision + '/' + quote(path, safe='/._-')
    value += '#' + quote(anchor, safe='._-') if anchor else ''
    parse(value)
    return value


def parse(value):
    parts = urlsplit(value)
    if parts.scheme != 'acme-source':
        return None
    if not re.fullmatch(r'repo[1-9][0-9]*', parts.netloc) or parts.query:
        raise ValueError('Invalid original repository locator.')
    revision, separator, path = unquote(parts.path.lstrip('/')).partition('/')
    item = PurePosixPath(path)
    if (not separator or not re.fullmatch(r'[0-9a-f]{40}|[0-9a-f]{64}', revision)
            or not path or item.is_absolute() or '..' in item.parts or ':' in path or '\\' in path
            or any(p.casefold() in {'.git', '.agents', '.codex'} for p in item.parts)):
        raise ValueError('Original source locator needs a fixed revision and safe material path.')
    return {'repository': parts.netloc, 'revision': revision, 'path': path,
            'anchor': unquote(parts.fragment)}


def external(path):
    return parse(path) is not None
