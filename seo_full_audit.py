import os
import re
import json
from html import unescape
from urllib.parse import urlparse, urljoin

root = os.getcwd()

placeholder_patterns = [
    '{{PHONE}}', '{{TELEGRAM}}', '{{WHATSAPP}}', '{{PRICE_DOOR}}', '{{PRICE_CAR}}',
    '{{PRICE_SAFE}}', '{{PRICE_GARAGE}}', '{{PRICE_REPAIR}}', '{{PRICE_CYLINDER}}', '{{PRICE_FALSE_CALL}}'
]

# site domain for absolute link resolution
DOMAIN = 'https://openme.com.ua'

# get all html file paths
html_paths = []
for dirpath, dirnames, filenames in os.walk(root):
    if dirpath.startswith(os.path.join(root, '.git')):
        continue
    for name in filenames:
        if name.lower().endswith('.html'):
            html_paths.append(os.path.relpath(os.path.join(dirpath, name), root).replace('\\','/'))
html_paths = sorted(html_paths)

# mapping from file path to URL path
url_by_path = {}
for path in html_paths:
    if path == 'index.html':
        url = '/'
    else:
        if path.endswith('/index.html'):
            url = '/' + path[:-len('index.html')]
        else:
            url = '/' + path
    url = url.replace('//','/')
    if url != '/' and url.endswith('/'):
        pass
    url_by_path[path] = url

# valid internal urls set
valid_urls = set(url_by_path.values())
# also accept with no trailing slash if path is root? We will normalize on lookup

def normalize_url(url):
    if url.startswith(DOMAIN):
        parsed = urlparse(url)
        return parsed.path if parsed.path else '/'
    if url.startswith('http://') or url.startswith('https://'):
        return urlparse(url).path or '/'
    if url.startswith('/'):
        return url
    return None


def get_text(html):
    # remove scripts/styles + tags
    clean = re.sub(r'(?is)<script.*?</script>', ' ', html)
    clean = re.sub(r'(?is)<style.*?</style>', ' ', clean)
    clean = re.sub(r'(?is)<!--.*?-->', ' ', clean)
    clean = re.sub(r'<[^>]+>', ' ', clean)
    return unescape(clean)


def extract_tags(html):
    return html


def parse_json_ld(html):
    items = []
    for match in re.finditer(r'<script[^>]+type=["\']application/ld\+json["\'][^>]*>(.*?)</script>', html, re.I | re.S):
        text = match.group(1).strip()
        if not text:
            continue
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            # try to fix common trailing commas
            fixed = re.sub(r',\s*([}\]])', r'\1', text)
            try:
                data = json.loads(fixed)
            except json.JSONDecodeError:
                items.append({'invalid': True, 'raw': text})
                continue
        if isinstance(data, list):
            items.extend(data)
        else:
            items.append(data)
    return items


def extract_meta(html, name):
    m = re.search(r'<meta[^>]+name=["\']{}["\'][^>]+content=["\']([^"\']+)["\']'.format(re.escape(name)), html, re.I)
    if m:
        return m.group(1).strip()
    return None


def extract_link_rel(html, rel):
    entries = []
    for match in re.finditer(r'<link[^>]+rel=["\']{}["\'][^>]*>'.format(re.escape(rel)), html, re.I):
        tag = match.group(0)
        href = re.search(r'href=["\']([^"\']+)["\']', tag, re.I)
        if href:
            entries.append(href.group(1).strip())
    return entries


def extract_meta_property(html, prop):
    m = re.search(r'<meta[^>]+property=["\']{}["\'][^>]+content=["\']([^"\']+)["\']'.format(re.escape(prop)), html, re.I)
    if m:
        return m.group(1).strip()
    return None


def extract_h1(html):
    return re.findall(r'<h1[^>]*>(.*?)</h1>', html, re.I | re.S)


def extract_title(html):
    m = re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
    return m.group(1).strip() if m else None


def extract_anchors(html):
    anchors = []
    for match in re.finditer(r'<a[^>]+href=["\']([^"\']+)["\']', html, re.I):
        anchors.append(match.group(1).strip())
    return anchors


