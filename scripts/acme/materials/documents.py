"""Bounded material-owned decisions, independent of C/T JSON storage."""
from dataclasses import dataclass, replace
from datetime import date
from pathlib import PurePosixPath
import re
from . import identity as identity
from ..core import links as links
from ..core import repository as shared
from ..core import source_refs
from . import validation as material_checks

require = identity.require
HEADER_FIELDS = {'author', 'source_repository', 'source_material'}
FIELDS = {'date', 'status', 'reason', 'authority'}
RELATIONS = {'statement', 'contract', 'argument', 'support', 'dependency', 'review'}
CLAIM_STATES = {'open', 'proved', 'refuted'}
TASK_STATES = {'proposed', 'active', 'paused', 'blocked', 'completed', 'retired'}


@dataclass(frozen=True)
class Locator:
    path: str
    anchor: str


@dataclass
class Decision:
    anchor: str
    fields: dict
    relations: list


@dataclass
class Document:
    path: str
    identity: identity.Identity
    header: dict
    title: str
    text: str
    current: Locator | None
    decisions: dict
    task_type: str = 'ordinary'
    joint_task: Locator | None = None


def unfenced(text):
    """Visible cell content; MarkdownInput separately determines structures."""
    return material_checks.visible_markdown(text)


def table_cells(line, *, structure=None):
    """Decode the shared Markdown table cell syntax, including escaped pipes."""
    mask = line if structure is None else structure
    pipes = links.table_pipes(mask)
    require(len(line) == len(mask) and len(pipes) >= 2 and
            not line[:pipes[0]].strip() and not line[pipes[-1] + 1:].strip(),
            'Unterminated material table row.')
    return [line[start + 1:end].strip().replace('\\|', '|') for start, end in zip(pipes, pipes[1:])]


class MarkdownInput:
    """Parallel structure and semantic views for small material-owned tables.

    Keep block examples excluded and inline cell syntax within its actual
    table. Unselected rich prose supplies no state to later declarations.
    """
    def __init__(self, raw, *, structure=None):
        self.text, self.structure = (links.declaration_views(raw)
                                     if structure is None else (raw, structure))

    def slice(self, start, end):
        return MarkdownInput(self.text[start:end], structure=self.structure[start:end])

    def sections(self, heading):
        pattern = r'^ {0,3}## ' + re.escape(heading) + r'[ \t]*\r?\n(.*?)(?=^ {0,3}#{1,2}(?:[ \t]|$)|\Z)'
        return [(self.slice(*item.span(1)), self.text[:item.start(1)].count('\n'))
                for item in re.finditer(pattern, self.structure, re.M | re.S)]

    def table_blocks(self):
        """Keep original eligible rows until their table structure is known."""
        block = []
        for number, (line, mask) in enumerate(zip(self.text.splitlines(), self.structure.splitlines())):
            first = re.match(r'^[ \t]*\|', line)
            if first and mask[first.end() - 1] == '|':
                block.append((line, mask, number))
            elif block:
                yield block
                block = []
        if block:
            yield block

    def tables(self, *, minimum_dashes=1, select_row=None):
        """Read complete header/delimiter blocks; orphan fragments declare nothing."""
        for block in self.table_blocks():
            if len(block) < 2:
                continue
            line, mask, _number = block[1]
            pipes = links.table_pipes(mask)
            if len(pipes) < 2 or line[:pipes[0]].strip() or line[pipes[-1] + 1:].strip():
                continue
            delimiter = [line[start + 1:end].strip() for start, end in zip(pipes, pipes[1:])]
            if not all(re.fullmatch(r':?-{' + str(minimum_dashes) + r',}:?', cell) for cell in delimiter):
                continue
            columns = table_cells(block[0][0], structure=block[0][1])
            if len(delimiter) != len(columns):
                continue
            # Orphan blocks supply no declarations. Within a real table, an
            # explicit caller selection precedes decoding unrelated data rows.
            rows = [(table_cells(line, structure=mask), number)
                    for line, mask, number in block[2:]
                    if select_row is None or select_row(line, mask)]
            yield columns, rows

    def table(self, columns, *, minimum_dashes=1):
        tables = list(self.tables(minimum_dashes=minimum_dashes))
        require(len(tables) <= 1, 'Expected one contiguous material table.')
        if not tables:
            return []
        header, result = tables[0]
        require(header == list(columns), 'Unexpected material table header.')
        require(all(len(cells) == len(columns) and all(cells) for cells, _ in result),
                'Material relationships need all declared fields.')
        require(len({tuple(cells) for cells, _ in result}) == len(result), 'Repeated material relationship.')
        return result


