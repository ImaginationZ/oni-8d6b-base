# Tools

| File | What it does |
|---|---|
| `gen.py` / `gen2.py` | Layout generators for v1 and v2. Each places buildings by bottom-left cell and validates overlaps, sealed rooms (flood fill, tile counts) and floor/ceiling mounting. They emit BNI-format JSON (`blueprintItems`, bottom-centre anchor) and `layout*.json` for the page. Usage: `python3 gen2.py <outdir>`. |
| `bni_database.json` | Building data from Blueprint Not Included (github.com/simonlourson/blueprintnotincluded), MIT licence, see `bni_database.LICENSE`. |
| `render.py` | ASCII render of any BNI-format JSON (`{"data":{"blueprintItems":[...]}}`). Sizes come from `bni_database.json` (BNI's old public DB) plus an EXTRA table for newer DLC buildings. |
| `page.py` / `page2.py` | Build the HTML design page (SVG section drawing, tables) from `layout*.json` + `template*.html`. Usage: `python3 page2.py <dir with layout_v2.json and base_8d6b_v2_bni.json> template2.html out.html`. |
| `template*.html`, `head.part`, `body2.part` | Page templates. `head.part` holds the CSS; `body2.part` is the v2 body. |
| `blueprint_rooms.py` | Analyse a Blueprints-mod `.blueprint`: structure and furniture ASCII layers, flood-filled rooms, and door access, checkpoint and sink-direction settings. `python3 -I blueprint_rooms.py <file>`. |
| `yuque.py` | Fetch a Yuque doc (text outline + all images): `python3 yuque.py <url> <outdir>`. |
| `bili_dl.py` | Download a Bilibili DASH stream with CDN fallback: `python3 bili_dl.py <BV> v|a <outfile>`. Needs `cookie.txt` and `view_<BV>.json` in the working dir (see docs/lessons.md). |
| `capdedupe.py` | Turn 1-fps caption-strip crops into deduplicated, timestamped pages to read. |

Facts the code relies on:
- ONI anchor: x0 = anchor − (w−1)//2, y0 = anchor y.
- Orientation 5 = flip H.
- Build rules from the DB: 0 = anywhere, 1 = on floor, 3 = on ceiling.
