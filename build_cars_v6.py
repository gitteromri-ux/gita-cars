#!/usr/bin/env python3
"""Build cars-data.js for v6 with new order and real cars.com galleries."""
import json, os

# Constants (per user spec)
USD = 2.93
SHIP = 2000
CUSTOMS_ILS = 2000
DISCOUNT = 3000  # USD
SERVICE_PCT = 0.05
VAT_PCT = 0.18

# Top 9 in order requested + 11 more from the spec
CARS = [
    # 1. Ford Bronco Raptor Certified (blue)
    {"id":"bronco-raptor-cert-blue","name":"Ford Bronco Raptor — Certified","nameHe":"פורד ברונקו Raptor — Certified","eyebrow":"V6 ביטורבו · 2024 · CPO","brand":"Ford","year":2024,"condition":"certified","fuel":"בנזין","engine":"3.0L Twin-Turbo V6","hp":418,"nm":590,"accel":5.5,"topSpeed":201,"transmission":"10A","drive":"4x4","mpg":"6.5 ק\"מ/ליטר","seats":5,"doors":4,"length":4811,"width":2189,"height":1925,"weight":2393,"dealerPrice":895000,"ourPrice":464434,"savingPct":48.1,"image":"images/gallery/bronco-raptor-cert-blue-1.jpg","tags":["FORD","CERTIFIED","OFF-ROAD"],"highlight":"ברונקו Raptor כחול מטאלי, Certified Pre-Owned מבית פורד"},
    # 2. Jeep Wrangler Unlimited Sport S
    {"id":"wrangler-sport-s","name":"Jeep Wrangler Unlimited Sport S","nameHe":"ג'יפ רנגלר אנלימיטד Sport S","eyebrow":"V6 · 2026 · 4x4","brand":"Jeep","year":2026,"condition":"new","fuel":"בנזין","engine":"3.6L V6 Pentastar","hp":285,"nm":353,"accel":7.6,"topSpeed":160,"transmission":"8A","drive":"4x4","mpg":"6.8 ק\"מ/ליטר","seats":5,"doors":4,"length":4882,"width":1894,"height":1839,"weight":1995,"dealerPrice":350000,"ourPrice":225867,"savingPct":35.5,"image":"images/gallery/wrangler-sport-s-1.jpg","tags":["JEEP","NEW","OFF-ROAD"],"highlight":"ג'יפ רנגלר חדש מהיצרן, 4 דלתות, מנוע V6"},
    # 3. BMW 228i Gran Coupe xDrive
    {"id":"bmw-228-gran-coupe","name":"BMW 228i Gran Coupé xDrive","nameHe":"במוו 228i Gran Coupé xDrive","eyebrow":"I4 ביטורבו · 2026 · קופה","brand":"BMW","year":2026,"condition":"new","fuel":"בנזין","engine":"2.0L Turbo I4","hp":241,"nm":400,"accel":6.0,"topSpeed":243,"transmission":"8A Steptronic","drive":"xDrive","mpg":"11.0 ק\"מ/ליטר","seats":5,"doors":4,"length":4546,"width":1800,"height":1418,"weight":1620,"dealerPrice":320000,"ourPrice":215000,"savingPct":32.8,"image":"images/gallery/bmw-228-gran-coupe-1.jpg","tags":["BMW","NEW","קופה"],"highlight":"BMW קופה ספורטיבית, מצורף xDrive, חדשה מהיצרן"},
    # 4. Mustang Convertible light blue
    {"id":"mustang-conv-light-blue","name":"Ford Mustang EcoBoost Convertible Premium","nameHe":"פורד מוסטנג קבריולה — תכלת","eyebrow":"I4 EcoBoost · 2026 · קבריולה","brand":"Ford","year":2026,"condition":"new","fuel":"בנזין","engine":"2.3L EcoBoost I4","hp":315,"nm":475,"accel":5.4,"topSpeed":250,"transmission":"10A","drive":"RWD","mpg":"9.4 ק\"מ/ליטר","seats":4,"doors":2,"length":4805,"width":1916,"height":1387,"weight":1740,"dealerPrice":390000,"ourPrice":250000,"savingPct":35.9,"image":"images/gallery/mustang-conv-light-blue-1.jpg","tags":["FORD","NEW","קבריולה"],"highlight":"מוסטנג קבריולה תכלת חולמני, ספורטיבי וחדש"},
    # 5. MINI Cooper 4-door pink
    {"id":"mini-cooper-4door-pink","name":"MINI Cooper S 4-door","nameHe":"מיני קופר S 4-דלתות — ורוד","eyebrow":"I4 Turbo · 2026 · 4 דלתות","brand":"MINI","year":2026,"condition":"new","fuel":"בנזין","engine":"2.0L Turbo I4","hp":201,"nm":300,"accel":6.6,"topSpeed":235,"transmission":"7DCT","drive":"FWD","mpg":"13.5 ק\"מ/ליטר","seats":5,"doors":4,"length":4036,"width":1727,"height":1432,"weight":1305,"dealerPrice":260000,"ourPrice":168830,"savingPct":35.1,"image":"images/gallery/mini-cooper-4door-pink-1.jpg","tags":["MINI","NEW","עירוני"],"highlight":"מיני 4 דלתות בצבע ורוד-פסטל מיוחד, סטייל קלאסי"},
    # 6. Land Cruiser 1958
    {"id":"landcruiser-1958","name":"Toyota Land Cruiser 1958","nameHe":"טויוטה לנד קרוזר 1958","eyebrow":"I4 Hybrid · 2026 · 4WD","brand":"Toyota","year":2026,"condition":"new","fuel":"היברידי","engine":"2.4L Turbo Hybrid I4","hp":326,"nm":630,"accel":7.5,"topSpeed":175,"transmission":"8A","drive":"4WD","mpg":"9.5 ק\"מ/ליטר","seats":5,"doors":5,"length":4925,"width":1980,"height":1925,"weight":2495,"dealerPrice":450000,"ourPrice":283250,"savingPct":37.1,"image":"images/gallery/landcruiser-1958-1.jpg","tags":["TOYOTA","NEW","4WD","היברידי"],"highlight":"לנד קרוזר 1958 — דגם משודרג שמבוקש מאוד בישראל"},
    # 7. GMC Yukon Denali 6.2
    {"id":"yukon-denali","name":"GMC Yukon Denali 6.2 4WD","nameHe":"GMC יוקון Denali 6.2","eyebrow":"V8 · 2026 · 7 מקומות","brand":"GMC","year":2026,"condition":"new","fuel":"בנזין","engine":"6.2L V8","hp":420,"nm":624,"accel":5.8,"topSpeed":180,"transmission":"10A","drive":"4WD","mpg":"5.5 ק\"מ/ליטר","seats":7,"doors":5,"length":5354,"width":2057,"height":1944,"weight":2724,"dealerPrice":750000,"ourPrice":439096,"savingPct":41.5,"image":"images/gallery/yukon-denali-1.jpg","tags":["GMC","NEW","V8","7 מקומות"],"highlight":"יוקון Denali — פאר אמריקאי 7 מקומות עם V8"},
    # 8. Cadillac Escalade Sport
    {"id":"escalade-sport","name":"Cadillac Escalade Sport V8 4WD","nameHe":"קדילק אסקלייד Sport V8","eyebrow":"V8 · 2026 · 7 מקומות","brand":"Cadillac","year":2026,"condition":"new","fuel":"בנזין","engine":"6.2L V8","hp":420,"nm":624,"accel":6.0,"topSpeed":180,"transmission":"10A","drive":"4WD","mpg":"5.0 ק\"מ/ליטר","seats":7,"doors":5,"length":5382,"width":2058,"height":1939,"weight":2812,"dealerPrice":1100000,"ourPrice":639314,"savingPct":41.9,"image":"images/gallery/escalade-sport-1.jpg","tags":["CADILLAC","NEW","V8","יוקרה"],"highlight":"אסקלייד Sport — סמל אמריקאי של פאר וגודל"},
    # 9. Wrangler Rubicon Certified
    {"id":"wrangler-rubicon-cert","name":"Jeep Wrangler Rubicon 4-door — Certified","nameHe":"ג'יפ רנגלר Rubicon — Certified","eyebrow":"V6 · 2024 · CPO","brand":"Jeep","year":2024,"condition":"certified","fuel":"בנזין","engine":"3.6L V6","hp":285,"nm":353,"accel":7.6,"topSpeed":160,"transmission":"8A","drive":"4x4","mpg":"6.5 ק\"מ/ליטר","seats":5,"doors":4,"length":4882,"width":1894,"height":1839,"weight":2050,"dealerPrice":408500,"ourPrice":225867,"savingPct":44.7,"image":"images/gallery/wrangler-rubicon-cert-1.jpg","tags":["JEEP","CERTIFIED","OFF-ROAD"],"highlight":"רנגלר Rubicon Certified — אגדה משופצת מהיצרן"},
    # 10+ remaining from spec (using existing images for now)
    {"id":"jeep-gc-summit","name":"Jeep Grand Cherokee Summit 4WD","nameHe":"ג'יפ גרנד צ'רוקי Summit","eyebrow":"V6 · 2026 · יוקרה","brand":"Jeep","year":2026,"condition":"new","fuel":"בנזין","engine":"3.6L V6","hp":293,"nm":353,"accel":7.5,"topSpeed":210,"transmission":"8A","drive":"4WD","mpg":"7.6 ק\"מ/ליטר","seats":5,"doors":5,"length":4914,"width":1979,"height":1799,"weight":2169,"dealerPrice":580000,"ourPrice":411994,"savingPct":29.0,"image":"images/car-jeep-gc-summit.jpg","tags":["JEEP","NEW","יוקרה"],"highlight":"גרנד צ'רוקי Summit — דגל היוקרה של ג'יפ"},
    {"id":"g63","name":"Mercedes-AMG G63","nameHe":"מרצדס-AMG G63","eyebrow":"V8 ביטורבו · 2026","brand":"Mercedes-AMG","year":2026,"condition":"new","fuel":"בנזין","engine":"4.0L Twin-Turbo V8","hp":577,"nm":850,"accel":4.5,"topSpeed":220,"transmission":"9G","drive":"4MATIC","mpg":"5.2 ק\"מ/ליטר","seats":5,"doors":5,"length":4866,"width":1985,"height":1969,"weight":2531,"dealerPrice":2100000,"ourPrice":1181274,"savingPct":43.7,"image":"images/car-mercedes-g63-amg.jpg","tags":["MERCEDES","NEW","V8","יוקרה"],"highlight":"AMG G63 — סמל הסטטוס האולטימטיבי"},
    {"id":"bronco-bigbend","name":"Ford Bronco Big Bend 4-door","nameHe":"פורד ברונקו Big Bend","eyebrow":"I4 EcoBoost · 2026","brand":"Ford","year":2026,"condition":"new","fuel":"בנזין","engine":"2.3L EcoBoost I4","hp":300,"nm":440,"accel":7.6,"topSpeed":180,"transmission":"10A","drive":"4x4","mpg":"7.5 ק\"מ/ליטר","seats":5,"doors":4,"length":4811,"width":1928,"height":1849,"weight":2073,"dealerPrice":420000,"ourPrice":279923,"savingPct":33.4,"image":"images/car-ford-bronco-bigbend.jpg","tags":["FORD","NEW","OFF-ROAD"],"highlight":"ברונקו Big Bend צבע Desert Sand — קלאסי ונחשק"},
    {"id":"mercedes-gle-450","name":"Mercedes-Benz GLE 450 4MATIC","nameHe":"מרצדס GLE 450 4MATIC","eyebrow":"I6 mild-hybrid · 2026","brand":"Mercedes-Benz","year":2026,"condition":"new","fuel":"בנזין","engine":"3.0L Turbo I6 + EQ Boost","hp":375,"nm":500,"accel":5.5,"topSpeed":250,"transmission":"9G","drive":"4MATIC","mpg":"8.5 ק\"מ/ליטר","seats":5,"doors":5,"length":4926,"width":2018,"height":1772,"weight":2185,"dealerPrice":700000,"ourPrice":463720,"savingPct":33.8,"image":"images/car-mercedes-gle-450.jpg","tags":["MERCEDES","NEW","יוקרה"],"highlight":"GLE 450 — SUV יוקרה גרמני קלאסי"},
    {"id":"jeep-gc-overland","name":"Jeep Grand Cherokee Overland 4WD","nameHe":"ג'יפ גרנד צ'רוקי Overland","eyebrow":"V6 · 2026","brand":"Jeep","year":2026,"condition":"new","fuel":"בנזין","engine":"3.6L V6","hp":293,"nm":353,"accel":7.5,"topSpeed":210,"transmission":"8A","drive":"4WD","mpg":"7.5 ק\"מ/ליטר","seats":5,"doors":5,"length":4914,"width":1979,"height":1799,"weight":2169,"dealerPrice":520000,"ourPrice":378178,"savingPct":27.3,"image":"images/car-jeep-gc-summit.jpg","tags":["JEEP","NEW"],"highlight":"גרנד צ'רוקי Overland — איזון יוקרה ושטח"},
    {"id":"mercedes-cla-250","name":"Mercedes-Benz CLA 250 Coupe","nameHe":"מרצדס CLA 250 Coupe","eyebrow":"I4 mild-hybrid · 2026","brand":"Mercedes-Benz","year":2026,"condition":"new","fuel":"היברידי","engine":"2.0L Turbo I4 + EQ","hp":221,"nm":350,"accel":6.3,"topSpeed":250,"transmission":"7G-DCT","drive":"FWD","mpg":"14.0 ק\"מ/ליטר","seats":5,"doors":4,"length":4688,"width":1830,"height":1439,"weight":1535,"dealerPrice":380000,"ourPrice":294952,"savingPct":22.4,"image":"images/car-mercedes-glb-cert.jpg","tags":["MERCEDES","NEW","קופה","היברידי"],"highlight":"CLA 250 — קופה גרמנית אלגנטית"},
    {"id":"bronco-outer-banks","name":"Ford Bronco Outer Banks 4-door","nameHe":"פורד ברונקו Outer Banks","eyebrow":"V6 · 2026","brand":"Ford","year":2026,"condition":"new","fuel":"בנזין","engine":"2.7L EcoBoost V6","hp":330,"nm":563,"accel":6.5,"topSpeed":180,"transmission":"10A","drive":"4x4","mpg":"6.8 ק\"מ/ליטר","seats":5,"doors":4,"length":4811,"width":1928,"height":1849,"weight":2200,"dealerPrice":540000,"ourPrice":361332,"savingPct":33.1,"image":"images/car-ford-bronco-bigbend.jpg","tags":["FORD","NEW","OFF-ROAD"],"highlight":"Bronco Outer Banks — מותרות בשטח"},
    {"id":"jeep-gc-limited","name":"Jeep Grand Cherokee Limited 4WD","nameHe":"ג'יפ גרנד צ'רוקי Limited","eyebrow":"V6 · 2026","brand":"Jeep","year":2026,"condition":"new","fuel":"בנזין","engine":"3.6L V6","hp":293,"nm":353,"accel":7.5,"topSpeed":210,"transmission":"8A","drive":"4WD","mpg":"7.5 ק\"מ/ליטר","seats":5,"doors":5,"length":4914,"width":1979,"height":1799,"weight":2150,"dealerPrice":450000,"ourPrice":326859,"savingPct":27.4,"image":"images/car-jeep-gc-altitude.jpg","tags":["JEEP","NEW"],"highlight":"גרנד צ'רוקי Limited — איזון מחיר-יוקרה"},
    {"id":"tesla-x","name":"Tesla Model X Long Range","nameHe":"טסלה Model X Long Range","eyebrow":"EV Dual Motor · 2026","brand":"Tesla","year":2026,"condition":"new","fuel":"חשמלי","engine":"Dual Motor AWD","hp":670,"nm":920,"accel":3.9,"topSpeed":250,"transmission":"חד-הילוכי","drive":"AWD","mpg":"564 ק\"מ טווח","seats":6,"doors":5,"length":5057,"width":2008,"height":1684,"weight":2509,"dealerPrice":600000,"ourPrice":350000,"savingPct":41.7,"image":"images/car-tesla-model-x.jpg","tags":["TESLA","NEW","EV"],"highlight":"Model X — מנוע חשמלי עם דלתות פלקון"},
    {"id":"jeep-compass","name":"Jeep Compass Limited 4WD","nameHe":"ג'יפ קומפאס Limited","eyebrow":"I4 · 2026","brand":"Jeep","year":2026,"condition":"new","fuel":"בנזין","engine":"2.4L I4","hp":175,"nm":230,"accel":9.5,"topSpeed":190,"transmission":"9A","drive":"4WD","mpg":"10.5 ק\"מ/ליטר","seats":5,"doors":5,"length":4404,"width":1819,"height":1644,"weight":1545,"dealerPrice":280000,"ourPrice":226694,"savingPct":19.0,"image":"images/car-jeep-wrangler.jpg","tags":["JEEP","NEW","קומפקטי"],"highlight":"קומפאס Limited — ג'יפ קומפקטי לכל יום"},
    {"id":"jeep-gladiator","name":"Jeep Gladiator Sport 4x4","nameHe":"ג'יפ Gladiator Sport","eyebrow":"V6 · 2026 · טנדר","brand":"Jeep","year":2026,"condition":"new","fuel":"בנזין","engine":"3.6L V6","hp":285,"nm":353,"accel":8.0,"topSpeed":160,"transmission":"8A","drive":"4x4","mpg":"6.0 ק\"מ/ליטר","seats":5,"doors":4,"length":5539,"width":1894,"height":1860,"weight":2100,"dealerPrice":430000,"ourPrice":264236,"savingPct":38.5,"image":"images/car-jeep-gladiator.jpg","tags":["JEEP","NEW","טנדר"],"highlight":"גלדיאטור Sport — טנדר אגדי בסגנון רנגלר"},
]

