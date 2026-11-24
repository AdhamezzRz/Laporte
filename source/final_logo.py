"""Builds 01_Final_Logo/ALaPorte_Final_Logo.html (rendered to PDF by render.js)."""
from brand import *

R, P, I, B, O, K, L = (C[k] for k in ('rouge', 'parchemin', 'ivoire', 'bordeaux', 'olive', 'cafe', 'laiton'))

_seal_n = [0]
def seal(color, size, ring=True):
    """Circular seal: hand & tray icon inside a ring of tracked type."""
    _seal_n[0] += 1; pid = f'sealpath{_seal_n[0]}'
    r = 150
    txt = '· À LA PORTE · A TRAY FOR EVERYDAY · À LA PORTE · A TRAY FOR EVERYDAY'
    ix, iy, iw, ih = VB['icon']
    icon_w = 190
    return f'''<svg width="{size}" height="{size}" viewBox="-200 -200 400 400" fill="{color}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs><path id="{pid}" d="M 0,0 m -{r},0 a {r},{r} 0 1,1 {2*r},0 a {r},{r} 0 1,1 -{2*r},0"/></defs>
  {'<circle r="188" fill="none" stroke="'+color+'" stroke-width="2.2"/><circle r="118" fill="none" stroke="'+color+'" stroke-width="1.2"/>' if ring else ''}
  <text font-family="Jost" font-weight="400" font-size="20"><textPath href="#{pid}" xlink:href="#{pid}" startOffset="2" textLength="{2*3.14159*r-24:.1f}" lengthAdjust="spacing">{txt}</textPath></text>
  <use href="#lp-icon" xlink:href="#lp-icon" x="{-icon_w/2}" y="{-icon_w*ih/iw/2 + 4}" width="{icon_w}" height="{icon_w*ih/iw}"/>
</svg>'''

def solo(bg, fg, label, sub, logo_w=880, folio_l='À la porte — Final logo', folio_r=''):
    return f'''<section class="page center" style="background:{bg};color:{fg}">
  <div class="head"><span class="label">{label}</span><span class="label">{sub}</span></div>
  {logo('full', fg, width=logo_w)}
  {folio(folio_l, folio_r)}
</section>'''

pages = []

# 1 — Cover
pages.append(f'''<section class="page" style="background:{P};color:{R}">
  <div class="head"><span class="label">Final logo &amp; colour</span><span class="label">Nouvelle identité</span></div>
  <div class="center" style="position:absolute;inset:0">{logo('full', R, width=980)}</div>
  {folio('À la porte', 'MMXXVI')}
</section>''')

# 2 — Intro statement
pages.append(f'''<section class="page" style="background:{R};color:{P}">
  <div class="head"><span class="label">The brief</span><span class="label">01</span></div>
  <div style="position:absolute;left:96px;top:300px;width:1180px">
    <p class="serif" style="font-weight:300;font-size:92px;line-height:1.02;letter-spacing:-.015em">The <em>script</em> of option three,<br>the <em>colour</em> of the door.</p>
    <p style="margin-top:56px;font-size:24px;line-height:1.6;max-width:880px;font-weight:300;opacity:.92">
      The final mark keeps the hand-written wordmark and the slogan exactly as drawn: <em class="serif" style="font-size:28px">à la porte — A TRAY FOR EVERYDAY</em>, with the hand presenting the tray.
      It is now set in <b style="font-weight:500">Rouge Porte</b> on <b style="font-weight:500">Parchemin</b>: a warm terracotta on a sun-washed cream, like a painted door in a plaster wall.</p>
  </div>
  <div style="position:absolute;right:120px;bottom:150px">{logo('icon', P, width=360)}</div>
  {folio('À la porte — Final logo', '')}
</section>''')

# 3 — Primary
pages.append(solo(P, R, 'Primary logo', 'Rouge Porte on Parchemin', 900, folio_r='02'))
# 4 — Reversed
pages.append(solo(R, P, 'Primary logo — reversed', 'Parchemin on Rouge Porte', 900, folio_r='03'))
# 5 — Bordeaux
pages.append(solo(B, P, 'Primary logo — evening', 'Parchemin on Bordeaux', 900, folio_r='04'))

# 6 — Colourways grid
def tile(bg, fg, name, note):
    return f'''<div style="background:{bg};color:{fg};position:relative" class="center">
      {logo('full', fg, width=430)}
      <div class="label" style="position:absolute;left:36px;bottom:30px;font-size:12px;opacity:.85">{name}</div>
      <div class="label" style="position:absolute;right:36px;bottom:30px;font-size:12px;opacity:.85">{note}</div></div>'''
