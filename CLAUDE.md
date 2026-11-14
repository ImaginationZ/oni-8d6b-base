# ONI 8+6 base: agent instructions

The owner is designing an end-game **Oxygen Not Included** base (all DLC) for **8 standard duplicants + 6 bionic duplicants** ("boops"). The work was started in a Claude Code session on the owner's desktop on 2026-11-13 and moved to their remote dev machine so they can continue from their phone.

Read these before doing anything:
1. `PROGRESS.md`: where the work stands and what's next. Update it whenever something is decided or done.
2. `docs/requirements.md`: the owner's requirements and every decision they've made, with dates. Their decisions override your own preferences.
3. `docs/findings.md`: what the reference designs actually do and why (design logic, flow, schedules). This is the main knowledge transfer.
4. `docs/lessons.md`: mistakes made so far, and how to avoid repeating them.

## Working rules (from the owner's feedback)
- **The owner's references are requirements.** If you can't open or see one, say so right away and ask. Never quietly substitute your own design and bury the gap in caveats.
- **Try hard before saying you can't access something.** Yuque bodies, Bilibili videos and captions are all retrievable; `docs/lessons.md` and `tools/` show how.
- **Check structural changes with the owner before rebuilding.** Show a short plan first. Pick sensible defaults for small things and say so.
- Verify game facts (wiki, blueprint files, BNI data) rather than asserting from memory, and mark anything unverified.
- Use they/them for anyone whose pronouns aren't stated.

## Layout of this repo
- `references/`: everything gathered (Yuque docs and images, both videos with caption pages, 拿个破笔水's actual `.blueprint` and save, BNI sample blueprints). Large media is untracked (`.gitignore`); see `references/README.md`.
- `tools/`: the generator, renderer and page builder for designs, plus the Yuque and Bilibili fetchers. See `tools/README.md`.
- `designs/v1`, `designs/v2`: earlier attempts, now superseded (see PROGRESS for why).
- `docs/`: requirements, findings, lessons.
