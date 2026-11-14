import json, html, sys
D = sys.argv[1]
L = json.load(open(f'{D}/layout.json'))
BNI = open(f'{D}/base_8p6_bni.json').read()
items = L['items']

C = 15  # px per tile
X0, X1, Y0, Y1 = -9, 46, -3, 39
W, H = (X1 - X0 + 1) * C, (Y1 - Y0 + 1) * C
def sx(x): return (x - X0) * C
def sy(y): return (Y1 - y) * C

ROOMS = [  # (xrange, yrange, class, label)
 ((1,16),(31,34),'r-sleep','Luxury Barracks · 4 dupes'), ((21,36),(31,34),'r-sleep','Luxury Barracks · 4 dupes'),
 ((1,16),(26,29),'r-bion','Luxury Barracks · 3 bionics'), ((21,36),(26,29),'r-bion','Luxury Barracks · 3 bionics'),
 ((1,16),(21,24),'r-wash','Washroom'), ((21,36),(21,24),'r-rec','Recreation Room'),
 ((1,7),(16,19),'r-suit','Suit airlock'), ((9,16),(16,19),'r-park','Nature Reserve'),
 ((21,28),(16,19),'r-park','Nature Reserve'), ((30,36),(16,19),'r-suit','Suit airlock'),
 ((1,16),(11,14),'r-kit','Kitchen'), ((21,36),(11,14),'r-ban','Banquet Hall'),
 ((1,16),(6,9),'r-bsvc','Bionic service'), ((21,36),(6,9),'r-pow','Power Plant'),
 ((1,9),(1,4),'r-life','SPOM'), ((11,16),(1,4),'r-life','Sieve'),
 ((21,30),(1,4),'r-work','Workshop'), ((32,36),(1,4),'r-steam','Steam'),
 ((18,19),(1,34),'r-shaft',''),
]
AB = {'LuxuryBed':'Comfy Bed','FlushToilet':'Lav','WashSink':'Sink','GunkEmptier':'Gunk Ext.','SodaFountain':'Soda',
 'ArcadeMachine':'Arcade','MassageTable':'Massage','BeachChair':'Beach','SunLamp':'Sun','SuitMarker':'CP','SuitLocker':'Dock',
 'TravelTubeEntrance':'Tube','GourmetCookingStation':'Gas Range','SpiceGrinder':'Spice','CookingStation':'Grill',
 'Refrigerator':'Fr','SolidConduitOutbox':'In','EspressoMachine':'Espresso','MultiMinionDiningTable':'Communal Table',
 'OilChanger':'Lube','GasBottler':'Canister','ElectrobankCharger':'Chg','StorageLockerSmart':'St','BatterySmart':'Bat',
 'HydrogenGenerator':'H₂ Gen','SteamTurbine2':'Turbine','Electrolyzer':'Elec','GasPump':'Pump','WaterPurifier':'Sieve',
 'LiquidConditioner':'AqT','SuitFabricator':'Suit Forge','CraftingTable':'Craft','LiquidReservoir':'Res','ParkSign':'P',
 'MarbleSculpture':'Sc','MetalSculpture':'Sc','CanvasTall':'Art','ItemPedestal':'Pd','FlowerVase':'✿','FlowerVaseHanging':'✿',
 'FlowerVaseHangingFancy':'✿','CeilingLight':'·'}

