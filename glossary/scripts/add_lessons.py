#!/usr/bin/env python3
"""Thêm hoặc sửa một lô "Yêu cầu cần đạt" (mảng lessons) vào glossary/<unit>/<unit>.json an toàn.

    python glossary/scripts/add_lessons.py <unit> <file-lo.json> [--update]

Lô là một mảng JSON các mục bài đầy đủ trường theo schema.json ($defs/lesson).
Khoá của một mục: (level, chapter, lesson); lesson = null nghĩa là cả chương (vd Unit Tiếng Anh).
- Mặc định: khoá đã có là lỗi.
- --update: thay thế mục có khoá đã tồn tại; khoá chưa tồn tại là lỗi.
Mảng lessons được sắp theo thứ tự chương/bài trong progress.json (SGK trước, chuyên đề sau).
Hợp lệ: sao lưu <unit>.json.bak -> ghi file tạm -> đổi tên đè. Không hợp lệ: in lỗi, không ghi gì.
"""
import argparse
import sys
from datetime import date

from _common import (data_path, dataset_path, lesson_errors, lesson_key, lesson_label, load_json,
                     load_schema, load_unit, parse_unit, progress_lessons, progress_order,
                     schema_errors, schema_validator, setup_stdout, write_json_atomic)

LEVEL_ORDER = {"co_ban": 0, "chuyen_de": 1}


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("unit")
    ap.add_argument("batch")
    ap.add_argument("--update", action="store_true", help="sửa mục đã có (theo khoá level, chapter, lesson)")
    a = ap.parse_args()

    if not parse_unit(a.unit):
        sys.exit(f"LỖI: tên bộ không hợp lệ: {a.unit}")
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

    lesson_v = schema_validator(schema, "#/$defs/lesson")
    for i, e in enumerate(batch):
        errs += schema_errors(lesson_v, e, f"lô[{i}]" + (lesson_label(e) if isinstance(e, dict) else ""))
    entries = [e for e in batch if isinstance(e, dict)]

    keys = [lesson_key(e) for e in entries]
    dup = {k for k in keys if keys.count(k) > 1}
    if dup:
        errs.append(f"khoá lặp trong lô: {sorted(dup, key=str)}")

    current = data.get("lessons") or []
    own = {lesson_key(e) for e in current}
    for e in entries:
        if a.update and lesson_key(e) not in own:
            errs.append(f"{lesson_label(e)} --update nhưng mục chưa tồn tại trong {a.unit}")
        elif not a.update and lesson_key(e) in own:
            errs.append(f"{lesson_label(e)} mục đã tồn tại trong {a.unit} (dùng --update để sửa)")

    new_by_key = {lesson_key(e): e for e in entries}
    if a.update:
        merged = [new_by_key.get(lesson_key(e), e) for e in current]
    else:
        merged = current + entries
    order = progress_order(a.unit)
    merged.sort(key=lambda e: (LEVEL_ORDER.get(e.get("level"), 9),
                               order.get((e.get("chapter"), e.get("lesson")), 1 << 20)))
    labels = {lesson_label(e) for e in entries}
    errs += [m for m in lesson_errors(a.unit, merged, progress_lessons(a.unit), {})
             if any(m.startswith(lab) for lab in labels)]

    if errs:
        print(f"KHÔNG GHI. {len(errs)} lỗi:")
        for m in errs:
            print("  -", m)
        sys.exit(1)

    data["lessons"] = merged
    data["meta"]["lesson_count"] = len(merged)
    data["meta"]["last_updated"] = date.today().isoformat()
    full_errs = schema_errors(schema_validator(schema), data, a.unit)
    if full_errs:
        print("KHÔNG GHI. Dữ liệu sau khi ghép không hợp lệ:")
        for m in full_errs:
            print("  -", m)
        sys.exit(1)

    write_json_atomic(path, data)
    verb = "Đã sửa" if a.update else "Đã thêm"
    print(f"{verb} {len(entries)} mục yêu cầu cần đạt vào {path.name}. Tổng: {len(merged)}.")
    print(f"Đã đồng bộ vào dataset/{dataset_path(a.unit).name}.")


if __name__ == "__main__":
    main()
