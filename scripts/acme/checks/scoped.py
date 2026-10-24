"""Check explicit selected material fields and changed Git-tree references."""
from pathlib import Path
import re
import subprocess
from ..core import repository as r
from ..core import identity as identity
from ..core import links as links
from ..materials import identity as names
from ..materials import documents as documents
from ..materials import runtime as runtime


def delta(tree, before):
    if before.ref is None:
        return set(tree.names), {}
    args = ['git', 'diff', '--name-status', '-z', '-M']
    if tree.ref == 'INDEX':
        args += ['--cached', before.ref]
    elif tree.ref == 'WORKTREE':
        args += [before.ref]
    else:
        args += [before.ref, tree.ref]
    result = subprocess.run(args, cwd=tree.root, capture_output=True)
    r.require(result.returncode == 0, 'Cannot select changed paths: ' + result.stderr.decode(errors='replace'))
    values = iter(result.stdout.decode().split('\0')[:-1])
    changed, renames = set(), {}
    for status in values:
        path = next(values); changed.add(path)
        if status.startswith(('R', 'C')):
            target = next(values); changed.add(target); renames[target] = path
    changed.update(tree.names - before.names)
    changed.update(before.names - tree.names)
    return changed, renames


def view_for(tree):
    view = tree.research_view()
    view.selected_tree = tree
    view.read_document = lambda path: r.json_from(view, path)
    return view


def registry_blocks(raw):
    """Slice actual registry accounts, preserving explicit preceding anchors."""
    raw = raw.replace('\r\n', '\n')
    structure = links.declaration_markdown(raw, preserve_offsets=True)
    starts = [match.start() for match in re.finditer(r'^ {0,3}#{1,3} [^\n]+', structure, re.M)]
    starts = [0, *starts] if not starts or starts[0] else starts
    for index in range(1, len(starts)):
        prefix = raw[:starts[index]]
        preceding = re.search(r'(?:^|\n)(?:<a\s+(?:id|name)=[^\n]+>[^\n]*\n[ \t]*\n?)+\Z', prefix)
        if preceding:
            starts[index] = preceding.start() + int(raw[preceding.start():].startswith('\n'))
    return [raw[start:end] for start, end in zip(starts, [*starts[1:], len(raw)])]


def changed_registry(tree, parents, path):
    """Return added/edited prose for ordinary links, not source validation."""
    from collections import Counter
    current = registry_blocks(tree.bytes(path).decode('utf-8-sig'))
    selected = set()
    for parent in parents:
        old = Counter(registry_blocks(parent.bytes(path).decode('utf-8-sig'))) if path in parent.names else Counter()
        for block in current:
            if old[block]: old[block] -= 1
            else: selected.add(block)
    return '\n'.join(block for block in current if block in selected)


def external_changes(tree, parents, changed):
    """Check changed external rows and their table-local counterparts only."""
    from ..core import external
    tables = {external.REPOSITORIES: ('repo', 'repositories'), external.PEOPLE: ('author', 'people')}
    selected = changed & tables.keys()
    if not selected: return set()
    view = view_for(tree)
    affected = {'repo': set(), 'author': set()}
    checked = set(selected)
    for path in sorted(selected):
        kind, field = tables[path]
        current = external.table(view, kind)
        now = {row['id']: row for row in current[field]}
        for parent in parents:
            old = parent.json(path) if path in parent.names else {}
            old = old if isinstance(old, dict) else {}
            prior_rows = old.get(field) if isinstance(old.get(field), list) else []
            previous = {row['id']: row for row in prior_rows
                        if isinstance(row, dict) and isinstance(row.get('id'), str)}
            if type(old.get('next')) is int:
                r.require(current['next'] >= old['next'], path + '.next cannot reuse an issued number.')
            affected[kind].update(key for key in now.keys() | previous.keys() if now.get(key) != previous.get(key))
    external.check_rows(view, affected['repo'], affected['author'])
    return checked


