# v3 plan (draft for the owner's approval, 2026-11-14)

**Basis:** 拿个破笔水's semi-open base (findings §5b) is the model, changed only where the owner's decisions differ. Other inputs: 大叔's base (findings §1–4) and the decisions in `docs/requirements.md`. Nothing gets built until the owner approves this plan.

## 1. Overall shape
Two blocks either side of a 3-wide central shaft, on the 4-tile storey grid. Target size is about **45 × 29** (7 storeys); the exact size comes out of the build.

```
          LEFT: living (~20 wide)        SHAFT   RIGHT: utilities + beds (~20 wide)
 S7  massage │ recreation (top)          ║ R ║   power: H2 generators, smart battery, transformers
 S6  recreation (wind tunnel, arcade…)   ║ E ║   cooling: steam turbine + liquid conditioner
 S5  banquet │ printing pod, O2, lube    ║ S ║   gym (manual generators) + sewage reed
 S4  banquet │ washroom ◄─ one way       ║ E ║   dock corridor ► checkpoint, 5 docks, 2 habitats
 S3  kitchen (frozen), fridge window     ║ R ║   misc: suit fabricator, med cot, apothecary
 S2  food store (frozen)                 ║ V ║   bionic chargers (4) + conveyor
            fire pole · ladder · tube in the shaft; horizontal doors top and bottom
```

## 2. Central shaft = nature reserve = up/down route
- It holds a fire pole, a ladder and a transit tube, as in 拿个破笔水's base. Wild plants (on natural tiles or in planters) and a park sign make it a Nature Reserve (32–120 tiles).
- Every dupe passes it going to bed and going to work, for +6 morale.
- Horizontal doors at the top (to space) and bottom (to the map floor).
- The tube leaves at the top and bottom through wall bridges and runs **left and right** along the base's outer edge, which meets the transit-tube requirement.

## 3. Bedroom: the habitat corridor (right block, S4)
- Order along the corridor: door from the shaft (**dupes only**) → checkpoint (arrow pointing to the shaft) → **5 docks** → **2 Spacefarer Modules**, 4 comfy beds each, using 拿个破笔水's interior layout. That's about 17 × 4 on the map.
- Only these interiors are suit-free. Everywhere else, dupes stay suited (semi-open).
- O₂ reaches the docks first, then the habitats (as 大叔 does). The exact feed route into a module still has to be worked out.

## 4. Dupe loop (4 shifts × 2, sleep first, then rest)
1. Shaft (reserve)
2. Dock corridor: suit off
3. Sleep in a habitat
4. Suit on, back to the shaft
5. **Washroom** on the same storey across the shaft: 2 lavatories, 2 sinks, one way right to left
6. Pick up food at the fridge window from the frozen kitchen below
7. Banquet hall: **one communal table**, shared by staggered schedules
8. Up to recreation
9. Back into the shaft
10. Fire pole down or tube out to work

## 5. Bionics (3 shifts × 2, no beds, 6 h of downtime every 3 cycles)
- They share the left block's one-way loop: shaft → washroom (**2 gunk extractors** beside the lavatories) → power banks + O₂ + lube station → recreation → shaft → out.
- They are barred only from the dock corridor, so they never take suits off. There is no separate bionic wing (拿个破笔水's semi-open approach; their closed base had one).
- 4 chargers on the right, fed by a conveyor loop (the author's rule: bionics ÷ 2 + 1).

## 6. Utilities and atmosphere
- **High-pressure O₂ electrolyzer** in the left block. One more for the docks if needed (大叔 uses one module per side).
- **Kitchen and food store deep-frozen** (owner's decision). Food is cooked below and passed up through the fridge window.
- **Sinks, no shine bugs** (owner's decision). One reed plant takes all the sewage.
- Power: hydrogen generators + smart battery, plus manual generators back-feeding through a transformer in the gym.
- Cooling: steam turbine room with a liquid conditioner; the cold loop wraps the life-support area.

## 7. Deliberately left out for now
- Docked O₂ storage rockets (owner: not decided).
- Lube-station timer doors (optional, per 大叔).

## 8. To check (marked unverified until done)
- Do bedroom morale bonuses apply inside a module? (Owner, by hovering in-game.)
- The O₂ feed into the modules.
- Do Spacefarer Modules need clear space above them? (Their base has rooms right above.)
- Is a frozen banquet hall OK with the decor and recreation items it needs?

## 9. Build steps after approval
1. `tools/gen3.py` (based on `gen2.py`): place the layout and validate overlaps, rooms (sizes and required buildings) and floors.
2. Render the section page and publish it as an Artifact for the phone.
3. Update PROGRESS and findings.
