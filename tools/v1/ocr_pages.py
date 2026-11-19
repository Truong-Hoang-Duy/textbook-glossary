"""Render trang SGK và OCR tiếng Việt bằng tesseract, ghi cache cache/ocr/<unit>/<pdf>/pNNNN.txt.

    python textbook/scripts/ocr_pages.py <unit> [--file F] [--pages a-b] [--dpi 300] [--jobs 4] [--force] [--psm N]

Trang in xoay ngang (ví dụ sơ đồ tóm tắt cuối chương): chạy lại riêng trang đó với --force --psm 1
để tesseract tự nhận hướng trang.

Mặc định OCR mọi file trong progress.json (hoặc mọi SGK*.pdf của bộ nếu chưa có progress.json)
và bỏ qua trang đã có cache. OCR chỉ để tham khảo và kiểm tra tự động; ảnh trang mới là chuẩn.
"""

import argparse
import os
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor

import pymupdf

from _common import (TESSDATA_DIR, book_dir, find_tesseract, load_profile, load_progress, ocr_cache_path,
                     setup_stdout)


def parse_pages(spec, count):
    if not spec:
        return list(range(1, count + 1))
    a, _, b = spec.partition("-")
    first, last = int(a), int(b or a)
    if not 1 <= first <= last <= count:
        raise SystemExit(f"--pages {spec} nằm ngoài 1-{count}")
    return list(range(first, last + 1))


def run_tesseract(exe, png, lang, psm=None):
    env = dict(os.environ, OMP_THREAD_LIMIT="1")
    proc = subprocess.run(
        [exe, "stdin", "stdout", "-l", lang, "--tessdata-dir", str(TESSDATA_DIR)]
        + (["--psm", str(psm)] if psm is not None else []),
        input=png, capture_output=True, env=env)
    if proc.returncode != 0:
        raise RuntimeError(proc.stderr.decode("utf-8", "replace").strip())
    return proc.stdout.decode("utf-8")


def main():
    setup_stdout()
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("unit")
    ap.add_argument("--file", help="chỉ OCR file này (tên file trong sgk/khoi_<lop>/<unit>/)")
    ap.add_argument("--pages", help="khoảng trang PDF, ví dụ 7-10")
    ap.add_argument("--dpi", type=int, default=300)
    ap.add_argument("--lang", help="mặc định lấy ocr_lang trong hồ sơ môn")
    ap.add_argument("--jobs", type=int, default=max(1, (os.cpu_count() or 2) - 1))
    ap.add_argument("--force", action="store_true", help="OCR lại cả trang đã có cache")
    ap.add_argument("--psm", type=int, help="chế độ phân trang của tesseract; 1 = tự nhận hướng trang")
    a = ap.parse_args()

    a.lang = a.lang or load_profile(a.unit)["ocr_lang"]
    exe = find_tesseract()
    if not exe:
        raise SystemExit("Không tìm thấy tesseract (xem requirements.txt).")

    if a.file:
        files = [a.file]
    else:
        progress = load_progress(a.unit)
        files = ([f["file"] for f in progress["files"]] if progress
                 else sorted(p.name for p in book_dir(a.unit).glob("SGK*.pdf")))
    if not files:
        raise SystemExit(f"Không có file SGK nào trong {book_dir(a.unit)}")

    failed = 0
    for name in files:
        doc = pymupdf.open(book_dir(a.unit) / name)
        pages = parse_pages(a.pages, doc.page_count)
        todo = [p for p in pages if a.force or not ocr_cache_path(a.unit, name, p).exists()]
        print(f"{name}: {len(pages)} trang, cần OCR {len(todo)}, đã có cache {len(pages) - len(todo)}")
        start = time.time()

        def work(page, png):
            text = run_tesseract(exe, png, a.lang, a.psm)
            out = ocr_cache_path(a.unit, name, page)
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(text, encoding="utf-8", newline="\n")
            return page, len(text)

        # PyMuPDF không an toàn với nhiều luồng: render tuần tự ở luồng chính, chỉ tesseract chạy song song.
        with ThreadPoolExecutor(max_workers=a.jobs) as pool:
            futures = []
            for page in todo:
                pix = doc[page - 1].get_pixmap(dpi=a.dpi, colorspace=pymupdf.csGRAY)
                futures.append(pool.submit(work, page, pix.tobytes("png")))
                while sum(not f.done() for f in futures) > a.jobs * 2:
                    time.sleep(0.05)
            for i, fut in enumerate(futures, 1):
                try:
                    page, n = fut.result()
                    if n == 0:
                        print(f"  cảnh báo: trang {page} không có chữ")
                except Exception as e:  # noqa: BLE001 - báo lỗi từng trang, chạy tiếp
                    failed += 1
                    print(f"  lỗi: {e}")
                if i % 20 == 0 or i == len(futures):
                    print(f"  {i}/{len(futures)} trang, {time.time() - start:.0f}s")
        doc.close()

    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
