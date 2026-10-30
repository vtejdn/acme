"""Factual source-account reads and explicitly requested whole-store byte inventory."""
import hashlib
from pathlib import Path
import re
import subprocess
from ..core import paths as paths
from ..core import links, source_files
from ..materials.documents import MarkdownInput

REGISTRY = paths.LOCAL_REGISTRY

HASH = r'(?<![A-Fa-f0-9])[A-Fa-f0-9]{64}(?![A-Fa-f0-9])'


def _accounts(text, *, include_preamble=False):
    document = MarkdownInput(text.replace('\r\n', '\n'))
    pattern = r'^ {0,3}### ([^\n]+)\n(.*?)(?=^ {0,3}#{1,3} |\Z)'
    sections = list(re.finditer(pattern, document.structure, re.M | re.S))
    if include_preamble:
        yield 'Unsectioned source declarations', document.slice(0, sections[0].start() if sections else len(document.text))
    for section in sections:
        yield document.text[section.start(1):section.end(1)], document.slice(*section.span(2))


def _fields(body):
    tables = [rows for header, rows in body.tables() if header == ['Field', 'Value']]
    if len(tables) > 1:
        candidates = '; '.join(str(index)+': '+repr([cells for cells, _ in rows])
                               for index, rows in enumerate(tables, 1))
        raise ValueError('A source account needs one contiguous Field/Value table; competing candidates: '+candidates)
    fields = {}
    for rows in tables:
        for cells, _ in rows:
            if len(cells) != 2 or not all(cells) or cells[0].casefold() in fields:
                raise ValueError('Source account fields need distinct names and explicit values; candidate row: '+
                                 repr(cells)+'; preceding fields: '+repr(fields))
            fields[cells[0].casefold()] = cells[1]
    return fields


def local_sources(text, *, strict=True):
    """Read actual local Markdown source links, without declaring an artifact."""
    names = []
    for _, _, _, _, _, href in links.markdown_link_details(text):
        try: destination = links.destination(REGISTRY.as_posix(), href)
        except ValueError:
            if strict: raise
            continue
        if destination is None: continue
        target, _ = destination
        if target.startswith(paths.PDF_ROOT.as_posix() + '/'):
            name = target[len(paths.PDF_ROOT.as_posix()) + 1:]
            if name not in names: names.append(name)
    return names


def declarations(body, *, strict=True):
    """Explicit Artifact lines only; each fingerprint belongs to its own line."""
    rows = []
    for line, mask in zip(body.text.splitlines(), body.structure.splitlines()):
        if not re.match(r'^ {0,3}Artifact:', mask): continue
        names = local_sources(line, strict=strict)
        hashes = re.findall(r'SHA-256[ \t]+`('+HASH+r')`', line)
        if strict:
            if len(re.findall(r'SHA-256',line)) != len(hashes):
                raise ValueError('Artifact fingerprint must be one exact SHA-256 inline-code value on its declaration line.')
            if len(names) != 1:
                raise ValueError('Artifact declaration needs one exact local target; candidates: '+repr(names))
            if len(hashes) > 1:
                raise ValueError('Artifact declaration needs one explicit SHA-256; candidates: '+repr(hashes))
            if not paths.valid_source_name(names[0]):
                raise ValueError('Unsupported source path or filename: '+names[0])
        for name in names:
            rows.append((name, hashes[0].lower() if len(names) == len(hashes) == 1 else None))
    if strict and len(rows) > 1:
        raise ValueError('Ambiguous source account; choose one Artifact declaration: '+repr(rows))
    return rows


def _primary_sources(body, *, strict=True):
    primary = [name for name, _ in declarations(body,strict=strict)]
    resources = []
    for line, mask in zip(body.text.splitlines(),body.structure.splitlines()):
        if re.match(r'^ {0,3}Resource:',mask): resources.extend(local_sources(line,strict=strict))
    return primary,list(dict.fromkeys(resources))


def local_artifacts(text):
    return [name for _,body in _accounts(text) for name,_ in declarations(body) if name.lower().endswith('.pdf')]


