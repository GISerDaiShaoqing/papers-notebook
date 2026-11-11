from __future__ import annotations

import re
from pathlib import Path

from ..models import PaperRecord


FIELD_PATTERNS: dict[str, re.Pattern[str]] = {
    "title": re.compile(r"^\*\*Title\s*:\s*\*\*\s*(.*)$", re.IGNORECASE),
    "link": re.compile(r"^\*\*Link\s*:\s*\*\*\s*(.*)$", re.IGNORECASE),
    "doi": re.compile(r"^\*\*Doi\s*:\s*\*\*\s*(.*)$", re.IGNORECASE),
    "notes": re.compile(r"^\*\*Notes\s*[:：]\s*\*\*\s*(.*)$", re.IGNORECASE),
    "highlights": re.compile(r"^\*\*H(?:igh|ight)lights\s*[:：]\s*\*\*\s*(.*)$", re.IGNORECASE),
    "research_gap": re.compile(r"^\*\*Research\s+gap/question\s*:\s*\*\*\s*(.*)$", re.IGNORECASE),
    "discussion": re.compile(r"^\*\*Discussion/Conclusion\s*[:：]?\s*\**\s*(.*)$", re.IGNORECASE),
    "graph_table": re.compile(r"^\*\*Graph/Table\s+interested\s*[:：]\s*\*\*\s*(.*)$", re.IGNORECASE),
    "resources": re.compile(r"^\*\*Resources\s*:\s*\*\*\s*(.*)$", re.IGNORECASE),
}

CATEGORY_RE = re.compile(r"^#\s+(.+?)\s*$")
PAPER_RE = re.compile(r"^##\s+(?:\d+\s+)?(.+?)\s*$")


def _is_empty(value: str) -> bool:
    value = value.strip()
    if not value:
        return True
    if value in {"[原文链接]()", "[原文链接]", "()"}:
        return True
    return False


def _field_value(lines: list[str], start: int, end: int, pattern: re.Pattern[str]) -> str:
    for offset, line in enumerate(lines[start:end], start=start):
        match = pattern.match(line.strip())
        if match:
            chunks = [match.group(1).strip()] if match.group(1).strip() else []
            for following in lines[offset + 1 : end]:
                stripped = following.strip()
                if any(other.match(stripped) for other in FIELD_PATTERNS.values()):
                    break
                if stripped:
                    chunks.append(stripped)
            # Preserve multiline notes while trimming only outer whitespace.
            return "\n".join(chunks).strip()
    return ""


def scan_readme(path: Path) -> list[PaperRecord]:
    """Parse paper sections from the existing README without rewriting it."""
    lines = path.read_text(encoding="utf-8").splitlines()
    records: list[PaperRecord] = []
    category = "Uncategorized"
    current: tuple[int, str, int] | None = None

    def finish(end: int) -> None:
        nonlocal current
        if current is None:
            return
        start, title, line_number = current
        fields = {
            name: _field_value(lines, start, end, pattern)
            for name, pattern in FIELD_PATTERNS.items()
        }
        fields = {name: ("" if _is_empty(value) else value) for name, value in fields.items()}
        records.append(
            PaperRecord(
                category=category,
                title=title,
                fields=fields,
                heading_line=line_number,
                source_path=path,
                raw_text="\n".join(lines[start:end]).strip(),
            )
        )
        current = None

    for index, line in enumerate(lines):
        category_match = CATEGORY_RE.match(line)
        if category_match:
            finish(index)
            category = category_match.group(1).strip()
            continue
        paper_match = PAPER_RE.match(line)
        if paper_match:
            finish(index)
            current = (index + 1, paper_match.group(1).strip(), index + 1)

    finish(len(lines))
    return records


def missing_fields(record: PaperRecord) -> list[str]:
    """Return fields that need human work, treating template links as empty."""
    return [name for name, value in record.fields.items() if _is_empty(value)]

