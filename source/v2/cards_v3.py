"""Social card — three design concepts (presentation renders). 1 mm = 12 px.
Facebook QR is shown as a ghosted placeholder until the page exists."""
import segno, re
from brand2 import *

MM = 12
IG_URL, IG = 'https://www.instagram.com/a.la.porte', '@a.la.porte'
FB_NAME = 'À La Porte'

def qr_svg(url, size, color, ghost=False):
    q = segno.make(url, error='m'); m = [list(r) for r in q.matrix]; n = len(m); u = size / n
    rects = ''.join(f'<rect x="{c*u:.2f}" y="{r*u:.2f}" width="{u+.3:.2f}" height="{u+.3:.2f}"/>' for r, row in enumerate(m) for c, v in enumerate(row) if v)
    op = ';opacity:.16' if ghost else ''
    return f'<svg width="{size}" height="{size}" style="display:block{op}"><g fill="{color}">{rects}</g></svg>'

def ig_icon(s, col):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" style="vertical-align:middle"><rect x="2" y="2" width="20" height="20" rx="6" fill="none" stroke="{col}" stroke-width="2"/>'
            f'<circle cx="12" cy="12" r="4.6" fill="none" stroke="{col}" stroke-width="2"/><circle cx="17.6" cy="6.4" r="1.3" fill="{col}"/></svg>')
def fb_icon(s, col):
    return (f'<svg width="{s}" height="{s}" viewBox="0 0 24 24" style="vertical-align:middle"><rect x="2" y="2" width="20" height="20" rx="6" fill="none" stroke="{col}" stroke-width="2"/>'
            f'<path d="M13.4 19 V12.6 H15.6 L16 10 H13.4 V8.5 C13.4 7.7 13.7 7.2 14.8 7.2 H16.1 V4.9 C15.6 4.8 14.9 4.7 14.1 4.7 C12.1 4.7 10.8 5.9 10.8 8.1 V10 H8.6 V12.6 H10.8 V19 Z" fill="{col}"/></svg>')

def face(w, h, bg, inner, id_, extra=''):
    return f'<div class="face" id="{id_}" style="width:{w*MM}px;height:{h*MM}px;background:{bg};{extra}">{inner}{GRAIN}</div>'

# ---------- A · Served (portrait 55 x 85) ----------
def A_front():
    W, H = 55, 85
    return face(W, H, BU, f'''
      <div class="abs center" style="left:0;right:0;top:{20*MM}px">{logo('full', CR, width=34*MM)}</div>
      <div class="abs sans center" style="left:0;right:0;bottom:{9*MM}px;color:{CR};font-size:{2.1*MM}px;letter-spacing:.42em">Platters · Trays · Gifts</div>''', 'A_front')

def A_back():
    W, H = 55, 85; iw = 50 * MM; ix, iy, iwv, ihv = VB['icon']; k = iw / iwv
    tray_y = 47 * MM                                   # where the tray surface sits
    icon_top = tray_y - (530.5 - iy) * k
    q = 15 * MM
    return face(W, H, CR, f'''
      <div class="abs" style="left:0;right:0;top:{8*MM}px;text-align:center;color:{BU}">
        <div class="script" style="font-size:{9*MM}px">Served fresh</div>
        <div class="cb" style="font-size:{3.2*MM}px;letter-spacing:.3em;margin-top:{1*MM}px">ON OUR SOCIALS</div></div>
      <div class="abs" style="left:{(W*MM-iw)/2}px;top:{icon_top}px">{logo('icon', BU, width=iw)}</div>
      <div class="abs" style="left:{8.5*MM}px;top:{tray_y - q - 0.6*MM}px">{qr_svg(IG_URL, q, BU)}</div>
      <div class="abs" style="left:{W*MM - 8.5*MM - q}px;top:{tray_y - q - 0.6*MM}px">{qr_svg('https://www.facebook.com/', q, BU, ghost=True)}</div>
      <div class="abs" style="left:{6*MM}px;right:{6*MM}px;bottom:{7*MM}px;display:flex;justify-content:space-between;color:{BU};font-family:Inter;font-weight:500;font-size:{2.5*MM}px">
        <span>{ig_icon(3.4*MM, BU)}&nbsp;{IG}</span><span>{fb_icon(3.4*MM, BU)}&nbsp;{FB_NAME}</span></div>''', 'A_back')

