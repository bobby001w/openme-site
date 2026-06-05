import os
pages = {
    'ru/raiony/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Районы Киева — аварийное вскрытие и ремонт замков | OpenMe</title>
  <meta name="description" content="Районные страницы OpenMe на русском языке: вскрытие дверей, авто, сейфов и ремонт замков по районам Киева. Работа 24/7, выезд мастера.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Какие районы Киева вы обслуживаете?","acceptedAnswer":{"@type":"Answer","text":"Мы работаем по всем основным районам Киева: Оболонь, Позняки, Печерск, Троещина, Соломенский, Шевченковский, Голосеевский, Дарница, Деснянский, Подол, Святошинский, Днепровский."}},{"@type":"Question","name":"Можете ли вы выехать ночью?","acceptedAnswer":{"@type":"Answer","text":"Да, наша служба работает круглосуточно и выезжает ночью на срочные вызовы."}},{"@type":"Question","name":"Сколько стоит срочное вскрытие?","acceptedAnswer":{"@type":"Answer","text":"Цена зависит от услуги, типа замка и сложности. Мы называем ориентировочную сумму после описания проблемы и фото."}},{"@type":"Question","name":"Работаете ли вы с автомобилями и сейфами?","acceptedAnswer":{"@type":"Answer","text":"Да. Мы выполняем вскрытие авто, сейфов, гаражей и дверей по всей сети районов."}},{"@type":"Question","name":"Есть ли у вас гарантия на работу?","acceptedAnswer":{"@type":"Answer","text":"Да, мы предоставляем гарантию на выполненные работы и замененные замки."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы RU","item":"https://openme.com.ua/ru/raiony/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Районы Киева — аварийное вскрытие и ремонт замков</h1>
    <p>OpenMe предоставляет аварийные услуги по вскрытию дверей, автомобилей, сейфов и ремонту замков в ключевых районах Киева. Наши мастера работают быстро по всем зонам города и ориентируются на особенности подъездов, парковки и улиц.</p>
    <p>Страница районов помогает быстро выбрать нужный адрес и направление: от центрального Печерска и Подола до правого берега Позняков и областей левого берега, таких как Троещина и Днепровский.</p>
    <h2>Почему важен район</h2>
    <p>Каждый район Киева имеет свои особенности: плотная застройка, узкие улицы, охранные системы, разные типы входных дверей и подъездов. Вызов мастера должен учитывать все это, чтобы не задерживать работу и не создавать дополнительных сложностей.</p>
    <h2>Услуги по районам</h2>
    <ul>
      <li>вскрытие дверей в квартирах и домах</li>
      <li>вскрытие автомобилей</li>
      <li>вскрытие сейфов</li>
      <li>ремонт и замена замков</li>
      <li>вскрытие гаражей</li>
    </ul>
    <p>Мы выезжаем в районы с учетом загруженности дорог, поэтому в популярных зонах, таких как Оболонь, Позняки, Печерск, Троещина и Подол, стационарно поддерживаем готовность на вызов.</p>
    <h2>Когда нужен Master на районе</h2>
    <ul>
      <li>ключ потерян или остался внутри помещения</li>
      <li>замок заклинил или перестал работать</li>
      <li>ключ сломался в замке</li>
      <li>нужно срочно поменять механизм после утраты ключа</li>
      <li>необходимо открыть гараж, склад или сейф</li>
    </ul>
    <p>Мы помогаем клиентам найти оптимальное решение, если стандартные способы вскрытия не подходят из-за архитектурных особенностей района.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Вызвать мастера</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>Популярные районы</h2>
    <p>Мы обслуживаем перечисленные районы с высоким уровнем подготовки мастеров:</p>
    <ul>
      <li><a href="/ru/raiony/obolon/">Оболонь</a></li>
      <li><a href="/ru/raiony/poznyaki/">Позняки</a></li>
      <li><a href="/ru/raiony/pechersk/">Печерск</a></li>
      <li><a href="/ru/raiony/troeshchina/">Троещина</a></li>
      <li><a href="/ru/raiony/solomenskiy-raion/">Соломенский район</a></li>
      <li><a href="/ru/raiony/shevchenkovskiy-raion/">Шевченковский район</a></li>
      <li><a href="/ru/raiony/goloseevskiy-raion/">Голосеевский район</a></li>
      <li><a href="/ru/raiony/darnitskiy-raion/">Дарницкий район</a></li>
      <li><a href="/ru/raiony/desnyanskiy-raion/">Деснянский район</a></li>
      <li><a href="/ru/raiony/podolskiy-raion/">Подольский район</a></li>
      <li><a href="/ru/raiony/svyatoshinskiy-raion/">Святошинский район</a></li>
      <li><a href="/ru/raiony/dneprovskiy-raion/">Днепровский район</a></li>
    </ul>
    <h2>Часто задаваемые вопросы</h2>
    <details><summary>Какие районы обслуживаются быстрее всего?</summary><p>Быстрее всего мы обслуживаем районы с хорошей логистикой и большим количеством точек выезда, такие как Оболонь, Позняки и Печерск.</p></details>
    <details><summary>Как узнать, что вы едете в нужный район?</summary><p>Уточните район и ближайшую станцию метро, чтобы мастер мог быстрее добраться до вас.</p></details>
    <details><summary>Сколько стоит выезд?</summary><p>В большинстве случаев выезд входит в стоимость услуги, но точную цену лучше уточнить по телефону.</p></details>
    <details><summary>Можно ли написать в мессенджер?</summary><p>Да, мы принимаем заказы через Telegram и WhatsApp, это особенно удобно для отправки фото замка.</p></details>
    <details><summary>Как быстро приезжает мастер?</summary><p>Среднее время выезда по Киеву составляет 20—45 минут, в зависимости от района и дорожной ситуации.</p></details>
  </main>
</body>
</html>''',
    'ru/raiony/darnitskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок в Дарницком районе — выезд мастера 24/7 | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков на Дарнице: быстрый выезд мастера, ремонт и замена замков, открытие авто и сейфов. Работаем круглосуточно.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/darnitskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/darnitskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/darnytskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Можно ли открыть замок на Дарнице в любое время?","acceptedAnswer":{"@type":"Answer","text":"Да, наши мастера работают круглосуточно по всему Дарницкому району."}},{"@type":"Question","name":"Выезжаете ли вы в отдаленные районы Дарницы?","acceptedAnswer":{"@type":"Answer","text":"Да, мы обслуживаем как центральные, так и отдаленные части района, включая жилые массивы у набережной."}},{"@type":"Question","name":"Сколько стоит выезд?","acceptedAnswer":{"@type":"Answer","text":"Выезд обычно входит в стоимость услуги, подробности уточняются при заказе."}},{"@type":"Question","name":"Работаете ли вы с гаражными замками?","acceptedAnswer":{"@type":"Answer","text":"Да, вскрытие гаражей и подсобных помещений входит в перечень наших услуг."}},{"@type":"Question","name":"Можно ли оплатить картой?","acceptedAnswer":{"@type":"Answer","text":"Да, оплата картой или наличными возможна при выполнении работ."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Дарницкий район","item":"https://openme.com.ua/ru/raiony/darnitskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок в Дарницком районе</h1>
    <p>Дарница — крупный район на правом берегу Киева, который включает разнообразные жилые массивы, коммерческие зоны и набережную Днепра. Наши мастера знают, как быстро добраться до вызова в этом районе, учитывая пробки и особенности подъездов.</p>
    <p>Часто на Дарнице обращаются по вопросам аварийного вскрытия дверей, когда ключ потерян, замок заклинил или ключ сломался. Мы также открываем автомобили, сейфы и гаражи, предлагая полный спектр услуг по ремонту и замене замков.</p>
    <h2>Локальные ориентиры Дарницы</h2>
    <p>Работаем рядом со станциями метро «Дарница», «Левобережная», ТЦ «Караван», улицей Энтузиастов и жилыми кварталами вдоль Березняковской набережной.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>аварийное вскрытие дверей</li>
      <li>вскрытие автомобилей</li>
      <li>вскрытие сейфов</li>
      <li>вскрытие гаражей</li>
      <li>ремонт и замена замков</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>ключи потеряны или остались внутри квартиры</li>
      <li>замок заклинил и дверь не открывается</li>
      <li>ключ сломался внутри механизма</li>
      <li>нужно срочно поменять замок после утраты ключей</li>
      <li>не открывается гараж или сейф</li>
    </ul>
    <p>Мы понимаем, что на Дарнице бывают плотные жилые кварталы и узкие выезды, поэтому заранее уточняем подъезд и место встречи, чтобы не тратить лишнее время.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Дарницкий район</h2>
    <details><summary>Можно ли вызвать мастера вечером?</summary><p>Да, выезд доступен в любое время суток.</p></details>
    <details><summary>Как быстро вы приезжаете?</summary><p>В среднем 20—40 минут, в зависимости от ситуации на дороге.</p></details>
    <details><summary>Можно ли оплатить картой?</summary><p>Да, оплата картой и наличными возможна на месте.</p></details>
    <details><summary>Работаете ли вы в новостройках?</summary><p>Да, мы работаем как в старых домах, так и в новостройках Дарницы.</p></details>
    <details><summary>Даёте ли вы гарантию?</summary><p>Да, гарантия предоставляется на выполненные работы.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/poznyaki/">Позняки</a>, <a href="/ru/raiony/dneprovskiy-raion/">Днепровский</a>.</p>
  </main>
</body>
</html>''',
    'ru/raiony/desnyanskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок в Деснянском районе — помощь мастера | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков в Деснянском районе. Выезд мастера, ремонт и замена замков, открытие авто, гаражей и сейфов.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/desnyanskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/desnyanskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/desnianskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Можно ли открыть замок на Деснянском районе быстро?","acceptedAnswer":{"@type":"Answer","text":"Да, наши мастера приезжают оперативно и выполняют работу в разумные сроки."}},{"@type":"Question","name":"Работаете ли вы с автомобилями на левом берегу?","acceptedAnswer":{"@type":"Answer","text":"Да, мы оказываем услуги по вскрытию авто на левом берегу Киева."}},{"@type":"Question","name":"Можно ли оплатить картой?","acceptedAnswer":{"@type":"Answer","text":"Да, оплата картой или наличными возможна после выполнения работ."}},{"@type":"Question","name":"Сколько стоит выезд?","acceptedAnswer":{"@type":"Answer","text":"Выезд, как правило, входит в стоимость услуги, подробности уточняются при заказе."}},{"@type":"Question","name":"Есть ли гарантия?","acceptedAnswer":{"@type":"Answer","text":"Да, мы даем гарантию на выполненные работы, согласно условиям услуги."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Деснянский район","item":"https://openme.com.ua/ru/raiony/desnyanskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок в Деснянском районе</h1>
    <p>Деснянский район — крупный левобережный массив с многими жилыми кварталами, остановками и рынками. Мы работаем с вызовами по всей территории района, включая улицы с плотной многоэтажной застройкой.</p>
    <p>Наши мастера имеют опыт работы с типовыми квартирами и частными домами на Деснянском районе. Мы быстро реагируем на сигналы, когда замок заклинил или ключ сломался, и выполняем аккуратное вскрытие.</p>
    <h2>Локальные ориентиры</h2>
    <p>Работаем возле станции метро «Черниговская», «Левобережная», рынка «Троещина» и жилых массивов на улице Деснянской.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>вскрытие дверей</li>
      <li>вскрытие авто</li>
      <li>вскрытие сейфов</li>
      <li>вскрытие гаражей</li>
      <li>ремонт и замена замков</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>ключ потерян или оставлен внутри</li>
      <li>замок заклинил</li>
      <li>ключ сломался в замке</li>
      <li>нужно срочно поменять замок</li>
      <li>не открывается гараж или сейф</li>
    </ul>
    <p>Для удобства мы заранее согласовываем подъезд и место встречи, особенно если речь идет о плотной застройке или частных кварталах.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Деснянский район</h2>
    <details><summary>Работаете ли вы в частных домах?</summary><p>Да, мы выезжаем на частные дома и многоквартирные здания.</p></details>
    <details><summary>Можно ли получить цену по фото?</summary><p>Да, фото замка позволяют назвать ориентировочную стоимость.</p></details>
    <details><summary>Какой средний срок выезда?</summary><p>Обычно 25—45 минут, в зависимости от дорожной ситуации.</p></details>
    <details><summary>Можно ли оплатить картой?</summary><p>Да, картой или наличными.</p></details>
    <details><summary>Есть ли гарантия?</summary><p>Да, мы предоставляем гарантию на выполненные работы.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/troeshchina/">Троещина</a>, <a href="/ru/raiony/svyatoshinskiy-raion/">Святошинский</a>.</p>
  </main>
</body>
</html>''',
    'ru/raiony/dneprovskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок в Днепровском районе — выезд мастера 24/7 | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков в Днепровском районе, выезд мастера, открытие авто, сейфов и гаражей. Быстрая помощь по левому берегу.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/dneprovskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/dneprovskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/dniprovskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Работаете ли вы на левом берегу в районе Днепровский?","acceptedAnswer":{"@type":"Answer","text":"Да, выезжаем по всему Днепровскому району, включая набережную и жилые массивы."}},{"@type":"Question","name":"Можно ли открыть замок на доме у воды?","acceptedAnswer":{"@type":"Answer","text":"Да, мы работаем с объектами у набережной и в прилегающих районах."}},{"@type":"Question","name":"Сколько времени занимает выезд?","acceptedAnswer":{"@type":"Answer","text":"В среднем 20—40 минут, в зависимости от пробок и адреса."}},{"@type":"Question","name":"Можно ли открыть сейф?","acceptedAnswer":{"@type":"Answer","text":"Да, мы открываем механические и некоторые электронные сейфы по согласованию прав доступа."}},{"@type":"Question","name":"Можно ли оплатить картой?","acceptedAnswer":{"@type":"Answer","text":"Да, оплата картой или наличными доступна после выполнения работ."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Днепровский район","item":"https://openme.com.ua/ru/raiony/dneprovskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок в Днепровском районе</h1>
    <p>Днепровский район тянется вдоль реки и включает крупные жилые массивы, набережные и коммерческие зоны. Мы выезжаем на вызовы, где требуется быстрое аварийное вскрытие дверей, автомобилей и сейфов.</p>
    <p>Наши мастера учитывают особенности района: узкие улицы, плотная застройка и доступ к набережной. Поэтому мы заранее уточняем точный адрес и удобное место для встречи.</p>
    <h2>Локальные ориентиры</h2>
    <p>Работаем рядом со станциями метро «Левобережная», «Дарница», жилыми кварталами на улице Бучмы и районами у набережной Днепра.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>вскрытие дверей</li>
      <li>вскрытие авто</li>
      <li>вскрытие сейфов</li>
      <li>вскрытие гаражей</li>
      <li>ремонт и замена замков</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>ключ потерян или остался внутри</li>
      <li>замок не срабатывает</li>
      <li>ключ сломался</li>
      <li>нужно срочно заменить замок</li>
      <li>не открывается сейф или гараж</li>
    </ul>
    <p>Мы помогаем клиентам выбрать оптимальный способ вскрытия, который сохранит целостность двери и не ухудшит состояние замка.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Днепровский район</h2>
    <details><summary>Можно ли открыть дверь без повреждений?</summary><p>Да, мы работаем аккуратно и стараемся сохранить целостность дверного полотна.</p></details>
    <details><summary>Работаете ли вы ночью?</summary><p>Да, наши мастера работают круглосуточно.</p></details>
    <details><summary>Можно ли оплатить картой?</summary><p>Да, оплата картой возможна.</p></details>
    <details><summary>Работаете ли вы с сейфами?</summary><p>Да, открываем механические и некоторые электронные сейфы.</p></details>
    <details><summary>Есть ли гарантия?</summary><p>Да, на выполненные работы предоставляется гарантия.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/troeshchina/">Троещина</a>, <a href="/ru/raiony/darnitskiy-raion/">Дарница</a>.</p>
  </main>
</body>
</html>''',
    'ru/raiony/goloseevskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок в Голосеевском районе — выезд мастера | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков в Голосеевском районе. Работаем рядом с Голосеевским парком, ТРЦ, открытие дверей, авто и сейфов.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/goloseevskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/goloseevskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/holosiivskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Работаете ли вы в районе вокруг Голосеевского парка?","acceptedAnswer":{"@type":"Answer","text":"Да, мы обслуживаем весь Голосеевский район, включая жилые кварталы у парка."}},{"@type":"Question","name":"Можно ли открыть замок возле ТРЦ?","acceptedAnswer":{"@type":"Answer","text":"Да, мы выезжаем на вызовы к торговым центрам и жилым домам района."}},{"@type":"Question","name":"Работаете ли вы в офисных зданиях?","acceptedAnswer":{"@type":"Answer","text":"Да, открываем двери офисов, квартир и гаражей."}},{"@type":"Question","name":"Можно ли оценить стоимость заранее?","acceptedAnswer":{"@type":"Answer","text":"Да, отправьте фото замка — мы дадим ориентир по стоимости."}},{"@type":"Question","name":"Есть ли у вас гарантия?","acceptedAnswer":{"@type":"Answer","text":"Да, гарантия предоставляется на все выполненные работы."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Голосеевский район","item":"https://openme.com.ua/ru/raiony/goloseevskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок в Голосеевском районе</h1>
    <p>Голосеевский район сочетает зеленые зоны и современную застройку. Мы работаем как возле Голосеевского парка, так и в жилых кварталах Академгородка и Теремков.</p>
    <p>Наше аварийное вскрытие включает двери квартир и частных домов, автомобили, сейфы и гаражи. Мы прибываем на вызовы с учетом местных особенностей дорог и ограничений по парковке.</p>
    <h2>Локальные ориентиры</h2>
    <p>Работаем рядом с ТРЦ Ocean Plaza, Голосеевским парком, станциями метро «Голосеевская» и «Выдубичи», а также с жилыми кварталами на улице Академика Заболотного.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>вскрытие дверей</li>
      <li>вскрытие автомобилей</li>
      <li>вскрытие сейфов</li>
      <li>ремонт и замена замков</li>
      <li>вскрытие гаражей</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>ключ потерян или остался внутри</li>
      <li>замок заклинил</li>
      <li>ключ сломался в замке</li>
      <li>нужно срочно заменить замок</li>
      <li>не открывается сейф или гараж</li>
    </ul>
    <p>Мы понимаем, что район сочетает и жилые кварталы, и крупные объекты, поэтому мастер заранее уточняет точный адрес и условия подъезда.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Голосеевский район</h2>
    <details><summary>Можно ли обращаться ночью?</summary><p>Да, работаем круглосуточно.</p></details>
    <details><summary>Как быстро вы приезжаете?</summary><p>Обычно 20—40 минут, в зависимости от дорожной ситуации.</p></details>
    <details><summary>Можно ли получить цену по фото?</summary><p>Да, отправьте фото замка, и мы назовем ориентировочную стоимость.</p></details>
    <details><summary>Работаете ли вы со складскими дверьми?</summary><p>Да, раскрываем гаражи и складские помещения.</p></details>
    <details><summary>Есть ли гарантия?</summary><p>Да, предоставляется гарантия на выполненные работы.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/darnitskiy-raion/">Дарница</a>, <a href="/ru/raiony/solomenskiy-raion/">Соломенский</a>.</p>
  </main>
</body>
</html>''',
    'ru/raiony/podolskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок на Подоле — исторический центр Киева | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков на Подоле. Аккуратное обслуживание старых дверей, открытие авто, сейфов и ремонт замков. Работаем 24/7.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/podolskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/podolskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/podilskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Можно ли аккуратно вскрыть старые двери на Подоле?","acceptedAnswer":{"@type":"Answer","text":"Да, мы применяем методы, минимизирующие риск повреждения старинных дверей."}},{"@type":"Question","name":"Работаете ли вы рядом с Контрактовой площадью?","acceptedAnswer":{"@type":"Answer","text":"Да, наши мастера выезжают на Подол, включая исторические улицы и узкие подъезды."}},{"@type":"Question","name":"Можно ли оценить стоимость до приезда?","acceptedAnswer":{"@type":"Answer","text":"Да, по фото или описанию мы ориентировочно оцениваем стоимость работ."}},{"@type":"Question","name":"Открываете ли вы гаражи на Подоле?","acceptedAnswer":{"@type":"Answer","text":"Да, мы открываем гаражные, складские и подсобные помещения."}},{"@type":"Question","name":"Можно ли оплатить картой?","acceptedAnswer":{"@type":"Answer","text":"Да, картой и наличными, как вам удобно."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Подольский район","item":"https://openme.com.ua/ru/raiony/podolskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок на Подоле</h1>
    <p>Подол — это исторический район с узкими улицами, зданием старой ратуши и уникальной архитектурой. В таких условиях важно аккуратно вскрывать двери, чтобы не повредить старинные элементы и не усложнить ремонт.</p>
    <p>Мы оказываем услуги по аварийному вскрытию дверей, автомобилей, сейфов и гаражей. Наш мастер заранее уточняет маршрут и место для встречи, чтобы добраться до вызова без лишних задержек.</p>
    <h2>Локальные ориентиры</h2>
    <p>Работаем рядом с Контрактовой площадью, Андреевским спуском, Верхним Валами и Набережным шоссе. Эти точки помогают быстро находить адреса и выбирать оптимальный подъезд.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>вскрытие дверей</li>
      <li>вскрытие автомобилей</li>
      <li>вскрытие сейфов</li>
      <li>ремонт и замена замков</li>
      <li>вскрытие гаражей</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>если ключ потерян или остался внутри</li>
      <li>если замок заклинил</li>
      <li>если ключ сломался</li>
      <li>если нужно срочно заменить замок</li>
      <li>если не открывается сейф или гараж</li>
    </ul>
    <p>Особенно важен правильный подход в старых домах Подола, где каждая дверь может иметь индивидуальные особенности. Мы работаем бережно и профессионально.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Подольский район</h2>
    <details><summary>Можно ли открыть дверь без повреждений?</summary><p>Да, мы применяем аккуратные методы, сохраняя целостность дверного полотна и фурнитуры.</p></details>
    <details><summary>Работаете ли вы на Андреевском спуске?</summary><p>Да, мы обслуживаем исторические улицы и труднодоступные подъезды Подола.</p></details>
    <details><summary>Можно ли оплатить картой?</summary><p>Да, картой и наличными.</p></details>
    <details><summary>Потребуется ли подтверждение права доступа?</summary><p>В отдельных случаях мастер может попросить документ, подтверждающий право доступа, особенно при работе с сейфами.</p></details>
    <details><summary>Есть ли гарантия?</summary><p>Да, предоставляется гарантия на выполненные работы.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/shevchenkovskiy-raion/">Шевченковский</a>, <a href="/ru/raiony/pechersk/">Печерск</a>.</p>
  </main>
</body>
</html>''',
    'ru/raiony/shevchenkovskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок в Шевченковском районе — центр и исторические улицы | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков в Шевченковском районе. Аккуратная работа в центре, замена замков, открытие авто и сейфов.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/shevchenkovskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/shevchenkovskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/shevchenkivskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Можно ли вскрыть замок в центре без повреждений?","acceptedAnswer":{"@type":"Answer","text":"Да. Мы используем аккуратные методы, подходящие для центра и исторических зданий."}},{"@type":"Question","name":"Работаете ли вы на Андреевском спуске?","acceptedAnswer":{"@type":"Answer","text":"Да, мы выезжаем в исторические районы Шевченковского района, включая Андреевский спуск."}},{"@type":"Question","name":"Можно ли заменить замок сразу?","acceptedAnswer":{"@type":"Answer","text":"Да, замена замка возможна сразу при наличии нужной модели."}},{"@type":"Question","name":"Что делать, если замок не закрывается?","acceptedAnswer":{"@type":"Answer","text":"Лучше вызвать мастера, чтобы избежать дополнительных повреждений механизма."}},{"@type":"Question","name":"Есть ли у вас гарантия?","acceptedAnswer":{"@type":"Answer","text":"Да, мы даем гарантию на выполненные работы в зависимости от услуги."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Шевченковский район","item":"https://openme.com.ua/ru/raiony/shevchenkovskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок в Шевченковском районе</h1>
    <p>Шевченковский район — это динамичный центр с деловыми кварталами, университетами и историческими памятниками. Мы выполняем аккуратное вскрытие дверей, сохраняя эстетику зданий и снижая риск повреждений.</p>
    <p>Наши мастера работают в центральных частях города, на улице Сечевых Стрельцов, возле Андреевского спуска и в районах с высокой плотностью трафика. Мы быстро добираемся до вызова и подбираем метод вскрытия, подходящий для конкретной двери.</p>
    <h2>Локальные ориентиры</h2>
    <p>Работаем рядом с метро «Золотые Ворота», «Университет», «Театральная», улицей Сечевых Стрельцов и рядом с Национальным университетом.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>вскрытие дверей</li>
      <li>вскрытие автомобилей</li>
      <li>вскрытие сейфов</li>
      <li>ремонт и замена замков</li>
      <li>вскрытие гаражей</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>если ключ потерян или остался внутри</li>
      <li>если замок заклинил</li>
      <li>если ключ сломался</li>
      <li>если нужно срочно заменить замок</li>
      <li>если не открывается сейф или гараж</li>
    </ul>
    <p>В центральном районе важна скорость и точность: мы заранее уточняем подъезд и согласовываем внедрение, чтобы не тратить ничье время.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Шевченковский район</h2>
    <details><summary>Можно ли вызвать мастера для офиса?</summary><p>Да, мы обслуживаем жилые, офисные и коммерческие объекты.</p></details>
    <details><summary>Выдавливали ли вы замки в старинных дверях?</summary><p>Мы используем минимально инвазивные методы.</p></details>
    <details><summary>Можно ли оплатить картой?</summary><p>Да, картой или наличными.</p></details>
    <details><summary>Что делать, если ключ потерян?</summary><p>Лучше сразу вызвать мастера для безопасного открытия и настройки замка.</p></details>
    <details><summary>Можете ли вы открыть сейф?</summary><p>Да, открываем механические и некоторые электронные сейфы.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/pechersk/">Печерск</a>, <a href="/ru/raiony/podolskiy-raion/">Подольский</a>.</p>
  </main>
</body>
</html>''',
    'ru/raiony/solomenskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок в Соломенском районе — ремонт и замена замков | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков в Соломенском районе. Выезд мастера, ремонт замков, открытие авто и сейфов. Оперативная помощь 24/7.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/solomenskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/solomenskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/solomianskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Работаете ли вы в районе Соломенский?","acceptedAnswer":{"@type":"Answer","text":"Да, мы обслуживаем весь Соломенский район, включая район вокзала и промзоны."}},{"@type":"Question","name":"Сколько стоит аварийное вскрытие?","acceptedAnswer":{"@type":"Answer","text":"Ориентировочная стоимость зависит от типа замка. Фото до выезда помогают дать точную оценку."}},{"@type":"Question","name":"Можно ли открыть старую входную дверь?","acceptedAnswer":{"@type":"Answer","text":"Да, мы аккуратно вскрываем старые двери, сохраняя их внешний вид."}},{"@type":"Question","name":"Работаете ли вы с гаражными замками?","acceptedAnswer":{"@type":"Answer","text":"Да, при необходимости вскроем гараж или подсобное помещение."}},{"@type":"Question","name":"Можно ли оплатить картой?","acceptedAnswer":{"@type":"Answer","text":"Да, оплата картой и наличными возможна по договоренности."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Соломенский район","item":"https://openme.com.ua/ru/raiony/solomenskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок в Соломенском районе</h1>
    <p>Соломенский район охватывает важные транспортные артерии, станцию вокзала и жилые кварталы. Часто сюда вызывают мастера из-за сложных подъездов и ограниченной парковки.</p>
    <p>Мы выезжаем с инструментами, которые подходят как для квартир в жилых комплексах, так и для гаражей и офисных помещений. Работаем бережно с записями и защитными дверями.</p>
    <h2>Локальные ориентиры</h2>
    <p>Работаем рядом с железнодорожным вокзалом, метро «Вокзальная», улицей Антоновича, проспектом Победы и жилыми кварталами, прилегающими к музею авиации.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>вскрытие дверей</li>
      <li>вскрытие автомобилей</li>
      <li>вскрытие сейфов</li>
      <li>ремонт и замена замков</li>
      <li>вскрытие гаражей</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>ключ остался внутри квартиры</li>
      <li>замок заклинил</li>
      <li>ключ сломался при повороте</li>
      <li>необходимо срочно заменить замок</li>
      <li>дверь не открывается после аварийной ситуации</li>
    </ul>
    <p>Мы заранее согласовываем адрес и место встречи, чтобы обеспечить своевременный приезд даже в районе с интенсивным движением.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Соломенский район</h2>
    <details><summary>Что делать, если ключ сломался внутри?</summary><p>Не пытайтесь вытаскивать его самостоятельно. Это может повредить замок.</p></details>
    <details><summary>Работаете ли вы с дверями старого фонда?</summary><p>Да, используем щадящие методики для старых и современных дверей.</p></details>
    <details><summary>Можно ли вскрыть автомобиль без повреждений?</summary><p>В большинстве случаев да, мы применяем методы сохранения целостности авто.</p></details>
    <details><summary>Где лучше ждать мастера?</summary><p>Лучше встречать его у входа или на стоянке рядом с подъездом.</p></details>
    <details><summary>Нужна ли предварительная запись?</summary><p>Для срочных вызовов запись не обязательна — мы выезжаем по первому звонку.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/darnitskiy-raion/">Дарница</a>, <a href="/ru/raiony/holoseevskiy-raion/">Голосеевский</a>.</p>
  </main>
</body>
</html>''',
    'ru/raiony/shevchenkovskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок в Шевченковском районе — центр и исторические улицы | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков в Шевченковском районе. Аккуратная работа в центре, замена замков, открытие авто и сейфов.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/shevchenkovskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/shevchenkovskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/shevchenkivskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Можно ли вскрыть замок в центре без повреждений?","acceptedAnswer":{"@type":"Answer","text":"Да. Мы используем аккуратные методы, подходящие для центра и исторических зданий."}},{"@type":"Question","name":"Работаете ли вы на Андреевском спуске?","acceptedAnswer":{"@type":"Answer","text":"Да, мы выезжаем в исторические районы Шевченковского района, включая Андреевский спуск."}},{"@type":"Question","name":"Можно ли заменить замок сразу?","acceptedAnswer":{"@type":"Answer","text":"Да, замена замка возможна сразу при наличии нужной модели."}},{"@type":"Question","name":"Что делать, если замок не закрывается?","acceptedAnswer":{"@type":"Answer","text":"Лучше вызвать мастера, чтобы избежать дополнительных повреждений механизма."}},{"@type":"Question","name":"Есть ли у вас гарантия?","acceptedAnswer":{"@type":"Answer","text":"Да, мы даем гарантию на выполненные работы в зависимости от услуги."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Шевченковский район","item":"https://openme.com.ua/ru/raiony/shevchenkovskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок в Шевченковском районе</h1>
    <p>Шевченковский район — это центральный квартал Киева, где расположены университеты, офисные центры и культурные объекты. Мы предлагаем аккуратное вскрытие дверей и замков, учитывая исторический контекст и плотный трафик.</p>
    <p>Мастер быстро добирается до вызова на центральных улицах, заранее согласовав удобное место встречи. Это особенно важно, когда требуется оперативная помощь в центре города.</p>
    <h2>Локальные ориентиры</h2>
    <p>Работаем рядом с метро «Золотые Ворота», «Университет», «Театральная», улицей Сечевых Стрельцов и Андреевским спуском.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>вскрытие дверей</li>
      <li>вскрытие автомобилей</li>
      <li>вскрытие сейфов</li>
      <li>ремонт и замена замков</li>
      <li>вскрытие гаражей</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>ключ потерян или остался внутри</li>
      <li>замок заклинил</li>
      <li>ключ сломался в замке</li>
      <li>нужно срочно заменить замок</li>
      <li>не открывается сейф или гараж</li>
    </ul>
    <p>Мы ориентируемся на особенности центральных улиц, чтобы не создавать дополнительных проблем при подъезде и парковке.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Шевченковский район</h2>
    <details><summary>Можно ли вызвать мастера для офиса?</summary><p>Да, мы обслуживаем офисы, квартиры и коммерческие помещения.</p></details>
    <details><summary>Выдавали ли вы замки в старинных дверях?</summary><p>Да, применяем щадящие методы для старых дверей и фасадов.</p></details>
    <details><summary>Можно ли оплатить картой?</summary><p>Да, оплатить картой можно на месте.</p></details>
    <details><summary>Что делать, если ключ потерян?</summary><p>Лучше сразу вызвать мастера для безопасного открытия и замены замка.</p></details>
    <details><summary>Можете ли вы открыть сейф?</summary><p>Да, открываем механические и электронные сейфы.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/pechersk/">Печерск</a>, <a href="/ru/raiony/podolskiy-raion/">Подольский</a>.</p>
  </main>
</body>
</html>''',
    'ru/raiony/solomenskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок в Соломенском районе — ремонт и замена замков | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков в Соломенском районе. Выезд мастера, ремонт замков, открытие авто и сейфов. Оперативная помощь 24/7.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/solomenskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/solomenskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/solomianskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Работаете ли вы в районе Соломенский?","acceptedAnswer":{"@type":"Answer","text":"Да, мы обслуживаем весь Соломенский район, включая район вокзала и промзоны."}},{"@type":"Question","name":"Сколько стоит аварийное вскрытие?","acceptedAnswer":{"@type":"Answer","text":"Ориентировочная стоимость зависит от типа замка. Фото до выезда помогают дать точную оценку."}},{"@type":"Question","name":"Можно ли открыть старую входную дверь?","acceptedAnswer":{"@type":"Answer","text":"Да, мы аккуратно вскрываем старые двери, сохраняя их внешний вид."}},{"@type":"Question","name":"Работаете ли вы с гаражными замками?","acceptedAnswer":{"@type":"Answer","text":"Да, при необходимости вскроем гараж или подсобное помещение."}},{"@type":"Question","name":"Можно ли оплатить картой?","acceptedAnswer":{"@type":"Answer","text":"Да, оплата картой и наличными возможна по договоренности."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Соломенский район","item":"https://openme.com.ua/ru/raiony/solomenskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок в Соломенском районе</h1>
    <p>Соломенский район охватывает важные транспортные артерии, железнодорожный вокзал и тысячи жилых домов. Часто сюда вызывают мастера из-за сложных подъездов и ограничений по парковке.</p>
    <p>Мы выезжаем с инструментами, которые подходят как для квартир в жилых комплексах, так и для гаражей и офисных помещений. Работаем бережно с дверями и замками, минимизируя риск повреждений.</p>
    <h2>Локальные ориентиры</h2>
    <p>Обслуживаем район возле железнодорожного вокзала, метро «Вокзальная», улицы Антоновича, проспекта Победы и жилых кварталов, прилегающих к музею авиации.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>вскрытие дверей</li>
      <li>вскрытие автомобилей</li>
      <li>вскрытие сейфов</li>
      <li>ремонт и замена замков</li>
      <li>вскрытие гаражей</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>ключ остался внутри квартиры</li>
      <li>замок заклинил</li>
      <li>ключ сломался при повороте</li>
      <li>необходимо срочно заменить замок</li>
      <li>дверь не открывается после аварии</li>
    </ul>
    <p>Мы заранее согласовываем адрес и место встречи, чтобы обеспечить своевременный приезд даже в районе с интенсивным трафиком.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Соломенский район</h2>
    <details><summary>Что делать, если ключ сломался внутри?</summary><p>Не пытайтесь вытаскивать его самостоятельно. Это может повредить замок.</p></details>
    <details><summary>Работаете ли вы с дверями старого фонда?</summary><p>Да, используем щадящие методики для старых и современных дверей.</p></details>
    <details><summary>Можно ли вскрыть автомобиль без повреждений?</summary><p>В большинстве случаев да, мы применяем методы, сохраняющие целостность авто.</p></details>
    <details><summary>Где лучше ждать мастера?</summary><p>Лучше встречать его у входа или на стоянке рядом с подъездом.</p></details>
    <details><summary>Нужна ли предварительная запись?</summary><p>Для срочных вызовов запись не обязательна — мы выезжаем по первому звонку.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/darnitskiy-raion/">Дарница</a>, <a href="/ru/raiony/goloseevskiy-raion/">Голосеевский</a>.</p>
  </main>
</body>
</html>''',
    'ru/raiony/svyatoshinskiy-raion/index.html': '''<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <title>Вскрыть замок в Святошинском районе — выезд мастера | OpenMe</title>
  <meta name="description" content="Аварийное вскрытие замков в Святошинском районе. Выезд мастера, ремонт, замена замков, открытие авто и сейфов.">
  <link rel="canonical" href="https://openme.com.ua/ru/raiony/svyatoshinskiy-raion/">
  <link rel="alternate" href="https://openme.com.ua/ru/raiony/svyatoshinskiy-raion/" hreflang="ru">
  <link rel="alternate" href="https://openme.com.ua/raiony/sviatoshynskyi-raion/" hreflang="uk">
  <link rel="stylesheet" href="/styles.css">
  <script src="/config.js"></script>
  <script src="/app.js" defer></script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[{"@type":"Question","name":"Работаете ли вы по всему Святошинскому району?","acceptedAnswer":{"@type":"Answer","text":"Да, мы обслуживаем весь район, включая жилые массивы и пригородные улицы."}},{"@type":"Question","name":"Можно ли открыть замок ночью?","acceptedAnswer":{"@type":"Answer","text":"Да, наша служба работает круглосуточно."}},{"@type":"Question","name":"Возможно ли открыть авто без повреждений?","acceptedAnswer":{"@type":"Answer","text":"Да, при правильном подходе мы сохраняем целостность замка и авто."}},{"@type":"Question","name":"Можно ли оценить проблему по фото?","acceptedAnswer":{"@type":"Answer","text":"Да, отправьте фото замка, и мы дадим предварительную оценку."}},{"@type":"Question","name":"Есть ли гарантия?","acceptedAnswer":{"@type":"Answer","text":"Да, на услуги предоставляется гарантия в зависимости от типа работы."}}]}
  </script>
  <script type="application/ld+json">
  {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"Главная","item":"https://openme.com.ua/"},{"@type":"ListItem","position":2,"name":"Районы","item":"https://openme.com.ua/raiony/"},{"@type":"ListItem","position":3,"name":"Святошинский район","item":"https://openme.com.ua/ru/raiony/svyatoshinskiy-raion/"}]}
  </script>
</head>
<body class="bg-dark">
  <main class="container">
    <h1>Вскрыть замок в Святошинском районе</h1>
    <p>Святошинский район — зеленый и спокойный район на западе Киева с пригородной застройкой. Мы выезжаем по всем микрорайонам района, обслуживая как новые жилые комплексы, так и частные дома.</p>
    <p>Мастера учитывают особенности местных улиц и частных заездов, поэтому выезд на Святошин требует точного указания адреса и согласования места встречи.</p>
    <h2>Локальные ориентиры</h2>
    <p>Работаем возле метро «Святошино», «Житомирская», парковой зоны и жилых кварталов вокруг станции.</p>
    <h2>Наши услуги</h2>
    <ul>
      <li>вскрытие дверей</li>
      <li>вскрытие авто</li>
      <li>вскрытие сейфов</li>
      <li>ремонт и замена замков</li>
      <li>вскрытие гаражей</li>
    </ul>
    <h2>Когда нужен мастер</h2>
    <ul>
      <li>ключ потерян или остался внутри</li>
      <li>замок заклинил</li>
      <li>ключ сломался</li>
      <li>нужно срочно заменить замок</li>
      <li>не открывается гараж или сейф</li>
    </ul>
    <p>Мы предлагаем быстрый выезд и аккуратную работу по всему району, чтобы не создавать лишних неудобств для жильцов и соседей.</p>
    <div class="cta-block" style="margin-top:18px">
      <a class="btn btn-primary" href="tel:{{PHONE}}">Позвонить мастеру</a>
      <a class="btn btn-ghost" href="{{TELEGRAM}}">Написать в Telegram</a>
      <a class="btn btn-ghost" href="{{WHATSAPP}}">Написать в WhatsApp</a>
    </div>
    <h2>FAQ — Святошинский район</h2>
    <details><summary>Можно ли вскрыть дверь без повреждений?</summary><p>Да, мы используем аккуратные методы.</p></details>
    <details><summary>Работаете ли вы ночью?</summary><p>Да, наша служба доступна круглосуточно.</p></details>
    <details><summary>Можно ли оплатить картой?</summary><p>Да, картой и наличными возможна оплата.</p></details>
    <details><summary>Как быстро вы приезжаете?</summary><p>Обычно 20—40 минут, в зависимости от дорожной ситуации.</p></details>
    <details><summary>Есть ли гарантия?</summary><p>Да, гарантия предоставляется на выполненные работы.</p></details>
    <p class="muted">Соседние районы: <a href="/ru/raiony/solomenskiy-raion/">Соломенский</a>, <a href="/ru/raiony/desnyanskiy-raion/">Деснянский</a>.</p>
  </main>
</body>
</html>'''
}
root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
for rel, content in pages.items():
    path = os.path.join(root, *rel.split('/'))
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)
print('updated', len(pages), 'RU low-word pages')
