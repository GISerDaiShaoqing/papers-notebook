from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from .markdown_service import write_text


@dataclass(frozen=True, slots=True)
class PaperMetadata:
    doi: str
    title: str
    authors: tuple[str, ...] = ()
    year: int | None = None
    venue: str = ""
    url: str = ""
    abstract: str = ""


class MetadataLookupError(RuntimeError):
    """Raised when a public metadata provider cannot answer a DOI lookup."""


def normalize_doi(value: str) -> str:
    doi = value.strip()
    doi = re.sub(r"^https?://(dx\.)?doi\.org/", "", doi, flags=re.IGNORECASE)
    doi = re.sub(r"^doi:\s*", "", doi, flags=re.IGNORECASE)
    return doi.rstrip(" .")


def _clean_abstract(value: str) -> str:
    return re.sub(r"<[^>]+>", "", value or "").replace("\n", " ").strip()


def fetch_crossref(doi: str, timeout: float = 15.0) -> PaperMetadata:
    normalized = normalize_doi(doi)
    if not normalized:
        raise MetadataLookupError("A DOI is required")

    url = f"https://api.crossref.org/works/{normalized}"
    request = Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": "Dai_PNS/0.2.0",
        },
    )
    try:
        with urlopen(request, timeout=timeout) as response:
            payload = json.load(response)
    except (HTTPError, URLError, TimeoutError, OSError) as exc:
        raise MetadataLookupError(f"Crossref lookup failed for {normalized}: {exc}") from exc

    message = payload.get("message", {})
    titles = message.get("title") or []
    title = str(titles[0]).strip() if titles else ""
    authors = tuple(
        " ".join(part for part in (author.get("given"), author.get("family")) if part).strip()
        for author in message.get("author", [])
    )
    date_parts = (message.get("published-print") or message.get("published-online") or {}).get("date-parts", [[]])
    year = date_parts[0][0] if date_parts and date_parts[0] else None
    venues = message.get("container-title") or []
    return PaperMetadata(
        doi=normalized,
        title=title,
        authors=tuple(author for author in authors if author),
        year=year,
        venue=str(venues[0]).strip() if venues else "",
        url=str(message.get("URL") or f"https://doi.org/{normalized}"),
        abstract=_clean_abstract(str(message.get("abstract") or "")),
    )


def render_metadata_draft(metadata: PaperMetadata, source: str = "Crossref") -> str:
    authors = ", ".join(metadata.authors) if metadata.authors else ""
    lines = [
        "<!-- AUTO-GENERATED DRAFT: verify against the original paper before merging. -->",
        f"<!-- source: {source}; retrieved: {date.today().isoformat()} -->",
        "",
        f"# {metadata.title or '[title unavailable]'}",
        "",
        "## Bibliographic metadata",
        "",
        f"- DOI: {metadata.doi}",
        f"- Authors: {authors}",
        f"- Year: {metadata.year or ''}",
        f"- Venue: {metadata.venue}",
        f"- URL: {metadata.url}",
        "",
        "## Abstract from provider",
        "",
        metadata.abstract,
        "",
        "## Human reading notes",
        "",
        "- Research question and motivation:",
        "- Data and study area:",
        "- Method and assumptions:",
        "- Results and evidence:",
        "- Limitations and uncertainty:",
        "- Personal evaluation:",
        "- Follow-up questions:",
        "",
    ]
    return "\n".join(lines)


def write_metadata_draft(path: Path, metadata: PaperMetadata, source: str = "Crossref") -> None:
    if path.exists():
        raise FileExistsError(f"Refusing to overwrite existing file: {path}")
    write_text(path, render_metadata_draft(metadata, source=source))


def update_note_frontmatter(path: Path, metadata: PaperMetadata, source: str = "Crossref") -> list[str]:
    """Fill only empty metadata keys in an existing migrated note."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"\A---\r?\n(?P<body>.*?)\r?\n---\r?\n", text, flags=re.DOTALL)
    if not match:
        raise ValueError(f"Note has no frontmatter: {path}")

    lines = match.group("body").splitlines()
    values = {
        "doi": metadata.doi,
        "authors": json.dumps(list(metadata.authors), ensure_ascii=False),
        "year": str(metadata.year or ""),
        "venue": json.dumps(metadata.venue, ensure_ascii=False),
        "url": json.dumps(metadata.url, ensure_ascii=False),
        "metadata_source": json.dumps(source, ensure_ascii=False),
        "metadata_retrieved": date.today().isoformat(),
    }
    changed: list[str] = []
    present: set[str] = set()
    for index, line in enumerate(lines):
        field = re.match(r"^(\w+):\s*(.*)$", line)
        if not field or field.group(1) not in values:
            continue
        key, current = field.group(1), field.group(2).strip()
        present.add(key)
        if current not in {"", "[]", "\"\"", "''", "null"}:
            continue
        lines[index] = f"{key}: {values[key]}"
        changed.append(key)

    insert_at = len(lines)
    for key, value in values.items():
        if key not in present:
            lines.insert(insert_at, f"{key}: {value}")
            insert_at += 1
            changed.append(key)

    if changed:
        updated = "---\n" + "\n".join(lines) + "\n---\n" + text[match.end() :]
        write_text(path, updated)
    return changed

