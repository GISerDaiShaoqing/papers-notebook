from __future__ import annotations

import hashlib
import json
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path

from ..models import PaperRecord
from .markdown_service import write_text
from .note_scanner import scan_readme


@dataclass(frozen=True, slots=True)
class MigrationResult:
    created: int
    skipped: int
    files: tuple[Path, ...]


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKC", value).strip().lower()
    slug = re.sub(r"[^\w\s-]", "", normalized, flags=re.UNICODE)
    slug = re.sub(r"[-\s]+", "-", slug).strip("-_")
    if slug:
        if len(slug) > 80:
            digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:8]
            slug = f"{slug[:71].rstrip('-')}-{digest}"
        return slug
    digest = hashlib.sha1(value.encode("utf-8")).hexdigest()[:10]
    return f"paper-{digest}"


def render_note(record: PaperRecord) -> str:
    fields = record.fields
    title = json.dumps(record.title, ensure_ascii=False)
    category = json.dumps(record.category, ensure_ascii=False)
    link = fields.get("link", "")
    doi = fields.get("doi", "")

    def section(name: str, key: str) -> str:
        return f"## {name}\n\n{fields.get(key, '').strip()}\n"

    return (
        "---\n"
        f"title: {title}\n"
        f"category: {category}\n"
        f"status: {record.status.value}\n"
        "source: ../../README.md\n"
        "---\n\n"
        f"# {record.title}\n\n"
        "## Bibliographic information\n\n"
        f"- Link: {link}\n"
        f"- DOI: {doi}\n\n"
        f"{section('Notes', 'notes')}\n"
        f"{section('Highlights', 'highlights')}\n"
        f"{section('Research gap/question', 'research_gap')}\n"
        f"{section('Discussion/Conclusion', 'discussion')}\n"
        f"{section('Graph/Table interested', 'graph_table')}\n"
        f"{section('Resources', 'resources')}\n"
        "## Reading checklist\n\n"
        "- [ ] Research question and motivation\n"
        "- [ ] Data, study area, time range, and scale\n"
        "- [ ] Method and assumptions\n"
        "- [ ] Evidence from key figures and tables\n"
        "- [ ] Limitations and uncertainty\n"
        "- [ ] Personal evaluation and follow-up questions\n"
    )


def migrate_readme(readme: Path, output: Path, apply: bool = False) -> MigrationResult:
    """Plan or perform a non-destructive migration from README sections."""
    records = scan_readme(readme)
    created = 0
    skipped = 0
    files: list[Path] = []
    seen: set[Path] = set()
    name_counts: dict[Path, int] = {}

    for record in records:
        category_directory = output / slugify(record.category)
        base_destination = category_directory / f"{slugify(record.title)}.md"
        destination = base_destination
        if base_destination in name_counts:
            name_counts[base_destination] += 1
            destination = base_destination.with_name(
                f"{base_destination.stem}-{name_counts[base_destination]}{base_destination.suffix}"
            )
        else:
            name_counts[base_destination] = 1

        while destination in seen:
            name_counts[base_destination] += 1
            destination = base_destination.with_name(
                f"{base_destination.stem}-{name_counts[base_destination]}{base_destination.suffix}"
            )

        if destination.exists():
            skipped += 1
            continue
        seen.add(destination)
        files.append(destination)
        if apply:
            write_text(destination, render_note(record))
            created += 1

    return MigrationResult(created=created, skipped=skipped, files=tuple(files))

