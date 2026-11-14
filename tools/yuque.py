import re, json, sys, urllib.parse, html, subprocess, os
url, out = sys.argv[1], sys.argv[2]
UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36'
os.makedirs(out, exist_ok=True)
page = subprocess.run(['curl', '-sL', '-m', '30', '-A', UA, url], capture_output=True, text=True).stdout
m = re.search(r'window\.appData = JSON\.parse\(decodeURIComponent\("(.*?)"\)\);', page, re.S)
app = json.loads(urllib.parse.unquote(m.group(1)))
book = app['book']; doc = app['doc']; slug = url.rstrip('/').split('/')[-1]
print('BOOK:', book.get('name'), '|', book.get('description')); print('DOC:', doc.get('title'), '| words', doc.get('word_count'), '| updated', doc.get('content_updated_at'))
api = f"https://www.yuque.com/api/docs/{slug}?book_id={book['id']}&merge_dynamic_data=false"
d = json.loads(subprocess.run(['curl', '-s', '-m', '30', '-A', UA, '-H', f'Referer: {url}', api], capture_output=True, text=True).stdout)['data']
c = d.get('content') or ''
open(f'{out}/content.html', 'w').write(c)
ev = [(m.start(), 'h', re.sub('<[^>]+>', '', m.group(1))) for m in re.finditer(r'<h\d[^>]*>(.*?)</h\d>', c, re.S)]
ev += [(m.start(), 'i', m.group(1)) for m in re.finditer(r'<card[^>]*name="image"[^>]*value="([^"]*)"', c)]
ev += [(m.start(), 't', m.group(1)) for m in re.finditer(r'<p[^>]*>(.*?)</p>', c, re.S)]
ev += [(m.start(), 't', m.group(1)) for m in re.finditer(r'<li[^>]*>(.*?)</li>', c, re.S)]
ev.sort(); n = 0
for _, k, v in ev:
    if k == 'h': print('\n##', v.strip())
    elif k == 'i':
        v = html.unescape(v); v = urllib.parse.unquote(v[5:]) if v.startswith('data:') else v
        j = json.loads(v); n += 1; fn = f'{out}/{n:02d}.jpg'
        subprocess.run(['curl', '-s', '-m', '30', '-A', UA, '-H', 'Referer: https://www.yuque.com/', '-o', fn, j['src'].split('?')[0]])
        print(f'  [img {n:02d}] {j.get("originWidth")}x{j.get("originHeight")} {j.get("name","")}')
    else:
        t = html.unescape(re.sub('<card[^>]*>', '', re.sub(r'<(?!card)[^>]+>', '', v))).strip().replace('​', '')
        if t: print('  ', t)
