import os, re, json
from pathlib import Path

root = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
ua_dir = root / 'raiony'
ru_dir = root / 'ru' / 'raiony'

PHONE = None
# attempt to find a phone in index.html
try:
    idx = (root / 'index.html').read_text(encoding='utf-8')
    m = re.search(r'href=["\']tel:([^"\']+)["\']', idx)
    if m:
        PHONE = m.group(1)
except Exception:
    PHONE = None
if not PHONE:
    PHONE = '+380441234567'

ua_template_faq = [
    ("Скільки коштує виїзд майстра?", "Вартість виїзду по Києву зазвичай фіксована — уточнюйте при дзвінку; вартість робіт залежить від складності.") ,
    ("Чи можна відкрити двері без пошкоджень?", "Так, багато сучасних замків можна відкрити без пошкоджень — майстер підбере оптимальний метод.") ,
    ("Скільки часу займає відкриття?", "У типовому випадку — від 10 до 40 хвилин в залежності від замка та ситуації."),
    ("Чи надаєте гарантію?", "Так, на послуги з відкриття та встановлення замків надається гарантія — термін уточнюється індивідуально.") ,
    ("Чи потрібен документ власника?", "Якщо ви не власник, майстер може попросити підтвердження повноважень; у випадку екстреного відкриття ми реагуємо оперативно.")
]

ru_template_faq = [
    ("Сколько стоит выезд мастера?", "Стоимость выезда по Киеву фиксирована — уточняйте при звонке; цена работ зависит от сложности.") ,
    ("Можно ли открыть дверь без повреждений?", "Да, большинство современных замков можно открыть без повреждений — мастер выберет оптимальный метод."),
    ("Сколько времени занимает вскрытие?", "В типичном случае — от 10 до 40 минут в зависимости от замка и ситуации."),
    ("Даёте ли вы гарантию?", "Да, на работы по вскрытию и установке замков предоставляется гарантия — срок уточняется индивидуально."),
    ("Нужен ли документ владельца?", "Если вы не владелец, мастер может попросить подтверждение полномочий; в экстренном случае мы выезжаем оперативно.")
]

service_list_ua = ["Відкриття вхідних дверей","Заміна та ремонт замків","Відкриття сейфів","Відкриття гаражів","Терміновий виїзд майстра"]
service_list_ru = ["Вскрытие дверей","Замена и ремонт замков","Вскрытие сейфов","Вскрытие гаражей","Срочный выезд мастера"]

modified = []
issues_fixed = []

# helper
def ensure_head_inserts(text, inserts):
    # insert before </head>
    if '</head>' in text:
        return text.replace('</head>', inserts + '\n</head>')
    else:
        return inserts + '\n' + text


