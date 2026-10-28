"""Cổng 0 và cổng 1 (spec mục 7): kiểm tra progress.json và các file bài học Tầng 1.

    python textbook/scripts/check_lesson.py <unit> [--lesson ID ...] [--threshold 0.65] [--mark] [--verbose]

Cổng 0: progress.json hợp lệ theo schema, id không trùng.
Cổng 1, với mỗi bài đã có file:
  - frontmatter đủ khoá và khớp progress.json; tiêu đề # đúng tên bài;
  - mốc <!-- pdf:N --> đủ mọi trang trong pdf_pages, theo thứ tự;
  - mỗi đoạn có tỉ lệ bigram có dấu khớp OCR trang (trang N và N+1) ≥ ngưỡng. Đoạn bị gắn cờ phải
    đối chiếu ảnh trang; đúng thì thêm ngay sau đoạn một dòng <!-- ocr-ok: <lý do> --> để bỏ qua;
  - hình trong figures.json của bài có file trong img/, được chèn vào bài và có dòng trong bảng 📷.
--mark: bài qua cổng 1 được đổi status thành layer1 trong progress.json và status: verified ở frontmatter.
"""

import argparse
import re
import sys
import unicodedata

import yaml

from _common import (display_title, iter_nodes, load_json, load_profile, load_progress, ocr_cache_path,
                     parse_unit, progress_path, schema_errors, section_matchers, setup_stdout, unit_dir,
                     write_json)

FM_KEYS = ["unit", "lesson_id", "toc_path", "source_file", "pdf_pages", "lesson_type", "status"]
PAGE_RE = re.compile(r"^<!--\s*pdf:(\d+)\s*-->$")
OK_RE = re.compile(r"^<!--\s*ocr-ok:.*-->$")
IMG_RE = re.compile(r"!\[[^\]]*\]\(img/([^)]+)\.png\)")
EMOJI_H2 = ("🎯", "🔤", "🔴", "❓", "💡", "📌", "✏️", "📷")


def tokens(text):
    text = unicodedata.normalize("NFC", text.lower())
    text = re.sub(r"\$[^$]*\$", " ", text)              # bỏ LaTeX
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)   # bỏ ảnh
    return re.findall(r"\w+", text)


def bigrams(toks):
    return list(zip(toks, toks[1:]))


def lesson_paths(unit, toc):
    """id -> (node, đường dẫn file Tầng 1, tuple nút cha)."""
    base = unit_dir(unit)
    out = {}
    for node, parents in iter_nodes(toc):
        if node["role"] == "group" or not node.get("file"):
            continue
        folder = base.joinpath(*[p["dir"] for p in parents])
        out[node["id"]] = (node, folder / node["file"], parents)
    return out


def split_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None, text
    return yaml.safe_load(m.group(1)), text[m.end():]


def blocks_by_page(body):
    """Tách thân bài thành các đoạn (cách nhau bởi dòng trống), gắn với trang PDF của mốc gần nhất phía trước."""
    page, blocks, cur, in_figlist, in_code = None, [], [], False, False

    def flush():
        if cur:
            blocks.append((page, list(cur)))
            cur.clear()

    for line in body.splitlines():
        s = line.strip()
        if s.startswith("```"):
            flush()
            in_code = not in_code  # mã lệnh chép từ ảnh, không đem so OCR (spec 4.3)
            continue
        if in_code:
            continue
        m = PAGE_RE.match(s)
        if m:
            flush()
            page = int(m.group(1))
            continue
        if s.startswith("## "):
            in_figlist = s.startswith("## 📷")
        if in_figlist or s.startswith("# ") or s.startswith(tuple("## " + e for e in EMOJI_H2)):
            continue  # tiêu đề bài (đã so với progress.json) và nhãn hộp là nhãn cấu trúc; OCR khó đọc chữ trang trí
        if not s:
            flush()
        elif OK_RE.match(s):
            flush()
            if blocks:
                blocks[-1] = (blocks[-1][0], blocks[-1][1], "ok")
        elif s.startswith("<!--"):
            flush()  # ghi chú của người chép, không phải chữ của sách
        else:
            cur.append(s)
    flush()
    return blocks


