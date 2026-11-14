"""Generate the 8+6 base layout: validates overlaps & rooms, emits BNI json + layout json for the page."""
import json, collections, sys

OUT = sys.argv[1] if len(sys.argv) > 1 else '.'

# (w,h) footprints (verified from BNI db / wiki / real blueprints)
SIZE = {
 'InsulationTile':(1,1),'Tile':(1,1),'CarpetTile':(1,1),'FirePole':(1,1),'LadderFast':(1,1),'TravelTube':(1,1),
 'Door':(1,2),'PressureDoor':(1,2),'LuxuryBed':(4,2),'FlowerVaseHangingFancy':(1,2),'FlowerVaseHanging':(1,2),'FlowerVase':(1,1),
 'ItemPedestal':(1,2),'MetalSculpture':(1,3),'MarbleSculpture':(2,3),'Sculpture':(1,3),'SmallSculpture':(1,2),
 'Canvas':(2,2),'CanvasTall':(2,3),'CanvasWide':(3,2),'ParkSign':(1,2),'CeilingLight':(1,1),'SunLamp':(2,4),
 'FlushToilet':(2,3),'WashSink':(2,3),'GunkEmptier':(3,3),'SodaFountain':(2,2),'ArcadeMachine':(3,3),'MassageTable':(2,2),
 'BeachChair':(2,3),'SuitMarker':(1,3),'SuitLocker':(1,3),'TravelTubeEntrance':(3,2),'GourmetCookingStation':(3,3),
 'SpiceGrinder':(2,3),'CookingStation':(3,2),'Refrigerator':(1,2),'SolidConduitOutbox':(1,2),'EspressoMachine':(3,3),
 'MultiMinionDiningTable':(5,1),'OilChanger':(3,3),'GasBottler':(3,2),'ElectrobankCharger':(2,2),'StorageLockerSmart':(1,2),
 'BatterySmart':(2,2),'HydrogenGenerator':(4,3),'SteamTurbine2':(5,3),'Electrolyzer':(2,2),'GasPump':(2,2),
 'WaterPurifier':(4,3),'LiquidConditioner':(2,2),'SuitFabricator':(4,3),'CraftingTable':(2,2),'LiquidReservoir':(2,3),
 'GasFilter':(3,1),
}
SOLID = {'InsulationTile','Tile','CarpetTile','SteamTurbine2'}   # bound rooms
DOORS = {'Door','PressureDoor'}
CEIL = {'FlowerVaseHangingFancy','FlowerVaseHanging','CeilingLight'}
NOFLOOR = CEIL | {'TravelTube','FirePole','LadderFast','GasPump','Canvas','CanvasTall','CanvasWide','SolidConduitOutbox','GasFilter','SteamTurbine2'}

items = []   # dicts: id, x0, y0 (bottom-left), w, h, tag
occ = {}     # (layer, x, y) -> item index
def place(pid, x0, y0, tag='', layer='b', orient=0):
    w, h = SIZE[pid]
    it = dict(id=pid, x0=x0, y0=y0, w=w, h=h, tag=tag, orient=orient, layer=layer)
    for dx in range(w):
        for dy in range(h):
            k = (layer, x0+dx, y0+dy)
            if k in occ:
                o = items[occ[k]]
                raise SystemExit(f'OVERLAP {pid}@{x0},{y0} with {o["id"]}@{o["x0"]},{o["y0"]} at {k}')
            occ[k] = len(items)
    items.append(it)
def tile(pid, x, y): place(pid, x, y, layer='b')
def tiles(pid, xs, ys):
    for x in xs:
        for y in ys:
            if ('b', x, y) not in occ: tile(pid, x, y)

# ---------------- geometry ----------------
W_L = range(1, 17)     # left wing interior x
W_R = range(21, 37)    # right wing interior x
SHAFT_WALL = (17, 20)
FL = {7:1, 6:6, 5:11, 4:16, 3:21, 2:26, 1:31}  # floor -> bottom interior y
TOP = 35

