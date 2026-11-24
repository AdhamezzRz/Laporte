"""Builds the full brand identity book: 02_Brand_Identity/ALaPorte_Brand_Identity.pdf"""
from brand import *
import final_logo as FL
from final_logo import seal
from door import door_static

R, P, I, B, O, K, L = (C[k] for k in ('rouge', 'parchemin', 'ivoire', 'bordeaux', 'olive', 'cafe', 'laiton'))
POSTS = 'assets/'
pages = []
F = lambda n: folio('À la porte — Brand identity', n)

def head(title, n, color=R):
    return f'<div class="head" style="color:{color}"><h2>{title}</h2><span class="label">{n}</span></div>'

# 1 — Cover
pages.append(f'''<section class="page" style="background:{P}">
  <div style="position:absolute;left:0;top:0;bottom:0;width:1040px;background:{R}" class="center">{logo('full', P, width=760)}</div>
  <div style="position:absolute;left:1040px;right:0;top:0;bottom:0" class="center">{door_static(470)}</div>
  <div class="label" style="position:absolute;left:96px;top:84px;color:{P}">Brand identity</div>
  <div class="label" style="position:absolute;right:96px;top:84px;color:{R}">MMXXVI</div>
  <div class="folio" style="color:{P};right:auto;width:850px"><span>À la porte</span><span>v1.0</span></div>
</section>''')

# 2 — The idea
pages.append(f'''<section class="page" style="background:{I};color:{K}">
  {head('The <em>idea</em>', '01')}
  <div style="position:absolute;left:96px;top:250px;width:1040px">
    <p class="serif" style="font-size:88px;font-weight:300;line-height:1.02;color:{R};letter-spacing:-.015em"><em>À la porte</em> means<br>“at the door.”</p>
    <p style="margin-top:48px;font-size:24px;line-height:1.65;font-weight:300;max-width:900px">It is the moment the doorbell rings and something beautiful arrives: a tray, arranged by hand, presented as a maître d’ would present it. Not a delivery, an arrival.</p>
    <p style="margin-top:22px;font-size:24px;line-height:1.65;font-weight:300;max-width:900px">The identity is built from two objects: <b style="font-weight:500">the door</b>, where every order ends, and <b style="font-weight:500">the hand</b> that carries it there. Everything else is warmth, restraint and a little old-world ceremony, for every day.</p>
  </div>
  <div style="position:absolute;right:96px;top:250px;width:560px;display:flex;flex-direction:column;gap:0">
    {''.join(f"""<div style="border-top:1px solid {R}55;padding:30px 0;display:flex;justify-content:space-between;align-items:baseline">
      <span class="serif it" style="font-size:48px;color:{R};font-weight:300">{w}</span><span class="label" style="font-size:13px">{d}</span></div>""" for w, d in [('Gracious', 'Served, not sent'), ('Generous', 'Abundant trays'), ('Everyday', 'Ritual, not occasion'), ('Personal', 'By hand, to your door')])}
  </div>
  {F('')}
</section>''')

# 3 — Two symbols
pages.append(f'''<section class="page" style="background:{R};color:{P}">
  {head('The door <em>&amp;</em> the hand', '02', P)}
  <div style="position:absolute;left:0;right:0;top:220px;bottom:170px;display:flex;align-items:center;justify-content:center;gap:120px">
    <div style="text-align:center">{door_static(330)}<div class="label" style="margin-top:34px;font-size:13px">La porte · where it ends</div></div>
    <div class="serif" style="font-size:120px;font-weight:300;opacity:.8">+</div>
    <div style="text-align:center"><div class="center" style="height:515px">{logo('icon', P, width=460)}</div><div class="label" style="margin-top:34px;font-size:13px">La main · how it gets there</div></div>
    <div class="serif" style="font-size:120px;font-weight:300;opacity:.8">=</div>
    <div style="text-align:center"><div class="center" style="height:515px">{logo('full', P, width=480)}</div><div class="label" style="margin-top:34px;font-size:13px">À la porte</div></div>
  </div>
  {F('')}
</section>''')

# 4-8 — logo pages reused from the final-logo file (primary, family, clear space, palette, typography)
import re as _re
for n, idx in enumerate((2, 7, 8, 9, 11), start=3):
    pg = FL.pages[idx].replace('À la porte — Final logo', 'À la porte — Brand identity')
    pg = _re.sub(r'<span class="label">\d\d</span></div>', f'<span class="label">{n:02d}</span></div>', pg, count=1)
    pg = pg.replace('<span>02</span>', f'<span>{n:02d}</span>')
    pages.append(pg)

