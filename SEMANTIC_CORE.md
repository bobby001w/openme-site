# Semantic Core for OpenMe

This semantic core maps search queries to existing pages and recommends coverage for missing request types. It is focused on Kiev locksmith services in Ukrainian and Russian.

## Cluster overview

| Cluster | Description |
|---|---|
| main | Brand and top-level locksmith queries for Kyiv |
| doors | Emergency door opening and apartment entry services |
| car | Car opening and automotive lockout services |
| safe | Safe opening services |
| garage | Garage and gate opening services |
| repair | Lock repair, replacement, and cylinder replacement |
| districts | Local district-level queries for Kyiv neighborhoods |
| faq | Informational questions and troubleshooting queries |

## UA semantics

The Ukrainian part of the semantic core covers the following service groups:

- Main: аварійне відкриття замків, майстер по замках, відкрити замок без пошкоджень.
- Doors: аварійне відкриття дверей, відкриття квартири, ключі залишилися в квартирі.
- Car: відкриття авто, відкрити машину, ключі залишилися в машині.
- Safe: відкриття сейфів, забув код, сейф не відкривається.
- Garage: відкриття гаража, заклинив гаражний замок, відкриття навісного замка.
- Repair: ремонт замків, заміна замків, заміна серцевини замка.
- Districts: локальні запити для районів Києва.
- FAQ: інформаційні питання по замках, виклику майстра, часу приїзду.

## RU semantics

- Main: аварийное вскрытие замков, мастер по замкам, открыть замок без повреждений.
- Doors: аварийное вскрытие дверей, вскрытие квартиры, захлопнулась дверь.
- Car: вскрытие авто, открыть машину, ключи остались в машине.
- Safe: вскрытие сейфов, забыл код, сейф не открывается.
- Garage: вскрытие гаража, открыть навесной замок, мастер по гаражным замкам.
- Repair: ремонт замков, замена замков, замена личинки замка.
- Districts: запросы для районов Киева.
- FAQ: информационные вопросы по замкам, вызову мастера и времени выезда.

## District semantics

Each Kyiv district has a localized query group for locksmith services in that area. The district pages cover the following query patterns:

- open lock [district]
- door opening [district]
- emergency door opening [district]
- car opening [district]
- lock repair [district]
- lock replacement [district]
- locksmith [district]

## FAQ and informational semantics

These queries are best supported by FAQ sections on the home page and service pages, not by separate landing pages.

## Coverage and recommendations

Most core service queries are already covered by existing pages. The site now has dedicated pages for cylinder replacement and lock opening without damage in both Ukrainian and Russian; remaining recommendations focus on broken keys, keys left in cars, and jammed locks.

### Recommended future pages

- /zlamavsia-kliuch-u-zamku/ — for emergency queries about broken keys in the lock.
- /kluchi-zalyshylys-v-avto/ — for automotive lockout queries about keys left in the car.
- /zaklynyv-zamok/ — for troubleshooting and lock jam queries.
- /ru/slomalsya-klyuch-v-zamke/ — for broken key-in-lock queries in Russian.
- /ru/klyuchi-ostalis-v-avto/ — for keys-left-in-car queries in Russian.
- /ru/zaklinil-zamok/ — for jammed lock troubleshooting queries in Russian.