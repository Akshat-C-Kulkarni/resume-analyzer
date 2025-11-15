# src/extraction.py
import pdfplumber
import re
from pathlib import Path

def clean_text(text: str) -> str:
    """Basic cleanup of extracted text."""
    if not text:
        return ""
    text = text.replace("\r", "\n")
    text = re.sub(r"\n\s*\n+", "\n\n", text)      # collapse multiple blank lines
    text = re.sub(r"[ \t]+", " ", text)          # reduce extra spaces
    text = text.strip()
    text = text.lower()
    return text

def extract_page_whole(page):
    """Extract text normally from a full page."""
    return page.extract_text() or ""

def extract_page_columns(page):
    """Try extracting as two vertical columns (heuristic)."""
    w = page.width
    mid = w / 2

    left = page.within_bbox((0, 0, mid, page.height)).extract_text() or ""
    right = page.within_bbox((mid, 0, w, page.height)).extract_text() or ""

    return left + "\n" + right

def extract_text_from_pdf(path: str, try_columns=True) -> str:
    """Extract text from a PDF, handling both single and multi-column resumes."""
    path = Path(path)
    if not path.exists():
        raise FileNotFoundError(path)

    all_pages = []

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            whole = extract_page_whole(page).strip()

            if try_columns:
                cols = extract_page_columns(page).strip()
                chosen = cols if len(cols) > len(whole) else whole
            else:
                chosen = whole

            all_pages.append(chosen)

    full_text = "\n\n".join(p for p in all_pages if p)
    return clean_text(full_text)

def save_text(text: str, out_path: str):
    out_path = Path(out_path)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Extract text from PDF resumes.")
    parser.add_argument("inputs", nargs="+", help="PDF files to extract")
    parser.add_argument("--outdir", default="data/extracted", help="Output folder for .txt")

    args = parser.parse_args()

    outdir = Path(args.outdir)
    outdir.mkdir(parents=True, exist_ok=True)

    for file in args.inputs:
        try:
            text = extract_text_from_pdf(file)
            out_file = outdir / (Path(file).stem + ".txt")
            save_text(text, out_file)
            print(f"[OK] {file} → {out_file} ({len(text)} chars)")
        except Exception as e:
            print(f"[ERROR] {file}: {e}")
