"""Build the v3 design page: python3 page3.py <dir with layout_v3.json + base_8d6b_v3_bni.json> <out.html>
Uses head.part (CSS) + body3.part (text, with %%SVG%%, %%BNI%%, %%ROOMS%% placeholders)."""
import json, html, sys, os
T = os.path.dirname(os.path.abspath(__file__))
D, OUTF = sys.argv[1], sys.argv[2]
L = json.load(open(f'{D}/layout_v3.json'))
BNI = open(f'{D}/base_8d6b_v3_bni.json').read()
items = L['items']

C = 15
X0, X1, Y0, Y1 = -9, 54, -4, 29
W, H = (X1 - X0 + 1) * C, (Y1 - Y0 + 1) * C
def sx(x): return (x - X0) * C
def sy(y): return (Y1 - y) * C

AB = {'LuxuryBed':'Comfy Bed','FlushToilet':'Lav','WashSink':'Sink','GunkEmptier':'Gunk','SodaFountain':'Soda',
 'ArcadeMachine':'Arcade','MassageTable':'Massage','BeachChair':'Beach','MechanicalSurfboard':'Surf','WaterCooler':'Cooler',
 'SuitMarker':'CP','SuitLocker':'Dock','TravelTubeEntrance':'Tube','GourmetCookingStation':'Range','SpiceGrinder':'Spice',
 'CookingStation':'Grill','MicrobeMusher':'Mush','Refrigerator':'Fr','SolidConduitOutbox':'In','SolidConduitInbox':'Ld',
 'MultiMinionDiningTable':'Communal Table','OilChanger':'Lube','ElectrobankCharger':'Chg','StorageLockerSmart':'St',
 'StorageLocker':'St','BatterySmart':'Bat','HydrogenGenerator':'H₂ Gen','SteamTurbine2':'Turbine','Electrolyzer':'Elec',
 'GasPump':'Pump','WaterPurifier':'Sieve','LiquidConditioner':'AqT','LiquidReservoir':'Res','SuitFabricator':'Suit Forge',
 'ManualGenerator':'Gym','PowerTransformer':'Xfmr','MedicalCot':'Cot','Apothecary':'Apoth','ParkSign':'P',
 'MetalSculpture':'Sc','CanvasTall':'Art','ItemPedestal':'Pd','FlowerVase':'✿','FlowerVaseHangingFancy':'✿',
 'CeilingLight':'·','Headquarters':'Printing Pod','HabitatModuleMedium':'Habitat · 4 beds'}
DECO = {'FlowerVase','FlowerVaseHangingFancy','MetalSculpture','CanvasTall','ItemPedestal','ParkSign','CeilingLight'}

s = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Side view of the v3 semi-open base, tile grid">']
s.append(f'<defs><pattern id="g" width="{C}" height="{C}" patternUnits="userSpaceOnUse"><path d="M {C} 0 L 0 0 0 {C}" fill="none" class="grid"/></pattern></defs>')
s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#g)"/>')
for r in L['named']:
    for (x, y) in r['cells']:
        s.append(f'<rect class="{r["cls"]}" x="{sx(x)}" y="{sy(y)}" width="{C}" height="{C}"/>')
for it in items:
    i, x, y = it['id'], it['x0'], it['y0']
    if i in ('Tile', 'InsulationTile', 'TravelTubeWallBridge'):
        cls = {'Tile': 'tile', 'InsulationTile': 'ins', 'TravelTubeWallBridge': 'tube'}[i]
        s.append(f'<rect class="{cls}" x="{sx(x)}" y="{sy(y)}" width="{C}" height="{C}"/>')
for it in items:
    i, x, y, w, h = it['id'], it['x0'], it['y0'], it['w'], it['h']
    if i == 'FirePole':
        s.append(f'<line class="pole" x1="{sx(x)+C/2}" x2="{sx(x)+C/2}" y1="{sy(y)}" y2="{sy(y)+C}"/>')
    elif i == 'LadderFast':
        s.append(f'<g class="ladder"><line x1="{sx(x)+3}" x2="{sx(x)+3}" y1="{sy(y)}" y2="{sy(y)+C}"/><line x1="{sx(x)+C-3}" x2="{sx(x)+C-3}" y1="{sy(y)}" y2="{sy(y)+C}"/><line x1="{sx(x)+3}" x2="{sx(x)+C-3}" y1="{sy(y)+C/2}" y2="{sy(y)+C/2}"/></g>')
    elif i == 'TravelTube':
        s.append(f'<rect class="tube" x="{sx(x)}" y="{sy(y)+4}" width="{C}" height="{C-8}"/>')
    elif i in ('Door', 'PressureDoor'):
        cls = 'pdoor' if i == 'PressureDoor' else 'door'
        t = html.escape(it['tag'] or i)
        if w == 1: s.append(f'<rect class="{cls}" x="{sx(x)+3}" y="{sy(y+h-1)}" width="{C-6}" height="{h*C}"><title>{t}</title></rect>')
        else: s.append(f'<rect class="{cls}" x="{sx(x)}" y="{sy(y)+3}" width="{w*C}" height="{C-6}"><title>{t}</title></rect>')
