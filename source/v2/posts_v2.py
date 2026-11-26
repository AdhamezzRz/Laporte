"""À LA PORTE — December content plan, posts 2-6 (1080 x 1350). Post 1 is the animated reel (reel_v2.py)."""
from brand2 import *

A = 'assets/'

def p2():
    """Let the good bites begin — tray in a tilted oval on burgundy, editorial type."""
    return f'''<div class="post" id="post2" style="background:radial-gradient(ellipse 90% 80% at 62% 55%, {WI} 0%, {BU} 45%, {OX} 100%)">
  <div class="abs" style="left:250px;top:430px;width:960px;height:640px;border:1.6px solid {CR}66;border-radius:50%;transform:rotate(-20deg)"></div>
  <div class="abs" style="left:230px;top:380px;width:960px;height:640px;border-radius:50%;overflow:hidden;transform:rotate(-27deg);box-shadow:0 50px 90px rgba(20,0,4,.55)">
    <img src="{A}heart.jpg" style="position:absolute;left:-57px;top:-67px;width:1040px;height:1150px;object-fit:cover;transform-origin:537px 387px;transform:rotate(27deg) scale(1.3)">
  </div>
  <div class="abs cb" style="left:70px;top:96px;color:{CR};font-size:152px">LET THE<br>GOOD<br>BITES</div>
  <div class="abs script" style="left:520px;top:960px;color:{CR};font-size:270px;transform:rotate(-7deg);text-shadow:0 10px 30px rgba(30,0,6,.45)">begin</div>
  <div class="abs" style="left:450px;top:1000px">{sparkle(64, CR, 3.2)}</div>
  <div class="abs" style="left:985px;top:930px">{sparkle(38, CR, 3)}</div>
  <div class="abs" style="right:70px;top:92px">{logo('full', CR, width=150)}</div>
  <div class="abs sans" style="left:72px;bottom:64px;color:{CR};font-size:15px;opacity:.85">À la porte · platters</div>
  {GRAIN}
</div>'''

def p3():
    """Hello December — client's platter full-bleed, overlay, cream card with search field."""
    mag = (f'<svg width="30" height="30" viewBox="0 0 30 30"><circle cx="12.5" cy="12.5" r="9" fill="none" stroke="{BU}" stroke-width="2.6"/>'
           f'<path d="M19.5 19.5 L27 27" stroke="{BU}" stroke-width="2.8" stroke-linecap="round"/></svg>')
    return f'''<div class="post" id="post3">
  <img src="{A}dec_bg_2k.jpg" class="abs" style="left:0;top:0;width:1080px;height:1350px;object-fit:cover">
  <div class="abs" style="inset:0;background:linear-gradient(180deg, rgba(59,0,12,.55) 0%, rgba(59,0,12,.18) 30%, rgba(59,0,12,.18) 70%, rgba(59,0,12,.62) 100%)"></div>
  <div class="abs center" style="left:0;right:0;top:64px">{logo('full', CR, width=124)}</div>
  <div class="abs" style="left:190px;top:400px;width:700px;height:520px;background:{CR};border-radius:34px;box-shadow:0 40px 90px rgba(30,0,6,.55);text-align:center">
    <div class="script" style="color:{BU};font-size:170px;margin-top:40px">hello</div>
    <div class="cb" style="color:{BU};font-size:112px;letter-spacing:.02em;margin-top:-8px">DECEMBER</div>
    <div style="margin:44px auto 0;width:590px;height:70px;border-radius:35px;background:#fbf5e6;box-shadow:inset 0 0 0 1.5px {BU}33, 0 8px 18px rgba(85,11,24,.12);display:flex;align-items:center;padding:0 28px;gap:14px">
      <div style="width:2px;height:30px;background:{BU}"></div>
      <div class="ci" style="color:{BU};font-size:29px;flex:1;text-align:left">a little more delightful</div>{mag}</div>
  </div>
  <div class="abs" style="left:132px;top:352px">{sparkle(70, CR, 3)}</div>
  <div class="abs" style="left:880px;top:880px">{sparkle(56, CR, 3)}</div>
  <div class="abs" style="left:910px;top:356px">{sparkle(30, CR, 2.6)}</div>
  <div class="abs sans center" style="left:0;right:0;bottom:70px;color:{CR};font-size:15px">À la porte · platters &amp; trays</div>
  {GRAIN}
</div>'''

def sticker(name, x, y, w, rot):
    return (f'<img src="{A}cut_{name}.png" class="abs" style="left:{x}px;top:{y}px;width:{w}px;transform:rotate({rot}deg);'
            f'filter:drop-shadow(0 16px 18px rgba(59,0,12,.28)) drop-shadow(0 3px 3px rgba(59,0,12,.25))">')

