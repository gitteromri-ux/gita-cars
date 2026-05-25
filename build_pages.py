#!/usr/bin/env python3
"""Generate all inner pages for AutoImports v4 with consistent layout."""
import os, json

OUT = '/home/user/workspace/site-number-1'

# Shared HTML head + header
def page_shell(title, eyebrow, page_title, subtitle, body, has_dark_cta=True):
    cta = '''
<section class="page-cta">
  <h2>מוכן להתחיל?</h2>
  <p>אנחנו כאן 24/7 בוואטסאפ. תהליך מלא, שקוף, ומתחיל בפיקדון של ₪500 בלבד.</p>
  <div class="cta-btns">
    <a class="btn-wa" href="https://wa.me/972500000000" target="_blank">דבר איתנו בוואטסאפ ←</a>
    <a class="btn-out" href="index.html#catalog">לקטלוג המלא</a>
  </div>
</section>''' if has_dark_cta else ''
    return f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} · AutoImports</title>
<meta name="description" content="{subtitle}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Heebo:wght@100;200;300;400;500;600;700;800;900&family=Inter:wght@100;200;300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;0,800;0,900;1,400;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="css/style.css">
<link rel="stylesheet" href="css/pages.css">
</head>
<body>

<!-- HEADER -->
<header class="hero-nav" style="position:fixed;top:0;left:0;right:0;background:rgba(10,10,10,0.85);backdrop-filter:blur(20px);z-index:90;padding:18px 32px;">
  <div class="nav-row" style="max-width:1400px;margin:0 auto;display:flex;justify-content:space-between;align-items:center;">
    <div class="nav-cta-wrap"><a href="forms.html" class="nav-cta" style="background:#fff;color:#0a0a0a;padding:10px 22px;border-radius:100px;text-decoration:none;font-family:'Heebo';font-weight:500;font-size:14px;">התחל הזמנה</a> <a href="bot.html" class="nav-cta nav-cta-secondary" style="color:#fff;margin-right:12px;font-family:'Heebo';font-size:14px;text-decoration:none;">בוט עזרה</a></div>
    <nav class="nav-center" style="display:flex;gap:32px;align-items:center;">
      <a href="faq.html" style="color:rgba(255,255,255,0.85);text-decoration:none;font-family:'Heebo';font-size:14px;">שאלות</a>
      <a href="about.html" style="color:rgba(255,255,255,0.85);text-decoration:none;font-family:'Heebo';font-size:14px;">אודות</a>
      <a href="how.html" style="color:rgba(255,255,255,0.85);text-decoration:none;font-family:'Heebo';font-size:14px;">תהליך</a>
      <a href="reviews.html" style="color:rgba(255,255,255,0.85);text-decoration:none;font-family:'Heebo';font-size:14px;">ביקורות</a>
      <a href="why.html" style="color:rgba(255,255,255,0.85);text-decoration:none;font-family:'Heebo';font-size:14px;">השוואה</a>
      <a href="catalog.html" style="color:rgba(255,255,255,0.85);text-decoration:none;font-family:'Heebo';font-size:14px;">קטלוג</a>
      <a href="blog.html" style="color:rgba(255,255,255,0.85);text-decoration:none;font-family:'Heebo';font-size:14px;">בלוג</a>
    </nav>
    <a href="index.html" class="nav-logo" style="display:flex;align-items:center;gap:10px;text-decoration:none;color:#fff;font-family:'Heebo';font-weight:700;font-size:18px;">AutoImports <span style="background:#fff;color:#0a0a0a;width:32px;height:32px;border-radius:8px;display:flex;align-items:center;justify-content:center;font-size:14px;font-weight:700;">AI</span></a>
  </div>
</header>

<!-- PAGE HERO -->
<section class="page-hero">
  <a href="index.html" class="back-link">← חזור לדף הבית</a>
  <div class="page-eyebrow">{eyebrow}</div>
  <h1 class="page-title">{page_title}</h1>
  <p class="page-subtitle">{subtitle}</p>
</section>

{body}

{cta}

<!-- FOOTER -->
<footer style="background:#0a0a0a;color:#fff;padding:60px 32px;text-align:center;border-top:1px solid rgba(255,255,255,0.06);">
  <div style="max-width:1280px;margin:0 auto;">
    <div style="display:flex;justify-content:center;gap:24px;flex-wrap:wrap;margin-bottom:32px;">
      <a href="index.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">בית</a>
      <a href="catalog.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">קטלוג</a>
      <a href="how.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">תהליך</a>
      <a href="why.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">למה אנחנו</a>
      <a href="reviews.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">ביקורות</a>
      <a href="regulations.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">רגולציה</a>
      <a href="used-cars.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">משומשים</a>
      <a href="trust.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">אמון</a>
      <a href="terms.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">תקנון</a>
      <a href="about.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">אודות</a>
      <a href="forms.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">טפסים</a>
      <a href="faq.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">שאלות</a>
      <a href="blog.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">בלוג</a>
      <a href="bot.html" style="color:rgba(255,255,255,0.6);text-decoration:none;font-family:'Heebo';font-size:14px;">בוט עזרה</a>
    </div>
    <div style="font-family:'Heebo';font-size:13px;color:rgba(255,255,255,0.4);">© 2026 AutoImports.co.il · יבוא אישי מארה"ב · רישיון מס׳ 12345</div>
  </div>
</footer>

</body>
</html>
'''


# ===== PAGE BODIES =====

how_body = '''
<section class="page-section">
  <div class="video-wrap" onclick="alert('סרטון הסבר יוטמע בקרוב')">
    <img src="images/car-mercedes-g63-amg.jpg" alt="איך זה עובד">
    <div class="video-play"><div class="video-play-btn">▶</div></div>
  </div>
  <p style="text-align:center;margin-top:24px;font-family:'Heebo';font-size:15px;color:#888;">סרטון 2 דקות שמסביר את כל התהליך</p>
</section>

<section class="page-section dark">
  <div style="max-width:1280px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:80px;">
      <div class="page-eyebrow">15 שלבים</div>
      <h2 style="color:#fff;">מהבחירה ועד המפתחות</h2>
      <p style="color:rgba(255,255,255,0.7);max-width:600px;margin:0 auto;">שקיפות בכל שלב. אנחנו מלווים — אתה בשליטה.</p>
    </div>
    <div style="max-width:900px;margin:0 auto;">