SIMPLE_LINK = re.compile(r'\[([^\[\]\r\n`]+)\]\(([^()<>\s]+)\)')


def locator(path, value):
    value = value.strip()
    parsed = SIMPLE_LINK.fullmatch(value)
    require(parsed is not None and parsed[1].strip(),
            'Expected one explicit Markdown material link in simple single-line form: ' + value)
    href = parsed[2]
    original = source_refs.parse(href)
    if original is not None:
        return Locator(href.partition('#')[0], original['anchor'])
    result = links.destination(path, href)
    require(result is not None, 'Decision locators must name available repository material.')
    target, anchor = result
    from ..core import paths
    paths.check_local_role(target)
    paths.check_public_target(target)
    require(not any(p in {'.git', '.agents', '.codex'} for p in PurePosixPath(target).parts), 'Protected material locator.')
    return Locator(target, anchor)


def valid_date(value):
    # Historical calendar precision is preserved; full event values are UTC minutes.
    require(isinstance(value, str), 'Invalid decision date.')
    if re.fullmatch(r'\d{4}(?:-\d{2}(?:-\d{2})?)?', value):
        try:
            date.fromisoformat(value + ('-01-01' if len(value) == 4 else '-01' if len(value) == 7 else ''))
        except ValueError as error:
            raise ValueError('Invalid decision date: ' + value) from error
        return
    shared.valid_stamp(value)


def assessment_records(path, ident, history, *, original_material=None):
    """Read decisions under the same current contract in every source context."""
    sections = list(re.finditer(r'^ {0,3}### Decision ([A-Za-z0-9-]+)[ \t]*$', history.structure, re.M))
    decisions = {}
    for index, section in enumerate(sections):
        anchor = 'decision-' + section[1].lower()
        require(anchor not in decisions, 'Repeated decision anchor: ' + anchor)
        content = history.slice(section.end(), sections[index + 1].start() if index + 1 < len(sections) else len(history.text))
        fields, relations = {}, []
        seen = set()
        for columns, rows in content.tables():
            schema = tuple(columns)
            require(schema in {('Field', 'Value'), ('Relation', 'Target', 'Scope')},
                    'Unexpected decision table header.')
            require(schema not in seen, 'Repeated decision table.')
            seen.add(schema)
            for cells, _number in rows:
                require(len(cells) == len(schema), 'Decision row needs a real table header and separator.')
                if schema == ('Field', 'Value'):
                    key, value = cells
                    require(key in FIELDS and key not in fields and value, 'Invalid or repeated decision field: ' + key)
                    fields[key] = value
                else:
                    role, target, scope = cells
                    require(role in RELATIONS and scope, 'Decision relationship needs a role and actual scope.')
                    relations.append((role, locator(path, target), scope))
        require({'date', 'status'} <= fields.keys(), 'Decision needs date and explicit status.')
        valid_date(fields['date'])
        require(fields['status'] in (CLAIM_STATES if ident.kind == 'C' else TASK_STATES), 'Undefined mathematical disposition.')
        primary = 'statement' if ident.kind == 'C' else 'contract'
        targets = [loc for role, loc, _ in relations if role == primary]
        require(len(targets) == 1, 'Decision needs exactly one selected ' + primary + '.')
        original_primary = source_refs.parse(targets[0].path)
        selected = identity.parse(original_primary['path'] if original_primary else targets[0].path)
        require(not original_primary or original_material is not None,
                'An original primary target needs its source_material owner.')
        expected = identity.parse(original_material) if original_primary and original_material else ident
        require(selected.family == expected.family, 'Decision selects another material family.')
        if original_primary:
            require(original_primary['repository'] == ident.source_repository,
                    'Decision selects another original repository.')
        require(selected.version <= expected.version, 'Decision cannot bind a later material revision.')
        roles = {role for role, _, _ in relations}
        if ident.kind == 'T':
            require(fields.get('authority') and fields.get('reason'), 'Task decisions need reason and actual authority.')
            require(fields['status'] != 'completed' or 'review' in roles, 'Completion needs an adopted review.')
        if ident.kind == 'C' and fields['status'] in {'proved', 'refuted'}:
            require({'argument', 'review'} <= roles, 'Accepted Claim needs selected argument and review.')
        for role, loc, _ in relations:
            original = source_refs.parse(loc.path)
            target_identity = identity.parse(original['path'] if original else loc.path)
            if role == 'argument' and ident.kind == 'C':
                require(target_identity.kind == 'C', 'A Claim argument must belong to fixed C material.')
            if target_identity.kind == 'U':
                require(role in {'support', 'dependency'} and loc.anchor == target_identity.anchor,
                        'A source unit is an exact unit support/dependency, not a Claim argument or review.')
            if role in {'argument', 'support', 'dependency'}:
                require(target_identity.kind not in 'DS',
                        'A mutable draft or rolling Strategy cannot be fixed decision evidence.')
            if role == 'review':
                require(target_identity.kind in 'RL', 'Adopted reviews require fixed R/L material.')
        decisions[anchor] = Decision(anchor, fields, relations)
    return decisions