# 9 — Graphic elements
tile_icons = ''.join(f'<div class="center" style="width:120px;height:120px">{logo("icon", R, width=74) if (i + i//6) % 2 == 0 else "<div style=\'width:34px;height:52px;border-radius:17px 17px 0 0;background:" + R + "\'></div>"}</div>' for i in range(36))
pages.append(f'''<section class="page" style="background:{P};color:{K}">
  {head('Graphic <em>elements</em>', '08')}
  <div style="position:absolute;left:96px;top:230px;display:grid;grid-template-columns:720px 1fr;gap:80px;right:96px">
    <div style="background:{I};width:720px;height:720px;display:grid;grid-template-columns:repeat(6,120px);overflow:hidden">{tile_icons}</div>
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:56px 64px">
      <div><div class="center" style="height:250px;background:{I}">{seal(R, 220)}</div><div class="label" style="font-size:13px;margin-top:16px">The seal</div><p style="font-size:17px;line-height:1.55;font-weight:300;margin-top:8px">Stickers, wax-style closures, stamps on kraft.</p></div>
      <div><div class="center" style="height:250px;background:{I}">{door_static(140)}</div><div class="label" style="font-size:13px;margin-top:16px">The door</div><p style="font-size:17px;line-height:1.55;font-weight:300;margin-top:8px">Illustration for launches, gifting and seasonal campaigns.</p></div>
      <div><div class="center" style="height:250px;background:{I};gap:18px">{''.join(f'<div style="width:46px;height:84px;border-radius:23px 23px 0 0;background:{c}"></div>' for c in (R, B, O, L, P))}</div><div class="label" style="font-size:13px;margin-top:16px">The arch</div><p style="font-size:17px;line-height:1.55;font-weight:300;margin-top:8px">A frame for photos, swatches and story highlights.</p></div>
      <div><div class="center" style="height:250px;background:{I};flex-direction:column;gap:26px">
          <svg width="380" height="16" viewBox="0 0 380 16"><rect x="0" y="5" width="380" height="5" rx="2.5" fill="{R}"/><rect x="24" y="12" width="332" height="2" fill="{R}"/></svg>
          <div class="serif it" style="font-size:30px;color:{R}">Le menu du jour</div>
          <svg width="380" height="16" viewBox="0 0 380 16"><rect x="0" y="5" width="380" height="5" rx="2.5" fill="{R}"/><rect x="24" y="12" width="332" height="2" fill="{R}"/></svg></div>
        <div class="label" style="font-size:13px;margin-top:16px">The tray line</div><p style="font-size:17px;line-height:1.55;font-weight:300;margin-top:8px">The tray from the mark, used as a divider.</p></div>
    </div>
  </div>
  <div class="label" style="position:absolute;left:96px;top:968px;font-size:13px">Pattern · hands &amp; arches, for tray liners and tissue</div>
  {F('')}
</section>''')

# 10 — Voice
lines = [('Knock, knock.', 'Launches & new menus'), ('Served by hand.', 'Craft & care'), ('Breakfast is at the door.', 'Morning orders'),
         ('A tray for everyday.', 'Always, the sign-off'), ('Something lovely is on its way.', 'Order confirmation'), ('Merci, see you at the door.', 'Thank-you cards')]
pages.append(f'''<section class="page" style="background:{B};color:{P}">
  {head('Tone of <em>voice</em>', '09', P)}
  <div style="position:absolute;left:96px;top:240px;width:620px">
    <p class="serif" style="font-size:54px;font-weight:300;line-height:1.12">Warm like a host,<br><em>never loud.</em></p>
    <p style="margin-top:30px;font-size:21px;line-height:1.65;font-weight:300;opacity:.9">We speak the way a good host greets you at the door: short, warm, a touch of French. One French word per line at most, always easy to read. Never shout prices, never use more than one emoji.</p>
  </div>
  <div style="position:absolute;left:840px;right:96px;top:240px">
    {''.join(f"""<div style="display:flex;justify-content:space-between;align-items:baseline;border-top:1px solid {P}44;padding:24px 0">
      <span class="serif it" style="font-size:42px;font-weight:300">{a}</span><span class="label" style="font-size:12px;opacity:.75">{b}</span></div>""" for a, b in lines)}
  </div>
  {F('')}
</section>''')

