"""Read, author, navigate and acquire explicit mathematical materials."""
import argparse
import json
from pathlib import Path
import sys
from . import documents, identity, runtime, discovery, write as writer
from ..core import repository as shared


def fixed_locator(value):
    path, separator, anchor = value.partition('#')
    if not separator or not anchor:
        raise argparse.ArgumentTypeError('Use PATH#decision-anchor.')
    if identity.parse(path).kind not in 'CT':
        raise argparse.ArgumentTypeError('A decision belongs to C/T material.')
    return {'path': path, 'anchor': anchor}


def result(doc, read, *, source_info=None):
    try:
        selected = documents.selected(doc, read) if doc.current else None
    except FileNotFoundError:
        if not doc.identity.source_repository: raise
        selected = None
    row = {'path': doc.path, 'identity': doc.identity.name, 'title': doc.title, 'author': doc.header['author'],
           'selected_decision': vars(doc.current) if doc.current else None,
           'source_status' if doc.identity.source_repository else 'status': selected.fields['status'] if selected else None}
    if doc.identity.source_repository:
        row['source'] = doc.header
        row['acquisition'] = source_info(doc) if source_info else None
    if doc.identity.kind == 'U': row['source_inspection'] = documents.source_unit_scope(doc)
    for field in ('notices', 'execution', 'source_holding'):
        if hasattr(doc, field): row[field] = getattr(doc, field)
    return row


def argument_parser():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    root = argparse.ArgumentParser(add_help=False)
    root.add_argument('--root', type=Path, default=argparse.SUPPRESS)
    commands = parser.add_subparsers(dest='command', required=True)
    for name in ('show', 'check', 'routes', 'indexes'):
        command = commands.add_parser(name, parents=[root]); command.add_argument('paths', nargs='+')
    command = commands.add_parser('discover', parents=[root]); command.add_argument('--kind', choices=list('CTSRDJLU'))
    command = commands.add_parser('intake', parents=[root], help='Receive prepared mathematical units at a fixed source revision')
    command.add_argument('--source', type=Path, required=True); command.add_argument('--revision', required=True)
    command.add_argument('--source-repository', required=True, help='Registered receiving repoN for the immediate sender')
    command.add_argument('--correspondence', type=Path, required=True, help='Prepared repository and qualified author mappings')
    command.add_argument('--selections', type=Path, required=True, help='JSON list of path, anchor and scope; - reads stdin')
    command.add_argument('--include', action='append', default=[], help='Explicit indispensable file of a selected J group')
    command.add_argument('--mapping', type=Path, help='JSON source/local locator rows; correspondence is supplied by the agent')
    command.add_argument('--instruction', required=True); command.add_argument('--initiator')
    command.add_argument('--maintenance-wait', type=float, default=30)
    command.add_argument('--refresh-j', action='store_true', help='Permit selected file replacement for the same original J; the agent maintains current consumers and needed inputs')
    command = commands.add_parser('import', parents=[root], help='Install explicitly selected own content and directed necessary dependencies')
    command.add_argument('--source', type=Path, required=True)
    command.add_argument('--plan', type=Path, required=True, help='Prepared roots and entries; - reads stdin')
    command.add_argument('--author')
    command.add_argument('--maintenance-wait', type=float, default=30)
    command = commands.add_parser('fetch-source', parents=[root], help='Fetch supplied addresses for inspection without registering an association')
    command.add_argument('--url', action='append', required=True)
    command.add_argument('--output', type=Path, required=True)
    command.add_argument('--format', choices=['pdf', 'html'], required=True)
    command = commands.add_parser('register-source', parents=[root], help='Apply chosen bibliographic fields and retain explicitly associated local bytes')
    command.add_argument('--file', type=Path, required=True, help='One new entry or exact chosen field updates; - reads stdin')
    choice = command.add_mutually_exclusive_group(required=True)
    choice.add_argument('--new-work', action='store_true')
    choice.add_argument('--existing-key')
    command.add_argument('--chosen-key', help='Unoccupied key for the explicitly new work; otherwise allocate its alpha key')
    command.add_argument('--local-pdf', type=Path, help='Explicit PDF input; a missing file records unavailability at a free destination')
    command.add_argument('--local-html', type=Path, help='Explicit original HTML input; a missing file records unavailability at a free destination')
    command.add_argument('--html-name', default='source.html')
    command.add_argument('--artifact-suffix', default='')
    command.add_argument('--selected-url', action='append', default=None)
    command.add_argument('--obtained-url', action='append', default=None)
    command.add_argument('--source-version', action='append', default=None)
    command.add_argument('--limitation', action='append', default=None)
    command.add_argument('--registry-update', type=Path, help='Prepared registry JSON: expected-text edits or expected original text and final text')
    command.add_argument('--maintenance-wait', type=float, default=30)
    command = commands.add_parser('create', parents=[root])
    command.add_argument('--kind', required=True, choices=list('CTSRDJL'))
    context = command.add_mutually_exclusive_group()
    context.add_argument('--line'); context.add_argument('--task')
    command.add_argument('--author'); command.add_argument('--file', type=Path, required=True, help='Authored Markdown, or - for stdin')
    command.add_argument('--new-decision', action='append', default=[], help='Explicit actual new decision anchor to check; file addition implies no new decision')
    for name in ('revise', 'append-decision', 'select'):
        help_text = 'Append a decision; unchanged Claim role organization retains its selected assessment' if name == 'append-decision' else None
        command = commands.add_parser(name, parents=[root], help=help_text); command.add_argument('path')
        command.add_argument('--expect', type=fixed_locator, required=name != 'revise')
        if name == 'select': command.add_argument('--decision', type=fixed_locator, required=True)
        else: command.add_argument('--file', type=Path, required=True)
        if name == 'revise': command.add_argument('--new-decision', action='append', default=[])
        if name == 'append-decision': command.add_argument('--candidate', action='store_true')
    return parser


