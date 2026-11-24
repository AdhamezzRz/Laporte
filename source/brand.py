"""Shared brand system for À LA PORTE: logo symbols, palette, base CSS.

The logo vectors are taken unchanged from the designer's Illustrator file
(Option 3: Vladimir Script wordmark + slogan + hand-and-tray icon), recoloured
to the client's chosen terracotta.
"""
import os, re
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'logo_parts.py')).read())  # DEFS, WM, SL, IC

PALETTE = [
    # key, French name, role, hex
    ('rouge',     'Rouge Porte', 'Primary · the door',         '#B75548'),
    ('parchemin', 'Parchemin',   'Primary · the wall',          '#E2CDA1'),
    ('ivoire',    'Ivoire',      'Light ground · linen',        '#F5EEDF'),
    ('bordeaux',  'Bordeaux',    'Depth · evenings & gifting',  '#5C1F1A'),
    ('olive',     'Olive',       'Accent · garden & freshness', '#6F6B3B'),
    ('cafe',      'Café',        'Text · espresso',             '#2B1D18'),
    ('laiton',    'Laiton',      'Foil & special finishes',     '#B08D57'),
]
C = {k: h for k, _, _, h in PALETTE}

def rgb(h):
    h = h.lstrip('#'); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def cmyk(h):
    r, g, b = [v/255 for v in rgb(h)]
    k = 1 - max(r, g, b)
    if k == 1: return (0, 0, 0, 100)
    return tuple(round(100*v) for v in ((1-r-k)/(1-k), (1-g-k)/(1-k), (1-b-k)/(1-k), k))

# viewBoxes measured from the source artwork (units = PDF points)
VB = {
    'full':   (714, 414, 492, 291),     # wordmark + slogan + icon (primary)
    'word':   (720, 420, 480, 147),     # wordmark + slogan (horizontal)
    'script': (729, 429, 462, 126),     # wordmark only
    'icon':   (863.5, 577.5, 193, 117), # hand & tray
}
BODY = {'full': WM + SL + IC, 'word': WM + SL, 'script': WM, 'icon': IC}

def symbols():
    """One hidden SVG holding glyphs + logo symbols, referenced with <use>."""
    syms = ''.join(
        f'<symbol id="lp-{k}" viewBox="{" ".join(map(str, VB[k]))}" overflow="visible">{BODY[k]}</symbol>'
        for k in VB)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'width="0" height="0" style="position:absolute"><defs>{DEFS}{syms}</defs></svg>')

def logo(kind='full', color='#B75548', width=None, height=None, cls='', style=''):
    x, y, w, h = VB[kind]
    if width and not height: height = width * h / w
    if height and not width: width = height * w / h
    return (f'<svg class="lp {cls}" style="{style}" width="{width:.1f}" height="{height:.1f}" '
            f'viewBox="0 0 {w} {h}" fill="{color}" xmlns="http://www.w3.org/2000/svg" '
            f'xmlns:xlink="http://www.w3.org/1999/xlink"><use href="#lp-{kind}" xlink:href="#lp-{kind}" '
            f'width="{w}" height="{h}"/></svg>')

def standalone_svg(kind, color):
    x, y, w, h = VB[kind]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" '
            f'viewBox="{x} {y} {w} {h}" width="{w*4:.0f}" height="{h*4:.0f}"><defs>{DEFS}</defs>'
            f'<g fill="{color}">{BODY[kind]}</g></svg>')

FONTS = open(os.path.join(HERE, 'fonts_local.css')).read()

BASE_CSS = FONTS + f"""
*{{box-sizing:border-box;margin:0;padding:0}}
html,body{{background:{C['parchemin']}}}
body{{font-family:'Jost',sans-serif;color:{C['cafe']};-webkit-font-smoothing:antialiased}}
.page{{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;break-after:page}}
.page:last-child{{page-break-after:auto}}
.center{{display:flex;align-items:center;justify-content:center}}
.label{{font-family:'Jost';font-weight:400;font-size:15px;letter-spacing:.42em;text-transform:uppercase}}
.serif{{font-family:'Cormorant Garamond',serif}}
.it{{font-style:italic}}
.folio{{position:absolute;left:96px;right:96px;bottom:56px;display:flex;justify-content:space-between;
  font-family:'Jost';font-size:13px;letter-spacing:.38em;text-transform:uppercase;opacity:.75}}
.head{{position:absolute;left:96px;top:84px;right:96px;display:flex;justify-content:space-between;align-items:baseline}}
.head h2{{font-family:'Cormorant Garamond';font-weight:300;font-size:64px;letter-spacing:-.01em;line-height:1}}
.head h2 em{{font-style:italic}}
.head .label{{opacity:.8}}
.rule{{height:1px;background:currentColor;opacity:.35}}
"""

def page_html(title, pages, extra_css=''):
    return (f'<!doctype html><html><head><meta charset="utf-8"><title>{title}</title>'
            f'<style>{BASE_CSS}{extra_css}@page{{size:1920px 1080px;margin:0}}</style></head>'
            f'<body>{symbols()}{"".join(pages)}</body></html>')

def folio(left, right, color=None):
    st = f' style="color:{color}"' if color else ''
    return f'<div class="folio"{st}><span>{left}</span><span>{right}</span></div>'