def _source_facts(body):
    facts = {field:[] for field in ('urls','obtained_urls','versions','limitations','access_limitations')}
    labels = {'Selected source URL':'urls','Source URL':'obtained_urls','Source version':'versions',
              'Source association':'limitations','Current access limitation':'access_limitations'}
    for line, mask in zip(body.text.splitlines(),body.structure.splitlines()):
        for label,field in labels.items():
            match = re.match(r'^ {0,3}'+re.escape(label)+r':[ \t]*(.*)$',mask)
            if match:
                value = line[match.start(1):match.end(1)].strip()
                if value and value not in facts[field]: facts[field].append(value)
    # A table is not a primary edition/fingerprint source, but actual malformed
    # declarations in a selected account remain concrete structural errors.
    _fields(body)
    return facts


def artifact_source_facts(text):
    result = {}
    for _,body in _accounts(text):
        for name,_ in declarations(body):
            if name in result: raise ValueError('Competing source accounts for '+name)
            result[name] = _source_facts(body)
    return result


def registered_sources(text, keys=None):
    expected,errors = {},[]
    for heading,body in _accounts(text):
        try:
            rows = declarations(body)
            facts = _source_facts(body) if rows else None
            for name,fingerprint in rows:
                key = name.split('/',1)[0] if '/' in name else name.removesuffix('.pdf').split('--',1)[0]
                if keys is not None and key not in keys:
                    raise ValueError('Source artifact has no canonical bibliographic key: '+name)
                if name in expected:
                    raise ValueError('Competing source accounts for '+name+'; candidates: '+repr((expected[name]['section'],heading)))
                expected[name] = {'sha256':fingerprint,'section':heading,'key':key,
                    'format':'pdf' if name.lower().endswith('.pdf') else 'html' if name.lower().endswith(('.html','.htm')) else 'resource',
                    'source':facts}
        except ValueError as error: errors.append(str(error))
    return expected,errors


def registered_pdfs(text, keys=None):
    expected,errors = registered_sources(text,keys)
    return {name:value for name,value in expected.items() if value['format']=='pdf'},errors


def _holding_candidates(body, *, selected=False):
    try: tables = list(body.tables())
    except ValueError:
        if selected: raise
        return []
    return [cells for header,rows in tables if header == ['Field','Value']
            for cells,_ in rows if len(cells) == 2]


def source_holdings(text, keys=None, *, artifacts=None):
    """Read explicit work/edition/extent relations, without guessing from titles."""
    if artifacts is None: artifacts, errors = registered_sources(text, keys)
    else: errors = []
    holdings = {}
    for heading, body in _accounts(text):
        fields = _fields(body)
        if 'holding' not in fields: continue
        key, kind = fields.get('source-key'), fields['holding']
        if not key or (keys is not None and key not in keys):
            errors.append('Source holding needs its canonical source-key: ' + heading); continue
        owner = re.match(r'([A-Za-z0-9+_.-]+)(?=[:\s])', heading)
        if owner and keys is not None and owner[1] in keys and owner[1] != key:
            errors.append('Source holding differs from its registry work key: ' + key); continue
        targets = local_sources(fields.get('source-artifact', ''))
        if len(targets) != 1 or targets[0] not in artifacts:
            errors.append('Source holding needs one explicitly registered artifact: ' + key); continue
        if kind not in {'selected source', 'complete contribution', 'partial source'}:
            errors.append('Unsupported source holding extent: ' + key); continue
        if not fields.get('source-edition'):
            errors.append('Source holding needs its explicit edition: ' + key); continue
        item = {'artifact': targets[0], 'key': key, 'coverage': kind,
                'edition': fields.get('source-edition'), 'section': heading}
        if kind == 'partial source':
            if not item['edition'] or not fields.get('source-limitation'):
                errors.append('Partial source needs its edition and actual coverage limitation: ' + key); continue
            item['limitation'] = fields['source-limitation']
        if kind == 'complete contribution':
            match = re.fullmatch(r'(\d+)\s*(?:–|--|-)\s*(\d+)', fields.get('pdf-pages', ''))
            count = fields.get('artifact-pdf-pages', '')
            if (not match or not count.isdecimal() or
                    not 1 <= int(match[1]) <= int(match[2]) <= int(count) or
                    not item['edition'] or fields.get('artifact-edition') != item['edition'] or
                    not fields.get('contribution') or not fields.get('printed-pages') or
                    artifacts[targets[0]]['format'] != 'pdf'):
                errors.append('Incomplete or conflicting contribution/edition/page association: ' + key); continue
            item.update(pdf_pages=[int(match[1]), int(match[2])], printed_pages=fields['printed-pages'],
                        contribution=fields['contribution'], artifact_pages=int(count))
        if key in holdings and holdings[key] != item:
            errors.append('Ambiguous selected source holding: ' + key)
        holdings[key] = item
    return holdings, errors


