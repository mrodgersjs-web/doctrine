"""Command line: list, show and validate doctrine files."""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from . import __version__
from .loader import Repo, load_repo
from .model import KINDS
from .validator import Problem, validate_record, validate_repo


def _emit_json(payload) -> None:
    print(json.dumps(payload, indent=2, default=str))


def _cmd_list(args) -> int:
    repo = load_repo(args.root)
    records = [r for r in repo.records if args.kind is None or r.kind == args.kind]
    if args.json:
        _emit_json({"counts": repo.counts(), "records": [r.as_dict() for r in records]})
        return 0
    for record in records:
        print(f"{record.id:40} {record.kind:10} {record.title}")
    return 0


def _cmd_show(args) -> int:
    repo = load_repo(args.root)
    record = repo.find(args.id)
    if record is None:
        print(f"error: no doctrine record named {args.id!r}", file=sys.stderr)
        return 2
    if args.json:
        _emit_json(record.as_dict())
        return 0
    print(f"id:       {record.id}")
    print(f"kind:     {record.kind}")
    print(f"title:    {record.title}")
    print(f"path:     {record.path}")
    print(f"sections: {', '.join(record.sections) or '(none)'}")
    if record.front_matter:
        for key, value in record.front_matter.items():
            print(f"{key}: {value}")
    print()
    print(record.body)
    return 0


def _problems_for(args) -> tuple[Repo, list[Problem]]:
    repo = load_repo(args.root)
    if not args.paths:
        return repo, validate_repo(repo)
    problems: list[Problem] = []
    for raw in args.paths:
        path = Path(raw)
        for record in repo.records:
            if record.path == path.resolve() or record.path.parent == path.resolve():
                problems.extend(validate_record(record))
    return repo, problems


def _cmd_validate(args) -> int:
    repo, problems = _problems_for(args)
    if args.json:
        _emit_json(
            {
                "ok": not problems,
                "counts": repo.counts(),
                "problems": [vars(p) for p in problems],
            }
        )
        return 0 if not problems else 1
    scope = " ".join(args.paths) if args.paths else f"{len(repo.records)} record(s)"
    print(f"checked {scope}")
    for problem in problems:
        print(f"ERROR {problem}")
    print("OK" if not problems else f"FAILED ({len(problems)} problem(s))")
    return 0 if not problems else 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="rig-doctrine", description=__doc__)
    parser.add_argument("--version", action="version", version=__version__)
    parser.add_argument("--root", default=".", help="repository root (default: current directory)")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list", help="list doctrine records")
    p.add_argument("--kind", choices=KINDS)
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=_cmd_list)

    p = sub.add_parser("show", help="show one record by id")
    p.add_argument("id")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=_cmd_show)

    p = sub.add_parser("validate", help="validate the repository (or specific files/directories)")
    p.add_argument("paths", nargs="*")
    p.add_argument("--json", action="store_true")
    p.set_defaults(fn=_cmd_validate)

    args = parser.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