# special: steam turbine replaces floor tiles at y=5, x=32..36 (sits above the steam chamber)
place('SteamTurbine2', 32, 5, 'Steam turbine: recovers aquatuner heat')

# envelope
for y in range(0, TOP+1):
    for x in (0, 37):
        if not (y in (16, 17)):   # middle-floor airlock doors placed later
            tiles('InsulationTile', [x], [y])
tiles('InsulationTile', range(0, 38), [0, TOP])
# floors between storeys
for y in (5, 10, 15, 20, 25, 30):
    tiles('Tile', list(W_L) + list(W_R), [y])
# shaft walls with a door on every storey
for x in SHAFT_WALL:
    for f, yb in FL.items():
        place('Door', x, yb, f'F{f} shaft door')
    for y in range(1, TOP):
        tiles('Tile', [x], [y])
# internal shaft: fire pole down, plastic ladder up
for y in range(1, TOP):
    place('FirePole', 18, y, layer='b'); place('LadderFast', 19, y, layer='b')

# exterior spines (suited zone) running past the base to space and to the bottom
for y in range(-6, TOP + 7):
    place('LadderFast', -2, y); place('FirePole', -1, y)
    place('FirePole', 38, y); place('LadderFast', 39, y)
# airlock exits on the middle floor
place('PressureDoor', 0, 16, 'Mechanized airlock to west spine')
place('PressureDoor', 37, 16, 'Mechanized airlock to east spine')
tiles('InsulationTile', [0, 37], [18, 19])
# transit tube stations hanging off each spine (tube heads west / east)
tiles('Tile', range(-6, -3), [15]); place('TravelTubeEntrance', -6, 16, 'Tube access (west)')
tiles('Tile', range(41, 44), [15]); place('TravelTubeEntrance', 41, 16, 'Tube access (east)')
for x in range(-12, -4): place('TravelTube', x, 18, layer='u')
for x in range(42, 50): place('TravelTube', x, 18, layer='u')

def mirror(x): return 37 - x  # left<->right
# ---------------- F1: standard barracks (8 comfy beds) ----------------
yb = FL[1]
for i in range(4):
    place('LuxuryBed', 1 + 4*i, yb, 'Comfy bed - standard dupe')
    place('FlowerVaseHangingFancy', 2 + 4*i, yb + 2, 'Hanging pot (decor)')
    place('LuxuryBed', 21 + 4*i, yb, 'Comfy bed - standard dupe')
    place('FlowerVaseHangingFancy', 35 - 4*i, yb + 2, 'Hanging pot (decor)')
# ---------------- F2: bionic barracks (6 comfy beds) ----------------
yb = FL[2]
for i in range(3):
    place('LuxuryBed', 1 + 4*i, yb, 'Comfy bed - bionic (defrag)')
    place('FlowerVaseHangingFancy', 2 + 4*i, yb + 2, 'Hanging pot (decor)')
    place('LuxuryBed', 25 + 4*i, yb, 'Comfy bed - bionic (defrag)')
    place('FlowerVaseHangingFancy', 35 - 4*i, yb + 2, 'Hanging pot (decor)')
place('ItemPedestal', 13, yb, 'Pedestal'); place('MetalSculpture', 14, yb, 'Sculpture'); place('CanvasTall', 15, yb, 'Portrait canvas')
place('CanvasTall', 21, yb, 'Portrait canvas'); place('MetalSculpture', 23, yb, 'Sculpture'); place('ItemPedestal', 24, yb, 'Pedestal')
# ---------------- F3: washroom (L) + recreation room (R) ----------------
yb = FL[3]
place('FlushToilet', 1, yb, 'Lavatory'); place('FlushToilet', 3, yb, 'Lavatory')
place('GunkEmptier', 5, yb, 'Gunk Extractor (bionics)')
place('WashSink', 8, yb, 'Sink'); place('WashSink', 10, yb, 'Sink')
place('CanvasTall', 13, yb, 'Portrait canvas'); place('ItemPedestal', 15, yb, 'Pedestal')
place('CeilingLight', 12, yb + 3, 'Light')
place('SodaFountain', 22, yb, 'Soda Fountain'); place('ArcadeMachine', 24, yb, 'Arcade Cabinet')
place('MassageTable', 27, yb, 'Massage Table'); place('BeachChair', 29, yb, 'Beach Chair')
place('SunLamp', 31, yb, 'Sun Lamp (beach chairs +8)'); place('BeachChair', 33, yb, 'Beach Chair')
place('MetalSculpture', 35, yb, 'Sculpture')
# ---------------- F4: airlock + nature reserve floor ----------------
yb = FL[4]
for x in (8, 29):
    place('Door', x, yb, 'Door into suit room'); tiles('Tile', [x], [yb + 2, yb + 3])
