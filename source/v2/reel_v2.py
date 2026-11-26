"""Post 1 — animated reel (1080x1920): the bell rings, 'A little something is changing.' writes itself,
then the new identity is revealed. Background = real-looking bell shot (Higgsfield), everything else is
designed motion typography in the brand fonts. reel_v2_render.js steps window.setTime(t)."""
import re
from brand2 import *

W, H = 1080, 1920
LW = 520; fx, fy, fw, fh = VB['full']; LH = LW * fh / fw

def glyph_spans(text, cls):
    out = ''
    for c in text:
        ff = 'font-family:Corm;font-weight:600;' if c in ".’'" else ''
        out += f'<span class="{cls}" style="display:inline-block;opacity:0;{ff}">{"&nbsp;" if c == " " else c}</span>'
    return out

html = f'''<!doctype html><html><head><meta charset="utf-8"><style>{CSS}
html,body{{width:{W}px;height:{H}px;overflow:hidden;background:{OX}}}
#stage{{position:absolute;inset:0;overflow:hidden;background:{OX}}}
#cam{{position:absolute;inset:0;transform-origin:50% 78%}}
#cam img{{position:absolute;inset:0;width:{W}px;height:{H}px;object-fit:cover}}
#still{{opacity:0}}
#shade{{position:absolute;inset:0;background:linear-gradient(180deg, rgba(59,0,12,.35) 0%, rgba(59,0,12,0) 45%)}}
#txt{{position:absolute;left:0;right:0;top:520px;text-align:center;color:{CR}}}
#l1{{font-size:150px;white-space:nowrap;display:inline-block;-webkit-mask-image:linear-gradient(90deg,#000 0%,#000 0%,transparent 0%);padding:0 20px}}
#l2{{font-size:98px;letter-spacing:.06em;margin-top:6px}}
#end{{position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% 48%, {BU} 0%, {OX} 75%);opacity:0}}
#logo{{position:absolute;left:{(W-LW)/2}px;top:{(H-LH)/2-90}px;opacity:0}}
#tuned{{position:absolute;left:0;right:0;top:{(H+LH)/2-40}px;text-align:center;color:{CR};opacity:0}}
#vig{{position:absolute;inset:0;pointer-events:none;background:radial-gradient(ellipse at 50% 50%,rgba(0,0,0,0) 55%,rgba(20,0,4,.45) 100%)}}
#grain{{position:absolute;inset:0;opacity:.12;mix-blend-mode:overlay;pointer-events:none}}
</style></head><body>{symbols()}
<div id="stage">
  <div id="cam"><img id="vid" src="assets/bellframes/f_0001.jpg"><img id="still" src="assets/bellframes/f_0001.jpg"></div>
  <div id="shade"></div>
  <div id="txt">
    <div id="l1" class="script">A little something</div>
    <div id="l2" class="cb">{glyph_spans('IS CHANGING.', 'g2')}</div>
  </div>
  <div id="end"></div>
  <div id="logo">{logo('full', CR, width=LW)}</div>
  <div id="tuned"><span class="script" style="font-size:96px">Stay tuned</span>
    <span style="display:inline-block;vertical-align:middle;margin-left:10px">{heart(54, CR, 3.4, -8)}</span></div>
  <div id="vig"></div>
  <svg id="grain" width="100%" height="100%"><filter id="gf"><feTurbulence id="turb" type="fractalNoise" baseFrequency=".85" numOctaves="3" seed="1" stitchTiles="stitch"/><feColorMatrix type="saturate" values="0"/></filter><rect width="100%" height="100%" filter="url(#gf)"/></svg>
</div>
<script>
const $=id=>document.getElementById(id);
const clamp=(x,a=0,b=1)=>Math.min(b,Math.max(a,x));
const seg=(t,a,b)=>clamp((t-a)/(b-a));
const eIO=x=>x<.5?4*x*x*x:1-Math.pow(-2*x+2,3)/2;
const eO=x=>1-Math.pow(1-x,3);
const g2=[...document.querySelectorAll('.g2')];
window.DUR=12.0;
let lastSrc='';
window.setTime=async function(t, frame){{
  const vf=Math.min(151, Math.floor(t*30)+1);
  const src='assets/bellframes/f_'+String(vf).padStart(4,'0')+'.jpg';
  if(src!==lastSrc){{ $('vid').src=src; await $('vid').decode(); lastSrc=src; }}
  // dissolve the exiting hand into the clean frame, then a slow push-in
  $('still').style.opacity=eIO(seg(t,4.55,5.15));
  const push=1+0.06*eIO(seg(t,4.4,9.6));
  $('cam').style.transform=`scale(${{push}})`;
  // the line writes itself (script wipe), then the caps land letter by letter
  const w=eIO(seg(t,4.45,6.15)), p=-10+w*125;
  $('l1').style.webkitMaskImage=`linear-gradient(90deg,#000 0%,#000 ${{p-10}}%,transparent ${{p}}%)`;
  g2.forEach((g,i)=>{{ const x=eO(seg(t,6.0+i*0.055,6.45+i*0.055)); g.style.opacity=x; g.style.transform=`translateY(${{(1-x)*14}}px)`; }});
  const out=eIO(seg(t,8.7,9.3));
  $('txt').style.opacity=1-out; $('txt').style.transform=`translateY(${{-out*20}}px)`;
  // reveal
  $('end').style.opacity=eIO(seg(t,8.85,9.55));
  const lg=eO(seg(t,9.45,10.4));
  $('logo').style.opacity=lg; $('logo').style.transform=`translateY(${{(1-lg)*26}}px) scale(${{0.96+0.04*lg}})`;
  const tu=eO(seg(t,10.2,10.9));
  $('tuned').style.opacity=tu; $('tuned').style.transform=`translateY(${{(1-tu)*16}}px)`;
  $('turb').setAttribute('seed',(frame||0)%6+1);
}};
</script></body></html>'''

if __name__ == '__main__':
    open(os.path.join(HERE, 'reel_v2.html'), 'w').write(html)
    print('ok')