''' + '\n'.join([f'''      <div class="info-step">
        <div class="step-num">{i+1:02d}</div>
        <div><h4>{title}</h4><p>{desc}</p></div>
      </div>''' for i, (title, desc) in enumerate([
        ('בחירת רכב', 'בוחרים דגם, רמת גימור, צבע ומפרט מדויק. מקבלים הערכת מחיר מיידית באתר.'),
        ('פתיחת מרכז שירות 24/7', 'מקבלים יועץ אישי שמלווה אותך לאורך כל הדרך — בוואטסאפ, בטלפון, ובאפליקציה.'),
        ('הזמנה ופיקדון', 'פיקדון של ₪500 בלבד ל-15 דקות. סכום סמלי שמאבטח את ההזמנה ומתחיל את התהליך.'),
        ('סריקת רכבים בארה"ב', '48-72 שעות של סריקה אצל סוחרים, מכרזים, ובמסגרות פרטיות. אנחנו מחפשים את הדיל הטוב ביותר.'),
        ('הצעת מחיר מחייבת', '72 שעות לקבלת הצעה מפורטת עם פירוט כל העלויות. ללא הפתעות.'),
        ('הסדר מימון (אופציה)', 'אם רוצים — מסדרים מימון מבנקים מובילים תוך 1-3 ימי עסקים.'),
        ('אישור סופי', 'אתה מאשר את הרכב והעסקה לפני שאנחנו רוכשים אותו בשמך.'),
        ('בדיקה מקצועית', 'שבוע של בדיקה מקצועית בארה"ב: PPI, Carfax, אחריות. שום רכב לא יוצא בלי אישור.'),
        ('שילוח ימי', '38 ימים בים, מנמל בארה"ב לחיפה. ביטוח מלא לכל המסע.'),
        ('ניירת ומסמכים', '5 ימים של טיפול בכל הנירת — שטר מטען, חשבונית, אישורי יצרן.'),
        ('שחרור מהמכס', '2-3 ימי עבודה. אנחנו מטפלים בכל המסמכים, התשלומים, וההליכים.'),
        ('בדיקת תקינה', '3-5 ימים של בדיקות תקינה ישראליות. כל מה שצריך כדי לקבל רישיון.'),
        ('רישוי', '2 ימים לקבלת לוחיות, רישיון רכב, וביטוח חובה.'),
        ('המפתחות בידיך 🎉', 'הרכב נמסר אליך נקי, בדוק, ועם כל המסמכים. עוטף בקרטון.'),
        ('ביטוח ושירות שוטף', 'ממשיכים ללוות גם אחרי המסירה — ביטוח, שירות, ותחזוקה.'),
    ])]) + '''
    </div>
  </div>
</section>
'''


why_body = '''
<section class="page-section">
  <div style="text-align:center;max-width:720px;margin:0 auto;">
    <p>במקום לשלם 100% מחיר מלא ליבואן רשמי, או להסתבך לבד עם יבוא אישי — אנחנו המודל החדש. מקצועיים, שקופים, וזולים משמעותית.</p>
  </div>
  <div class="compare-chart">
    <div class="cmp-head">פרמטר</div>
    <div class="cmp-head">יבוא אישי לבד</div>
    <div class="cmp-head us">AutoImports</div>
    <div class="cmp-head">יבואן רשמי</div>
''' + ''.join([f'''
    <div class="cmp-cell cmp-label">{label}</div>
    <div class="cmp-cell"><span class="{cls_a}">{val_a}</span></div>
    <div class="cmp-cell us"><span class="cmp-yes">{val_us}</span></div>
    <div class="cmp-cell"><span class="{cls_c}">{val_c}</span></div>
''' for label, val_a, cls_a, val_us, val_c, cls_c in [
    ('מחיר רכב מלא', 'משתנה', 'cmp-mid', 'הזול ביותר ✓', 'הגבוה ביותר ✗', 'cmp-no'),
    ('שקיפות בעלויות', 'תלוי בך', 'cmp-mid', 'מלאה ✓', 'נמוכה ✗', 'cmp-no'),
    ('ליווי אישי 24/7', 'אין ✗', 'cmp-no', 'יש ✓', 'מוגבל', 'cmp-mid'),
    ('בדיקת PPI + Carfax', 'תלוי בך', 'cmp-mid', 'כלול ✓', 'לא כלול ✗', 'cmp-no'),
    ('אחריות יצרן מקורית', 'אולי', 'cmp-mid', 'כן ✓', 'כן ✓', 'cmp-yes'),
    ('זמן תהליך', '3-6 חודשים', 'cmp-no', '~75 ימים ✓', '3-12 חודשים', 'cmp-no'),
    ('סיכון ביורוקרטי', 'גבוה ✗', 'cmp-no', 'אפס ✓', 'נמוך', 'cmp-yes'),
    ('פיקדון התחלתי', 'גבוה', 'cmp-no', '₪500 בלבד ✓', '10%-20% ✗', 'cmp-no'),
    ('שירות אחרי מסירה', 'אין ✗', 'cmp-no', 'מלא ✓', 'מלא ✓', 'cmp-yes'),
    ('חיסכון מצופה', '15%-30%', 'cmp-mid', '30%-60% ✓', '0%', 'cmp-no'),
]]) + '''
  </div>
</section>

<section class="page-section dark">
  <div style="max-width:1280px;margin:0 auto;text-align:center;">
    <div class="page-eyebrow">המודל החדש</div>
    <h2 style="color:#fff;">למה אנחנו פשוט יותר טובים</h2>
    <div class="grid-3" style="margin-top:60px;">
      <div class="pillar-card"><div class="pillar-num">01</div><h3>אפס סיכון</h3><p>פיקדון של ₪500 בלבד. אם משהו לא מתאים — מקבלים החזר מלא.</p></div>
      <div class="pillar-card"><div class="pillar-num">02</div><h3>חיסכון אמיתי</h3><p>30%-60% מתחת ליבואן רשמי. מבוסס על מאות עסקאות.</p></div>
      <div class="pillar-card"><div class="pillar-num">03</div><h3>שקיפות מלאה</h3><p>כל שלב מתועד. כל עלות מפורטת. אין הפתעות.</p></div>
    </div>
  </div>
</section>
'''


about_body = '''
<section class="page-section">
  <div class="grid-2">
    <div>
      <h2>על AutoImports</h2>
      <p>נוסדנו בישראל ב-2023 על ידי צוות יזמים שהאמינו שאפשר אחרת. מאסנו במחירים מנופחים של יבואנים רשמיים. מאסנו מהסיבוכים של יבוא אישי לבד.</p>
      <p>בנינו מודל חדש: אנחנו לוקחים על עצמנו את כל התהליך — מהבחירה בארה"ב ועד מסירת המפתחות בישראל. עם שקיפות מלאה, מחירים זולים, וליווי אישי.</p>
      <p>היום אנחנו מובילים בתחום, עם מאות עסקאות מאחורינו ולקוחות מרוצים בכל הארץ.</p>
    </div>
    <div>
      <img src="images/car-mercedes-g63-amg.jpg" alt="AutoImports" style="width:100%;border-radius:24px;">
    </div>
  </div>
</section>

<section class="page-section dark">
  <div style="max-width:1280px;margin:0 auto;text-align:center;">
    <div class="page-eyebrow">המספרים שלנו</div>
    <h2 style="color:#fff;">מאות עסקאות. אלפי שעות עבודה.</h2>
    <div class="grid-4" style="margin-top:60px;text-align:center;">
      <div><div style="font-family:'Playfair Display';font-size:72px;font-weight:300;color:#c9a96e;">500+</div><div style="font-family:'Heebo';color:rgba(255,255,255,0.6);">רכבים מיובאים</div></div>
      <div><div style="font-family:'Playfair Display';font-size:72px;font-weight:300;color:#c9a96e;">98%</div><div style="font-family:'Heebo';color:rgba(255,255,255,0.6);">לקוחות מרוצים</div></div>
      <div><div style="font-family:'Playfair Display';font-size:72px;font-weight:300;color:#c9a96e;">75</div><div style="font-family:'Heebo';color:rgba(255,255,255,0.6);">ימי תהליך ממוצע</div></div>
      <div><div style="font-family:'Playfair Display';font-size:72px;font-weight:300;color:#c9a96e;">₪M-46</div><div style="font-family:'Heebo';color:rgba(255,255,255,0.6);">חיסכון ללקוחות</div></div>
    </div>
  </div>
</section>

<section class="page-section">
  <div style="text-align:center;margin-bottom:60px;">
    <div class="page-eyebrow">הצוות</div>
    <h2>מי אנחנו</h2>
  </div>
  <div class="grid-3">
    <div class="pillar-card"><div class="pillar-num">CEO</div><h3>עמרי גיטר</h3><p>מנכ"ל ומייסד. רקע באוטומוטיב ויזמות. 12 שנה בתעשייה.</p></div>
    <div class="pillar-card"><div class="pillar-num">OPS</div><h3>צוות תפעול</h3><p>5 אנשי מפתח שמטפלים בכל לקוח — מהזמנה ועד מסירה.</p></div>
    <div class="pillar-card"><div class="pillar-num">US</div><h3>שותפים בארה"ב</h3><p>נציגים מקומיים ב-12 מדינות שסורקים את השוק 24/7.</p></div>
  </div>