def external_references(tree, selections):
    """Check explicit path-to-field selections using this Git view's readers."""
    from ..core import external, source_refs
    r.require(isinstance(selections, dict), 'Select external-reference paths and their fields explicitly.')
    view = view_for(tree)
    checked, files = [], set()

    def field(owner, label, operation, *args):
        try: value = operation(*args)
        except (ValueError, KeyError, IndexError, TypeError) as error:
            raise ValueError(owner + ':' + label + ': ' + str(error)) from error
        return value

    def provenance(value, label):
        if label == 'transport.repository': return value['transport']['repository'], None
        match = re.fullmatch(r'items\[(0|[1-9][0-9]*)\]\.(source\.(repository|author)|'
                             r'output_attachments\[(0|[1-9][0-9]*)\]\.transport\.repository)', label)
        r.require(match is not None, 'Unsupported intake reference field: ' + label)
        item = value['items'][int(match[1])]
        if match[3] == 'repository': return item['source']['repository'], None
        if match[3] == 'author':
            r.require(item['kind'] in {'C', 'T', 'R', 'L', 'J'}, 'This item kind has no external author field.')
            source = item['source']
            r.require(isinstance(source['author_name'], str) and source['author_name'].strip(),
                      'source.author_name needs the qualified original name.')
            return source['repository'], (source['author'], source['author_name'])
        return item['output_attachments'][int(match[4])]['transport']['repository'], None

    for path, selected in selections.items():
        r.require(isinstance(path, str) and isinstance(selected, (list, tuple, set)) and selected
                  and all(isinstance(label, str) for label in selected) and len(selected) == len(set(selected)),
                  'Select a path and distinct nonempty reference fields.')
        r.paths.check_public_target(path)
        r.require(not r.paths.protected_path(Path(path)) and not r.paths.in_pdf_store(path),
                  'Selected reference is not a public material path: ' + path)
        if path.endswith('.md'):
            r.require(set(selected) <= {'identity', 'source_links'}, path + ': choose identity or source_links.')
            raw = tree.bytes(path).decode('utf-8-sig')
            if 'identity' in selected:
                ident, values, _ = field(path, 'identity', documents.author_header, path, raw)
                if ident.source_repository:
                    field(path, 'source_repository', external.repository, view, ident.source_repository)
                    if ident.kind in 'CTRLJ':
                        original = names.parse(values['source_material']) if 'source_material' in values else None
                        field(path, 'author/source_material', external.person,
                              view, ident.author, ident.source_repository, original.author if original else None)
                checked.append({'path': path, 'field': 'identity'})
            if 'source_links' in selected:
                for start, _end, href in links.markdown_link_spans(raw):
                    original = field(path, 'source_links@' + str(start), source_refs.parse, href.strip().strip('<>'))
                    if original is not None:
                        field(path, href, external.repository, view, original['repository'])
                        checked.append({'path': path, 'field': 'source_links@' + str(start)})
        elif re.fullmatch(r'intake/[^/]+/[^/]+\.json', path):
            value = field(path, 'JSON', tree.json, path)
            for label in sorted(selected):
                source, author = field(path, label, provenance, value, label)
                field(path, label, external.repository, view, source)
                if author is not None: field(path, label, external.person, view, author[0], source, author[1])
                checked.append({'path': path, 'field': label})
        else:
            raise ValueError(path + ': select public Markdown or an intake operation.')
        files.add(path)
    return {'files': len(files), 'fields': len(checked), 'checked': checked}


