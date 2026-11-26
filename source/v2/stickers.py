"""Print-ready round stickers (4 cm and 6 cm), vector, CMYK, 3 mm bleed, CutContour die line.

Outputs (05_Stickers_Print/):
  ALaPorte_Sticker_40mm_Round.pdf   - 2 pages (burgundy, cream), one sticker per page with bleed
  ALaPorte_Sticker_60mm_Round.pdf   - same at 60 mm
  ALaPorte_Sticker_Sheets_A4.pdf    - A4 gang sheets (4 pages) with cut lines, for digital print & cut
"""
import os, re
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import CMYKColor, CMYKColorSep
from reportlab.lib.pagesizes import A4

HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'logo1_paths.py')).read())          # ICON, WORD (identity PDF outlines)
OUT = os.path.join(HERE, '..', '..', '05_Stickers_Print'); os.makedirs(OUT, exist_ok=True)

# Brand colours as print CMYK (from #550b18 burgundy and #f2e5c5 cream). Proof before the full run.
BURG = CMYKColor(0.25, 1.00, 0.78, 0.50)
CREAM = CMYKColor(0.04, 0.09, 0.25, 0.00)
CUT = CMYKColorSep(0, 1, 0, 0, spotName='CutContour', density=1)

LOGO_BOX = (790, 359, 340, 362)          # logo viewBox in source units (x, y, w, h)
DESIGNS = {'Burgundy': (BURG, CREAM), 'Cream': (CREAM, BURG)}
BLEED = 3 * mm

def tokens(d):
    return re.findall(r'[MLCZ]|-?\d+(?:\.\d+)?', d)

def draw_logo(c, cx, cy, width, color):
    """Draw the outlined logo centred at (cx, cy), flipping SVG y-down into PDF y-up."""
    x0, y0, w, h = LOGO_BOX
    s = width / w
    X = lambda x: cx + (float(x) - (x0 + w / 2)) * s
    Y = lambda y: cy - (float(y) - (y0 + h / 2)) * s
    c.setFillColor(color)
    for d in [ICON] + WORD:
        p = c.beginPath(); t = tokens(d); i = 0
        while i < len(t):
            k = t[i]; i += 1
            if k == 'M': p.moveTo(X(t[i]), Y(t[i+1])); i += 2
            elif k == 'L': p.lineTo(X(t[i]), Y(t[i+1])); i += 2
            elif k == 'C':
                p.curveTo(X(t[i]), Y(t[i+1]), X(t[i+2]), Y(t[i+3]), X(t[i+4]), Y(t[i+5])); i += 6
            elif k == 'Z': p.close()
        c.drawPath(p, stroke=0, fill=1, fillMode=0)   # non-zero winding, as in the source artwork

def sticker(c, cx, cy, d, design, with_bleed=True):
    bg, fg = DESIGNS[design]
    r = d / 2
    c.setFillColor(bg)
    c.circle(cx, cy, r + (BLEED if with_bleed else 0), stroke=0, fill=1)
    # thin keyline inside the edge (sits 2.6 mm in, clear of cutting tolerance)
    c.setStrokeColor(fg); c.setLineWidth(0.5)
    c.circle(cx, cy, r - 2.6 * mm, stroke=1, fill=0)
    # logo: optically centred (nudged up 1.5%)
    draw_logo(c, cx, cy + d * 0.015, d * 0.54, fg)

def cut_line(c, cx, cy, d):
    c.saveState()
    c.setStrokeColor(CUT); c.setLineWidth(0.25)
    try: c.setStrokeOverprint(True)
    except Exception: pass
    c.circle(cx, cy, d / 2, stroke=1, fill=0)
    c.restoreState()

def single(d_mm):
    d = d_mm * mm; side = d + 2 * BLEED
    path = os.path.join(OUT, f'ALaPorte_Sticker_{d_mm}mm_Round.pdf')
    c = canvas.Canvas(path, pagesize=(side, side))
    c.setTitle(f'À La Porte sticker {d_mm} mm round'); c.setAuthor('À La Porte'); c.setSubject('Print-ready: CMYK, 3 mm bleed, CutContour die line')
    for design in DESIGNS:
        c.setTrimBox((BLEED, BLEED, BLEED + d, BLEED + d))
        c.setBleedBox((0, 0, side, side))
        sticker(c, side / 2, side / 2, d, design)
        cut_line(c, side / 2, side / 2, d)
        c.showPage()
    c.save(); return path

def sheets():
    path = os.path.join(OUT, 'ALaPorte_Sticker_Sheets_A4.pdf')
    c = canvas.Canvas(path, pagesize=A4)
    c.setTitle('À La Porte sticker sheets A4'); c.setAuthor('À La Porte')
    W, H = A4
    for d_mm, gap_mm in ((40, 6), (60, 6)):
        d = d_mm * mm; pitch = d + gap_mm * mm
        cols = int((W - 10 * mm + gap_mm * mm) // pitch); rows = int((H - 22 * mm + gap_mm * mm) // pitch)
        gw, gh = cols * pitch - gap_mm * mm, rows * pitch - gap_mm * mm
        ox, oy = (W - gw) / 2, (H - gh) / 2 - 4 * mm
        for design in DESIGNS:
            for rI in range(rows):
                for cI in range(cols):
                    cx = ox + cI * pitch + d / 2; cy = oy + rI * pitch + d / 2
                    c.saveState(); p = c.beginPath(); p.circle(cx, cy, d / 2 + BLEED * 0.9); c.clipPath(p, stroke=0)
                    sticker(c, cx, cy, d, design); c.restoreState()
                    cut_line(c, cx, cy, d)
            c.setFillColor(CMYKColor(0, 0, 0, 0.6)); c.setFont('Helvetica', 7)
            c.drawString(10 * mm, H - 8 * mm, f'A LA PORTE  |  round sticker {d_mm} mm  |  {design}  |  {rows * cols} per sheet  |  magenta circle = CutContour (do not print)')
            c.showPage()
    c.save(); return path

if __name__ == '__main__':
    for p in (single(40), single(60), sheets()):
        print(p)