def count_words(text):
    words = re.findall(r'[\w\u0400-\u04FF]+', text)
    return len(words)


def contains_russian(text):
    keywords = ['наш мастер','наш мастер', 'Позвонить', 'Мы ', 'мы ', 'майстер приедет', 'выезжает', 'работы', 'сейф', 'высота', 'Вопросы', 'Вопрос']
    text_low = text.lower()
    return any(k.lower() in text_low for k in keywords)


def contains_ukrainian(text):
    keywords = ['майстер', 'виїзд', 'район', 'відкриття', 'запитання', 'ціна', 'телефон', 'послуга', 'двері', 'гаражів']
    text_low = text.lower()
    return any(k.lower() in text_low for k in keywords)


audit = {
    'summary': {},
    'pages': {},
    'sitemap': {},
    'issues': []
}

for path in html_paths:
    html = open(os.path.join(root, path), encoding='utf-8').read()
    page = {
        'path': path,
        'url': url_by_path[path],
        'title': extract_title(html),
        'meta_description': extract_meta(html, 'description'),
        'canonical': extract_link_rel(html, 'canonical')[0] if extract_link_rel(html, 'canonical') else None,
        'hreflang': [],
        'og': {},
        'h1': extract_h1(html),
        'jsonld': parse_json_ld(html),
        'word_count': count_words(get_text(html)),
        'placeholders': [p for p in placeholder_patterns if p in html],
        'html_count': {tag: len(re.findall(fr'<{tag}\b[^>]*>', html, re.I)) + len(re.findall(fr'</{tag}>', html, re.I)) for tag in ['html','head','body']},
        'anchor_hrefs': extract_anchors(html),
        'raw': html,
        'faq_details': len(re.findall(r'<details[^>]*>', html, re.I)),
    }
    # hreflang links
    for tag in re.findall(r'<link\b[^>]*>', html, re.I):
        if re.search(r'rel=["\']alternate["\']', tag, re.I):
            lang = re.search(r'hreflang=["\']([^"\']+)["\']', tag, re.I)
            href = re.search(r'href=["\']([^"\']+)["\']', tag, re.I)
            if lang and href:
                page['hreflang'].append({'lang': lang.group(1).lower(), 'href': href.group(1).strip()})

    # OG properties
    for prop in ['og:title','og:description','og:url','og:type']:
        page['og'][prop] = extract_meta_property(html, prop)

    audit['pages'][path] = page

# count pages
all_html = html_paths
total_html_pages = len(all_html)
non_404_pages = [p for p in all_html if p != '404.html']
ua_pages = [p for p in non_404_pages if not p.startswith('ru/')]
ru_pages = [p for p in non_404_pages if p.startswith('ru/')]
ua_raion_pages = [p for p in ua_pages if p.startswith('raiony/') and p != 'raiony/index.html']
ru_raion_pages = [p for p in ru_pages if p.startswith('ru/raiony/') and p != 'ru/raiony/index.html']

# sitemap parse
sitemap_xml = open(os.path.join(root, 'sitemap.xml'), encoding='utf-8').read()
locs = re.findall(r'<loc>([^<]+)</loc>', sitemap_xml)
sitemap_pages = [normalize_url(x) for x in locs if x.strip()]

# check 404 not in sitemap
sitemap_404 = any(normalize_url(x) == '/404.html' for x in locs)

