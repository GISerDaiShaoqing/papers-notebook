# Repository scripts

Maintenance scripts should be safe to run repeatedly and produce a reviewable diff before changing paper notes.

- `prepare_site.py` generates the MkDocs source tree from `notes/`, `Picture/`, and `website/`.
- `serve_site.ps1` prepares and opens a local preview at `http://127.0.0.1:8000`.

