#!/usr/bin/env python3
# tools/mkdocs_placeholders.py
import argparse, re, sys
from pathlib import Path
from typing import Dict, List, Tuple
from PIL import Image, ImageDraw, ImageFont

IMG_W, IMG_H = 1600, 900
MARGIN = 48
BG = (245, 247, 250)
FG = (50, 63, 79)
FRAME = (180, 186, 194)
TITLE_SIZE = 48
SUB_SIZE = 28

FIGURE_LINE_RE = re.compile(r'^\s*[-*]?\s*\*\*?Figure\s+(\d+)\s*:\*\*?\s*(.+?)\s*$', re.IGNORECASE)
CAPTION_LINE_RE = re.compile(r'^\s*Figure\s+(\d+)\s*:\s*(.+?)\s*$', re.IGNORECASE)

def slugify(text: str) -> str:
    import re
    out = re.sub(r'[^A-Za-z0-9]+', '-', text).strip('-').lower()
    return out or 'figure'

def load_font(size: int):
    from PIL import ImageFont
    for path in ["arial.ttf",
                 "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                 "/Library/Fonts/Arial.ttf",
                 "C:\\Windows\\Fonts\\arial.ttf"]:
        try:
            return ImageFont.truetype(path, size=size)
        except Exception:
            pass
    return ImageFont.load_default()

def draw_centered(draw, text: str, y: int, font, img_w: int):
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0]
    x = (img_w - w) // 2
    draw.text((x, y), text, fill=FG, font=font)

def make_placeholder(path: Path, fig_no: int, caption: str):
    from PIL import Image, ImageDraw
    title = f"Figure {fig_no}"
    subtitle = caption
    path.parent.mkdir(parents=True, exist_ok=True)
    img = Image.new("RGB", (IMG_W, IMG_H), BG)
    d = ImageDraw.Draw(img)
    d.rectangle([(MARGIN, MARGIN), (IMG_W - MARGIN, IMG_H - MARGIN)], outline=FRAME, width=4)
    title_font = load_font(TITLE_SIZE)
    sub_font = load_font(SUB_SIZE)
    draw_centered(d, title, y=MARGIN + 24, font=title_font, img_w=IMG_W)
    draw_centered(d, subtitle, y=MARGIN + 24 + TITLE_SIZE + 12, font=sub_font, img_w=IMG_W)
    box_w, box_h = IMG_W - 2*MARGIN - 160, IMG_H - 2*MARGIN - 180
    top_left = (MARGIN + 80, MARGIN + 140)
    bottom_right = (top_left[0] + box_w, top_left[1] + box_h)
    d.rectangle([top_left, bottom_right], outline=FRAME, width=3)
    hint = "Placeholder"
    hb = d.textbbox((0,0), hint, font=sub_font)
    d.text((IMG_W - (hb[2]-hb[0]) - MARGIN - 8, IMG_H - (hb[3]-hb[1]) - MARGIN - 8),
           hint, fill=FRAME, font=sub_font)
    img.save(path, format="PNG", optimize=True)

def parse_figures_from_text(md_text: str) -> Dict[int, str]:
    found: Dict[int, str] = {}
    for line in md_text.splitlines():
        m = FIGURE_LINE_RE.match(line) or CAPTION_LINE_RE.match(line)
        if m:
            idx, cap = int(m.group(1)), m.group(2).strip()
            found[idx] = cap
    return found

def ensure_image_links(md_text: str, images_rel: str, fig_map: Dict[int, str]) -> str:
    lines = md_text.splitlines()
    out: List[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        out.append(line)
        m = CAPTION_LINE_RE.match(line) or FIGURE_LINE_RE.match(line)
        if m:
            fig_no = int(m.group(1))
            caption = fig_map.get(fig_no, m.group(2).strip())
            filename = f"fig{fig_no:02d}-{slugify(caption)}.png"
            img_line = f"![Figure {fig_no}: {caption}]({images_rel}/{filename})"
            j = i + 1
            already = False
            import re as _re
            while j < len(lines) and lines[j].strip() == "":
                j += 1
            if j < len(lines) and _re.match(r'!\[.*\]\(.*\)', lines[j].strip()):
                already = True
            if not already:
                out.append("")
                out.append(img_line)
                out.append("")
        i += 1
    return "\n".join(out)

def process_path(target: Path, inject: bool):
    if target.is_dir():
        md_files = sorted(list(target.glob("*.md")))
    else:
        md_files = [target]
    results = []
    for md in md_files:
        text = md.read_text(encoding="utf-8")
        fig_map = parse_figures_from_text(text)
        if not fig_map:
            continue
        images_dir = md.parent / "images"
        images_dir.mkdir(parents=True, exist_ok=True)
        for num in sorted(fig_map.keys()):
            caption = fig_map[num]
            filename = f"fig{num:02d}-{slugify(caption)}.png"
            out_path = images_dir / filename
            if not out_path.exists():
                make_placeholder(out_path, num, caption)
            results.append((num, caption, out_path))
        if inject:
            new_text = ensure_image_links(text, images_rel="images", fig_map=fig_map)
            if new_text != text:
                md.write_text(new_text, encoding="utf-8")
                print(f"Updated image links in {md}")
    return results

def main(argv=None):
    parser = argparse.ArgumentParser(description="Generate figure placeholder images for MkDocs Markdown.")
    parser.add_argument("path", help="Markdown file or docs/ directory to scan", type=str)
    parser.add_argument("--inject", action="store_true", help="Inject image links after 'Figure N:' lines if missing")
    args = parser.parse_args(argv)
    target = Path(args.path)
    if not target.exists():
        print(f"Path not found: {target}", file=sys.stderr); return 2
    results = process_path(target, inject=args.inject)
    if not results:
        print("No figures found. Make sure your captions look like 'Figure 1: Title'."); return 1
    print(f"Generated/verified {len(results)} placeholders:")
    for num, caption, path in results:
        print(f"  - Figure {num}: {caption} -> {path.as_posix()}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
