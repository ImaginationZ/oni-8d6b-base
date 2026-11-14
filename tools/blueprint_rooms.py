"""Analyse a Blueprints-mod .blueprint: structure/furniture ASCII layers, flood-filled rooms, door access and checkpoint data.
Usage: python3 -I tools/blueprint_rooms.py <file.blueprint>
Caveats: natural tiles and plants are not in blueprints, so rooms can over-merge; sizes for some DLC buildings come from render.EXTRA.
AccessControl values: 0 both, 1 goLeft, 2 goRight, 3 neither. Door requestedState: 0 auto, 1 open, 2 locked (ONI enums, from memory)."""
import json,sys,collections
import os; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
import render
render.EXTRA.update({'Telephone':(1,2)})
d=json.load(open(sys.argv[1]))
B=[]
for x in d['buildings']:
    o=x.get('offset',{}); B.append(dict(id=x['buildingdef'],x=o.get('x',0),y=o.get('y',0),o=x.get('orientation',0),bd={kv['Key']:kv['Value'] for kv in x.get('buildingData') or []}))
def cells(b):
    w,h=render.size(b['id']); 
    if b['o'] in (1,3): w,h=h,w
    x0=b['x']-(w-1)//2
    return [(x0+i,b['y']+j) for i in range(w) for j in range(h)]
SOLID={'InsulationTile','MetalTile','Tile','CarpetTile','MeshTile','GlassTile','GasPermeableMembrane','StorageTile','TravelTubeWallBridge','FloorSwitch'}
DOOR={'Door','PressureDoor'}
struct={}
CH={'FloorSwitch':'W','InsulationTile':'I','MetalTile':'M','Tile':'#','CarpetTile':'c','MeshTile':'+','GlassTile':'g','GasPermeableMembrane':'%','StorageTile':'S','TravelTubeWallBridge':'E','Door':'d','PressureDoor':'D','LadderFast':'H','FirePole':'|','TravelTube':'o','TravelTubeEntrance':'T'}
for b in B:
    if b['id'] in CH:
        for c in cells(b): struct[c]=CH[b['id']]
FURN_SKIP=set(render.UTIL)|SOLID|DOOR|{'LadderFast','FirePole','TravelTube','TravelTubeEntrance','LiquidConduitBridge','GasConduitBridge','LogicWireBridge','WireRefinedBridgeHighWattage','ContactConductivePipeBridge','LogicGateNOT','LogicGateFILTER','LogicGateBUFFER','LogicRibbonWriter','LiquidConduitElementSensor','LiquidConduitTemperatureSensor','CeilingLight','LogicWire','WireRubber','TravelTubeWallBridge','SolidConduitInbox','SolidConduitOutbox','SolidTransferArm','SolidVent','GasVent','LiquidVent','GasVentHighPressure'}
keys=iter('ABCFGJKLNOPQRUVWXYZabefhijklmnpqrstuvwxyz0123456789@$&*!;:<>~^=?')
leg={}; furn={}
for b in B:
    if b['id'] in FURN_SKIP: continue
    if b['id'] not in leg: leg[b['id']]=next(keys)
    for c in cells(b): furn[c]=leg[b['id']]
allc=list(struct)+list(furn)
X0=min(c[0] for c in allc);X1=max(c[0] for c in allc);Y0=min(c[1] for c in allc);Y1=max(c[1] for c in allc)
hdr='     '+''.join(str(x%10) for x in range(X0,X1+1))
print(hdr+'   '+hdr[5:])
for y in range(Y1,Y0-1,-1):
    s=''.join(struct.get((x,y),'.') for x in range(X0,X1+1))
    f=''.join(furn.get((x,y), struct.get((x,y),' ') if struct.get((x,y),' ') in 'dD|H' else ('·' if (x,y) in struct and struct[(x,y)] not in 'dD|H' else ' ')) for x in range(X0,X1+1))
    print(f'{y:3d}  {s}   {f}')
print('legend:',', '.join(f'{v}={k}' for k,v in leg.items()))
# rooms: flood fill over non-solid cells, bounded by solid + doors
wall=lambda c: c in struct and struct[c] in 'IMcg+%#SEdDW'
seen={};rooms=[]
for y in range(Y0,Y1+1):
  for x in range(X0,X1+1):
    c=(x,y)
    if wall(c) or c in seen: continue
    st=[c]; seen[c]=len(rooms); cs=[]
    out=False
    while st:
        p=st.pop(); cs.append(p)
        for q in ((p[0]+1,p[1]),(p[0]-1,p[1]),(p[0],p[1]+1),(p[0],p[1]-1)):
            if not(X0<=q[0]<=X1 and Y0<=q[1]<=Y1): out=True; continue
            if wall(q) or q in seen: continue
            seen[q]=len(rooms); st.append(q)
    rooms.append((cs,out))
print()
for i,(cs,out) in enumerate(rooms):
    S=set(cs)
    ids=collections.Counter(b['id'] for b in B if b['id'] not in FURN_SKIP and (b['x'],b['y']) in S)
    xs=[c[0] for c in cs]; ys=[c[1] for c in cs]
    print(f'room{i} n={len(cs)} x{min(xs)}-{max(xs)} y{min(ys)}-{max(ys)} open={out}:', dict(ids))
print()
PERM={0:'both',1:'goLeft',2:'goRight',3:'neither'}
for b in B:
    if b['id'] in DOOR or b['id'] in ('SuitMarker','SuitLocker','LuxuryBed','HandSanitizer','WashSink','FlushToilet'):
        ac=b['bd'].get('AccessControl'); 
        p=''
        if ac:
            t=json.loads(ac['defaultPermissionByTag']); p=' '.join(f"{e['Key']['Name']}={PERM[e['Value']]}" for e in t)
        print(b['id'],(b['x'],b['y']),'orient',b['o'],'state',b['bd'].get('Door',{}).get('requestedState'),p, b['bd'].get('DirectionControl',''))