def source_accounts(registry_text, *, artifact_names=(), holding_keys=()):
    """Return exact selected accounts and a selected holding's direct artifact account.

    Reading the registry text does not make unrelated accounts validation inputs.
    Supplied artifact names select their primary accounts, never arbitrary links.
    """
    selected = set(artifact_names or ())
    holding_keys = set(holding_keys)
    sections = list(_accounts(registry_text, include_preamble=True))
    retained = set()
    for index, (heading, body) in enumerate(sections):
        owner = re.match(r'([A-Za-z0-9+_.-]+)(?=[:\s]|$)', heading)
        rows = _holding_candidates(body, selected=bool(owner and owner[1] in holding_keys))
        if not any(name.casefold() == 'holding' for name, value in rows): continue
        if not any(name.casefold() == 'source-key' and value in holding_keys for name, value in rows): continue
        targets = [target for name, value in rows if name.casefold() == 'source-artifact' for target in local_sources(value, strict=False)]
        if artifact_names is not None and not selected.intersection(targets): continue
        retained.add(index)
        selected.update(targets)
    for index, (heading, body) in enumerate(sections):
        names, resources = _primary_sources(body, strict=False)
        if not selected.intersection(names+resources): continue
        retained.add(index)
    return '# Selected source accounts\n\n' + '\n'.join('### '+heading+'\n'+body.text
        for index, (heading, body) in enumerate(sections) if index in retained)


def source_catalog(registry_text, keys=None, *, artifact_names=None, holding_keys=None):
    """Read declared relationships at the supplied metadata scope, without selecting sources."""
    if artifact_names is not None or holding_keys is not None:
        registry_text = source_accounts(registry_text, artifact_names=artifact_names, holding_keys=holding_keys or ())
    artifacts, errors = registered_sources(registry_text, keys)
    holdings, other = source_holdings(registry_text, keys, artifacts=artifacts)
    if errors or other: raise ValueError('; '.join(errors + other))
    resources = {}
    for _,body in _accounts(registry_text):
        names,related = _primary_sources(body)
        if related: resources.setdefault(names[0] if names else '',[]).extend(related)
    return {'artifacts': artifacts, 'holdings': holdings, 'resources':resources}


def holding_status(root, registry_text, key, selected=(), keys=None, *, catalog=None):
    """Display an explicit selection/holding and file presence without inspecting bytes."""
    catalog = catalog or source_catalog(registry_text, keys, artifact_names=selected or None, holding_keys=(key,))
    artifacts, holdings = catalog['artifacts'], catalog['holdings']
    holding = holdings.get(key, {})
    names = list(dict.fromkeys(selected)) or ([holding['artifact']] if holding else [])
    if not names and not holding: return None
    result = {'coverage': holding.get('coverage'), 'edition': holding.get('edition'),
              'artifacts': [], 'resources': [], 'notices': []}
    if holding.get('limitation'):
        result['notices'].append('Recorded source limitation: '+key+'; '+holding['limitation'])
    for name in names:
        identity = artifacts.get(name)
        if identity is None:
            result['notices'].append('Explicit source artifact is not registered: '+name)
            continue
        facts = identity['source']
        result['notices'] += ['Recorded source limitation: '+name+'; '+value
                              for value in facts['limitations'] + facts['access_limitations']]
        target = paths.source_path(root, paths.PDF_ROOT/name, work_key=identity['key'])
        available = target.is_file()
        result['artifacts'].append({'path': (paths.PDF_ROOT/name).as_posix(), 'format': identity['format'],
                                    'available': available, 'source': facts})
        for related in catalog.get('resources',{}).get(name,[]):
            target = paths.source_path(root,paths.PDF_ROOT/related)
            result['resources'].append({'path':(paths.PDF_ROOT/related).as_posix(),
                                        'available':target.is_file(),'registered':related in artifacts})
        if not available: result['notices'].append('Registered source is unavailable: '+name)
    return result


