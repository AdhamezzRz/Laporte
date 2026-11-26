"""Client presentation: each December post beside its brief / TOV / caption (1920x1080 pages)."""
from brand2 import *
D = '../../04_December_Content/'
POSTS = [
 ('01', 'Post1_Reel_Cover_1080x1920.jpg', True, 'Animated reel · the bell', 'A little something is changing.',
  'A little change is coming, and we can’t wait for you to see it.<br>Stay tuned. ♡', '#StayTuned',
  'A white-gloved maître d’ rings the service bell; “A little something is changing.” writes itself in Vladimir Script, then the new logo is revealed. 12 s, sound on.'),
 ('02', 'Post2_Let-The-Good-Bites-Begin_1080x1350.png', False, 'Platter on a solid background', 'Let the good bites begin',
  'The little bites that make every gathering a little more special. ♡<br>Made to share, made to enjoy, and always made with love.', '#ALaPorte #ALaPortePlatters',
  'The client’s heart-shaped platter in a tilted oval on burgundy, framed on the salami and grapefruit roses; editorial Cormorant capitals and “begin” in the brand script.'),
 ('03', 'Post3_Hello-December_1080x1350.png', False, 'Platter background · text in a box', 'Making December a little more delightful',
  'There’s something about December that makes every gathering feel a little more special. More moments to share, more reasons to gather, and always room for a little something delicious. ♡', '#ALaPorte #ALaPortePlatters',
  'A real platter close-up full-bleed under a soft burgundy overlay; a cream card with a “search bar” that types the line.'),
 ('04', 'Post4_Little-Things-Delicious_1080x1350.png', False, 'Quote on a solid background', 'The little things make life delicious',
  'It’s often the simplest things that leave the sweetest impression. A little flavour, a thoughtful touch, and the pleasure of enjoying something truly good. ♡', '#ALaPorte #ALaPortePlatters',
  'The quote set as a poster; the “little things” are cut-outs of the client’s own grapefruit, lemon and salami roses and kiwi flower.'),
 ('05', 'Post5_Festive-Moment_1080x1350.png', False, 'Platter on a festive table', 'A platter for every festive moment',
  'Christmas celebrations call for a little extra joy, festive moments, and a table worth gathering around. Let À La Porte add the perfect touch to your celebrations. ♡', '#ALaPorte #ALaPortePlatters',
  'The client’s letter-A platter, cut out and composited onto a Christmas table with matched light and shadow.'),
 ('06', 'Post6_Christmas-A-Little-Tastier_1080x1350.png', False, 'A gift, hand to hand', 'Make someone’s Christmas a little tastier',
  'Looking for a gift that feels a little more special? Our platters make the perfect festive surprise, thoughtfully prepared to bring a little joy to someone’s Christmas. ♡', '#ALaPorte #ALaPortePlatters',
  'Two hands passing a ribboned gift box, with a die-cut À La Porte gift tag illustrated on top.'),
]
CSSD = CSS + f'''
.page{{width:1920px;height:1080px;position:relative;overflow:hidden;page-break-after:always;background:{CR}}}
.lab{{font-family:Inter;font-size:15px;letter-spacing:.32em;text-transform:uppercase;font-weight:500}}
'''
pages = [f'''<section class="page center" style="background:{BU};flex-direction:column">
  {logo('full', CR, width=340)}
  <div class="script" style="color:{CR};font-size:110px;margin-top:60px">December content</div>
  <div class="lab" style="color:{CR};margin-top:26px;opacity:.85">Six posts · one reel · À la porte</div></section>''']
for n, f, reel, brief, tov, cap, tags, idea in POSTS:
    img = (f'<img src="{D}{f}" style="height:900px;border-radius:6px;box-shadow:0 30px 60px rgba(59,0,12,.3)">')
    pages.append(f'''<section class="page">
  <div class="abs center" style="left:90px;top:90px;width:{506 if reel else 720}px;height:900px">{img}</div>
  <div class="abs" style="left:{700 if reel else 900}px;top:120px;right:110px;color:{BU}">
    <div class="lab">Post {n} · {brief}</div>
    <div class="cb" style="font-size:78px;margin-top:30px;line-height:1">{tov.replace('’', '<span style="font-family:Corm;font-weight:600">’</span>')}</div>
    <div style="height:1px;background:{BU}55;margin:44px 0 36px"></div>
    <div class="lab" style="font-size:13px;opacity:.75">The idea</div>
    <div class="ci" style="font-size:31px;line-height:1.35;margin-top:12px">{idea}</div>
    <div class="lab" style="font-size:13px;opacity:.75;margin-top:40px">Caption</div>
    <div style="font-family:Inter;font-size:21px;line-height:1.6;margin-top:12px;color:{OX}">{cap}</div>
    <div style="font-family:Inter;font-size:19px;margin-top:16px;color:{WI};font-weight:500">{tags}</div>
  </div>
  <div class="abs" style="right:110px;bottom:60px">{logo('full', BU, width=86)}</div></section>''')
if __name__ == '__main__':
    open(os.path.join(HERE, 'deck_v2.html'), 'w').write(f'<!doctype html><html><head><meta charset="utf-8"><style>{CSSD}@page{{size:1920px 1080px;margin:0}}</style></head><body>{symbols()}{"".join(pages)}</body></html>')
    print(len(pages))
