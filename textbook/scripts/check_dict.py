"""Cổng 2 (spec mục 5, 7): kiểm tra từ điển Tầng 2 Tu-dien-*.md của một bộ.

    python textbook/scripts/check_dict.py <unit> [--file Tu-dien-….md] [--threshold 0.65] [--mark] [--verbose]

Với mỗi từ điển:
  - frontmatter đủ khoá; 'chuong' (và 'phan' nếu có) khớp tên nhóm trong progress.json;
  - có mục Quy ước sử dụng, Ghi chú nguồn cần kiểm tra; mỗi bài (kind bai) của nhóm có một mục
    "## <label>: <title>", không có mục bài lạ;
  - mọi bảng đúng tiêu đề 4 cột; dòng "Ngoài nguồn" đúng mẫu spec 5.2;
  - thuật ngữ có định nghĩa: tên chính hoặc tên trong ngoặc phải trùng một cụm in đậm ở Tầng 1 của nhóm
    (kể cả tiêu đề in đậm "**a) …**"), và Giải nghĩa khớp đoạn chứa cụm đó (bigram có dấu ≥ ngưỡng);
  - thuật ngữ mô tả (Bối cảnh bắt đầu bằng "[mô tả] "): không có chỗ in đậm, có ít nhất một đoạn Tầng 1
    gắn nhãn <!-- term: <tên> -->, và Giải nghĩa khớp phần ghép các đoạn đó (bigram ≥ ngưỡng);
  - ghi chú nguồn đúng dạng spec 5.6; trang_thai verified thì không còn ghi chú [mở].
--mark: từ điển đạt thì đổi các bài của nhóm từ layer1 sang layer2 trong progress.json.
"""

import argparse
import re
import sys
import unicodedata

from _common import (display_title, iter_nodes, load_profile, load_progress, progress_path, setup_stdout,
                     unit_dir, write_json)
from check_lesson import bigrams, lesson_paths, split_frontmatter, tokens

FM_KEYS = ["name", "description", "loai_hoc_lieu", "mon", "lop", "chuong", "bai_so", "nguon",
           "ngay_tao", "ngay_cap_nhat", "trang_thai"]
OUT_RE = re.compile(r"^Ngoài nguồn — chưa định nghĩa trong (.+?)\. Xem: (.+)$")
NOTE_RE = re.compile(r"^\d+\. \[(mở|đóng)\] (.+?) — Thuật ngữ: (.+?) — (.+)$")
CLOSED_RE = re.compile(r" → .+ \(\d{4}-\d{2}-\d{2}\)$")
BOLD_RE = re.compile(r"\*\*([^*]+)\*\*")
TERM_RE = re.compile(r"<!--\s*term:\s*(.+?)\s*-->")
DESC = "[mô tả] "


def norm(text):
    return unicodedata.normalize("NFC", text).strip().lower()


def split_term(cell):
    """'Điểm khởi đầu sao chép (Ori)' -> ('Điểm khởi đầu sao chép', ['Ori']).

    Tên phụ phải cách tên chính bằng dấu cách, để tên có ngoặc liền chữ như 'Keo dán poly(urea-formaldehyde)'
    không bị tách.
    """
    m = re.fullmatch(r"(.+?)\s+\((.+)\)", cell.strip())
    if not m:
        return cell.strip(), []
    return m.group(1).strip(), [a.strip() for a in re.split(r"[;,]", m.group(2)) if a.strip()]


def bold_index(lesson_files):
    """(cụm in đậm, nhãn mô tả): mỗi cái là dict tên (chuẩn hoá) -> [(id bài, đoạn)]."""
    index, described = {}, {}
    for lid, path in lesson_files:
        _, body = split_frontmatter(path.read_text(encoding="utf-8"))
        paras = re.split(r"\n\s*\n", body)
        for i, para in enumerate(paras):
            heading = re.fullmatch(r"\*\*[a-z]\)\s*([^*]+)\*\*", para.strip())
            if heading:
                # tiêu đề "**a) mRNA**": nội dung là các đoạn sau đến tiêu đề kế tiếp
                body_paras = []
                for nxt in paras[i + 1:]:
                    s = nxt.strip()
                    if s.startswith("#") or re.fullmatch(r"\*\*[a-z]\)[^*]+\*\*", s):
                        break
                    body_paras.append(nxt)
                index.setdefault(norm(heading.group(1)), []).append((lid, "\n".join(body_paras)))
                continue
            for name in TERM_RE.findall(para):
                described.setdefault(norm(name), []).append((lid, TERM_RE.sub("", para)))
            for b in BOLD_RE.findall(para):
                phrase = b.strip().rstrip(":")
                index.setdefault(norm(phrase), []).append((lid, para))
    return index, described


