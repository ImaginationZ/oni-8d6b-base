# Lessons so far

## Mistakes and what to do instead
1. **Designed v1 without actually seeing the owner's references.** I couldn't watch the videos, built my own layout anyway, and mentioned the gap only at the bottom of the page. The owner felt their intent was ignored. **Do:** confirm each reference is accessible before substantial work, and if one isn't, stop and ask.
2. **Gave up too early on access.** All three sources turned out to be retrievable with a little effort (below). **Do:** try the techniques here before saying "can't".
3. **Added beds for bionics.** Both references give bionics no beds. **Do:** derive the design from the references' logic.
4. **Stacked rooms by type, not by routine** (v2). That caused backtracking (beds → washroom → past the exit → dining → back up to recreation). **Do:** design the flow first (sections 2 and 3 of findings.md), then place rooms along it.
5. **Checkpoint orientation was backwards in v1 and v2.** Docks go on the clean side, opposite the arrow.

## How to get at the sources
- **Yuque docs:** WebFetch returns only the title. `tools/yuque.py <url> <outdir>` reads `window.appData` for the book_id, calls `https://www.yuque.com/api/docs/<slug>?book_id=<id>&merge_dynamic_data=false`, prints the text outline and downloads every image (cdn.nlark.com, with a yuque Referer).
- **Bilibili videos:**
  - Without a visitor cookie the API returns HTTP 412. Get one from `https://api.bilibili.com/x/frontend/finger/spi` (b_3 → `buvid3`, b_4 → `buvid4`).
  - Then `x/web-interface/view?bvid=` gives the cid, and `x/player/playurl?bvid&cid&qn=80&fnval=16` gives DASH streams. 480p works without logging in.
  - Some CDN hosts return HTML. `tools/bili_dl.py` falls back through the backup URLs and resumes partial downloads.
  - No subtitle tracks exist, but captions are burned in: `ffmpeg -vf fps=1,crop=...` on the bottom strip, then `tools/capdedupe.py` stacks the distinct caption lines into readable pages.
- **BNI:**
  - `https://blueprintnotincluded.org/api/getblueprints?olderthan=<epoch ms>&filterName=<q>` pages through the catalog, 100 at a time. Use the `oldest` field for the next page.
  - `api/getblueprint/<id>` returns `data.blueprintItems` (id, position = bottom-centre anchor, orientation; 5 = flip H).
  - urllib's default User-Agent gets 403, so use curl or a browser UA.
- **wiki.gg** blocks scripted `?action=raw`. WebFetch of the normal page works.
