import json
import os
import re
from pathlib import Path

root = Path(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
issues_path = root / 'remaining_issues.json'
remaining = json.loads(issues_path.read_text(encoding='utf-8'))

COUNTERPARTS = {
    'avariine-vidkryttia-avto/': 'ru/avarijnoe-vskrytie-avto/',
    'avariine-vidkryttia-dverei/': 'ru/avarijnoe-vskrytie-dverej/',
    'remont-zamina-zamkiv/': 'ru/remont-zamena-zamkov/',
    'vidkryttia-harazhiv/': 'ru/vskrytie-garazhej/',
    'vidkryttia-seifiv/': 'ru/vskrytie-sejfov/',
    'raiony/': 'ru/raiony/',
    'raiony/obolon/': 'ru/raiony/obolon/',
    'raiony/pozniaky/': 'ru/raiony/poznyaki/',
    'raiony/pechersk/': 'ru/raiony/pechersk/',
    'raiony/troieshchyna/': 'ru/raiony/troeshchina/',
    'raiony/solomianskyi-raion/': 'ru/raiony/solomenskiy-raion/',
    'raiony/shevchenkivskyi-raion/': 'ru/raiony/shevchenkovskiy-raion/',
    'raiony/holosiivskyi-raion/': 'ru/raiony/goloseevskiy-raion/',
    'raiony/darnytskyi-raion/': 'ru/raiony/darnitskiy-raion/',
    'raiony/desnianskyi-raion/': 'ru/raiony/desnyanskiy-raion/',
    'raiony/podilskyi-raion/': 'ru/raiony/podolskiy-raion/',
    'raiony/sviatoshynskyi-raion/': 'ru/raiony/svyatoshinskiy-raion/',
    'raiony/dniprovskyi-raion/': 'ru/raiony/dneprovskiy-raion/',
    'index.html': 'ru/index.html',
}
# reverse mapping for RU -> UA
COUNTERPARTS.update({v: k for k, v in list(COUNTERPARTS.items())})

META_TEMPLATES = {
    '404.html': {
        'uk': 'Сторінка не знайдена. Поверніться на головну або зателефонуйте майстру OpenMe для термінового відкриття замків у Києві.',
    },
    'index.html': {
        'uk': 'OpenMe пропонує аварійне відкриття замків, дверей, авто, сейфів і гаражів у Києві. Дзвоніть 24/7 для виїзду майстра.',
        'ru': 'OpenMe предлагает аварийное вскрытие замков, дверей, авто, сейфов и гаражей в Киеве. Звоните 24/7 для выезда мастера.',
    },
    'avariine-vidkryttia-avto/': {
        'uk': 'Відкриття авто у Києві без пошкоджень. Допомога при ключах в салоні, розрядженому акумуляторі або багажнику.',
        'ru': 'Вскрытие авто в Киеве без повреждений. Помощь при ключах в салоне, разряженном аккумуляторе или проблемах с багажником.',
    },
    'avariine-vidkryttia-dverei/': {
        'uk': 'Аварійне відкриття дверей у Києві. Майстер відкриє квартиру, офіс або під’їзд акуратно та оперативно.',
        'ru': 'Аварийное вскрытие дверей в Киеве. Мастер откроет квартиру, офис или подъезд аккуратно и оперативно.',
    },
    'remont-zamina-zamkiv/': {
        'uk': 'Ремонт і заміна замків у Києві. Відновлюємо працездатність замка або встановлюємо новий із виїздом майстра.',
        'ru': 'Ремонт и замена замков в Киеве. Восстанавливаем замок или устанавливаем новый с выездом мастера.',
    },
    'vidkryttia-harazhiv/': {
        'uk': 'Відкриття гаражів у Києві. Швидко та акуратно розкриваємо гаражні та роллетні замки.',
        'ru': 'Вскрытие гаражей в Киеве. Быстро и аккуратно открываем гаражные и рольставневые замки.',
    },
    'vidkryttia-seifiv/': {
        'uk': 'Відкриття сейфів у Києві. Працюємо з механічними та електронними замками, зберігаючи конфіденційність.',
        'ru': 'Вскрытие сейфов в Киеве. Работаем с механическими и электронными замками, сохраняя конфиденциальность.',
    },
}

FAQ_TEMPLATES = {
    'index.html': {
        'uk': [
            ('Які послуги надає OpenMe?', 'Ми відкриваємо двері, авто, сейфи, гаражі, ремонтуємо та замінюємо замки по Києву 24/7.'),
            ('Скільки часу займає виїзд майстра?', 'Час виїзду залежить від району, зазвичай 20–60 хвилин у межах Києва.'),
            ('Чи можна відкрити двері без пошкоджень?', 'У більшості випадків використовується акуратна техніка, яка не пошкоджує замок або двері.'),
            ('Чи приїжджають уночі?', 'Так, служба працює цілодобово, включно з нічними викликами.'),
            ('Як швидко можна дізнатися ціну?', 'Ми називаємо орієнтовну ціну після опису замка або фото, а остаточну — після огляду на місці.'),
        ],
        'ru': [
            ('Какие услуги предлагает OpenMe?', 'Мы вскрываем двери, авто, сейфы, гаражи, ремонтируем и заменяем замки по Киеву 24/7.'),
            ('Сколько времени занимает выезд мастера?', 'Время выезда зависит от района, обычно 20–60 минут в пределах Киева.'),
            ('Можно ли открыть дверь без повреждений?', 'В большинстве случаев используется аккуратная техника, не повреждающая замок или дверь.'),
            ('Работаете ли вы ночью?', 'Да, служба работает круглосуточно, включая ночные вызовы.'),
            ('Когда вы называете цену?', 'Ориентировочную цену называем по фото или описанию, окончательная цена после осмотра.'),
        ],
    },
    'avariine-vidkryttia-avto/': {
        'uk': [
            ('Чи можна відкрити авто без розбиття скла?', 'Так, ми працюємо без розбиття скла, використовуючи спеціалізовані методики.'),
            ('Що робити, якщо ключі залишилися в салоні?', 'Подзвоніть нам, майстер приїде і відкриє авто акуратно без пошкоджень.'),
            ('Чи ви працюєте з електромобілями?', 'Так, ми працюємо з більшістю сучасних авто, включно з гібридними та електромобілями.'),
            ('Скільки коштує відкриття авто?', 'Ціна залежить від марки та ситуації, орієнтовно від {{PRICE_CAR}} грн.'),
            ('Чи потрібен документ власника?', 'Якщо ви не власник, може знадобитися підтвердження повноважень, але в екстрених випадках виїжджаємо швидко.'),
        ],
        'ru': [
            ('Можно ли открыть авто без разбития стекла?', 'Да, мы работаем без разбития стекла, используя специализированные методики.'),
            ('Что делать, если ключи остались в салоне?', 'Позвоните нам, мастер приедет и аккуратно откроет авто без повреждений.'),
            ('Работаете ли вы с электромобилями?', 'Да, мы работаем с большинством современных авто, включая гибриды и электромобили.'),
            ('Сколько стоит вскрытие авто?', 'Цена зависит от марки и ситуации, ориентировочно от {{PRICE_CAR}} грн.'),
            ('Нужен ли документ владельца?', 'Если вы не владелец, может потребоваться подтверждение полномочий, но в экстренном случае выезжаем быстро.'),
        ],
    },
    'avariine-vidkryttia-dverei/': {
        'uk': [
            ('Чи можна відкрити вхідні двері без пошкоджень?', 'Так, багато типів замків відкриваємо акуратно без пошкоджень дверей.'),
            ('Скільки часу займає відкриття дверей?', 'Зазвичай 15–45 хвилин залежно від замка та замаслювання механізму.'),
            ('Чи ви приїжджаєте у під’їзд?', 'Так, виїжджаємо до квартир, приватних будинків, офісів і під’їздів.'),
            ('Чи можна відкрити двері після замку MultiLock?', 'Так, майстер підбере метод для складних мультизамків та броньованих дверей.'),
            ('Чи можна встановити новий замок одразу?', 'У багатьох випадках можна зробити заміну під час виїзду, якщо є потрібний замок.'),
        ],
        'ru': [
            ('Можно ли открыть входную дверь без повреждений?', 'Да, многие типы замков открываем аккуратно без повреждений двери.'),
            ('Сколько времени занимает вскрытие двери?', 'Обычно 15–45 минут в зависимости от замка и состояния механизма.'),
            ('Вы приезжаете в подъезд?', 'Да, выезжаем в квартиры, частные дома, офисы и подъезды.'),
            ('Можно ли открыть дверь после замка MultiLock?', 'Да, мастер подберет метод для сложных мултизамков и бронедверей.'),
            ('Можно ли сразу установить новый замок?', 'В многих случаях можно заменить замок при выезде, если есть нужная модель.'),
        ],
    },
    'remont-zamina-zamkiv/': {
        'uk': [
            ('Коли варто ремонтувати замок, а не замінювати?', 'Якщо механізм працює, але клинить, ми ремонтуємо; якщо замок зношений або пошкоджений, рекомендуємо заміну.'),
            ('Чи замінюєте серцевину замка?', 'Так, майстер може замінити серцевину або весь замок на новий під час виїзду.'),
            ('Чи потрібна попередня діагностика?', 'Перш ніж працювати, майстер оглядає замок і розповідає варіанти ремонту.'),
            ('Яка гарантія на ремонт?', 'Гарантія на роботи та запчастини надається індивідуально, уточнюйте при дзвінку.'),
            ('Чи можна замінити замок після злому?', 'Так, ми встановлюємо нові замки після злому або спроби відмикання.'),
        ],
        'ru': [
            ('Когда стоит ремонтировать замок, а не менять?', 'Если механизм работает, но клинит, мы ремонтируем; если замок изношен или поврежден, рекомендуем замену.'),
            ('Меняете ли вы сердцевину замка?', 'Да, мастер может заменить сердцевину или весь замок на новый при выезде.'),
            ('Нужна ли предварительная диагностика?', 'Перед работой мастер осматривает замок и рассказывает варианты ремонта.'),
            ('Какая гарантия на ремонт?', 'Гарантия на работы и запчасти предоставляется индивидуально, уточняйте при звонке.'),
            ('Можно ли заменить замок после взлома?', 'Да, мы устанавливаем новые замки после взлома или попытки вскрытия.'),
        ],
    },
    'vidkryttia-harazhiv/': {
        'uk': [
            ('Чи відкриваєте гаражні замки та ролетні системи?', 'Так, працюємо з гаражними замками, ролетами та секційними воротами.'),
            ('Чи приїжджаєте до приватних гаражів і кооперативів?', 'Так, виїжджаємо в гаражні кооперативи, приватні та сусідні парковки.'),
            ('Скільки коштує відкриття гаража?', 'Ціна залежить від типу замка та механізму, орієнтовно від {{PRICE_GARAGE}} грн.'),
            ('Чи можна відкрити замок уночі?', 'Так, ми працюємо цілодобово, тому виїжджаємо навіть вночі.'),
            ('Чи можна змінити замок після відкриття?', 'Так, майстер може одразу встановити новий замок після відкриття.'),
        ],
        'ru': [
            ('Открываете ли вы гаражные замки и роллеты?', 'Да, работаем с гаражными замками, рольставнями и секционными воротами.'),
            ('Выезжаете ли вы к частным гаражам и кооперативам?', 'Да, выезжаем в гаражные кооперативы, частные и соседние парковки.'),
            ('Сколько стоит открытие гаража?', 'Цена зависит от типа замка и механизма, ориентировочно от {{PRICE_GARAGE}} грн.'),
            ('Можно ли открыть замок ночью?', 'Да, мы работаем круглосуточно, поэтому выезжаем даже ночью.'),
            ('Можно ли заменить замок сразу после открытия?', 'Да, мастер может сразу установить новый замок после открытия.'),
        ],
    },
    'vidkryttia-seifiv/': {
        'uk': [
            ('Чи працюєте з електронними сейфами?', 'Так, відкриваємо як механічні, так і електронні сейфи, зберігаючи конфіденційність.'),
            ('Чи можна відкрити сейф без пошкоджень?', 'Ми мінімізуємо ризик пошкодження корпусу і внутрішнього механізму.'),
            ('Що робити, якщо забули код?', 'Зателефонуйте, майстер підбере метод залежно від типу сейфа.'),
            ('Чи потрібен документ власника?', 'У багатьох випадках майстер може попросити підтвердження права доступу.'),
            ('Скільки часу займає відкриття сейфа?', 'Зазвичай від 30 до 90 хвилин, залежно від моделі і доступу.'),
        ],
        'ru': [
            ('Работаете ли вы с электронными сейфами?', 'Да, открываем как механические, так и электронные сейфы, сохраняя конфиденциальность.'),
            ('Можно ли открыть сейф без повреждений?', 'Мы минимизируем риск повреждения корпуса и внутреннего механизма.'),
            ('Что делать, если забыли код?', 'Позвоните, мастер подберет метод в зависимости от типа сейфа.'),
            ('Нужен ли документ владельца?', 'Во многих случаях мастер может попросить подтверждение права доступа.'),
            ('Сколько времени занимает открытие сейфа?', 'Обычно от 30 до 90 минут в зависимости от модели и доступа.'),
        ],
    },
    'raiony/index.html': {
        'uk': [
            ('В яких районах Києва ви працюєте?', 'Ми обслуговуємо центральні та віддалені райони Києва, включно з Оболонню, Печерськом, Позняками і Троєщиною.'),
            ('Чи виїжджаєте в ті райони, де поганий під’їзд?', 'Так, майстер працює з будь-якими адресами в межах Києва, в тому числі з вузькими вулицями та закритими під’їздами.'),
            ('Скільки часу займає приїзд в районі Києва?', 'У межах міста зазвичай 20–60 хвилин, залежно від завантаження і конкретного району.'),
            ('Чи можна викликати майстра на квартиру?', 'Так, ми виїжджаємо на квартири, приватні будинки і офіси по всіх районах Києва.'),
            ('Як знайти свій район на сайті?', 'Клікніть на потрібний район у списку, щоб подивитися послуги та переваги роботи в цій частині міста.'),
        ],
        'ru': [
            ('В каких районах Киева вы работаете?', 'Мы обслуживаем центральные и удаленные районы Киева, включая Оболонь, Печерск, Позняки и Троещину.'),
            ('Вы выезжаете в районы с плохим подъездом?', 'Да, мастер работает с любыми адресами в пределах Киева, включая узкие улицы и закрытые подъезды.'),
            ('Сколько времени занимает приезд в районе Киева?', 'В пределах города обычно 20–60 минут в зависимости от загруженности и района.'),
            ('Можно ли вызвать мастера на квартиру?', 'Да, мы выезжаем на квартиры, частные дома и офисы по всем районам Киева.'),
            ('Как найти свой район на сайте?', 'Нажмите на нужный район в списке, чтобы увидеть услуги и преимущества работы в этой части города.'),
        ],
    },
    'ru/index.html': {
        'ru': [
            ('Какие услуги предлагает OpenMe?', 'Мы вскрываем двери, авто, сейфы, гаражи и ремонтируем замки по Киеву круглосуточно.'),
            ('Как быстро мастер выезжает?', 'Время выезда зависит от района, обычно 20–60 минут в пределах города.'),
            ('Можно ли вызвать мастера ночью?', 'Да, мы работаем 24/7 и можем выехать ночью на срочный вызов.'),
            ('Как оплатить услугу?', 'Оплата возможна наличными или переводом, уточняйте удобный способ при звонке.'),
            ('Что делать, если не нашли нужную страницу?', 'Позвоните нам, і ми підкажемо найближчий сервіс або районну сторінку.'),
        ],
    },
    'ru/raiony/index.html': {
        'ru': [
            ('В каких районах Киева вы работаете?', 'Мы обслуживаем районы Киева: Оболонь, Печерск, Позняки, Троещину, Соломенский и другие.'),
            ('Есть ли у вас выезд в удаленные районы?', 'Да, мастер выезжает в любые районы Киева, включая отдаленные жилые массивы.'),
            ('Можно ли выбрать район на сайте?', 'Да, на странице районов можно перейти к нужному району и получить описание услуг.'),
            ('Работаете ли вы с многоэтажными домами?', 'Да, выезда возможны к квартирам и офисам даже в центральных многоэтажках.'),
            ('Как быстро вы отвечаете на звонок?', 'Мы стараемся ответить быстро и направить мастера как можно скорее.'),
        ],
    },
    '404.html': {
        'uk': [
            ('Що означає ця сторінка?', 'Це означає, що сторінка не знайдена. Поверніться на головну або зателефонуйте нам для швидкої допомоги.'),
            ('Як знайти потрібний розділ сайту?', 'Використайте меню або перейдіть на головну сторінку, щоб обрати потрібну послугу чи район.'),
            ('Чи можна викликати майстра з цієї сторінки?', 'Так, просто натисніть на телефонний номер у шапці або нижній частині сайту.'),
            ('Чи працює OpenMe 24/7?', 'Так, ми працюємо цілодобово, тому ви можете звернутися в будь-який час.'),
            ('Чи можна отримати допомогу, якщо сторінка не відкривається?', 'Так, зателефонуйте або напишіть у месенджер, ми одразу підкажемо, як отримати послугу.'),
        ],
    },
}

PAGE_LINKS = {
    'uk': [
        ('/raiony/', 'Райони Києва'),
        ('/avariine-vidkryttia-avto/', 'Відкриття авто'),
        ('/avariine-vidkryttia-dverei/', 'Відкриття дверей'),
        ('/remont-zamina-zamkiv/', 'Ремонт замків'),
    ],
    'ru': [
        ('/ru/raiony/', 'Районы Киева'),
        ('/ru/avarijnoe-vskrytie-avto/', 'Вскрытие авто'),
        ('/ru/avarijnoe-vskrytie-dverej/', 'Вскрытие дверей'),
        ('/ru/remont-zamena-zamkov/', 'Ремонт замков'),
    ],
}

PHONE = None
try:
    index_text = (root / 'index.html').read_text(encoding='utf-8')
    m = re.search(r'href=["\']tel:([^"\']+)["\']', index_text)
    if m:
        PHONE = m.group(1)
except Exception:
    PHONE = None
if not PHONE:
    PHONE = '+380441234567'


def head_insert(text, insert):
    if '</head>' in text:
        return text.replace('</head>', insert + '\n</head>')
    return insert + '\n' + text


def ensure_link(text, tag):
    if tag in text:
        return text
    return head_insert(text, tag)


def rel_from_path(path):
    rel = str(path.relative_to(root)).replace('\\', '/')
    return rel


def page_name(rel, lang):
    title_match = re.search(r'<h1[^>]*>(.*?)</h1>', page_texts[rel], re.I|re.S)
    if title_match:
        return re.sub('<[^<]+>', '', title_match.group(1)).strip()
    if rel.endswith('index.html'):
        rel_no_index = rel[:-10]
        rel_no_index = rel_no_index.rstrip('/')
        return rel_no_index.replace('ru/', '').replace('-', ' ').title()
    return rel.replace('ru/', '').replace('-', ' ').title()


def build_breadcrumb(rel, lang, current_name):
    items = []
    home_name = 'Головна' if lang == 'uk' else 'Главная'
    home_url = 'https://openme.com.ua/' if lang == 'uk' else 'https://openme.com.ua/'
    items.append({'@type': 'ListItem', 'position': 1, 'name': home_name, 'item': home_url})
    if rel == 'index.html' or rel == 'ru/index.html':
        return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}
    if rel == '404.html':
        items.append({'@type': 'ListItem', 'position': 2, 'name': '404', 'item': 'https://openme.com.ua/404.html'})
        return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}
    if rel.endswith('raiony/index.html'):
        mid_name = 'Райони' if lang == 'uk' else 'Районы'
        mid_url = 'https://openme.com.ua/raiony/' if lang == 'uk' else 'https://openme.com.ua/ru/raiony/'
        items.append({'@type': 'ListItem', 'position': 2, 'name': mid_name, 'item': mid_url})
        if rel not in ('raiony/index.html', 'ru/raiony/index.html'):
            items.append({'@type': 'ListItem', 'position': 3, 'name': current_name, 'item': build_url(rel)})
        return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}
    if rel.startswith('raiony/') or rel.startswith('ru/raiony/'):
        mid_name = 'Райони' if lang == 'uk' else 'Районы'
        mid_url = 'https://openme.com.ua/raiony/' if lang == 'uk' else 'https://openme.com.ua/ru/raiony/'
        items.append({'@type': 'ListItem', 'position': 2, 'name': mid_name, 'item': mid_url})
        items.append({'@type': 'ListItem', 'position': 3, 'name': current_name, 'item': build_url(rel)})
        return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}
    items.append({'@type': 'ListItem', 'position': 2, 'name': current_name, 'item': build_url(rel)})
    return {'@context': 'https://schema.org', '@type': 'BreadcrumbList', 'itemListElement': items}


