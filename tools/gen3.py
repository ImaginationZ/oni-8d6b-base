"""v3 generator: semi-open 8 dupes + 6 bionics, modelled on 拿个破笔水's semi-open base (docs/findings.md §5b).
Places buildings by bottom-left cell, validates overlaps, floors/ceilings and rooms (size + required buildings),
and emits BNI-format JSON plus layout_v3.json for page3.py.  Usage: python3 gen3.py <outdir>
Coordinates: x 0..45 left to right, y 0..25 bottom to top (outside stubs go beyond)."""
import json, collections, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

# (w,h) footprints. Source: BNI db unless noted. (*) = wiki or measured from 拿个破笔水's blueprints. (?) = unverified.
SIZE = {
 'InsulationTile':(1,1),'Tile':(1,1),'CarpetTile':(1,1),'FirePole':(1,1),'LadderFast':(1,1),'TravelTube':(1,1),
 'TravelTubeWallBridge':(1,1),'Door':(1,2),'PressureDoor':(1,2),'LuxuryBed':(4,2),
 'FlowerVase':(1,1),'FlowerVaseHangingFancy':(1,2),'ItemPedestal':(1,2),'MetalSculpture':(1,3),'CanvasTall':(2,3),
 'ParkSign':(1,2),'CeilingLight':(1,1),'FlushToilet':(2,3),'WashSink':(2,3),'GunkEmptier':(3,3),          # Gunk (*)
 'SodaFountain':(2,2),'ArcadeMachine':(3,3),'MassageTable':(2,2),'BeachChair':(2,3),'MechanicalSurfboard':(2,3),
 'WaterCooler':(2,2),'SuitMarker':(1,3),'SuitLocker':(1,3),'TravelTubeEntrance':(3,2),
 'GourmetCookingStation':(3,3),'SpiceGrinder':(2,3),'CookingStation':(3,2),'MicrobeMusher':(2,3),
 'Refrigerator':(1,2),'StorageLockerSmart':(1,2),'StorageLocker':(1,2),'SolidConduitOutbox':(1,2),'SolidConduitInbox':(1,2),
 'MultiMinionDiningTable':(5,1),'OilChanger':(3,3),'ElectrobankCharger':(2,2),                            # (*)
 'Headquarters':(4,4),'BatterySmart':(2,2),'HydrogenGenerator':(4,3),'SteamTurbine2':(5,3),'Electrolyzer':(2,2),
 'GasPump':(2,2),'WaterPurifier':(4,3),'LiquidConditioner':(2,2),'LiquidReservoir':(2,3),'SuitFabricator':(4,3),
 'ManualGenerator':(2,2),'PowerTransformer':(3,2),'MedicalCot':(3,2),'Apothecary':(2,3),
 'HabitatModuleMedium':(5,4),   # Spacefarer Module: 5x4 per wiki; prefab ID (?)
}
SOLID = {'InsulationTile','Tile','CarpetTile','SteamTurbine2','TravelTubeWallBridge'}   # bound rooms
DOORS = {'Door','PressureDoor'}
CEIL = {'FlowerVaseHangingFancy','CeilingLight'}
NOFLOOR = CEIL | {'SolidConduitInbox','SolidConduitOutbox','TravelTube','FirePole','LadderFast','GasPump',
                  'CanvasTall','SteamTurbine2','TravelTubeWallBridge'}

items = []; occ = {}
def place(pid, x0, y0, tag='', layer='b', orient=0):
    w, h = SIZE[pid]
    if orient in (1, 3): w, h = h, w
    it = dict(id=pid, x0=x0, y0=y0, w=w, h=h, tag=tag, orient=orient, layer=layer)
    for dx in range(w):
        for dy in range(h):
            k = (layer, x0+dx, y0+dy)
            if k in occ:
                o = items[occ[k]]
                raise SystemExit(f'OVERLAP {pid}@{x0},{y0} with {o["id"]}@{o["x0"]},{o["y0"]} at {k}')
            occ[k] = len(items)
    items.append(it)
