from __future__ import annotations

import html
import json
import re
from pathlib import Path


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def render_html(markdown_text: str) -> str:
    """Render a paper note as a calm, long-form article for the live preview."""
    import markdown

    metadata: dict[str, str] = {}
    frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*(?:\n|$)", markdown_text, re.DOTALL)
    if frontmatter:
        for line in frontmatter.group(1).splitlines():
            match = re.match(r"^([\w-]+):\s*(.*)$", line)
            if not match:
                continue
            key, value = match.groups()
            value = value.strip()
            try:
                value = str(json.loads(value))
            except json.JSONDecodeError:
                value = value.strip("\"'")
            metadata[key] = value
        markdown_text = markdown_text[frontmatter.end():]

    title = metadata.get("title", "").strip()
    first_heading = re.match(r"\s*#\s+(.+?)\s*(?:\n|$)", markdown_text)
    if first_heading:
        if not title:
            title = first_heading.group(1).strip()
        if first_heading.group(1).strip().casefold() == title.casefold():
            markdown_text = markdown_text[first_heading.end():]

    body = markdown.markdown(
        markdown_text,
        extensions=["extra", "sane_lists", "tables", "fenced_code"],
    )
    title_html = f'<h1 class="article-title">{html.escape(title)}</h1>' if title else ""
    category = html.escape(metadata.get("category", "论文阅读笔记"))
    status = {
        "reviewed": "已完成",
        "reading": "阅读中",
        "partial": "持续补充",
        "unread": "待读",
        "needs-source": "待补原文",
    }.get(metadata.get("status", ""), "论文阅读笔记")
    return f"""<!doctype html>
<html><head><meta charset="utf-8"><style>
body {{ background: #f4f7f6; color: #34434a; font-family: "Segoe UI", "Microsoft YaHei UI", "PingFang SC", "Noto Sans CJK SC", sans-serif; font-size: 15px; line-height: 1.95; }}
.article {{ background: #ffffff; margin: 18px auto; padding: 30px 38px 48px; max-width: 760px; }}
.article-header {{ border-bottom: 1px solid #edf0ee; margin-bottom: 26px; padding-bottom: 20px; }}
.article-brand {{ color: #83928d; font-size: 10px; font-weight: bold; letter-spacing: 2px; }}
.article-title {{ color: #263a36; font-size: 25px; font-weight: 700; line-height: 1.48; margin: 14px 0 13px; }}
.article-meta {{ color: #87938f; font-size: 12px; line-height: 1.6; }}
.article-meta .category {{ color: #367c6a; }}
.article-body p {{ margin: 0 0 1.15em; }}
.article-body h1 {{ color: #263a36; font-size: 23px; line-height: 1.5; }}
.article-body h2 {{ background: #f3f8f6; border-left: 3px solid #5b9a83; color: #315f52; font-size: 18px; line-height: 1.55; margin: 2em 0 1em; padding: 7px 12px; }}
.article-body h3 {{ color: #3b6659; font-size: 16px; margin: 1.7em 0 .8em; }}
.article-body ul, .article-body ol {{ padding-left: 1.6em; }}
.article-body li {{ margin: .35em 0; }}
.article-body blockquote {{ background: #f5f8f7; border-left: 3px solid #8bb5a7; color: #687772; margin: 1.2em 0; padding: 10px 16px; }}
.article-body code {{ background: #f1f4f3; border-radius: 3px; color: #815c42; font-family: Consolas, monospace; padding: 2px 4px; }}
.article-body pre {{ background: #f3f5f4; border-radius: 5px; padding: 12px 15px; }}
.article-body img {{ display: block; height: auto; margin: 1.5em auto; max-width: 100%; }}
.article-body a {{ color: #287b68; text-decoration: none; }}
.article-body table {{ border-collapse: collapse; margin: 1.2em 0; }}
.article-body th {{ background: #f2f6f4; color: #3f5f53; }}
.article-body th, .article-body td {{ border: 1px solid #e1e8e4; padding: 7px 10px; }}
hr {{ border: 0; border-top: 1px solid #e8ecea; margin: 1.8em 0; }}
</style></head><body><div class="article"><div class="article-header">
<div class="article-brand">DAI_PNS · PAPER NOTE STUDIO</div>{title_html}
<div class="article-meta"><span class="category">{category}</span>　·　{html.escape(status)}</div>
</div><div class="article-body">{body}</div></div></body></html>"""

