"""Render the illustrated manual introductions or export portable Markdown product pages."""
import argparse
import hashlib
import html
import json
from pathlib import Path
import re
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
START = '<!-- smarttools-catalog:start -->'
END = '<!-- smarttools-catalog:end -->'


def manual_url(path):
    return 'https://jelararagi.github.io/SmartTools/' + quote(path.removeprefix('docs/'))


def workflow_html(text):
    steps = []
    for index, step in enumerate(text['workflow']):
        arrow = '<span aria-hidden="true"> → </span>' if index else ''
        steps.append(f'<li style="display:inline">{arrow}{html.escape(step)}</li>')
    return '<ol style="padding:0;line-height:1.8;font-weight:600">' + ''.join(steps) + '</ol>'


def comparison_html(text, lang):
    item = text.get('comparison')
    if not item:
        return ''
    label = '比較対象の資料' if lang == 'ja' else 'Comparison reference'
    return f'<p>{html.escape(item["note"])} {label} · <a href="{html.escape(item["url"])}">{html.escape(item["name"])}</a></p>'


def card(item, lang):
    esc = html.escape
    text = item['locales'][lang]
    figures = []
    for figure in text['figures']:
        src = Path(figure['path']).relative_to(Path(text['manual']).parent).as_posix()
        caption = esc(figure['caption'])
        zoom = '原寸で見る' if lang == 'ja' else 'View full size'
        figures.append(f'<figure style="margin:0"><a href="{esc(src)}" title="{zoom}"><img loading="lazy" style="width:100%;height:auto" src="{esc(src)}" alt="{caption}"></a><figcaption>{caption}</figcaption></figure>')
    tip = '試す前に' if lang == 'ja' else 'Before you try it'
    help_text = '導入・トラブルのヘルプ' if lang == 'ja' else 'Installation and troubleshooting help'
    return '\n'.join([START, '<section aria-labelledby="smarttools-example-preview">', f'<h2 id="smarttools-example-preview">{esc(text["headline"])}</h2>', f'<p>{esc(text["description"])}</p>', workflow_html(text), '<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,260px),1fr));gap:1rem">', *figures, '</div>', comparison_html(text, lang), f'<p><strong>{tip}</strong>　{esc(text["try_first"])}</p>', f'<p><a href="../../#help">{help_text}</a></p>', '</section>', END])


def update_manual(item, lang, check):
    file = ROOT / item['locales'][lang]['manual']
    original = file.read_bytes()
    doc = original.decode('utf-8')
    new = card(item, lang)
    if START in doc:
        if doc.count(START) != 1 or doc.count(END) != 1:
            raise ValueError(f'Invalid markers in {file}')
        base = re.sub(r'\n?' + re.escape(START) + '.*?' + re.escape(END), '', doc, count=1, flags=re.S)
    else:
        base = doc
    if '</header>' not in base:
        raise ValueError(f'Missing cover in {file}')
    result = base.replace('</header>', '</header>\n' + new, 1)
    if result != doc:
        if check:
            raise ValueError(f'Outdated introduction in {file}')
        file.write_bytes(result.encode('utf-8'))


def export_product(item, lang, dest, release):
    text = item['locales'][lang]
    product_dir = dest / lang / item['product']
    media = product_dir / 'images'
    media.mkdir(parents=True, exist_ok=True)
    lines = [f'# {item["product"]} — {text["headline"]}', '', text['description'], '']
    lines += [' → '.join(text['workflow']), '']
    if text.get('comparison'):
        item = text['comparison']
        lines += [f'{item["note"]} [{item["name"]}]({item["url"]})', '']
    for fig in text['figures']:
        src = ROOT / fig['path']
        data = src.read_bytes()
        digest = hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
        if digest != fig['git_blob']:
            raise ValueError(f'Figure changed; review the caption before export: {src}')
        (media / src.name).write_bytes(data)
        lines += ['![](' + 'images/' + src.name + ')', '', fig['caption'], '']
    tips, guide, free = ('試す前に','図付きの解説書','無料公開の1.0.0') if lang == 'ja' else ('Before you try it','Full illustrated manual','Free 1.0.0 release')
    lines += ['## ' + tips, '', text['try_first'], '', f'[{guide}]({manual_url(text["manual"])}) · [{free}]({release})']
    help_path = 'docs/' if lang == 'ja' else 'docs/en/'
    help_label = 'SmartToolsヘルプ' if lang == 'ja' else 'SmartTools Help'
    lines += ['', f'[{help_label}]({manual_url(help_path)}#help)']
    (product_dir / 'index.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    action = parser.add_mutually_exclusive_group(required=True)
    action.add_argument('--update-manuals', action='store_true')
    action.add_argument('--check', action='store_true')
    action.add_argument('--export', type=Path, metavar='EMPTY_DIRECTORY')
    args = parser.parse_args()
    catalog = json.loads((HERE / 'products.json').read_text(encoding='utf-8'))
    if args.export and args.export.exists() and any(args.export.iterdir()):
        parser.error('Choose a new or empty output directory.')
    for item in catalog['products']:
        for lang in ('ja', 'en'):
            if args.export:
                export_product(item, lang, args.export, catalog['free_release'])
            else:
                update_manual(item, lang, args.check)
    print(f'{len(catalog["products"])} products, 2 languages')


if __name__ == '__main__':
    main()
