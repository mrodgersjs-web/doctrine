"""Schema and integrity checks for doctrine records and the repository."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

from .loader import Repo, first_h1, relative_links
from .model import (
    AGENT_PACK,
    DOCTRINE,
    INTAKE,
    INTAKE_REQUIRED_KEYS,
    INTAKE_STATUSES,
    DoctrineRecord,
)


@dataclass(frozen=True)
class Problem:
    """One validation finding."""

    path: str
    rule: str
    message: str

    def __str__(self) -> str:
        return f"{self.path}: {self.rule}: {self.message}"


def validate_record(record: DoctrineRecord) -> list[Problem]:
    """Schema checks for one record. Returns [] when clean."""
    problems: list[Problem] = []
    where = str(record.path)

    def bad(rule: str, message: str) -> None:
        problems.append(Problem(where, rule, message))

    if len(record.body.strip()) < 40:
        bad("body", "body is empty or too short to be a doctrine")

    if record.kind == DOCTRINE:
        h1s = [line for line in record.body.splitlines() if line.startswith("# ")]
        if len(h1s) != 1:
            bad("h1", f"expected exactly one level-1 heading, found {len(h1s)}")
        elif first_h1(record.body) is None:  # pragma: no cover - implied by the count
            bad("h1", "level-1 heading is malformed")
        if not record.sections:
            bad("sections", "needs at least one level-2 section")

    if record.kind == INTAKE:
        missing = [k for k in INTAKE_REQUIRED_KEYS if k not in record.front_matter]
        for key in missing:
            bad("front-matter", f"missing required key '{key}'")
        status = record.front_matter.get("status")
        if status is not None and status not in INTAKE_STATUSES:
            bad("front-matter", f"status {status!r} must be one of {', '.join(INTAKE_STATUSES)}")

    if record.kind == AGENT_PACK:
        if first_h1(record.body) is None:
            bad("h1", "needs a level-1 heading")
        if not record.sections:
            bad("sections", "needs at least one level-2 section")

    for target in relative_links(record.body):
        resolved = (record.path.parent / target).resolve()
        if not resolved.is_file():
            bad("link", f"relative link target does not exist: {target}")

    return problems


def validate_repo(repo: Repo) -> list[Problem]:
    """Record checks plus repository-level checks (duplicate ids)."""
    problems: list[Problem] = []
    seen: dict[str, Path] = {}
    for record in repo.records:
        if record.id in seen:
            problems.append(
                Problem(str(record.path), "id", f"duplicate id '{record.id}' (also {seen[record.id]})")
            )
        seen[record.id] = record.path
        problems.extend(validate_record(record))
    return problems
