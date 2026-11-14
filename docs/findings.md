# Findings: what the references do and why

Sources: both videos, watched in full (every caption line read from burned-in subtitles), 大叔's Yuque doc with 35 screenshots, and 拿个破笔水's two Yuque docs plus their `.blueprint`. Raw material is in `references/`. Caption pages are `capd_*.png` (大叔) and `capz_*.png` (拿个破笔水), each line timestamped.

## 1. Schedules decide how much furniture you need
- **Standard dupes, in both bases:** 4 shifts × 2 dupes. Each shift **sleeps first, then rests** ("先睡后休"), and sleep times are **fully staggered**.
  - 大叔's screens: each shift is Work 16 h, Bedtime 4 h, Downtime 4 h, with shifts starting 5 h apart. Shift 1 sleeps hours 15–18, shift 2 sleeps 10–13, and so on (`references/dashu_yuque/img/31.jpg`).
  - Result: only 2 dupes are ever off shift together, so one 3-seat communal table, 2 lavatories and one rec room are always enough.
- **Bionics:** no Bedtime at all.
  - 大叔: 3 shifts × 2 on a **3-cycle schedule**. Each pair gets 6 h of Downtime on its own cycle and works every other hour (`img/32.jpg`).
  - 拿个破笔水: "不安排睡眠，每3周期休息1次，每人6格休息时间，每个机哥之间的休息时间也间隔6小时". Each bionic shift is **a single bionic**, because there is only one gunk extractor. The bionic schedule is sized to the single shared machine.
  - 大叔 also matches power-bank drain to rest time (video BV1Q27gzkEDS), so a bionic never has to come home mid-shift for a bank. Re-sync every ~500 cycles because it drifts.

## 2. Flow (动线): rooms follow the daily routine in order, and door permissions enforce it
- **Dupes: a loop with no backtracking.**
  - 拿个破笔水's diagram (`references/videos/napobi_BV1Zi2EBYE25/z_full_57.jpg`): ① enter past the nature reserve → ② sleep → ③ toilet (one-way door) → ④ pick up food → ⑤ eat → ⑥ recreation and socialising → ⑦ leave past the nature reserve again.
  - 大叔 (video 0:54–4:44): sleep (suits off) → straight to the toilet → banquet hall, where food made upstairs is dropped down → recreation → leave through the nature reserve by the printing pod.
- **Bionics: one-way, entering on one side and leaving on the other.**
  - 拿个破笔水 (`z_full_21.jpg`): ① enter from the base's right side → ② gunk, power, oxygen → ③ recreation and socialising → ④ leave through the protected-area door. Bionics may enter the massage room from above.
  - 大叔 (5:39–7:07): come back from work → toilet (gunk) → "eat" power banks → lube → breathe O₂ → leave through a door that only opens rightward.
- **Exclusive and shared zones** (拿个破笔水 1:51–2:13):
  - Bionic life support is off-limits to dupes.
  - The dupes' washroom, kitchen and dining are off-limits to bionics.
  - Rec room, massage room and gym are shared.
  - Enforced with door access settings: 禁止通行 (no entry) and 单向通行 (one way).
- **Nature reserve placement.** 大叔 deliberately makes it the **last room before leaving for work**, at the printing pod. The park buff is short, so it should be fresh as work starts. Bionics are kept out of it (optional).
- **Lube station.** 3 timer sensors open its doors only during each bionic group's rest window, so only that group can refuel (大叔 12:15). Beginners can just leave the doors open.

## 3. Atmosphere strategy
- **大叔's base is semi-open.**
  - Dupes keep atmo suits on inside the base and take them off only to sleep. His bedroom is a rocket habitat with 8 cots, so its interior is off-map.
  - The suit docks sit at the habitat entrance. The O₂ line fills the docks first, then the habitat.
  - Only 5 docks are needed, because every dupe owns a suit and at most 2 are asleep (Yuque note).
  - A "gas-eating door" at the spot where dupes take suits off removes the CO₂ they exhale. Pee leaking from a suit can't block it.
  - **Kitchen and banquet hall are deep-frozen below −18 °C** so food never spoils (14:00). That works because dupes are suited.
  - The bionic zone is **high-pressure O₂** (about 20 kg per tile), so bionics refill in place. Canister fillers are optional extras for exploration bottles.
- **拿个破笔水: bionics never take their suits off** ("考虑到机哥不脱气压服"). That makes them immune to popped eardrums and heat, so the bionic-side high-pressure electrolyzer is open and vents hot gas into their life-support area.
  - The rest of the life-support zone is walled in insulation, or vacuum where it touches outer walls.