</section>
'''


# FAQ data — multi-category
faq_data = [
    ('כללי', [
        ('מי אתם?', 'AutoImports — חברה ישראלית שמתמחה ביבוא אישי של רכבי יוקרה מארה"ב. נוסדה ב-2023. מובילה בשוק עם 500+ עסקאות.'),
        ('איך אתם זולים יותר?', 'אנחנו עוקפים את היבואן הרשמי שמוסיף 30%-50% למחיר. אנחנו קונים ישירות, יודעים לנהל מכרזים, ויש לנו שותפים מקומיים בארה"ב.'),
        ('האם זה חוקי?', 'כן, לחלוטין. יבוא אישי הוא תהליך חוקי ומוסדר במדינת ישראל. אנחנו עומדים בכל הדרישות של רשות המסים והרישוי.'),
    ]),
    ('תהליך', [
        ('כמה זמן לוקח כל התהליך?', 'בממוצע 75 ימים מיום ההזמנה ועד מסירת המפתחות. 38 ימים בים, השאר זה ביורוקרטיה.'),
        ('מה הפיקדון?', '₪500 בלבד. כן, אתה לא קורא לא נכון. סכום סמלי שמאבטח את ההזמנה.'),
        ('מה קורה אם הרכב לא מתאים בסוף?', 'מבטלים. אתה מקבל את הפיקדון בחזרה. עד הרגע שבו אתה מאשר את הצעת המחיר הסופית — אין התחייבות.'),
        ('מי מטפל בכל הנירת?', 'אנחנו. מסמכים, מכס, רישוי, תקינה — הכל אצלנו. אתה רק מקבל את המפתחות.'),
    ]),
    ('רכבים', [
        ('אילו רכבים אתם מביאים?', 'הכל כמעט. ההתמחות שלנו: Mercedes (G-Class, GLE, GLS, S-Class), BMW (X5, X7), Tesla (כל הדגמים), Ford (Mustang, Bronco, F-150), Lucid, Rivian, Cybertruck.'),
        ('האם אפשר להזמין דגם ספציפי?', 'בוודאי. תגיד לנו דגם, צבע, רמת גימור, ותוספות — נמצא אותו.'),
        ('חדש או משומש?', 'שניהם. רוב הלקוחות בוחרים חדש (0 ק"מ), אבל יש לנו גם רכבי 1-2 שנים עם 5,000-30,000 ק"מ.'),
    ]),
    ('עלויות', [
        ('מה כלול במחיר?', 'הכל. מחיר רכב, שילוח, מכס, מע"מ, רישוי, ביטוח לכל הדרך, ניירת — הכל. ללא הפתעות.'),
        ('האם יש עלויות נוספות אחרי המסירה?', 'לא מצידנו. ביטוח שוטף, דלק, תחזוקה — באחריותך.'),
        ('האם אפשר במימון?', 'כן. אנחנו מסדרים מימון מבנקים מובילים. 1-3 ימי עסקים.'),
    ]),
    ('אחריות', [
        ('יש אחריות יצרן?', 'כן, מקורית. 4 שנים על הרכב, 8 שנים על סוללה לחשמליים.'),
        ('מה אם משהו מתקלקל?', 'מטופל כמו כל רכב חדש מיבואן רשמי. מוסכים מורשים בארץ.'),
        ('PPI ו-Carfax?', 'כלולים. כל רכב עובר בדיקה מקצועית בארה"ב + Carfax history report.'),
    ]),
]

faq_body = '<section class="page-section faq-full" style="max-width:900px;">'
for cat, items in faq_data:
    faq_body += f'<div class="faq-cat-title">{cat}</div>'
    for q, a in items:
        faq_body += f'<details><summary>{q}</summary><div>{a}</div></details>'
faq_body += '</section>'


reviews_body = '''
<section class="page-section">
  <div class="grid-3">
''' + ''.join([f'''
    <div class="testi-card">
      <div class="testi-quote-icon">"</div>
      <div class="testi-stars">★★★★★</div>
      <p class="testi-body">{body}</p>
      <div class="testi-meta">
        <div class="testi-avatar">{name[0]}</div>
        <div><div class="testi-name">{name}</div><div class="testi-role">{role}</div></div>
      </div>
    </div>''' for name, role, body in [
    ('יעל כהן', 'תל אביב · Mercedes G63', 'חיסכון של מעל ₪900,000 על G63 חדש. כל התהליך היה שקוף. הצוות ליווה אותי 24/7. עוטף כשהמכונית הגיעה — באמת.'),
    ('דני לוי', 'חיפה · Tesla Cybertruck', 'הזמנתי Cybertruck. הגיע אחרי 78 ימים בדיוק כמו שהבטיחו. מחיר חצי מהדילר. שירות מעולה.'),
    ('רחל ברק', 'ירושלים · BMW X5', 'תהליך נקי, מקצועי, ויסודי. הבדיקות בארה"ב הצילו אותי מקנייה לא טובה. עזרו לי למצוא רכב יותר טוב במחיר זול יותר.'),
    ('מתן פרידמן', 'באר שבע · Lucid Air', 'הם הביאו לי Lucid Air לפני שזה היה בכלל בארץ. מקצועי, שקוף, ועם תמיכה אדירה. ממליץ בחום.'),
    ('שירה אזולאי', 'נתניה · Mustang GT', 'הזמנתי Mustang GT V8 לבעלי במתנה ליום הולדת. הפתעה מלאה — הם תיאמו את ההגעה במדויק. ₪180K פחות ממה שיבואן רשמי ביקש.'),
    ('עמית רוזן', 'הרצליה · Ford Bronco Raptor', 'הם מצאו לי Bronco Raptor 2025 במפרט שביקשתי בדיוק. ₪336K פחות. כל הניירת היתה מסודרת. המלצה חמה.'),
    ('נועה שטרן', 'גבעתיים · Mercedes GLE 450d', 'GLE 450d בדיזל. ₪465K במקום ₪800K אצל היבואן. ההפרש הזה זה דירת חדר בתל אביב. תודה לאוטו-אימפורטס!'),
    ('עידן ביטון', 'אשדוד · Tesla Model X', 'הליווי האישי היה מטורף. כל יום עדכון, כל שאלה — מענה מיידי. הרכב הגיע במצב מושלם. 0 ק"מ אמיתי.'),
    ('דנה אלון', 'ראשון לציון · Kia EV9', 'יבואן רשמי ביקש ₪510K. הם הביאו ב-₪297K. אותו רכב בדיוק. אחריות מלאה. מתי שתרצי לקנות — תפני אליהם.'),
]]) + '''
  </div>
</section>

<section class="page-section dark">
  <div style="max-width:900px;margin:0 auto;text-align:center;">
    <div class="page-eyebrow">דירוג ממוצע</div>
    <div style="font-family:'Playfair Display';font-size:120px;font-weight:300;color:#c9a96e;line-height:1;">4.9</div>
    <div style="color:#c9a96e;font-size:32px;">★★★★★</div>
    <p style="color:rgba(255,255,255,0.7);font-size:18px;margin-top:24px;">מבוסס על 247 ביקורות אמיתיות מלקוחות מרוצים</p>
  </div>