# ---------- B · Le Bistro (landscape 85 x 55) ----------
def B_front():
    W, H = 85, 55
    tile = ''.join(f'<div class="abs" style="left:{(i%7)*13*MM + (6*MM if (i//7)%2 else 0) - 4*MM}px;top:{(i//7)*11*MM - 3*MM}px;transform:rotate({[-12,8,-4,14,-9,5][i%6]}deg)">{logo("icon", WI, width=9*MM)}</div>' for i in range(42))
    return face(W, H, BU, f'''{tile}
      <div class="abs center" style="left:{(W/2-21)*MM}px;top:{(H/2-17)*MM}px;width:{42*MM}px;height:{34*MM}px;background:{BU};border-radius:50%;box-shadow:0 0 0 {0.5*MM}px {BU}, 0 0 0 {0.8*MM}px {CR}">
        {logo('full', CR, width=21*MM)}</div>''', 'B_front')

def B_back():
    W, H = 85, 55; q = 14 * MM
    lead = lambda a, b, icon: (f'<div style="display:flex;align-items:baseline;gap:{1.4*MM}px;margin-top:{2.6*MM}px">{icon}'
                               f'<span class="cb" style="font-size:{3.6*MM}px;letter-spacing:.06em">{a}</span>'
                               f'<span style="flex:1;border-bottom:{0.35*MM}px dotted {BU};transform:translateY(-{0.8*MM}px)"></span>'
                               f'<span style="font-family:Inter;font-weight:500;font-size:{2.6*MM}px">{b}</span></div>')
    return face(W, H, CR, f'''
      <div class="abs" style="left:{3*MM}px;top:{3*MM}px;right:{3*MM}px;bottom:{3*MM}px;border:{0.3*MM}px solid {BU}"></div>
      <div class="abs" style="left:{4.2*MM}px;top:{4.2*MM}px;right:{4.2*MM}px;bottom:{4.2*MM}px;border:{0.15*MM}px solid {BU}"></div>
      <div class="abs" style="left:{9*MM}px;top:{8*MM}px;width:{44*MM}px;color:{BU}">
        <div class="script" style="font-size:{7.6*MM}px;white-space:nowrap">Retrouvez<span style="font-family:Corm;font-style:italic">-</span>nous</div>
        <div class="sans" style="font-size:{1.9*MM}px;letter-spacing:.38em;margin-top:{1*MM}px">Find us · Follow us</div>
        <div style="margin-top:{3*MM}px">{lead('Instagram', IG, ig_icon(3*MM, BU))}{lead('Facebook', FB_NAME, fb_icon(3*MM, BU))}</div>
        <div style="margin-top:{4*MM}px">{logo('full', BU, width=8*MM)}</div></div>
      <div class="abs" style="left:{58*MM}px;top:{9*MM}px;text-align:center;color:{BU}">
        {qr_svg(IG_URL, q, BU)}<div class="sans" style="font-size:{1.6*MM}px;margin:{1*MM}px 0 {2.4*MM}px">Instagram</div>
        {qr_svg('https://www.facebook.com/', q, BU, ghost=True)}<div class="sans" style="font-size:{1.6*MM}px;margin-top:{1*MM}px">Facebook</div></div>''', 'B_back')

# ---------- C · À la porte — doors (landscape 85 x 55) ----------
def arch(w, h, inner, col, bg):
    return (f'<div style="width:{w}px;height:{h}px;border-radius:{w/2}px {w/2}px {0.8*MM}px {0.8*MM}px;background:{bg};'
            f'box-shadow:0 0 0 {0.35*MM}px {bg}, 0 0 0 {0.6*MM}px {col};display:flex;align-items:flex-end;justify-content:center;padding-bottom:{2.4*MM}px">{inner}</div>')

