"""Six food posts (1080 x 1350) built on the client's own tray photography."""
from brand import *
from final_logo import seal
from posts import GRAIN, CSS

R, P, I, B, O, K, L = (C[k] for k in ('rouge', 'parchemin', 'ivoire', 'bordeaux', 'olive', 'cafe', 'laiton'))
PH = 'client_photos/crops/'

CSS2 = CSS + f'''
.ph{{display:block;object-fit:cover}}
.arch{{overflow:hidden;position:relative}}
.cap{{font-family:'Cormorant Garamond';font-style:italic;font-weight:400}}
.toprow{{position:absolute;left:72px;right:72px;top:62px;display:flex;justify-content:space-between}}
'''

def toprow(l, r, color):
    return f'<div class="toprow lab" style="color:{color}"><span>{l}</span><span>{r}</span></div>'

def arch_img(src, w, h, extra=''):
    return f'<div class="arch" style="width:{w}px;height:{h}px;border-radius:{w/2}px {w/2}px 0 0;{extra}"><img class="ph" src="{PH}{src}" style="width:{w}px;height:{h}px"></div>'

# 4 — A is for à la porte
def p4():
    w, h = 680, 864
    return f'''<div class="post" id="post4" style="background:{P};color:{R}">
  {toprow('Le menu', 'Nº 4', R)}
  <div style="position:absolute;left:0;right:0;top:118px;text-align:center">
    <div class="serif" style="font-size:66px;font-weight:300;line-height:1">A is for</div>
    <div class="center" style="margin-top:14px">{logo('script', R, width=500)}</div>
  </div>
  <div style="position:absolute;left:{(1080-w)/2}px;top:398px">
    <div style="position:absolute;left:-16px;top:-16px;width:{w+32}px;height:{h+16}px;border:1.5px solid {R};border-bottom:none;border-radius:{(w+32)/2}px {(w+32)/2}px 0 0"></div>
    {arch_img('a_box.jpg', w, h)}
  </div>
  <div class="lab" style="position:absolute;left:0;right:0;top:1290px;text-align:center;font-size:14px;color:{K}">The letter box &nbsp;·&nbsp; ask for your initial</div>
  {GRAIN}
</div>'''

# 5 — Le jardin: the edible roses
def p5():
    d = 330
    roses = [('rose_cucumber', 'Rose de concombre', 'cucumber'), ('rose_lemon', 'Rose de citron', 'lemon'),
             ('rose_grapefruit', 'Rose de pamplemousse', 'grapefruit'), ('rose_salami', 'Rose de salami', 'salami')]
    cells = ''
    for i, (f, fr, en) in enumerate(roses):
        cx = 300 if i % 2 == 0 else 780
        cy = 548 if i < 2 else 990
        cells += f'''<div style="position:absolute;left:{cx-d/2-12}px;top:{cy-d/2-12}px;width:{d+24}px;height:{d+24}px;border-radius:50%;border:1.3px solid {R}"></div>
  <img class="ph" src="{PH}{f}.jpg" style="position:absolute;left:{cx-d/2}px;top:{cy-d/2}px;width:{d}px;height:{d}px;border-radius:50%">
  <div style="position:absolute;left:{cx-230}px;width:460px;top:{cy+d/2+26}px;text-align:center">
    <div class="cap" style="font-size:31px;color:{R}">{fr}</div>
    <div class="lab" style="font-size:12px;margin-top:4px;color:{K};opacity:.75">{['i', 'ii', 'iii', 'iv'][i]}. &nbsp;{en}</div></div>'''
    return f'''<div class="post" id="post5" style="background:{I};color:{R}">
  {toprow('Le jardin', 'Nº 5', R)}
  <div style="position:absolute;left:72px;top:122px">
    <div class="serif" style="font-size:84px;font-weight:300;line-height:.98;letter-spacing:-.01em">Our roses<br><em>are edible.</em></div></div>
  <div style="position:absolute;right:72px;top:150px;text-align:right;color:{K};font-size:18px;line-height:1.55;font-weight:300;width:330px">Cut, curled and set by hand, petal by petal, on every tray.</div>
  {cells}
  {GRAIN}
</div>'''

# 6 — Anatomy of a tray
def p6():
    X0, Y0, S = 60, 488, 960 / 720
    pt = lambda x, y: (X0 + x * S, Y0 + y * S)
    top = [('Walnuts &amp; cold cuts', (105, 140), 196), ('Cucumber rose', (245, 133), 452), ('Waffles', (565, 73), 813)]
    bot = [('Honey &amp; jam', (425, 258), 600), ('Grapes &amp; strawberries', (622, 222), 880)]
    svg = ''
    labels = ''
    for t, (x, y), lx in top:
        px, py = pt(x, y)
        svg += f'<path d="M{lx},{442} L{lx},{460} L{px},{py-8}" fill="none" stroke="{R}" stroke-width="1.4"/><circle cx="{px}" cy="{py}" r="7" fill="{I}" stroke="{R}" stroke-width="2"/>'
        labels += f'<div class="cap" style="position:absolute;left:{lx-160}px;width:320px;top:396px;text-align:center;font-size:27px;color:{R}">{t}</div>'
    for t, (x, y), lx in bot:
        px, py = pt(x, y)
        svg += f'<path d="M{px},{py+8} L{lx},{1000} L{lx},{1020}" fill="none" stroke="{I}" stroke-width="1.4"/><circle cx="{px}" cy="{py}" r="7" fill="{I}" stroke="{R}" stroke-width="2"/>'
        svg += f'<path d="M{lx},{976} L{lx},{1020}" fill="none" stroke="{R}" stroke-width="1.4"/>'
        labels += f'<div class="cap" style="position:absolute;left:{lx-170}px;width:340px;top:1026px;text-align:center;font-size:27px;color:{R}">{t}</div>'
    return f'''<div class="post" id="post6" style="background:{P};color:{R}">
  {toprow('Anatomy of a tray', 'Nº 6', R)}
  <div style="position:absolute;left:72px;top:128px" class="serif"><div style="font-size:84px;font-weight:300;line-height:.98">What’s on<br><em>the tray?</em></div></div>
  <div style="position:absolute;right:72px;top:160px;width:340px;text-align:right;color:{K};font-size:18px;line-height:1.55;font-weight:300">The “get well soon” tray, read like a menu.</div>
  <div style="position:absolute;left:{X0-12}px;top:{Y0-12}px;width:{960+24}px;height:{480+24}px;border:1.4px solid {R}"></div>
  <img class="ph" src="{PH}tray_anatomy.jpg" style="position:absolute;left:{X0}px;top:{Y0}px;width:960px;height:480px">
  <svg width="1080" height="1350" style="position:absolute;inset:0">{svg}</svg>
  {labels}
  <div style="position:absolute;left:0;right:0;top:1168px" class="center">{logo('word', R, width=330)}</div>
  {GRAIN}
</div>'''

