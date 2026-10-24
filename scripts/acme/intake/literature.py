"""Explicit bibliographic updates, factual fetch and selected local-source retention."""
import hashlib
from pathlib import Path
from urllib.parse import quote
from urllib.request import Request, urlopen
from ..core import repository as r, paths, links, source_files
from . import bibliography as bib

REGISTRY = 'mathematics/literature/registry.md'
FACT_FIELDS = ('urls', 'obtained_urls', 'versions', 'limitations', 'access_limitations')


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
    root = Path(root).resolve()
    output = Path(output)
    if output.is_absolute():
        r.require(output.is_relative_to(root), 'Local output must stay inside the selected repository.')
        output = output.relative_to(root)
    destination = paths.material_path(root, output)
    r.require(not destination.exists(), 'Local output already exists; choose an unoccupied destination.')
    retrieve = retrieve or (fetch_html if source_format == 'html' else fetch)
    attempts = []
    for url in urls:
        response = {'requested_url': url, 'final_url': None}
        try:
            raw, final = retrieve(url)
            response.update(final_url=final, bytes=len(raw), sha256=hashlib.sha256(raw).hexdigest())
            info = source_files.validate(raw, 'response.' + source_format)
            response['format_facts'] = _json_info(info)
            destination.parent.mkdir(parents=True, exist_ok=True)
            r.write_bytes(destination, raw, exclusive=True, root=root)
            attempts.append(response)
            return {'available': True, 'local_file': str(destination.resolve()), 'association': 'unestablished', 'attempts': attempts}
        except (OSError, ValueError) as error:
            response['error'] = str(error)
            attempts.append(response)
    return {'available': False, 'local_file': None, 'association': 'unestablished', 'attempts': attempts}


def _json_info(info):
    return {field: sorted(value) if isinstance(value, set) else value for field, value in info.items()}


def _local_bytes(filename):
    """A named source attachment can be unavailable; it never selects another file."""
    if filename is None: return None
    try: return Path(filename).read_bytes()
    except FileNotFoundError: return None


def _entry_snapshot(repo, existing_key):
    text = (repo.root/bib.BIB).read_text(encoding='utf-8-sig') if (repo.root/bib.BIB).exists() else ''
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


def register(repo, entry=None, *, existing_key=None, new_work=False, chosen_key=None, field_updates=None,
             local_pdf=None, local_html=None, html_name='source.html', source_format='pdf', suffix='',
             timeout=30, source_facts=None, registry_update=None):
    """Register the agent's chosen work/artifact association from explicit local bytes."""
    r.require(local_pdf is None or local_html is None, 'Select one actual source format per registration.')
    if local_html is not None: source_format = 'html'
    r.require(source_format in {'pdf', 'html'}, 'Source registration supports PDF or original HTML.')
    r.require(not suffix or (suffix.startswith('--') and paths.valid_pdf_name('Abc26'+suffix+'.pdf')), 'Use an explicit --edition artifact suffix.')
    snapshot = _entry_snapshot(repo, existing_key)
    supplied = local_html if source_format == 'html' else local_pdf
    raw = _local_bytes(supplied)
    if raw is not None:
        source_files.validate(raw, 'source.' + source_format)
    with r.locked(repo.root, timeout=timeout):
        entries = bib.parse((repo.root/bib.BIB).read_text(encoding='utf-8-sig')) if (repo.root/bib.BIB).exists() else {}
        key = _choose(entries, entry, existing_key=existing_key, new_work=new_work, chosen_key=chosen_key,
                      field_updates=field_updates, snapshot=snapshot)
        if source_format == 'html':
            r.require(not suffix and html_name.lower().endswith(('.html', '.htm')), 'Select a contained original HTML filename.')
            filename = key + '/' + html_name
        else: filename = key + suffix + '.pdf'
        return _publish(repo, entries, key, filename, raw, source_facts, registry_update)


