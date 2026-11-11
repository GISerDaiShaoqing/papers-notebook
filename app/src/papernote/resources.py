from __future__ import annotations

import sys
from pathlib import Path


def bundled_asset(name: str) -> Path:
    """Return an asset path in source checkouts and PyInstaller bundles."""
    if getattr(sys, "frozen", False):
        base = Path(getattr(sys, "_MEIPASS", Path(sys.executable).resolve().parent))
    else:
        base = Path(__file__).resolve().parents[2]
    return base / "assets" / name