# 7 — For every occasion
def p7():
    w, h, g = 300, 434, 45
    x0 = (1080 - 3 * w - 2 * g) / 2
    occ = [('occ_getwell', 'Get well soon'), ('occ_babygirl', 'Welcome, baby girl'), ('brunch', 'Sunday brunch')]
    arches = ''.join(f'''<div style="position:absolute;left:{x0+i*(w+g)}px;top:330px">{arch_img(f + '.jpg', w, h)}
      <div class="cap" style="text-align:center;font-size:30px;margin-top:22px;color:{P}">{t}</div></div>''' for i, (f, t) in enumerate(occ))
    return f'''<div class="post" id="post7" style="background:{R};color:{P}">
  {toprow('For every occasion', 'Nº 7', P)}
  <div style="position:absolute;left:0;right:0;top:122px;text-align:center" class="serif"><div style="font-size:64px;font-weight:300;line-height:1.04">A tray for every day,<br><em>and every occasion.</em></div></div>
  {arches}
  <div style="position:absolute;left:0;right:0;top:905px" class="center">{logo('icon', P, width=250)}</div>
  <div style="position:absolute;left:0;right:0;top:1105px;text-align:center"><span class="serif" style="font-size:36px;font-weight:300">Tell us the occasion, <em>we’ll set the tray.</em></span></div>
  <div class="lab" style="position:absolute;left:0;right:0;top:1262px;text-align:center;font-size:14px">Order by DM &nbsp;·&nbsp; @a.la.porte</div>
  {GRAIN}
</div>'''

# 8 — Made by hand (details)
def p8():
    return f'''<div class="post" id="post8" style="background:{R};color:{P}">
  <img class="ph" src="{PH}details.jpg" style="position:absolute;left:0;top:0;width:1080px;height:848px">
  <div style="position:absolute;left:0;top:848px;width:1080px;height:502px;background:{R}"></div>
  <div style="position:absolute;right:64px;top:736px;width:224px;height:224px;border-radius:50%;background:{P}" class="center">{seal(R, 206)}</div>
  <div class="lab" style="position:absolute;left:72px;top:902px;font-size:15px">Nº 8 &nbsp;·&nbsp; Fait main</div>
  <div class="serif" style="position:absolute;left:72px;top:950px;font-size:70px;font-weight:300;line-height:1.02">Made by hand,<br><em>down to the last petal.</em></div>
  <div style="position:absolute;left:72px;top:1150px;width:620px;font-size:20px;line-height:1.6;font-weight:300;opacity:.92">Every cucumber rose, every fig, every ribbon is arranged by hand, then carried to your door.</div>
  <div style="position:absolute;right:72px;bottom:66px">{logo('word', P, width=250)}</div>
  {GRAIN}
</div>'''

# 9 — Knock, knock: the hand serves the tray
def p9():
    w, h = 520, 727
    iw = 600; ik = iw / VB['icon'][2]
    tray_off = (587.64 - VB['icon'][1]) * ik       # distance from icon top to the tray surface
    ay = 128; ab = ay + h
    return f'''<div class="post" id="post9" style="background:{R};color:{P}">
  {toprow('Knock, knock', 'Nº 9', P)}
  <div style="position:absolute;left:{(1080-w)/2}px;top:{ay}px">{arch_img('order.jpg', w, h)}</div>
  <div style="position:absolute;left:{(1080-iw)/2}px;top:{ab - tray_off + 2}px">{logo('icon', P, width=iw)}</div>
  <div style="position:absolute;right:72px;top:1052px;text-align:right" class="serif"><div style="font-size:58px;font-weight:300;line-height:1.02">Breakfast<br><em>is at the door.</em></div></div>
  <div class="lab" style="position:absolute;left:72px;right:72px;top:1268px;display:flex;justify-content:space-between;font-size:14px"><span>Order by DM</span><span>@a.la.porte</span></div>
  {GRAIN}
</div>'''

POSTS2 = [p4, p5, p6, p7, p8, p9]

if __name__ == '__main__':
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{CSS2}body{{background:#999}}</style></head>'
            f'<body>{symbols()}{"".join(p() for p in POSTS2)}</body></html>')
    open(os.path.join(HERE, 'posts2.html'), 'w').write(html)
    print('ok')
