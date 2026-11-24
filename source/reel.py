"""Animated post (Reel, 1080 x 1920): 'Knock, knock' — the new identity at your door.

Writes reel.html exposing window.setTime(t). reel_render.js steps it frame by frame.
All key content stays inside the 4:5 grid crop (y 285..1635).
"""
from brand import *
from door import frame_svg, leaf_svg

R, P, I, B, O, K, L = (C[k] for k in ('rouge', 'parchemin', 'ivoire', 'bordeaux', 'olive', 'cafe', 'laiton'))

W, H = 1080, 1920
# Final logo geometry
LW = 860; k = LW / VB['full'][2]; LX = (W - LW) / 2; LT = 600
ICON = dict(left=LX + (VB['icon'][0] - VB['full'][0]) * k, top=LT + (VB['icon'][1] - VB['full'][1]) * k,
            width=VB['icon'][2] * k)
# Door geometry: local (300,600) sits on the icon centre
DS = 700 / 600; DL = 540 - 300 * DS
icon_cy = ICON['top'] + VB['icon'][3] * k / 2
DT = icon_cy - 600 * DS
ORX, ORY = 540, DT + 485 * DS       # zoom origin = doorway centre
DOOR_BOTTOM = DT + 900 * DS

import re
def glyph_uses(markup, cls):
    i = [0]
    def rep(m):
        i[0] += 1
        return f'<use class="{cls}" data-i="{i[0]-1}" '
    return re.sub(r'<use ', rep, markup)

extra = (f'<defs><radialGradient id="glow" cx="50%" cy="62%" r="60%"><stop offset="0" stop-color="#F3D9A4"/>'
         f'<stop offset=".45" stop-color="{L}"/><stop offset="1" stop-color="{B}" stop-opacity="0"/></radialGradient></defs>'
         f'<path id="glowp" d="M70,900 V300 A230,230 0 0 1 530,300 V900 Z" fill="url(#glow)" opacity="0"/>'
         f'<path id="rougep" d="M70,900 V300 A230,230 0 0 1 530,300 V900 Z" fill="{R}" opacity="0"/>')

