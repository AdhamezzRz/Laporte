# À LA PORTE — Final logo & brand identity

**Final logo:** the *à la porte* script wordmark with the slogan **A TRAY FOR EVERYDAY**, as drawn in Option 3, and the hand-and-tray icon. It is set in **Rouge Porte `#B75548`** on **Parchemin `#E2CDA1`**, the client's chosen colour.

| Folder | Contents |
|---|---|
| `01_Final_Logo/` | `ALaPorte_Final_Logo.pdf` (14 pages: logo, colourways, anatomy, logo family, clear space, palette, typography, misuse) · `svg/` vector logos · `png/` transparent logos (primary, wordmark, icon × terracotta, parchment, bordeaux, espresso) |
| `02_Brand_Identity/` | `ALaPorte_Brand_Identity.pdf` (17 pages: idea, symbols, logo system, palette, type, graphic elements, voice, packaging, print, launch posts, reel storyboard, feed, captions) |
| `03_Social_Posts/` | Post 1 *Identity reveal* · Post 2 *Served by hand* · Post 3 *Knock, knock*, the animated reel (`.mp4` 1080×1920 + 1080×1350 feed cut, with sound) + its grid cover + a GIF preview |
| `source/` | Generators (Python → HTML → Chromium PDF/PNG). Logo vectors come untouched from the designer's Illustrator file. |

## Palette
| Name | HEX | Role |
|---|---|---|
| Rouge Porte | `#B75548` | Primary: logo, headlines, the door |
| Parchemin | `#E2CDA1` | Primary: grounds |
| Ivoire | `#F5EEDF` | Light ground |
| Bordeaux | `#5C1F1A` | Depth, evenings, gifting |
| Olive | `#6F6B3B` | Seasonal accent |
| Café | `#2B1D18` | Text |
| Laiton | `#B08D57` | Foil only |

## Typography
Logotype: Vladimir Script (outlined artwork) · Display: Cormorant Garamond · Text: Jost (free Google Fonts).

## Rebuild
```bash
cd source
python3 final_logo.py && node render.js final_logo.html ../01_Final_Logo/ALaPorte_Final_Logo.pdf
python3 posts.py && node shoot.js posts.html <outDir> .post 1
python3 reel.py && node reel_render.js reel.html <framesDir> 30   # then ffmpeg (see commit notes)
python3 identity.py && node render.js identity.html ../02_Brand_Identity/ALaPorte_Brand_Identity.pdf
```

---

## December content (final identity)
The client's approved visual identity (logo option 1 · `#3b000c` `#550b18` `#76152d` `#f2e5c5` · Cormorant Garamond, Acumin, Vladimir Script) drives `04_December_Content/`:

| File | Post |
|---|---|
| `Post1_Animated_Reel_A-Little-Something_1080x1920.mp4` (+ `_Feed_1080x1350.mp4`, cover) | The bell: "A little something is changing." |
| `Post2_Let-The-Good-Bites-Begin_1080x1350.png` | Platter on solid background |
| `Post3_Hello-December_1080x1350.png` | Platter background + card |
| `Post4_Little-Things-Delicious_1080x1350.png` | Quote on solid background |
| `Post5_Festive-Moment_1080x1350.png` | Platter on a festive table |
| `Post6_Christmas-A-Little-Tastier_1080x1350.png` | A gift, hand to hand |
| `ALaPorte_December_Content_Presentation.pdf` | Each post with its brief, idea and caption |

All food is the client's own photography (cut-outs, crops, gentle grade). Higgsfield was used only for the bell shot, the empty Christmas table, the gift hands, background removal and upscaling. Sources: `source/v2/`.

## Stickers (print)
`05_Stickers_Print/`: round stickers, vector, CMYK, 3 mm bleed, die line in the `CutContour` spot colour (overprint, do not print).
- `ALaPorte_Sticker_40mm_Round.pdf` / `ALaPorte_Sticker_60mm_Round.pdf`: one sticker per page (burgundy, then cream), TrimBox = sticker, BleedBox = +3 mm.
- `ALaPorte_Sticker_Sheets_A4.pdf`: A4 gang sheets: 24 × 40 mm or 12 × 60 mm per sheet, each in both colourways.
- CMYK: burgundy C25 M100 Y78 K50, cream C4 M9 Y25 K0. Ask the printer for a proof.

## Butter paper & social card (print)
`06_Print_Pattern_Card/`:
- `ALaPorte_ButterPaper_30x40cm.pdf`, `ALaPorte_ButterPaper_40x50cm.pdf`: one-ink (burgundy) pattern for translucent greaseproof paper, no background fill.
- `ALaPorte_Social_Card_85x55mm.pdf`: p1 front · p2 back with Instagram QR (ready now) · p3 back with Instagram + Facebook (Facebook slot pending). CMYK, 3 mm bleed. QR codes verified by decoding.
- To add Facebook: set `SOCIAL['facebook']` in `source/v2/print_extras.py` and run `python3 print_extras.py`.
