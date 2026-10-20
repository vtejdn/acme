"""Validate retained source formats without converting or executing them."""
import codecs
from html.parser import HTMLParser
import posixpath
import re
from urllib.parse import unquote, urlsplit


class _HTML(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.anchors, self.resources, self.text = set(), [], []
        self.title, self.in_title, self.in_head, self.hidden, self.document = [], False, False, 0, False

    def handle_starttag(self, tag, pairs):
        attrs = dict(pairs)
        if tag in {'html', 'body'}: self.document = True
        if tag == 'head': self.in_head = True
        if tag in {'script', 'style'}: self.hidden += 1
        if tag == 'title': self.in_title = True
        for field in ('id', 'name'):
            if attrs.get(field): self.anchors.add(attrs[field])
        if tag in {'img', 'source'} and attrs.get('src'):
            self.resources.append(attrs['src'])
        if tag == 'img' and attrs.get('alt') and not self.hidden and not self.in_head:
            self.text.append(attrs['alt'])

    def handle_endtag(self, tag):
        if tag in {'script', 'style'}: self.hidden = max(0, self.hidden - 1)
        if tag == 'title': self.in_title = False
        if tag == 'head': self.in_head = False

    def handle_data(self, data):
        if self.in_title: self.title.append(data)
        if not self.hidden and not self.in_title and not self.in_head and data.strip(): self.text.append(data)


def html_info(data):
    """Inspect a disposable decoded view; callers retain the original bytes."""
    if not data.strip(): raise ValueError('Empty HTML source.')
    encoding = next((encoding for marker, encoding in
                     ((codecs.BOM_UTF32_LE,'utf-32'),(codecs.BOM_UTF32_BE,'utf-32'),
                      (codecs.BOM_UTF16_LE,'utf-16'),(codecs.BOM_UTF16_BE,'utf-16'),
                      (codecs.BOM_UTF8,'utf-8-sig')) if data.startswith(marker)),None)
    if encoding is None:
        declared = re.search(br'<meta\b[^>]*(?:charset\s*=\s*[\"\']?\s*)([A-Za-z0-9_.-]+)', data[:8192], re.I)
        encoding = declared[1].decode('ascii') if declared else 'utf-8'
    try:
        text = data.decode(encoding)
    except UnicodeDecodeError as error:
        if encoding != 'utf-8': raise ValueError('HTML bytes do not match their declared encoding.') from error
        # HTML without an encoding declaration commonly uses Windows-1252.
        try:
            encoding, text = 'windows-1252', data.decode('windows-1252')
        except UnicodeDecodeError as fallback_error:
            raise ValueError('HTML bytes have no supported readable encoding.') from fallback_error
    except LookupError as error:
        raise ValueError('Unsupported declared HTML encoding.') from error
    page = _HTML()
    page.feed(text); page.close()
    title = ' '.join(page.title).strip()
    return {'encoding': encoding, 'title': title, 'anchors': page.anchors,
            'resources': page.resources, 'text': '\n'.join(page.text),
            'bytes': len(data), 'document_tags': page.document}


def local_resource(filename, href):
    """Locate a contained relative reference; its URL grants no file authority."""
    from .paths import valid_source_name
    try:
        uri = urlsplit(href)
    except ValueError:
        return None
    if uri.scheme or uri.netloc or uri.path.startswith('/') or not uri.path:
        return None
    name = posixpath.normpath(posixpath.join(posixpath.dirname(filename), unquote(uri.path)))
    group = filename.split('/', 1)[0]
    return name if name.startswith(group + '/') and valid_source_name(name) else None


def validate(data, filename):
    if filename.lower().endswith('.pdf'):
        if not data.startswith(b'%PDF-'): raise ValueError('Invalid PDF signature: ' + filename)
        return {'format': 'pdf'}
    if filename.lower().endswith(('.html', '.htm')):
        return {'format': 'html', **html_info(data)}
    if not data: raise ValueError('Empty retained source resource: ' + filename)
    return {'format': 'resource'}
