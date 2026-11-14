# Progress

## Status (2026-11-13)
Research is done; the v3 design hasn't started. One decision is pending with the owner.

## Done
- [x] Researched BNI's catalog and sample 8-dupe and bionic bases (`references/bni_samples/`).
- [x] Researched bionic mechanics and building sizes (wiki), recorded in findings and the tools.
- [x] **v1** (Twin-Spine, 38 × 36, 7 storeys): superseded. It had bionic beds, no flow design, and the docks on the wrong side.
- [x] **v2** (38 × 31, 6 storeys, the owner's first round of changes): superseded. It stacks rooms by type, has no dupe/bionic separation, and the docks are on the wrong side.
- [x] Read 大叔's Yuque doc and all 35 screenshots.
- [x] Downloaded and watched both videos in full (every caption read); design logic written up in `docs/findings.md`.
- [x] Fetched 拿个破笔水's two Yuque docs (85 + 30 images), not yet reviewed image by image.
- [x] Got 拿个破笔水's `.blueprint` and save (from the owner's download).
- [x] Moved the project to the owner's remote dev machine.

## Pending decision (ask the owner first)
**Where the bedroom airlock goes in the semi-open design.** 8 comfy beds fill two 16-wide wings, which leaves no room on that storey for checkpoint + 8 docks.
- **A.** 4 docks + checkpoint inside each barracks, at the door. Compact, but only valid if suit docks aren't "industrial machinery"; otherwise the room loses its Luxury Barracks status. The owner can check in-game by hovering a dock.
- **B.** A separate dressing room in a wider central column, about 46 tiles wide (大叔's base is 45). Safe.
- **C.** Dressing room one storey below the beds, linked by a ladder through a horizontal door. Compact but fiddly.

Recommended: A if docks aren't industrial, otherwise B. **Also check how 拿个破笔水's blueprint solves this.** It has 8 `LuxuryBed` and about 9 `SuitLocker` in 31 × 33, so it already fits proper beds and docks compactly.

## Next
1. Parse `references/napobi_save_blueprint/napobi_8p6.blueprint` properly: per-room building lists, where the beds, docks and checkpoints sit, and the flow. Review the semi-open Yuque images (`references/napobi_yuque_semi_open/`, especially 10, 11, 25–37).
2. Agree the v3 plan with the owner: dupe loop (downward via the fire pole: beds → washroom → food → banquet → recreation → nature reserve with printing pod → exit), one-way bionic wing, door permissions, the semi-open bedroom airlock, up/down access and tube room.
3. Build v3 with `tools/gen2.py` as a starting point (it validates overlaps, rooms and floors), render the page, publish or serve it, and update this file.

## How to view designs
`tools/page2.py` builds an HTML page from a layout. To serve locally: `python3 -m http.server <port> --bind 127.0.0.1 --directory <dir>`. From the phone, an Artifact page (claude.ai) is easier to open.
