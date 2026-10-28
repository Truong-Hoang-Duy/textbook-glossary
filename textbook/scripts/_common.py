"""Hàm dùng chung cho textbook/scripts/.

Bố cục (spec mục 2):
    <gốc>/sgk/khoi_<lop>/<unit>/SGK*.pdf          nguồn
    <gốc>/textbook/khoi_<lop>/<unit>/              kết quả của bộ
    <gốc>/cache/ocr/<unit>/<pdf>/pNNNN.txt          cache OCR (tự sinh, không thuộc kết quả)
    <gốc>/textbook/schema/*.schema.json            schema
    <gốc>/textbook/tessdata/                       dữ liệu tesseract
"""

import json
import os
import re
import shutil
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TEXTBOOK_DIR = ROOT / "textbook"
SCHEMA_DIR = TEXTBOOK_DIR / "schema"
TESSDATA_DIR = TEXTBOOK_DIR / "tessdata"
SGK_DIR = ROOT / "sgk"
PROFILE_DIR = ROOT / "specs" / "profiles"
OCR_CACHE_DIR = ROOT / "cache" / "ocr"

UNIT_RE = re.compile(r"^([a-z]+(?:_[a-z]+)*)_(10|11|12)$")


def setup_stdout():
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")


def parse_unit(unit):
    """'sinh_12' -> ('sinh', 12)."""
    m = UNIT_RE.match(unit)
    if not m:
        raise SystemExit(f"Tên bộ không hợp lệ: {unit!r} (dạng <mon>_<lop>, ví dụ sinh_12)")
    return m.group(1), int(m.group(2))


def unit_dir(unit):
    _, grade = parse_unit(unit)
    return TEXTBOOK_DIR / f"khoi_{grade}" / unit


def book_dir(unit):
    _, grade = parse_unit(unit)
    return SGK_DIR / f"khoi_{grade}" / unit


def progress_path(unit):
    return unit_dir(unit) / "progress.json"


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def write_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    with open(tmp, "w", encoding="utf-8", newline="\n") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")
    os.replace(tmp, path)


def load_progress(unit):
    path = progress_path(unit)
    return load_json(path) if path.exists() else None


def schema_errors(data, schema_name):
    """Danh sách lỗi (chuỗi) khi kiểm tra data theo textbook/schema/<schema_name>.schema.json."""
    from jsonschema import Draft202012Validator

    schema = load_json(SCHEMA_DIR / f"{schema_name}.schema.json")
    validator = Draft202012Validator(schema)
    errors = sorted(validator.iter_errors(data), key=lambda e: list(e.absolute_path))
    return ["/".join(str(p) for p in e.absolute_path) + ": " + e.message for e in errors]


def iter_nodes(toc, parents=()):
    """Duyệt cây toc theo thứ tự in; trả về (node, tuple các nút cha)."""
    for node in toc:
        yield node, parents
        yield from iter_nodes(node.get("children", []), parents + (node,))


def display_title(node):
    """Tên hiển thị đầy đủ: 'label. title' hoặc chỉ 'title' (spec mục 3.3)."""
    return f"{node['label']}. {node['title']}" if node.get("label") else node["title"]


def strip_accents(text):
    text = text.replace("đ", "d").replace("Đ", "D")
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")


def slugify(text, max_len=50):
    """'Di truyền học' -> 'Di-truyen-hoc'. Giữ hoa/thường, cắt ở ranh giới từ khi dài quá max_len."""
    words = re.findall(r"[A-Za-z0-9]+", strip_accents(text))
    out = ""
    for w in words:
        nxt = f"{out}-{w}" if out else w
        if len(nxt) > max_len and out:
            break
        out = nxt
    return out


def load_profile(unit):
    """Hồ sơ môn của bộ (spec mục 10): _default.json phủ bởi hồ sơ có 'subjects' chứa mã môn."""
    subject, _ = parse_unit(unit)
    profile = load_json(PROFILE_DIR / "_default.json")
    for path in sorted(PROFILE_DIR.glob("*.json")):
        if path.name == "_default.json":
            continue
        data = load_json(path)
        if subject in data.get("subjects", []):
            profile.update(data)
            break
    else:
        profile["profile"] = "_default"
    return profile


def section_matchers(profile):
    """[(prefix, regex đã biên dịch)] theo thứ tự cấp mục, từ ngoài vào trong."""
    return [(lv["prefix"], re.compile(lv["regex"])) for lv in profile["section_levels"]]


def find_tesseract():
    exe = shutil.which("tesseract")
    if exe:
        return exe
    for cand in (r"C:\Program Files\Tesseract-OCR\tesseract.exe",
                 r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"):
        if Path(cand).exists():
            return cand
    return None


def ocr_cache_path(unit, pdf_name, page):
    """Trang page (đánh số từ 1) của file pdf_name -> cache/ocr/<unit>/<tên pdf>/pNNNN.txt."""
    parse_unit(unit)
    return OCR_CACHE_DIR / unit / Path(pdf_name).stem / f"p{page:04d}.txt"
