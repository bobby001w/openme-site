import re
from pathlib import Path

DOMAIN = 'https://openme.com.ua'

SERVICE_JSONLD_TEMPLATE = """<script type="application/ld+json">
{{"@context":"https://schema.org","@type":"Service","name":"{name}","description":"{description}","provider":{{"@type":"LocalBusiness","name":"OpenMe","telephone":"+380501234567"}},"url":"{url}","serviceType":"Emergency locksmith service"}}
</script>
"""

OG_TEMPLATE = """  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:url" content="{url}">
  <meta property="og:type" content="service">
"""


def normalize_url(path: Path, canonical: str | None) -> str:
    if canonical:
        if canonical.startswith('http'):
            return canonical
        if canonical.startswith('/'):
            return DOMAIN.rstrip('/') + canonical
    if path.name == 'index.html':
        if path.parent == Path('.'):
            return DOMAIN.rstrip('/') + '/'
        return DOMAIN.rstrip('/') + '/' + str(path.parent).replace('\\', '/') + '/'
    return DOMAIN.rstrip('/') + '/' + str(path).replace('\\', '/')


def inject_og_and_service(html: str, title: str, description: str, canonical_url: str) -> str:
    og_needed = not all(re.search(r'<meta[^>]+property=["\']{}["\'][^>]*>'.format(prop), html, re.I)
                        for prop in ['og:title', 'og:description', 'og:url', 'og:type'])
    service_needed = not re.search(r'"@type"\s*:\s*"Service"', html, re.I)
    if not og_needed and not service_needed:
        return html

    insert_at = None
    m = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]*>', html, re.I)
    if m:
        insert_at = m.end()
    else:
        m = re.search(r'<meta[^>]+name=["\']description["\'][^>]*>', html, re.I)
        if m:
            insert_at = m.end()
        else:
            m = re.search(r'<title[^>]*>.*?</title>', html, re.I | re.S)
            if m:
                insert_at = m.end()
    if insert_at is None:
        m = re.search(r'</head>', html, re.I)
        insert_at = m.start() if m else len(html)

    inserts = ''
    if og_needed:
        inserts += OG_TEMPLATE.format(
            title=title.replace('"', '&quot;'),
            description=description.replace('"', '&quot;'),
            url=canonical_url
        )
    if service_needed:
        inserts += SERVICE_JSONLD_TEMPLATE.format(
            name=title.replace('"', '&quot;'),
            description=description.replace('"', '&quot;'),
            url=canonical_url
        )
    return html[:insert_at] + inserts + html[insert_at:]


if __name__ == '__main__':
    updated = []
    for path in sorted(Path('.').rglob('*.html')):
        if path.name == '404.html':
            continue
        html = path.read_text(encoding='utf-8')
        title_match = re.search(r'<title[^>]*>(.*?)</title>', html, re.I | re.S)
        desc_match = re.search(r'<meta[^>]+name=["\']description["\'][^>]+content=["\']([^"\']+)["\']', html, re.I)
        canonical_match = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)["\']', html, re.I)
        title = title_match.group(1).strip() if title_match else 'OpenMe'
        description = desc_match.group(1).strip() if desc_match else 'OpenMe — аварійне відкриття та ремонт замків в Києві.'
        canonical = canonical_match.group(1).strip() if canonical_match else normalize_url(path, None)
        new_html = inject_og_and_service(html, title, description, canonical)
        if new_html != html:
            path.write_text(new_html, encoding='utf-8')
            updated.append(str(path))

    troieshchyna_file = Path('raiony') / 'troieshchyna' / 'index.html'
    if troieshchyna_file.exists():
        text = troieshchyna_file.read_text(encoding='utf-8')
        fixed = text.replace('https://openme.com.ua/ru/raiony/troieshchyna/', 'https://openme.com.ua/ru/raiony/troeshchina/')
        if fixed != text:
            troieshchyna_file.write_text(fixed, encoding='utf-8')
            updated.append(str(troieshchyna_file) + ' (hreflang corrected)')

    if updated:
        print('Updated files:')
        for entry in updated:
            print(entry)
    else:
        print('No files updated.')