# 11 — Packaging
box = f'''<div style="position:relative;width:520px;height:520px;background:{P};box-shadow:26px 30px 0 rgba(60,18,14,.18), 0 2px 0 rgba(0,0,0,.05)">
  <div class="center" style="position:absolute;left:0;top:0;bottom:0;width:380px">{logo('full', R, width=300)}</div>
  <div style="position:absolute;left:400px;top:0;bottom:0;width:44px;background:{R}"></div>
  <div style="position:absolute;left:340px;top:330px;width:164px;height:164px;border-radius:50%;background:{B}" class="center">{seal(P, 150, ring=True)}</div></div>'''
liner = f'''<div style="position:relative;width:640px;height:420px;border-radius:50%;background:{L};box-shadow:16px 20px 0 rgba(60,18,14,.16)" class="center">
  <div style="width:600px;height:380px;border-radius:50%;overflow:hidden;background:{I};display:grid;grid-template-columns:repeat(10,60px);transform:rotate(0deg)">
   {''.join(f'<div class="center" style="width:60px;height:60px">{logo("icon", R, width=34) if (i + i//10) % 2 == 0 else ""}</div>' for i in range(70))}</div></div>'''
pages.append(f'''<section class="page" style="background:{R};color:{P}">
  {head('Packaging', '10', P)}
  <div style="position:absolute;left:120px;top:250px">{box}<div class="label" style="margin-top:56px;font-size:13px">Gift box · Parchemin board, Rouge ribbon, Bordeaux seal</div></div>
  <div style="position:absolute;left:880px;top:300px">{liner}<div class="label" style="margin-top:56px;font-size:13px">Tray liner · Ivoire tissue with the hand pattern</div></div>
  <div style="position:absolute;right:150px;top:740px;width:190px;height:190px;border-radius:50%;background:{P}" class="center">{seal(R, 176)}</div>
  {F('')}
</section>''')

# 12 — Print: cards + bag
bag = f'''<svg width="430" height="620" viewBox="0 0 430 620">
  <path d="M120,110 C120,10 310,10 310,110" fill="none" stroke="{B}" stroke-width="9"/>
  <rect x="15" y="100" width="400" height="510" fill="#D7BD8C"/>
  <rect x="15" y="100" width="400" height="34" fill="#D3B985"/>
  <line x1="15" y1="590" x2="415" y2="590" stroke="#C9AE7B" stroke-width="2"/>
  <circle cx="120" cy="118" r="6" fill="{B}"/><circle cx="310" cy="118" r="6" fill="{B}"/>
  <foreignObject x="15" y="200" width="400" height="300"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;justify-content:center;align-items:center;height:300px">{logo('full', R, width=300)}</div></foreignObject>
</svg>'''
card_front = f'<div class="center" style="width:504px;height:288px;background:{R};box-shadow:14px 18px 0 rgba(60,18,14,.18)">{logo("full", P, width=250)}</div>'
card_back = f'''<div style="width:504px;height:288px;background:{I};box-shadow:14px 18px 0 rgba(60,18,14,.14);position:relative;padding:40px 44px;color:{K}">
  <div class="serif it" style="font-size:38px;color:{R};font-weight:300">Merci,</div>
  <div class="serif" style="font-size:26px;font-weight:300;margin-top:4px">see you at the door.</div>
  <div class="label" style="position:absolute;left:44px;bottom:40px;font-size:12px;color:{R}">@a.la.porte</div>
  <div style="position:absolute;right:36px;bottom:30px">{logo('icon', R, width=110)}</div></div>'''
pages.append(f'''<section class="page" style="background:{I};color:{K}">
  {head('Print', '11')}
  <div style="position:absolute;left:140px;top:250px">{bag}<div class="label" style="margin-top:28px;font-size:13px">Delivery bag · kraft, Bordeaux cord</div></div>
  <div style="position:absolute;left:760px;top:290px;transform:rotate(-4deg)">{card_front}</div>
  <div style="position:absolute;left:1180px;top:520px;transform:rotate(3deg)">{card_back}</div>
  <div class="label" style="position:absolute;left:760px;top:900px;font-size:13px">Card · front in Rouge Porte, thank-you note on Ivoire</div>
  {F('')}
</section>''')

# 13 — Launch posts
def shot(src, cap, w=470):
    return f'''<div><img src="{src}" style="width:{w}px;display:block;box-shadow:18px 22px 0 rgba(60,18,14,.14)">
      <div class="label" style="font-size:12px;margin-top:30px">{cap}</div></div>'''