# Add gallery field per car using gallery images if available
import os
GAL_DIR = "/home/user/workspace/site-number-1/images/gallery"
for c in CARS:
    cid = c["id"]
    gallery = []
    for i in range(1, 9):
        p = f"images/gallery/{cid}-{i}.jpg"
        full = os.path.join("/home/user/workspace/site-number-1", p)
        if os.path.exists(full):
            gallery.append(p)
    if len(gallery) < 8:
        # fallback to repeat main image
        while len(gallery) < 8:
            gallery.append(c["image"])
    c["gallery"] = gallery

# Write JS file
js = "// AutoImports cars data v6 — built " + __import__('datetime').datetime.now().isoformat() + "\n"
js += f"const FX = {{ USD: {USD}, SHIP: {SHIP}, CUSTOMS_ILS: {CUSTOMS_ILS}, DISCOUNT: {DISCOUNT}, SERVICE_PCT: {SERVICE_PCT}, VAT_PCT: {VAT_PCT} }};\n\n"
js += "const CARS = [\n"
for c in CARS:
    js += "  " + json.dumps(c, ensure_ascii=False) + ",\n"
js += "];\n\n"
js += """// Stock board (top 9 in order — same as catalog top)
const STOCK_MODELS = CARS.slice(0, 9).map(c => ({
  id: c.id,
  symbol: (c.brand || '').toUpperCase().slice(0,4),
  name: c.nameHe,
  price: c.ourPrice,
  ours: c.ourPrice,
  dealer: c.dealerPrice,
  change: (c.dealerPrice - c.ourPrice),
  pct: c.savingPct || 0,
  savingPct: c.savingPct,
  image: c.image,
}));

if (typeof window !== 'undefined') { window.CARS = CARS; window.FX = FX; window.STOCK_MODELS = STOCK_MODELS; }
"""

with open("/home/user/workspace/site-number-1/js/cars-data.js", "w", encoding="utf-8") as f:
    f.write(js)

print(f"Wrote {len(CARS)} cars to cars-data.js")
print("Top 9 with real cars.com galleries:")
for c in CARS[:9]:
    g_count = len([x for x in c["gallery"] if "gallery/" in x])
    print(f"  - {c['nameHe']} ({c['id']}): {g_count}/8 real gallery images")
