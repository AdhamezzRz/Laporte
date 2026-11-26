"""Print files: butter-paper (greaseproof) pattern sheets + social card with QR codes.

Outputs (06_Print_Pattern_Card/):
  ALaPorte_ButterPaper_30x40cm.pdf, ALaPorte_ButterPaper_40x50cm.pdf  - one ink (burgundy), no background
  ALaPorte_Social_Card_85x55mm.pdf                                    - p1 front, p2 back (Instagram), p3 back (Instagram + Facebook)
Edit SOCIAL below when the Facebook page exists, then re-run.
"""
import os, re, math, random
import segno
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.lib.colors import CMYKColor, CMYKColorSep
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'logo1_paths.py')).read())   # ICON, WORD
FONTS = os.path.join(HERE, '..', 'fonts')
OUT = os.path.join(HERE, '..', '..', '06_Print_Pattern_Card'); os.makedirs(OUT, exist_ok=True)
pdfmetrics.registerFont(TTFont('Vladimir', os.path.join(FONTS, 'VladimirScript-fixed.ttf')))
pdfmetrics.registerFont(TTFont('CormB', os.path.join(FONTS, 'CormorantGaramond-Bold-fixed.ttf')))
pdfmetrics.registerFont(TTFont('Inter', os.path.join(FONTS, 'Inter-Medium.ttf')))

SOCIAL = {
    'instagram': {'handle': '@a.la.porte', 'url': 'https://www.instagram.com/a.la.porte'},
    'facebook':  {'handle': None, 'url': None},     # e.g. {'handle': 'À La Porte', 'url': 'https://www.facebook.com/alaporte'}
}

BURG = CMYKColor(0.25, 1.00, 0.78, 0.50)
WINE = CMYKColor(0.15, 0.95, 0.60, 0.30)
CREAM = CMYKColor(0.04, 0.09, 0.25, 0.00)
CUT = CMYKColorSep(0, 1, 0, 0, spotName='CutContour', density=1)
LOGO_BOX = {'full': (790, 359, 340, 362), 'icon': (790, 525, 340, 196), 'word': (795, 359, 330, 158)}

def tok(d): return re.findall(r'[MLCZ]|-?\d+(?:\.\d+)?', d)

def svg_path(c, d, X, Y):
    p = c.beginPath(); t = tok(d); i = 0
    while i < len(t):
        k = t[i]; i += 1
        if k == 'M': p.moveTo(X(t[i]), Y(t[i+1])); i += 2
        elif k == 'L': p.lineTo(X(t[i]), Y(t[i+1])); i += 2
        elif k == 'C': p.curveTo(X(t[i]), Y(t[i+1]), X(t[i+2]), Y(t[i+3]), X(t[i+4]), Y(t[i+5])); i += 6
        elif k == 'Z': p.close()
    return p

def logo(c, kind, cx, cy, width, color, rot=0):
    x0, y0, w, h = LOGO_BOX[kind]; s = width / w
    paths = {'full': [ICON] + WORD, 'icon': [ICON], 'word': WORD}[kind]
    c.saveState(); c.translate(cx, cy); c.rotate(rot); c.setFillColor(color)
    for d in paths:
        c.drawPath(svg_path(c, d, lambda x: (float(x) - (x0 + w/2)) * s, lambda y: -(float(y) - (y0 + h/2)) * s), stroke=0, fill=1, fillMode=0)
    c.restoreState()

# hand-drawn doodles (same shapes as the social posts), drawn centred, size = width in points
SPARKLE = 'M 0 -46 C 3 -14 8 -6 46 0 C 9 5 3 13 0 46 C -4 14 -9 5 -46 0 C -8 -5 -3 -13 0 -46 Z'
HEART = 'M 50 84 C 30 66 6 52 6 30 C 6 14 18 5 30 6 C 40 7 47 14 50 24 C 53 13 61 5 72 6 C 85 7 95 17 93 32 C 91 52 68 66 51 85'
def doodle(c, d, cx, cy, size, color, lw, box=(-50, -50, 100, 100), rot=0):
    x0, y0, w, h = box; s = size / w
    c.saveState(); c.translate(cx, cy); c.rotate(rot); c.setStrokeColor(color); c.setLineWidth(lw); c.setLineCap(1); c.setLineJoin(1)
    c.drawPath(svg_path(c, d.replace('M', 'M').replace(' ', ' '), lambda x: (float(x) - (x0 + w/2)) * s, lambda y: -(float(y) - (y0 + h/2)) * s), stroke=1, fill=0)
    c.restoreState()

BASE = {'à': ('a', 'grave'), 'é': ('e', 'acute'), 'À': ('A', 'grave'), 'É': ('E', 'acute')}

