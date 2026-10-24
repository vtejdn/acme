"""Bounded material-owned decisions, independent of C/T JSON storage."""
from dataclasses import dataclass, field, replace
from datetime import date
from pathlib import PurePosixPath
import re
from . import identity as identity
from ..core import links as links
from ..core import repository as shared
from ..core import source_refs
from . import validation as material_checks

require = identity.require
HEADER_FIELDS = {'author', 'framework', 'source_repository', 'source_material'}
CLAIM_ONLY_FIELDS = {'review-status', 'role'}
FIELDS = {'date', 'status', 'reason', 'authority'} | CLAIM_ONLY_FIELDS
RELATIONS = {'statement', 'contract', 'argument', 'support', 'dependency', 'review'}
CLAIM_STATES = {'open', 'proved', 'refuted'}
PAST_CLAIM_STATES = {'proof draft', 'conditional'}
TASK_STATES = {'proposed', 'active', 'paused', 'blocked', 'completed', 'retired'}
REVIEW_STATES = {'unreviewed', 'under review', 'self-reviewed', 'independently reviewed', 'changes required'}
ARCHIVAL_NOTICE = 'No current assessment is selected for this physical material version.'


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
    historical_assessments: dict = field(default_factory=dict)
    archival: bool = False
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

    Slice both views together so a literal opened outside a section cannot
    become authoritative when that section or row is read in isolation.
    """
    def __init__(self, raw, *, structure=None):
        self.text, self.structure = (links.markdown_views(raw)
                                     if structure is None else (raw, structure))

    def slice(self, start, end):
        return MarkdownInput(self.text[start:end], structure=self.structure[start:end])

    def sections(self, heading):
        pattern = r'^ {0,3}## ' + re.escape(heading) + r'[ \t]*\n(.*?)(?=^ {0,3}#{1,2}(?:[ \t]|$)|\Z)'
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


def locator(path, value):
    match = re.fullmatch(r'\[[^\]\n]+\]\(([^)\n]+)\)', value.strip())
    require(match is not None, 'Expected one explicit Markdown material link: ' + value)
    original = source_refs.parse(match[1])
    if original is not None:
        return Locator(match[1].partition('#')[0], original['anchor'])
    result = links.destination(path, match[1])
    require(result is not None, 'Decision locators must name available repository material.')
    target, anchor = result
    from ..core import paths
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


def assessment_records(path, ident, history, *, historical=False, legacy=False, original_material=None):
    """Read retained facts without making an archival assessment adoptable."""
    heading = 'Historical assessment' if historical else 'Decision'
    prefix = 'historical-assessment-' if historical else 'decision-'
    sections = list(re.finditer(r'^ {0,3}### ' + heading + r' ([A-Za-z0-9-]+)[ \t]*$', history.structure, re.M))
    decisions = {}
    for index, section in enumerate(sections):
        anchor = prefix + section[1].lower()
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
        require(fields['status'] in (CLAIM_STATES | PAST_CLAIM_STATES if ident.kind == 'C' else TASK_STATES), 'Undefined mathematical disposition.')
        require(ident.kind == 'C' or not CLAIM_ONLY_FIELDS & fields.keys(),
                'Task decisions cannot contain Claim-only fields: review-status or role.')
        require('review-status' not in fields or fields['review-status'] in REVIEW_STATES, 'Undefined review classification.')
        require(ident.kind != 'C' or 'role' not in fields or fields['role'] in {'lemma', 'theorem', 'corollary'},
                'Undefined Claim role.')
        primary = 'statement' if ident.kind == 'C' else 'contract'
        targets = [loc for role, loc, _ in relations if role == primary]
        require(len(targets) == 1, 'Decision needs exactly one selected ' + primary + '.')
        original_primary = source_refs.parse(targets[0].path)
        selected = identity.parse(original_primary['path'] if original_primary else targets[0].path)
        expected = identity.parse(original_material) if original_primary and original_material else ident
        require(selected.family == expected.family, 'Decision selects another material family.')
        if original_primary:
            require(original_primary['repository'] == ident.source_repository,
                    'Decision selects another original repository.')
        require(selected.version <= ident.version, 'Decision cannot bind a later material revision.')
        roles = {role for role, _, _ in relations}
        if ident.kind == 'T':
            require(fields.get('authority') and fields.get('reason'), 'Task decisions need reason and actual authority.')
            require(fields['status'] != 'completed' or 'review' in roles, 'Completion needs an adopted review.')
        if not historical:
            if ident.kind == 'C' and fields['status'] in {'proved', 'refuted'}:
                require({'argument', 'review'} <= roles, 'Accepted Claim needs selected argument and review.')
            if ident.kind == 'C' and fields['status'] != 'open':
                require('argument' in roles, 'Argument-bearing Claim needs an explicit argument.')
        for role, loc, _ in relations:
            original = source_refs.parse(loc.path)
            target_identity = identity.parse(original['path'] if original else loc.path)
            if role == 'argument' and ident.kind == 'C' and not legacy:
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


def new_decision(document, decision):
    """Validate supplied current/new declarations, leaving past/source facts readable."""
    if document.identity.kind == 'C':
        require(decision.fields['status'] in CLAIM_STATES, 'New/current local Claims use open, proved or refuted.')
        require('review-status' not in decision.fields, 'New/current local Claim decisions cannot contain retired review-status.')
    for role, loc, _scope in decision.relations:
        if role == 'review':
            require(identity.parse(loc.path).kind == 'R', 'New/current local formal reviews require fixed R findings.')


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
            original = identity.parse(header['source_material'])
            require((ident.kind == 'U') == (original.kind == 'U'),
                    'A source unit retains its dedicated original-unit contract.')
            require(ident.kind != 'U' or original.author == ident.author,
                    'An acquired source unit retains its original author.')
    else:
        require(not source_fields & header.keys(), 'Local material cannot acquire an imported source binding.')
    return ident, header, content


def parse(path, text, *, legacy=False):
    ident, header, content = author_header(path, text)
    body = MarkdownInput(content)
    headings = [body.text[item.start(1):item.end(1)] for item in re.finditer(r'^# ([^\n]+)$', body.structure, re.M)]
    require(len(headings) == 1, 'Material needs one main title.')
    current, decisions, historical_assessments, archival = None, {}, {}, False
    if ident.kind in 'CT':
        name = 'Current assessment' if ident.kind == 'C' else 'Current decision'
        sections = body.sections(name)
        archives = body.sections('Historical material')
        require(len(archives) <= 1, 'Repeated historical material notice.')
        if archives:
            require(ident.kind == 'C' and archives[0][0].structure.strip() == ARCHIVAL_NOTICE,
                    'Historical material needs the explicit Claim archival notice.')
            require(not sections, 'Archival material cannot select a current assessment.')
            archival = True
        else:
            require(len(sections) == 1, 'Material needs exactly one ' + name + ' section.')
            current = locator(path, sections[0][0].structure.strip())
        # Decision anchors and tables are parsed only in the designated history.
        history_name = 'Assessment history' if ident.kind == 'C' else 'Lifecycle and completion'
        histories = body.sections(history_name)
        require(len(histories) <= 1, 'Repeated decision history.')
        history = histories[0][0] if histories else MarkdownInput('')
        decisions = assessment_records(path, ident, history, legacy=legacy, original_material=header.get('source_material'))
        require(not archival or not decisions, 'Archival material cannot own adoptable decisions.')
        histories = body.sections('Historical assessments')
        require(len(histories) <= 1, 'Repeated historical assessments.')
        require(not histories or ident.kind == 'C', 'Historical assessments belong only to Claims.')
        if histories:
            historical_assessments = assessment_records(path, ident, histories[0][0], historical=True, legacy=legacy, original_material=header.get('source_material'))
            require(historical_assessments, 'Historical assessments need explicit retained records.')
    document = Document(path, ident, header, headings[0], text, current, decisions, historical_assessments, archival)
    if ident.kind == 'T':
        from . import tasks
        document.task_type, document.joint_task = tasks.declarations(path, body)
        require(not ident.source_repository or document.task_type == 'joint',
                'An external T is a necessary joint contract, never another human\'s ordinary Task.')
    if ident.kind == 'U':
        source_unit_scope(document)
    return document


def source_unit_scope(document):
    """Read stated edition, passage and inspection limits; infer no verdict."""
    require(document.identity.kind == 'U', 'Expected a fixed source-unit document.')
    require(links.anchor_occurrences(document.text)[document.identity.anchor] == 1,
            'Source unit needs its actual source-key/unit anchor.')
    sections = MarkdownInput(document.text.replace('\r\n', '\n')).sections('Source and inspection')
    require(len(sections) == 1, 'Source unit needs one Source and inspection section.')
    rows = sections[0][0].table(('Field', 'Value'), minimum_dashes=3)
    require(len(rows) == 3, 'Source inspection uses one Field/Value table with three facts.')
    scope = {}
    for cells, _number in rows:
        require(len(cells) == 2 and cells[0] in {'source-version', 'source-locator', 'inspection'} and
                cells[0] not in scope and cells[1], 'Missing, repeated or unknown source inspection fact.')
        scope[cells[0]] = cells[1]
    return scope


def original_family(document):
    """Original family under its receiving repository, independent of local serial."""
    if document.identity.source_repository:
        return (document.header['source_repository'],
                identity.parse(document.header['source_material']).family if 'source_material' in document.header
                else document.identity.family)
    return None, document.identity.family


def revision_inputs(document, read):
    """Read explicitly designated earlier receiving inputs, never guess ancestry."""
    chosen = []
    if document.identity.kind in 'CT' and document.current:
        chosen = [(loc, scope) for role, loc, scope in selected(document, read).relations
                  if role in {'support', 'dependency'}]
    else:
        sections = MarkdownInput(document.text).sections('Inputs')
        require(len(sections) <= 1, 'A material has at most one explicit Inputs section.')
        if sections:
            for _first, _last, label, _start, _end, href in links.markdown_link_details(sections[0][0].text):
                destination = links.destination(document.path, href)
                if destination is not None:
                    chosen.append((Locator(*destination), label))
    result = []
    for loc, scope in chosen:
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
        require(scope.strip(), 'State the actual input scope at its responsible reference.')
        item = {'path': loc.path, 'anchor': loc.anchor, 'scope': scope}
        if item not in result:
            result.append(item)
    return result


def selection(document, read):
    """Resolve the selected decision together with the material that owns it."""
    require(not document.archival, 'Archival material has no adoptable current assessment.')
    require(document.current is not None, 'Only C/T material has a current decision.')
    pointer = document.current
    if source_refs.external(pointer.path):
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


def check(document, read, *, paths=(), unavailable_output=None):
    if document.identity.kind == 'T':
        from . import tasks
        tasks.validate(document, read, paths=paths)
    review_targets = []
    if document.identity.kind in 'RL':
        from . import review
        review_targets = [vars(target) for _finding, target, _scope in review.bindings(
            document, legacy=bool(document.identity.source_repository))
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

    decisions = [(document, decision) for decision in
                 (*document.decisions.values(), *document.historical_assessments.values())]
    if document.current:
        if not source_refs.external(document.current.path):
            owner, decision = selection(document, lambda path: target(path).text)
            decisions.append((owner, decision))
    for owner, decision in decisions:
        primary = 'statement' if owner.identity.kind == 'C' else 'contract'
        for role, loc, _ in decision.relations:
            if source_refs.external(loc.path):
                require(bool(document.identity.source_repository), 'An unacquired source locator cannot supply a local fixed decision input.')
                continue
            if identity.parse(loc.path).kind == 'U':
                source_unit_scope(target(loc.path))
            if role == primary:
                chosen = target(loc.path)
                require(chosen.identity.family == owner.identity.family,
                        'Decision selects another material family.')
                require(original_family(chosen) == original_family(owner),
                        'Selected ' + primary + ' belongs to another original family.')
                require(chosen.identity.version <= owner.identity.version,
                        'Decision cannot bind a later material revision.')
    locators = review_targets + [vars(loc) for _, decision in decisions for _, loc, _ in decision.relations if not source_refs.external(loc.path)]
    if unavailable_output is not None:
        missing = {item['path'] for item in locators if unavailable_output(item['path'])}
        if missing:
            document.notices = list(dict.fromkeys(getattr(document, 'notices', []) +
                ['Local computation output unavailable in selected view: ' + path for path in sorted(missing)]))
        locators = [item for item in locators if item['path'] not in missing]
    material_checks.validate_locator_targets(locators, lambda path: loaded[path].text if path in loaded else read(path))


def current(paths, family):
    candidates = [(identity.parse(p), p) for p in paths]
    candidates = [(i.version, p) for i, p in candidates if i.family == family]
    require(candidates and all(version is not None for version, _ in candidates), 'No fixed main-material sequence: ' + family)
    versions = [v for v, _ in candidates]
    require(len(versions) == len(set(versions)), 'More than one main material owns a revision.')
    return max(candidates)[1]