def tiles(pid, xs, ys):
    for x in xs:
        for y in ys:
            if ('b', x, y) not in occ: place(pid, x, y)

# ---------------- geometry ----------------
W, TOP = 45, 25                       # outer walls at x=0, x=45, y=0, y=25
L = range(1, 21)                      # left block interior x
R = range(26, 45)                     # right block interior x
SH = (22, 23, 24)                     # shaft interior: ladder, fire pole, ladder
LF = [4, 8, 13, 17, 21]               # left floor rows  -> storeys 1-3, 5-7(+banquet 5-12), 9-12, 14-16, 18-20, 22-24
RF = [4, 9, 13, 17, 21]               # right floor rows -> storeys 1-3, 5-8 (corridor), 10-12, 14-16, 18-20, 22-24

ROOMS = []   # (name, cls, x-range, y-range, size rule, required ids) for drawing + checks

# --- special pieces that replace floor tiles (place before floors) ---
place('SteamTurbine2', 40, 17, 'Steam Turbine: sits on the steam chamber, turns aquatuner heat into power')

# --- envelope ---
door_holes = {(22, 0), (23, 0), (22, TOP), (23, TOP), (19, TOP)}
for y in range(0, TOP + 1):
    for x in (0, W):
        tiles('InsulationTile', [x], [y])
for x in range(0, W + 1):
    for y in (0, TOP):
        if (x, y) not in door_holes: tiles('InsulationTile', [x], [y])
# exits: mechanized airlocks laid flat in roof and floor over the ladder + pole
place('PressureDoor', 22, TOP, 'Roof airlock: up to space (ladder continues outside)', orient=1)
place('PressureDoor', 22, 0, 'Floor airlock: down to the bottom of the map', orient=1)

# --- left block floors (banquet column x1-7 is open between y5 and y12, with its own ledge at y8) ---
for y in LF:
    xs = [x for x in L if not (y == 8 and x <= 7)]
    if y == 13: xs = [x for x in xs if x not in (1, 2, 19, 20)]   # horizontal doors placed later
    if y == 17: xs = [x for x in xs if x not in (1, 2)]
    tiles('Tile', xs, [y])
tiles('Tile', range(2, 8), [8])                                   # banquet ledge (x1 stays open for the ladder)
# --- right block floors ---
for y in RF:
    tiles('Tile', [x for x in R if not (y == 17 and 40 <= x <= 44)], [y])

# --- shaft walls with doors (x=21 left, x=25 right) ---
place('Door', 21, 1, 'Kitchen door (from shaft)')
place('Door', 21, 5, 'Washroom entry: one way, right to left, everyone')
place('Door', 21, 14, 'Recreation exit into the shaft')
for y in range(1, TOP):
    if 22 <= y <= 24: continue                                   # open: reserve landing joins the shaft
    tiles('Tile', [21], [y])
for yb, tag in [(1, 'Medical room door'), (5, 'Dock corridor door: DUPES ONLY (bionics no entry)'), (10, 'Gym door'),
                (14, 'Cooling plant door'), (18, 'Power room door'), (22, 'Generator room door')]:
    place('Door', 25, yb, tag)
tiles('Tile', [25], range(1, TOP))
# --- shaft: ladder, fire pole, ladder; continues outside as short stubs ---
for y in range(1, TOP):
    place('LadderFast', 22, y, 'Plastic ladder'); place('FirePole', 23, y, 'Fire pole'); place('LadderFast', 24, y, 'Plastic ladder')
for y in list(range(-3, 0)) + list(range(TOP + 1, TOP + 4)):
    place('LadderFast', 22, y, 'Ladder (outside)'); place('FirePole', 23, y, 'Fire pole (outside)')