pages.append(f'''<section class="page" style="background:{I};color:{K}">
  {head('The <em>launch</em> · three posts', '12')}
  <div style="position:absolute;left:0;right:0;top:220px;display:flex;justify-content:center;gap:70px">
    {shot(POSTS + 'Post1_Identity_Reveal_1080x1350.jpg', 'Nº 1 · The reveal')}
    {shot(POSTS + 'Post2_Served_By_Hand_1080x1350.jpg', 'Nº 2 · Served by hand')}
    {shot(POSTS + 'Post3_Reel_Cover_1080x1350.jpg', 'Nº 3 · Knock, knock (animated)')}
  </div>
  {F('Post in this order, one per day')}
</section>''')

# 14 — Reel storyboard
frames = [('t_0.90', '0:00', 'Knock, knock.'), ('t_2.60', '0:02', 'The doors open'), ('t_3.90', '0:03', 'Through the door'),
          ('t_5.70', '0:05', 'The script writes itself'), ('t_6.90', '0:06', 'The bell rings'), ('t_9.60', '0:09', 'At your door.')]
pages.append(f'''<section class="page" style="background:{R};color:{P}">
  {head('Nº 3 · <em>Knock, knock</em> · the reel', '13', P)}
  <div style="position:absolute;left:96px;right:96px;top:230px;display:flex;justify-content:space-between">
    {''.join(f"""<div><img src="assets/{f}.jpg" style="width:260px;height:462px;display:block;object-fit:cover;outline:1px solid {P}55">
      <div class="label" style="font-size:12px;margin-top:22px">{t}</div><div class="serif it" style="font-size:24px;margin-top:6px;font-weight:300">{c}</div></div>""" for f, t, c in frames)}
  </div>
  {F('11.5 s · 1080×1920 + 4:5 cut · sound: knocks, whoosh, service bell')}
</section>''')

# 15 — Instagram profile
grid = [('img', POSTS + 'Post3_Reel_Cover_1080x1350.jpg'), ('img', POSTS + 'Post2_Served_By_Hand_1080x1350.jpg'),
        ('img', POSTS + 'Post1_Identity_Reveal_1080x1350.jpg'),
        ('html', f'<div class="center" style="background:{B};width:100%;height:100%">{logo("full", L, width=96)}</div>'),
        ('html', f'<div class="center" style="background:{P};width:100%;height:100%">{seal(R, 92)}</div>'),
        ('html', f'<div class="center" style="background:{O};width:100%;height:100%;color:{P}"><span class="serif it" style="font-size:19px">Served by hand.</span></div>'),
        ('html', f'<div class="center" style="background:{I};width:100%;height:100%">{logo("icon", R, width=80)}</div>'),
        ('html', f'<div class="center" style="background:{R};width:100%;height:100%;color:{P}"><span class="serif it" style="font-size:19px">Knock, knock.</span></div>'),
        ('html', f'<div class="center" style="background:{P};width:100%;height:100%">{door_static(60)}</div>')]
cells = ''.join(f'<div style="width:125px;height:156px;overflow:hidden">' + (f'<img src="{v}" style="width:125px;height:156px;object-fit:cover;display:block">' if t == 'img' else v) + '</div>' for t, v in grid)
hl = ''.join(f'''<div style="text-align:center"><div style="width:58px;height:74px;border-radius:29px 29px 0 0;background:{c}" class="center">{logo('icon', P, width=40)}</div><div style="font-size:11px;margin-top:6px">{n}</div></div>''' for n, c in [('Menu', R), ('Trays', B), ('Order', O), ('Love', L)])
phone = f'''<div style="width:430px;height:880px;border-radius:58px;background:#1d1512;padding:16px;box-shadow:24px 30px 0 rgba(60,18,14,.18)">
  <div style="width:100%;height:100%;border-radius:44px;background:#fff;overflow:hidden;position:relative;color:#111;font-family:'Jost'">
    <div style="padding:46px 22px 0;display:flex;align-items:center;justify-content:space-between"><b style="font-weight:500;font-size:17px">a.la.porte</b><span style="font-size:20px;letter-spacing:2px">···</span></div>
    <div style="padding:18px 22px 0;display:flex;align-items:center;gap:26px">
      <div style="width:86px;height:86px;border-radius:50%;background:{R};padding:4px;box-shadow:0 0 0 2px #fff, 0 0 0 4px {L}" class="center">{seal(P, 80, ring=False)}</div>
      <div style="display:flex;gap:22px;font-size:13px;text-align:center"><div><b style="font-weight:500;font-size:16px">9</b><br>posts</div><div><b style="font-weight:500;font-size:16px">—</b><br>followers</div><div><b style="font-weight:500;font-size:16px">—</b><br>following</div></div></div>
    <div style="padding:14px 22px 0;font-size:13.5px;line-height:1.45"><b style="font-weight:500">à la porte</b><br>A tray for everyday 🤍<br>Trays arranged by hand, delivered to your door.<br><span style="color:#5b4a8a">Order by DM</span></div>
    <div style="padding:16px 22px 14px;display:flex;gap:18px">{hl}</div>
    <div style="display:grid;grid-template-columns:repeat(3,125px);gap:2px;justify-content:center">{cells}</div>
  </div></div>'''
