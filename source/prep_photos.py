"""Crop + gently grade the client's own Instagram photos for the food posts.
No generative edits: crop, resize (Lanczos), mild warm grade, light sharpening.
Crops deliberately exclude balloons and framed photos of people."""
import os
from PIL import Image, ImageEnhance, ImageFilter, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, 'client_photos')
OUT = os.path.join(SRC, 'crops'); os.makedirs(OUT, exist_ok=True)

def grade(im):
    im = ImageEnhance.Color(im).enhance(0.9)
    im = ImageEnhance.Contrast(im).enhance(1.04)
    r, g, b = im.split()
    r = r.point(lambda v: min(255, int(v * 1.03 + 2)))
    b = b.point(lambda v: int(v * 0.95))
    im = Image.merge('RGB', (r, g, b))
    return im.point(lambda v: int(10 + v * 243 / 255))   # lift blacks a touch: printed-paper feel

def crop(src, box, size, name, circle=False):
    im = Image.open(os.path.join(SRC, src)).convert('RGB').crop(box)
    im = im.resize(size, Image.LANCZOS)
    im = im.filter(ImageFilter.UnsharpMask(radius=1.2, percent=60, threshold=2))
    im = grade(im)
    im.save(os.path.join(OUT, name + '.jpg'), quality=93)

# 1 — the letter-A box (carousel arrow on the right edge is cropped out)
crop('src_5.png', (12, 0, 1048, 1316), (1036, 1316), 'a_box')
# 2 — the roses (square crops, shown as circles)
crop('src_5.png', (398, 720, 698, 1020), (560, 560), 'rose_grapefruit')
crop('src_5.png', (85, 1112, 340, 1367), (560, 560), 'rose_salami')
crop('src_5.png', (528, 305, 806, 583), (560, 560), 'rose_lemon')
crop('src_5.png', (300, 282, 552, 534), (560, 560), 'rose_cucumber')
# 3 — the get-well tray, below the framed photo
crop('src_4.png', (125, 1032, 845, 1392), (1440, 720), 'tray_anatomy')
# 4 — occasions (portrait crops for arches)
crop('src_4.png', (560, 885, 850, 1305), (580, 840), 'occ_getwell')
crop('src_2.png', (858, 1118, 1036, 1376), (580, 840), 'occ_babygirl')
crop('src_2.png', (112, 76, 540, 696), (580, 840), 'brunch')
# 5 — details (well below the framed photo of people)
crop('src_3.png', (0, 700, 808, 1334), (1080, 848), 'details')
# 6 — croissants, kiwi flowers & grapefruit rose (play icon cropped out)
crop('src_2.png', (1095, 72, 1560, 722), (930, 1300), 'order')
print('ok', sorted(os.listdir(OUT)))