pages.append(f'''<section class="page" style="background:{I};color:{K}">
  <div style="position:absolute;inset:0;display:grid;grid-template-columns:1fr 1fr 1fr;grid-template-rows:1fr 1fr">
    {tile(I, R, 'Rouge on Ivoire', 'Packaging · menus')}
    {tile(O, P, 'Parchemin on Olive', 'Seasonal')}
    {tile(B, L, 'Laiton on Bordeaux', 'Foil · gifting')}
    {tile(P, K, 'Café on Parchemin', 'One colour')}
    {tile(R, I, 'Ivoire on Rouge', 'Social')}
    {tile(K, P, 'Parchemin on Café', 'Night')}
  </div>
</section>''')

# 7 — Anatomy
pages.append(f'''<section class="page" style="background:{P};color:{R}">
  <div class="head"><span class="label">Anatomy</span><span class="label">05</span></div>
  <div class="center" style="position:absolute;left:0;top:0;bottom:0;width:1150px">{logo('full', R, width=820)}</div>
  <div style="position:absolute;left:1180px;top:290px;width:620px;color:{K}">
    {''.join(f"""<div style="display:flex;gap:28px;padding:30px 0;border-top:1px solid {R}55">
      <div class="serif it" style="font-size:44px;color:{R};width:60px;line-height:1">{n}</div>
      <div><div class="label" style="color:{R};font-size:14px">{t}</div>
      <p style="margin-top:12px;font-size:20px;line-height:1.55;font-weight:300">{d}</p></div></div>""" for n, t, d in [
      ('i.', 'The wordmark', 'Hand-lettered script in the spirit of a written invitation. Always used as artwork, never re-typed.'),
      ('ii.', 'The slogan', 'A TRAY FOR EVERYDAY: tracked capitals tucked beneath the script, as drawn. The descender of the p threads through it.'),
      ('iii.', 'The hand', 'The maître d’s gesture. A gloved hand presents the tray, the brand’s promise of service at your door.')])}
  </div>
  {folio('À la porte — Final logo', '')}
</section>''')

# 8 — Variations
def var(content, name):
    return f'''<div style="display:flex;flex-direction:column;align-items:center;justify-content:space-between;height:520px">
      <div class="center" style="flex:1">{content}</div>
      <div class="label" style="font-size:13px;color:{K};opacity:.8">{name}</div></div>'''
pages.append(f'''<section class="page" style="background:{I};color:{R}">
  <div class="head"><span class="label">Logo family</span><span class="label">06</span></div>
  <div style="position:absolute;left:96px;right:96px;top:290px;display:grid;grid-template-columns:1.25fr 1.25fr 1fr 1fr;gap:60px">
    {var(logo('full', R, width=400), 'Primary · stacked')}
    {var(logo('word', R, width=420), 'Secondary · wordmark')}
    {var(logo('icon', R, width=240), 'Icon · the hand')}
    {var(seal(R, 300), 'Seal · stickers &amp; stamps')}
  </div>
  {folio('À la porte — Final logo', 'Use the primary logo wherever space allows')}
</section>''')

# 9 — Clear space & minimum size
ax, ay, aw, ah = 734.25, 434.11, 451.5, 250.51   # artwork bbox
X = 14.72                                          # cap height of the slogan
s = 1.45; pad = 3 * X * s
w, h = aw * s, ah * s
pages.append(f'''<section class="page" style="background:{P};color:{R}">
  <div class="head"><span class="label">Clear space &amp; minimum size</span><span class="label">07</span></div>
  <div style="position:absolute;left:150px;top:250px;width:{w+2*pad}px;height:{h+2*pad}px;border:1.5px dashed {R}aa">
    <div style="position:absolute;inset:{pad}px;outline:1px solid {R}44">
      <svg width="{w}" height="{h}" viewBox="{ax} {ay} {aw} {ah}" fill="{R}"><use href="#lp-full" x="{VB['full'][0]}" y="{VB['full'][1]}" width="{VB['full'][2]}" height="{VB['full'][3]}"/></svg>
    </div>
    {''.join(f'<div style="position:absolute;{pos};width:{pad}px;height:{pad}px;background:{R}22" class="center"><span class="serif it" style="font-size:30px">3x</span></div>' for pos in ['left:0;top:0', f'right:0;top:0', 'left:0;bottom:0', 'right:0;bottom:0'])}
  </div>
  <div style="position:absolute;left:1120px;top:280px;width:700px;color:{K}">
    <p class="serif" style="font-size:44px;font-weight:300;line-height:1.15;color:{R}">Give it room to breathe.</p>
    <p style="margin-top:22px;font-size:20px;line-height:1.6;font-weight:300">Keep a clear space of <b style="font-weight:500">3x</b> on every side, where <b style="font-weight:500">x</b> is the cap height of the slogan. No text, edges or images enter this zone.</p>
    <div class="rule" style="margin:48px 0 40px;color:{R}"></div>
    <div style="display:flex;gap:56px;align-items:flex-end">
      <div>{logo('full', R, width=120)}<div class="label" style="font-size:12px;margin-top:16px">Primary · 30 mm / 120 px</div></div>
      <div>{logo('word', R, width=110)}<div class="label" style="font-size:12px;margin-top:16px">Wordmark · 28 mm / 110 px</div></div>
      <div>{logo('icon', R, width=40)}<div class="label" style="font-size:12px;margin-top:16px">Icon · 10 mm / 40 px</div></div>
    </div>
  </div>
  {folio('À la porte — Final logo', '')}
</section>''')

