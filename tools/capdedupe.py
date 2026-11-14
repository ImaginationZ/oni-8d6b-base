import sys, glob, os
from PIL import Image, ImageChops, ImageDraw, ImageStat
d = sys.argv[1]; out = sys.argv[2]
files = sorted(glob.glob(f'{d}/*.jpg'))
def textmask(im):
    # subtitles are bright white text with dark outline: keep near-white pixels only
    g = im.convert('L').point(lambda v: 255 if v > 225 else 0)
    return g
kept = []; last = None
for i, f in enumerate(files):
    im = Image.open(f); m = textmask(im)
    ink = ImageStat.Stat(m).mean[0]
    if ink < 1.0:   # no caption
        last = None; continue
    if last is not None:
        diff = ImageStat.Stat(ImageChops.difference(m, last)).mean[0]
        if diff < 6: continue
    kept.append((i, im)); last = m
print(len(kept), 'distinct captions')
# stack into pages of 30 rows, with timestamp
W = kept[0][1].width + 70; rowh = kept[0][1].height
page = 0
for s in range(0, len(kept), 30):
    chunk = kept[s:s+30]
    canvas = Image.new('RGB', (W, rowh * len(chunk)), 'black')
    dr = ImageDraw.Draw(canvas)
    for r, (i, im) in enumerate(chunk):
        canvas.paste(im, (70, r * rowh))
        dr.text((4, r * rowh + rowh // 3), f'{i//60}:{i%60:02d}', fill='yellow')
    canvas.save(f'{out}_{page:02d}.png'); page += 1
print(page, 'pages')