def text_acc(c, text, font, size, cx, cy, color, rot=0, centred=True, tracking=0):
    """Draw text, replacing accented letters (missing from the embedded subsets) with base letter + drawn accent."""
    plain = ''.join(BASE.get(ch, (ch,))[0] for ch in text)
    widths = [pdfmetrics.stringWidth(ch, font, size) + tracking for ch in plain]
    total = sum(widths) - tracking
    c.saveState(); c.translate(cx, cy); c.rotate(rot); c.setFillColor(color); c.setStrokeColor(color)
    x = -total / 2 if centred else 0; y = -size * 0.28 if font == 'Vladimir' else 0
    for ch, orig, w in zip(plain, text, widths):
        c.setFont(font, size); c.drawString(x, y, ch)
        if orig in BASE:
            kind = BASE[orig][1]; up = orig.isupper()
            mx = x + (w - tracking) * ((0.86 if kind == 'grave' else 0.62) if font == 'Vladimir' else 0.5)
            top = y + size * (0.86 if up else ((0.5 if kind == 'grave' else 0.58) if font == 'Vladimir' else 0.66))
            dx, dy = size * 0.10, size * 0.13
            c.setLineWidth(size * (0.055 if font == 'Vladimir' else 0.07)); c.setLineCap(1)
            if kind == 'grave': c.line(mx - dx, top + dy, mx + dx * 0.4, top)
            else: c.line(mx - dx * 0.4, top, mx + dx, top + dy)
        x += w
    c.restoreState()

def script(c, text, cx, cy, size, color, rot=0):
    text_acc(c, text, 'Vladimir', size, cx, cy, color, rot)

def dots(c, cx, cy, color, r=0.55 * mm, rot=0):
    c.saveState(); c.translate(cx, cy); c.rotate(rot); c.setFillColor(color)
    for i in range(3): c.circle((i - 1) * 3 * mm, 0, r, stroke=0, fill=1)
    c.restoreState()

# ---------------- butter paper ----------------
def motif(c, k, x, y, rot):
    if k == 0: logo(c, 'icon', x, y, 26 * mm, BURG, rot)
    elif k == 1: script(c, 'à la porte', x, y, 30, BURG, rot)
    elif k == 2:
        doodle(c, SPARKLE, x - 3 * mm, y + 2 * mm, 9 * mm, BURG, 0.9, rot=rot)
        doodle(c, SPARKLE, x + 5 * mm, y - 4 * mm, 4.5 * mm, BURG, 0.8, rot=rot)
    elif k == 3: logo(c, 'full', x, y, 19 * mm, BURG, rot)
    elif k == 4: script(c, 'bon appétit', x, y, 26, BURG, rot)
    elif k == 5:
        doodle(c, HEART, x, y, 7.5 * mm, BURG, 0.9, box=(0, 0, 100, 90), rot=rot)
        dots(c, x, y - 7 * mm, BURG, rot=rot)