def validate(tree, parents, author, authors_by_path=None):
    r.require(not any(r.paths.private_file(Path(path)) for path in tree.names),
              'Private profile secrets cannot be published as repository artifacts.')
    import ast
    from ..intake import acquire as intake, bibliography as bib
    from ..materials import review, discovery
    view = view_for(tree)
    reader = runtime.Reader(view, parents=parents)
    deltas = [delta(tree, parent) for parent in parents]
    changed = set().union(*(item[0] for item in deltas))
    renames = {old: new for _, mapping in deltas for new, old in mapping.items()}
    canonical = set(runtime.entrances(tree.names, strict=False))
    text = lambda path, source=tree: source.bytes(path).decode('utf-8-sig')
    markdown = lambda path: path.endswith('.md') and not r.paths.protected_path(Path(path))
    visited, owners, notices = set(), set(), []
    external_checked = external_changes(tree, parents, changed)
    visited.update(external_checked)
    config_path = 'repository/config.json'
    if config_path in changed:
        names.material_next(view.config)
    for parent in parents:
        if config_path in parent.names:
            old = parent.json(config_path)
            if config_path in changed: names.material_next(view.config, old)
            people_path = 'repository/people.json'
            previous = {p['id']: p for p in parent.json(people_path)['people']}
            current = {p['id']: p for p in identity.registry(view)['people']}
            r.require(previous.keys() <= current.keys(), 'Permanent human keys cannot be removed or renamed.')
            signatures = {(sig['name'], sig['email'].casefold()): person['id'] for person in previous.values() for sig in person.get('git_identities', [])}
            for person in current.values():
                for sig in person.get('git_identities', []):
                    r.require(signatures.get((sig['name'], sig['email'].casefold()), person['id']) == person['id'], 'Git identity reassigned to a different human.')
    registry = 'mathematics/literature/registry.md'
    def local_only_location(path):
        if not r.paths.in_pdf_store(path): return False
        label = 'PDF' if path.lower().endswith('.pdf') else 'source file'
        r.require(path not in tree.names, 'Local-only ' + label + ' must not be tracked: ' + path)
        return True
    for path in sorted(tree.names):
        if r.paths.in_pdf_store(path): local_only_location(path)
    for path in sorted(changed & tree.names):
        local_only_location(path)
        if re.fullmatch(r'execution/[^/]+_E_[A-Z][0-9]+\.md', path):
            from ..execution import records
            records.validate(view, records.parse(path, text(path)), path)
        if path.startswith('intake/') and path.endswith('.json'):
            value = tree.json(path); intake.validate_operation(view, path, value)
            def selection(item):
                source, local = item['source'], item['local']
                return (item['kind'], source['repository'], source['revision'], source['path'],
                        source.get('anchor', ''), local.get('anchor', ''))
            prior_selections = set()
            for parent in parents:
                old_path = path if path in parent.names else next((old for old, new in renames.items()
                                                                  if new == path and old in parent.names), None)
                if old_path:
                    prior_selections.update(selection(item) for item in parent.json(old_path)['items'])
            added = [item for item in value['items'] if selection(item) not in prior_selections]
            if added:
                intake.validate_operation(view, path, {**value, 'items': added}, new_selection=True)
            if not any(path in parent.names for parent in parents):
                r.require(value['recorded_by'] in (authors_by_path or {}).get(path, {author}), 'Intake recorder differs from the actual contributor.')
            visited.add(path)
        elif path.endswith('.json'): tree.json(path)
        if path == 'framework/export-manifest.json':
            from ..framework import export
            manifest = tree.json(path); r.version.validate_manifest(manifest)
            for name in set(manifest['copy']) | set(manifest['templates'].values()):
                export.relative(name); export.refuse_history(name)
                r.require(name in tree.names and tree.modes.get(name) not in {'120000', '160000'}, 'Missing or unsafe export input: ' + name)
            runtime_sources = {name for name in tree.names if name.startswith('scripts/') and name.endswith('.py')}
            r.require(runtime_sources <= set(manifest['copy']), 'Maintained runtime sources missing from export: ' + ', '.join(sorted(runtime_sources-set(manifest['copy']))))
            r.require(not any(name.startswith('blueprint/') for name in manifest['copy']), 'Developer helpers/tests are not runtime exports.')
        if path.endswith('.bib'):
            current_bib = bib.parse(text(path))
            errors = bib.check(current_bib)
            r.require(not errors, '; '.join(errors))
        if path == bib.BIB:
            for parent in parents:
                if bib.BIB in parent.names:
                    for old_key in bib.parse(text(bib.BIB, parent)).keys() - current_bib.keys():
                        old_units = [p for p in tree.names if p.startswith('mathematics/audits/literature/' + old_key + '/')]
                        r.require(not old_units, 'Key maintenance left earlier source-unit history under the old key: ' + ', '.join(old_units))
    selected = changed & canonical
    siblings = set()
    for path in selected:
        siblings.update(discovery.selected(canonical, family=names.parse(path)))
    if siblings: discovery.families(siblings, reader.read, source_info=reader.source_info)
    for path in sorted(selected):
        doc = reader.check(path); owners.add(path)
        contributors = (authors_by_path or {}).get(path, {author})
        if not doc.identity.source_repository:
            r.require(doc.identity.author in contributors,
                      'Authored material belongs to its actual human; another human corrects it in a separate document: ' + path)
        elif any(path in parent.names and tree.bytes(path) != parent.bytes(path) for parent in parents):
            same_human = identity.source_author(view, doc.identity.author, doc.identity.source_repository).get('local_human')
            r.require(same_human in contributors,
                      'Changing a received authored body requires adopted same-human correspondence: ' + path)
        if doc.identity.kind == 'T':
            from ..materials import tasks
            for parent in parents:
                prior_tasks = [documents.parse(candidate, text(candidate, parent))
                               for candidate in discovery.selected(parent.names, family=doc.identity)]
                tasks.validate(doc, reader.read, previous=prior_tasks)
        # Fixed versions retain a family; a genuinely new address must also
        # respect the actual preimage's issued bound, including retired gaps.
        def same_position(candidate):
            if doc.identity.kind == 'U':
                item = names.candidate(candidate)
                return (item is not None and item['kind'] == 'U'
                        and item['source_key'] == doc.identity.source_key and item['number'] == doc.identity.number)
            return names.in_namespace(candidate, family=doc.identity)
        existing = any(any(same_position(candidate) for candidate in parent.names) for parent in parents)
        if names.namespace(doc.identity) is not None and not existing:
            established = False
            if doc.identity.source_repository:
                for parent in parents:
                    if config_path not in parent.names: continue
                    for _record, operation in intake.operations(view_for(parent)):
                        for item in operation['items']:
                            if not isinstance(item, dict) or item.get('kind') != doc.identity.kind: continue
                            local, source = item.get('local', {}), item.get('source', {})
                            if (not isinstance(local, dict) or not isinstance(local.get('path'), str)
                                    or not same_position(local['path'])): continue
                            r.require(isinstance(source, dict), 'Missing selected original-family correspondence: ' + path)
                            original = (source.get('repository'), names.parse(source['path']).family)
                            if 'source_material' in doc.header:
                                r.require(original == documents.original_family(doc),
                                          'Established receiving position belongs to another original family: ' + path)
                            else:
                                r.require(source.get('author') == doc.identity.author
                                          and names.parse(local['path']).family == doc.identity.family,
                                          'A combined receiving family retains its actual single author and per-unit accounts.')
                            established = True
            for parent in parents or (None,):
                names.check_issued(doc.identity, view.config,
                    previous=parent.json(config_path) if parent is not None and config_path in parent.names else None,
                    established=established)
        if path not in changed: continue
        # Local C/T decisions and explicitly declared R finding scopes use the
        # actual preimage; other material kinds do not author these declarations.
        if doc.identity.kind not in 'CTR' or doc.identity.source_repository:
            visited.add(path)
            continue
        previous = []
        for parent in parents:
            old_path = path if path in parent.names else next((old for old, new in renames.items() if new == path and old in parent.names), None)
            if old_path is None:
                prior = [candidate for candidate in discovery.selected(parent.names, family=doc.identity)
                         if names.parse(candidate).version < doc.identity.version]
                if prior: old_path = documents.current(prior, doc.identity.family)
            if old_path:
                old = documents.parse(old_path, text(old_path, parent), legacy=True)
                if old.identity.family == doc.identity.family: previous.append((old, parent))
        if doc.identity.kind == 'R':
            for old, _parent in previous or [(None, None)]:
                review.check_findings(doc, previous=old)
            visited.add(path)
            continue
        # A file/anchor difference does not date a mathematical decision or
        # establish a new acceptance. Agents choose new-decision checks at the
        # actual content scope; generic views retain historical precision.
        visited.add(path)
    def link_check(owner, target, anchor):
        r.paths.check_public_target(target)
        if r.paths.in_pdf_store(target): return
        if r.paths.in_computation_outputs(target):
            candidate = r.safe_path(tree.root, target)
            present = candidate.is_file() if tree.ref == 'WORKTREE' else target in tree.names
            if not present: notices.append('Local computation output unavailable in selected view: ' + target)
            return
        if local_only_location(target): return
        r.require(tree.modes.get(target) not in {'120000', '160000'}, 'Linked target is not an ordinary file: ' + target)
        if target == '.' or (target not in tree.names and any(p.startswith(target.rstrip('/') + '/') for p in tree.names)): return
        r.require(target in tree.names, owner + ': missing local target: ' + target)
        if anchor and target.endswith('.md'):
            count = tree.anchor_counts(target)[anchor]
            r.require(count == 1, owner + (': missing anchor: ' if not count else ': ambiguous anchor: ') + target + '#' + anchor)
    for path in sorted(changed & tree.names):
        if markdown(path):
            raw = text(path)
            r.require(not re.search(r'[ \t]+$', raw, re.M), path + ': trailing whitespace')
            outgoing = changed_registry(tree, parents, path) if path == registry else raw
            for destination in reader.destinations(path, outgoing):
                link_check(path, *destination)
            visited.add(path)
        elif path.endswith('.py'): ast.parse(tree.bytes(path), filename=path)
    return {'materials': len(owners), 'changed_paths': len(changed), 'checked_items': len(visited),
            'external_table_files': len(external_checked),
            'notices': sorted(set(notices))}
