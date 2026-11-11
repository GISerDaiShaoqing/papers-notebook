from __future__ import annotations

import argparse
from collections import Counter
from pathlib import Path
import sys

from .services.index_service import sync_index
from .services.metadata_service import (
    MetadataLookupError,
    fetch_crossref,
    update_note_frontmatter,
    write_metadata_draft,
)
from .services.note_migration import migrate_readme
from .ui.main_window import run_gui
from .services.note_scanner import scan_readme


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Maintain the Dai_PNS paper notebook")
    subparsers = parser.add_subparsers(dest="command", required=True)

    scan = subparsers.add_parser("scan", help="list paper entries and missing template fields")
    scan.add_argument("--readme", type=Path, required=True, help="README.md to scan")
    scan.add_argument("--all", action="store_true", help="include papers without missing fields")
    run = subparsers.add_parser("run", help="start the desktop application")
    run.add_argument("--root", type=Path, required=True, help="papers-notebook repository root")
    migrate = subparsers.add_parser("migrate", help="plan or create individual paper note files")
    migrate.add_argument("--readme", type=Path, required=True, help="legacy README.md to parse")
    migrate.add_argument("--output", type=Path, required=True, help="notes directory to create")
    migrate.add_argument("--apply", action="store_true", help="write files; default is preview only")
    report = subparsers.add_parser("report", help="summarize paper reading progress")
    report.add_argument("--readme", type=Path, required=True, help="README.md to scan")
    index = subparsers.add_parser("sync-index", help="generate an index for individual notes")
    index.add_argument("--notes", type=Path, required=True, help="individual notes directory")
    index.add_argument("--output", type=Path, required=True, help="index Markdown file")
    index.add_argument("--apply", action="store_true", help="write the index; default is preview only")
    enrich = subparsers.add_parser("enrich", help="retrieve DOI metadata into a reviewable draft")
    enrich.add_argument("--doi", required=True, help="DOI or DOI URL")
    enrich.add_argument("--output", type=Path, help="new draft Markdown file")
    enrich.add_argument("--note", type=Path, help="existing note whose empty metadata fields may be filled")
    enrich.add_argument("--apply", action="store_true", help="write the draft; default is preview only")
    return parser


def main(argv: list[str] | None = None) -> None:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = _build_parser().parse_args(argv)
    if args.command == "scan":
        records = scan_readme(args.readme)
        for record in records:
            missing = record.missing_fields
            if missing or args.all:
                suffix = ", ".join(missing) if missing else "complete"
                print(f"[{record.status.value}] {record.category} / {record.title}: {suffix}")
        print(f"Scanned {len(records)} paper entries from {args.readme}")
    elif args.command == "run":
        run_gui(args.root)
    elif args.command == "migrate":
        result = migrate_readme(args.readme, args.output, apply=args.apply)
        action = "Created" if args.apply else "Planned"
        for path in result.files:
            print(f"{action}: {path}")
        print(f"{action.lower()} {len(result.files)} files; skipped {result.skipped}")
    elif args.command == "report":
        records = scan_readme(args.readme)
        statuses = Counter(record.status.value for record in records)
        missing = Counter(
            field for record in records for field in record.missing_fields
        )
        print(f"papers: {len(records)}")
        print("statuses:")
        for status, count in sorted(statuses.items()):
            print(f"  {status}: {count}")
        print("missing fields:")
        for field, count in missing.most_common():
            print(f"  {field}: {count}")
    elif args.command == "sync-index":
        count = sync_index(args.notes, args.output, apply=args.apply)
        action = "Wrote" if args.apply else "Planned"
        print(f"{action} index for {count} individual notes: {args.output}")
    elif args.command == "enrich":
        if bool(args.output) == bool(args.note):
            raise SystemExit("enrich requires exactly one of --output or --note")
        try:
            metadata = fetch_crossref(args.doi)
        except MetadataLookupError as exc:
            raise SystemExit(f"metadata lookup failed: {exc}") from exc
        print(f"title: {metadata.title}")
        print(f"doi: {metadata.doi}")
        print(f"authors: {', '.join(metadata.authors)}")
        print(f"year: {metadata.year or ''}")
        print(f"venue: {metadata.venue}")
        if args.apply:
            try:
                if args.note:
                    changed = update_note_frontmatter(args.note, metadata)
                    print(f"Updated {args.note}: {', '.join(changed) or 'no empty fields'}")
                else:
                    write_metadata_draft(args.output, metadata)
                    print(f"Wrote reviewable draft: {args.output}")
            except (FileExistsError, ValueError) as exc:
                raise SystemExit(str(exc)) from exc
        else:
            target = args.note or args.output
            action = "fill empty metadata fields" if args.note else "write a reviewable draft"
            print(f"Planned to {action}: {target} (use --apply to write)")

