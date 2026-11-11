from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path


class ReadingStatus(str, Enum):
    UNREAD = "unread"
    READING = "reading"
    PARTIAL = "partial"
    REVIEWED = "reviewed"
    NEEDS_SOURCE = "needs-source"


@dataclass(slots=True)
class PaperRecord:
    """A paper entry parsed from the legacy README format."""

    category: str
    title: str
    fields: dict[str, str] = field(default_factory=dict)
    heading_line: int | None = None
    source_path: Path | None = None
    raw_text: str = ""

    @property
    def missing_fields(self) -> list[str]:
        return [name for name, value in self.fields.items() if not value.strip()]

    @property
    def status(self) -> ReadingStatus:
        explicit = self.fields.get("status", "").strip().lower()
        if explicit in {item.value for item in ReadingStatus}:
            return ReadingStatus(explicit)
        if any(value.strip() for value in self.fields.values()):
            return ReadingStatus.PARTIAL
        return ReadingStatus.UNREAD