def current_decision(document, decision):
    """Check current fields without turning retained evidence into a new review."""
    if document.identity.kind == 'C':
        require(decision.fields['status'] in CLAIM_STATES, 'New/current local Claims use open, proved or refuted.')


def new_decision(document, decision):
    """Validate genuinely new declarations, leaving past/source facts readable."""
    current_decision(document, decision)
    for role, loc, _scope in decision.relations:
        if role == 'review':
            require(identity.parse(loc.path).kind == 'R', 'New/current local formal reviews require fixed R findings.')


def header_stream(stream):
    """Read only the actual scalar header from a binary file/object stream."""
    first = stream.readline()
    require(first.removeprefix(b'\xef\xbb\xbf').strip() == b'---', 'Material needs a leading author header.')
    lines = [first]
    for line in stream:
        lines.append(line)
        if line.strip() == b'---':
            return b''.join(lines).decode('utf-8-sig')
    raise ValueError('Unterminated material author header.')


def header_values(text, *, known=True):
    """Read a single scalar-author header without assigning a path identity."""
    require(text.startswith('---\n') or text.startswith('---\r\n'), 'Material needs a leading author header.')
    normalized = text.replace('\r\n', '\n')
    parts = normalized.split('\n---\n', 1)
    require(len(parts) == 2, 'Unterminated author header.')
    header = {}
    for line in parts[0].splitlines()[1:]:
        match = re.fullmatch(r'([a-z_]+):\s*(\S(?:.*\S)?)', line)
        require(match is not None and (not known or match[1] in HEADER_FIELDS), 'Invalid or unsupported header field: ' + line)
        require(match[1] not in header, 'Repeated header field: ' + match[1])
        header[match[1]] = match[2]
    require(isinstance(header.get('author'), str) and re.fullmatch(r'[A-Za-z0-9]+(?:-[A-Za-z0-9]+)*', header['author']),
            'Every mathematical document needs exactly one scalar human author.')
    return header, parts[1]


def author_header(path, text):
    """Read the shared physical identity/original binding without body validation."""
    ident = identity.parse(path)
    require(not ident.source_repository or ident.kind not in 'SD', 'External S/D mathematics uses a suitable receiving fixed home.')
    header, content = header_values(text)
    require(header.get('author') == ident.author, 'Path and author header disagree.')
    require(header.get('source_repository') == ident.source_repository, 'Path and source repository disagree.')
    source_fields = {'source_material'}
    if ident.source_repository:
        require(ident.kind != 'U' or source_fields <= header.keys(), 'A source unit needs its original material binding.')
        if 'source_material' in header:
            if ident.kind == 'U':
                # A genuine original locator is a source fact, not a second
                # local naming contract or a parser for retired U versions.
                source_refs.check_path(header['source_material'])
            else:
                original = identity.parse(header['source_material'])
                require(original.kind != 'U', 'A source unit retains its dedicated original-unit contract.')
    else:
        require(not source_fields & header.keys(), 'Local material cannot acquire an imported source binding.')
    return ident, header, content


