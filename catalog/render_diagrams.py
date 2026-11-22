"""Make a downloadable sheet from the product's own verified screenshots."""
from argparse import ArgumentParser
from functools import lru_cache
from hashlib import sha1
from io import BytesIO
import json
from pathlib import Path
import re

from PIL import Image, ImageDraw, ImageFont, ImageOps

ROOT = Path(__file__).resolve().parents[1]
BG, PAPER, INK, MUTED, LINE = '#f1f4f4', '#ffffff', '#172e35', '#34525b', '#cbd5d6'
GUTTER, WIDTH = 55, 1720


def font_path(explicit, bold):
    if explicit:
        return explicit
    names = (
        ['C:/Windows/Fonts/meiryob.ttc', '/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc', '/System/Library/Fonts/ヒラギノ角ゴシック W6.ttc']
        if bold else
        ['C:/Windows/Fonts/meiryo.ttc', '/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc', '/System/Library/Fonts/ヒラギノ角ゴシック W3.ttc']
    )
    for path in names:
        if Path(path).is_file():
            return path
    raise SystemExit('Supply a Japanese-capable font with --font and --bold-font.')


@lru_cache
def font(path, size):
    return ImageFont.truetype(str(path), size)


def wrap(line, face, width, ja):
    chunks = list(line) if ja else re.findall(r'\S+\s*', line)
    result, current = [], ''
    for chunk in chunks:
        candidate = current + chunk
        if current and face.getlength(candidate.rstrip()) > width:
            result.append(current.rstrip())
            current = chunk
        else:
            current = candidate
    if current:
        result.append(current.rstrip())
    return result


def draw_text(draw, text, xy, face, width, ja, fill=INK):
    x, y = xy
    for line in wrap(text, face, width, ja):
        draw.text((x, y), line, font=face, fill=fill, anchor='lt')
        y += round(face.size * 1.5)
    return y


def screenshot(path, expected):
    data = path.read_bytes()
    if sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() != expected:
        raise ValueError(f'Unreviewed screenshot: {path}')
    with Image.open(BytesIO(data)) as picture:
        return picture.convert('RGB')


def place(canvas, source, bounds):
    x, y, w, h = bounds
    img = ImageOps.contain(source, (w, h), Image.Resampling.LANCZOS)
    canvas.paste(img, (x + (w - img.width) // 2, y + (h - img.height) // 2))


def render(item, lang, body, bold):
    ja = lang == 'ja'
    text = item['locales'][lang]
    manual = (ROOT / text['manual']).parent
    panel = text['panel']
    page = Image.new('RGB', (WIDTH, 2700), PAPER)
    draw = ImageDraw.Draw(page)
    body_font, small, heading = font(body, 32), font(body, 27), font(bold, 40)
    y = draw_text(draw, item['product'] + ' 1.0.0', (GUTTER, 36), font(bold, 29), WIDTH-2*GUTTER, ja, MUTED)
    y = draw_text(draw, text['headline'], (GUTTER, y+5), font(bold, 50), WIDTH-2*GUTTER, ja) + 8
    y = draw_text(draw, '最初に開く画面' if ja else 'Where to start', (GUTTER, y), heading, WIDTH-2*GUTTER, ja)+7
    top = y
    draw.rounded_rectangle((GUTTER, y, 790, y+425), 14, fill=BG, outline=LINE, width=2)
    place(page, screenshot(manual/panel['image'], panel['git_blob']), (GUTTER+12, y+12, 790-GUTTER-24, 401))
    right, rw = 830, WIDTH-830-GUTTER
    y = draw_text(draw, '開き方' if ja else 'Open the panel', (right, top+7), font(bold, 32), rw, ja)
    y = draw_text(draw, panel['where'], (right, y+4), body_font, rw, ja) + 9
    y = draw_text(draw, '画面の目印' if ja else 'What to look for', (right, y), font(bold, 32), rw, ja)
    y = draw_text(draw, panel['look'], (right, y+4), body_font, rw, ja)
    y = max(top+425, y) + 38
    y = draw_text(draw, '操作前後の実例' if ja else 'The worked example', (GUTTER, y), heading, WIDTH-2*GUTTER, ja)+10
    captions = []
    margin = 30
    col = (WIDTH-2*GUTTER-margin)//2
    for index, fig in enumerate(text['figures']):
        x = GUTTER + index*(col+margin)
        image = screenshot(ROOT/fig['path'], fig['git_blob'])
        draw.rounded_rectangle((x, y, x+col, y+455), 12, fill=BG, outline=LINE, width=2)
        place(page, image, (x+10,y+10,col-20,435))
        captions.append(draw_text(draw, fig['caption'], (x, y+475), small, col, ja))
    bottom = max(captions)+GUTTER
    if bottom > page.height:
        raise ValueError(f'Layout exceeds page for {item["product"]}/{lang}')
    dest=ROOT/'docs'/'diagrams'/lang/(item['product']+'.png')
    dest.parent.mkdir(exist_ok=True, parents=True)
    page.crop((0, 0, WIDTH, bottom)).save(dest, optimize=True)


def main():
    parser=ArgumentParser(description=__doc__)
    parser.add_argument('--product')
    parser.add_argument('--font')
    parser.add_argument('--bold-font')
    args=parser.parse_args()
    rows=json.loads((ROOT/'catalog/products.json').read_text(encoding='utf-8'))['products']
    if args.product:
        rows=[p for p in rows if p['product']==args.product]
        if not rows:
            parser.error('Unknown product')
    regular=font_path(args.font, False)
    bold=font_path(args.bold_font, True)
    for row in rows:
        for lang in ('ja','en'):
            render(row, lang, regular, bold)
    print(f'{len(rows)} illustrated workflow sheets in two languages')


if __name__=='__main__':
    main()
