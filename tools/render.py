import json,sys,collections
import os
DB=os.path.join(os.path.dirname(os.path.abspath(__file__)),'bni_database.json')
db={b['prefabId']:b for b in json.load(open(DB))['buildings']}
EXTRA={ # newer buildings missing from old DB: (w,h)
 'MultiMinionDiningTable':(5,1),'ElectrobankCharger':(2,2),'GunkEmptier':(3,3),'OilChanger':(3,3),'MilkPress':(2,3),
 'LargeElectrobankDischarger':(2,2),'SmallElectrobankDischarger':(1,1),'BionicUpgradeStation':(3,3),
 'FlowerVaseHangingFancy':(1,2),'LuxuryBed':(4,2),'LadderFast':(1,1),'FirePole':(1,1),'Canvas':(2,2),'CanvasTall':(2,3),'CanvasWide':(3,2),
 'CornerMoulding':(1,1),'CrownMoulding':(1,1),'ParkSign':(1,2),'Element':(1,1),
}
UTIL={'Wire','WireRefined','WireRubber','HighWattageWire','WireRefinedHighWattage','LogicWire','LogicRibbon','GasConduit','GasConduitRadiant','InsulatedGasConduit','LiquidConduit','LiquidConduitRadiant','InsulatedLiquidConduit','SolidConduit','TravelTube','GasConduitPreferentialFlow','CrownMoulding','CornerMoulding','Element'}
def size(i):
    if i in db: s=db[i]['sizeInCells']; return s['x'],s['y']
    return EXTRA.get(i,(1,1))
def cells(it):
    w,h=size(it['id']); x0=it['position']['x']-(w-1)//2; y0=it['position']['y']
    o=it.get('orientation',0)
    if o in (1,3): w,h=h,w
    return [(x0+dx,y0+dy) for dx in range(w) for dy in range(h)]
def render(path, show_util=False):
    d=json.load(open(path)); its=d['data']['blueprintItems']
    print('#',d['name'],'|',d.get('description'),'|',d.get('requiredDlcs'),'|rooms',d.get('rooms'))
    grid={}; legend={}; keys=iter('ACEFGJKLNOPQRSTUVWYZabefhijklmnqrstuvwxyz0123456789@$&*?!;:<>~^=')
    tiles={'Tile':'#','InsulationTile':'I','MeshTile':'+','GasPermeableMembrane':'%','GlassTile':'g','MetalTile':'M','RubberTile':'#','BunkerTile':'B','CarpetTile':'c','PlasticTile':'p','Ladder':'H','LadderFast':'H','FirePole':'|','Door':'d','PressureDoor':'D','ManualPressureDoor':'D','TravelTube':'o','ExteriorWall':'.','Canvas':None}
    unknown=set()
    for it in its:
        i=it['id']
        if i not in db and i not in EXTRA: unknown.add(i)
        if i in UTIL or (i in db and db[i]['isUtility'] and i!='TravelTube'):
            continue
        if i in tiles and tiles[i]:
            ch=tiles[i]
            for c in cells(it): grid.setdefault(c,ch) if ch!='d' and ch!='D' else grid.__setitem__(c,ch)
            continue
        if i not in legend: legend[i]=next(keys,'?')
        for c in cells(it): grid[c]=legend[i]
    xs=[c[0] for c in grid]; ys=[c[1] for c in grid]
    for y in range(max(ys),min(ys)-1,-1):
        print(f'{y:4d} '+''.join(grid.get((x,y),' ') for x in range(min(xs),max(xs)+1)))
    print('bbox',max(xs)-min(xs)+1,'x',max(ys)-min(ys)+1)
    print('legend:',', '.join(f'{v}={k}' for k,v in legend.items()))
    if unknown: print('UNKNOWN sizes:',unknown)
if __name__=='__main__':
    for p in sys.argv[1:]: render(p); print()
