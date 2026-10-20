"""Render derived Claim, Task and route navigation from material authority."""
from pathlib import Path
import argparse
from ..core import repository as r
from . import render as navigation
ROOT = Path(__file__).resolve().parents[3]

def render(root=ROOT):
    repo = r.Repository(root)
    changed = navigation.render(repo)
    print(f'Rendered navigation; updated {changed['changed']} generated files.')

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=ROOT)
    parser.add_argument('--maintenance-wait', type=float, default=30)
    args = parser.parse_args(argv)
    repo = r.Repository(args.root)
    print(navigation.render(repo, timeout=args.maintenance_wait))
    return 0
