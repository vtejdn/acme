"""Check staged changes, or final base-to-HEAD changes and outgoing header identities."""
import argparse
import json
from pathlib import Path
from ..core import repository as r
from . import submission as submission

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__, epilog=(
        'Optional check of the selected view and affected references. '
        'External registration edits check tables only; choose unchanged external-reference fields through the shared API. '
        'Structural success supplies no mathematical judgment; routine J/E/intake edits add no generic reminder.'))
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument('--working-tree', action='store_true')
    mode.add_argument('--commits', metavar='BASE')
    parser.add_argument('--github-account')
    parser.add_argument('--push', action='store_true', help='Outgoing identity check context only; never performs a network push.')
    parser.add_argument('--details', action='store_true', help='Print optional scope diagnostics.')
    args = parser.parse_args(argv)
    try:
        result = submission.check(args.root, working_tree=args.working_tree, commits=args.commits,
              github_account=args.github_account, push=args.push)
        print(json.dumps(result, indent=2) if args.details else submission.report(result))
    except (r.ResearchError, OSError, ValueError, KeyError, TypeError, SyntaxError) as error:
        print('Submission refused: ' + str(error))
        return 1