def build_url(rel):
    url = 'https://openme.com.ua/' + rel.replace('index.html', '')
    return url


def faq_items_for(rel, lang):
    key = rel
    if key not in FAQ_TEMPLATES and key.endswith('index.html'):
        key = rel
    tpl = FAQ_TEMPLATES.get(key)
    if tpl and lang in tpl:
        return tpl[lang]
    # fallback generic
    base = FAQ_TEMPLATES['index.html'][lang]
    return base


def meta_for(rel, lang, current_name):
    key = rel
    if key in META_TEMPLATES and lang in META_TEMPLATES[key]:
        return META_TEMPLATES[key][lang]
    rel_no_index = rel if not rel.endswith('index.html') else rel[:-10]
    rel_no_index = rel_no_index.rstrip('/')
    if rel_no_index in META_TEMPLATES and lang in META_TEMPLATES[rel_no_index]:
        return META_TEMPLATES[rel_no_index][lang]
    if lang == 'uk':
        return f'{current_name} у Києві. Термінове відкриття, ремонт та виїзд майстра по місту.'
    else:
        return f'{current_name} в Киеве. Срочное вскрытие, ремонт и выезд мастера по городу.'


def build_internal_links(lang):
    return PAGE_LINKS[lang]


page_texts = {}
for path in root.rglob('*.html'):
    rel = rel_from_path(path)
    page_texts[rel] = path.read_text(encoding='utf-8')

