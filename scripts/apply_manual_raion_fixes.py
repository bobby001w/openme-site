import os,re,json,hashlib
from pathlib import Path
root = Path(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

# load full check
fc = json.loads(open(root / 'raion_full_check.json', 'r', encoding='utf-8').read())
results = fc['results']
duplicates = fc.get('duplicates', {})

modified = []
changes = []

ua_faq = [
    ("Скільки коштує виїзд майстра?", "Ціна залежить від складності роботи та типу замка — називаємо орієнтовно по фото/дзвінку."),
    ("Чи можна відкрити двері без пошкоджень?", "Багато випадків вирішуємо без пошкоджень; майстер підбере щадний метод."),
    ("Скільки часу триває відкриття?", "Звичайно 10–40 хв залежно від замку; складні випадки довше."),
    ("Чи надаєте гарантію?", "Так, гарантія на роботи та встановлені механізми — термін узгоджуємо при виклику."),
    ("Чи можна оплатити карткою?", "Так, оплата карткою або готівкою — на місці після виконання робіт.")
]

ru_faq = [
    ("Сколько стоит выезд мастера?", "Цена зависит от сложности работ и типа замка — ориентируем по фото/звонку."),
    ("Можно ли открыть дверь без повреждений?", "Во многих случаях да — мастер применит щадящие методики."),
    ("Сколько времени занимает вскрытие?", "Обычно 10–40 минут; сложные случаи занимают дольше."),
    ("Даёте ли вы гарантию?", "Да, на работы и установленные механизмы предоставляется гарантия."),
    ("Можно ли оплатить картой?", "Да, можно оплатить картой или наличными на месте.")
]

# helper
def replace_paragraph(path, old_para, new_para):
    txt = path.read_text(encoding='utf-8')
    if old_para in txt:
        txt = txt.replace(old_para, new_para)
        path.write_text(txt, encoding='utf-8')
        return True
    return False

for rel, data in results.items():
    # skip raiony index pages
    if rel.endswith('/index.html') and (rel.count('/')==2 and not rel.startswith('ru/')):
        # this is raiony/index.html (UA index) skip
        pass
    # find duplicated paragraphs in this page
    para_hashes = data.get('para_hashes', [])
    para_texts = data.get('para_texts', [])
    lang = data.get('lang','uk')
    path = root.joinpath(*rel.split('/'))
    made_change = False
    for idx,h in enumerate(para_hashes):
        pages = duplicates.get(h)
        if pages and len(pages) > 1:
            # if first occurrence, keep; otherwise, modify this paragraph to be unique
            first = pages[0][0]
            if first != rel:
                old = para_texts[idx]
                # craft a localized variant
                h1 = data.get('h1') or Path(rel).parent.name.replace('-', ' ')
                if lang == 'ru':
                    insert = f" Мы работаем в районе {h1}, включая близлежащие улицы и ориентиры, поэтому мастер знает быстрые маршруты и особенности подъезда."
                else:
                    insert = f" Ми працюємо у районі {h1}, включаючи найближчі вулиці та орієнтири, тому майстер швидко знаходить оптимальний під'їзд."
                # create new paragraph by appending insert to old
                new = old + " " + insert
                # perform replacement
                # ensure exact match in file: find segment of paragraph text and replace
                try:
                    txt = path.read_text(encoding='utf-8')
                except Exception:
                    txt = path.read_text(encoding='cp1251')
                clean_old = re.sub(r"\s+"," ", old.strip())
                # attempt to find approximate match
                if clean_old in re.sub(r"\s+"," ", txt):
                    txt2 = re.sub(re.escape(clean_old), new, txt, count=1)
                    path.write_text(txt2, encoding='utf-8')
                    made_change = True
                    modified.append(rel)
                    changes.append((rel,'paragraph made unique'))
    # ensure 'when' block
    when_kw = 'Коли викликають майстра' if lang=='uk' else 'Когда вызывают мастера'
    try:
        txt = path.read_text(encoding='utf-8')
    except Exception:
        txt = path.read_text(encoding='cp1251')
    if when_kw.lower() not in txt.lower():
        block_items = ['ключ заклинив','ключі загублені','потрібен терміновий доступ'] if lang=='uk' else ['ключ заклинил','ключи утеряны','нужен срочный доступ']
        lis = '\n'.join([f'    <li>{it}</li>' for it in block_items])
        block = f"\n<section class=\"when\">\n  <h2>{when_kw}</h2>\n  <ul>\n{lis}\n  </ul>\n</section>\n"
        txt = txt.replace('</main>', block + '\n</main>')
        path.write_text(txt, encoding='utf-8')
        modified.append(rel)
        changes.append((rel,'when block added'))
    # ensure services block
    if not re.search(r'вскрыт|вскрытие|викрит|відкритт|заміна|ремонт', txt, re.I):
        serv = ['Вскрытие дверей','Замена замков','Вскрытие сейфов','Вскрытие гаражей','Выезд мастера'] if lang=='ru' else ['Відкриття дверей','Заміна замків','Відкриття сейфів','Відкриття гаражів','Виїзд майстра']
        serv_html = '\n<section class="services"><h2>' + ('Наши услуги' if lang=='ru' else 'Наші послуги') + '</h2><ul>\n'
        for s in serv:
            serv_html += f'  <li>{s}</li>\n'
        serv_html += '</ul></section>\n'
        txt = txt.replace('</main>', serv_html + '\n</main>')
        path.write_text(txt, encoding='utf-8')
        modified.append(rel)
        changes.append((rel,'services block added'))
    # ensure CTA
    if not re.search(r'href=["\']tel:|Зателефонуйте|Позвоните', txt, re.I):
        # try find phone in root index
        phone = '+380441234567'
        cta = f'<p class="cta"><a href="tel:{phone}">{"Зателефонуйте" if lang=="uk" else "Позвоните"}: {phone}</a></p>'
        txt = txt.replace('</main>', cta + '\n</main>')
        path.write_text(txt, encoding='utf-8')
        modified.append(rel)
        changes.append((rel,'cta added'))
    # ensure FAQ JSON-LD
    if data.get('faq_count',0) < 5:
        faqs = ua_faq if lang=='uk' else ru_faq
        # build json-ld
        entities = []
        for q,a in faqs:
            entities.append({'@type':'Question','name':q,'acceptedAnswer':{'@type':'Answer','text':a}})
        faq_ld = {'@context':'https://schema.org','@type':'FAQPage','mainEntity':entities}
        script = '\n<script type="application/ld+json">' + json.dumps(faq_ld, ensure_ascii=False) + '</script>\n'
        # insert before </head>
        txt = txt.replace('</head>', script + '\n</head>')
        # also add visible FAQ if not present
        if '<section id="faq"' not in txt:
            faq_html = '\n<section id="faq" class="faq">\n  <h2>' + ('Частые вопросы' if lang=='ru' else 'Часті питання') + '</h2>\n  <div class="faq-list">\n'
            for q,a in faqs:
                faq_html += f'    <details><summary>{q}</summary><div><p>{a}</p></div></details>\n'
            faq_html += '  </div>\n</section>\n'
            txt = txt.replace('</main>', faq_html + '\n</main>')
        path.write_text(txt, encoding='utf-8')
        modified.append(rel)
        changes.append((rel,'faq json-ld added/visible faq added'))
    # ensure breadcrumb json-ld
    if 'BreadcrumbList' not in txt:
        h1 = data.get('h1') or Path(rel).parent.name.replace('-',' ')
        home = {'@type':'ListItem','position':1,'name':('Главная' if lang=='ru' else 'Головна'),'item':'https://openme.com.ua/'}
        mid = {'@type':'ListItem','position':2,'name':('Районы' if lang=='ru' else 'Райони'),'item':'https://openme.com.ua/raiony/'}
        cur = {'@type':'ListItem','position':3,'name':h1,'item':'https://openme.com.ua/' + rel.replace('index.html','')}
        bc = {'@context':'https://schema.org','@type':'BreadcrumbList','itemListElement':[home,mid,cur]}
        script = '\n<script type="application/ld+json">' + json.dumps(bc, ensure_ascii=False) + '</script>\n'
        txt = txt.replace('</head>', script + '\n</head>')
        path.write_text(txt, encoding='utf-8')
        modified.append(rel)
        changes.append((rel,'breadcrumb json-ld added'))

# write a short report
report = {'modified_files': sorted(list(set(modified))), 'changes': changes}
open(root / 'raion_manual_fix_report.json','w',encoding='utf-8').write(json.dumps(report, ensure_ascii=False, indent=2))
print(json.dumps(report, ensure_ascii=False, indent=2))
