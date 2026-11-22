"""Build the bilingual illustrated guides and export their shop-ready Markdown."""
import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re
from urllib.parse import quote

from field_guide import anchor_examples, parse_manual

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
START = '<!-- smarttools-catalog:start -->'
END = '<!-- smarttools-catalog:end -->'
STYLE = """.sg-intro{margin:1.3rem 0 2rem}
.sg-intro h2,.sg-intro h3{scroll-margin-top:4rem}
.sg-start{display:grid;grid-template-columns:minmax(0,1.22fr) minmax(0,1fr);gap:clamp(1rem,3vw,2rem);align-items:start}
.sg-intro figure{margin:0;min-width:0}
.sg-start figure{padding:0;overflow:hidden}
.sg-photo{display:block;text-align:center;background:#26282a}
.sg-start .sg-photo{max-height:clamp(240px,51vh,490px);overflow:auto;scrollbar-gutter:stable}
.sg-intro .sg-photo img{display:block;width:100%;height:auto;max-height:none;margin:auto;object-fit:contain}
.sg-start .sg-photo img{width:auto;max-width:100%}
.sg-start figcaption{padding:.4rem .65rem}
.sg-intro p{margin:.4rem 0 .85rem}
.sg-start .sg-copy h3{margin:0 0 .3rem;font-size:1.1rem}
.sg-intro .sg-pair{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:1rem;align-items:start}
.sg-intro .sg-pair figure{background:var(--card);padding:.45rem}
.sg-intro .sg-pair a{display:block}
.sg-intro .sg-pair img{display:block;width:100%;height:auto}
.sg-intro figcaption{line-height:1.55}
.sg-intro .sg-links{display:flex;flex-wrap:wrap;gap:.25rem 1.1rem;margin:.6rem 0 1rem}
.sg-intro .sg-steps{padding-inline-start:1.5rem;margin:.4rem 0 .8rem}
.sg-intro summary,.sg-product-overview summary{cursor:pointer}
.sg-intro details{margin:.8rem 0}
.sg-intro [id]{scroll-margin-top:4rem}
@media(max-width:700px){.sg-start,.sg-intro .sg-pair{grid-template-columns:1fr}.sg-start .sg-photo{max-height:48vh}}
@media print{.sg-start .sg-photo{overflow:visible;max-height:none}.sg-start .sg-photo img{max-height:10cm;object-fit:contain}}"""
LABELS = {
    'ja': ('最初に開く画面', '開き方', '画面の目印', 'この作例の手順を見る', '試す前に',
           '別の作例を試す', '機能別の解説', 'すべての実例', '関連ツールの公式資料', '作例を画像で保存',
           '解説書', '導入・トラブルのヘルプ', '無料公開版 1.0.0', 'この製品について', '原寸で見る'),
    'en': ('Where to start', 'Open the panel', 'What to look for', 'Follow the worked example', 'Before you try it',
           'Try another example', 'Feature reference', 'All worked examples', 'Official documentation for related tools', 'Download the illustrated example',
           'Full manual', 'Setup and troubleshooting help', 'Free 1.0.0 release', 'About this tool', 'View full size'),
}


def url(path):
    return 'https://jelararagi.github.io/SmartTools/' + quote(path.removeprefix('docs/'))


def diagram_path(product, lang):
    return ROOT / 'docs' / 'diagrams' / lang / (product + '.png')


def original_manual(doc):
    if START not in doc:
        return doc
    if doc.count(START) != 1 or doc.count(END) != 1:
        raise ValueError('Invalid guide markers')
    return re.sub(r'\r?\n?' + re.escape(START) + '.*?' + re.escape(END), '', doc, count=1, flags=re.S)


def photos_for_example(item, lang):
    text = item['locales'][lang]
    parent = Path(text['manual']).parent
    return [(Path(fig['path']).relative_to(parent).as_posix(), fig['caption'], fig['git_blob']) for fig in text['figures']]


def photo(src, caption):
    src = escape(src, quote=True)
    cap = escape(caption, quote=True)
    return f'<figure><a href="{src}"><img loading="lazy" src="{src}" alt="{cap}"></a><figcaption>{cap}</figcaption></figure>'


def pair(photos):
    return '<div class="sg-pair">' + ''.join(photo(src, caption) for src, caption in photos) + '</div>'


def index_details(label, rows):
    return (f'<details><summary>{escape(label)} ({len(rows)})</summary><ul>' +
            ''.join(f'<li><a href="#{escape(anchor)}">{escape(title)}</a></li>' for anchor, title in rows) + '</ul></details>')


def related_sources(item, label):
    links = ''.join(f'<li><a href="{escape(ref["url"], quote=True)}">{escape(ref["name"])}</a></li>' for ref in item['sources'])
    return f'<details><summary>{escape(label)}</summary><ul>{links}</ul></details>'