def heading_ok(line, profile):
    """Heading ## / ### hợp lệ: hộp emoji, một cấp mục của hồ sơ, hoặc heading thêm của hồ sơ."""
    level, text = line.split(" ", 1)
    if level == "##" and text.startswith(EMOJI_H2):
        return True
    for prefix, rx in section_matchers(profile):
        if prefix == level + " " and rx.match(text):
            return True
    return any(re.match(rx, text) for rx in profile["extra_headings"])


def check_lesson(unit, node, path, parents, threshold, verbose):
    errors, flags = [], []
    profile = load_profile(unit)
    text = path.read_text(encoding="utf-8")
    fm, body = split_frontmatter(text)

    # frontmatter
    if fm is None:
        return ["thiếu frontmatter"], [], None
    for k in FM_KEYS:
        if k not in fm:
            errors.append(f"frontmatter thiếu khoá '{k}'")
    expect = {
        "unit": unit, "lesson_id": node["id"],
        "toc_path": [display_title(p) for p in parents] + [display_title(node)],
        "source_file": node["source_file"], "pdf_pages": node["pdf_pages"],
        "lesson_type": node.get("lesson_type"),
    }
    for k, v in expect.items():
        if k in fm and fm[k] != v:
            errors.append(f"frontmatter '{k}' = {fm[k]!r}, progress.json là {v!r}")
    if fm.get("status") not in ("draft", "verified"):
        errors.append("frontmatter 'status' phải là draft hoặc verified")

    # tiêu đề
    h1 = [l[2:].strip() for l in body.splitlines() if l.startswith("# ")]
    want = (f"{node['label']}: {node['title']}" if node.get("label") else node["title"]).upper()
    if h1 != [want]:
        errors.append(f"tiêu đề # phải là đúng một dòng '{want}', đang có {h1}")

    # heading
    for line in body.splitlines():
        if line.startswith(("## ", "### ", "#### ")) and not heading_ok(line, profile):
            errors.append(f"heading không đúng khung (spec 4.2, hồ sơ '{profile['profile']}'): {line}")

    # mốc trang
    marks = [int(m.group(1)) for m in (PAGE_RE.match(l.strip()) for l in body.splitlines()) if m]
    first, last = node["pdf_pages"]
    if marks != list(range(first, last + 1)):
        errors.append(f"mốc trang phải là {first}..{last} đủ và theo thứ tự, đang có {marks}")
    if body.strip() and not PAGE_RE.match(body.strip().splitlines()[0].strip()):
        errors.append("dòng đầu thân bài phải là mốc <!-- pdf:N -->")

    # so khớp OCR theo đoạn
    page_bigrams = {}

    def ocr(page):
        if page not in page_bigrams:
            f = ocr_cache_path(unit, node["source_file"], page)
            page_bigrams[page] = set(bigrams(tokens(f.read_text(encoding="utf-8")))) if f.exists() else None
        return page_bigrams[page]

    for blk in blocks_by_page(body):
        page, lines = blk[0], blk[1]
        reviewed = len(blk) > 2
        para = " ".join(lines)
        bg = bigrams(tokens(re.sub(r"[|*_>#\\-]", " ", para)))
        if len(bg) < 4 or page is None:
            continue
        ref = set()
        for p in (page, page + 1):
            if first <= p <= last:
                got = ocr(p)
                if got is None:
                    errors.append(f"chưa có cache OCR trang {p} (chạy ocr_pages.py)")
                    got = set()
                ref |= got
        ratio = sum(b in ref for b in bg) / len(bg)
        if verbose:
            print(f"    pdf:{page} {ratio:.2f} {para[:70]}")
        if ratio < threshold and not reviewed:
            flags.append(f"pdf:{page} khớp {ratio:.2f}: {para[:90]}")

    # hình
    folder = path.parent
    fig_file = folder / "figures.json"
    figures = load_json(fig_file) if fig_file.exists() else {}
    subject, grade = parse_unit(unit)
    prefix = f"H{grade}-{subject}-{node['id']}-"
    mine = {k for k in figures if k.startswith(prefix)}
    used = set(IMG_RE.findall(body))
    table = body.split("## 📷", 1)[1] if "## 📷" in body else ""
    for fid in sorted(mine):
        if not (folder / "img" / f"{fid}.png").exists():
            errors.append(f"hình {fid}: chưa có img/{fid}.png (chạy crop_figures.py)")
        if fid not in used:
            errors.append(f"hình {fid}: chưa chèn vào bài")
        if f"| {fid} |" not in table:
            errors.append(f"hình {fid}: chưa có dòng trong bảng 📷")
    for fid in sorted(used - mine):
        errors.append(f"hình {fid} được chèn nhưng không có trong figures.json")
    if used and "## 📷" not in body:
        errors.append("bài có hình nhưng thiếu mục ## 📷 Danh sách hình trong bài")

    return errors, flags, fm


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("unit")
    ap.add_argument("--lesson", nargs="+", metavar="ID")
    ap.add_argument("--threshold", type=float, default=0.65)
    ap.add_argument("--mark", action="store_true")
    ap.add_argument("--verbose", action="store_true")
    a = ap.parse_args()

    progress = load_progress(a.unit)
    if progress is None:
        raise SystemExit(f"Chưa có {progress_path(a.unit)}")
    profile = load_profile(a.unit)
    if profile["verbatim_scope"] == "cho_quyet_dinh":
        raise SystemExit(f"Hồ sơ môn '{profile['profile']}' chưa chốt phạm vi chép nguyên văn (verbatim_scope): "
                         "hỏi người dùng rồi sửa specs/profiles/ trước khi làm Tầng 1.")
    if profile["status"] != "da_kiem_chung":
        print(f"Cảnh báo: hồ sơ môn '{profile['profile']}' chưa kiểm chứng trên PDF — khảo sát 1–2 bài đầu, "
              "sửa hồ sơ và đổi status thành da_kiem_chung trước khi làm hàng loạt (spec 10).")

    # cổng 0
    errs = schema_errors(progress, "progress")
    ids = [n["id"] for n, _ in iter_nodes(progress["toc"])]
    errs += [f"id trùng: {i}" for i in sorted({i for i in ids if ids.count(i) > 1})]
    if errs:
        print("Cổng 0 KHÔNG ĐẠT:\n  " + "\n  ".join(errs))
        sys.exit(1)
    print("Cổng 0: progress.json hợp lệ.")

    lessons = lesson_paths(a.unit, progress["toc"])
    wanted = a.lesson or [i for i, (_, p, _) in lessons.items() if p.exists()]
    bad = 0
    passed = []
    for lid in wanted:
        if lid not in lessons:
            print(f"{lid}: không có trong progress.json hoặc không có file Tầng 1")
            bad += 1
            continue
        node, path, parents = lessons[lid]
        if not path.exists():
            print(f"{lid}: chưa có file {path.relative_to(unit_dir(a.unit))}")
            bad += 1
            continue
        errors, flags, fm = check_lesson(a.unit, node, path, parents, a.threshold, a.verbose)
        ok = not errors and not flags
        print(f"{lid} {'ĐẠT' if ok else 'KHÔNG ĐẠT'} — {len(errors)} lỗi, {len(flags)} đoạn cần đối chiếu ảnh")
        for e in errors:
            print(f"  lỗi: {e}")
        for f in flags:
            print(f"  cờ:  {f}")
        if ok:
            passed.append((node, path, fm))
        else:
            bad += 1

    if a.mark and passed:
        for node, path, fm in passed:
            if node["status"] == "pending":
                node["status"] = "layer1"
            if fm.get("status") != "verified":
                text = path.read_text(encoding="utf-8")
                path.write_text(re.sub(r"(?m)^status: draft$", "status: verified", text, count=1),
                                encoding="utf-8", newline="\n")
        write_json(progress_path(a.unit), progress)
        print(f"Đã đánh dấu {len(passed)} bài qua cổng 1.")

    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