pages.append(f'''<section class="page" style="background:{P};color:{K}">
  {head('The <em>feed</em>', '14')}
  <div style="position:absolute;left:1340px;top:96px">{phone}</div>
  <div style="position:absolute;left:96px;top:300px;width:1050px">
    <p class="serif" style="font-size:58px;font-weight:300;line-height:1.1;color:{R}">A grid that reads like<br><em>a row of painted doors.</em></p>
    <p style="margin-top:30px;font-size:21px;line-height:1.65;font-weight:300">Alternate one photograph of a real tray with one graphic tile: a colour, a line, the seal. Photographs are always the client’s own trays in natural daylight, never stock or generated imagery. Story highlights sit inside arches, each with the hand.</p>
    <div style="margin-top:40px;display:flex;gap:16px">{''.join(f'<div style="width:70px;height:96px;border-radius:35px 35px 0 0;background:{c};box-shadow:inset 0 0 0 1px {R}66"></div>' for c in (R, P, B, I, O, R, L))}</div>
  </div>
  {F('Profile mockup · counts left blank on purpose')}
</section>''')

# 16 — Captions
caps = [('Nº 1 · The reveal', 'Same trays, a new door. ✨ Meet the new à la porte: a little more grace, the same love on every tray. A tray for everyday.',
         'نفس الصواني… بباب جديد. هوية جديدة لـ à la porte، بنفس الحب في كل صينية.'),
        ('Nº 2 · Served by hand', 'The hand in our new mark is the gesture behind every tray: arranged by hand, carried with care, presented at your door.',
         'الإيد اللي في اللوجو الجديد هي نفس الإيد اللي بترتّب كل صينية وتوصلها لحد بابك.'),
        ('Nº 3 · Knock, knock', 'Knock, knock. 🚪 Someone new is at the door. Sound on.',
         'تك تك… في حد جديد على الباب. شغّل الصوت.')]
pages.append(f'''<section class="page" style="background:{I};color:{K}">
  {head('Captions', '15')}
  <div style="position:absolute;left:96px;right:96px;top:250px;display:grid;grid-template-columns:repeat(3,1fr);gap:64px">
    {''.join(f"""<div><div class="label" style="font-size:13px;color:{R}">{t}</div><div class="rule" style="margin:18px 0 26px;color:{R}"></div>
      <p class="serif" style="font-size:31px;line-height:1.3;font-weight:300">{en}</p>
      <p style="margin-top:26px;font-size:22px;line-height:1.7;direction:rtl;text-align:right;font-family:'Noto Naskh Arabic','DejaVu Sans',sans-serif;opacity:.85">{ar}</p></div>""" for t, en, ar in caps)}
  </div>
  <div style="position:absolute;left:96px;right:96px;top:860px;font-size:18px;line-height:1.6;font-weight:300">
    <span class="label" style="font-size:12px;color:{R}">Hashtags</span>&nbsp;&nbsp; #alaporte #atrayforeveryday #newidentity #breakfasttray #grazingtray
  </div>
  {F('')}
</section>''')

# 17 — Close
pages.append(f'''<section class="page center" style="background:{R};color:{P};flex-direction:column">
  {door_static(300)}
  <div class="serif" style="font-size:54px;font-weight:300;margin-top:60px">See you <em>at the door.</em></div>
  <div class="folio" style="color:{P}"><span>À la porte</span><span>Brand identity · v1.0</span></div>
</section>''')

if __name__ == '__main__':
    open(os.path.join(HERE, 'identity.html'), 'w').write(page_html('À LA PORTE — Brand Identity', pages))
    print(len(pages), 'pages')
