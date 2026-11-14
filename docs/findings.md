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

## 5. 拿个破笔水's actual blueprint (`references/napobi_save_blueprint/napobi_8p6.blueprint`)
- 31 × 33 tiles, 1661 entries (Blueprints-mod JSON, `blueprintVersion` 3). There's an ASCII render in `napobi_ascii.txt` (rough: logic parts are drawn too).
- Notable building IDs it confirms exist in-game:
  - Bionic: `GunkEmptier`, `OilChanger`, `ElectrobankCharger`
  - Dupe furniture and rooms: `LuxuryBed`, `MultiMinionDiningTable`, `Telephone`, `SpiceGrinder`
  - Suits: `SuitLocker`, `SuitMarker`
  - Kitchen: `Deepfryer`, `Smoker`, `MicrobeMusher`
- The bionic side also has `HandSanitizer` and `MedicalCot`.
- **Next step:** parse it properly (rooms, which buildings sit where, door access isn't stored) and compare with the Yuque screenshots.

## 6. Checkpoint orientation (wiki, verified)
"A checkpoint must have an atmo suit dock built on the opposite side its arrow faces." The arrow points to the dirty or suited side, and **docks go on the clean side**. Our v1 and v2 got this backwards.
