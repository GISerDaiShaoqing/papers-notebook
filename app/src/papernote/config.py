from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True, slots=True)
class ProjectPaths:
    repository: Path

    @property
    def readme(self) -> Path:
        return self.repository / "README.md"

    @property
    def assets(self) -> Path:
        return self.repository / "app" / "assets"

    @property
    def picture_directory(self) -> Path:
        return self.repository / "Picture"

    @classmethod
    def from_root(cls, root: Path) -> "ProjectPaths":
        repository = root.expanduser().resolve()
        if not (repository / "README.md").is_file():
            raise FileNotFoundError(f"README.md was not found under {repository}")
        return cls(repository)