# 10 — Palette
def sw(key, name, role, hx, flex):
    r, g, b = rgb(hx); c, m, y, k = cmyk(hx)
    light = key in ('parchemin', 'ivoire', 'laiton')
    fg = K if light else I
    bd = f'box-shadow:inset 0 0 0 1px {C["parchemin"]};' if key=='ivoire' else ''
    return f'''<div style="flex:{flex};background:{hx};color:{fg};position:relative;padding:44px 32px;{bd}">
      <div class="serif" style="font-size:{46 if flex>1 else 34}px;font-weight:400;line-height:1">{name}</div>
      <div style="font-size:15px;margin-top:12px;opacity:.85;font-weight:300">{role}</div>
      <div style="position:absolute;left:32px;bottom:40px;font-size:15px;line-height:1.9;letter-spacing:.06em">
        <div><b style="font-weight:500">HEX</b>&nbsp; {hx.upper()}</div><div><b style="font-weight:500">RGB</b>&nbsp; {r} {g} {b}</div><div><b style="font-weight:500">CMYK</b>&nbsp; {c} {m} {y} {k}</div></div></div>'''
pages.append(f'''<section class="page" style="background:{I};color:{K}">
  <div class="head" style="color:{R}"><h2>La <em>palette</em></h2><span class="label">08</span></div>
  <div style="position:absolute;left:96px;right:96px;top:220px;bottom:150px;display:flex;gap:0">
    {''.join(sw(k, n, r_, h_, 1.7 if k in ('rouge', 'parchemin') else 1) for k, n, r_, h_ in PALETTE)}
  </div>
  {folio('Primary: Rouge Porte + Parchemin · Laiton for foil only', 'CMYK: proof on press')}
</section>''')

# 11 — Colour proportion
pages.append(f'''<section class="page" style="background:{P};color:{K}">
  <div class="head" style="color:{R}"><h2>In <em>proportion</em></h2><span class="label">09</span></div>
  <div style="position:absolute;left:96px;right:96px;top:250px;height:120px;display:flex">
    <div style="flex:45;background:{P};outline:1px solid {R}55"></div><div style="flex:25;background:{R}"></div><div style="flex:12;background:{I}"></div>
    <div style="flex:8;background:{B}"></div><div style="flex:5;background:{O}"></div><div style="flex:4;background:{K}"></div><div style="flex:1;background:{L}"></div></div>
  <div style="position:absolute;left:96px;right:96px;top:390px;display:flex;font-size:14px;letter-spacing:.2em;text-transform:uppercase">
    <div style="flex:45">Parchemin 45%</div><div style="flex:25">Rouge 25%</div><div style="flex:12">Ivoire 12%</div><div style="flex:8">Bord. 8</div><div style="flex:5">Ol. 5</div><div style="flex:4"></div><div style="flex:1"></div></div>
  <div style="position:absolute;left:96px;top:520px;width:1100px">
    <p class="serif" style="font-size:52px;font-weight:300;line-height:1.12;color:{R}">Mostly wall, some door, and a little garden.</p>
    <p style="margin-top:24px;font-size:21px;line-height:1.65;font-weight:300;max-width:900px">Parchemin and Ivoire carry the space. Rouge Porte is the voice: the logo, a headline, a ribbon. Bordeaux and Olive add depth and seasonality; Café is for reading. Laiton appears only as foil, never as flat ink.</p>
  </div>
  <div style="position:absolute;right:140px;top:560px">{seal(R, 320)}</div>
  {folio('À la porte — Final logo', '')}
</section>''')