# analyze pages
issues = []
page_stats = {}
for path, page in audit['pages'].items():
    if path == '404.html':
        continue
    stats = {'issues': []}
    if not page['title']:
        stats['issues'].append('missing_title')
    if not page['meta_description']:
        stats['issues'].append('missing_meta_description')
    if len(page['h1']) != 1:
        if len(page['h1']) == 0:
            stats['issues'].append('missing_h1')
        else:
            stats['issues'].append('duplicate_h1')
    if not page['canonical']:
        stats['issues'].append('missing_canonical')
    else:
        expected = urljoin(DOMAIN, page['url'].lstrip('/'))
        if page['url'] == '/':
            expected = DOMAIN + '/'
        if page['canonical'].rstrip('/') + '/' != expected.rstrip('/') + '/':
            stats['issues'].append('canonical_mismatch')
    if not page['og'].get('og:title') or not page['og'].get('og:description') or not page['og'].get('og:url') or not page['og'].get('og:type'):
        stats['issues'].append('missing_og')
    if page['url'] != '/' and page['url'] not in sitemap_pages and page['path'] != '404.html':
        stats['issues'].append('missing_from_sitemap')
    if any('index.html' in href for href in [alt['href'] for alt in page['hreflang']]):
        stats['issues'].append('hreflang_index_html')
    if page['canonical'] and 'index.html' in page['canonical']:
        stats['issues'].append('canonical_index_html')
    # JSON-LD checks
    jsonld = page['jsonld']
    faq_objs = [obj for obj in jsonld if isinstance(obj, dict) and obj.get('@type') == 'FAQPage']
    breadcrumb_objs = [obj for obj in jsonld if isinstance(obj, dict) and obj.get('@type') == 'BreadcrumbList']
    service_objs = [obj for obj in jsonld if isinstance(obj, dict) and obj.get('@type') == 'Service']
    if not faq_objs:
        stats['issues'].append('missing_faq_jsonld')
    else:
        faq = faq_objs[0]
        main = faq.get('mainEntity')
        if not isinstance(main, list) or len(main) < 5:
            stats['issues'].append('missing_faq')
    if not breadcrumb_objs:
        stats['issues'].append('missing_breadcrumb_jsonld')
    if not service_objs:
        stats['issues'].append('missing_service_jsonld')
    # internal links check
    internal_hrefs = []
    for href in page['anchor_hrefs']:
        norm = normalize_url(href)
        if norm is None:
            if href.startswith(DOMAIN):
                norm = normalize_url(href)
        if norm and (href.startswith('/') or href.startswith(DOMAIN) or href.startswith('http://') or href.startswith('https://')):
            if urlparse(href).netloc in ['', urlparse(DOMAIN).netloc] or href.startswith('/'):
                internal_hrefs.append(norm)
    for href in internal_hrefs:
        if href == '/404.html':
            stats['issues'].append('link_to_404')
        if href not in valid_urls and href != '/':
            stats['issues'].append('broken_internal_link:' + href)
    # placeholders
    if page['placeholders']:
        stats['issues'].append('placeholders:' + ','.join(page['placeholders']))
    # duplicates of html/head/body
    for tag in ['html','head','body']:
        if page['html_count'][tag] > 2:
            stats['issues'].append(f'duplicate_{tag}')
    # language insertion
    page_text = get_text(page['raw'])
    if path.startswith('ru/'):
        if any(k in page_text for k in ['майстер', 'виїзд', 'відкриття', 'ціна', 'послуга', 'двері', 'серцевина', 'заміна', 'виїжджає', 'виїжджаємо']):
            stats['issues'].append('ua_in_ru')
    elif path != '404.html':
        if any(k in page_text for k in ['Позвонить', 'Наш мастер', 'Звоните', 'мастер выезжает', 'мы выезжаем', 'ваш мастер']):
            stats['issues'].append('ru_in_ua')
    # special text count requirements
    if path in ['vidkryttia-zamka-bez-poshkodzhen/index.html', 'zamina-sertsevyny-zamka/index.html', 'ru/vskrytie-zamka-bez-povrezhdeniy/index.html', 'ru/zamena-lichinki-zamka/index.html']:
        if page['word_count'] < 700:
            stats['issues'].append('seo_text_too_short')
    if (path.startswith('raiony/') and path != 'raiony/index.html') or (path.startswith('ru/raiony/') and path != 'ru/raiony/index.html'):
        if page['word_count'] < 400 or page['word_count'] > 700:
            stats['issues'].append('raion_text_wordcount_bad')
    page_stats[path] = stats
    if stats['issues']:
        issues.append((path, stats['issues']))

