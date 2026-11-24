"""Flat vector arched door — the brand's 'porte'. Drawn in palette colours.

Local coordinates: the full door unit is 600 x 940.
Doorway opening: x 70..530, y 70..900 (arch radius 230, centre (300,300)).
Each leaf is 230 x 830 in its own coordinates.
"""
from brand import C, logo

FRAME = '#D3B985'      # moulding: Parchemin, one step deeper
FRAME_LINE = '#C2A673'
PANEL = '#9C4438'      # Rouge Porte, one step deeper (panel recesses)

LEAF_PATH = 'M0,830 V230 A230,230 0 0 1 230,0 V830 Z'

def leaf_svg(mirror=False, width=None):
    """One door leaf (left by default). Right leaf = mirrored."""
    t = 'transform="translate(230,0) scale(-1,1)"' if mirror else ''
    knob_x = 206
    return f'''<svg viewBox="0 0 230 830" width="{width or 230}" xmlns="http://www.w3.org/2000/svg" style="display:block;overflow:visible">
  <g {t}>
    <path d="{LEAF_PATH}" fill="{C['rouge']}"/>
    <path d="M32,470 V230 A198,198 0 0 1 200,34.3 V470 Z" fill="none" stroke="{PANEL}" stroke-width="4"/>
    <path d="M46,456 V232 A184,184 0 0 1 186,52 V456 Z" fill="none" stroke="{PANEL}" stroke-width="1.6" opacity=".7"/>
    <rect x="32" y="500" width="168" height="300" fill="none" stroke="{PANEL}" stroke-width="4"/>
    <rect x="46" y="514" width="140" height="272" fill="none" stroke="{PANEL}" stroke-width="1.6" opacity=".7"/>
    <circle cx="{knob_x}" cy="485" r="9" fill="{C['laiton']}"/>
    <circle cx="{knob_x}" cy="485" r="9" fill="none" stroke="#8C6C3C" stroke-width="1.5"/>
    <line x1="229" y1="0" x2="229" y2="830" stroke="{PANEL}" stroke-width="3"/>
  </g>
</svg>'''

def frame_svg(interior=None, mat=True, extra=''):
    """Wall moulding + step + dark interior (leaves are layered on top separately)."""
    interior = interior or C['bordeaux']
    mat_logo = ''
    if mat:
        mat_logo = f'''<rect x="190" y="902" width="220" height="30" rx="2" fill="{C['rouge']}"/>
        <foreignObject x="190" y="902" width="220" height="30"><div xmlns="http://www.w3.org/1999/xhtml" style="display:flex;align-items:center;justify-content:center;height:30px">{logo('script', C['parchemin'], height=19)}</div></foreignObject>'''
    return f'''<svg viewBox="0 0 600 940" xmlns="http://www.w3.org/2000/svg" style="display:block;overflow:visible" width="100%" height="100%">
  <path d="M30,900 V300 A270,270 0 0 1 570,300 V900 Z" fill="{FRAME}"/>
  <path d="M30,900 V300 A270,270 0 0 1 570,300 V900" fill="none" stroke="{FRAME_LINE}" stroke-width="2"/>
  <path d="M52,900 V300 A248,248 0 0 1 548,300 V900" fill="none" stroke="{FRAME_LINE}" stroke-width="1.5"/>
  <path d="M276,32 L324,32 L316,78 L284,78 Z" fill="{FRAME}" stroke="{FRAME_LINE}" stroke-width="2"/>
  <path d="M70,900 V300 A230,230 0 0 1 530,300 V900 Z" fill="{interior}"/>
  {extra}
  <rect x="0" y="898" width="600" height="42" fill="{FRAME}"/>
  <line x1="0" y1="898" x2="600" y2="898" stroke="{FRAME_LINE}" stroke-width="2"/>
  {mat_logo}
</svg>'''

def door_static(width):
    """Closed door, for static layouts. Returns positioned HTML (width px)."""
    s = width / 600
    return f'''<div style="position:relative;width:{width}px;height:{940*s}px">
  <div style="position:absolute;inset:0">{frame_svg()}</div>
  <div style="position:absolute;left:{70*s}px;top:{70*s}px;width:{230*s}px">{leaf_svg(False, 230*s)}</div>
  <div style="position:absolute;left:{300*s}px;top:{70*s}px;width:{230*s}px">{leaf_svg(True, 230*s)}</div>
</div>'''
