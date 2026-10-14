#!/usr/bin/env python3
"""Thêm hoặc sửa một lô thuật ngữ vào glossary/<unit>/<unit>.json một cách an toàn.

    python glossary/scripts/add_terms.py <unit> <file-lo.json> [--update]

Lô là một mảng JSON các thuật ngữ đầy đủ trường theo schema.json.
- Mặc định: id trùng với id đã có trong toàn môn là lỗi.
- --update: thay thế thuật ngữ có id đã tồn tại trong cùng bộ; id chưa tồn tại là lỗi.
Hợp lệ: sao lưu <unit>.json.bak -> ghi file tạm -> đổi tên đè. Không hợp lệ: in lỗi, không ghi gì.
"""
import argparse
import sys
from datetime import date

from _common import (data_path, load_json, load_schema, load_unit, parse_unit,
                     progress_lessons, schema_errors, schema_validator, setup_stdout,
                     subject_ids, term_errors, write_json_atomic)


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("unit")
    ap.add_argument("batch")
    ap.add_argument("--update", action="store_true", help="sửa thuật ngữ đã có (theo id)")
    a = ap.parse_args()

    parsed = parse_unit(a.unit)
    if not parsed:
        sys.exit(f"LỖI: tên bộ không hợp lệ: {a.unit}")
    subject, _ = parsed
    path = data_path(a.unit)
    if not path.exists():
        sys.exit(f"LỖI: không thấy {path}. Tạo bộ trước (xem README).")

    try:
        batch = load_json(a.batch)
    except (OSError, ValueError) as e:
        sys.exit(f"LỖI: không đọc được lô {a.batch}: {e}")
    if not isinstance(batch, list) or not batch:
        sys.exit("LỖI: lô phải là một mảng JSON không rỗng")

    data = load_unit(a.unit)
    schema = load_schema()
    errs = []

    term_v = schema_validator(schema, "#/$defs/term")
    for i, t in enumerate(batch):
        lab = f"lô[{i}]" + (f"[{t.get('id')}]" if isinstance(t, dict) else "")
        errs += schema_errors(term_v, t, lab)

    batch_ids = [t.get("id") for t in batch if isinstance(t, dict)]
    dup = {x for x in batch_ids if batch_ids.count(x) > 1}
    if dup:
        errs.append(f"id lặp trong lô: {sorted(dup)}")

    own_ids = {t["id"] for t in data["terms"]}
    other_ids = subject_ids(subject, exclude_unit=a.unit)
    for tid in batch_ids:
        if a.update:
            if tid not in own_ids:
                errs.append(f"[{tid}] --update nhưng id chưa tồn tại trong {a.unit}")
        else:
            if tid in own_ids:
                errs.append(f"[{tid}] id đã tồn tại trong {a.unit} (dùng --update để sửa)")
            elif tid in other_ids:
                errs.append(f"[{tid}] id đã tồn tại ở bộ {other_ids[tid]}")

    # Ghép kết quả dự kiến rồi kiểm tra toàn bộ.
    new_by_id = {t.get("id"): t for t in batch if isinstance(t, dict)}
    if a.update:
        merged = [new_by_id.get(t["id"], t) for t in data["terms"]]
    else:
        merged = data["terms"] + [t for t in batch if isinstance(t, dict)]
    known = set(other_ids) | {t.get("id") for t in merged}
    batch_set = set(new_by_id)
    errs += [e for e in term_errors(a.unit, merged, known, progress_lessons(a.unit), {})
             if e[1:].split("]")[0] in batch_set or not e.startswith("[")]

    if errs:
        print(f"KHÔNG GHI. {len(errs)} lỗi:")
        for e in errs:
            print("  -", e)
        sys.exit(1)

    data["terms"] = merged
    data["meta"]["term_count"] = len(merged)
    data["meta"]["last_updated"] = date.today().isoformat()
    full_errs = schema_errors(schema_validator(schema), data, a.unit)
    if full_errs:
        print("KHÔNG GHI. Dữ liệu sau khi ghép không hợp lệ:")
        for e in full_errs:
            print("  -", e)
        sys.exit(1)

    write_json_atomic(path, data)
    verb = "Đã sửa" if a.update else "Đã thêm"
    print(f"{verb} {len(batch)} thuật ngữ vào {path.name}. Tổng: {len(merged)}.")


if __name__ == "__main__":
    main()
