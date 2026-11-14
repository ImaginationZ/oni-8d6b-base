import json, subprocess, sys
bv, kind, out = sys.argv[1], sys.argv[2], sys.argv[3]
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36'
cookie = open('cookie.txt').read().strip()
view = json.load(open(f'view_{bv}.json'))['data']
r = subprocess.run(['curl', '-s', '-A', UA, '-e', f'https://www.bilibili.com/video/{bv}', '-H', f'Cookie: {cookie}',
    f"https://api.bilibili.com/x/player/playurl?bvid={bv}&cid={view['cid']}&qn=80&fnval=16"], capture_output=True, text=True)
d = json.loads(r.stdout)['data']['dash']
if kind == 'v':
    s = [x for x in d['video'] if x['id'] == 32 and x['codecs'].startswith('avc')][0]
else:
    s = sorted(d['audio'], key=lambda a: a['bandwidth'])[-1]
urls = [s['baseUrl']] + (s.get('backupUrl') or s.get('backup_url') or [])
for u in urls:
    subprocess.run(['curl', '-s', '-L', '--retry', '5', '-C', '-', '-A', UA, '-e', 'https://www.bilibili.com/', '-o', out, u])
    head = open(out, 'rb').read(16)
    if b'html' not in head.lower():
        print('ok', out, u.split('/')[2]); break
    print('fail', u.split('/')[2])