tiles('InsulationTile', [24], [0, TOP])
ROOMS.append(('Nature Reserve (shaft + landing)', 'r-park', (15, 24), (1, 24), (32, 120), ['ParkSign']))

# ======================= LEFT BLOCK =======================
# L1 (y1-3): frozen food store + frozen kitchen
place('Door', 7, 1, 'Food store door'); tiles('InsulationTile', [7], [3])
ROOMS.append(('Food store (deep-frozen)', 'r-kit', (1, 6), (1, 3), (1, 999), []))
for x in (1, 2, 3, 4): place('Refrigerator', x, 1, 'Refrigerator (deep-frozen room, belt-fed)')
place('StorageLockerSmart', 5, 1, 'Smart storage (ingredients)'); place('StorageLockerSmart', 6, 1, 'Smart storage (ingredients)')
place('SolidConduitOutbox', 8, 1, 'Conveyor receptacle: raw ingredients in')
place('MicrobeMusher', 9, 1, 'Microbe Musher')
place('GourmetCookingStation', 11, 1, 'Gas Range'); place('CookingStation', 14, 1, 'Electric Grill')
place('SpiceGrinder', 17, 1, 'Spice Grinder')
place('SolidConduitInbox', 20, 1, 'Conveyor loader: finished meals up to the banquet fridge')
place('CeilingLight', 15, 3, 'Light')
ROOMS.append(('Kitchen (deep-frozen)', 'r-kit', (8, 20), (1, 3), (12, 96), ['GourmetCookingStation']))

# L2 (y5-7): washroom x9-20; banquet hall x1-7 spans y5-12
place('WashSink', 9, 5, 'Sink: used walking right to left')
place('FlushToilet', 11, 5, 'Lavatory'); place('FlushToilet', 13, 5, 'Lavatory')
place('GunkEmptier', 15, 5, 'Gunk Extractor (bionics)'); place('GunkEmptier', 18, 5, 'Gunk Extractor (bionics)')
place('Door', 8, 5, 'Washroom exit: one way, right to left'); tiles('Tile', [8], [7])
ROOMS.append(('Washroom (shared)', 'r-wash', (9, 20), (5, 7), (12, 64), ['FlushToilet', 'WashSink']))
place('LadderFast', 1, 5, 'Ladder up to recreation')
for y in range(6, 13): place('LadderFast', 1, y, 'Ladder up to recreation')
place('Refrigerator', 2, 5, 'Meal fridge: the food window, filled from the kitchen below')
place('MultiMinionDiningTable', 3, 5, 'Communal Table: the ONE table, 3 seats, shared by staggered shifts')
place('SodaFountain', 2, 9, 'Soda Fountain (recreation building)'); place('ItemPedestal', 4, 9, 'Pedestal (displayed ornament)')
place('MetalSculpture', 5, 9, 'Sculpture (decor)'); place('CanvasTall', 6, 9, 'Painting (decor)')
place('CeilingLight', 4, 12, 'Light')
place('Door', 8, 9, 'Banquet ledge -> bionic room: BIONICS ONLY, one way right'); tiles('Tile', [8], [11, 12])
ROOMS.append(('Banquet Hall (deep-frozen)', 'r-ban', (1, 7), (5, 12), (32, 120), ['MultiMinionDiningTable', 'ItemPedestal', 'SodaFountain']))

# L3 (y9-12, 4 tall): bionic service + printing pod
place('OilChanger', 9, 9, 'Lubrication Station')
place('SolidConduitOutbox', 12, 9, 'Conveyor receptacle: charged power banks')
place('StorageLockerSmart', 13, 9, 'Smart storage (charged power banks)')
place('Headquarters', 14, 9, 'Printing Pod (new dupes climb to recreation, then pick up a suit at the docks)')
place('ItemPedestal', 18, 9, 'Pedestal')
for y in range(9, 13): place('LadderFast', 20, y, 'Ladder up to recreation')
place('CeilingLight', 11, 12, 'Light; high-pressure O2 vent for bionics also here')
ROOMS.append(('Bionic service + Printing Pod', 'r-bsvc', (9, 20), (9, 12), (1, 999), ['OilChanger', 'Headquarters']))
place('Door', 19, 13, 'Horizontal door up to recreation', orient=1)
place('Door', 1, 13, 'Horizontal door: banquet up to recreation', orient=1)