s = [f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Side view of the 8+6 base, tile grid">']
s.append(f'<defs><pattern id="g" width="{C}" height="{C}" patternUnits="userSpaceOnUse"><path d="M {C} 0 L 0 0 0 {C}" fill="none" class="grid"/></pattern></defs>')
s.append(f'<rect x="0" y="0" width="{W}" height="{H}" fill="url(#g)"/>')
for (xr, yr, cls, lab) in ROOMS:
    s.append(f'<rect class="{cls}" x="{sx(xr[0])}" y="{sy(yr[1])}" width="{(xr[1]-xr[0]+1)*C}" height="{(yr[1]-yr[0]+1)*C}"/>')
# tiles & structure
for it in items:
    i = it['id']; x, y, w, h = it['x0'], it['y0'], it['w'], it['h']
    if i in ('Tile', 'InsulationTile'):
        s.append(f'<rect class="{"ins" if i=="InsulationTile" else "tile"}" x="{sx(x)}" y="{sy(y)}" width="{C}" height="{C}"/>')
for it in items:
    i = it['id']; x, y, w, h = it['x0'], it['y0'], it['w'], it['h']
    if i == 'FirePole':
        s.append(f'<line class="pole" x1="{sx(x)+C/2}" x2="{sx(x)+C/2}" y1="{sy(y)}" y2="{sy(y)+C}"/>')
    elif i == 'LadderFast':
        s.append(f'<g class="ladder"><line x1="{sx(x)+3}" x2="{sx(x)+3}" y1="{sy(y)}" y2="{sy(y)+C}"/><line x1="{sx(x)+C-3}" x2="{sx(x)+C-3}" y1="{sy(y)}" y2="{sy(y)+C}"/><line x1="{sx(x)+3}" x2="{sx(x)+C-3}" y1="{sy(y)+C/2}" y2="{sy(y)+C/2}"/></g>')
    elif i == 'TravelTube':
        s.append(f'<rect class="tube" x="{sx(x)}" y="{sy(y)+4}" width="{C}" height="{C-8}"/>')
    elif i in ('Door', 'PressureDoor'):
        s.append(f'<rect class="{"pdoor" if i=="PressureDoor" else "door"}" x="{sx(x)+3}" y="{sy(y+h-1)}" width="{C-6}" height="{h*C}"><title>{html.escape(it["tag"] or i)}</title></rect>')
for it in items:
    i = it['id']; x, y, w, h = it['x0'], it['y0'], it['w'], it['h']
    if i in ('Tile','InsulationTile','FirePole','LadderFast','TravelTube','Door','PressureDoor'): continue
    cls = 'b-deco' if i in ('FlowerVase','FlowerVaseHanging','FlowerVaseHangingFancy','MarbleSculpture','MetalSculpture','CanvasTall','ItemPedestal','ParkSign','CeilingLight') else 'b'
    if i in ('LuxuryBed',): cls = 'b-bed'
    if i in ('SuitLocker','SuitMarker','TravelTubeEntrance'): cls = 'b-suit'
    if i == 'MultiMinionDiningTable': cls = 'b-key'
    s.append(f'<g><title>{html.escape(it["tag"] or i)} ({i}, {w}×{h})</title><rect class="{cls}" x="{sx(x)+1}" y="{sy(y+h-1)+1}" width="{w*C-2}" height="{h*C-2}" rx="2"/>')
    lab = AB.get(i, i[:4])
    fs = 8 if len(lab) * 5 > w * C - 2 else 9
    if len(lab) * 4.6 > w * C and h >= 2 and w == 1:
        pass
    vertical = (w == 1 and h >= 2 and len(lab) > 2)
    cx, cy = sx(x) + w * C / 2, sy(y + h - 1) + h * C / 2
    if vertical:
        s.append(f'<text class="lbl" x="{cx}" y="{cy}" font-size="8" transform="rotate(-90 {cx} {cy})">{html.escape(lab)}</text></g>')
    else:
        s.append(f'<text class="lbl" x="{cx}" y="{cy}" font-size="{fs}">{html.escape(lab)}</text></g>')
# storey labels & annotations
for f, yb in {1:31,2:26,3:21,4:16,5:11,6:6,7:1}.items():
    s.append(f'<text class="axis" x="{sx(-8)}" y="{sy(yb)+-C*1.2}">F{f}</text>')
for (xr, yr, cls, lab) in ROOMS:
    if lab:
        s.append(f'<text class="rlab" x="{sx(xr[0])+3}" y="{sy(yr[1])+10}">{html.escape(lab)}</text>')
s.append(f'<text class="note" x="{sx(-2)-2}" y="{sy(Y1)+12}" text-anchor="end">↑ space</text>')
s.append(f'<text class="note" x="{sx(-2)-2}" y="{sy(Y0)-4}" text-anchor="end">↓ bottom</text>')
s.append(f'<text class="note" x="{sx(41)+46}" y="{sy(Y1)+12}" text-anchor="end">space ↑</text>')
s.append(f'<text class="note" x="{sx(41)+46}" y="{sy(Y0)-4}" text-anchor="end">bottom ↓</text>')
s.append(f'<text class="note" x="{sx(-9)+2}" y="{sy(19)+2}">← tube</text>')
s.append(f'<text class="note" x="{sx(46)-2}" y="{sy(19)+2}" text-anchor="end">tube →</text>')
s.append('</svg>')
svg = '\n'.join(s)

tpl = open(sys.argv[2]).read()
out = tpl.replace('%%SVG%%', svg).replace('%%BNI%%', html.escape(BNI))
open(sys.argv[3], 'w').write(out)
print('ok', len(out))
