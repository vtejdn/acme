"""Inventory the requested whole source store: bytes, formats and recorded limitations."""
import argparse
import json
from pathlib import Path
from . import literature as literature_storage


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path(__file__).resolve().parents[3])
    args = parser.parse_args()
    result = literature_storage.check(args.root)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return int(bool(result['errors']))


if __name__ == '__main__':
    raise SystemExit(main())