place('SuitMarker', 7, yb, 'Atmo Suit Checkpoint', orient=5)
place('SuitMarker', 30, yb, 'Atmo Suit Checkpoint')
for x in range(1, 7):
    place('SuitLocker', x, yb, 'Atmo Suit Dock'); place('SuitLocker', mirror(x), yb, 'Atmo Suit Dock')
# nature reserves (32 tiles each) every out-going dupe walks through
place('ParkSign', 9, yb, 'Park Sign'); place('ParkSign', 28, yb, 'Park Sign')
for x in (10, 13, 14, 15):
    place('FlowerVase', x, yb, 'Wild plant in pot (Mirth Leaf / Bluff Briar)')
    place('FlowerVase', mirror(x), yb, 'Wild plant in pot (Mirth Leaf / Bluff Briar)')
place('MarbleSculpture', 11, yb, 'Marble sculpture'); place('MarbleSculpture', 25, yb, 'Marble sculpture')
for x in (10, 14, 23, 27):
    place('FlowerVaseHanging', x, yb + 2, 'Hanging wild plant')
place('ItemPedestal', 16, yb, 'Pedestal'); place('ItemPedestal', 21, yb, 'Pedestal')
# ---------------- F5: kitchen (L) + banquet hall (R) ----------------
yb = FL[5]
place('SolidConduitOutbox', 1, yb, 'Conveyor receptacle (raw food in)')
place('GourmetCookingStation', 2, yb, 'Gas Range'); place('SpiceGrinder', 5, yb, 'Spice Grinder')
place('CookingStation', 7, yb, 'Electric Grill')
place('StorageLockerSmart', 11, yb, 'Smart storage (salt / caviar / ingredients)')
for x in (13, 14, 15): place('Refrigerator', x, yb, 'Refrigerator (finished meals)')
place('CeilingLight', 9, yb + 3, 'Light')
place('ItemPedestal', 22, yb, 'Pedestal (displayed ornament)')
place('EspressoMachine', 23, yb, 'Espresso Machine (recreation building)')
place('MultiMinionDiningTable', 27, yb, 'Communal Table - the ONE table, 3 seats')
place('MarbleSculpture', 33, yb, 'Marble sculpture'); place('CanvasTall', 35, yb, 'Portrait canvas')
place('CeilingLight', 29, yb + 3, 'Light'); place('CeilingLight', 24, yb + 3, 'Light')
# ---------------- F6: bionic service (L) + power plant (R) ----------------
yb = FL[6]
place('OilChanger', 1, yb, 'Lubrication Station (phyto/crude oil pipe)')
place('GasBottler', 4, yb, 'Canister Filler (O2 for bionics)')
for i in range(4): place('ElectrobankCharger', 7 + 2*i, yb, 'Power Bank Charger')
place('StorageLockerSmart', 15, yb, 'Smart storage (charged power banks)')
place('BatterySmart', 21, yb, 'Smart Battery')
place('HydrogenGenerator', 23, yb, 'Hydrogen Generator'); place('HydrogenGenerator', 27, yb, 'Hydrogen Generator')
# ---------------- F7: life support (L) + workshop/cooling (R) ----------------
yb = FL[7]
place('Electrolyzer', 1, yb, 'Electrolyzer'); place('Electrolyzer', 3, yb, 'Electrolyzer')
place('GasPump', 1, yb + 2, 'Gas pump (H2, top)'); place('GasPump', 3, yb + 2, 'Gas pump (H2, top)')
place('GasPump', 5, yb, 'Gas pump (O2)'); place('GasPump', 7, yb, 'Gas pump (O2)')
place('Door', 10, yb, 'Door'); tiles('Tile', [10], [yb + 2, yb + 3])
place('WaterPurifier', 12, yb, 'Water Sieve (toilet/sink loop)')
place('SuitFabricator', 22, yb, 'Exosuit Forge'); place('CraftingTable', 26, yb, 'Crafting Station (power banks)')
place('LiquidReservoir', 28, yb, 'Coolant buffer')
tiles('InsulationTile', [31], range(1, 5))
place('LiquidConditioner', 33, yb, 'Thermo Aquatuner (in steam chamber)')

