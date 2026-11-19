"""Cắt hình minh họa từ ảnh trang theo figures.json, ghi img/<mã hình>.png (spec mục 4.4).

    python textbook/scripts/crop_figures.py <unit> <thư mục nhóm> [--only MÃ ...] [--dpi 300]
    python textbook/scripts/crop_figures.py <unit> --grid TRANG [TRANG ...]

<thư mục nhóm> tính từ thư mục bộ, ví dụ Phan-04-Di-truyen-hoc/Chuong-01-Di-truyen-phan-tu.
figures.json: { "<mã hình>": {"pdf_page": N, "bbox": [x0, y0, x1, y1]} }, đơn vị point của PDF.
Khoá tuỳ chọn "rotate": 90 | 180 | 270 xoay ảnh cắt theo chiều kim đồng hồ (trang in xoay ngang).
Khoá tuỳ chọn "allow_edge_ink": true kèm "edge_ink_note": "<lý do>" (bắt buộc): chấp nhận cạnh khung cắt qua nét vẽ,
chỉ in cảnh báo. Chỉ dùng khi không có khung chữ nhật nào vừa đủ hình mà không dính chữ đoạn văn bên cạnh.

Quy trình:
  1. --grid: vẽ lưới 10 pt lên trang (100 dpi) ở cache/figures/<unit>/grid_pNNN.png để đo bbox.
  2. Cắt: khung = bbox + lề PAD pt. Mỗi cạnh khung phải nằm trên nền trắng; cạnh nào cắt ngang nét vẽ
     (hình bị cắt mất, hoặc dính chữ bên cạnh) thì báo lỗi, phải sửa bbox rồi chạy lại.
  3. Xem ảnh kiểm tra cache/figures/<unit>/<mã>.png: toàn trang, khung cắt màu đỏ. Khung phải gồm đủ mọi
     nhãn, mũi tên, chú giải (a)/(b) VÀ chú thích "Hình x.y. …" (bảng: tiêu đề "Bảng x.y. …" phía trên và khối
     "Chú thích:" phía dưới); không gồm đoạn văn bên cạnh và chú thích chân trang "(*) Nguồn hình".
"""

import argparse
import re
import sys
from pathlib import Path

import numpy as np
import pymupdf

from _common import ROOT, book_dir, iter_nodes, load_json, load_progress, parse_unit, setup_stdout, unit_dir

PAD = 4          # lề quanh bbox (pt)
EDGE_INK = 0     # số điểm có nét tối đa cho phép trên một cạnh khung (chữ mảnh chỉ để lại 1–3 điểm)


def lesson_of(fig_id, unit):
    """'H12-sinh-b01-03' -> 'b01'."""
    subject, grade = parse_unit(unit)
    m = re.fullmatch(rf"H{grade}-{re.escape(subject)}-(.+)-(\d{{2}})", fig_id)
    if not m:
        raise SystemExit(f"Mã hình sai dạng H{grade}-{subject}-<id bài>-<stt>: {fig_id}")
    return m.group(1)


def ink_mask(page):
    """Mặt nạ 1 px = 1 pt: True ở điểm có nét (đậm hoặc có màu); bỏ nền trắng và chữ chìm nhạt."""
    pix = page.get_pixmap(dpi=72, colorspace=pymupdf.csRGB, alpha=False)
    a = np.frombuffer(pix.samples, dtype=np.uint8).reshape(pix.height, pix.width, 3).astype(int)
    darkness = 255 - a.min(axis=2)
    saturation = a.max(axis=2) - a.min(axis=2)
    return (darkness > 60) | (saturation > 50)


def edges_on_ink(mask, box):
    """Các cạnh của khung đi qua nét vẽ."""
    h, w = mask.shape
    x0, y0, x1, y1 = (int(round(v)) for v in box)
    x1, y1 = min(x1, w - 1), min(y1, h - 1)
    lines = {"trái": mask[y0:y1, x0], "phải": mask[y0:y1, x1], "trên": mask[y0, x0:x1], "dưới": mask[y1, x0:x1]}
    return [f"{k} ({int(v.sum())} điểm)" for k, v in lines.items() if v.sum() > EDGE_INK]


def render_grid(page, out):
    page = page.parent.load_page(page.number)  # bản riêng để không vẽ đè lên trang dùng cho cắt
    w, h = page.rect.width, page.rect.height
    sh = page.new_shape()
    for x in range(0, int(w) + 1, 10):
        sh.draw_line((x, 0), (x, h))
        sh.finish(color=(1, 0, 0) if x % 100 == 0 else (1, .55, .55) if x % 50 == 0 else (1, .85, .85),
                  width=.6 if x % 50 == 0 else .25)
    for y in range(0, int(h) + 1, 10):
        sh.draw_line((0, y), (w, y))
        sh.finish(color=(0, 0, 1) if y % 100 == 0 else (.55, .55, 1) if y % 50 == 0 else (.85, .85, 1),
                  width=.6 if y % 50 == 0 else .25)
    sh.commit()
    for x in range(50, int(w), 50):
        page.insert_text((x + 1, 7), str(x), fontsize=6, color=(1, 0, 0))
        page.insert_text((x + 1, h - 2), str(x), fontsize=6, color=(1, 0, 0))
    for y in range(50, int(h), 50):
        page.insert_text((1, y - 1), str(y), fontsize=6, color=(0, 0, 1))
        page.insert_text((w - 16, y - 1), str(y), fontsize=6, color=(0, 0, 1))
    out.parent.mkdir(parents=True, exist_ok=True)
    page.get_pixmap(dpi=100).save(out)


