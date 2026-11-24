"""Static Instagram posts (1080 x 1350) for the new-identity launch."""
from brand import *
from final_logo import seal
from door import door_static

R, P, I, B, O, K, L = (C[k] for k in ('rouge', 'parchemin', 'ivoire', 'bordeaux', 'olive', 'cafe', 'laiton'))

GRAIN = '''<svg class="grain" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg"><filter id="g"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="3" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .17  0 0 0 0 .11  0 0 0 0 .09  0 0 0 .55 0"/></filter><rect width="100%" height="100%" filter="url(#g)"/></svg>'''

CSS = '''
.post{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:40px}
.grain{position:absolute;inset:0;pointer-events:none;opacity:.16;mix-blend-mode:multiply}
.lab{font-family:'Jost';font-size:17px;letter-spacing:.42em;text-transform:uppercase}
'''

def post1():
    """Identity reveal: logo + arched palette (the doors of the palette)."""
    arches = [(P, 'Parchemin', K), (I, 'Ivoire', K), (B, 'Bordeaux', P), (O, 'Olive', P), (L, 'Laiton', K)]
    arch = lambda bg, n, fg: f'''<div style="display:flex;flex-direction:column;align-items:center;gap:20px">
        <div style="width:150px;height:250px;background:{bg};border-radius:75px 75px 0 0;position:relative"></div>
        <div class="lab" style="font-size:13px;color:{P};letter-spacing:.32em">{n}</div></div>'''
    return f'''<div class="post" id="post1" style="background:{R};color:{P}">
  <div style="position:absolute;left:72px;right:72px;top:66px;display:flex;justify-content:space-between" class="lab"><span>Nouvelle identité</span><span>MMXXVI</span></div>
  <div class="center" style="position:absolute;left:0;right:0;top:170px">{logo('full', P, width=780)}</div>
  <div style="position:absolute;left:0;right:0;top:760px;display:flex;justify-content:center;gap:34px">{''.join(arch(*a) for a in arches)}</div>
  <div style="position:absolute;left:0;right:0;bottom:70px;text-align:center">
    <div class="serif" style="font-size:46px;font-weight:300">Same trays, <em>a new door.</em></div></div>
  {GRAIN}
</div>'''

def post2():
    """'By hand' — the icon blown up to architectural scale."""
    ix, iy, iw, ih = VB['icon']
    big = 1900
    return f'''<div class="post" id="post2" style="background:{P};color:{R}">
  <div style="position:absolute;left:-420px;top:520px">{logo('icon', R, width=big)}</div>
  <div style="position:absolute;left:76px;top:96px">
    <div class="lab" style="color:{R}">Nouvelle identité · nº 2</div>
    <div class="serif" style="margin-top:36px;font-size:112px;line-height:.98;font-weight:300;letter-spacing:-.02em;color:{R}">Served<br><em>by hand,</em><br>every day.</div>
  </div>
  <div style="position:absolute;right:76px;top:110px;width:330px;text-align:right">
    {seal(R, 210)}
  </div>
  <div style="position:absolute;right:76px;bottom:72px;text-align:right;color:{K}">
    <p style="font-size:21px;line-height:1.6;font-weight:300;max-width:440px;margin-left:auto">The hand in our new mark is the gesture behind every tray: carried with care, presented at your door.</p>
  </div>
  {GRAIN}
</div>'''

def post3_cover():
    """Cover frame for the animated reel (grid thumbnail): the closed door."""
    return f'''<div class="post" id="post3cover" style="background:{P};color:{R}">
  <div style="position:absolute;left:72px;right:72px;top:66px;display:flex;justify-content:space-between" class="lab"><span>Knock, knock</span><span>nº 3</span></div>
  <div class="center" style="position:absolute;left:0;right:0;top:150px">{door_static(560)}</div>
  <div style="position:absolute;inset:0;background:linear-gradient(115deg, rgba(92,31,26,0) 0%, rgba(92,31,26,0) 52%, rgba(92,31,26,.10) 52.2%, rgba(92,31,26,.06) 100%);mix-blend-mode:multiply"></div>
  <div style="position:absolute;left:0;right:0;bottom:78px;text-align:center">
    <div class="serif" style="font-size:52px;font-weight:300">Someone new <em>is at the door.</em></div></div>
  {GRAIN}
</div>'''

POSTS = [post1, post2, post3_cover]

if __name__ == '__main__':
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}{CSS}body{{background:#999}}</style></head>'
            f'<body>{symbols()}{"".join(p() for p in POSTS)}</body></html>')
    open(os.path.join(HERE, 'posts.html'), 'w').write(html)
    print('ok')