def process_page(path, lang):
    txt = path.read_text(encoding='utf-8')
    orig = txt
    changed = False
    rel = str(path.relative_to(root)).replace('\\','/')
    # title, meta, h1
    title_m = re.search(r'<title[^>]*>(.*?)</title>', txt, re.I|re.S)
    title = title_m.group(1).strip() if title_m else ''
    desc_m = re.search(r'<meta[^>]+name=["\']description["\'][^>]*content=["\'](.*?)["\']', txt, re.I|re.S)
    desc = desc_m.group(1).strip() if desc_m else ''
    h1_m = re.search(r'<h1[^>]*>(.*?)</h1>', txt, re.I|re.S)
    h1 = re.sub('<[^<]+>','', h1_m.group(1)).strip() if h1_m else ''

    # ensure uniqueness by appending raion identifier if identical to filename
    filename_raion = Path(path.parent.name).name
    if not title or filename_raion.replace('-',' ') in title.lower():
        # make title if missing or generic
        new_title = f"{h1} — Відкриття замків у Києві" if lang=='uk' else f"{h1} — Вскрытие замков в Киеве"
        if title != new_title:
            if title_m:
                txt = re.sub(r'<title[^>]*>.*?</title>', f'<title>{new_title}</title>', txt, flags=re.I|re.S)
            else:
                txt = txt.replace('</head>', f'  <title>{new_title}</title>\n</head>')
            changed = True
            issues_fixed.append((rel, 'title set/updated'))

    # meta description
    if not desc or len(desc) < 50:
        snippet = h1
        new_desc = (f"Термінове відкриття замків і дверей у {h1}. Виїзд майстра по району, досвідчений фахівець, гарантія на роботи.") if lang=='uk' else (f"Срочное вскрытие замков и дверей в {h1}. Выезд мастера по району, опытный специалист, гарантия на работы.")
        if desc_m:
            txt = re.sub(r'(<meta[^>]+name=["\']description["\'][^>]*content=["\'])(.*?)(["\'])', lambda m: m.group(1) + new_desc + m.group(3), txt, flags=re.I|re.S)
        else:
            # insert in head
            meta_tag = f'<meta name="description" content="{new_desc}">'
            txt = txt.replace('</head>', meta_tag + '\n</head>')
        changed = True
        issues_fixed.append((rel, 'meta description set/updated'))

    # canonical
    if not re.search(r'<link[^>]+rel=["\']canonical["\']', txt, re.I):
        url = 'https://openme.com.ua/' + rel.replace('index.html','')
        can = f'<link rel="canonical" href="{url}">'
        txt = txt.replace('</head>', can + '\n</head>')
        changed = True
        issues_fixed.append((rel, 'canonical added'))

    # hreflang: add counterpart if exists
    counterpart = None
    if lang=='uk':
        ru_path = root / 'ru' / rel
        if ru_path.exists():
            counterpart = 'https://openme.com.ua/' + ('ru/' + rel).replace('index.html','')
            alt_ru = f'<link rel="alternate" hreflang="ru" href="{counterpart}">'
            # also add ua link on RU later
            if 'hreflang' not in txt:
                txt = txt.replace('</head>', alt_ru + '\n</head>')
                changed = True
                issues_fixed.append((rel,'hreflang ru added'))
    else:
        ua_rel = rel.replace('ru/','')
        ua_path = root / ua_rel
        if ua_path.exists():
            counterpart = 'https://openme.com.ua/' + ua_rel.replace('index.html','')
            alt_ua = f'<link rel="alternate" hreflang="uk" href="{counterpart}">'
            if 'hreflang' not in txt:
                txt = txt.replace('</head>', alt_ua + '\n</head>')
                changed = True
                issues_fixed.append((rel,'hreflang uk added'))

    # Breadcrumb JSON-LD
    if 'BreadcrumbList' not in txt:
        # build simple breadcrumb
        home = {'@type':'ListItem','position':1,'name':'Головна' if lang=='uk' else 'Главная','item':'https://openme.com.ua/'}
        mid = {'@type':'ListItem','position':2,'name':'Райони' if lang=='uk' else 'Районы','item':'https://openme.com.ua/raiony/'}
        cur = {'@type':'ListItem','position':3,'name':h1 or filename_raion,'item':'https://openme.com.ua/' + rel.replace('index.html','')}
        bc = {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[home,mid,cur]}
        script = '<script type="application/ld+json">' + json.dumps(bc, ensure_ascii=False) + '</script>'
        txt = ensure_head_inserts(txt, script)
        changed = True
        issues_fixed.append((rel,'breadcrumb json-ld added'))

    # FAQ visible and FAQ JSON-LD
    # detect existing FAQ Qs
    faq_count = len(re.findall(r'<div[^>]+class=["\']?faq|<section[^>]+id=["\']faq', txt, re.I))
    # simpler: count <h3> or <h2> with question words
    qcount = len(re.findall(r'<h[23][^>]*>.*?(Питання|Питань|Питання:|Як|Чи|Скільки|Що|Когда|Как|Сколько|Нужно|Нужен).*?</h[23]>', txt, re.I))
    if qcount < 5:
        # add visible FAQ section before </main>
        faqs = ua_template_faq if lang=='uk' else ru_template_faq
        # tailor by h1
        place = h1 or filename_raion.replace('-',' ')
        faq_html = '\n<section id="faq" class="faq">\n  <h2>' + ('Часті питання' if lang=='uk' else 'Частые вопросы') + '</h2>\n  <div class="faq-list">\n'
        for q,a in faqs:
            faq_html += f'    <details><summary>{q}</summary><div><p>{a}</p></div></details>\n'
        faq_html += '  </div>\n</section>\n'
        txt = txt.replace('</main>', faq_html + '\n</main>')
        changed = True
        issues_fixed.append((rel,'visible faq added'))
        # add JSON-LD for FAQPage in head
        faq_items = []
        for q,a in faqs:
            faq_items.append({'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}})
        faq_ld = {'@context':'https://schema.org','@type':'FAQPage','mainEntity':faq_items}
        script = '<script type="application/ld+json">' + json.dumps(faq_ld, ensure_ascii=False) + '</script>'
        txt = ensure_head_inserts(txt, script)
        changed = True
        issues_fixed.append((rel,'faq json-ld added'))

    # local mention check: look for 'метро' or 'вулиц' or 'парк'
    if not re.search(r'метро|вулиц|вул\.|парк|мікрорайон|ст\.м\.|проспект', txt, re.I):
        # insert a small paragraph before </main>
        place = h1 or filename_raion.replace('-',' ')
        local_p = ('<p>Майстри працюють по всьому району, включаючи мікрорайони та околиці, поруч із місцевими орієнтирами та станціями метро.</p>') if lang=='uk' else ('<p>Мастера работают по всему району, включая микрорайоны и окрестности, рядом с местными ориентирами и станциями метро.</p>')
        txt = txt.replace('</main>', local_p + '\n</main>')
        changed = True
        issues_fixed.append((rel,'local mention added'))

    # 'Коли викликають майстра' block
    keyphrase = 'Коли викликають майстра' if lang=='uk' else 'Когда вызывают мастера'
    if keyphrase.lower() not in txt.lower():
        block = '\n<section class="when">\n  <h2>' + ( 'Коли викликають майстра' if lang=='uk' else 'Когда вызывают мастера') + '</h2>\n  <ul>\n'
        points = [
            'Ключ застряг у замку' if lang=='uk' else 'Ключ застрял в замке',
            'Втрачено ключі / потрібно замінити замок' if lang=='uk' else 'Потеряны ключи / нужно заменить замок',
            'Потрібно потрапити до квартири чи офісу' if lang=='uk' else 'Нужно попасть в квартиру или офис',
            'Замок після взлому чи пошкодження' if lang=='uk' else 'Замок после взлома или повреждения',
            'Гарантійне відновлення або заміна' if lang=='uk' else 'Гарантийный ремонт или замена'
        ]
        for p in points:
            block += f'    <li>{p}</li>\n'
        block += '  </ul>\n</section>\n'
        txt = txt.replace('</main>', block + '\n</main>')
        changed = True
        issues_fixed.append((rel,'' + ('when block added' if lang=='uk' else 'when block added')))

    # services block
    if not re.search(r'Відкриття|замін|ремонт|сейф|гараж|вскрыт', txt, re.I):
        services = service_list_ua if lang=='uk' else service_list_ru
        serv_html = '\n<section class="services"><h2>' + ('Наші послуги' if lang=='uk' else 'Наши услуги') + '</h2><ul>\n'
        for s in services:
            serv_html += f'  <li>{s}</li>\n'
        serv_html += '</ul></section>\n'
        txt = txt.replace('</main>', serv_html + '\n</main>')
        changed = True
        issues_fixed.append((rel,'services block added'))

    # CTA
    if not re.search(r'href=["\']tel:|Зателефонуйте|Зв"язатися|Позвоните|Заказать', txt, re.I):
        cta_html = f'<p class="cta"><a href="tel:{PHONE}">{"Зателефонуйте" if lang=="uk" else "Позвоните"}: {PHONE}</a></p>'
        txt = txt.replace('</main>', cta_html + '\n</main>')
        changed = True
        issues_fixed.append((rel,'cta added'))

    if changed:
        path.write_text(txt, encoding='utf-8')
        modified.append(rel)


# gather all raion pages
pages = []
for d in [ua_dir, ru_dir]:
    if d.exists():
        for child in d.iterdir():
            if child.is_dir():
                idx = child / 'index.html'
                if idx.exists():
                    pages.append(idx)

for p in pages:
    lang = 'uk' if '/ru/' not in str(p).replace('\\','/') else 'ru'
    process_page(p, lang)

# output a report
report = {'modified_files': modified, 'issues_fixed': issues_fixed}
print(json.dumps(report, ensure_ascii=False, indent=2))