- **Late game:** idle dupes wait at the checkpoint and tie up docks. Fix it with a gym of manual generators outside, or only enable the checkpoint when a duplicant sensor detects someone (大叔's Yuque note).

## 4. Life support and utilities
- **One electrolyzer supplies 8 people.**
  - 大叔 builds 2 separate high-pressure O₂ modules, one for dupes and one for bionics, each with its own hydrogen generator and one smart battery.
  - A gas pressure sensor controls the pump and electrolyzer.
  - A **liquid element sensor on the electrolyzer's water input** pauses the game with an alarm if the water stops or isn't water. He calls this mandatory for high-pressure O₂.
- **O₂ priority order (大叔):** dupe suits/docks first, then the bedroom; surplus goes to 2 gas cargo rockets. "Empty storage" on a rocket drops bottled O₂/H₂ for explorers.
- **Cooling (大叔):** a cooling module cools only the O₂ zone. A second loop deep-freezes kitchen and banquet hall. A hydrogen loop moves a little cold downward when the lower area goes above about 12 °C.
- **拿个破笔水:** one reed plant drinks all the sewage; 8 dupes make 133.6 kg/cycle, and the reed uses 160 kg/cycle. A long sewage pipe has an automation alarm. The cooling loop wraps around life support without entering it. Two reeds were cut to one.
- **Food logistics:** cook upstairs, drop food down to the banquet hall's cold storage. The conveyor carries finished dishes only, never raw ingredients, eggshells, polluted dirt or rot. Power banks go round a conveyor loop to the chargers.
- **Germs:** both bases skip sinks and use 2 shine bugs or depleted-uranium tiles to sterilise. **The owner rejected this; we use sinks.**

## 5. 拿个破笔水's actual blueprint (`references/napobi_save_blueprint/napobi_8d6b.blueprint`)
Parsed with `tools/blueprint_rooms.py` (2026-11-14) and checked against the base doc's screenshots (`references/napobi_yuque_base/03.jpg` overview, `04.jpg` bionic flow, `05.jpg` dupe flow).

**Which base it is.** The friendly name is "（U59重制）8复制人+6仿生人混合基地": the **closed** mixed base (Yuque "8复制人+6仿生人混合基地", 31 × 33), **not the semi-open one**. Inside it everyone breathes freely, and suits come off once, at the base entrance. Coordinates below are tiles, x 0–30 left to right, y 0–32 bottom to top.

**Bedrooms: 8 comfy beds in 12 × 8 tiles.**
- Three rows of beds, each row its own room, **12 wide × 2 tall inside** (x16–27), with 1-tile floors between rows. Rows hold 3 + 3 + 2 beds; the bottom row's spare 4 tiles hold a canister filler (`GasBottler`) and a hanging cactus vase.
- Beds sit side by side, 4 tiles each (`LuxuryBed` at x17/21/25). Each row is exactly 24 tiles.
- The left wall is a **column of 5 stacked doors** (x15, y18–27, all "bionics: no entry"). Each row's right end is a door (x28) onto a fire-pole shaft (x29) that drops dupes to the washroom. So dupes walk in on the left and leave on the right: one-way through the beds.
- **The rows are probably plain Barracks (+1 morale), not Luxury Barracks (+2).** The wiki says Luxury Barracks needs a ceiling of at least 4 (one column of 4 is enough), and these rows are 2 tall. The room overlay (`05.jpg`) colours them as some kind of bedroom but doesn't say which. *Unverified in-game.* 拿个破笔水 traded the morale point for compactness.

**Suit docks and checkpoint: inside the nature reserve, at the base entrance.**
- The transit-tube entrance is inside the left wall (x1–3, y20–21). Then comes the checkpoint (`SuitMarker` x5, flipped, arrow pointing left/out), then **8 docks in a row** (x6–13; the 8th is one tile higher), then the bedroom doors. Docks are on the clean side, as the wiki rule requires.
- That whole corridor (park sign at x1 y17, wild plants on natural tiles, which blueprints don't store) is the **nature reserve**: flow step ① "进门经过自然保护区". The dressing room *is* the nature reserve, so it costs no extra room.
- **Evidence that docks and checkpoints aren't industrial machinery.** A Nature Reserve forbids industrial machinery, and `05.jpg` shows the reserve coloured as a valid room with the checkpoint and all 8 docks inside it. This is strong but indirect: neither wiki page states it. Hovering a dock in-game would settle it.
- Bionics are barred from the upper part of the reserve "so they don't pass the checkpoint and drop their suits" (`04.jpg`). Bionics wear suits for life, which spares suit repairs.

**Dupe loop, as the door settings enforce it** (`05.jpg`):
① tube in → checkpoint → docks (suit off) → reserve → ② a bed row (enter left, exit right) → fire pole down (x29, then x27 through a horizontal door, bionics: no entry) → ③ washroom (2 lavatories, 2 sinks set one-way) → ④ pick up food at the fridge in the kitchen strip → ⑤ banquet hall bottom-left (communal table, phone, water cooler) → ladder up through a bionics-no-entry door → ⑥ rec room (arcade, beach chair, soda fountain) → ⑦ back through the reserve, suit on, tube out.

**Bionics, one-way right → left** (`04.jpg`):
① enter on the right → ② gunk extractor + hand sanitiser room (x21–25 y12–15), chargers (4 `ElectrobankCharger`, bottom right), lube station in the middle → ③ shared rec/social area → ④ leave through the lower reserve by a left-wall door set "bionics: go left only, dupes: no entry".
- Bionics may also enter the massage room from above.
- Early game: cots in the bottom row, where bionics can sleep to make chips ("前期使用小床 可安排机哥进宿舍睡觉产出芯片").

**Door access *is* stored.** An earlier note here said it wasn't. `Door.AccessControl.defaultPermissionByTag` holds per-tag (`Minion`, `BionicMinion`) values. 29 doors and 3 pressure doors carry settings: 11 restrict bionics or dupes, and the rest are open to both.

**Other contents worth reusing:**
- 2 electrolyzers (one high-pressure O₂ module per side), 3 hydrogen generators.
- A steam-turbine cooling room with 2 liquid conditioners.
- Kitchen: microbe musher → electric grill → gas range, plus deep fryer, smoker and spice grinder. Robo-arms feed it.
- A communal table in the banquet hall, and a second one in the middle shared room (purpose unclear).
- 2 manual generators back-feeding the grid through a transformer, a medical cot, a massage table and an apothecary.
- 8 `SuitLocker` (an earlier count said about 9), one `SuitFabricator`, and 1 transit-tube entrance.

## 5b. 拿个破笔水's semi-open base: the primary reference (`references/napobi_semi_open_save_blueprint/`)
Sources: the author's own download (two `.blueprint` files + sandbox `.sav`), parsed with `tools/blueprint_rooms.py` on 2026-11-14 and checked against the semi-open Yuque images (`references/napobi_yuque_semi_open/` 04 overview, 10 dupe flow, 11 bionic flow, 25 zones, 26 room overlay, 27 and 30 dock corridor). Coordinates: x 0–44 left to right, y 0–26 bottom to top.

**Overall: 45 × 27, two blocks around a central shaft.**
- **Left block (x0–20), mixed living.** Kitchen at the bottom → washroom → banquet hall on the left → rec room on top (wind tunnel, surfboard, arcade, beach chair) → massage room in the top-left corner. High-pressure O₂ room in the middle; lube station room beside it.
- **Central shaft (x21–23): the nature reserve.** Fire pole, ladder and transit tube side by side, wild cacti on natural tiles, park sign, 114 tiles. It runs the full height and exits top and bottom through horizontal doors, so it is also the up/down route to work ("小人上下班都经过一次 获得+6士气加成").
- **Right block (x24–44), utilities.** Steam-turbine cooling, hydrogen generators and power at the top, a sewage/manual-generator gym, the **suit-dock corridor**, then a misc room (suit fabricator, medical cot, apothecary) and the electrobank chargers at the bottom.

**Bedroom = 2 Spacefarer Modules in the dock corridor.**
- The corridor (x25–43, y7–10, 4 tall) runs: door from the shaft (x24, *dupes both ways, bionics no entry*) → checkpoint (`SuitMarker` x25, flipped, arrow pointing left/out to the shaft) → **8 docks** (x26–33) → **two habitat modules side by side** (x34–43, 5 × 4 each).
- **Images 27 and 30** show the modules standing straight on the corridor floor, hatches facing the corridor. There's no launch pad, engine or nosecone visible. Rocket parts aren't stored in blueprints, so the main `.blueprint` just leaves the space empty.
- **Interior** (`napobi_8d6b_semi_open_spacefarer_module.blueprint`, 10 × 8): 4 `LuxuryBed`, two rows of 2. Rows are 2 tall, with floors of metal, carpet and airflow tiles. A ladder column at x1 runs the full height. There's a gas vent (O₂ in), an element sensor + timer + buffer driving it, and a locked pressure door at the hatch row.
- The interior is one room of about 50 tiles. The ladder column is 7 tall, so the wiki's ceiling rule (one column of 4 or more) and size rule (12–64) for Luxury Barracks are met. Decor items and whether room bonuses apply inside a rocket interior are *unverified*.
- **Why it's compact.** All 8 beds plus their airlock take 19 × 4 = 76 tiles on the map. The interiors are off-map and automatically suit-free, so there's no bedroom atmosphere to manage. The closed base needed 12 × 8 for beds alone; our two 16-wide wings needed 32 × 4 plus an airlock.
- **Building without a launch pad: confirmed by the owner (2026-11-14).** A Spacefarer Module can be built without a Rocket Platform underneath, so the trick works in normal play, not only in sandbox. Still *unverified*: whether bedroom room bonuses apply inside the interior, and how O₂ reaches it (the interior has a gas vent; the supply route from outside isn't worked out yet).

**Dupe flow** (`10.jpg`; 4 shifts × 2, sleep first then rest):
① come down or up the shaft (nature reserve) → ② through the bionic-proof door into the dock corridor, suit off → ③ sleep in a habitat → ④ suit on, back to the shaft → ⑤ washroom (enter from the shaft via door x20 y8, one way, right to left for everyone) → ⑥ pick up food at the fridge window from the kitchen below → ⑦ banquet hall (communal table, phone, soda fountain; one-way door x5) → ⑧ up to the rec room → ⑨ back into the shaft → ⑩ tube (top) or fire pole (bottom) to work.

**Bionic flow** (`11.jpg`; **3 shifts × 2**, no sleep):
① enter via the shaft → ② the **same washroom**, which has 2 gunk extractors beside the 2 lavatories and 2 sinks, one way right to left → ③ power banks + O₂ near the banquet hall and lube room → ④ rec room → ⑤ shaft → ⑥ out.
- **There is no separate bionic zone here**, unlike the closed base. Both kinds share the left block on the same one-way loop. The only bionic ban is the dock corridor (so bionics never take their suits off). The base is semi-open, so everyone else is suited anyway.
- Chargers: 4 for 6 bionics, with robo-arms feeding them. The author's rule (`30.jpg`) is bionics ÷ 2 + 1, the +1 because swaps aren't seamless.

**Door access in this blueprint:**
- Every one-way door is "go left" for `Minion`, `BionicMinion` and `Robot` (x5 y7, x6 y12/14, x17 y18, x20 y8, and the locked pressure door x13 y21).
- x24 y8 (into the dock corridor) is dupes only.
- x35 y3 lets bionics go left only.

**Compared with our decisions:**
- *Docks:* they use 8. 大叔 uses 5, and the reasoning in requirements (2026-11-14) still says about 5 is enough.
- *Comfy beds and rockets:* the habitats hold proper comfy beds (`LuxuryBed`), so the 2026-11-13 comfy-bed requirement is met. The owner relaxed "no rocket beds" on 2026-11-14 if it saves space or suits the design. It clearly saves space, if the build question above has a good answer.
- *Sinks:* they have 2 real sinks in the washroom, which matches our "sinks, not shine bugs" decision.

## 6. Checkpoint orientation (wiki, verified)
"A checkpoint must have an atmo suit dock built on the opposite side its arrow faces." The arrow points to the dirty or suited side, and **docks go on the clean side**. Our v1 and v2 got this backwards.

## 7. Room rules that constrain the bedroom (wiki.gg Room Overlay and Luxury Barracks pages, fetched 2026-11-14)
| Room | Size (tiles) | Key requirements | Morale |
|---|---|---|---|
| Barracks | 12–64 | a bed, no industrial machinery | +1 |
| Luxury Barracks | 12–64 | comfy bed(s), no cots, a decor item, no industrial machinery, **ceiling ≥ 4** | +2 |
| Private Bedroom | 24–64 | exactly one comfy bed, 2 decor items, ceiling ≥ 4, backwall throughout | +3 |
| Nature Reserve | 32–120 | park sign, 4 wild plants, no industrial machinery | +6 |
| Banquet Hall | 32–120 | communal table, decor, a recreation building, a displayed ornament, no mess table | +6 |

- **Ceiling ≥ 4 means 4 clear tiles inside, and a 4-tile storey grid gives only 3.** Per the wiki tip, only one vertical line needs to reach 4, so one raised column (a notch in the slab above) is enough. Earlier wing sketches assumed Luxury Barracks without this.
- **64-tile cap.** A 16-wide wing with 4 interior rows is exactly 64. Adding a checkpoint and 4 docks to such a wing (option A) would push it to 21 × 3 + notch, about 64: right at the limit.
- Whether atmo suit docks and checkpoints count as industrial machinery isn't stated on the wiki. §5 has indirect evidence that they don't.