def parse(path, text):
    ident, header, content = author_header(path, text)
    body = MarkdownInput(content)
    headings = [body.text[item.start(1):item.end(1)] for item in re.finditer(r'^# ([^\n]+)$', body.structure, re.M)]
    require(len(headings) == 1, 'Material needs one main title.')
    current, decisions = None, {}
    if ident.kind in 'CT':
        name = 'Current assessment' if ident.kind == 'C' else 'Current decision'
        sections = body.sections(name)
        require(len(sections) == 1, 'Material needs exactly one ' + name + ' section.')
        # Inline syntax is interpreted only in this explicitly selected field,
        # after block examples and unrelated sections have been excluded.
        field = links.markdown_views(sections[0][0].structure)[1].strip()
        current = locator(path, field)
        # Decision anchors and tables are parsed only in the designated history.
        history_name = 'Assessment history' if ident.kind == 'C' else 'Lifecycle and completion'
        histories = body.sections(history_name)
        require(len(histories) <= 1, 'Repeated decision history.')
        history = histories[0][0] if histories else MarkdownInput('')
        decisions = assessment_records(path, ident, history, original_material=header.get('source_material'))
    document = Document(path, ident, header, headings[0], text, current, decisions)
    if ident.kind == 'T':
        from . import tasks
        document.task_type, document.joint_task = tasks.declarations(path, body)
        require(not ident.source_repository or document.task_type == 'joint',
                'An external T is a necessary joint contract, never another human\'s ordinary Task.')
    if ident.kind == 'U':
        check_source_unit(document)
    return document


def check_source_unit(document):
    """Check the file-local unit anchor, without interpreting inspection prose."""
    require(document.identity.kind == 'U', 'Expected a rolling source-unit document.')
    require(links.anchor_occurrences(document.text)[document.identity.anchor] == 1,
            'Source unit needs its actual source-key/unit anchor.')


def original_family(document):
    """Original family under its receiving repository, independent of local serial."""
    if document.identity.source_repository:
        return (document.header['source_repository'],
                (document.header['source_material'] if document.identity.kind == 'U'
                 else identity.parse(document.header['source_material']).family) if 'source_material' in document.header
                else document.identity.family)
    return None, document.identity.family


def revision_inputs(document, read):
    """Read explicit input locators, independently of decisions and scope prose."""
    chosen = []
    sections = MarkdownInput(document.text).sections('Inputs')
    require(len(sections) <= 1, 'A material has at most one explicit Inputs section.')
    if sections:
        content = sections[0][0]
        for line, mask in zip(content.text.splitlines(), content.structure.splitlines()):
            prefix = re.match(r'[ \t]*(?:[-*] )?', line).end()
            parsed = SIMPLE_LINK.match(line, prefix)
            if parsed is not None and mask[prefix:prefix + 1] == '[':
                chosen.append(locator(document.path, parsed[0]))
    result = []
    for loc in chosen:
        if source_refs.external(loc.path):
            continue
        candidate = identity.candidate(loc.path)
        if candidate is None:
            continue
        ident = identity.parse(loc.path)
        if ident.family != document.identity.family:
            continue
        require(ident.version is not None and document.identity.version is not None
                and ident.version < document.identity.version,
                'An explicit revision input must be an earlier fixed receiving version.')
        item = {'path': loc.path, 'anchor': loc.anchor}
        if item not in result:
            result.append(item)
    return result