modified = []
fixed = []

for rel in set(sum([v for v in remaining.values()], [])):
    path = root / rel
    if not path.exists():
        continue
    text = path.read_text(encoding='utf-8')
    lang = 'ru' if rel.startswith('ru/') else 'uk'
    current_name = page_name(rel, lang)
    current_url = build_url(rel)
    changed = False

    # Meta description
    if not re.search(r'<meta[^>]+name=["\']description["\']', text, re.I):
        desc = meta_for(rel, lang, current_name)
        meta_tag = f'<meta name="description" content="{desc}">'
        text = text.replace('</head>', meta_tag + '\n</head>')
        changed = True
        fixed.append((rel, 'meta description'))

    # canonical
    if not re.search(r'<link[^>]+rel=["\']canonical["\']', text, re.I):
        can = f'<link rel="canonical" href="{current_url}">'
        text = text.replace('</head>', can + '\n</head>')
        changed = True
        fixed.append((rel, 'canonical'))

    # hreflang alternates
    alt_tags = set(re.findall(r'<link[^>]+rel=["\']alternate["\'][^>]*>', text, re.I))
    if rel == '404.html':
        pass
    else:
        key = rel if rel in COUNTERPARTS else (rel[:-10] if rel.endswith('index.html') else rel)
        counterpart = COUNTERPARTS.get(key)
        if counterpart:
            ua_url = build_url(rel if lang == 'uk' else counterpart)
            ru_url = build_url(rel if lang == 'ru' else counterpart)
            ua_tag = f'<link rel="alternate" hreflang="uk" href="{ua_url}">' if lang == 'uk' else f'<link rel="alternate" hreflang="uk" href="{ua_url}">'
            ru_tag = f'<link rel="alternate" hreflang="ru" href="{ru_url}">' if lang == 'ru' else f'<link rel="alternate" hreflang="ru" href="{ru_url}">'
            if ua_tag not in text:
                text = text.replace('</head>', ua_tag + '\n</head>')
                changed = True
                fixed.append((rel, 'hreflang uk'))
            if ru_tag not in text:
                text = text.replace('</head>', ru_tag + '\n</head>')
                changed = True
                fixed.append((rel, 'hreflang ru'))
            if rel == 'index.html' and 'x-default' not in text:
                xdef = f'<link rel="alternate" hreflang="x-default" href="{ua_url}">'
                text = text.replace('</head>', xdef + '\n</head>')
                changed = True
                fixed.append((rel, 'hreflang x-default'))

    # BreadcrumbList
    if 'BreadcrumbList' not in text:
        bc = build_breadcrumb(rel, lang, current_name)
        script = '<script type="application/ld+json">' + json.dumps(bc, ensure_ascii=False) + '</script>'
        text = head_insert(text, script)
        changed = True
        fixed.append((rel, 'breadcrumb json-ld'))

    # FAQ block detection
    faq_section = re.search(r'<section[^>]+id=["\']faq["\'][^>]*>.*?</section>', text, re.I|re.S)
    faq_existing = bool(faq_section)
    details = re.findall(r'<details>\s*<summary>(.*?)</summary>\s*<p>(.*?)</p>\s*</details>', text, re.I|re.S)
    if faq_existing and len(details) >= 5:
        faq_qas = [(re.sub('<[^<]+>', '', q).strip(), re.sub('<[^<]+>', '', a).strip()) for q, a in details[:5]]
    else:
        faq_qas = faq_items_for(rel, lang)
    if not faq_existing:
        faq_html = '\n<section id="faq" class="faq">\n  <h2>' + ('Питання та відповіді' if lang == 'uk' else 'Вопросы и ответы') + '</h2>\n'
        for q, a in faq_qas:
            faq_html += f'  <details><summary>{q}</summary><p>{a}</p></details>\n'
        faq_html += '</section>\n'
        if '</main>' in text:
            text = text.replace('</main>', faq_html + '\n</main>')
        else:
            text += faq_html
        changed = True
        fixed.append((rel, 'visible faq'))
    elif len(details) < 5:
        extra = faq_items_for(rel, lang)
        needed = 5 - len(details)
        more = extra[:needed]
        insert_html = ''.join(f'  <details><summary>{q}</summary><p>{a}</p></details>\n' for q, a in more)
        text = re.sub(r'(</section>\s*</main>)', insert_html + r'\1', text, flags=re.I|re.S)
        changed = True
        fixed.append((rel, 'visible faq extended'))

    # FAQ JSON-LD
    if 'FAQPage' not in text:
        faq_ld_items = []
        for q, a in faq_qas:
            faq_ld_items.append({'@type': 'Question', 'name': q, 'acceptedAnswer': {'@type': 'Answer', 'text': a}})
        faq_ld = {'@context': 'https://schema.org', '@type': 'FAQPage', 'mainEntity': faq_ld_items}
        script = '<script type="application/ld+json">' + json.dumps(faq_ld, ensure_ascii=False) + '</script>'
        text = head_insert(text, script)
        changed = True
        fixed.append((rel, 'faq json-ld'))

    # Internal links block if missing
    if '/raiony/' not in text and '/services' not in text and '/uslugi' not in text:
        links = build_internal_links(lang)
        links_html = '\n<section class="links">\n  <h2>' + ('Корисні посилання' if lang == 'uk' else 'Полезные ссылки') + '</h2>\n  <ul>\n'
        for href, label in links:
            links_html += f'    <li><a href="{href}">{label}</a></li>\n'
        links_html += '  </ul>\n</section>\n'
        if '</main>' in text:
            text = text.replace('</main>', links_html + '\n</main>')
        else:
            text += links_html
        changed = True
        fixed.append((rel, 'internal links'))

    if changed:
        path.write_text(text, encoding='utf-8')
        modified.append(rel)

report = {
    'before_counts': {k: len(v) for k, v in remaining.items()},
    'fixed_items': fixed,
    'modified_files': modified,
}
(report_path := root / 'fix_remaining_seo_report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding='utf-8')
print(json.dumps(report, ensure_ascii=False, indent=2))
