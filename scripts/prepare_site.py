from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTES_ROOT = ROOT / "notes"
SITE_DOCS = ROOT / "webdocs"

STATUS_LABELS = {
    "reviewed": "已完成",
    "reading": "阅读中",
    "partial": "持续补充",
    "unread": "待读",
    "needs-source": "待补原文",
}


def _yaml_value(value: str) -> str:
    value = value.strip()
    try:
        return str(json.loads(value))
    except json.JSONDecodeError:
        return value.strip("\"'")


def _metadata_and_body(text: str) -> tuple[dict[str, str], str]:
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", text, re.DOTALL)
    if not frontmatter:
        return {}, text

    metadata: dict[str, str] = {}
    for line in frontmatter.group(1).splitlines():
        match = re.match(r"^([\w-]+):\s*(.*)$", line)
        if match:
            metadata[match.group(1)] = _yaml_value(match.group(2))
    return metadata, text[frontmatter.end():]


def _article_markdown(text: str) -> str:
    metadata, body = _metadata_and_body(text)
    title = metadata.get("title", "").strip()
    heading = re.match(r"\s*#\s+(.+?)\s*(?:\n|$)", body)
    if heading:
        if not title:
            title = heading.group(1).strip()
        if heading.group(1).strip().casefold() == title.casefold():
            body = body[heading.end():]

    category = metadata.get("category", "论文阅读笔记")
    status = STATUS_LABELS.get(metadata.get("status", ""), "论文阅读笔记")
    title_block = f"# {title}\n\n" if title else ""
    return f"{title_block}_{category} · {status}_\n\n---\n\n{body.lstrip()}"


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.casefold()).strip("-")


def prepare_site() -> None:
    if SITE_DOCS.resolve().parent != ROOT.resolve():
        raise RuntimeError(f"Unexpected generated site directory: {SITE_DOCS}")
    if SITE_DOCS.exists():
        shutil.rmtree(SITE_DOCS)

    SITE_DOCS.mkdir(parents=True)
    shutil.copy2(ROOT / "website" / "index.md", SITE_DOCS / "index.md")
    shutil.copytree(
        NOTES_ROOT,
        SITE_DOCS / "notes",
        ignore=shutil.ignore_patterns("README.md", "categories.json"),
    )
    shutil.copytree(ROOT / "Picture", SITE_DOCS / "Picture")
    styles = SITE_DOCS / "styles"
    styles.mkdir()
    shutil.copy2(ROOT / "website" / "paper-notes.css", styles / "paper-notes.css")

    categories = json.loads((NOTES_ROOT / "categories.json").read_text(encoding="utf-8"))
    grouped: dict[str, list[tuple[str, str, str]]] = {category: [] for category in categories}
    for path in (SITE_DOCS / "notes").rglob("*.md"):
        if path.name == "INDEX.md":
            continue
        raw_text = path.read_text(encoding="utf-8")
        metadata, _ = _metadata_and_body(raw_text)
        category = metadata.get("category", "")
        if category in grouped:
            grouped[category].append((metadata.get("title", path.stem), path.relative_to(SITE_DOCS / "notes").as_posix(), metadata.get("status", "")))
        path.write_text(_article_markdown(raw_text), encoding="utf-8", newline="\n")

    category_pages = SITE_DOCS / "notes" / "categories"
    category_pages.mkdir()
    for category, entries in grouped.items():
        lines = [f"# {category}", "", "该主题下的论文阅读笔记：", ""]
        if entries:
            for title, relative_path, status in sorted(entries, key=lambda entry: entry[0].casefold()):
                label = STATUS_LABELS.get(status, "论文阅读笔记")
                lines.append(f"- [{title}](../{relative_path}) — {label}")
        else:
            lines.append("目前还没有笔记，后续可以在 Dai_PNS 中新建。")
        (category_pages / f"{_slug(category)}.md").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


if __name__ == "__main__":
    prepare_site()