</section>
'''


regulations_body = '''
<section class="page-section dark">
  <div style="max-width:900px;margin:0 auto;">
    <div class="info-step"><div class="step-num">01</div><div><h4>מי רשאי לייבא רכב באופן אישי?</h4><p>כל אזרח ישראלי בגיר רשאי לייבא רכב חדש או משומש לשימוש אישי. אין צורך ברישיון יבואן.</p></div></div>
    <div class="info-step"><div class="step-num">02</div><div><h4>מה מותר לייבא?</h4><p>רכבים עד גיל 2 שנים מתאריך הייצור (משומשים), או חדשים לחלוטין. רוב הדגמים האירופאיים והאמריקאיים מותרים, אבל יש בדיקת התאמה לתקני בטיחות ופליטות.</p></div></div>
    <div class="info-step"><div class="step-num">03</div><div><h4>מסים ועלויות מדינה</h4><p>מע"מ 18% על מחיר ה-CIF (רכב + שילוח + ביטוח). מס קנייה משתנה לפי דגם — בין 30%-83% לרכבי דלק, 18%-35% לחשמליים. בדוק מראש ברשות המסים.</p></div></div>
    <div class="info-step"><div class="step-num">04</div><div><h4>תהליך רישום ותקינה</h4><p>הרכב חייב לעמוד בתקני בטיחות ישראליים (UN R-numbers). דורש בדיקה במכון הרישוי הטכני. אם הרכב לא עומד בתקן — נדרשת התאמה (חגורות, פנסים, הילוכים).</p></div></div>
    <div class="info-step"><div class="step-num">05</div><div><h4>מסמכים נדרשים</h4><p>שטר מטען (Bill of Lading), חשבונית מקור, אישור יבוא ממשרד התחבורה, אישור עמידה בתקנים, פוליסת ביטוח חובה, תעודת זהות ורישיון נהיגה.</p></div></div>
    <div class="info-step"><div class="step-num">06</div><div><h4>מגבלות מכירה</h4><p>רכב שיובא ביבוא אישי — לא ניתן למכור 24 חודשים מיום הרישום הראשון בישראל. אחרת חוזרים את הפטור.</p></div></div>
    <div class="info-step"><div class="step-num">07</div><div><h4>עזרה מקצועית</h4><p>אנחנו ב-AutoImports מטפלים בכל זה עבורך — מקבלים על עצמנו את כל הניירת, המכס, התקינה, הרישוי. אתה רק מקבל את המפתחות.</p></div></div>
  </div>
</section>
'''


trust_body = '''
<section class="page-section">
  <div class="grid-3">
    <div class="pillar-card"><div class="pillar-num">01</div><h3>רישיון רשמי</h3><p>אנחנו חברה רשומה ברשם החברות, מאושרת על ידי רשות המסים, ועם רישיון יבוא רכבים תקף.</p></div>
    <div class="pillar-card"><div class="pillar-num">02</div><h3>פיקדון נמוך</h3><p>₪500 בלבד. עד הרגע שבו אתה מאשר את הצעת המחיר — מקבל החזר מלא. אפס סיכון.</p></div>
    <div class="pillar-card"><div class="pillar-num">03</div><h3>חוזה ברור</h3><p>חוזה מפורט שמגדיר בדיוק מה מקבלים, מתי, ובאיזה מחיר. ללא אותיות קטנות.</p></div>
    <div class="pillar-card"><div class="pillar-num">04</div><h3>תיעוד מלא</h3><p>כל שלב מתועד באפליקציה. תמונות, מסמכים, מספרי VIN, חתימות. הכל זמין לך 24/7.</p></div>
    <div class="pillar-card"><div class="pillar-num">05</div><h3>ביטוח מלא</h3><p>הרכב מבוטח מהרגע שהוא יוצא מהדילר בארה"ב ועד שאתה מקבל אותו. ביטוח ימי + יבשתי.</p></div>
    <div class="pillar-card"><div class="pillar-num">06</div><h3>צוות מקצועי</h3><p>5 אנשי מפתח, נציגים ב-12 מדינות בארה"ב, ושירות לקוחות 24/7 בעברית.</p></div>
  </div>
</section>

<section class="page-section dark" style="text-align:center;">
  <div style="max-width:900px;margin:0 auto;">
    <div class="page-eyebrow">לקוחות מספרים</div>
    <h2 style="color:#fff;">98% מהלקוחות שלנו ממליצים</h2>
    <p style="color:rgba(255,255,255,0.7);font-size:18px;">בעקבות 247 ביקורות אמיתיות. דירוג ממוצע: 4.9/5</p>
  </div>
</section>
'''


used_cars_body = '''
<section class="page-section dark">
  <div style="max-width:900px;margin:0 auto;">
    <div class="info-step"><div class="step-num">01</div><div><h4>Carfax History Report</h4><p>דו"ח היסטוריה מלא של הרכב: כל הבעלים, תאונות, תיקונים, רישומי שירות, קריאות מד-מרחק. שקיפות 100%.</p></div></div>
    <div class="info-step"><div class="step-num">02</div><div><h4>PPI — Pre-Purchase Inspection</h4><p>בדיקה מקצועית של 200+ נקודות לפני הקנייה. מבצעת על ידי טכנאי מוסמך, עצמאי מהמוכר. דו"ח מפורט עם תמונות.</p></div></div>
    <div class="info-step"><div class="step-num">03</div><div><h4>אחריות יצרן מקורית</h4><p>רכבים בני 1-3 שנים עדיין במסגרת אחריות יצרן מקורית. מועברת אוטומטית בעת רכישה.</p></div></div>
    <div class="info-step"><div class="step-num">04</div><div><h4>אחריות הרחבה</h4><p>אופציה לרכוש אחריות הרחבה של עד 5 שנים נוספות. כיסוי מלא לכל מערכות הרכב.</p></div></div>
    <div class="info-step"><div class="step-num">05</div><div><h4>בדיקה ישראלית</h4><p>בנוסף ל-PPI בארה"ב, הרכב עובר בדיקה במכון רישוי בארץ. אישור מלא לפני קבלת לוחיות.</p></div></div>
    <div class="info-step"><div class="step-num">06</div><div><h4>חיסכון אמיתי</h4><p>רכב משומש בן שנה יכול לחסוך לך 40%-60% מהמחיר של חדש מיבואן. עם אחריות, היסטוריה ידועה, ומצב כמעט-חדש.</p></div></div>
  </div>
</section>

<section class="page-section">
  <div style="text-align:center;max-width:720px;margin:0 auto;">
    <h2>למה לקנות משומש דרכנו?</h2>
    <p>אנחנו הגוף היחיד בארץ שמשלב יבוא אישי עם בדיקה מקצועית של רכב משומש בארה"ב. שום סיכון, מקסימום חיסכון.</p>
  </div>
