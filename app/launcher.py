from __future__ import annotations

import os
import sys
from pathlib import Path


def find_repository() -> Path | None:
    configured = os.environ.get("PAPERNOTE_REPOSITORY")
    if configured:
        candidate = Path(configured).expanduser().resolve()
        if (candidate / "README.md").is_file() and (candidate / "notes").is_dir():
            return candidate

    executable_dir = Path(sys.executable if getattr(sys, "frozen", False) else __file__).resolve().parent
    for candidate in (executable_dir, *executable_dir.parents):
        if (candidate / "README.md").is_file() and (candidate / "notes").is_dir():
            return candidate
    return None


def main() -> None:
    from papernote.ui.main_window import run_gui

    run_gui(find_repository())


if __name__ == "__main__":
    main()