# 12 — Typography
pages.append(f'''<section class="page" style="background:{I};color:{K}">
  <div class="head" style="color:{R}"><h2><em>Typography</em></h2><span class="label">10</span></div>
  <div style="position:absolute;left:96px;right:96px;top:250px;display:grid;grid-template-columns:1fr 1fr 1fr;gap:72px">
    <div><div class="label" style="color:{R};font-size:13px">Logotype</div><div class="rule" style="margin:18px 0 34px;color:{R}"></div>
      {logo('script', R, width=440)}
      <p style="margin-top:36px;font-size:18px;line-height:1.6;font-weight:300">Vladimir Script, outlined as artwork. Reserved for the logo; it is never typed out for headlines.</p></div>
    <div><div class="label" style="color:{R};font-size:13px">Display — Cormorant Garamond</div><div class="rule" style="margin:18px 0 20px;color:{R}"></div>
      <div class="serif" style="font-size:150px;font-weight:300;line-height:1;color:{R}">Aa <em>Aa</em></div>
      <p class="serif" style="margin-top:20px;font-size:34px;font-weight:300;line-height:1.2">Breakfast at your door, <em>served like a ritual.</em></p>
      <p style="margin-top:20px;font-size:18px;line-height:1.6;font-weight:300">Light &amp; Light Italic for headlines and menu names. Mix roman and italic within a line for warmth.</p></div>
    <div><div class="label" style="color:{R};font-size:13px">Text — Jost</div><div class="rule" style="margin:18px 0 20px;color:{R}"></div>
      <div style="font-size:150px;font-weight:300;line-height:1;color:{R}">Aa</div>
      <p style="margin-top:28px;font-size:16px;letter-spacing:.42em;text-transform:uppercase">A tray for everyday</p>
      <p style="margin-top:20px;font-size:18px;line-height:1.6;font-weight:300">Light &amp; Regular for body copy, captions and labels. Labels in capitals, tracked +400, echoing the slogan.</p></div>
  </div>
  {folio('Cormorant Garamond &amp; Jost are free Google Fonts', '')}
</section>''')

# 13 — Misuse
def bad(inner, bg, cap):
    return f'''<div><div class="center" style="background:{bg};height:300px;position:relative;overflow:hidden">{inner}
      <svg width="44" height="44" viewBox="0 0 44 44" style="position:absolute;right:18px;top:18px"><circle cx="22" cy="22" r="21" fill="{I}" stroke="{R}"/><path d="M14 14 L30 30 M30 14 L14 30" stroke="{R}" stroke-width="2"/></svg></div>
      <div class="label" style="font-size:12px;margin-top:18px;letter-spacing:.3em">{cap}</div></div>'''
pages.append(f'''<section class="page" style="background:{P};color:{K}">
  <div class="head" style="color:{R}"><h2>Please, <em>don’t</em></h2><span class="label">11</span></div>
  <div style="position:absolute;left:96px;right:96px;top:230px;display:grid;grid-template-columns:repeat(3,1fr);gap:40px 48px">
    {bad(logo('full', R, width=300, style='transform:scaleX(1.45)'), I, 'Stretch or squash')}
    {bad(logo('full', '#2E6FD8', width=300), I, 'Use off-palette colours')}
    {bad(logo('full', R, width=300, style='transform:rotate(-14deg)'), I, 'Rotate or tilt')}
    {bad(logo('full', R, width=300, style=f'filter:drop-shadow(6px 8px 4px rgba(0,0,0,.45))'), I, 'Add shadows or effects')}
    {bad(logo('full', O, width=300), R, 'Place on low contrast')}
    {bad(f'<div class="serif it" style="font-size:72px;color:{R}">à la porte</div>', I, 'Re-type the wordmark')}
  </div>
  {folio('À la porte — Final logo', '')}
</section>''')

# 14 — Close
pages.append(f'''<section class="page center" style="background:{R};color:{P};flex-direction:column">
  {logo('full', P, width=620)}
  <div class="serif it" style="font-size:40px;font-weight:300;margin-top:70px">Merci.</div>
  {folio('À la porte', 'Final logo · v1.0')}
</section>''')

if __name__ == '__main__':
    out = os.path.join(HERE, 'final_logo.html')
    open(out, 'w').write(page_html('À LA PORTE — Final Logo', pages))
    print(out)