def parse_rows(lines):
    """Các dòng bảng sau tiêu đề 4 cột -> list 4 ô."""
    rows = []
    for l in lines:
        if not l.startswith("|") or set(l.replace("|", "").strip()) <= {"-", " "}:
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        rows.append(cells)
    return rows


def header_of(profile):
    return "| " + " | ".join(profile["dictionary_columns"]["headers"]) + " |"


def check_dict(unit, path, progress, threshold, verbose):
    errors, flags = [], []
    HEADER = header_of(load_profile(unit))
    fm, body = split_frontmatter(path.read_text(encoding="utf-8"))
    if fm is None:
        return ["thiếu frontmatter"], [], None, None
    for k in FM_KEYS:
        if k not in fm:
            errors.append(f"frontmatter thiếu khoá '{k}'")

    group, parents = None, ()
    for node, par in iter_nodes(progress["toc"]):
        if node["role"] == "group" and display_title(node) == fm.get("chuong"):
            group, parents = node, par
    if group is None:
        return errors + [f"'chuong' = {fm.get('chuong')!r} không trùng tên nhóm nào trong progress.json"], [], fm, None
    if parents and fm.get("phan") != display_title(parents[-1]):
        errors.append(f"'phan' phải là {display_title(parents[-1])!r}")
    if fm.get("trang_thai") not in ("draft", "verified"):
        errors.append("'trang_thai' phải là draft hoặc verified")

    lessons = [n for n in group["children"] if n["role"] == "lesson"]
    files = lesson_paths(unit, progress["toc"])
    lesson_files = [(n["id"], files[n["id"]][1]) for n in lessons if n["id"] in files and files[n["id"]][1].exists()]
    missing = [n["id"] for n in lessons if (n["id"], files.get(n["id"], (None, None))[1]) not in lesson_files]
    if missing:
        errors.append(f"chưa có Tầng 1 cho: {', '.join(missing)}")
    glossaries = [(n["id"], files[n["id"]][1]) for n, _ in iter_nodes(progress["toc"])
                  if n["role"] == "back_matter" and n["id"] in files and files[n["id"]][1].exists()]
    bolds, described = bold_index(lesson_files + glossaries)

    # tách mục ##
    sections, cur = {}, None
    for line in body.splitlines():
        if line.startswith("## "):
            cur = line[3:].strip()
            sections[cur] = []
        elif cur:
            sections[cur].append(line)
    for need in ("Quy ước sử dụng", "Ghi chú nguồn cần kiểm tra"):
        if need not in sections:
            errors.append(f"thiếu mục '## {need}'")
    want = {f"{n['label']}: {n['title']}" if n.get("label") else n["title"]: n for n in lessons if n["kind"] == "bai"}
    allowed = set(want) | {"Quy ước sử dụng", "Thuật ngữ dùng chung", "Đã xét, không tạo mục", "Ghi chú nguồn cần kiểm tra"}
    for name in sections:
        if name not in allowed:
            errors.append(f"mục '## {name}' không khớp bài nào trong nhóm (phải là '## <label>: <title>')")
    for name in want:
        if name not in sections:
            errors.append(f"thiếu mục '## {name}'")

    # bảng thuật ngữ
    seen, out_count, term_count, desc_count = set(), 0, 0, 0
    for name, lines in sections.items():
        if name in ("Quy ước sử dụng", "Đã xét, không tạo mục", "Ghi chú nguồn cần kiểm tra"):
            continue
        tables = [l.strip() for l in lines if l.startswith("|")]
        if tables and tables[0] != HEADER:
            errors.append(f"[{name}] tiêu đề bảng phải là: {HEADER}")
        for cells in parse_rows(tables[1:]):
            if len(cells) != 4:
                errors.append(f"[{name}] dòng không đủ 4 cột: {' | '.join(cells)[:80]}")
                continue
            term, aliases = split_term(cells[0])
            key = norm(term)
            if key in seen:
                errors.append(f"[{name}] thuật ngữ trùng: {term}")
            seen.add(key)
            term_count += 1
            meaning = cells[2]
            if meaning.startswith("Ngoài nguồn"):
                out_count += 1
                if not OUT_RE.match(meaning):
                    errors.append(f"[{name}] {term}: dòng Ngoài nguồn sai mẫu spec 5.2 (không được kèm định nghĩa)")
                continue
            keys = [key] + [norm(a) for a in aliases]
            hits = [h for k in keys for h in bolds.get(k, [])]
            tagged = [h for k in keys for h in described.get(k, [])]
            if cells[3].startswith(DESC):
                desc_count += 1
                if hits:
                    errors.append(f"[{name}] {term}: sách đã có câu định nghĩa (chỗ in đậm), bỏ tiền tố [mô tả]")
                    continue
                if not tagged:
                    errors.append(f"[{name}] {term}: dòng mô tả nhưng Tầng 1 không có đoạn gắn nhãn <!-- term: {term} -->")
                    continue
                refs = [" ".join(p for _, p in tagged)]
            else:
                if not hits:
                    errors.append(f"[{name}] {term}: không có chỗ in đậm ở Tầng 1"
                                  + (" (có nhãn mô tả: thêm tiền tố [mô tả] ở cột Bối cảnh)" if tagged else ""))
                    continue
                refs = [p for _, p in hits]
            bg = bigrams(tokens(meaning))
            if len(bg) < 2:
                errors.append(f"[{name}] {term}: Giải nghĩa quá ngắn")
                continue
            ratio = max(sum(b in set(bigrams(tokens(p))) for b in bg) / len(bg) for p in refs)
            if verbose:
                print(f"    {ratio:.2f} {term} ({(hits or tagged)[0][0]})")
            if ratio < threshold:
                flags.append(f"[{name}] {term}: Giải nghĩa khớp đoạn Tầng 1 {ratio:.2f} < {threshold}")

    # ghi chú nguồn
    open_notes = 0
    for line in sections.get("Ghi chú nguồn cần kiểm tra", []):
        s = line.strip()
        if not s or not re.match(r"^\d+\.", s):
            continue
        m = NOTE_RE.match(s)
        if not m:
            errors.append(f"ghi chú sai dạng spec 5.6: {s[:80]}")
            continue
        if m.group(1) == "mở":
            open_notes += 1
        elif not CLOSED_RE.search(s):
            errors.append(f"ghi chú [đóng] thiếu ' → <kết luận> (YYYY-MM-DD)': {s[:80]}")
    if fm.get("trang_thai") == "verified" and open_notes:
        errors.append(f"trang_thai verified nhưng còn {open_notes} ghi chú [mở]")

    stats = {"terms": term_count, "desc": desc_count, "out": out_count, "open": open_notes}
    return errors, flags, fm, (group, stats)


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("unit")
    ap.add_argument("--file")
    ap.add_argument("--threshold", type=float, default=0.65)
    ap.add_argument("--mark", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    progress = load_progress(a.unit)
    base = unit_dir(a.unit)
    paths = [base / a.file] if a.file else sorted(base.glob("Tu-dien-*.md"))
    if not paths:
        raise SystemExit(f"Chưa có từ điển Tu-dien-*.md trong {base}")
    bad = 0
    for path in paths:
        errors, flags, fm, info = check_dict(a.unit, path, progress, a.threshold, a.verbose)
        ok = not errors and not flags
        extra = ""
        if info:
            st = info[1]
            extra = f" ({st['terms']} thuật ngữ, {st['desc']} mô tả, {st['out']} Ngoài nguồn, {st['open']} ghi chú mở)"
        print(f"{path.name} {'ĐẠT' if ok else 'KHÔNG ĐẠT'}{extra} — {len(errors)} lỗi, {len(flags)} cờ")
        for e in errors:
            print(f"  lỗi: {e}")
        for f in flags:
            print(f"  cờ:  {f}")
        if not ok:
            bad += 1
        elif a.mark:
            for n in info[0]["children"]:
                if n.get("status") == "layer1":
                    n["status"] = "layer2"
            write_json(progress_path(a.unit), progress)
            print("  đã đổi các bài của nhóm sang layer2")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