def _facts(current, supplied):
    """Retain recorded facts unless the caller explicitly updates that field."""
    current = current or {}
    result = {field: list(current.get(field, ())) for field in FACT_FIELDS}
    if supplied is not None:
        r.require(not set(supplied) - set(FACT_FIELDS), 'Unsupported source fact field.')
        for field, values in supplied.items():
            r.require(isinstance(values, (list, tuple)) and all(isinstance(value, str) and '\n' not in value and '\r' not in value for value in values), 'Source facts are lists of literal strings.')
            result[field] = list(dict.fromkeys(values))
    return result


def target_path(root, name):
    return (paths.source_path(root,name) if paths.in_pdf_store(Path(name))
            else r.safe_path(root,name))


def _new_account(repo, request, digest, facts):
    key,filename,raw = request['key'],request['filename'],request['raw']
    body = '### '+key+': source artifact\n\n'
    body += ('Bibliography: `'+key+'` in [references.bib](references.bib).\n'
             'Recorded by '+repo.actor()+'.\n')
    body += ('Access date: ' if raw is None else 'Acquisition date: ')+repo.now()+'.\n\n'
    body += 'Artifact: ['+filename+'](pdf/'+quote(filename,safe='/._-')+'). '
    body += 'Selected local artifact is unavailable.' if raw is None else 'Retained unchanged.'
    if digest: body += ' SHA-256 `'+digest+'`.'
    body += '\n'
    labels = {'urls':'Selected source URL','obtained_urls':'Source URL','versions':'Source version',
              'limitations':'Source association','access_limitations':'Current access limitation'}
    for field,values in facts.items():
        for value in values: body += '\n'+labels[field]+': '+value+'\n'
    if raw is not None and filename.lower().endswith(('.html','.htm')):
        info = source_files.html_info(raw)
        body += '\nOriginal HTML; encoding '+info['encoding']+'; title '+info['title']+'.\nRetained without conversion.\n'
    return body


def prepare_sources(repo, entries, requests, text, *, registry_update=None):
    """Prepare one selected batch without publishing any shared file."""
    from ..checks import literature as storage
    from .addresses import prepared_text
    # A prepared resolution is evaluated before strict reading of old ambiguity.
    updated = prepared_text(text,registry_update) if registry_update is not None else text
    gathered, pending, expected, results = {}, {}, {}, {}
    for request in requests:
        r.require('expected_sha256' not in request, 'Supplied fingerprint inputs are not supported; use actual local bytes.')
        key,filename,raw = request['key'],request['filename'],request['raw']
        r.require(key in entries,'Register the chosen work before its source: '+key)
        target = paths.source_path(repo.root,paths.PDF_ROOT/filename,work_key=key)
        name = (paths.PDF_ROOT/filename).as_posix()
        old_bytes = target.read_bytes() if target.exists() else None
        expected[name] = old_bytes
        digest = hashlib.sha256(raw).hexdigest() if raw is not None else None
        if raw is not None:
            source_files.validate(raw,filename)
            r.require(old_bytes is None or old_bytes == raw,'Different bytes occupy the selected artifact address: '+filename)
        else:
            r.require(old_bytes is None,'Selected source destination/account is occupied: '+filename+'; supply the chosen bytes.')
        # Preserve only the selected account's unambiguous existing baseline.
        old_rows = [(actual,sha) for _,body in storage._accounts(text)
                    if any(actual == filename for actual,_ in storage.declarations(body,strict=False))
                    for actual,sha in storage.declarations(body,strict=False)]
        old_constraints = {sha for actual,sha in old_rows if actual == filename and sha} if len(old_rows) == 1 else set()
        if raw is None and old_constraints:
            digest = next(iter(old_constraints))
        r.require(not old_constraints or old_constraints == {digest},
                  ('Selected source destination/account is occupied with a registered fingerprint: ' if raw is None else
                   'Supplied artifact differs from its registered fingerprint: ')+filename+'; '+repr(sorted(old_constraints)))
        catalog = storage.source_catalog(updated,entries,artifact_names=[filename])
        current = catalog['artifacts'].get(filename)
        facts = _facts(current['source'] if current else None,request.get('source_facts'))
        chosen = (key,raw,digest,facts)
        if filename in gathered:
            r.require(gathered[filename] == chosen,'Conflicting selected source requests: '+filename+
                      '; key/fingerprint/facts: '+repr((gathered[filename][::2],chosen[::2],gathered[filename][3],facts)))
            continue
        gathered[filename] = chosen
        if registry_update is None:
            if current:
                r.require(facts == current['source'] and digest == current['sha256'],
                          'Existing source account needs an explicit prepared registry update: '+filename)
            else:
                updated = updated.rstrip()+'\n\n'+_new_account(repo,request,digest,facts)+'\n'
        else:
            r.require(current is not None,'Prepared registry must select one actual artifact account: '+filename)
        current = storage.source_catalog(updated,entries,artifact_names=[filename])['artifacts'][filename]
        r.require(current['sha256'] == digest and current['source'] == facts,
                  'Prepared registry facts or fingerprint disagree with supplied current source facts: '+filename)
        if raw is not None and old_bytes is None: pending[name] = raw
        notices = (['Registered source is unavailable: '+filename] if raw is None else [])
        notices += ['Recorded source limitation: '+filename+'; '+value for value in facts['limitations']+facts['access_limitations']]
        results[filename] = {'key':key,'artifact':filename,'available':raw is not None,'sha256':digest,
                             'source':current['source'],'notice':'; '.join(notices) or None}
    return updated,pending,expected,results


