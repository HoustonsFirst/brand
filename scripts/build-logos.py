#!/usr/bin/env python3
"""Build web-ready logo files in assets/logos/ from the Creative Team's SVG exports.

    python3 scripts/build-logos.py SOURCE_DIR           # write cleaned SVGs and PNGs
    python3 scripts/build-logos.py SOURCE_DIR --svg-only

SOURCE_DIR holds Illustrator exports named lo-{scope}-{horizontal|vertical}-lockup-{black|white}.svg
or lo-houstonsfirst-mark-{black|white}.svg, where scope is houstonsfirst or {campus}-campus.

For each file this:
  - renames it to the repo convention (houstonsfirst[-campus]-{primary|stacked|mark}-{variant})
  - strips editor metadata, IDs, classes, and per-shape styles; sets one fill on <svg>
  - adds role="img" and a <title> so the logo has an accessible name when inlined
  - rounds coordinates to 3 decimals
  - renders transparent PNGs at @1x and @2x with headless Google Chrome
"""
import pathlib, re, subprocess, sys, tempfile

root = pathlib.Path(__file__).resolve().parent.parent
out_root = root / "assets" / "logos"
chrome = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CHURCH = "Houston's First Baptist Church"
CAMPUSES = {  # source slug -> (repo slug, approved name from writing-style-guide.md)
    "the-loop": ("loop", "The Loop Campus"),
    "cypress": ("cypress", "Cypress Campus"),
    "downtown": ("downtown", "Downtown Campus"),
    "sienna": ("sienna", "Sienna Campus"),
}
LOCKUPS = {"horizontal-lockup": "primary", "vertical-lockup": "stacked", "mark": "mark"}
PNG_HEIGHT = {"primary": 150, "stacked": 300, "mark": 300}  # @1x, in px
FILLS = {"black": "#000", "white": "#fff"}

PRECISION = 3  # 2 drifts visibly: rounding error accumulates along relative path commands
NUM = re.compile(r"-?(?:\d+\.?\d*|\.\d+)(?:[eE][-+]?\d+)?")


def fmt(n):
    s = f"{round(float(n), PRECISION):.{PRECISION}f}".rstrip("0").rstrip(".")
    s = s.replace("-0.", "-.") if s.startswith("-0.") else (s[1:] if s.startswith("0.") else s)
    return "0" if s in ("", "-0", "-") else s


def clean_path(d):
    """Round every number and rejoin with the fewest separators that stay unambiguous."""
    out, prev = [], None
    for tok in re.findall(r"[A-Za-z]|" + NUM.pattern, d):
        if tok.isalpha():
            out.append(tok)
            prev = None
            continue
        n = fmt(tok)
        if prev is not None and not (n.startswith("-") or (n.startswith(".") and "." in prev)):
            out.append(" ")
        out.append(n)
        prev = n
    return "".join(out)


def parse_name(stem):
    m = re.fullmatch(r"lo-(houstonsfirst|[a-z-]+?-campus)-(horizontal-lockup|vertical-lockup|mark)-(black|white)", stem)
    if not m:
        return None
    scope, lockup, variant = m.groups()
    if scope == "houstonsfirst":
        folder, name, title = "campuswide", "houstonsfirst", CHURCH
    else:
        slug, label = CAMPUSES[scope.removesuffix("-campus")]
        folder, name, title = f"{slug}-campus", f"houstonsfirst-{slug}", f"{label} of {CHURCH}"
    return folder, f"{name}-{LOCKUPS[lockup]}-{variant}", LOCKUPS[lockup], variant, title


def clean_svg(src, variant, title):
    s = src.read_text()
    vb = [fmt(v) for v in re.search(r'viewBox="([^"]+)"', s).group(1).split()]
    shapes = []
    for tag, attrs in re.findall(r"<(path|rect)\b([^>]*)/?>", s):
        if tag == "path":
            shapes.append(f'<path d="{clean_path(re.search(r"\sd=\"([^\"]+)\"", attrs).group(1))}"/>')
        else:
            a = dict(re.findall(r'\s(x|y|width|height)="([^"]+)"', attrs))
            shapes.append('<rect ' + " ".join(f'{k}="{fmt(a[k])}"' for k in ("x", "y", "width", "height") if k in a) + "/>")
    title = title.replace("'", "’")
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{" ".join(vb)}" role="img" fill="{FILLS[variant]}">'
            f"<title>{title}</title>{''.join(shapes)}</svg>\n"), float(vb[2]) / float(vb[3])


def render_png(svg_path, png_path, height, ratio):
    from PIL import Image
    w, h = round(height * ratio), height
    with tempfile.TemporaryDirectory() as tmp:
        page = pathlib.Path(tmp) / "r.html"
        page.write_text(f'<!doctype html><style>html,body{{margin:0;background:transparent}}'
                        f'img{{display:block;width:{w}px;height:{h}px}}</style><img src="{svg_path.as_uri()}">')
        shot = pathlib.Path(tmp) / "r.png"
        subprocess.run([chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                        "--default-background-color=00000000", "--allow-file-access-from-files",
                        f"--window-size={max(w, 800)},{max(h, 600)}", f"--screenshot={shot}", page.as_uri()],
                       check=True, capture_output=True)
        Image.open(shot).crop((0, 0, w, h)).save(png_path, optimize=True)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    if len(args) != 1:
        sys.exit(__doc__)
    sources = sorted(pathlib.Path(args[0]).expanduser().rglob("*.svg"))
    for src in sources:
        parsed = parse_name(src.stem)
        if not parsed:
            print(f"skip (unrecognized name): {src.name}")
            continue
        folder, name, lockup, variant, title = parsed
        dest = out_root / folder
        (dest / "png").mkdir(parents=True, exist_ok=True)
        svg, ratio = clean_svg(src, variant, title)
        svg_path = dest / f"{name}.svg"
        svg_path.write_text(svg)
        line = f"{src.stat().st_size:>6} -> {len(svg.encode()):>6}  {folder}/{name}.svg"
        if "--svg-only" not in sys.argv:
            for scale, suffix in ((1, ""), (2, "@2x")):
                render_png(svg_path, dest / "png" / f"{name}{suffix}.png", PNG_HEIGHT[lockup] * scale, ratio)
            line += " + png @1x/@2x"
        print(line)


if __name__ == "__main__":
    main()
