from __future__ import annotations

import os
import sys
from pathlib import Path


APP_ROOT = Path(__file__).resolve().parent


def _build_path(path: str) -> str:
    """Keep host-injected native libraries out of PyInstaller's DLL scan."""
    return os.pathsep.join(
        entry for entry in path.split(os.pathsep) if "codex-runtimes" not in entry.casefold()
    )


def main() -> None:
    from PyInstaller.__main__ import run

    os.chdir(APP_ROOT)
    icon_name = {
        "win32": "papernote.ico",
        "darwin": "papernote.icns",
    }.get(sys.platform, "papernote.png")
    icon_path = APP_ROOT / "assets" / icon_name
    add_data = f"{APP_ROOT / 'assets'}{os.pathsep}assets"
    original_path = os.environ.get("PATH", "")
    os.environ["PATH"] = _build_path(original_path)
    try:
        build_args = [
            "--noconfirm",
            "--clean",
            "--windowed",
            "--onefile",
            "--name",
            "Dai_PNS",
            "--distpath",
            str(APP_ROOT / "dist"),
            "--workpath",
            str(APP_ROOT / "build"),
            "--specpath",
            str(APP_ROOT),
            "--icon",
            str(icon_path),
            "--paths",
            str(APP_ROOT / "src"),
            "--add-data",
            add_data,
            "--collect-all",
            "pypdfium2",
            "--collect-all",
            "pypdfium2_raw",
            "--collect-all",
            "keyring",
        ]
        if sys.platform == "win32":
            conda_runtime = Path(sys.base_prefix) / "Library" / "bin"
            for name in (
                "ffi.dll",
                "libcrypto-3-x64.dll",
                "libssl-3-x64.dll",
                "liblzma.dll",
                "libbz2.dll",
                "libexpat.dll",
            ):
                runtime_dll = conda_runtime / name
                if runtime_dll.is_file():
                    build_args.extend(["--add-binary", f"{runtime_dll}{os.pathsep}."])
        build_args.append(str(APP_ROOT / "launcher.py"))
        run(build_args)
    finally:
        os.environ["PATH"] = original_path


if __name__ == "__main__":
    main()