def save_check(page, box, out):
    """Ảnh kiểm tra: toàn trang, khung cắt màu đỏ."""
    pix = page.get_pixmap(dpi=100, colorspace=pymupdf.csRGB, alpha=False)
    doc = pymupdf.open()
    p = doc.new_page(width=page.rect.width, height=page.rect.height)
    p.insert_image(p.rect, pixmap=pix)
    p.draw_rect(pymupdf.Rect(box), color=(1, 0, 0), width=1)
    out.parent.mkdir(parents=True, exist_ok=True)
    p.get_pixmap(dpi=100).save(out)


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("unit")
    ap.add_argument("group_dir", nargs="?")
    ap.add_argument("--only", nargs="+", metavar="MÃ")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--grid", nargs="+", type=int, metavar="TRANG", help="chỉ vẽ lưới đo bbox cho các trang PDF này")
    ap.add_argument("--file", help="file PDF cho --grid khi SGK có nhiều tập")
    a = ap.parse_args()

    progress = load_progress(a.unit)
    check_dir = ROOT / "cache" / "figures" / a.unit
    if a.grid:
        names = [f["file"] for f in progress["files"]]
        if a.file is None and len(names) > 1:
            ap.error(f"SGK có {len(names)} tập, cần --file (một trong: {names})")
        name = a.file or names[0]
        doc = pymupdf.open(book_dir(a.unit) / name)
        for p in a.grid:
            out = check_dir / (f"grid_p{p:03d}.png" if len(names) == 1 else f"grid_{Path(name).stem}_p{p:03d}.png")
            render_grid(doc[p - 1], out)
            print(out.relative_to(ROOT))
        return
    if not a.group_dir:
        ap.error("cần <thư mục nhóm> hoặc --grid")

    folder = unit_dir(a.unit) / a.group_dir
    figures = load_json(folder / "figures.json")
    sources = {n["id"]: n["source_file"] for n, _ in iter_nodes(progress["toc"]) if "source_file" in n}
    docs, masks, errors = {}, {}, 0
    (folder / "img").mkdir(exist_ok=True)

    for fig_id, spec in figures.items():
        if a.only and fig_id not in a.only:
            continue
        lesson = lesson_of(fig_id, a.unit)
        if lesson not in sources:
            print(f"lỗi: {fig_id}: không có bài '{lesson}' trong progress.json")
            errors += 1
            continue
        name = sources[lesson]
        doc = docs.setdefault(name, pymupdf.open(book_dir(a.unit) / name))
        page = doc[spec["pdf_page"] - 1]
        x0, y0, x1, y1 = spec["bbox"]
        box = pymupdf.Rect(x0 - PAD, y0 - PAD, x1 + PAD, y1 + PAD) & page.rect
        if not pymupdf.Rect(spec["bbox"]).is_valid or not page.rect.contains(pymupdf.Rect(spec["bbox"])):
            print(f"lỗi: {fig_id}: bbox {spec['bbox']} nằm ngoài trang {page.rect}")
            errors += 1
            continue
        key = (name, spec["pdf_page"])
        if key not in masks:
            masks[key] = ink_mask(page)
        bad = edges_on_ink(masks[key], box)
        mat = pymupdf.Matrix(a.dpi / 72, a.dpi / 72).prerotate(spec.get("rotate", 0))
        pix = page.get_pixmap(matrix=mat, clip=box)
        pix.save(folder / "img" / f"{fig_id}.png")
        save_check(page, box, check_dir / f"{fig_id}.png")
        if bad and spec.get("allow_edge_ink"):
            if not str(spec.get("edge_ink_note", "")).strip():
                errors += 1
                print(f"lỗi: {fig_id}: có allow_edge_ink nhưng thiếu edge_ink_note (ghi lý do)")
            else:
                print(f"cảnh báo: {fig_id}: trang {spec['pdf_page']}, cạnh khung cắt qua nét vẽ: {', '.join(bad)}"
                      f" — chấp nhận theo allow_edge_ink: {spec['edge_ink_note']}")
        elif bad:
            errors += 1
            print(f"lỗi: {fig_id}: trang {spec['pdf_page']}, cạnh khung cắt qua nét vẽ: {', '.join(bad)} — sửa bbox")
        else:
            print(f"{fig_id}: trang {spec['pdf_page']}, {pix.width}x{pix.height} px")

    print(f"Ảnh kiểm tra (phải xem trước khi coi là đạt): {check_dir.relative_to(ROOT)}")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
