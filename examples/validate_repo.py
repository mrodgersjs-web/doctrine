#!/usr/bin/env python3
"""Runnable example: validate this doctrine repository and print a summary.

Usage: python examples/validate_repo.py
Exit code 0 when every record passes, 1 otherwise.
"""

import sys
from pathlib import Path

from rig_doctrine.loader import load_repo
from rig_doctrine.validator import validate_repo

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    repo = load_repo(ROOT)
    problems = validate_repo(repo)
    counts = repo.counts()
    print(
        f"loaded {len(repo.records)} records: "
        f"{counts['doctrine']} doctrine, {counts['intake']} intake, {counts['agent-pack']} agent-pack"
    )
    for problem in problems:
        print(f"ERROR {problem}")
    print("doctrine corpus OK" if not problems else "doctrine corpus FAILED")
    return 0 if not problems else 1


if __name__ == "__main__":
    sys.exit(main())