</section>
'''


bot_body = '''
<section class="page-section">
  <div class="bot-page-wrap">
    <div style="display:flex;align-items:center;gap:16px;margin-bottom:24px;">
      <div style="width:56px;height:56px;border-radius:50%;background:linear-gradient(135deg,#c9a96e,#b8965a);display:flex;align-items:center;justify-content:center;color:#0a0a0a;font-weight:700;font-size:20px;font-family:'Heebo';">AI</div>
      <div>
        <div style="font-family:'Heebo';font-weight:500;font-size:20px;color:#fff;">בוט עזרה חכם</div>
        <div style="font-family:'Heebo';font-size:14px;color:#c9a96e;">פעיל עכשיו · תגובה מיידית</div>
      </div>
    </div>
    <p style="color:rgba(255,255,255,0.8);font-family:'Heebo';font-size:16px;">היי, איך אוכל לעזור? בחר אחת מהשאלות הנפוצות, או פתח שיחה חדשה:</p>
    <div class="bot-suggestions">
      <button class="bot-suggest" onclick="botAsk(this)">מה המחיר של G63?</button>
      <button class="bot-suggest" onclick="botAsk(this)">כמה זמן לוקח?</button>
      <button class="bot-suggest" onclick="botAsk(this)">איך מתחילים?</button>
      <button class="bot-suggest" onclick="botAsk(this)">מה האחריות?</button>
      <button class="bot-suggest" onclick="botAsk(this)">רכבים חשמליים?</button>
      <button class="bot-suggest" onclick="botAsk(this)">מימון אפשרי?</button>
    </div>
    <div class="bot-conversation" id="bot-conv">
      <div class="bot-msg bot">שלום! 👋 אני הבוט החכם של AutoImports. בחר שאלה מלמעלה או כתוב לי.</div>
    </div>
    <div style="display:flex;gap:12px;margin-top:16px;">
      <input id="bot-input" type="text" placeholder="כתוב הודעה..." style="flex:1;padding:14px 18px;border:1px solid rgba(255,255,255,0.15);border-radius:100px;background:rgba(255,255,255,0.05);color:#fff;font-family:'Heebo';outline:none;">
      <button onclick="botSubmit()" style="background:#c9a96e;color:#0a0a0a;border:none;padding:14px 28px;border-radius:100px;font-family:'Heebo';font-weight:500;cursor:pointer;">שלח</button>
    </div>
  </div>
</section>