def selection(document, read, *, source_info=None):
    """Resolve the selected decision together with the material that owns it."""
    require(document.current is not None, 'Only C/T material has a current decision.')
    pointer = document.current
    original = source_refs.parse(pointer.path)
    if original is not None:
        require(bool(document.identity.source_repository),
                'A local Current selector cannot select an unacquired source decision.')
        require(pointer.anchor, 'Current source selector needs a nonempty decision anchor.')
        chosen = identity.parse(original['path'])
        require(chosen.kind == document.identity.kind,
                'Current source decision belongs to another material kind.')
        if 'source_material' in document.header:
            owners = {(document.header['source_repository'], document.header['source_material'])}
        else:
            require(source_info is not None,
                    'Current source selector needs its explicit original owner path and version.')
            try:
                owners = {(row['source']['repository'], row['source']['path'])
                          for row in source_info(document)['acquisitions']}
            except (FileNotFoundError, KeyError) as error:
                raise ValueError('Current source selector cannot establish its original owner path and version: '
                                 + str(error)) from error
        require(owners, 'Current source selector needs its explicit original owner path and version.')
        require(any(repository == original['repository'] for repository, _path in owners),
                'Current source decision belongs to another original repository.')
        matching = {path for repository, path in owners
                    if repository == original['repository'] and identity.parse(path).family == chosen.family}
        require(matching, 'Current source decision belongs to another original family.')
        require(len(matching) == 1,
                'Current source selector needs one explicit original owner version.')
        owner = identity.parse(next(iter(matching)))
        require(owner.version is not None and chosen.version is not None,
                'Current source selector needs fixed original owner and target versions.')
        require(chosen.version <= owner.version, 'Current source selection points to a later original revision.')
        raise FileNotFoundError('Selected source decision was not acquired: ' + pointer.path)
    target = document if pointer.path == document.path else parse(pointer.path, read(pointer.path))
    require(target.identity.family == document.identity.family, 'Current decision belongs to another family.')
    require(original_family(target) == original_family(document),
            'Current decision belongs to another original family.')
    require(target.identity.version <= document.identity.version, 'Current selection points to a later revision.')
    require(pointer.anchor in target.decisions, 'Current selection does not name a fixed decision: ' + pointer.anchor)
    require(links.anchor_occurrences(target.text)[pointer.anchor] == 1,
            'Current decision anchor must identify exactly one target: ' + pointer.anchor)
    return target, target.decisions[pointer.anchor]


def selected(document, read):
    """Resolve the one selected decision, never the newest review or status."""
    return selection(document, read)[1]


def check(document, read, *, paths=(), source_info=None):
    if document.identity.kind == 'T':
        from . import tasks
        tasks.validate(document, read, paths=paths)
    review_targets = []
    if document.identity.kind in 'RL':
        from . import review
        review_targets = [vars(target) for _finding, target, _scope in review.bindings(document)
                          if not source_refs.external(target.path)]
    if document.identity.kind == 'S':
        from . import navigation as material_navigation
        material_navigation.validate_routes([document], read, paths=paths)
    loaded = {document.path: document}

    def target(path):
        if path not in loaded:
            try:
                loaded[path] = parse(path, read(path))
            except (FileNotFoundError, KeyError) as error:
                raise ValueError('Required material target is absent: ' + path) from error
        return loaded[path]

    decisions = [(document, decision) for decision in document.decisions.values()]
    if document.current:
        try:
            owner, decision = selection(document, lambda path: target(path).text, source_info=source_info)
        except FileNotFoundError:
            if not source_refs.external(document.current.path):
                raise
        else:
            decisions.append((owner, decision))
    for owner, decision in decisions:
        primary = 'statement' if owner.identity.kind == 'C' else 'contract'
        for role, loc, _ in decision.relations:
            if source_refs.external(loc.path):
                require(bool(document.identity.source_repository), 'An unacquired source locator cannot supply a local fixed decision input.')
                continue
            if identity.parse(loc.path).kind == 'U':
                check_source_unit(target(loc.path))
            if role == primary:
                chosen = target(loc.path)
                require(chosen.identity.family == owner.identity.family,
                        'Decision selects another material family.')
                require(original_family(chosen) == original_family(owner),
                        'Selected ' + primary + ' belongs to another original family.')
                require(chosen.identity.version <= owner.identity.version,
                        'Decision cannot bind a later material revision.')
    locators = review_targets + [vars(loc) for _, decision in decisions for _, loc, _ in decision.relations if not source_refs.external(loc.path)]
    material_checks.validate_locator_targets(locators, lambda path: loaded[path].text if path in loaded else read(path))


def current(paths, family):
    candidates = [(identity.parse(p), p) for p in paths]
    candidates = [(i.version, p) for i, p in candidates if i.family == family]
    require(candidates and all(version is not None for version, _ in candidates), 'No fixed main-material sequence: ' + family)
    versions = [v for v, _ in candidates]
    require(len(versions) == len(set(versions)), 'More than one main material owns a revision.')
    return max(candidates)[1]