def check(root):
    root = Path(root).resolve()
    report = {'storage': paths.PDF_ROOT.as_posix(), 'target': None, 'kind': None,
              'registered': 0, 'verified': 0, 'missing': [], 'resources': [], 'errors': [], 'warnings': []}
    try:
        registry = paths.ordinary_path(root, REGISTRY)
        from ..intake import bibliography as bib
        entries = bib.parse((root/bib.BIB).read_text(encoding='utf-8-sig')) if (root/bib.BIB).exists() else None
        registry_text = registry.read_text(encoding='utf-8-sig') if registry.exists() else ''
        expected, errors = registered_sources(registry_text, entries)
        holdings, holding_errors = source_holdings(registry_text, entries)
        errors.extend(holding_errors)
        for key, holding in holdings.items():
            if holding['coverage'] == 'partial source':
                report['warnings'].append('Partial source holding: ' + key + '; ' + holding['limitation'])
        if entries is not None:
            report['errors'].extend(bib.check(entries))
        report['registered'] = len(expected)
        report['errors'].extend(errors)
        report['warnings'].extend('Recorded source limitation: '+name+'; '+value
                                  for name, identity in expected.items()
                                  for value in identity['source']['limitations'] + identity['source']['access_limitations'])
        for _,body in _accounts(registry_text):
            for name in _primary_sources(body)[1]:
                try:
                    file = paths.source_path(root,paths.PDF_ROOT/name)
                    report['resources'].append({'path':(paths.PDF_ROOT/name).as_posix(),
                                                'available':file.is_file(),'registered':name in expected})
                except (OSError,ValueError) as error: report['errors'].append(str(error))
        mount, target = paths.pdf_storage(root)
        report['target'] = str(target)
        report['kind'] = 'junction' if mount.is_junction() else ('symlink' if mount.is_symlink() else 'directory')
        if mount.is_dir():
            # Never recurse into external storage, even if it contains directories.
            for item in mount.iterdir():
                if paths.is_reparse(item):
                    report['errors'].append(f'Unexpected nested link in PDF storage: {item.name}')
                elif item.is_dir():
                    groups = {name.split('/', 1)[0] for name in expected if '/' in name}
                    if item.name not in groups:
                        report['errors'].append(f'Unsupported PDF subdirectory: {item.name}; only registered HTML work groups are supported.')
        elif expected:
            report['warnings'].append(f'PDF directory/junction target is unavailable: {paths.PDF_ROOT.as_posix()}')
        for name, identity in sorted(expected.items()):
            try:
                file = paths.source_path(root, paths.PDF_ROOT / name, work_key=identity['key'])
                if not file.is_file():
                    report['missing'].append(name)
                    label = 'PDF' if identity['format'] == 'pdf' else 'source page/resource'
                    report['warnings'].append(f'Missing registered {label}: {name}; bibliography and source inspection scope remain available.')
                    continue
                digest = hashlib.sha256()
                with file.open('rb') as stream:
                    prefix = stream.read(5)
                    digest.update(prefix)
                    for block in iter(lambda: stream.read(1024 * 1024), b''):
                        digest.update(block)
                info = source_files.validate(prefix if identity['format'] == 'pdf' else file.read_bytes(), name)
                if info['format'] == 'html':
                    unretained = [href for href in info['resources'] if not href.lower().startswith('data:') and
                                  source_files.local_resource(name, href) not in expected]
                    if unretained:
                        report['warnings'].append(f'HTML related resources not retained: {name}; {len(unretained)} references; '
                                                  'only explicitly registered files are checked; no offline visual completeness is claimed.')
                label = 'PDF' if identity['format'] == 'pdf' else 'Source'
                if identity['sha256'] is None:
                    report['warnings'].append(f'Available {label} has no recorded byte fingerprint: {name}')
                elif digest.hexdigest() != identity['sha256']:
                    # Registered identity is retained for reference; changed bytes are a reminder, not corruption.
                    report['warnings'].append(f'{label} fingerprint mismatch: {name} ({identity["section"]})')
                else:
                    report['verified'] += 1
            except (OSError, ValueError, RuntimeError) as error:
                report['errors'].append(f'{name}: {error}')
        if (root / '.git').exists():
            tracked = subprocess.run(['git', 'ls-files', '-z', '--', paths.PDF_ROOT.as_posix()], cwd=root,
                                     capture_output=True, check=True).stdout
            if tracked:
                report['errors'].append('Local PDF storage or its link is tracked by Git.')
            ignored = subprocess.run(['git', 'check-ignore', '-q', '--', paths.PDF_ROOT.as_posix()],
                                     cwd=root, capture_output=True)
            if ignored.returncode != 0:
                report['errors'].append(f'{paths.PDF_ROOT.as_posix()} is not excluded from Git.')
    except (OSError, ValueError, RuntimeError, subprocess.SubprocessError) as error:
        report['errors'].append(str(error))
    return report
