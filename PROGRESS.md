# Progress

## Status (2026-11-14)
The blueprint is parsed and the findings are written (§5, §5b, §7). The v3 design hasn't started. The bedroom-airlock decision is pending with the owner.

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

## Pending decision (asked 2026-11-14)
**Where the bedroom airlock goes in the semi-open design.** What 拿个破笔水's files show (findings §5, §5b):
- The `.blueprint` is their *closed* base. Its airlock is a nature reserve at the entrance: tube → checkpoint → 8 docks → reserve → 3 stacked bed rows (12 × 2 inside, 3 + 3 + 2 beds; probably plain Barracks).
- Their *semi-open* base sleeps dupes in 2 rocket habitats, which the owner has ruled out.
- Docks and the checkpoint sit inside a valid Nature Reserve, which is good evidence they aren't industrial machinery.

Options:
- **A.** Checkpoint + 4 docks inside each barracks. Probably valid now, but it hits the 64-tile room cap.
- **B.** A separate dressing room in a wider central column.
- **C.** Dressing room one storey below the beds.
- **D (new, from the blueprint).** The nature reserve *is* the dressing room: checkpoint + 8 docks inside it, in front of the two bed wings. Dupes pass it going to bed and getting up, which is 拿个破笔水's step ①.

Recommended: D.

Also open: **Luxury Barracks needs a 4-tall ceiling.** A 4-tile storey gives 3, so we either raise one column (a notch) or accept plain Barracks the way 拿个破笔水 does.

## Next
1. ~~Parse the blueprint~~ (done 2026-11-14; `tools/blueprint_rooms.py`). Semi-open images 10, 25 and 26 reviewed; 27–37 (misc rooms, washroom, banquet, rec) are still worth a look when designing those rooms.
2. Agree the v3 plan with the owner: dupe loop (downward via the fire pole: beds → washroom → food → banquet → recreation → nature reserve with printing pod → exit), one-way bionic wing, door permissions, the semi-open bedroom airlock, up/down access and tube room.
3. Build v3 with `tools/gen2.py` as a starting point (it validates overlaps, rooms and floors), render the page, publish or serve it, and update this file.

## How to view designs
`tools/page2.py` builds an HTML page from a layout. To serve locally: `python3 -m http.server <port> --bind 127.0.0.1 --directory <dir>`. From the phone, an Artifact page (claude.ai) is easier to open.
