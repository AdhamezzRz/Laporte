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