def C_front():
    W, H = 85, 55
    return face(W, H, CR, f'''
      <div class="abs" style="left:{(W/2-17)*MM}px;top:{6*MM}px">{arch(34*MM, 43*MM, '', BU, BU)}</div>
      <div class="abs center" style="left:0;right:0;top:{16*MM}px">{logo('full', CR, width=22*MM)}</div>''', 'C_front')

def C_back():
    W, H = 85, 55; q = 12.5 * MM; aw, ah = 17 * MM, 26.5 * MM
    door = lambda url, ghost, icon, label: (f'<div style="text-align:center">{arch(aw, ah, qr_svg(url, q, BU, ghost), CR, CR)}'
                                            f'<div style="margin-top:{2*MM}px;color:{CR};font-family:Inter;font-weight:500;font-size:{2.3*MM}px">{icon}&nbsp;{label}</div></div>')
    return face(W, H, BU, f'''
      <div class="abs" style="left:{7*MM}px;top:{8*MM}px;color:{CR}">
        <div class="cb" style="font-size:{3*MM}px;letter-spacing:.32em">KNOCK<span style="font-family:Corm;font-weight:600">,</span> KNOCK</div>
        <div class="script" style="font-size:{7.4*MM}px;line-height:1;margin-top:{1.6*MM}px;white-space:nowrap">Come on in</div>
        <div class="ci" style="font-size:{2.8*MM}px;margin-top:{2.4*MM}px;opacity:.9">Our door is always open:<br>scan to follow along.</div>
        <div style="margin-top:{4*MM}px">{logo('full', CR, width=9*MM)}</div></div>
      <div class="abs" style="left:{43.5*MM}px;top:{10.5*MM}px;display:flex;gap:{3*MM}px">
        {door(IG_URL, False, ig_icon(2.8*MM, CR), IG)}{door('https://www.facebook.com/', True, fb_icon(2.8*MM, CR), FB_NAME)}</div>''', 'C_back')

CONCEPTS = [('A', 'Served', 'The hand from the logo serves your socials on its tray.', A_front, A_back, True),
            ('B', 'Le Bistro', 'A French bistro menu: handles listed like dishes, a pattern-filled front.', B_front, B_back, False),
            ('C', 'Come on in', 'À la porte means “at the door”: the QR codes sit inside door-shaped arches.', C_front, C_back, False)]

def board(letter, name, desc, f, b, portrait):
    return f'''<section class="board" id="board{letter}" style="width:1920px;height:1080px;background:{OX};position:relative;overflow:hidden;page-break-after:always">
  <div class="abs" style="left:90px;top:80px;color:{CR}">
    <div class="sans" style="font-size:16px">Social card · concept {letter}</div>
    <div class="script" style="font-size:110px;margin-top:20px">{name}</div>
    <div class="ci" style="font-size:30px;margin-top:10px;max-width:460px;opacity:.9">{desc}</div>
    <div class="sans" style="font-size:13px;margin-top:40px;opacity:.6;max-width:430px;line-height:1.8">{'55 × 85 mm portrait' if portrait else '85 × 55 mm'} · Facebook QR shown faded until the page is live</div></div>
  <div class="abs" style="left:{700 if portrait else 590}px;top:{110 if portrait else 250}px;display:flex;gap:{90 if portrait else 70}px;align-items:center;transform:scale({0.84 if portrait else 0.6});transform-origin:0 0">
    <div style="box-shadow:0 30px 60px rgba(0,0,0,.45);transform:rotate(-3deg)">{f()}</div>
    <div style="box-shadow:0 30px 60px rgba(0,0,0,.45);transform:rotate(2deg)">{b()}</div></div>
  <div class="abs" style="right:80px;bottom:60px">{logo('full', CR, width=80)}</div></section>'''

if __name__ == '__main__':
    css = CSS + '.face{position:relative;overflow:hidden;border-radius:6px}@page{size:1920px 1080px;margin:0}'
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{css}</style></head><body style="background:{OX}">{symbols()}'
            + ''.join(board(*c) for c in CONCEPTS) + '</body></html>')
    open(os.path.join(HERE, 'cards_v3.html'), 'w').write(html); print('ok')
