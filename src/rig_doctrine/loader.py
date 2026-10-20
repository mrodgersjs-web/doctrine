"""Discover and parse doctrine files from the repository layout."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path

from .model import KIND_DIRS, DoctrineRecord

_H1_RE = re.compile(r"^#\s+(.+?)\s*$", re.MULTILINE)
_MD_LINK_RE = re.compile(r"\]\(([^)\s]+)")


@dataclass
class Repo:
    """Everything loaded from a doctrine repository root."""

    root: Path
    records: list[DoctrineRecord] = field(default_factory=list)

    @property
    def by_id(self) -> dict[str, DoctrineRecord]:
        return {r.id: r for r in self.records}

    def find(self, record_id: str) -> DoctrineRecord | None:
        """Look up a record by id (lowercased file stem) or file name."""
        needle = record_id.lower().removesuffix(".md")
        return self.by_id.get(needle)

    def counts(self) -> dict[str, int]:
        out = {kind: 0 for kind in KIND_DIRS}
        for record in self.records:
            out[record.kind] += 1
        return out


def parse_front_matter(text: str) -> tuple[dict, str]:
    """Split YAML-subset front matter from the body. ({} , text) when absent."""
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    data: dict = {}
    for raw in text[4:end].splitlines():
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        key, sep, value = raw.partition(":")
        if not sep:
            continue
        value = value.strip()
        if len(value) >= 2 and value[0] == value[-1] and value[0] in "'\"":
            value = value[1:-1]
        data[key.strip()] = None if value == "null" else value
    return data, text[end + 5 :]


def first_h1(body: str) -> str | None:
    match = _H1_RE.search(body)
    return match.group(1).strip() if match else None


def load_record(path: Path, kind: str) -> DoctrineRecord:
    """Parse one markdown file into a DoctrineRecord (structure only)."""
    text = path.read_text(encoding="utf-8")
    front_matter, body = parse_front_matter(text)
    title = front_matter.get("title") or first_h1(body) or path.stem
    return DoctrineRecord(
        id=path.stem.lower(),
        kind=kind,
        title=str(title),
        path=path,
        body=body,
        front_matter=front_matter,
    )


def load_repo(root: str | Path) -> Repo:
    """Load every doctrine, intake and agent-pack file under ``root``."""
    root = Path(root)
    repo = Repo(root=root)
    for kind, dirname in KIND_DIRS.items():
        directory = root / dirname
        if not directory.is_dir():
            continue
        for path in sorted(directory.glob("*.md")):
            repo.records.append(load_record(path, kind))
    return repo


def relative_links(body: str) -> list[str]:
    """Local markdown link targets in a body (fragment-free)."""
    out = []
    for target in _MD_LINK_RE.findall(body):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        out.append(target.split("#", 1)[0])
    return [t for t in out if t]
