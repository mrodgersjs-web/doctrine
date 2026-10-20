"""Data model: what one doctrine file is."""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path

DOCTRINE = "doctrine"
INTAKE = "intake"
AGENT_PACK = "agent-pack"

KINDS: tuple[str, ...] = (DOCTRINE, INTAKE, AGENT_PACK)

#: Directories scanned per kind.
KIND_DIRS: dict[str, str] = {
    DOCTRINE: "doctrines",
    INTAKE: "intake",
    AGENT_PACK: "agent-packs",
}

#: Front-matter keys every intake record must carry.
INTAKE_REQUIRED_KEYS: tuple[str, ...] = ("title", "source", "received", "status", "promoted_to")

#: Values allowed for intake front-matter `status`.
INTAKE_STATUSES: tuple[str, ...] = ("intake", "candidate", "promoted", "retired")


@dataclass
class DoctrineRecord:
    """One markdown file in the doctrine repository."""

    id: str
    kind: str
    title: str
    path: Path
    body: str = ""
    front_matter: dict = field(default_factory=dict)

    @property
    def sections(self) -> list[str]:
        """Level-2 headings in document order."""
        import re

        return [m.group(1).strip() for m in re.finditer(r"^##\s+(.+?)\s*$", self.body, re.MULTILINE)]

    def as_dict(self) -> dict:
        return {
            "id": self.id,
            "kind": self.kind,
            "title": self.title,
            "path": str(self.path),
            "sections": self.sections,
            "front_matter": self.front_matter,
        }
