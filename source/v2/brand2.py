"""À LA PORTE — final visual identity (client-approved): logo option 1,
burgundy palette, Cormorant Garamond / Acumin (Inter stand-in) / Vladimir Script."""
import os
HERE = os.path.dirname(os.path.abspath(__file__))
exec(open(os.path.join(HERE, 'logo1_paths.py')).read())   # ICON, WORD (outlined from the identity PDF)

OX, BU, WI, CR = '#3b000c', '#550b18', '#76152d', '#f2e5c5'   # oxblood, burgundy, wine, cream
BRASS = '#c9a46a'   # tiny accent only (bell, foil-like details)

VB = {'full': (790, 359, 340, 362), 'word': (795, 359, 330, 158), 'icon': (790, 525, 340, 196)}

def symbols():
    body = {'full': ''.join(f'<path d="{d}"/>' for d in [ICON] + WORD),
            'word': ''.join(f'<path d="{d}"/>' for d in WORD),
            'icon': f'<path d="{ICON}"/>'}
    syms = ''.join(f'<symbol id="L-{k}" viewBox="{" ".join(map(str, VB[k]))}">{body[k]}</symbol>' for k in VB)
    return f'<svg width="0" height="0" style="position:absolute"><defs>{syms}</defs></svg>'

def logo(kind='full', color=CR, width=None, height=None, style='', cls=''):
    x, y, w, h = VB[kind]
    if width and not height: height = width * h / w
    if height and not width: width = height * w / h
    return (f'<svg class="{cls}" style="{style}" width="{width:.1f}" height="{height:.1f}" viewBox="0 0 {w} {h}" '
            f'fill="{color}"><use href="#L-{kind}" width="{w}" height="{h}"/></svg>')

def standalone(kind, color):
    x, y, w, h = VB[kind]
    paths = [ICON] + WORD if kind == 'full' else (WORD if kind == 'word' else [ICON])
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{x} {y} {w} {h}" width="{w*4}" height="{h*4}">'
            f'<g fill="{color}">{"".join(f"<path d=\"{d}\"/>" for d in paths)}</g></svg>')

# ---- hand-drawn doodles (stroke) ----
def sparkle(size, color, sw=3, rot=0):
    return (f'<svg width="{size}" height="{size}" viewBox="-50 -50 100 100" style="transform:rotate({rot}deg);overflow:visible">'
            f'<path d="M0,-46 C3,-14 8,-6 46,0 C9,5 3,13 0,46 C-4,14 -9,5 -46,0 C-8,-5 -3,-13 0,-46 Z" fill="none" stroke="{color}" '
            f'stroke-width="{sw}" stroke-linejoin="round"/></svg>')

def heart(size, color, sw=3, rot=0):
    return (f'<svg width="{size}" height="{size}" viewBox="0 0 100 90" style="transform:rotate({rot}deg);overflow:visible">'
            f'<path d="M50,84 C30,66 6,52 6,30 C6,14 18,5 30,6 C40,7 47,14 50,24 C53,13 61,5 72,6 C85,7 95,17 93,32 '
            f'C91,52 68,66 51,85" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/></svg>')

def squiggle(w, color, sw=3):
    return (f'<svg width="{w}" height="{w*0.12}" viewBox="0 0 300 36" preserveAspectRatio="none" style="overflow:visible">'
            f'<path d="M4,22 C30,4 46,34 72,18 C98,2 112,32 140,18 C166,5 182,30 208,17 C232,6 250,28 296,12" fill="none" '
            f'stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/></svg>')

def arrow(w, color, sw=3, flip=False):
    t = 'transform:scaleX(-1);' if flip else ''
    return (f'<svg width="{w}" height="{w*0.7}" viewBox="0 0 140 100" style="{t}overflow:visible">'
            f'<path d="M8,16 C36,74 82,90 124,66" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round"/>'
            f'<path d="M104,56 L126,65 L112,85" fill="none" stroke="{color}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/></svg>')

FONT_DIR = os.path.join(os.path.dirname(HERE), 'fonts')
FONTS = f"""
@font-face{{font-family:'Vladimir';src:url(../fonts/VladimirScript-fixed.ttf) format('truetype');}}
@font-face{{font-family:'CormB';src:url(../fonts/CormorantGaramond-Bold-fixed.ttf) format('truetype');font-weight:700;}}
@font-face{{font-family:'Corm';font-style:normal;font-weight:500;src:url(../fonts/CormorantGaramond-500.woff2) format('woff2');}}
@font-face{{font-family:'Corm';font-style:italic;font-weight:500;src:url(../fonts/CormorantGaramond-500i.woff2) format('woff2');}}
@font-face{{font-family:'Corm';font-style:normal;font-weight:600;src:url(../fonts/CormorantGaramond-600.woff2) format('woff2');}}
@font-face{{font-family:'Corm';font-style:italic;font-weight:400;src:url(../fonts/CormorantGaramond-400i.woff2) format('woff2');}}
"""

CSS = FONTS + f"""
*{{margin:0;padding:0;box-sizing:border-box}}
body{{background:#777;-webkit-font-smoothing:antialiased}}
.post{{width:1080px;height:1350px;position:relative;overflow:hidden;margin-bottom:40px}}
.abs{{position:absolute}}
.script{{font-family:'Vladimir',cursive;font-weight:400;line-height:1}}
.cb{{font-family:'CormB',serif;font-weight:700;line-height:.9;letter-spacing:-.01em}}
.ci{{font-family:'Corm',serif;font-style:italic;font-weight:500}}
.sans{{font-family:'Inter',sans-serif;font-weight:500;letter-spacing:.34em;text-transform:uppercase}}
.grain{{position:absolute;inset:0;pointer-events:none;opacity:.14;mix-blend-mode:overlay}}
.center{{display:flex;align-items:center;justify-content:center}}
"""

GRAIN = ('<svg class="grain" width="100%" height="100%"><filter id="gr"><feTurbulence type="fractalNoise" '
         'baseFrequency=".9" numOctaves="3" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter>'
         '<rect width="100%" height="100%" filter="url(#gr)"/></svg>')