# L4 (y14-16): recreation room
place('LadderFast', 1, 14, 'Ladder'); place('LadderFast', 1, 15, 'Ladder'); place('LadderFast', 1, 16, 'Ladder')
place('ArcadeMachine', 3, 14, 'Arcade Cabinet'); place('BeachChair', 7, 14, 'Beach Chair')
place('MechanicalSurfboard', 10, 14, 'Mechanical Surfboard'); place('WaterCooler', 13, 14, 'Water Cooler')
place('MetalSculpture', 16, 14, 'Sculpture'); place('CanvasTall', 17, 14, 'Painting'); place('LadderFast', 20, 14, 'Ladder (from the bionic room below)')
place('CeilingLight', 6, 16, 'Light'); place('CeilingLight', 12, 16, 'Light')
ROOMS.append(('Recreation Room', 'r-rec', (1, 20), (14, 16), (12, 96), ['ArcadeMachine']))
place('Door', 1, 17, 'Horizontal door up to massage', orient=1)

# L5 (y18-20): massage clinic + high-pressure O2 module
for y in (18, 19, 20): place('LadderFast', 1, y, 'Ladder')
place('MassageTable', 3, 18, 'Massage Table'); place('CanvasTall', 5, 18, 'Painting (decor)')
tiles('InsulationTile', [7], [18, 19, 20])
ROOMS.append(('Massage Clinic', 'r-rec', (1, 6), (18, 20), (12, 64), ['MassageTable']))
place('Electrolyzer', 9, 18, 'Electrolyzer (high pressure)'); place('Electrolyzer', 11, 18, 'Electrolyzer (high pressure)')
place('GasPump', 13, 19, 'Gas pump: H2, at the top'); place('GasPump', 15, 18, 'Gas pump: O2, at the bottom')
place('GasPump', 17, 18, 'Gas pump: O2, at the bottom')
ROOMS.append(('High-pressure O2 (sealed)', 'r-life', (8, 20), (18, 20), (1, 999), []))

# L6 (y22-24): workshop + nature reserve landing with the tube station
place('SuitFabricator', 2, 22, 'Exosuit Forge'); place('StorageLockerSmart', 7, 22, 'Smart storage (suits, materials)')
place('StorageLockerSmart', 8, 22, 'Smart storage'); place('CeilingLight', 10, 24, 'Light')
place('Door', 14, 22, 'Workshop door (off the landing)'); tiles('Tile', [14], [24])
ROOMS.append(('Workshop', 'r-work', (1, 13), (22, 24), (1, 999), []))
place('FlowerVase', 15, 22, 'Wild plant in pot'); place('FlowerVase', 16, 22, 'Wild plant in pot')
place('FlowerVaseHangingFancy', 15, 23, 'Hanging wild plant'); place('FlowerVaseHangingFancy', 16, 23, 'Hanging wild plant')
place('ParkSign', 17, 22, 'Park Sign')
place('TravelTubeEntrance', 18, 22, 'Transit tube station (tube leaves through the roof, then left and right)')
place('TravelTubeWallBridge', 19, TOP, 'Tube crossing through the roof')
for x in range(-8, W + 9): place('TravelTube', x, TOP + 2, 'Transit tube along the roof, left and right', layer='u')
place('TravelTube', 19, TOP + 1, 'Transit tube', layer='u')

