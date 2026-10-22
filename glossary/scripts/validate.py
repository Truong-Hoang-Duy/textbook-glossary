#!/usr/bin/env python3
"""Kiểm tra cấu trúc dữ liệu glossary.

    python glossary/scripts/validate.py [<unit>|<mon>]

Không tham số: kiểm tra mọi bộ. Mã thoát 1 nếu có lỗi.
"""
import sys

from _common import (GLOSSARY_DIR, ROOT, book_dir, classify_book, data_path, dataset_path,
                     lesson_errors, list_units, load_json, load_schema, parse_unit,
                     progress_lessons, progress_path, schema_errors, schema_validator,
                     setup_stdout, term_errors, unit_dir)

SIZE_WARN = 300 * 1024
STATUSES = {"pending", "in_progress", "done"}


def check_progress(unit):
    errs = []
    p = progress_path(unit)
    if not p.exists():
        return [f"thiếu {p.relative_to(GLOSSARY_DIR.parent)}"]
    try:
        prog = load_json(p)
    except ValueError as e:
        return [f"progress.json không phải JSON hợp lệ: {e}"]
    if prog.get("unit") != unit:
        errs.append(f"progress.json: unit = {prog.get('unit')!r}, phải là {unit!r}")
    books = prog.get("books") or {}
    if book_dir(unit).is_dir():
        for pdf in sorted(book_dir(unit).glob("*.pdf")):
            if pdf.name not in books:
                errs.append(f"progress.json: thiếu sách {pdf.name} trong books (mọi PDF của bộ, kể cả SGV, phải có mặt)")
            if classify_book(pdf.name) is None:
                errs.append(f"không nhận diện được loại sách theo tên file: {pdf.name}")
    for fname, b in books.items():
        if not (book_dir(unit) / fname).exists():
            try:
                rel_dir = book_dir(unit).relative_to(GLOSSARY_DIR.parent)
            except ValueError:
                rel_dir = unit
            errs.append(f"progress.json: sách không có trong {rel_dir}/: {fname}")
        if b.get("status") not in STATUSES:
            errs.append(f"progress.json [{fname}]: status không hợp lệ: {b.get('status')!r}")
        for ch, chd in (b.get("chapters") or {}).items():
            for le, led in (chd.get("lessons") or {}).items():
                if led.get("status") not in STATUSES:
                    errs.append(f"progress.json [{fname}] {le}: status không hợp lệ: {led.get('status')!r}")
    return errs


def check_unit(unit, schema, all_ids):
    errs, warns = [], []
    parsed = parse_unit(unit)
    if not parsed:
        return [f"tên thư mục không đúng quy ước {{mon}}_{{lop}}: {unit}"], warns
    subject, grade = parsed
    path = data_path(unit)
    if not path.exists():
        try:
            rel_p = path.relative_to(ROOT)
        except ValueError:
            rel_p = f"{unit}.json"
        return [f"thiếu file dữ liệu {rel_p} (tên file phải trùng tên thư mục)"], warns
    if not dataset_path(unit).exists():
        warns.append(f"chưa có bản sao đồng bộ trong glossary/dataset/{unit}.json")
    if dataset_path(unit).with_name(f"{unit}.json.bak").exists():
        errs.append(f"không để file .bak trong glossary/dataset/: {unit}.json.bak")
    stray = [p.name for p in unit_dir(unit).glob("*.json")
             if p.name not in (f"{unit}.json", "progress.json")]
    if stray:
        warns.append(f"file JSON lạ trong thư mục bộ: {stray}")
    if not book_dir(unit).is_dir():
        errs.append(f"không có thư mục sách {book_dir(unit)}")
    try:
        data = load_json(path)
    except ValueError as e:
        return [f"JSON không hợp lệ: {e}"], warns

    errs += schema_errors(schema_validator(schema), data, unit)
    meta = data.get("meta") or {}
    if meta.get("unit") != unit:
        errs.append(f"meta.unit = {meta.get('unit')!r}, phải là {unit!r}")
    if meta.get("grade") != grade:
        errs.append(f"meta.grade = {meta.get('grade')!r}, phải là {grade}")
    if meta.get("subject") != subject:
        errs.append(f"meta.subject = {meta.get('subject')!r}, phải là {subject!r}")
    terms = [t for t in data.get("terms") or [] if isinstance(t, dict)]
    if meta.get("term_count") != len(terms):
        errs.append(f"meta.term_count = {meta.get('term_count')}, thực tế {len(terms)}")
    lessons = [e for e in data.get("lessons") or [] if isinstance(e, dict)]
    if meta.get("lesson_count") != len(lessons):
        errs.append(f"meta.lesson_count = {meta.get('lesson_count')}, thực tế {len(lessons)}")

    prog_lessons = progress_lessons(unit)
    page_counts = {}
    errs += term_errors(unit, terms, all_ids.get(subject, {}), prog_lessons, page_counts)
    errs += lesson_errors(unit, lessons, prog_lessons, page_counts)
    errs += check_progress(unit)
    if dataset_path(unit).exists() and load_json(dataset_path(unit)) != data:
        warns.append(f"glossary/dataset/{unit}.json khác bản trong thư mục bộ (chưa đồng bộ)")

    size = path.stat().st_size
    info = f"{len(terms)} thuật ngữ, {len(lessons)} bài YCCĐ, {size / 1024:.1f} KB"
    if size > SIZE_WARN:
        warns.append(f"file lớn hơn 300 KB ({size / 1024:.1f} KB)")
    return errs, warns, info


def main():
    setup_stdout()
    target = sys.argv[1] if len(sys.argv) > 1 else None
    schema = load_schema()
    units = list_units()

    # id toàn môn (để kiểm tra trùng và related_terms xuyên bộ).
    all_ids, owners, dup_errs = {}, {}, []
    for u in units:
        parsed = parse_unit(u)
        if not parsed or not data_path(u).exists():
            continue
        try:
            terms = load_json(data_path(u)).get("terms") or []
        except ValueError:
            continue
        for t in terms:
            if not isinstance(t, dict) or "id" not in t:
                continue
            key = (parsed[0], t["id"])
            if key in owners:
                dup_errs.append((u, f"id trùng trong môn {parsed[0]}: {t['id']} (đã có ở {owners[key]})"))
            owners[key] = u
            all_ids.setdefault(parsed[0], {})[t["id"]] = u

    if target:
        if parse_unit(target):
            units = [target] if target in units else []
            if not units:
                try:
                    rel_u = unit_dir(target).relative_to(ROOT)
                except ValueError:
                    rel_u = target
                sys.exit(f"LỖI: không có {rel_u}/")
        else:
            units = [u for u in units if parse_unit(u) and parse_unit(u)[0] == target]
            if not units:
                sys.exit(f"LỖI: không có bộ nào thuộc môn '{target}'")

    total_err = 0
    for u in units:
        res = check_unit(u, schema, all_ids)
        errs, warns = res[0], res[1]
        errs += [m for du, m in dup_errs if du == u]
        info = res[2] if len(res) > 2 else ""
        status = "OK" if not errs else f"{len(errs)} LỖI"
        print(f"== {u}: {status}" + (f" ({info})" if info else ""))
        for e in errs:
            print("  LỖI:", e)
        for w in warns:
            print("  CẢNH BÁO:", w)
        total_err += len(errs)
    print(f"\nTổng: {len(units)} bộ, {total_err} lỗi.")
    sys.exit(1 if total_err else 0)


if __name__ == "__main__":
    main()