# hreflang validation by page
for path, page in audit['pages'].items():
    if path == '404.html':
        continue
    if not page['hreflang']:
        page_stats[path]['issues'].append('missing_hreflang')
        issues.append((path, ['missing_hreflang']))
    else:
        valid_count = 0
        for alt in page['hreflang']:
            norm = normalize_url(alt['href'])
            if norm and (norm in valid_urls or norm == '/'): 
                valid_count += 1
            else:
                page_stats[path]['issues'].append('hreflang_invalid:' + alt['href'])
                issues.append((path, ['hreflang_invalid:' + alt['href']]))
        if valid_count == 0:
            page_stats[path]['issues'].append('hreflang_no_valid')
            issues.append((path, ['hreflang_no_valid']))

# count missing assets
missing_assets = []
for asset in ['favicon.ico','apple-touch-icon.png','manifest.json']:
    if not os.path.exists(os.path.join(root, asset)):
        missing_assets.append(asset)

summary = {
    'total_html_pages': total_html_pages,
    'sitemap_pages': len(sitemap_pages),
    'ua_pages': len(ua_pages),
    'ru_pages': len(ru_pages),
    'ua_raion_pages': len(ua_raion_pages),
    'ru_raion_pages': len(ru_raion_pages),
    'missing_meta': sum(1 for p in page_stats.values() if 'missing_meta_description' in p['issues']),
    'missing_hreflang': sum(1 for p in page_stats.values() if any(i.startswith('missing_hreflang') for i in p['issues'])),
    'missing_internal_links': sum(1 for p in page_stats.values() if any(i.startswith('broken_internal_link') or i == 'link_to_404' for i in p['issues'])),
    'missing_faq': sum(1 for p in page_stats.values() if any(i in ['missing_faq_jsonld','missing_faq'] for i in p['issues'])),
    'missing_breadcrumb': sum(1 for p in page_stats.values() if any(i == 'missing_breadcrumb_jsonld' for i in p['issues'])),
    'bad_h1': sum(1 for p in page_stats.values() if any(i in ['missing_h1','duplicate_h1'] for i in p['issues'])),
    'invalid_jsonld': sum(1 for p in page_stats.values() if any(i in ['missing_faq_jsonld','missing_breadcrumb_jsonld','missing_service_jsonld'] for i in p['issues'])),
    'duplicate_title': 0,
    'duplicate_meta': 0,
    'broken_internal_links': sum(1 for p in page_stats.values() if any(i.startswith('broken_internal_link') for i in p['issues'])),
    'unreplaced_placeholders': sum(len([i for i in p['issues'] if i.startswith('placeholders:')]) for p in page_stats.values()),
    'missing_assets': missing_assets,
    'sitemap_404': sitemap_404,
}

# duplicate title/meta detection
titles = {}
metas = {}
for p, info in audit['pages'].items():
    if info['title']:
        titles.setdefault(info['title'], []).append(p)
    if info['meta_description']:
        metas.setdefault(info['meta_description'], []).append(p)
summary['duplicate_title'] = sum(1 for v in titles.values() if len(v) > 1)
summary['duplicate_meta'] = sum(1 for v in metas.values() if len(v) > 1)

# new pages existence
expected_new = [
    '/vidkryttia-zamka-bez-poshkodzhen/',
    '/zamina-sertsevyny-zamka/',
    '/ru/vskrytie-zamka-bez-povrezhdeniy/',
    '/ru/zamena-lichinki-zamka/',
]
new_exists = {url: url in valid_urls for url in expected_new}
summary['new_pages'] = new_exists

with open('seo_audit_output.json', 'w', encoding='utf-8') as f:
    json.dump({'summary': summary, 'page_stats': page_stats, 'issues': issues, 'sitemap_pages': sitemap_pages}, f, indent=2, ensure_ascii=False)

print(json.dumps(summary, indent=2, ensure_ascii=False))
print('\nissues count', len(issues))
for path, issue_list in issues[:80]:
    print(path, issue_list)