<script>
function botAsk(btn) {
  const q = btn.textContent;
  const conv = document.getElementById('bot-conv');
  conv.insertAdjacentHTML('beforeend', '<div class="bot-msg user">' + q + '</div>');
  setTimeout(() => {
    const answers = {
      'מה המחיר של G63?': 'Mercedes-AMG G63 2025 חדש - V8 4.0L, 577 כ"ס. אצלנו ₪1.18M, ביבואן רשמי ₪2.10M. חיסכון של ₪920K.',
      'כמה זמן לוקח?': 'בממוצע 75 ימים מההזמנה ועד מסירה. כולל 38 ימי שילוח ים.',
      'איך מתחילים?': 'מתחילים בפיקדון של ₪500 (סמלי). ממלאים טופס באתר, ותוך 72 שעות מקבלים הצעה מלאה.',
      'מה האחריות?': 'אחריות יצרן מקורית — 4 שנים על הרכב, 8 שנים על סוללה (חשמלי). מועברת אוטומטית.',
      'רכבים חשמליים?': 'יש לנו 6 דגמים: Tesla Cybertruck/Model X, Lucid Air, Kia EV9, Rivian R1S, Mercedes G580 EQ.',
      'מימון אפשרי?': 'כן, מסדרים מימון מבנקים מובילים תוך 1-3 ימי עסקים. אופציה ב-100% מהמחיר.'
    };
    conv.insertAdjacentHTML('beforeend', '<div class="bot-msg bot">' + (answers[q] || 'תודה על השאלה! נציג יחזור אליך תוך 2 דקות.') + '</div>');
    conv.scrollTop = conv.scrollHeight;
  }, 600);
}
function botSubmit() {
  const i = document.getElementById('bot-input');
  if (!i.value.trim()) return;
  const conv = document.getElementById('bot-conv');
  conv.insertAdjacentHTML('beforeend', '<div class="bot-msg user">' + i.value + '</div>');
  const q = i.value;
  i.value = '';
  setTimeout(() => {
    conv.insertAdjacentHTML('beforeend', '<div class="bot-msg bot">קיבלתי! נציג חוזר אליך תוך 2 דקות בוואטסאפ.</div>');
    conv.scrollTop = conv.scrollHeight;
  }, 600);
}
</script>
'''


# Blog posts data
blog_posts = [
    ('CELEBRATE', 'מסירת Mercedes G63 ה-100 שלנו', 'ציון דרך מיוחד עבורנו — מאה מכוניות G-Class יובאו על ידינו ללקוחות בישראל. תודה לכל הלקוחות שבחרו בנו.', 'images/car-mercedes-g63-amg.jpg', '12 באוקטובר 2025'),
    ('NEW MODEL', 'Lucid Air Pure הגיע לישראל', 'הגדלנו את הקטלוג שלנו עם Lucid Air Pure — הרכב החשמלי המתקדם בעולם. טווח 660 ק"מ.', 'images/car-lucid-air-pure.jpg', '5 באוקטובר 2025'),
    ('MILESTONE', '₪46M חיסכון מצטבר ללקוחות', 'מאז שהקמנו את החברה, חסכנו ללקוחות שלנו יותר מ-46 מיליון ש"ח. וזה רק ההתחלה.', 'images/car-tesla-cybertruck-awd.jpg', '28 בספטמבר 2025'),
    ('FEATURE', 'אפליקציית מעקב חדשה', 'השקנו אפליקציה שמאפשרת לך לעקוב אחרי הרכב שלך בכל שלב — מהדילר בארה"ב ועד הבית.', 'images/car-ford-bronco-raptor.jpg', '20 בספטמבר 2025'),
    ('GUIDE', 'מדריך: איך לבחור רכב יבוא נכון', 'מה כדאי לבדוק לפני שאתה מתחיל? כל הטיפים מהמומחים שלנו.', 'images/car-mustang-gt-v8.jpg', '15 בספטמבר 2025'),
    ('NEWS', 'שינויים ברגולציה הישראלית 2026', 'משרד התחבורה הכריז על הקלות חדשות ביבוא רכבים חשמליים. מה זה אומר עבורך?', 'images/car-kia-ev9.jpg', '10 בספטמבר 2025'),
]

blog_body = '<section class="page-section"><div class="blog-grid">'
for cat, title, excerpt, img, date in blog_posts:
    blog_body += f'''
    <article class="blog-card">
      <div class="blog-img"><img src="{img}" alt="{title}"></div>
      <div class="blog-body">
        <div class="blog-cat">{cat}</div>
        <div class="blog-title">{title}</div>
        <div class="blog-excerpt">{excerpt}</div>
        <div class="blog-meta">{date}</div>
      </div>
    </article>
    '''
blog_body += '</div></section>'


terms_body = '''
<section class="page-section" style="max-width:900px;">
  <div class="legal-section">
    <h3><span class="legal-num">1.</span>הגדרות</h3>
    <p>"החברה" — AutoImports.co.il, חברה רשומה בישראל. "הלקוח" — כל אדם שהזמין שירות באמצעות האתר. "הרכב" — הרכב שהוזמן בהזמנה. "התהליך" — תהליך יבוא הרכב מארה"ב לישראל.</p>
  </div>
  <div class="legal-section">
    <h3><span class="legal-num">2.</span>פיקדון והזמנה</h3>
    <p>הזמנת רכב מתחילה בפיקדון של ₪500 בלבד. הפיקדון יוחזר במלואו במידה והלקוח אינו מאשר את הצעת המחיר הסופית תוך 72 שעות מקבלתה.</p>
    <p>הזמנה הופכת לסופית רק עם אישור הצעת המחיר ותשלום מקדמה של 30% משווי הרכב.</p>
  </div>
  <div class="legal-section">
    <h3><span class="legal-num">3.</span>הצעת מחיר</h3>
    <p>הצעת המחיר תוצג לאחר 48-72 שעות סריקה. ההצעה תכלול: מחיר רכב, שילוח, מכס, מע"מ, רישוי, ביטוח, דמי שירות (5%), ומסי קנייה.</p>
    <p>ההצעה תהיה תקפה ל-7 ימים. לאחר מכן ייתכנו שינויי מחירים בשוק.</p>
  </div>
  <div class="legal-section">
    <h3><span class="legal-num">4.</span>זמני אספקה</h3>
    <p>זמן ממוצע: 60-90 ימים מיום אישור ההזמנה הסופית. החברה תעדכן את הלקוח על כל שלב בתהליך.</p>
    <p>החברה אינה אחראית לעיכובים שאינם בשליטתה (מכס, נמלים, שביתות, מזג אוויר וכו').</p>
  </div>
  <div class="legal-section">
    <h3><span class="legal-num">5.</span>בדיקת רכב</h3>
    <p>כל רכב עובר PPI מקצועית בארה"ב, Carfax history report, ובדיקה במכון רישוי בישראל. במידה והרכב לא עובר את הבדיקות — הלקוח רשאי לבטל ולקבל החזר מלא.</p>
  </div>
  <div class="legal-section">
    <h3><span class="legal-num">6.</span>אחריות</h3>
    <p>אחריות יצרן מקורית מועברת ללקוח עם המסירה. אחריות החברה מוגבלת לתהליך היבוא בלבד.</p>
    <p>במקרה של בעיה ברכב — החברה תסייע בקשר עם היצרן ובהפעלת האחריות, ללא תשלום נוסף.</p>
  </div>
  <div class="legal-section">
    <h3><span class="legal-num">7.</span>ביטול עסקה</h3>
    <p>הלקוח רשאי לבטל את העסקה עד אישור הצעת המחיר הסופית — החזר מלא.</p>
    <p>לאחר אישור — חיובים יעמדו על העלויות שנגרמו בפועל (סריקה, שירות, חוזים).</p>
  </div>
  <div class="legal-section">
    <h3><span class="legal-num">8.</span>פרטיות ונתונים</h3>
    <p>החברה תשמור על פרטיות הלקוח ולא תעביר את פרטיו לצדדים שלישיים, למעט הגורמים המעורבים בתהליך היבוא.</p>
  </div>
  <div class="legal-section">
    <h3><span class="legal-num">9.</span>מגבלות מכירה</h3>
    <p>על פי החוק הישראלי, רכב שיובא ביבוא אישי אינו ניתן למכירה במהלך 24 חודשים מיום הרישום הראשון בישראל. מכירה לפני כן — תחויב בהחזר פטור.</p>
  </div>
  <div class="legal-section">
    <h3><span class="legal-num">10.</span>שיפוט</h3>
    <p>סמכות השיפוט הבלעדית בכל סכסוך תהיה לבית המשפט המוסמך במחוז מרכז, ישראל. החוק הישראלי יחול על תקנון זה.</p>
  </div>
</section>
'''


forms_body = '''
<section class="page-section">
  <div class="form-block">
    <h2 style="text-align:center;margin-bottom:32px;font-size:36px;">התחל את התהליך</h2>
    <p style="text-align:center;color:#666;margin-bottom:32px;">מלא את הטופס — ניצור איתך קשר תוך 2 שעות עסקיות.</p>
    <form onsubmit="event.preventDefault();alert('תודה! יצרנו עמך קשר.');">
      <div class="form-row"><label>שם מלא *</label><input type="text" required placeholder="ישראל ישראלי"></div>
      <div class="form-row"><label>טלפון *</label><input type="tel" required placeholder="050-0000000"></div>
      <div class="form-row"><label>דוא"ל</label><input type="email" placeholder="you@example.com"></div>
      <div class="form-row"><label>איזה רכב מעניין אותך? *</label>
        <select required>
          <option value="">בחר דגם...</option>
          <option>Mercedes G63 AMG</option>
          <option>Mercedes G500 / G580 EQ</option>
          <option>Mercedes GLE / GLS</option>
          <option>BMW X5 / X7</option>
          <option>Tesla Cybertruck</option>
          <option>Tesla Model X / S</option>
          <option>Lucid Air</option>
          <option>Rivian R1S</option>
          <option>Ford Bronco / Raptor</option>
          <option>Ford F-150 Raptor</option>
          <option>Ford Mustang GT</option>
          <option>Chevy Tahoe / Traverse</option>
          <option>Kia EV9</option>
          <option>Jeep Wrangler</option>
          <option>אחר — נציין בהערות</option>
        </select>
      </div>
      <div class="form-row"><label>שנת ייצור מועדפת</label>
        <select><option>2025 חדש</option><option>2024 כמעט חדש</option><option>2023</option><option>2022</option><option>פתוח לכל שנה</option></select>
      </div>
      <div class="form-row"><label>תקציב (אופציונלי)</label>
        <select><option>פתוח</option><option>עד ₪300,000</option><option>₪300K-500K</option><option>₪500K-800K</option><option>₪800K-1.2M</option><option>₪1.2M+</option></select>
      </div>
      <div class="form-row"><label>הערות נוספות</label><textarea placeholder="צבע, רמת גימור, תוספות מיוחדות..."></textarea></div>
      <button type="submit" class="form-submit">שלח · נחזור אליך תוך 2 שעות</button>
    </form>
  </div>
</section>

<section class="page-section dark" style="text-align:center;">
  <div style="max-width:600px;margin:0 auto;">
    <div class="page-eyebrow">או דרכים נוספות</div>
    <h2 style="color:#fff;font-size:36px;">צור איתנו קשר ישירות</h2>
    <div style="display:flex;justify-content:center;gap:16px;margin-top:32px;flex-wrap:wrap;">
      <a href="https://wa.me/972500000000" target="_blank" style="background:#25D366;color:#fff;padding:18px 32px;border-radius:100px;text-decoration:none;font-family:'Heebo';">WhatsApp</a>
      <a href="tel:+972500000000" style="background:#c9a96e;color:#0a0a0a;padding:18px 32px;border-radius:100px;text-decoration:none;font-family:'Heebo';">050-000-0000</a>
      <a href="mailto:info@autoimports.co.il" style="background:transparent;color:#fff;border:1px solid rgba(255,255,255,0.3);padding:18px 32px;border-radius:100px;text-decoration:none;font-family:'Heebo';">דוא"ל</a>
    </div>
  </div>
</section>
'''


# Catalog full page — renders all 17 cars + filter pills + sort
catalog_body = '''
<section class="page-section">
  <div class="catalog-toolbar">
    <button class="filter-pill active" data-filter="all">הכל</button>
    <button class="filter-pill" data-filter="EV">חשמלי</button>
    <button class="filter-pill" data-filter="V8">V8</button>
    <button class="filter-pill" data-filter="DIESEL">דיזל</button>
    <button class="filter-pill" data-filter="PHEV">היברידי</button>
    <button class="filter-pill" data-filter="MERCEDES">Mercedes</button>
    <button class="filter-pill" data-filter="BMW">BMW</button>
    <button class="filter-pill" data-filter="TESLA">Tesla</button>
    <button class="filter-pill" data-filter="FORD">Ford</button>
    <select class="sort-select" id="sort-select">
      <option value="discount">סדר לפי: חיסכון גבוה</option>
      <option value="price-low">מחיר זול ↑</option>
      <option value="price-high">מחיר יקר ↓</option>
      <option value="hp">כוח סוס</option>
    </select>
  </div>
  <div class="catalog-grid" id="catalog-page-grid"></div>
</section>

<script src="js/cars-data.js"></script>
<script>
(function(){
  const fmt = (n) => '₪' + Math.round(n).toLocaleString('he-IL');
  let activeFilter = 'all';
  let activeSort = 'discount';

  function render() {
    let cars = window.CARS.slice();
    if (activeFilter !== 'all') {
      cars = cars.filter(c => c.eyebrow.toUpperCase().includes(activeFilter));
    }
    if (activeSort === 'discount') cars.sort((a,b) => (b.dealerPrice-b.ourPrice) - (a.dealerPrice-a.ourPrice));
    else if (activeSort === 'price-low') cars.sort((a,b) => a.ourPrice - b.ourPrice);
    else if (activeSort === 'price-high') cars.sort((a,b) => b.ourPrice - a.ourPrice);
    else if (activeSort === 'hp') cars.sort((a,b) => b.hp - a.hp);

    document.getElementById('catalog-page-grid').innerHTML = cars.map(c => {
      const saving = c.dealerPrice - c.ourPrice;
      const pct = Math.round((saving/c.dealerPrice)*100);
      const parts = c.eyebrow.split(' \u00b7 ');
      return `
        <article class="car-card" onclick="window.location='car.html?id=${c.id}'">
          <div class="car-img-wrap"><img src="${c.image}" alt="${c.nameHe}" loading="lazy"><span class="car-badge-discount">\u2212${pct}%</span></div>
          <div class="car-info">
            <div class="car-eyebrow-row"><span>${parts[0]||''}</span><span class="dot">\u00b7</span><span>${parts[1]||''}</span><span class="dot">\u00b7</span><span>${parts[2]||''}</span></div>
            <h3 class="car-name">${c.name}</h3>
            <div class="car-specs-row">
              <div class="car-spec"><div class="car-spec-val">${c.accel}s</div><div class="car-spec-label">0-100</div></div>
              <div class="car-spec"><div class="car-spec-val">${c.hp}</div><div class="car-spec-label">HP</div></div>
              <div class="car-spec"><div class="car-spec-val">${c.nm}</div><div class="car-spec-label">N\u00b7M</div></div>
            </div>
            <div class="car-price-section">
              <div><div class="car-price-our-label">המחיר שלנו</div><div class="car-price-our">${fmt(c.ourPrice)}</div><div class="car-price-old">${fmt(c.dealerPrice)}</div></div>
              <div style="text-align:left"><div class="car-price-our-label">חיסכון</div><div style="font-family:'Inter';font-weight:700;font-size:18px;color:#d62828">\u2212${Math.round(saving/1000)}K</div></div>
            </div>
            <button class="car-cta-build">צפה במפרט מלא \u2190</button>
          </div>
        </article>`;
    }).join('');
  }

  document.querySelectorAll('.filter-pill').forEach(p => p.addEventListener('click', () => {
    document.querySelectorAll('.filter-pill').forEach(x => x.classList.remove('active'));
    p.classList.add('active');
    activeFilter = p.dataset.filter;
    render();
  }));
  document.getElementById('sort-select').addEventListener('change', e => { activeSort = e.target.value; render(); });
  render();
})();
</script>
'''


# Car single page — loads ?id=xxx from query
car_body = '''
<section class="page-section" id="car-page-body">
  <div style="text-align:center;padding:80px 20px;">
    <div style="font-family:'Heebo';color:#888;">טוען רכב...</div>
  </div>
</section>

<script src="js/cars-data.js"></script>
<script>
(function(){
  const fmt = (n) => '\u20aa' + Math.round(n).toLocaleString('he-IL');
  const fmtShort = (n) => n >= 1000000 ? '\u20aa' + (n/1000000).toFixed(2) + 'M' : '\u20aa' + Math.round(n/1000) + 'K';
  const params = new URLSearchParams(window.location.search);
  const id = params.get('id') || 'g63';
  const c = window.CARS.find(x => x.id === id) || window.CARS[0];
  const saving = c.dealerPrice - c.ourPrice;
  const pct = Math.round((saving/c.dealerPrice)*100);

  const FX = window.FX;
  const usdBase = (c.ourPrice/2.93)*0.78;
  const shipping = FX.shippingUsd*FX.usdIls;
  const customs = FX.customsIls;
  const service = c.ourPrice*FX.servicePct;
  const vat = c.ourPrice*FX.vat/(1+FX.vat);

  document.title = c.name + ' \u00b7 AutoImports';
  document.getElementById('car-page-body').innerHTML = `
    <div style="display:grid;grid-template-columns:1fr 1fr;gap:60px;margin-bottom:60px;">
      <div>
        <div style="aspect-ratio:16/10;border-radius:24px;overflow:hidden;background:#f0eeea;margin-bottom:16px;">
          <img id="main-img" src="${c.gallery[0]}" alt="${c.nameHe}" style="width:100%;height:100%;object-fit:cover;">
        </div>
        <div style="display:flex;gap:8px;overflow-x:auto;">
          ${c.gallery.map((g,i) => `<button onclick="document.getElementById('main-img').src='${g}'" style="border:none;padding:0;width:120px;height:80px;border-radius:12px;overflow:hidden;cursor:pointer;background:none;"><img src="${g}" style="width:100%;height:100%;object-fit:cover;"></button>`).join('')}
        </div>
      </div>
      <div>
        <div style="font-family:'Inter';font-size:12px;letter-spacing:0.3em;color:#c9a96e;font-weight:500;margin-bottom:16px;">${c.eyebrow}</div>
        <h1 style="font-family:'Playfair Display';font-size:64px;font-weight:300;margin:0 0 16px;letter-spacing:-0.02em;">${c.name}</h1>
        <p style="font-family:'Heebo';color:#666;font-size:18px;margin-bottom:32px;">${c.nameHe}</p>
        <div style="display:grid;grid-template-columns:repeat(4,1fr);gap:16px;margin-bottom:32px;">
          <div style="text-align:center;padding:16px;background:#faf9f6;border-radius:16px;"><div style="font-family:'Playfair Display';font-size:32px;font-weight:300;">${c.accel}<small>s</small></div><div style="font-family:'Heebo';font-size:12px;color:#888;">0-100</div></div>
          <div style="text-align:center;padding:16px;background:#faf9f6;border-radius:16px;"><div style="font-family:'Playfair Display';font-size:32px;font-weight:300;">${c.hp}</div><div style="font-family:'Heebo';font-size:12px;color:#888;">HP</div></div>
          <div style="text-align:center;padding:16px;background:#faf9f6;border-radius:16px;"><div style="font-family:'Playfair Display';font-size:32px;font-weight:300;">${c.nm}</div><div style="font-family:'Heebo';font-size:12px;color:#888;">N\u00b7m</div></div>
          <div style="text-align:center;padding:16px;background:#faf9f6;border-radius:16px;"><div style="font-family:'Playfair Display';font-size:32px;font-weight:300;">${c.topSpeed}</div><div style="font-family:'Heebo';font-size:12px;color:#888;">קמ"ש</div></div>
        </div>
        <div style="background:linear-gradient(135deg,#0a0a0a 0%,#1f1f1f 100%);color:#fff;padding:32px;border-radius:24px;margin-bottom:24px;">
          <div style="font-family:'Inter';font-size:11px;letter-spacing:0.3em;color:#c9a96e;margin-bottom:8px;">המחיר שלנו \u00b7 הכל כלול</div>
          <div style="font-family:'Inter';font-size:56px;font-weight:700;line-height:1;">${fmt(c.ourPrice)}</div>
          <div style="font-family:'Heebo';font-size:14px;color:rgba(255,255,255,0.5);margin-top:8px;">יבואן רשמי: <s>${fmt(c.dealerPrice)}</s></div>
          <div style="display:inline-block;background:#d62828;color:#fff;padding:6px 14px;border-radius:100px;font-family:'Heebo';font-size:13px;margin-top:16px;">חיסכון ${fmtShort(saving)} (${pct}%)</div>
        </div>
        <a href="https://wa.me/972500000000?text=${encodeURIComponent('שלום, מעוניין ב-'+c.nameHe)}" target="_blank" style="display:block;background:#25D366;color:#fff;padding:18px;text-align:center;border-radius:100px;text-decoration:none;font-family:'Heebo';font-weight:500;margin-bottom:12px;">התחל תהליך בוואטסאפ \u2190</a>
        <a href="forms.html" style="display:block;background:#0a0a0a;color:#fff;padding:18px;text-align:center;border-radius:100px;text-decoration:none;font-family:'Heebo';font-weight:500;">בקש הצעת מחיר רשמית</a>
      </div>
    </div>

    <div style="display:grid;grid-template-columns:2fr 1fr;gap:60px;margin-top:80px;">
      <div>
        <h2 style="font-family:'Heebo';font-size:32px;font-weight:300;margin-bottom:32px;">מפרט טכני מלא</h2>
        <table style="width:100%;border-collapse:collapse;font-family:'Heebo';">
          ${[
            ['מנוע', c.engine],['הספק', c.hp+' כ"ס'],['מומנט', c.nm+' N\u00b7m'],
            ['תאוצה 0-100', c.accel+' שניות'],['מהירות שיא', c.topSpeed+' קמ"ש'],
            ['תיבת הילוכים', c.transmission],['מערכת הינע', c.drive],
            ['צריכה / טווח', c.mpg],['סוג דלק', c.fuel],['מושבים', c.seats],['דלתות', c.doors],
            ['אורך', c.length+' מ"מ'],['רוחב', c.width+' מ"מ'],['גובה', c.height+' מ"מ'],['משקל', c.weight+' ק"ג']
          ].map(([k,v]) => `<tr style="border-bottom:1px solid #f0eeea;"><td style="padding:14px 0;color:#888;font-size:15px;">${k}</td><td style="padding:14px 0;font-weight:500;text-align:left;">${v}</td></tr>`).join('')}
        </table>

        <h2 style="font-family:'Heebo';font-size:32px;font-weight:300;margin:60px 0 32px;">תוספות וציוד</h2>
        <ul style="list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:14px;font-family:'Heebo';">
          ${c.features.map(f => `<li style="padding:14px 18px;background:rgba(201,169,110,0.06);border-right:3px solid #c9a96e;border-radius:12px;font-size:15px;">${f}</li>`).join('')}
        </ul>

        <h2 style="font-family:'Heebo';font-size:32px;font-weight:300;margin:60px 0 32px;">היסטוריה ואחריות</h2>
        <p style="font-family:'Heebo';font-size:17px;line-height:1.8;color:#444;background:#faf9f6;padding:32px;border-radius:20px;">${c.history}</p>
      </div>
      <div>
        <div style="position:sticky;top:120px;background:#faf9f6;padding:32px;border-radius:24px;">
          <h3 style="font-family:'Heebo';font-size:20px;font-weight:500;margin:0 0 24px;">פירוט מחיר \u00b7 15 שלבים</h3>
          ${[
            ['מחיר רכב יבוא (FOB)', fmt(usdBase*2.93)],
            ['שילוח ימי ($2,000)', fmt(shipping)],
            ['מכס וביטוח', fmt(customs)],
            ['דמי שירות (5%)', fmt(service)],
            ['מע"מ (18%)', fmt(vat)],
            ['הנחת קבוצה (\u2212$3,000)', '\u2212'+fmt(FX.discountUsd*FX.usdIls)],
            ['פיקדון התחלתי', '\u20aa500']
          ].map(([k,v]) => `<div style="display:flex;justify-content:space-between;padding:12px 0;border-bottom:1px solid rgba(0,0,0,0.06);font-family:'Heebo';font-size:14px;"><span style="color:#666;">${k}</span><span style="font-weight:500;">${v}</span></div>`).join('')}
          <div style="display:flex;justify-content:space-between;padding:20px 0 0;font-family:'Heebo';font-size:18px;font-weight:700;color:#0a0a0a;"><span>סה"כ</span><span>${fmt(c.ourPrice)}</span></div>
        </div>
      </div>
    </div>
  `;
})();
</script>
'''


# ===== WRITE ALL PAGES =====
pages = [
    ('how.html', 'איך זה עובד', 'תהליך 15 שלבים', 'מהבחירה ועד המפתחות', 'שקיפות בכל שלב. אנחנו מלווים — אתה בשליטה. סרטון הסבר + מדריך מפורט.', how_body),
    ('why.html', 'למה אנחנו', 'יבוא אישי לבד · AUTOIMPORTS · יבואן רשמי', 'למה אצלנו', 'השוואה מלאה בין שלוש האופציות שלך לקנות רכב מארה"ב.', why_body),
    ('about.html', 'אודות', 'מי אנחנו', 'AutoImports', 'נוסדה ב-2023 בישראל. מובילים בתחום היבוא האישי עם מאות עסקאות וצוות מקצועי.', about_body),
    ('faq.html', 'שאלות נפוצות', 'FAQ', 'שאלות נפוצות', 'הכל מה שצריך לדעת על יבוא אישי דרכנו. אם לא מצאת תשובה — דבר איתנו בוואטסאפ.', faq_body),
    ('terms.html', 'תקנון', 'TERMS', 'תקנון השירות', 'תנאים והוראות לשימוש בשירותי AutoImports. נא קרא בעיון לפני הזמנה.', terms_body),
    ('catalog.html', 'קטלוג רכבים', '17 דגמים זמינים', 'קטלוג מלא', 'כל הרכבים שלנו במקום אחד. סנן לפי סוג מנוע, יצרן, או מחיר. לחץ על רכב לצפייה במפרט מלא.', catalog_body),
    ('car.html', 'פרטי רכב', 'CAR DETAIL', 'רכב מותאם', 'מפרט מלא, גלריה, פירוט מחיר 15 שלבים.', car_body, False),
    ('reviews.html', 'ביקורות', 'TESTIMONIALS', 'מה אומרים הלקוחות', '247 ביקורות, דירוג 4.9/5, ולקוחות מאושרים בכל הארץ.', reviews_body),
    ('regulations.html', 'רגולציה', 'CAR IMPORT REGULATIONS', 'רגולציית יבוא בישראל', 'כל מה שצריך לדעת על חוקי היבוא, מסים, ותקנים — מסביר על ידי המומחים שלנו.', regulations_body),
    ('trust.html', 'אמון', 'WHY TRUST US', 'למה אפשר לסמוך עלינו', '6 סיבות שעושות אותנו הבחירה הבטוחה ביותר ליבוא אישי בישראל.', trust_body),
    ('used-cars.html', 'רכבים משומשים', 'USED CARS', 'קניית רכב משומש בביטחון', 'Carfax, PPI, אחריות, ובדיקות ישראליות — כל מה שצריך לדעת על רכבים משומשים.', used_cars_body),
    ('bot.html', 'בוט עזרה', 'AI ASSISTANT', 'בוט עזרה חכם', 'תשובות מיידיות לכל שאלה — מחיר, תהליך, אחריות, מימון. שאל אותו!', bot_body),
    ('blog.html', 'בלוג', 'STORIES & UPDATES', 'בלוג AutoImports', 'מסירות, חידושים, מילסטונים, ומדריכים מהצוות שלנו.', blog_body),
    ('forms.html', 'טפסים', 'GET STARTED', 'התחל את התהליך', 'מלא טופס קצר ונחזור אליך תוך 2 שעות עסקיות עם הצעת מחיר מותאמת.', forms_body),
]

for p in pages:
    fname, title, eyebrow, page_title, subtitle, body = p[:6]
    has_cta = p[6] if len(p) > 6 else True
    out = page_shell(title, eyebrow, page_title, subtitle, body, has_dark_cta=has_cta)
    with open(os.path.join(OUT, fname), 'w', encoding='utf-8') as f:
        f.write(out)
    print(f'wrote {fname} ({len(out)} bytes)')

print('DONE')
