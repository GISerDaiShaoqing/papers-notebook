from __future__ import annotations

import subprocess
from pathlib import Path


class TocGenerationError(RuntimeError):
    """Raised when gh-md-toc cannot generate an index."""


def generate_toc(executable: Path, markdown_file: Path) -> str:
    if not executable.is_file():
        raise TocGenerationError(f"目录工具不存在: {executable}")
    if not markdown_file.is_file():
        raise TocGenerationError(f"Markdown 文件不存在: {markdown_file}")

    try:
        result = subprocess.run(
            [str(executable), markdown_file.name],
            cwd=str(markdown_file.parent),
            capture_output=True,
            check=True,
            encoding="utf-8",
            errors="replace",
        )
    except (OSError, subprocess.CalledProcessError) as exc:
        detail = getattr(exc, "stderr", "") or str(exc)
        raise TocGenerationError(f"目录生成失败: {detail}") from exc
    return result.stdout