# ---------------- validation: rooms ----------------
solid = set(); door = set()
for it in items:
    if it['layer'] != 'b': continue
    for dx in range(it['w']):
        for dy in range(it['h']):
            c = (it['x0'] + dx, it['y0'] + dy)
            if it['id'] in SOLID: solid.add(c)
            if it['id'] in DOORS: door.add(c)
seen = set(); rooms = []
for x in range(1, 37):
    for y in range(1, TOP):
        if (x, y) in solid or (x, y) in door or (x, y) in seen: continue
        stack = [(x, y)]; cells = set()
        while stack:
            c = stack.pop()
            if c in seen or c in solid or c in door: continue
            if not (0 <= c[0] <= 37 and 0 <= c[1] <= TOP): cells.add('LEAK'); continue
            seen.add(c); cells.add(c)
            stack += [(c[0]+1, c[1]), (c[0]-1, c[1]), (c[0], c[1]+1), (c[0], c[1]-1)]
        leak = 'LEAK' in cells; cells.discard('LEAK')
        bs = sorted({it['id'] for it in items if it['layer'] == 'b' and it['id'] not in SOLID|DOORS|{'FirePole','LadderFast'}
                     and any((it['x0']+dx, it['y0']+dy) in cells for dx in range(it['w']) for dy in range(it['h']))})
        xs = [c[0] for c in cells]; ys = [c[1] for c in cells]
        rooms.append(dict(x=(min(xs), max(xs)), y=(min(ys), max(ys)), n=len(cells), leak=leak, b=bs))
for r in rooms: print(r)

# every non-hanging building needs a floor under it
problems = []
for it in items:
    if it['layer'] != 'b' or it['id'] in SOLID|NOFLOOR|DOORS or it['id'] in ('SuitLocker',): pass
    if it['layer'] != 'b' or it['id'] in SOLID | NOFLOOR | DOORS: continue
    for dx in range(it['w']):
        if (it['x0'] + dx, it['y0'] - 1) not in solid: problems.append((it['id'], it['x0'], it['y0'])); break
for it in items:
    if it['id'] in CEIL:
        for dx in range(it['w']):
            if (it['x0']+dx, it['y0']+it['h']) not in solid: problems.append(('ceil', it['id'], it['x0'], it['y0'])); break
print('floor problems:', problems)

# ---------------- emit ----------------
def anchor(it):  # ONI/BNI anchor = bottom-centre cell
    return it['x0'] + (it['w'] - 1) // 2, it['y0']
bni = {'blueprintItems': []}
for it in items:
    ax, ay = anchor(it)
    e = {'id': it['id'], 'position': {'x': ax, 'y': ay}}
    if it['orient']: e['orientation'] = it['orient']
    bni['blueprintItems'].append(e)
json.dump({'friendlyname': '8+6 Mixed Base (8 dupes + 6 bionics)', **bni}, open(f'{OUT}/base_8p6_bni.json', 'w'), indent=1)
json.dump({'items': items, 'rooms': rooms}, open(f'{OUT}/layout.json', 'w'))
print('items', len(items), collections.Counter(i['id'] for i in items).most_common(12))
