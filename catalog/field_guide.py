"""Read the existing manual's feature list and illustrated examples."""
from html import unescape
import re


OPEN = re.compile(r'<div class="example"(?: id="case-[\w-]+")?>')
PHOTO = re.compile(r'<img src="(images/ex_([\w-]+)_(\d+)\.(?:jpg|png))" alt="([^"]*)"')
FEATURE = re.compile(r'<section class="feat" id="([^"]+)"><h4>(.*?)</h4>', re.S)


def plain(value):
    return unescape(re.sub(r'<[^>]+>', '', value)).strip()


def parse_manual(doc):
    cases = {}
    for part in OPEN.split(doc)[1:]:
        body = part.split('<div class="exdo">', 1)[0].split('</section>', 1)[0]
        photos = PHOTO.findall(body)
        if not photos:
            continue
        key = photos[0][1]
        photos = [(src, unescape(alt)) for src, k, _, alt in photos if k == key]
        title = re.match(r'<p class="exhead"><span class="extag">[^<]*</span>(.*?)(?:<span class="exscene">|</p>)', body, re.S)
        intro = re.search(r'<p class="exintro">(.*?)</p>', body, re.S)
        if not title or not intro:
            raise ValueError(f'Missing title or introduction for {key}')
        cases[key] = (plain(title[1]), plain(intro[1]), photos)
    if not cases:
        raise ValueError('No worked examples in source manual')
    return cases, [(anchor, plain(title)) for anchor, title in FEATURE.findall(doc)]


def anchor_examples(doc, keys):
    offsets = {}
    for marker in OPEN.finditer(doc):
        photo = PHOTO.search(doc, marker.end(), marker.end() + 4000)
        if photo and photo[2] in keys:
            offsets[photo[2]] = (marker.start(), marker.end())
    if set(offsets) != set(keys):
        raise ValueError('Example index could not locate every example')
    for key, (start, end) in sorted(offsets.items(), key=lambda pair: pair[1], reverse=True):
        doc = doc[:start] + f'<div class="example" id="case-{key}">' + doc[end:]
    return doc

def first_recipe(doc):
    """Read the first worked procedure in chapter six, using that edition's button labels."""
    chapter = re.search(r'<h2\b[^>]*>\s*6[.．].*?</h2>(.*?)(?:<h2\b|$)', doc, re.S)
    if not chapter:
        raise ValueError('Missing common tasks chapter')
    for block in re.findall(r'<section\b[^>]*class=["\']feat["\'][^>]*>(.*?)</section>', chapter[1], re.S):
        steps = re.search(r'<ol\b[^>]*class=["\']steps["\'][^>]*>(.*?)</ol>', block, re.S)
        if steps:
            title = re.search(r'<h4>(.*?)</h4>', block, re.S)
            sequence = [plain(step) for step in re.findall(r'<li>(.*?)</li>', steps[1], re.S)]
            if not title or not sequence:
                raise ValueError('Incomplete first recipe')
            return plain(title[1]), sequence
    raise ValueError('No procedure found in common tasks')