def butter_paper(w_cm, h_cm):
    W, H = w_cm * 10 * mm, h_cm * 10 * mm
    path = os.path.join(OUT, f'ALaPorte_ButterPaper_{w_cm}x{h_cm}cm.pdf')
    c = canvas.Canvas(path, pagesize=(W, H))
    c.setTitle(f'À La Porte butter paper {w_cm}×{h_cm} cm'); c.setAuthor('À La Porte')
    c.setSubject('One ink: burgundy (C25 M100 Y78 K50 / or Pantone match). No background: prints on translucent greaseproof paper.')
    rnd = random.Random(7)
    cell = 46 * mm; cols = int(W / cell) + 3; rows = int(H / (cell * 0.72)) + 3
    order = [0, 1, 2, 3, 4, 5]
    for r in range(-1, rows):
        for col in range(-1, cols):
            x = col * cell + (cell / 2 if r % 2 else 0) + rnd.uniform(-4, 4) * mm
            y = r * cell * 0.72 + rnd.uniform(-3, 3) * mm
            k = order[(col + r * 4 + (r // 2)) % len(order)]
            motif(c, k, x, y, rnd.uniform(-16, 16))
    c.showPage(); c.save(); return path

# ---------------- social card ----------------
CW, CH, BL = 85 * mm, 55 * mm, 3 * mm

def ig_icon(c, x, y, s, color):
    c.saveState(); c.setStrokeColor(color); c.setLineWidth(s * 0.09)
    c.roundRect(x, y, s, s, s * 0.28, stroke=1, fill=0); c.circle(x + s/2, y + s/2, s * 0.23, stroke=1, fill=0)
    c.setFillColor(color); c.circle(x + s * 0.77, y + s * 0.77, s * 0.06, stroke=0, fill=1); c.restoreState()

def fb_icon(c, x, y, s, color):
    c.saveState(); c.setStrokeColor(color); c.setLineWidth(s * 0.09); c.roundRect(x, y, s, s, s * 0.28, stroke=1, fill=0)
    c.setFillColor(color); c.setFont('CormB', s * 0.95); c.drawCentredString(x + s * 0.56, y + s * 0.14, 'f'); c.restoreState()

def qr(c, url, x, y, size, color):
    q = segno.make(url, error='m', micro=False)
    m = [list(row) for row in q.matrix]; n = len(m); u = size / n
    c.setFillColor(color)
    for ri, row in enumerate(m):
        ci = 0
        while ci < n:
            if row[ci]:
                start = ci
                while ci < n and row[ci]: ci += 1
                c.rect(x + start * u, y + (n - 1 - ri) * u, (ci - start) * u + 0.02, u + 0.02, stroke=0, fill=1)
            else: ci += 1

def card_page(c, draw):
    c.setTrimBox((BL, BL, BL + CW, BL + CH)); c.setBleedBox((0, 0, CW + 2*BL, CH + 2*BL))
    c.saveState(); c.translate(BL, BL); draw(c); c.restoreState(); c.showPage()

def front(c):
    c.setFillColor(BURG); c.rect(-BL, -BL, CW + 2*BL, CH + 2*BL, stroke=0, fill=1)
    c.setStrokeColor(CREAM); c.setLineWidth(0.5); c.rect(3.2*mm, 3.2*mm, CW - 6.4*mm, CH - 6.4*mm, stroke=1, fill=0)
    logo(c, 'full', CW/2, CH/2 + 0.6*mm, 29 * mm, CREAM)

def back(c, with_fb):
    c.setFillColor(CREAM); c.rect(-BL, -BL, CW + 2*BL, CH + 2*BL, stroke=0, fill=1)
    c.setStrokeColor(BURG); c.setLineWidth(0.5); c.rect(3.2*mm, 3.2*mm, CW - 6.4*mm, CH - 6.4*mm, stroke=1, fill=0)
    nets = [('instagram', ig_icon)] + ([('facebook', fb_icon)] if with_fb else [])
    q = 21 * mm
    if len(nets) == 1:
        # left: words, right: one QR
        script(c, 'Stay in touch', 26*mm, CH - 15.5*mm, 19, BURG)
        text_acc(c, 'À LA PORTE', 'CormB', 7.5, 26*mm, CH - 23*mm, BURG, tracking=1.6)
        doodle(c, HEART, 26*mm, 22*mm, 5*mm, BURG, 0.6, box=(0, 0, 100, 90))
        ig_icon(c, 10.5*mm, 10.5*mm, 3.6*mm, BURG); c.setFillColor(BURG); c.setFont('Inter', 8); c.drawString(15.6*mm, 11.4*mm, SOCIAL['instagram']['handle'])
        qr(c, SOCIAL['instagram']['url'], CW - 9*mm - q, (CH - q)/2 + 2.2*mm, q, BURG)
        c.setFont('Inter', 5.2); c.drawCentredString(CW - 9*mm - q/2, (CH - q)/2 - 2.2*mm, 'SCAN TO FOLLOW')
    else:
        script(c, 'Stay in touch', CW/2, CH - 10.5*mm, 15, BURG)
        for i, (net, icon) in enumerate(nets):
            cx = CW/2 + (i - 0.5) * 33*mm
            info = SOCIAL[net]; qx, qy = cx - q/2, 13.2*mm
            if info['url']: qr(c, info['url'], qx, qy, q, BURG)
            else:
                c.setStrokeColor(BURG); c.setDash(2, 2); c.setLineWidth(0.5); c.rect(qx, qy, q, q, stroke=1, fill=0); c.setDash()
                c.setFillColor(BURG); c.setFont('Inter', 5); c.drawCentredString(cx, qy + q/2 - 1, 'FACEBOOK QR — PENDING')
            label = info['handle'] or 'facebook page'
            c.setFont('Inter', 7); tw = pdfmetrics.stringWidth(label, 'Inter', 7)
            icon(c, cx - (tw + 4.4*mm)/2, 7.4*mm, 3.2*mm, BURG); c.setFillColor(BURG)
            c.drawString(cx - (tw + 4.4*mm)/2 + 4.4*mm, 8.2*mm, label)

def social_card():
    path = os.path.join(OUT, 'ALaPorte_Social_Card_85x55mm.pdf')
    c = canvas.Canvas(path, pagesize=(CW + 2*BL, CH + 2*BL))
    c.setTitle('À La Porte social card 85×55 mm'); c.setAuthor('À La Porte'); c.setSubject('CMYK, 3 mm bleed. p1 front, p2 back (Instagram), p3 back (Instagram + Facebook)')
    card_page(c, front)
    card_page(c, lambda c: back(c, False))
    card_page(c, lambda c: back(c, True))
    c.save(); return path

if __name__ == '__main__':
    for p in (butter_paper(30, 40), butter_paper(40, 50), social_card()): print(os.path.normpath(p))
