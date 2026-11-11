"""Chosen bibliography fields and explicit retrieval; no source accounts."""
import os
from pathlib import Path
from urllib.request import Request, urlopen
from ..core import repository as r, paths, source_files
from . import bibliography as bib


def fetch(url, timeout=12, *, source_format='pdf'):
    """Fetch one supplied address and return original bytes and actual final URL."""
    request = Request(url, headers={'User-Agent': 'ACME-source-reader/1.0'})
    with urlopen(request, timeout=timeout) as response:
        data = response.read(64 * 1024 * 1024 + 1)
        r.require(len(data) <= 64 * 1024 * 1024, 'Source response exceeds the bounded byte limit.')
        return data, response.geturl()


def fetch_html(url, timeout=12):
    return fetch(url, timeout, source_format='html')


def fetch_source(urls, output, *, root, source_format='pdf', retrieve=None):
    """Return an unestablished response for inspection, without registering it."""
    urls = list(dict.fromkeys(urls))
    r.require(1 <= len(urls) <= 2, 'Supply one or two exact retrieval addresses.')
    r.require(source_format in {'pdf', 'html'}, 'Select PDF or HTML format facts.')
    root = paths.resolved_path(root)
    output = Path(output)
    if output.is_absolute():
        r.require(output.is_relative_to(root), 'Local output must stay inside the selected repository.')
        output = output.relative_to(root)
    source_prefix = paths.PDF_ROOT.parts
    source_output = output.parts[:len(source_prefix)] == source_prefix and len(output.parts) > len(source_prefix)
    temporary_output = output.parts[:1] == ('.tmp',) and len(output.parts) > 1
    r.require(source_output or temporary_output,
              'Choose an output beneath root .tmp/ or mathematics/literature/pdf/.')
    if source_output:
        r.require(output.suffix.lower() in ({'.pdf'} if source_format == 'pdf' else {'.html', '.htm'}),
                  'A retained original filename must agree with its selected source format.')
        destination = paths.source_path(root, output)
    else:
        if os.name == 'nt':
            r.require(all(part.rstrip(' .') == part for part in output.parts),
                      'Choose a canonical disposable output path without trailing-dot or space aliases.')
        destination = paths.material_path(root, output)
        r.require(destination.is_relative_to(root / '.tmp') and destination != root / '.tmp',
                  'A disposable response must resolve beneath root .tmp/.')
    r.require(not destination.exists(), 'Local output already exists; choose an unoccupied destination.')
    retrieve = retrieve or (fetch_html if source_format == 'html' else fetch)
    attempts = []
    for url in urls:
        response = {'requested_url': url, 'final_url': None}
        try:
            raw, final = retrieve(url)
            response.update(final_url=final, bytes=len(raw))
            info = source_files.validate(raw, 'response.' + source_format)
            response['format_facts'] = _json_info(info)
            destination.parent.mkdir(parents=True, exist_ok=True)
            r.write_bytes(destination, raw, exclusive=True, root=None if source_output else root)
            attempts.append(response)
            return {'available': True, 'local_file': str(destination.resolve()), 'association': 'unestablished', 'attempts': attempts}
        except (OSError, ValueError) as error:
            response['error'] = str(error)
            attempts.append(response)
    return {'available': False, 'local_file': None, 'association': 'unestablished', 'attempts': attempts}


def _json_info(info):
    return {field: sorted(value) if isinstance(value, set) else value for field, value in info.items()}


def _entry_snapshot(repo, existing_key):
    path = r.safe_path(repo.root, bib.BIB)
    text = path.read_bytes().decode('utf-8-sig') if path.exists() else ''
    entries = bib.parse(text)
    if existing_key is not None:
        r.require(existing_key in entries, 'Chosen existing bibliography key is absent: ' + existing_key)
        current = entries[existing_key]
        return current.kind, current.fields.copy()
    return None


def _choose(entries, entry, *, existing_key, new_work, chosen_key, field_updates, snapshot):
    r.require(bool(new_work) != (existing_key is not None), 'Choose an existing key or explicitly choose a new work.')
    updates = dict(entry.fields) if entry is not None else {}
    updates.update(field_updates or {})
    if existing_key is not None:
        r.require(chosen_key is None, 'A chosen new key requires a new-work selection.')
        current = entries.get(existing_key)
        r.require(current is not None and (current.kind, current.fields) == snapshot,
                  'Chosen bibliography entry changed during preparation; retry with current explicit inputs.')
        fields = current.fields.copy()
        for field, value in updates.items():
            if value is None: fields.pop(field, None)
            else: fields[field] = value
        selected = bib.Entry(current.kind, existing_key, fields)
    else:
        r.require(entry is not None, 'A new work needs the supplied bibliographic entry.')
        key = chosen_key or bib.allocate(entries, entry)
        r.require(key.casefold() not in {value.casefold() for value in entries}, 'Chosen new bibliography key is occupied: ' + key)
        selected = bib.Entry(entry.kind, key, updates)
    r.require(not bib.check({selected.key: selected}), '; '.join(bib.check({selected.key: selected})))
    entries[selected.key] = selected
    return selected.key


def register_work(repo, entry=None, *, existing_key=None, new_work=False, chosen_key=None, field_updates=None, timeout=30):
    """Apply exact chosen bibliographic fields without creating an artifact account."""
    snapshot = _entry_snapshot(repo, existing_key)
    with r.locked(repo.root, timeout=timeout):
        path = r.safe_path(repo.root, bib.BIB)
        original = path.read_bytes() if path.exists() else None
        entries = bib.parse(original.decode('utf-8-sig')) if original is not None else {}
        key = _choose(entries, entry, existing_key=existing_key, new_work=new_work, chosen_key=chosen_key,
                      field_updates=field_updates, snapshot=snapshot)
        updated = bib.edit_selected(original, {key: entries[key]})
        if updated != original:
            r.write_bytes(path, updated, root=repo.root)
    return key