def publish_files(repo, pending, expected):
    """Publish through the shared guard with the actual source-store locator."""
    from ..core.publication import publish_files as publish
    return publish(repo, pending, expected, locate=target_path)


def _publish(repo, entries, key, filename, raw, source_facts, registry_update=None):
    expected = {name:(repo.root/name).read_bytes() if (repo.root/name).exists() else None for name in (bib.BIB,REGISTRY)}
    text = expected[REGISTRY].decode('utf-8-sig') if expected[REGISTRY] is not None else '# Source acquisition registry\n'
    request = {'key':key,'filename':filename,'raw':raw,'source_facts':source_facts}
    updated,pending,source_expected,results = prepare_sources(repo,entries,[request],text,registry_update=registry_update)
    expected.update(source_expected)
    if updated != text: pending[REGISTRY] = updated.encode('utf8')
    old_bib = expected[bib.BIB]
    if old_bib is None or bib.parse(old_bib.decode('utf-8-sig')) != entries: pending[bib.BIB] = bib.render(entries).encode('utf8')
    publish_files(repo,pending,expected)
    return results[filename]


def register_resource(repo, key, local_file, relative, *, source_facts=None, timeout=30, registry_update=None):
    """Copy one explicitly selected resource and preserve its recorded limitations."""
    raw = _local_bytes(local_file)
    name = key + '/' + relative
    r.require(paths.valid_source_name(name) and not name.lower().endswith(('.pdf','.html','.htm')),
              'Select a contained related resource; entry pages use source registration.')
    if raw is not None: source_files.validate(raw, name)
    with r.locked(repo.root, timeout=timeout):
        entries = bib.parse((repo.root/bib.BIB).read_text(encoding='utf-8-sig'))
        r.require(key in entries, 'Register the chosen work before its resource.')
        # The common publisher retains the same literal source account facts.
        return _publish(repo, entries, key, name, raw, source_facts, registry_update)


def register_work(repo, entry=None, *, existing_key=None, new_work=False, chosen_key=None, field_updates=None, timeout=30):
    """Apply exact chosen bibliographic fields without creating an artifact account."""
    snapshot = _entry_snapshot(repo, existing_key)
    with r.locked(repo.root, timeout=timeout):
        path = repo.root/bib.BIB
        entries = bib.parse(path.read_text(encoding='utf-8-sig')) if path.exists() else {}
        key = _choose(entries, entry, existing_key=existing_key, new_work=new_work, chosen_key=chosen_key,
                      field_updates=field_updates, snapshot=snapshot)
        r.write_bytes(path, bib.render(entries).encode('utf8'), root=repo.root)
    return key
