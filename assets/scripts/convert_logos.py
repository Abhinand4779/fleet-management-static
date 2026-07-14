from pathlib import Path
import fitz

root = Path(__file__).resolve().parent.parent / 'images' / 'logo'
root.mkdir(parents=True, exist_ok=True)

files = [
    ('LBT icon.pdf', 'lbt-icon.png'),
    ('LBT LOGO_h.pdf', 'lbt-logo-wordmark.png'),
]

for src_name, out_name in files:
    src = root / src_name
    out = root / out_name
    if not src.exists():
        print(f'Skipping missing file: {src}')
        continue
    doc = fitz.open(src)
    page = doc.load_page(0)
    pix = page.get_pixmap(matrix=fitz.Matrix(3, 3), alpha=True)
    pix.save(out)
    doc.close()
    print(f'Created {out}')