# ======================= RIGHT BLOCK =======================
# R1 (y1-3): medical + bionic chargers
place('MedicalCot', 27, 1, 'Sick Bay cot'); place('Apothecary', 31, 1, 'Apothecary')
place('Door', 35, 1, 'Charger room door'); tiles('Tile', [35], [3])
ROOMS.append(('Medical', 'r-work', (26, 34), (1, 3), (1, 999), []))
place('SolidConduitInbox', 36, 1, 'Conveyor loader: power-bank loop')
for i in range(4): place('ElectrobankCharger', 37 + 2 * i, 1, 'Power Bank Charger (bionics/2 + 1 = 4)')
ROOMS.append(('Bionic chargers', 'r-bsvc', (36, 44), (1, 3), (1, 999), []))

# R2 (y5-8, 4 tall): the bedroom corridor
place('SuitMarker', 26, 5, 'Atmo Suit Checkpoint (arrow points left, to the shaft = suited side)', orient=5)
for x in range(27, 32): place('SuitLocker', x, 5, 'Atmo Suit Dock (5 for 8 suits)')
place('HabitatModuleMedium', 32, 5, 'Spacefarer Module: 4 comfy beds inside (interior from 拿个破笔水)')
place('HabitatModuleMedium', 37, 5, 'Spacefarer Module: 4 comfy beds inside (interior from 拿个破笔水)')
place('ItemPedestal', 43, 5, 'Pedestal'); place('CeilingLight', 29, 8, 'Light')
ROOMS.append(('Dock corridor + 2 habitats (suit-free)', 'r-sleep', (26, 44), (5, 8), (1, 999), ['SuitMarker', 'HabitatModuleMedium']))

# R3 (y10-12): gym (manual generators) + water
for i in range(4): place('ManualGenerator', 26 + 2 * i, 10, 'Manual Generator (idle dupes back-feed the grid)')
place('PowerTransformer', 34, 10, 'Transformer (gym -> main grid)')
place('WaterPurifier', 38, 10, 'Water Sieve (washroom loop)'); place('LiquidReservoir', 43, 10, 'Water buffer')
ROOMS.append(('Gym + water', 'r-pow', (26, 44), (10, 12), (1, 999), []))

# R4 (y14-16): freezer plant + steam chamber
place('LiquidConditioner', 27, 14, 'Thermo Aquatuner: deep-freeze loop (kitchen, food store, banquet)')
place('LiquidReservoir', 30, 14, 'Coolant buffer')
tiles('InsulationTile', [39], [14, 15, 16])
place('LiquidConditioner', 41, 14, 'Thermo Aquatuner: base cooling loop, inside the steam chamber')
ROOMS.append(('Freezer plant', 'r-steam', (26, 38), (14, 16), (1, 999), []))
ROOMS.append(('Steam chamber', 'r-steam', (40, 44), (14, 16), (1, 999), []))

# R5 (y18-20): batteries + transformers (turbine top-right)
place('BatterySmart', 27, 18, 'Smart Battery'); place('BatterySmart', 29, 18, 'Smart Battery')
place('PowerTransformer', 32, 18, 'Large transformer'); place('PowerTransformer', 35, 18, 'Large transformer')
tiles('InsulationTile', [39], [18, 19, 20])
ROOMS.append(('Power control', 'r-pow', (26, 38), (18, 20), (1, 999), []))

# R6 (y22-24): hydrogen generators
for i in range(4): place('HydrogenGenerator', 26 + 4 * i, 22, 'Hydrogen Generator (fed by the O2 module H2)')
place('BatterySmart', 43, 22, 'Smart Battery')
ROOMS.append(('Generators', 'r-pow', (26, 44), (22, 24), (1, 999), []))

# ---------------- validation ----------------
solid = set(); door = set()
for it in items:
    if it['layer'] != 'b': continue
    for dx in range(it['w']):
        for dy in range(it['h']):
            c = (it['x0'] + dx, it['y0'] + dy)
            if it['id'] in SOLID: solid.add(c)
            if it['id'] in DOORS: door.add(c)
