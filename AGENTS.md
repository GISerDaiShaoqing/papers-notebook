# PaperNoteDesktop maintenance guide

## Project purpose

This repository stores the five finished research notes selected by the owner as the standard for future notes, along with the maintained Dai_PNS application and a generated reading website.

The outer `src/` and `win7/` folders are historical distributions. Keep them intact for reference and rollback. New application work belongs under `app/` in this repository.

## Repository layout

- `README.md`: repository home page and index of the five finished notes.
- `Picture/`: images referenced by existing notes.
- `notes/`: individual paper notes and the curated `categories.json` topic list.
- `website/`: maintained landing page and styling for the generated notes website.
- `webdocs/` and `site/`: generated website inputs and output; do not edit or commit these directories.
- `app/src/papernote/`: maintained Python application package.
- `app/legacy/`: archived copy of the original Python 2 application and build metadata.
- `app/assets/`: application icons and UI assets.
- `.agents/skills/paper-reading/`: reusable Codex skill for drafting paper reading notes.
- `app/tests/`: automated tests for parsing, file handling, and application services.
- `scripts/`: repository maintenance commands and index generation.

## Application rules

1. Use Python 3 and UTF-8 for all new code and text files.
2. Build the desktop interface with PySide6. Use `app/build.py` and `.github/workflows/build-desktop.yml` to create Windows, macOS, and Linux builds.
   - On Windows, keep the build-time `PATH` filter in `app/build.py`. Codex's injected Poppler runtime supplies an ICU DLL with version-suffixed exports that conflicts with PySide6's QtCore; the packaged app must use the compatible Windows ICU instead.
   - Keep the display name, author, repository links, and version in `app/src/papernote/__init__.py` synchronized with the About dialog, package metadata, and build artifact name.
   - The original `gnb.ico` is retained in `app/assets/` as the source reference. The active `papernote.svg`, PNG, ICO, and ICNS assets should preserve its notebook, binding, paperclip, and conversation motifs.
3. Keep user data operations separate from the UI. UI handlers should call application services rather than parse or rewrite notes directly.
4. Use `pathlib.Path` for filesystem paths. Resolve paths from the repository or an explicit configuration value; never depend on the process current directory.
5. Read and write text with an explicit UTF-8 encoding and preserve the original file before any bulk migration.
6. Do not overwrite non-empty user notes during automatic enrichment. Generate a diff or a draft file first.
7. External commands must use argument lists with `subprocess.run`; do not construct shell command strings.
8. Keep the legacy application available for comparison. Do not modify or delete the outer `src/` or `win7/` directories as part of routine refactoring.
9. When a note format changes, update the parser, template, index generator, and documentation together.
10. Build artifacts are outputs. Do not hand-edit generated executables or PyInstaller intermediate files.
11. Keep PDF highlights in an output copy. Send note or PDF text to an AI provider only when the user explicitly requests an AI action.
12. Treat `notes/categories.json` as the persistent topic list. Keep categories that the owner wants to explore even when they have no notes; do not remove categories when deleting incomplete papers.
13. Treat files under `notes/` and images under `Picture/` as the website's source of truth. Prepare local site input with `python scripts/prepare_site.py`, then build with `python -m mkdocs build --strict`; edit `website/` for the landing page or article styling, never generated `webdocs/` or `site/` files. On Windows, `scripts/serve_site.ps1` starts the local preview.
14. Do not create Git commits for the owner. After completing work, provide the relevant Git commands so the owner can review, stage, commit, and push changes themselves.

## Paper note schema

Each paper is one Markdown file under `notes/<category>/`. The owner's complete-note examples are:

- `notes/gis-remote-sensing-and-spatial-methods/r-package-gdistance-distances-and-routes-on-geographical-grids.md`
- `notes/urban-analytics-mobility-and-land-use/characterizing-mixed-use-buildings-based-on-multi-source-big-data.md`
- `notes/carbon-emissions-and-urban-development/chinas-co2-emissions-estimated-from-the-bottom-up-recent-trends-spatial-b078b474.md`
- `notes/remote-sensing-data-assimilation/a-simplified-data-assimilation-method-for-reconstructing-time-series-mo-2377ffec.md`
- `notes/forest-landscape-and-ecosystem-services/global-patterns-of-tropical-forest-fragmentation.md`

Treat these five notes as the authority for what “complete” means in this repository. Follow their level of detail, use of Chinese and English paper terminology, discussion of data and methods, evidence, figures, and personal interpretation. Do not add a generic checklist as a gate for completeness.

The existing README uses `Title`, `Link`, `Doi`, `Notes`, `Highlights`, `Research gap/question`, `Discussion/Conclusion`, `Graph/Table interested`, and `Resources`. The parser must continue to accept those labels, including the historical `Hightlights` spelling and both ASCII and full-width colons.

## Reading standard

The five examples above are complete because the owner designated them as such. Use them as the writing benchmark for future notes; an autogenerated checklist does not define completion. A title, abstract, or automatically retrieved metadata alone is not a finished note.

Recommended workflow:

1. Read the full paper when available and use the five examples to match the intended depth and voice.
2. Explain the paper's question, data, method, evidence, and conclusions in their context; cite page, figure, or table details where useful.
3. Separate claims in the paper from the note author's interpretation. Do not invent personal evaluations or missing evidence.
4. Preserve the headings used by the examples: `Notes`, `Highlights`, `Research gap/question`, `Discussion/Conclusion`, `Graph/Table interested`, and `Resources`.
5. Leave unavailable information explicitly blank or marked for review.

Use these statuses:

- `unread`: no substantive reading note yet.
- `reading`: active reading in progress.
- `partial`: some sections are filled but the argument is incomplete.
- `reviewed`: the owner considers the note complete by the standard of the five examples.
- `needs-source`: the original paper or reliable metadata is unavailable.

## Automatic updates

Automatic tools may fill reliable bibliographic metadata from a DOI or source URL. They may create a clearly marked reading prompt or draft, but must not invent methods, results, citations, or personal evaluations. Generated changes must retain their source, leave existing non-empty text untouched, and be reviewable as a Git diff. Generated text must not change a paper to `reviewed` without the owner's confirmation.

Invoke the repository's `$paper-reading` skill to draft or continue a note using the five examples as references. AI output is a draft for the owner to review; it must not overwrite a completed note or mark a paper complete on its own.

Useful maintenance commands will include:

- `papernote scan`: list empty fields and incomplete papers.
- `papernote enrich --doi <doi> --output <draft>`: retrieve public metadata into a reviewable draft.
- `papernote enrich --doi <doi> --note <path> --apply`: fill only empty metadata fields in an existing note.
- `papernote draft <paper>`: create a reading outline.
- `papernote sync-index`: rebuild the top-level README index.
- `papernote report`: summarize reading progress and missing sources.

