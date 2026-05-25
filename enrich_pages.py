#!/usr/bin/env python3
"""Inject deeper, substantive sections into inner pages.
Each page receives 2-3 additional rich content sections before page-cta.
"""
import re, os

ROOT = os.path.dirname(os.path.abspath(__file__))

# Content blocks per page (Hebrew RTL)
EXTRA = {
    "about.html": '''
<section class="page-section">
  <div style="max-width:1100px;margin:0 auto;">
    <div class="page-eyebrow">הסיפור שלנו</div>
    <h2>למה הקמנו את AutoImports</h2>
    <p style="font-size:18px;line-height:1.8;color:#333;margin:24px 0;">בעולם שבו רכב פרימיום בישראל עולה פי שלושה ממה שהוא עולה בארצות הברית, הבנו שיש פה משהו שבור — והוא לא יתוקן ע"י היבואנים. ייסדנו את AutoImports.co.il כדי שכל מי שחולם על רכב אמריקאי, גרמני או יפני נחשק, יוכל להחזיק בו במחיר שמכבד את כיסו ואת ההיגיון.</p>
    <p style="font-size:18px;line-height:1.8;color:#333;margin:24px 0;">אנחנו לא יבואנים, אנחנו לא דילרים — אנחנו <strong>שותפי הייבוא האישי שלך</strong>. אנחנו עובדים אך ורק עבורך, לוקחים על עצמנו את כל הסיכון הלוגיסטי, ומלווים אותך מהבחירה בארה"ב ועד מסירת המפתחות בחצר שלך.</p>
  </div>
</section>

<section class="page-section dark">
  <div style="max-width:1280px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:60px;">
      <div class="page-eyebrow">הערכים שלנו</div>
      <h2 style="color:#fff;">שקיפות, מקצועיות, אמון</h2>
    </div>
    <div class="grid-3">
      <div class="pillar-card"><div class="pillar-num">01</div><h3>שקיפות מלאה</h3><p>כל שקל בעסקה — אתה רואה. ספק רכב, ים, מכס, אגרות, שירות. אין הפתעות.</p></div>
      <div class="pillar-card"><div class="pillar-num">02</div><h3>מקצועיות</h3><p>כל רכב עובר בדיקה מקצועית בארה"ב לפני הזמנה. דו"ח Carfax/AutoCheck נשלח אליך.</p></div>
      <div class="pillar-card"><div class="pillar-num">03</div><h3>ליווי אישי</h3><p>אדם אחד מלווה אותך מהשלב הראשון. וואטסאפ, טלפון, פגישות — איך שנוח לך.</p></div>
    </div>
  </div>
</section>

<section class="page-section">
  <div style="max-width:1100px;margin:0 auto;">
    <div class="page-eyebrow">בארה"ב</div>
    <h2>הרשת הלוגיסטית שלנו</h2>
    <div class="grid-2" style="margin-top:40px;">
      <div>
        <h3 style="color:#0a0a0a;margin-bottom:16px;">12 מדינות. 60+ דילרים מאומתים.</h3>
        <p style="font-size:17px;line-height:1.7;color:#444;">השותפים שלנו בארה"ב סורקים את שוק הרכב האמריקאי 24/7. אנחנו מקבלים ראשונים גישה למלאי בלעדי בדילרים מובחרים, כולל רכבי Certified Pre-Owned של היצרן, ורכבים חדשים מהקופסה.</p>
      </div>
      <div>
        <h3 style="color:#0a0a0a;margin-bottom:16px;">מובילי ים. שיתופי פעולה מובילים.</h3>
        <p style="font-size:17px;line-height:1.7;color:#444;">משלוח באוניית RoRo (Roll-on/Roll-off) ייעודית מנמלי החוף המזרחי או טקסס. כיסוי ביטוחי מלא לאורך כל הדרך. גישה למידע סטאטוס בזמן אמת.</p>
      </div>
    </div>
  </div>
</section>
''',

    "how.html": '''
<section class="page-section">
  <div style="max-width:1100px;margin:0 auto;">
    <div class="page-eyebrow">התהליך לעומק</div>
    <h2>מה בעצם קורה מאחורי הקלעים</h2>
    <p style="font-size:18px;line-height:1.8;color:#333;margin:24px 0;">התהליך נמשך 60-90 ימים מהיום שאתה חותם ועד הרכב בחצר שלך. במהלך התקופה הזו אנחנו מבצעים יותר מ-40 פעולות שונות בארה"ב ובישראל — מבדיקת VIN ועד הוצאת רישיון.</p>
  </div>
</section>

<section class="page-section">
  <div style="max-width:1280px;margin:0 auto;">
    <h2 style="text-align:center;margin-bottom:60px;">החודש בארה"ב</h2>
    <div class="grid-3">
      <div class="pillar-card"><div class="pillar-num">01</div><h3>סריקת מלאי</h3><p>שותפינו סורקים 200+ דילרים. מסננים על פי מצב, צבע, מילאז', היסטוריה.</p></div>
      <div class="pillar-card"><div class="pillar-num">02</div><h3>בדיקת רכב</h3><p>בודק עצמאי בודק את הרכב — מנוע, גוף, ביצועים. דו"ח מלא נשלח אליך.</p></div>
      <div class="pillar-card"><div class="pillar-num">03</div><h3>רכישה</h3><p>סוגרים מחיר עם הדילר. רוכשים על שמך עם POA חתום מראש.</p></div>
      <div class="pillar-card"><div class="pillar-num">04</div><h3>הכנה למשלוח</h3><p>לוחיות זמניות, ביטוח, תיעוד US-DOT. הרכב יוצא לנמל בתוך 7-14 ימים.</p></div>
      <div class="pillar-card"><div class="pillar-num">05</div><h3>העמסה</h3><p>RoRo (Roll-on/Roll-off) באוניית נסיעות. הרכב מגיע בלי קונטיינר. בטיחות מקסימלית.</p></div>
      <div class="pillar-card"><div class="pillar-num">06</div><h3>מעקב</h3><p>קישור MarineTraffic אישי. אתה רואה את האונייה בכל רגע.</p></div>
    </div>
  </div>
</section>

<section class="page-section dark">
  <div style="max-width:1280px;margin:0 auto;">
    <h2 style="color:#fff;text-align:center;margin-bottom:60px;">החודש בישראל</h2>
    <div class="grid-3">
      <div class="pillar-card"><div class="pillar-num">07</div><h3>פריקה באשדוד</h3><p>הרכב יורד מהאונייה. המכס מתחיל הליך שחרור. עומסים יכולים להוסיף 3-7 ימים.</p></div>
      <div class="pillar-card"><div class="pillar-num">08</div><h3>שחרור מכסי</h3><p>שלם מע"מ, מס קנייה, מס חברה. הסכומים סוכמו מראש בהצעת המחיר.</p></div>
      <div class="pillar-card"><div class="pillar-num">09</div><h3>בדיקות מכון</h3><p>מכון רישוי מאומת בודק את הרכב. ההמרה לישראלי כוללת אורות, מד-מהירות, אגזוז.</p></div>
      <div class="pillar-card"><div class="pillar-num">10</div><h3>רישוי</h3><p>רישיון רכב ולוחיות זיהוי ישראליות. תהליך של 7-14 ימים.</p></div>
      <div class="pillar-card"><div class="pillar-num">11</div><h3>בדיקות סופיות</h3><p>צביעה (במידת הצורך), פוליש, התקנת אביזרים שביקשת. נקה ועיצוב.</p></div>
      <div class="pillar-card"><div class="pillar-num">12</div><h3>מסירה</h3><p>טקס מסירת מפתחות בחצר שלך. סקירה מקצועית, מפתחות, הדרכה, אחריות.</p></div>
    </div>
  </div>
</section>
''',

    "why.html": '''
<section class="page-section">
  <div style="max-width:1100px;margin:0 auto;">
    <div class="page-eyebrow">למה לא יבואן רשמי</div>
    <h2>הסיבה למחירים המנופחים בישראל</h2>
    <p style="font-size:18px;line-height:1.8;color:#333;">היבואן הרשמי מחזיק שטחי תצוגה, מחסנים, אולמות שירות, מאות עובדים — והכל יושב על מחיר הרכב שלך. בנוסף, היבואנים פועלים במונופול שמאפשר להעלות מחירים מעל המחיר ההגיוני. למה? כי אין תחרות אמיתית. עד היום.</p>
    <p style="font-size:18px;line-height:1.8;color:#333;margin-top:24px;">יבוא אישי דרכנו עוקף את כל המבנה הזה. אתה משלם את עלות הרכב האמיתית בארה"ב, פלוס לוגיסטיקה, מסים ושירות. סך הכל — בין 25%-45% פחות ממחיר היבואן.</p>
  </div>
</section>

<section class="page-section dark">
  <div style="max-width:1280px;margin:0 auto;">
    <div style="text-align:center;margin-bottom:60px;">
      <h2 style="color:#fff;">3 דרכים. מחיר אחד שמוביל.</h2>
    </div>
    <div class="grid-3">
      <div class="pillar-card"><div class="pillar-num" style="color:#ff6b6b;">A</div><h3>יבואן רשמי</h3><p>מחירים מנופחים, מלאי מוגבל, אין אופציה למפרט מותאם, אחריות מותנית בשירות הרשמי.</p><div style="margin-top:16px;color:#c9a96e;font-weight:600;">לא מומלץ לפרימיום</div></div>
      <div class="pillar-card"><div class="pillar-num" style="color:#f5a524;">B</div><h3>יבוא מקביל</h3><p>מחיר אמצע, אבל הסיכון על הצרכן. רכבים משומשים, מצב לא תמיד ברור, אחריות מצומצמת.</p><div style="margin-top:16px;color:#c9a96e;font-weight:600;">תלוי מי הספק</div></div>
      <div class="pillar-card"><div class="pillar-num" style="color:#10b981;">C</div><h3>אנחנו — יבוא אישי</h3><p>רכב חדש או Certified, על שמך, אחריות מקצועית, מחיר שקוף, ליווי מלא, בלי הפתעות.</p><div style="margin-top:16px;color:#10b981;font-weight:600;">המודל החדש</div></div>
    </div>
  </div>
</section>

<section class="page-section">
  <div style="max-width:1100px;margin:0 auto;">
    <h2 style="text-align:center;">המספרים מדברים</h2>
    <div class="grid-3" style="margin-top:48px;">
      <div style="text-align:center;"><div style="font-family:Playfair Display;font-size:72px;color:#0a0a0a;">35%</div><div style="color:#666;">חיסכון ממוצע מול יבואן</div></div>
      <div style="text-align:center;"><div style="font-family:Playfair Display;font-size:72px;color:#0a0a0a;">75</div><div style="color:#666;">ימים — תהליך ממוצע</div></div>
      <div style="text-align:center;"><div style="font-family:Playfair Display;font-size:72px;color:#0a0a0a;">₪500</div><div style="color:#666;">פיקדון בלבד לפתיחה</div></div>
    </div>
  </div>
</section>
''',

    "faq.html": '''
<section class="page-section">
  <div style="max-width:920px;margin:0 auto;">
    <div class="faq-item"><h3>כמה זמן לוקח התהליך?</h3><p>בין 60 ל-90 ימים מהיום שאתה חותם על הזמנה ועד מסירת המפתחות. תהליך הים לוקח 30-45 ימים, תהליך השחרור והרישוי בישראל לוקח 25-40 ימים נוספים.</p></div>
    <div class="faq-item"><h3>כמה חיסכון אפשרי באמת?</h3><p>בין 25% ל-45% מהמחיר הרשמי של היבואן. ככל שהרכב יקר יותר, החיסכון בש"ח גדל. דוגמאות: Mercedes G63 — כ-₪900K חיסכון; BMW X5 — כ-₪215K; Mustang Convertible — כ-₪137K.</p></div>
    <div class="faq-item"><h3>אילו רכבים אתם מייבאים?</h3><p>אנחנו מתעסקים רק עם רכבים חדשים מהיצרן, או רכבים בסטטוס Certified Pre-Owned משנת הרישום הקודמת, עם פחות מ-25,000 מייל. בלי משומשים רגילים, בלי תאונות.</p></div>
    <div class="faq-item"><h3>מה זה Certified Pre-Owned (CPO)?</h3><p>זוהי קטגוריה רשמית של היצרנים (Ford, Mercedes, Jeep, BMW...) — רכב שעבר 150+ בדיקות אצל הדילר הרשמי, יש לו אחריות יצרן מורחבת, וניתן רק לרכבים מתחת ל-25k מייל ופחות מ-5 שנים. המחיר נמוך משמעותית מרכב חדש, האיכות זהה.</p></div>
    <div class="faq-item"><h3>איך אני יודע שאני לא מקבל "פח"?</h3><p>כל רכב עובר בדיקה עצמאית בארה"ב לפני רכישה. דו"ח Carfax/AutoCheck מלא — אתה רואה כל בעלים קודם, כל תאונה, כל תיקון. בנוסף, רכבי Certified מגיעים עם הצהרת היצרן עצמו.</p></div>
    <div class="faq-item"><h3>איך אני מקבל אחריות?</h3><p>רכב חדש — אחריות יצרן מלאה (3-5 שנים תלוי במותג). רכב Certified — אחריות יצרן מורחבת לעוד 1-2 שנים מעבר לאחריות המקורית. בנוסף, אנחנו מעניקים אחריות מקצועית משלימה על מערכות שאינן בכיסוי היצרן.</p></div>
    <div class="faq-item"><h3>מה אם הרכב נפגע בים?</h3><p>הביטוח שלנו מכסה את הרכב מהיום שהוא נטען על המשאית בארה"ב ועד שהוא בחצר שלך. במקרה נדיר של נזק — אנחנו לוקחים אחריות מלאה.</p></div>
    <div class="faq-item"><h3>אני יכול לבחור צבע ומפרט?</h3><p>כן. ברכב חדש — אתה מקבל בדיוק את הצבע, הריפוד, החבילות שביקשת. ב-CPO — אנחנו מאתרים את הרכב הספציפי שמתאים לך.</p></div>
    <div class="faq-item"><h3>איך אני משלם?</h3><p>פיקדון של ₪500 לפתיחת תיק. תשלום על הרכב — חצי בעת ההזמנה, חצי כשהרכב מגיע לישראל. כל התשלומים בהעברה בנקאית מתועדים.</p></div>
    <div class="faq-item"><h3>מה אם החלטתי להפסיק באמצע?</h3><p>אם הרכב טרם נרכש בארה"ב — הפיקדון חוזר מינוס ₪500 דמי טיפול. אם הרכב כבר נרכש — חלים תנאי החוזה (פירוט מלא בעת חתימה).</p></div>
  </div>
</section>
''',

    "trust.html": '''
<section class="page-section">
  <div style="max-width:1100px;margin:0 auto;">
    <div class="page-eyebrow">למה לסמוך עלינו</div>
    <h2>שקיפות זה לא סיסמה — זו תשתית</h2>
    <p style="font-size:18px;line-height:1.8;color:#333;">כל לקוח מקבל גישה לפורטל אישי שבו רואים כל מסמך, כל חשבונית, כל סטאטוס בזמן אמת. אנחנו לא מסתירים שום עלות, ואנחנו לא מרוויחים מעמלות נסתרות. ההכנסה היחידה שלנו היא דמי שירות מוצהרים מראש בהצעת המחיר — 5% בלבד מערך הרכב.</p>
  </div>
</section>

<section class="page-section dark">
  <div style="max-width:1280px;margin:0 auto;">
    <h2 style="color:#fff;text-align:center;margin-bottom:60px;">7 שכבות אמון</h2>
    <div class="grid-3">
      <div class="pillar-card"><div class="pillar-num">01</div><h3>חוזה אישי</h3><p>חתימה דיגיטלית של עו"ד מטעמך. כל סעיף מוסבר ושקוף.</p></div>
      <div class="pillar-card"><div class="pillar-num">02</div><h3>פיקדון מוגן</h3><p>פיקדון של ₪500 לפתיחה — מוחזק בחשבון נאמנות.</p></div>
      <div class="pillar-card"><div class="pillar-num">03</div><h3>POA חתום</h3><p>ייפוי כוח לרכישה רק לרכב הספציפי שאישרת.</p></div>
      <div class="pillar-card"><div class="pillar-num">04</div><h3>ביטוח מלא</h3><p>ים, יבשה, פריקה. כיסוי מקיף לאורך כל הדרך.</p></div>
      <div class="pillar-card"><div class="pillar-num">05</div><h3>פורטל מעקב</h3><p>מסמכים, חשבוניות, מיקום אונייה — בזמן אמת.</p></div>
      <div class="pillar-card"><div class="pillar-num">06</div><h3>בדיקה עצמאית</h3><p>בודק חיצוני בארה"ב, לא קשור לדילר.</p></div>
      <div class="pillar-card"><div class="pillar-num">07</div><h3>אחריות מקצועית</h3><p>אחריות יצרן + אחריות שלנו על שירות.</p></div>
    </div>
  </div>
</section>
''',

    "regulations.html": '''
<section class="page-section">
  <div style="max-width:1100px;margin:0 auto;">
    <div class="page-eyebrow">המסגרת החוקית</div>
    <h2>ייבוא אישי — חוקי, מוסדר, ברור</h2>
    <p style="font-size:18px;line-height:1.8;color:#333;">ייבוא אישי של רכב מאושר על ידי משרד התחבורה תחת תקנה 271. אנחנו פועלים תחת מסגרת רגולטורית מלאה ושומרים על כל הסטנדרטים הנדרשים. אנחנו לא מבטיחים "פטור ממסים" כי כזה לא קיים — אבל אנחנו כן מציעים מחיר רכב נמוך משמעותית.</p>
  </div>
</section>

<section class="page-section">
  <div style="max-width:1100px;margin:0 auto;">
    <h2>המסים שתשלם</h2>
    <div class="grid-3" style="margin-top:32px;">
      <div class="pillar-card"><div class="pillar-num">18%</div><h3>מע"מ</h3><p>על ערך הרכב + שיגור (CIF). מחושב על פי מחיר הרכישה בארה"ב.</p></div>
      <div class="pillar-card"><div class="pillar-num">83-92%</div><h3>מס קנייה</h3><p>תלוי במנוע, פליטות, סוג רכב. EV — מס מופחת משמעותית.</p></div>
      <div class="pillar-card"><div class="pillar-num">10%</div><h3>מכס</h3><p>על רכב מארה"ב. ייתכן פטור מסוים בהסכמי סחר.</p></div>
    </div>
    <p style="font-size:16px;color:#666;margin-top:32px;text-align:center;">המספרים האלה כבר משוקללים בהצעת המחיר שאתה מקבל מאיתנו. אין הפתעות.</p>
  </div>
</section>

<section class="page-section dark">
  <div style="max-width:1100px;margin:0 auto;">
    <h2 style="color:#fff;">תקנה 271 — בקצרה</h2>
    <ul style="color:rgba(255,255,255,0.8);font-size:17px;line-height:2;margin-top:24px;">
      <li>אדם פרטי יכול לייבא עד 2 רכבים בשנה לשימוש אישי</li>
      <li>הרכב חייב להיות חדש או עם פחות מ-2 בעלים קודמים</li>
      <li>אסור למכור את הרכב במשך שנה מיום הרישוי</li>
      <li>בדיקת מכון רישוי חובה — לפני שהרכב יכול לקבל לוחיות</li>
      <li>חובה לעמוד בתקני הבטיחות הישראלים (אורות, אגזוז, מד-מהירות)</li>
    </ul>
  </div>
</section>
''',
}

def inject(filename, content):
    path = os.path.join(ROOT, filename)
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()
    # Inject before <section class="page-cta">
    if '<section class="page-cta">' not in html:
        print(f"SKIP {filename}: no page-cta anchor")
        return
    if 'הסיפור שלנו' in html or 'התהליך לעומק' in html or 'למה לא יבואן רשמי' in html or 'שכבות אמון' in html or 'המסים שתשלם' in html:
        # already enriched
        print(f"ALREADY ENRICHED {filename}")
        return
    html = html.replace('<section class="page-cta">', content + '\n\n<section class="page-cta">', 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"ENRICHED {filename}: +{len(content)} chars")

for fn, ct in EXTRA.items():
    inject(fn, ct)

print("Done.")