def cells_of(it): return [(it['x0'] + dx, it['y0'] + dy) for dx in range(it['w']) for dy in range(it['h'])]
seen = set(); rooms = []
for x in range(1, W):
    for y in range(1, TOP):
        if (x, y) in solid or (x, y) in door or (x, y) in seen: continue
        stack = [(x, y)]; cells = set(); leak = False
        while stack:
            c = stack.pop()
            if c in seen or c in solid or c in door: continue
            if not (0 <= c[0] <= W and 0 <= c[1] <= TOP): leak = True; continue
            seen.add(c); cells.add(c)
            stack += [(c[0]+1, c[1]), (c[0]-1, c[1]), (c[0], c[1]+1), (c[0], c[1]-1)]
        bs = collections.Counter(it['id'] for it in items if it['layer'] == 'b' and it['id'] not in SOLID | DOORS
                                 and any(c in cells for c in cells_of(it)))
        xs = [c[0] for c in cells]; ys = [c[1] for c in cells]
        rooms.append(dict(x=(min(xs), max(xs)), y=(min(ys), max(ys)), n=len(cells), leak=leak, b=dict(bs), cells=list(cells)))
errors = []; named_out = []
for r in rooms:
    if r['leak']: errors.append(f'LEAK {r}')
for name, cls, xr, yr, (lo, hi), req in ROOMS:
    m = [r for r in rooms if xr[0] <= r['x'][0] and r['x'][1] <= xr[1] and yr[0] <= r['y'][0] and r['y'][1] <= yr[1]]
    big = max(m, key=lambda r: r['n']) if m else None
    if not big: errors.append(f'NO ROOM for {name}'); continue
    if not (lo <= big['n'] <= hi): errors.append(f'SIZE {name}: {big["n"]} not in {lo}-{hi}')
    for q in req:
        if q not in big['b']: errors.append(f'MISSING {q} in {name}')
    print(f'{name:42s} {big["n"]:4d} tiles  x{big["x"]} y{big["y"]}')
    named_out.append(dict(name=name, cls=cls, n=big['n'], b=big['b'], cells=sorted(big['cells'])))
for it in items:
    if it['layer'] != 'b' or it['id'] in SOLID | NOFLOOR | DOORS: continue
    if any((it['x0'] + dx, it['y0'] - 1) not in solid for dx in range(it['w'])):
        if it['id'] == 'LadderFast': continue
        errors.append(f'NO FLOOR under {it["id"]}@{it["x0"]},{it["y0"]}')
for it in items:
    if it['id'] in CEIL and any((it['x0'] + dx, it['y0'] + it['h']) not in solid for dx in range(it['w'])):
        errors.append(f'NO CEILING over {it["id"]}@{it["x0"]},{it["y0"]}')
for it in items:
    if it['id'] in DOORS and it['orient'] == 0 and it['x0'] not in (0, W):
        if (it['x0'], it['y0'] - 1) not in solid: errors.append(f'NO FLOOR under door @{it["x0"]},{it["y0"]}')
print('\n'.join(errors) if errors else 'validation: OK')

# ---------------- emit ----------------
def anchor(it): return it['x0'] + (it['w'] - 1) // 2, it['y0']
bni = {'blueprintItems': []}
for it in items:
    ax, ay = anchor(it)
    e = {'id': it['id'], 'position': {'x': ax, 'y': ay}}
    if it['orient']: e['orientation'] = it['orient']
    bni['blueprintItems'].append(e)
json.dump({'friendlyname': '8d6b semi-open base v3 (8 dupes + 6 bionics)', **bni}, open(f'{OUT}/base_8d6b_v3_bni.json', 'w'), indent=1)
json.dump({'items': items, 'named': named_out, 'W': W, 'TOP': TOP, 'errors': errors}, open(f'{OUT}/layout_v3.json', 'w'))
print('items', len(items), 'envelope', W + 1, 'x', TOP + 1)
sys.exit(1 if errors else 0)
