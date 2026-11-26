"""Social card — concept A 'Served' (chosen). Print-ready: 55 x 85 mm portrait, CMYK, 3 mm bleed.
p1 front (burgundy, logo) · p2 back (cream, the logo's hand serves the QR code on its tray)."""
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
import print_extras as P

QR_URL = 'https://kliktick.com/a-la-porte'      # client's link page (Instagram, Facebook, ...)
HANDLE = '@a.la.porte'
W, H, BL = 55 * mm, 85 * mm, 3 * mm
OUT = os.path.join(P.OUT, 'ALaPorte_Social_Card_Served_55x85mm.pdf')

def front(c):
    c.setFillColor(P.BURG); c.rect(-BL, -BL, W + 2*BL, H + 2*BL, stroke=0, fill=1)
    P.logo(c, 'full', W/2, H/2 + 6*mm, 33*mm, P.CREAM)
    c.setFillColor(P.CREAM); c.setFont('Inter', 6.3)
    txt = 'PLATTERS  ·  TRAYS  ·  GIFTS'
    tw = sum(pdfmetrics.stringWidth(ch, 'Inter', 6.3) + 2.2 for ch in txt) - 2.2
    x = W/2 - tw/2
    for ch in txt:
        c.drawString(x, 9*mm, ch); x += pdfmetrics.stringWidth(ch, 'Inter', 6.3) + 2.2

def back(c):
    c.setFillColor(P.CREAM); c.rect(-BL, -BL, W + 2*BL, H + 2*BL, stroke=0, fill=1)
    # headline
    P.script(c, 'Served fresh', W/2, H - 13.5*mm, 27, P.BURG)
    P.text_acc(c, 'ON OUR SOCIALS', 'CormB', 8.6, W/2, H - 22.5*mm, P.BURG, tracking=2.6)
    # the hand serves the QR code: tray surface at tray_y
    iw = 43 * mm; x0, y0, w, h = P.LOGO_BOX['icon']; s = iw / w
    tray_y = 35.5 * mm
    cy = tray_y - (h/2 - (530.5 - y0)) * s            # icon centre so its tray top lands on tray_y
    P.logo(c, 'icon', W/2, cy, iw, P.BURG)
    q = 19 * mm
    P.qr(c, QR_URL, W/2 - q/2, tray_y + 1.0*mm, q, P.BURG)
    # handle line with icons
    c.setFillColor(P.BURG); c.setFont('Inter', 7.6)
    tw = pdfmetrics.stringWidth(HANDLE, 'Inter', 7.6); ic = 3.3*mm; gap = 1.3*mm
    total = ic*2 + gap + 2*mm + tw; x = W/2 - total/2; y = 6.6*mm
    P.ig_icon(c, x, y, ic, P.BURG); P.fb_icon(c, x + ic + gap, y, ic, P.BURG)
    c.setFillColor(P.BURG); c.drawString(x + ic*2 + gap + 2*mm, y + 0.85*mm, HANDLE)

def page(c, draw):
    c.setTrimBox((BL, BL, BL + W, BL + H)); c.setBleedBox((0, 0, W + 2*BL, H + 2*BL))
    c.saveState(); c.translate(BL, BL); draw(c); c.restoreState(); c.showPage()

if __name__ == '__main__':
    c = canvas.Canvas(OUT, pagesize=(W + 2*BL, H + 2*BL))
    c.setTitle('À La Porte social card — Served (55×85 mm)'); c.setAuthor('À La Porte')
    c.setSubject('CMYK, 3 mm bleed, TrimBox 55×85 mm. Page 1 front, page 2 back. QR → ' + QR_URL)
    page(c, front); page(c, back); c.save()
    print(os.path.normpath(OUT))