def intro(item, lang, cases, features):
    text = item['locales'][lang]
    p = text['panel']
    start, opening, look, follow, tip, more, feature, all_cases, refs, save, _, help_label, _, _, zoom = LABELS[lang]
    src = escape(p['image'], quote=True)
    cap = escape(p['caption'], quote=True)
    lead_figures = photos_for_example(item, lang)
    primary = escape(item['example'])
    png = ('../../diagrams/ja/' if lang == 'ja' else '../../../diagrams/en/') + item['product'] + '.png'
    html = [
        START, f'<style>{STYLE}</style>', '<section class="sg-intro">',
        f'<h2 id="compare-tools">{start}</h2>', '<div class="sg-start">',
        f'<figure><a class="sg-photo" href="{src}"><img fetchpriority="high" src="{src}" alt="{cap}"></a><figcaption><a href="{src}">{zoom}</a></figcaption></figure>',
        f'<div class="sg-copy"><h3>{opening}</h3><p>{escape(p["where"])}</p><h3>{look}</h3><p>{escape(p["look"])}</p></div></div>',
        f'<h2 id="smarttools-example-preview">{escape(text["headline"])}</h2><p>{escape(text["description"])}</p>',
        '<ol class="sg-steps">' + ''.join(f'<li>{escape(step)}</li>' for step in text['workflow']) + '</ol>',
        pair([(s, c) for s, c, _ in lead_figures]),
        f'<p><strong>{tip}</strong>　{escape(text["try_first"])}</p>',
        f'<p class="sg-links"><a href="#case-{primary}">{follow}</a><a href="{escape(png)}" download>{save} (PNG)</a><a href="../../#help">{help_label}</a></p>',
        f'<h2 id="more-workflows">{more}</h2>',
    ]
    for key in item['cases']:
        title, desc, figures = cases[key]
        if len(figures) < 2:
            raise ValueError(f'Expected an illustrated pair for {key}')
        html += [f'<article><h3>{escape(title)}</h3><p>{escape(desc)}</p>', pair([figures[0], figures[-1]]),
                 f'<p><a href="#case-{escape(key)}">{follow} · {escape(title)}</a></p></article>']
    html += [index_details(feature, features), index_details(all_cases, [('case-' + k, v[0]) for k, v in cases.items()]),
             related_sources(item, refs), '</section>', END]
    return '\n'.join(html)


def update(item, lang, check):
    file = ROOT / item['locales'][lang]['manual']
    original = file.read_bytes().decode('utf-8')
    base = original_manual(original)
    cases, features = parse_manual(base)
    base = anchor_examples(base, cases)
    header = re.search(r'<header class="cover">.*?</header>', base, re.S)
    if not header:
        raise ValueError(f'Missing product cover: {file}')
    cover = header[0]
    if 'sg-product-overview' not in cover:
        details = f'<details class="sg-product-overview"><summary>{LABELS[lang][13]}</summary>'
        cover, count = re.subn(r'(<p class="lead">.*?</p>)', lambda match: details + match[1] + '</details>', cover, count=1, flags=re.S)
        if count != 1:
            raise ValueError(f'Missing product description: {file}')
    result = base[:header.start()] + cover + '\n' + intro(item, lang, cases, features) + base[header.end():]
    if result != original:
        if check:
            raise ValueError(f'Outdated introduction: {file}')
        file.write_bytes(result.encode('utf-8'))


def verified_copy(src, dest, expected):
    data = src.read_bytes()
    actual = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
    if actual != expected:
        raise ValueError(f'Image changed since the caption was verified: {src}')
    dest.write_bytes(data)


def md_image(lines, path, caption):
    alt = caption.replace('[', '\\[').replace(']', '\\]')
    lines.extend([f'![{alt}]({path})', ''])


def export_product(item, lang, dest, release):
    text = item['locales'][lang]
    panel = text['panel']
    target = dest / lang / item['product']
    media = target / 'images'
    media.mkdir(parents=True, exist_ok=True)
    manual = ROOT / text['manual']
    manual_url = url(text['manual'])
    cases, _ = parse_manual(original_manual(manual.read_text(encoding='utf-8')))
    start, opening, look, follow, tip, more, _, _, refs, save, full, help_label, free, _, _ = LABELS[lang]
    lines = [f'# {item["product"]} — {text["headline"]}', '', '## ' + start, '']
    verified_copy(manual.parent / panel['image'], target / panel['image'], panel['git_blob'])
    md_image(lines, panel['image'], panel['caption'])
    lines += [f'**{opening}**　{panel["where"]}', '', f'**{look}**　{panel["look"]}', '', '## ' + text['headline'], '', text['description'], '']
    lines.extend(f'{i}. {step}' for i, step in enumerate(text['workflow'], 1))
    lines.append('')
    for src, caption, digest in photos_for_example(item, lang):
        verified_copy(manual.parent / src, target / src, digest)
        md_image(lines, src, caption)
    printable = diagram_path(item['product'], lang)
    (media / printable.name).write_bytes(printable.read_bytes())
    lines += [f'**{tip}**　{text["try_first"]}', '', f'[{follow}]({manual_url}#case-{item["example"]}) · [{save} (PNG)](images/{printable.name})', '',
              '## ' + more, '']
    for key in item['cases']:
        title, desc, figures = cases[key]
        lines += ['### ' + title, '', desc, '']
        for src, caption in [figures[0], figures[-1]]:
            verified_copy(manual.parent / src, target / src, text['case_images'][src])
            md_image(lines, src, caption)
        lines += [f'[{follow}]({manual_url}#case-{key})', '']
    lines += ['## ' + refs, '']
    lines.extend(f'- [{ref["name"]}]({ref["url"]})' for ref in item['sources'])
    help_url = url('docs/' if lang == 'ja' else 'docs/en/')
    lines += ['', f'[{full}]({manual_url}) · [{help_label}]({help_url}#help) · [{free}]({release})']
    (target / 'index.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    actions = parser.add_mutually_exclusive_group(required=True)
    actions.add_argument('--update-manuals', action='store_true')
    actions.add_argument('--check', action='store_true')
    actions.add_argument('--export', type=Path, metavar='EMPTY_DIRECTORY')
    args = parser.parse_args()
    catalog = json.loads((HERE / 'products.json').read_text(encoding='utf-8'))
    if args.export and args.export.exists() and any(args.export.iterdir()):
        parser.error('Choose a new or empty output directory.')
    for item in catalog['products']:
        for lang in ('ja', 'en'):
            if args.export:
                export_product(item, lang, args.export, catalog['free_release'])
            else:
                update(item, lang, args.check)
    print(f'{len(catalog["products"])} products in Japanese and English')


if __name__ == '__main__':
    main()
