"""Check one selected current Task-family execution boundary without history replay."""
import argparse
import json
import math
from pathlib import Path
import re
from ..core import repository as r
from ..core import identity as humans
from ..materials import identity as names
from ..materials import documents

STATES = {'not-running', 'running', 'stopped', 'ended'}
FIELDS = {'task', 'state', 'threshold_percent', 'baseline_percent', 'limit_percent', 'window', 'account', 'bucket'}


def address(task):
    item = names.parse(task)
    r.require(item.kind == 'T' and item.source_repository is None, 'Execution belongs to a local Task family.')
    return 'execution/' + item.family.replace('_T_', '_E_') + '.md'


def family(path):
    match = re.fullmatch(r'execution/([A-Za-z0-9-]+)_E_([A-Z][0-9]{4,})\.md', path)
    r.require(match is not None, 'Use the stable author/Task-family E address.')
    names.serial(match[2])
    return match[1] + '_T_' + match[2]


def parse(path, text):
    family(path)
    body = documents.MarkdownInput(text)
    tables = list(body.tables())
    r.require(len(tables) == 1 and tuple(tables[0][0]) == ('Field', 'Value'),
              'Current E needs one Field/Value table, not an event history.')
    rows = [cells for cells, _ in tables[0][1]]
    r.require(all(len(row) == 2 and all(row) for row in rows), 'Current E has an empty or malformed field.')
    record = dict(rows)
    r.require(len(record) == len(rows) and {'task', 'state'} <= record.keys() <= FIELDS,
              'Current E needs task/state and only applicable current-limit fields.')
    for field in ('threshold_percent', 'baseline_percent', 'limit_percent'):
        if field in record:
            record[field] = float(record[field])
            r.require(math.isfinite(record[field]) and 0 <= record[field] <= 100, 'Invalid current percentage: ' + field)
    r.require(('baseline_percent' in record) == ('limit_percent' in record), 'An incremental limit needs both baseline and upper bound.')
    if 'baseline_percent' in record:
        r.require(record['baseline_percent'] <= record['limit_percent'] and record.get('window'),
                  'Keep the actual incremental baseline, upper bound and applicable window.')
    return record


def validate(repo, record, path):
    expected = family(path)
    task, separator, anchor = record['task'].partition('#')
    ident = names.parse(task)
    r.require(separator and ident.kind == 'T' and ident.source_repository is None and ident.family == expected,
              'Current E must name an exact decision in its own local Task family.')
    humans.person(repo, ident.author)
    doc = documents.parse(task, r.read_from(repo, task).decode('utf-8-sig'))
    r.require(doc.task_type == 'ordinary', 'A joint Task cannot own an E or execute directly.')
    r.require(anchor in doc.decisions, 'Current E Task decision is absent: ' + record['task'])
    r.require(record['state'] in STATES, 'Invalid current execution state.')
    return {'path': path, **record}


def check(repo, task):
    doc = documents.parse(task, r.read_from(repo, task).decode('utf-8-sig'))
    r.require(doc.task_type == 'ordinary', 'Select the actual human\'s individual Task/E to continue a joint goal.')
    path = address(task)
    return validate(repo, parse(path, r.read_from(repo, path).decode('utf-8-sig')), path)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    commands = parser.add_subparsers(dest='command', required=True)
    command = commands.add_parser('check')
    command.add_argument('--task', required=True)
    command.add_argument('--view', default='WORKTREE', help='Actual WORKTREE, INDEX or fixed commit postimage')
    args = parser.parse_args(argv)
    try:
        if args.view == 'WORKTREE':
            result = check(r.Repository(args.root), args.task)
        else:
            from ..core.git_views import Tree
            with Tree(args.root, args.view) as tree:
                result = check(tree.research_view(), args.task)
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.exit(2, 'execution: ' + str(error) + '\n')