def p4():
    """The little things make life delicious — type poster with the client's own 'little things' as stickers."""
    return f'''<div class="post" id="post4" style="background:{CR}">
  <div class="abs center" style="left:0;right:0;top:62px">{logo('full', BU, width=112)}</div>
  <div class="abs cb" style="left:72px;top:300px;color:{BU};font-size:136px">THE LITTLE<br>THINGS MAKE<br>LIFE</div>
  <div class="abs script" style="left:300px;top:612px;color:{WI};font-size:250px;transform:rotate(-6deg)">delicious</div>
  {sticker('grapefruit', 770, 120, 250, 14)}
  {sticker('lemon', 455, 560, 150, -12)}
  {sticker('salami', 90, 930, 250, -8)}
  {sticker('kiwi', 740, 975, 200, 22)}
  <div class="abs" style="left:700px;top:100px">{sparkle(46, BU, 3)}</div>
  <div class="abs" style="left:508px;top:1070px">{heart(60, BU, 3.4, -10)}</div>
  <div class="abs" style="left:345px;top:880px">{squiggle(330, WI, 3.4)}</div>
  <div class="abs" style="left:950px;top:860px">{sparkle(34, BU, 3)}</div>
  <div class="abs sans center" style="left:0;right:0;bottom:62px;color:{BU};font-size:15px">@a.la.porte</div>
  {GRAIN}
</div>'''

def p5():
    """A platter for every festive moment — the client's letter box composited on a Christmas table."""
    return f'''<div class="post" id="post5">
  <img src="{A}xmas_table_2k.jpg" class="abs" style="left:0;top:0;width:1080px;height:1350px;object-fit:cover">
  <img src="{A}cut_abox.png" class="abs" style="left:262px;top:212px;width:560px;transform:rotate(-7deg);
      filter:brightness(.93) saturate(.96) drop-shadow(0 34px 30px rgba(25,0,5,.55)) drop-shadow(0 6px 6px rgba(25,0,5,.45))">
  <div class="abs" style="left:0;right:0;bottom:0;height:470px;background:linear-gradient(180deg, rgba(59,0,12,0) 0%, rgba(59,0,12,.78) 55%, rgba(59,0,12,.92) 100%)"></div>
  <div class="abs" style="left:0;right:0;top:0;height:220px;background:linear-gradient(0deg, rgba(59,0,12,0), rgba(59,0,12,.55))"></div>
  <div class="abs center" style="left:0;right:0;top:56px">{logo('full', CR, width=118)}</div>
  <div class="abs" style="left:0;right:0;top:1035px;text-align:center;color:{CR}">
    <div class="cb" style="font-size:60px;letter-spacing:.06em">A PLATTER FOR EVERY</div>
    <div class="script" style="font-size:168px;margin-top:-6px">festive moment</div>
  </div>
  <div class="abs" style="left:205px;top:1150px">{sparkle(40, CR, 2.8)}</div>
  {GRAIN}
</div>'''

def p6():
    """Make someone's Christmas a little tastier — the gift hand-over, with a die-cut brand tag."""
    tag = f'''<div class="abs" style="left:612px;top:742px;width:178px;height:250px;transform:rotate(-14deg);transform-origin:50% 0">
      <svg width="178" height="250" viewBox="0 0 178 250" style="position:absolute;inset:0;filter:drop-shadow(0 14px 14px rgba(25,0,5,.45))">
        <path d="M30,0 H148 L178,34 V250 H0 V34 Z" fill="{CR}"/><circle cx="89" cy="30" r="9" fill="{WI}"/>
        <path d="M30,0 H148 L178,34 V250 H0 V34 Z" fill="none" stroke="{BU}33" stroke-width="2"/></svg>
      <div class="abs center" style="left:0;right:0;top:66px">{logo('full', BU, width=112)}</div>
      <div class="abs script center" style="left:0;right:0;top:196px;color:{WI};font-size:34px">for you</div></div>
    <svg class="abs" style="left:0;top:0" width="1080" height="1350"><path d="M552,662 C590,690 640,700 700,752" fill="none" stroke="{CR}" stroke-width="2.2"/></svg>'''
    return f'''<div class="post" id="post6">
  <img src="{A}hands_2k.jpg" class="abs" style="left:0;top:0;width:1080px;height:1350px;object-fit:cover">
  <div class="abs" style="left:0;right:0;top:0;height:520px;background:linear-gradient(180deg, rgba(59,0,12,.75), rgba(59,0,12,0))"></div>
  <div class="abs" style="left:0;right:0;top:96px;text-align:center;color:{CR}">
    <div class="cb" style="font-size:66px;letter-spacing:.05em">MAKE SOMEONE<span style="font-family:Corm;font-weight:600">’</span>S</div>
    <div class="script" style="font-size:210px;margin-top:-10px;line-height:.9">Christmas</div>
    <div class="ci" style="font-size:60px;margin-top:6px">a little tastier.</div>
  </div>
  {tag}
  <div class="abs" style="left:0;right:0;bottom:0;height:260px;background:linear-gradient(0deg, rgba(59,0,12,.85), rgba(59,0,12,0))"></div>
  <div class="abs center" style="left:0;right:0;bottom:70px">
    <div class="sans" style="color:{CR};font-size:15px;border:1.5px solid {CR}aa;border-radius:40px;padding:18px 34px">Gift a platter · DM @a.la.porte</div></div>
  {GRAIN}
</div>'''

POSTS = [p2, p3, p4, p5, p6]

if __name__ == '__main__':
    html = (f'<!doctype html><html><head><meta charset="utf-8"><style>{CSS}</style></head>'
            f'<body>{symbols()}{"".join(p() for p in POSTS)}</body></html>')
    open(os.path.join(HERE, 'posts_v2.html'), 'w').write(html)
    print('ok')