for it in items:
    i, x, y, w, h = it['id'], it['x0'], it['y0'], it['w'], it['h']
    if i in ('Tile','InsulationTile','FirePole','LadderFast','TravelTube','TravelTubeWallBridge','Door','PressureDoor'): continue
    cls = 'b-deco' if i in DECO else 'b'
    if i in ('LuxuryBed', 'HabitatModuleMedium'): cls = 'b-bed'
    if i in ('SuitLocker', 'SuitMarker', 'TravelTubeEntrance'): cls = 'b-suit'
    if i == 'MultiMinionDiningTable': cls = 'b-key'
    s.append(f'<g><title>{html.escape(it["tag"] or i)} ({i}, {w}×{h})</title><rect class="{cls}" x="{sx(x)+1}" y="{sy(y+h-1)+1}" width="{w*C-2}" height="{h*C-2}" rx="2"/>')
    lab = AB.get(i, i[:4]); cx, cy = sx(x) + w*C/2, sy(y+h-1) + h*C/2
    if w == 1 and h >= 2 and len(lab) > 2:
        s.append(f'<text class="lbl" x="{cx}" y="{cy}" font-size="8" transform="rotate(-90 {cx} {cy})">{html.escape(lab)}</text></g>')
    else:
        fs = 8 if len(lab) * 5.2 > w*C - 2 else 9
        s.append(f'<text class="lbl" x="{cx}" y="{cy}" font-size="{fs}">{html.escape(lab)}</text></g>')
# room labels at the top-left cell of each room
LABEL = {'Nature Reserve (shaft + landing)': 'Nature Reserve', 'Dock corridor + 2 habitats (suit-free)': 'Bedroom corridor (suits off)',
         'Bionic service + Printing Pod': 'Bionic service · Pod', 'High-pressure O2 (sealed)': 'High-pressure O₂'}
for r in L['named']:
    name = LABEL.get(r['name'], r['name'].split(' (')[0])
    top = max(c[1] for c in r['cells']); x = min(c[0] for c in r['cells'] if c[1] == top)
    if r['name'].startswith('Nature'): x, top = 15, 24
    s.append(f'<text class="rlab" x="{sx(x)+2}" y="{sy(top)+10}">{html.escape(name)}</text>')
for n, yb in enumerate([1, 5, 9, 14, 18, 22], 1):
    s.append(f'<text class="axis" x="{sx(-8)}" y="{sy(yb)+2}">L{n}</text>')
for n, yb in enumerate([1, 5, 10, 14, 18, 22], 1):
    s.append(f'<text class="axis" x="{sx(47)}" y="{sy(yb)+2}">R{n}</text>')
s.append(f'<text class="note" x="{sx(25)+4}" y="{sy(Y1)+12}">↑ space (ladder + pole continue)</text>')
s.append(f'<text class="note" x="{sx(25)+4}" y="{sy(Y0)-4}">↓ bottom of the map</text>')
s.append(f'<text class="note" x="{sx(-9)+2}" y="{sy(28)+2}">← tube</text>')
s.append(f'<text class="note" x="{sx(54)-2}" y="{sy(28)+2}" text-anchor="end">tube →</text>')
s.append('</svg>')

rows = []
for r in L['named']:
    b = ', '.join(f'{AB.get(k, k)}{" ×"+str(v) if v > 1 else ""}' for k, v in r['b'].items()
                  if k not in ('LadderFast', 'FirePole', 'CeilingLight', 'TravelTube'))
    rows.append(f'<tr><td>{html.escape(r["name"])}</td><td class="n">{r["n"]}</td><td>{html.escape(b)}</td></tr>')

head = open(f'{T}/head.part').read().replace('<title>Twin-Spine 8+6 Base</title>', '<title>Semi-Open 8d6b Base</title>')
body = open(f'{T}/body3.part').read()
out = head + body.replace('%%SVG%%', '\n'.join(s)).replace('%%BNI%%', html.escape(BNI)).replace('%%ROOMS%%', '\n'.join(rows))
open(OUTF, 'w').write(out)
print('ok', len(out))
