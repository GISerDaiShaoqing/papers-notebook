from __future__ import annotations

import json
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from .markdown_service import read_text, write_text


@dataclass(frozen=True, slots=True)
class IndividualNote:
    path: Path
    title: str
    category: str
    status: str


def _frontmatter_value(text: str, key: str) -> str:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    if not match:
        return ""
    value = match.group(1).strip()
    try:
        decoded = json.loads(value)
    except json.JSONDecodeError:
        return value.strip('"\'')
    return str(decoded)


def scan_individual_notes(root: Path) -> list[IndividualNote]:
    notes: list[IndividualNote] = []
    for path in root.rglob("*.md"):
        if path.name in {"README.md", "INDEX.md"} or ".migration-backup-" in path.parts:
            continue
        text = read_text(path)
        title = _frontmatter_value(text, "title")
        category = _frontmatter_value(text, "category")
        status = _frontmatter_value(text, "status") or "untracked"
        if title:
            notes.append(IndividualNote(path=path, title=title, category=category, status=status))
    return sorted(notes, key=lambda item: (item.category.lower(), item.title.lower()))


def load_categories(root: Path) -> list[str]:
    """Load the curated category list, including categories with no notes yet."""
    path = root / "categories.json"
    if not path.is_file():
        return []
    try:
        values = json.loads(read_text(path))
    except (OSError, json.JSONDecodeError):
        return []
    if not isinstance(values, list):
        return []

    categories: list[str] = []
    seen: set[str] = set()
    for value in values:
        if not isinstance(value, str):
            continue
        category = value.strip()
        key = category.casefold()
        if category and key not in seen:
            categories.append(category)
            seen.add(key)
    return categories


def save_categories(root: Path, categories: list[str]) -> None:
    """Save unique categories while preserving their curated display order."""
    unique: list[str] = []
    seen: set[str] = set()
    for value in categories:
        category = value.strip()
        key = category.casefold()
        if category and key not in seen:
            unique.append(category)
            seen.add(key)
    write_text(root / "categories.json", json.dumps(unique, ensure_ascii=False, indent=2) + "\n")


def render_index(root: Path) -> str:
    entries = scan_individual_notes(root)
    grouped: dict[str, list[IndividualNote]] = defaultdict(list)
    for category in load_categories(root):
        grouped[category]
    for entry in entries:
        grouped[entry.category or "Uncategorized"].append(entry)

    lines = [
        "# Individual paper notes index",
        "",
        "This file is generated from the category list and Markdown files under `notes/`. Edit those sources instead.",
        "",
    ]
    for category in sorted(grouped, key=str.lower):
        lines.extend([f"## {category}", ""])
        for entry in grouped[category]:
            relative = entry.path.relative_to(root).as_posix()
            lines.append(f"- [{entry.title}]({relative}) — `{entry.status}`")
        if grouped[category]:
            lines.append("")
        else:
            lines.extend(["No notes yet.", ""])
    return "\n".join(lines).rstrip() + "\n"


def sync_index(notes_root: Path, output: Path, apply: bool = False) -> int:
    entries = scan_individual_notes(notes_root)
    if apply:
        write_text(output, render_index(notes_root))
    return len(entries)