def main(argv=None):
    parser = argument_parser(); args = parser.parse_args(argv)
    def supplied(path): return sys.stdin.read() if str(path) == '-' else path.read_text(encoding='utf-8-sig')
    try:
        repo = shared.Repository(args.root); reader = runtime.Reader(repo)
        if args.command in {'show', 'check'}:
            read_material = reader.show if args.command == 'show' else reader.check
            docs = [read_material(path) for path in args.paths]
            output = [result(doc, reader.read, source_info=reader.source_info) for doc in docs] if args.command == 'show' else {'checked': len(docs)}
            if args.command == 'check':
                notices = sorted({notice for doc in docs for notice in getattr(doc, 'notices', [])})
                if notices: output['notices'] = notices
        elif args.command == 'discover':
            output = discovery.families(discovery.inventory(repo.root, args.kind), reader.read, source_info=reader.source_info)
        elif args.command == 'routes':
            from . import navigation
            output = navigation.views([reader.check(path) for path in args.paths], reader.read, source_info=reader.source_info,
                                      paths=discovery.candidates(repo.root))
        elif args.command == 'indexes':
            from . import indexes
            output = indexes.views(args.paths, reader.read, source_info=reader.source_info)
        elif args.command == 'intake':
            from ..intake import acquire
            output = acquire.acquire(repo, args.source, json.loads(supplied(args.selections)), revision=args.revision,
                                     source_repository=args.source_repository, correspondence=json.loads(supplied(args.correspondence)),
                                     instruction=args.instruction, initiator=args.initiator, files=args.include, timeout=args.maintenance_wait, refresh_j=args.refresh_j,
                                     mapping=json.loads(supplied(args.mapping)) if args.mapping else ())
        elif args.command == 'import':
            from . import importing
            output = importing.import_content(repo, args.source, json.loads(supplied(args.plan)),
                                              author=args.author, timeout=args.maintenance_wait)
        elif args.command == 'fetch-source':
            from ..intake import literature
            output = literature.fetch_source(args.url, args.output, root=repo.root, source_format=args.format)
        elif args.command == 'register-source':
            from ..intake import bibliography, literature
            entries = bibliography.parse(supplied(args.file))
            shared.require(len(entries) == 1, 'Register one identified work per operation.')
            options = {'existing_key': args.existing_key, 'new_work': args.new_work, 'chosen_key': args.chosen_key, 'timeout': args.maintenance_wait}
            entry = next(iter(entries.values()))
            if args.local_pdf is None and args.local_html is None:
                shared.require(not any((args.artifact_suffix, args.selected_url, args.obtained_url, args.source_version, args.limitation, args.registry_update)),
                               'Artifact facts require the explicitly associated local artifact.')
                output = {'key': literature.register_work(repo, entry, **options)}
            else:
                facts = {name: value for name, value in (('urls', args.selected_url), ('obtained_urls', args.obtained_url),
                         ('versions', args.source_version), ('limitations', args.limitation)) if value is not None}
                output = literature.register(repo, entry, local_pdf=args.local_pdf, local_html=args.local_html,
                    html_name=args.html_name, suffix=args.artifact_suffix,
                    source_facts=facts or None,
                    registry_update=json.loads(supplied(args.registry_update)) if args.registry_update else None, **options)
        else:
            if args.command == 'create':
                doc = writer.create(repo, kind=args.kind, body=supplied(args.file), line=args.line, task=args.task,
                                    author=args.author, new_decisions=args.new_decision)
            elif args.command == 'revise':
                doc = writer.revise(repo, args.path, body=supplied(args.file), expected_current=args.expect,
                                    new_decisions=args.new_decision)
            elif args.command == 'append-decision':
                doc = writer.append_decision(repo, args.path, decision=supplied(args.file), expected_current=args.expect, select=not args.candidate)
            else:
                doc = writer.select_decision(repo, args.path, target=args.decision, expected_current=args.expect)
            output = result(doc, lambda path: shared.read_from(repo, path).decode('utf-8-sig'))
        print(json.dumps(output, ensure_ascii=False, indent=2)); return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(2, 'material: ' + str(error) + '\n')