fx, fy, fw, fh = VB['full']
html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{BASE_CSS}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{P}}}
#stage{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;overflow:hidden;background:{P}}}
#bgR{{position:absolute;inset:0;background:{R};opacity:0}}
#scene{{position:absolute;left:0;top:0;width:{W}px;height:{H}px;transform-origin:{ORX}px {ORY}px}}
#door{{position:absolute;left:{DL}px;top:{DT}px;width:{600*DS}px;height:{940*DS}px;perspective:2200px}}
#frame{{position:absolute;inset:0}}
.leaf{{position:absolute;top:{70*DS}px;width:{230*DS}px;height:{830*DS}px}}
#leafL{{left:{70*DS}px;transform-origin:0 50%}}
#leafR{{left:{300*DS}px;transform-origin:100% 50%}}
#iconwrap{{position:absolute;left:0;top:0;width:{W}px;height:{H}px}}
#icon{{position:absolute;left:{ICON['left']}px;top:{ICON['top']}px}}
#logo{{position:absolute;left:{LX}px;top:{LT}px;width:{LW}px;height:{fh*k}px}}
#wm{{position:absolute;inset:0}}
.txt{{position:absolute;left:0;right:0;text-align:center;opacity:0}}
#grain{{position:absolute;inset:0;opacity:.17;mix-blend-mode:multiply;pointer-events:none}}
#vig{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 45%,rgba(0,0,0,0) 55%,rgba(60,20,15,.18) 100%)}}
</style></head><body>{symbols()}
<div id="stage">
  <div id="bgR"></div>
  <div id="scene">
    <div id="door">
      <div id="frame">{frame_svg(extra=extra)}</div>
      <div class="leaf" id="leafL">{leaf_svg(False, 230*DS)}</div>
      <div class="leaf" id="leafR">{leaf_svg(True, 230*DS)}</div>
    </div>
  </div>
  <div id="iconwrap"><div id="icon">{logo('icon', P, width=ICON['width'])}</div></div>
  <div id="logo">
    <svg id="wm" viewBox="{fx} {fy} {fw} {fh}" fill="{P}" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g>{glyph_uses(WM, 'gw')}</g></svg>
    <svg id="sl" viewBox="{fx} {fy} {fw} {fh}" fill="{P}" style="position:absolute;inset:0" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><g>{glyph_uses(SL, 'gs')}</g></svg>
  </div>
  <div class="txt label" id="knock" style="top:{DOOR_BOTTOM+70}px;color:{R};font-size:0">
    <span class="serif it" id="k1" style="font-size:64px;letter-spacing:0;text-transform:none;opacity:0">Knock,</span>
    <span class="serif it" id="k2" style="font-size:64px;letter-spacing:0;text-transform:none;opacity:0">&nbsp;knock.</span></div>
  <div class="txt label" id="top" style="top:330px;color:{P};font-size:18px">Nouvelle identité &nbsp;·&nbsp; MMXXVI</div>
  <div class="txt" id="tag" style="top:{LT+fh*k+70}px;color:{P}"><span class="serif" style="font-size:58px;font-weight:300">A new look, <em>at your door.</em></span></div>
  <div class="txt label" id="handle" style="top:1530px;color:{P};font-size:21px;text-transform:none;letter-spacing:.3em">@a.la.porte</div>
  <svg id="grain" width="100%" height="100%" xmlns="http://www.w3.org/2000/svg"><filter id="gf"><feTurbulence id="turb" type="fractalNoise" baseFrequency=".8" numOctaves="3" seed="1" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 .17  0 0 0 0 .11  0 0 0 0 .09  0 0 0 .55 0"/></filter><rect width="100%" height="100%" filter="url(#gf)"/></svg>
  <div id="vig"></div>
</div>
<script>
const $=id=>document.getElementById(id);
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const seg=(t,a,b)=>clamp((t-a)/(b-a));
const eIO=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const eO=x=>1-Math.pow(1-x,3);
const eIOq=x=>x<.5?8*x*x*x*x:1-Math.pow(-2*x+2,4)/2;
const lerp=(a,b,x)=>a+(b-a)*x;
const gw=[...document.querySelectorAll('.gw')], gs=[...document.querySelectorAll('.gs')];
const DUR=11.5;
window.DUR=DUR;
window.setTime=function(t, frame){{
  // door entrance
  const a=eO(seg(t,0,.6));
  $('door').style.opacity=a;
  // knocks: shake
  let sh=0; for(const k of [.55,1.05]){{ const d=t-k; if(d>=0&&d<.28) sh+=Math.sin(d*90)*7*Math.exp(-d*16); }}
  const zoom=lerp(1,7.5,eIOq(seg(t,3.35,5.05)));
  const enter=lerp(.965,1,a);
  $('scene').style.transform=`translateX(${{sh}}px) scale(${{zoom*enter}})`;
  $('k1').style.opacity=eO(seg(t,.55,.8))*(1-seg(t,1.7,2.1));
  $('k2').style.opacity=eO(seg(t,1.05,1.3))*(1-seg(t,1.7,2.1));
  $('knock').style.transform=`translateX(${{sh*.6}}px)`; $('knock').style.opacity=1;
  // doors open
  const o=eIO(seg(t,1.6,3.2));
  $('leafL').style.transform=`rotateY(${{-o*104}}deg)`;
  $('leafR').style.transform=`rotateY(${{o*104}}deg)`;
  $('leafL').style.filter=$('leafR').style.filter=`brightness(${{1-o*.38}})`;
  $('glowp').setAttribute('opacity', eO(seg(t,1.8,3.0))*(1-seg(t,3.9,4.8)));
  $('rougep').setAttribute('opacity', seg(t,3.6,4.7));
  $('bgR').style.opacity=seg(t,4.4,5.0);
  // icon rises out of the doorway (clipped at the threshold until the zoom passes it)
  const r=eO(seg(t,2.35,3.6));
  const ic=$('icon'); ic.style.transform=`translateY(${{(1-r)*420}}px)`; ic.style.opacity=seg(t,2.35,2.9);
  const doorBottom={ORY}+({DOOR_BOTTOM}-{ORY})*zoom;
  $('iconwrap').style.clipPath=`inset(0 0 ${{Math.max(0,{H}-doorBottom)}}px 0)`;
  // wordmark writes on, left to right
  const w=seg(t,4.85,6.55), wp=lerp(-8,108,eIO(w));
  $('wm').style.webkitMaskImage=`linear-gradient(90deg,#000 0%,#000 ${{wp-7}}%,transparent ${{wp}}%,transparent 100%)`;
  // slogan letters land one by one (mask is lifted once the script is written)
  gs.forEach((g,i)=>{{ const x=eO(seg(t,6.1+i*.045,6.6+i*.045)); g.style.opacity=x; g.style.transform=`translateY(${{(1-x)*7}}px)`; }});
  $('top').style.opacity=eO(seg(t,7.3,8.1));
  const tg=eO(seg(t,7.6,8.5)); $('tag').style.opacity=tg; $('tag').style.transform=`translateY(${{(1-tg)*18}}px)`;
  $('handle').style.opacity=eO(seg(t,8.6,9.3));
  $('turb').setAttribute('seed', (frame||0)%7+1);
}};
window.setTime(0,0);
</script></body></html>'''

if __name__ == '__main__':
    open(os.path.join(HERE, 'reel.html'), 'w').write(html)
    print('ok', dict(ICON=ICON, DT=DT, ORY=ORY, DOOR_BOTTOM=DOOR_BOTTOM))
