"""Biên dịch các file Tu-dien-<Mon>.md sang glossary_master.json và dataset/by_subject/<mon>.json (SPEC-GLOSSARY-V2).

    python textbook/glossary_v2/scripts/build_glossary_v2.py [--md-dir textbook/glossary_v2/markdown] [--out-dir textbook/glossary_v2/dataset]
"""

from __future__ import annotations

import argparse
import collections
import datetime as dt
import json
import sys
from pathlib import Path

import jsonschema

from check_glossary_v2 import FILE_TO_DISCIPLINE, setup_utf8, validate_directory

SUBJECT_SLUGS = {v[0]: v[1] for v in FILE_TO_DISCIPLINE.values()}


def entry_matches_discipline(entry: dict, discipline: str) -> bool:
    if entry["origin_discipline"] == discipline:
        return True
    for ctx in entry["contexts"]:
        if discipline in ctx.get("disciplines", []):
            return True
    for src in entry["sources"]:
        if discipline.lower() in src["book"].lower():
            return True
    return False


def build_payload(
    entries: list[dict],
    kind: str,
    subject_filter: str | None,
    source_files: list[str],
    conflicts: list[dict] | None = None,
    review_items: list[dict] | None = None,
) -> dict:
    sorted_entries = sorted(entries, key=lambda e: (e["term_en"].lower(), e["term_en"]))
    by_disc = collections.Counter(e["origin_discipline"] for e in sorted_entries)
    multi_ctx = sum(1 for e in sorted_entries if len(e["contexts"]) > 1 or len(e["sources"]) > 1)
    alt_exp = sum(1 for e in sorted_entries if e["alt_explanations"])

    counts: dict = {
        "entries": len(sorted_entries),
        "by_origin_discipline": dict(sorted(by_disc.items())),
        "multi_context_entries": multi_ctx,
        "alt_explanation_entries": alt_exp,
    }
    payload: dict = {
        "meta": {
            "schema_version": "2.0",
            "kind": kind,
            "subject_filter": subject_filter,
            "generated_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            "source_markdown_files": source_files,
            "counts": counts,
        },
        "entries": sorted_entries,
    }
    if conflicts is not None:
        counts["conflicts"] = len(conflicts)
        payload["conflicts"] = conflicts
    if review_items is not None:
        counts["review_candidates"] = len(review_items)
        payload["review_candidates"] = review_items
    return payload


def main() -> None:
    setup_utf8()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--md-dir", default="glossary/v2/markdown")
    ap.add_argument("--out-dir", default="glossary/v2/data")
    ap.add_argument("--schema", default="tools/schema/glossary_v2.schema.json")
    args = ap.parse_args()

    md_dir = Path(args.md_dir)
    out_dir = Path(args.out_dir)
    schema_path = Path(args.schema)

    entries, conflicts, review_items, errors, warnings = validate_directory(md_dir)
    if errors:
        print(f"DỪNG BIÊN DỊCH: phát hiện {len(errors)} lỗi định dạng/chống trùng:")
        for e in errors[:40]:
            print(f"  - {e}")
        sys.exit(1)

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = jsonschema.Draft202012Validator(schema)

    source_files = sorted(p.name for p in md_dir.glob("Tu-dien-*.md"))
    out_dir.mkdir(parents=True, exist_ok=True)
    by_subj_dir = out_dir / "by_subject"
    by_subj_dir.mkdir(parents=True, exist_ok=True)

    master = build_payload(
        entries=entries,
        kind="master",
        subject_filter=None,
        source_files=source_files,
        conflicts=conflicts,
        review_items=review_items,
    )
    schema_errs = list(validator.iter_errors(master))
    if schema_errs:
        for se in schema_errs[:10]:
            print(f"  [SCHEMA ERROR] {list(se.path)}: {se.message}")
        sys.exit(1)

    master_path = out_dir / "glossary_master.json"
    master_path.write_text(json.dumps(master, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Đã xuất {master_path} ({len(master['entries'])} mục từ, 0 lỗi schema)")

    # Subject-specific JSON exports (pulling cross-disciplinary terms via contexts/sources)
    active_disciplines = {e["origin_discipline"] for e in entries} | {
        d for e in entries for c in e["contexts"] for d in c["disciplines"]
    }
    for disc in sorted(active_disciplines):
        slug = SUBJECT_SLUGS[disc]
        sub_entries = [e for e in entries if entry_matches_discipline(e, disc)]
        if not sub_entries:
            continue
        sub_payload = build_payload(
            entries=sub_entries,
            kind="subject",
            subject_filter=disc,
            source_files=source_files,
        )
        sub_errs = list(validator.iter_errors(sub_payload))
        if sub_errs:
            for se in sub_errs[:10]:
                print(f"  [SCHEMA ERROR {slug}] {list(se.path)}: {se.message}")
            sys.exit(1)
        sub_path = by_subj_dir / f"{slug}.json"
        sub_path.write_text(json.dumps(sub_payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        cross_cnt = sum(1 for e in sub_entries if e["origin_discipline"] != disc)
        print(f"Đã xuất {sub_path} ({len(sub_entries)} mục từ, gồm {cross_cnt} mục liên môn kéo kèm)")

    if warnings:
        print(f"Lưu ý: có {len(warnings)} cảnh báo nhẹ.")


if __name__ == "__main__":
    main()
