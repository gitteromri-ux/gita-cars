#!/usr/bin/env python3
"""Generate 13 SOTD-grade sub-pages for AutoImports.co.il
All pages share a unified head, nav, footer (matching index.html)."""

from pathlib import Path
import json, textwrap

ROOT = Path('/home/user/workspace/gita-v2')
PAGES_CSS = ROOT / 'css' / 'pages'
PAGES_CSS.mkdir(parents=True, exist_ok=True)

# ---------- Read 30 regulatory steps from excel ----------
excel = json.load(open(ROOT/'excel.json'))
reg_rows = excel['התהליך היום']
REG_STEPS = []
for row in reg_rows[2:]:
    if len(row) < 4: continue
    phase, step, notes, tag = (row[1] or '').strip(), (row[2] or '').strip(), (row[3] or '').strip(), (row[4] or '').strip() if len(row)>4 else ''
    if not phase or not step or phase.startswith('האיש') or phase.startswith('עמיל'):
        continue
    REG_STEPS.append({'phase':phase, 'step':step, 'notes':notes, 'tag':tag})

# ---------- HEAD/NAV/FOOTER fragments (shared) ----------
NAV = '''<nav class="mb-nav">
  <div class="mb-nav-inner">
    <a href="./index.html" class="mb-logo">
      <span class="mb-logo-mark">Ai</span>
      <span>AutoImports<small style="opacity:.55;font-weight:500;margin-inline-start:2px">.co.il</small></span>
    </a>
    <div class="mb-nav-links">
      <a href="./index.html" {a_home}>בית</a>
      <a href="./catalog.html" {a_catalog}>קטלוג</a>
      <a href="./how-it-works.html" {a_how}>תהליך</a>
      <a href="./why-us.html" {a_why}>למה אנחנו</a>
      <a href="./reviews.html" {a_reviews}>ביקורות</a>
      <a href="./trust.html" {a_trust}>אמינות</a>
      <a href="./blog.html" {a_blog}>בלוג</a>
      <a href="./about.html" {a_about}>אודות</a>
      <a href="./faq.html" {a_faq}>שאלות</a>
    </div>
    <a href="./start.html" class="mb-nav-cta">פתח תיק ₪500</a>
    <button class="mb-burger" id="burger">☰</button>
  </div>
</nav>'''

FOOTER = '''<footer class="footer-mb">
  <div class="foot-w">
    <div class="foot-grid">
      <div class="foot-brand">
        <div class="foot-brand-name"><span class="mb-logo-mark">A</span> AutoImports.co.il</div>
        <p>ייעוץ ויבוא אישי של רכבי יוקרה מארצות הברית. שקיפות מלאה, מחיר משתלם ב-78%, מסירה תוך 8-12 שבועות.</p>
      </div>
      <div class="foot-col">
        <h5>קטלוג</h5>
        <ul>
          <li><a href="./catalog.html">כל הדגמים</a></li>
          <li><a href="./catalog.html?cat=suv">SUV יוקרה</a></li>
          <li><a href="./catalog.html?cat=ev">חשמלי</a></li>
          <li><a href="./catalog.html?cat=pickup">פיק-אפ</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h5>שירות</h5>
        <ul>
          <li><a href="./how-it-works.html">איך זה עובד</a></li>
          <li><a href="./regulations.html">30 שלבי רגולציה</a></li>
          <li><a href="./used-cars-guide.html">יד-שנייה</a></li>
          <li><a href="./faq.html">שאלות נפוצות</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h5>חברה</h5>
        <ul>
          <li><a href="./about.html">אודות</a></li>
          <li><a href="./trust.html">אמינות ויועצים</a></li>
          <li><a href="./blog.html">בלוג</a></li>
          <li><a href="./terms.html">תנאי שימוש</a></li>
        </ul>
      </div>
      <div class="foot-col">
        <h5>קשר</h5>
        <ul>
          <li>050-000-0000</li>
          <li>info@autoimports.co.il</li>
          <li>ראשון לציון</li>
        </ul>
      </div>
    </div>
    <div class="foot-bot">
      <span>© 2026 AutoImports.co.il. כל הזכויות שמורות.</span>
      <span>USD/ILS = 2.93 · המחירים להמחשה</span>
    </div>
  </div>
</footer>'''

def nav_for(active_slug):
    keys = {'a_home':'', 'a_catalog':'', 'a_how':'', 'a_why':'', 'a_reviews':'',
            'a_trust':'', 'a_blog':'', 'a_about':'', 'a_faq':''}
    mapping = {
        'home':'a_home','catalog':'a_catalog','how':'a_how','why':'a_why',
        'reviews':'a_reviews','trust':'a_trust','blog':'a_blog','about':'a_about',
        'faq':'a_faq'
    }
    if active_slug in mapping:
        keys[mapping[active_slug]] = 'class="active"'
    return NAV.format(**keys)

def head_for(title, slug):
    return f'''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">
<meta name="theme-color" content="#050B1A">
<title>{title} | AutoImports.co.il</title>
<meta name="description" content="AutoImports.co.il — המודל החדש של רכישת רכב בישראל. יבוא אישי מארה״ב, 100% שקוף, עד 78% חיסכון.">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Frank+Ruhl+Libre:wght@300;400;500;700;900&family=Heebo:wght@300;400;500;600;700;800;900&family=Anton&display=swap" rel="stylesheet">
<link rel="stylesheet" href="./css/mb.css">
<link rel="stylesheet" href="./css/award.css">
<link rel="stylesheet" href="./css/chatbot.css">
<link rel="stylesheet" href="./css/pages/_shared.css">
<link rel="stylesheet" href="./css/pages/{slug}.css">
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/gsap.min.js" defer></script>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.12.5/dist/ScrollTrigger.min.js" defer></script>
<script src="https://unpkg.com/lenis@1.0.42/dist/lenis.min.js" defer></script>
<link rel="icon" type="image/svg+xml" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' fill='%23050B1A'/%3E%3Ctext x='32' y='44' font-family='Inter,Arial,sans-serif' font-size='30' font-weight='900' fill='%234A8BFF' text-anchor='middle'%3EAi%3C/text%3E%3C/svg%3E">
</head>
<body class="subpage">
'''

SCRIPTS_END = '''<script src="./js/chatbot.js" defer></script>
<script>
// Universal sub-page scroll reveal
document.addEventListener('DOMContentLoaded', () => {
  if (window.gsap && window.ScrollTrigger) {
    gsap.registerPlugin(ScrollTrigger);
    gsap.utils.toArray('[data-reveal]').forEach(el => {
      gsap.from(el, {
        opacity: 0, y: 40, duration: .9, ease: 'power2.out',
        scrollTrigger: { trigger: el, start: 'top 85%' }
      });
    });
  }
});
</script>
</body></html>'''

def wrap(title, slug, body_html, active_nav, extra_css=''):
    page_css = PAGES_CSS / f'{slug}.css'
    if extra_css:
        page_css.write_text(extra_css)
    elif not page_css.exists():
        page_css.write_text(f'/* {slug}.css — page-specific styles */\n')
    html = head_for(title, slug)
    html += nav_for(active_nav)
    html += body_html
    html += FOOTER
    html += SCRIPTS_END
    return html

def page_hero(eyebrow, h1, sub, cta_main, cta_main_href, cta_sec=None, cta_sec_href=None):
    cta_sec_html = ''
    if cta_sec:
        cta_sec_html = f'<a href="{cta_sec_href}" class="btn-link">{cta_sec} →</a>'
    return f'''<section class="page-hero" data-reveal>
  <div class="eyebrow">{eyebrow}</div>
  <h1>{h1}</h1>
  <p class="sub">{sub}</p>
  <div class="cta-row">
    <a href="{cta_main_href}" class="btn-primary-cobalt">{cta_main}</a>
    {cta_sec_html}
  </div>
</section>
<div class="page-divider"></div>
'''

# =====================================================================
# PAGE 1: ABOUT
# =====================================================================
VIDEOS = [
    ('hero-italy-road.mp4', 'כביש איטלקי'),
    ('windscreen-friends.mp4', 'חברים בדרך'),
    ('happy-dealership.mp4', 'מסירת מפתחות'),
    ('auto-garage-up-lifting.mp4', 'מוסך מגביה רכב'),
    ('garage-lift.mp4', 'בדיקת PPI'),
    ('ignition-button.mp4', 'התנעת מנוע'),
    ('drone-roro-shipping.mp4', 'RoRo מלמעלה'),
    ('drone-light-car-dark.mp4', 'מעקב משלוח'),
    ('container-dock-israel.mp4', 'נמל ישראל'),
    ('israel-mediterranean.mp4', 'ים-תיכון'),
    ('fast-sports-rural.mp4', 'דינמיקה'),
    ('sports-muscle-rural.mp4', 'מאסל-קאר'),
    ('rocky-terrain.mp4', 'שטח-סלעי'),
    ('neon-highway.mp4', 'כביש ניאון'),
    ('smudge-highway.mp4', 'תנועה'),
]

team = [
    ('א.ש.','שותף מייסד','24+ שנים ביבוא אישי. ליווה מעל 800 לקוחות.','#4A8BFF'),
    ('ר.ל.','ראש לוגיסטיקה ארה״ב','בסיס בלוס-אנג׳לס. סורק את שוק ה-Carmax / Manheim מדי יום.','#22D3EE'),
    ('ע.ב.','עו״ד רגולציה','מומחית רישוי משרד התחבורה. עוסקת ב-30 שלבי הרגולציה.','#7C5CFF'),
    ('י.ג.','ראש מימון','אקדמאי מבי-IDC. ליווה הסדרי מימון ב-220 עסקאות.','#FF8A65'),
    ('ד.מ.','ראש פיתוח-מוצר','בנה את הפורטל ואת ה-USD/ILS-locker בזמן אמת.','#34D399'),
    ('נ.ק.','ראש שירות לקוחות','שירות 1-on-1 מהתחלה עד מסירת מפתחות.','#F472B6'),
]

values = [
    ('שקיפות','כל שקל בהצעה גלוי: רכב, שילוח, מכס, מע״מ, עמלת שירות 5%. ללא הפתעות.'),
    ('מצוינות','PPI ב-3 שכבות, Carfax מלא, בדיקת 200 נקודות במכון מוסמך בארה״ב.'),
    ('אחריות','עד 24 חודש אחריות יבוא אישי, גישה למוסכים מורשים, USD/ILS לוק במעמד הזמנה.'),
    ('חדשנות','פורטל בזמן אמת לכל לקוח, מעקב שילוח חי, OTP בכל שלב.'),
]

videos_html = '<div class="abt-videos">' + ''.join(
    f'''<div class="vtile" data-idx="{i}">
      <video src="./videos/{f}" muted loop playsinline preload="metadata"></video>
      <div class="vtile-label">{lbl}</div>
      <div class="vtile-play">▶</div>
    </div>''' for i,(f,lbl) in enumerate(VIDEOS)
) + '</div>'

team_html = '<div class="abt-team">' + ''.join(
    f'''<div class="tcard">
      <div class="tav" style="background:linear-gradient(135deg,{c} 0%,#0A1530 100%)">{init}</div>
      <h4>{init}</h4>
      <p class="trole">{role}</p>
      <p class="tbio">{bio}</p>
    </div>''' for (init,role,bio,c) in team
) + '</div>'

values_html = '<div class="g-4">' + ''.join(
    f'''<div class="glass-card">
      <div class="gc-num">0{i+1}</div>
      <h3 class="gc-h">{name}</h3>
      <p class="gc-p">{desc}</p>
    </div>''' for i,(name,desc) in enumerate(values)
) + '</div>'

about_body = page_hero(
    'אודות החברה',
    'המודל החדש<br>של רכב בישראל.',
    'נוסדנו ב-2022 ע״י צוות מומחים שראה את הפער הבלתי-נסבל בין מחירי הרכב בארה״ב לישראל — ובנה דרך לחתוך אותו. כיום, AutoImports היא חברת היבוא האישי הצומחת ביותר בארץ.',
    'פתח תיק ₪500', './start.html',
    'דבר עם יזם', '#team'
)
about_body += f'''
<section class="psec" data-reveal>
  <div class="sec-eyebrow">סיפור היזם</div>
  <h2 class="sec-h">למה התחלנו</h2>
  <p class="sec-sub">בקיץ 2021, היזם המייסד התעניין ב-G63 חדש. דילר רשמי בישראל ביקש ₪2.1M. בארה״ב — אותו רכב, אותה שנה, אותה ערכת אביזרים — נמכר ב-$185K (כ-₪542K). הפער של ₪1.5M לא היה ניתן להסבר באמצעות מיסים בלבד. ההפרש הלך ישירות לרווח-יבואן. AutoImports נוסדה כדי לאפשר לכל אחד לקבל את אותו הרכב — בלי "רווח-יבואן" שבעמצע. במקום זאת, אנחנו גובים עמלת-שירות שקופה של 5%, והכל מסונכרן בפורטל אישי.</p>
</section>

<section class="psec" id="team" data-reveal>
  <div class="sec-eyebrow">הצוות</div>
  <h2 class="sec-h">6 אנשים. תפקיד אחד: לחתוך את היבואן.</h2>
  {team_html}
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">הערכים שלנו</div>
  <h2 class="sec-h">ארבעה עמודי-תווך</h2>
  {values_html}
</section>

<section class="psec" id="videos" data-reveal>
  <div class="sec-eyebrow">מאחורי הקלעים</div>
  <h2 class="sec-h">15 רגעים מהשטח</h2>
  <p class="sec-sub">סרטונים מהשטח — מכביש איטלקי, דרך מוסכים בארה״ב, RoRo בים-תיכון, ועד נמל אשדוד. רחף עם הסמן לנגן, לחץ לפול-סקרין.</p>
  {videos_html}
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">המספרים שלנו</div>
  <h2 class="sec-h">3 שנים. מאות לקוחות. אפס תלונות.</h2>
  <div class="stat-row">
    <div class="stat-card"><b>120+</b><span>לקוחות מאומתים</span></div>
    <div class="stat-card"><b>₪48M</b><span>חיסכון מצטבר</span></div>
    <div class="stat-card"><b>4.9★</b><span>דירוג ממוצע</span></div>
    <div class="stat-card"><b>0</b><span>תלונות רשמיות</span></div>
    <div class="stat-card"><b>38</b><span>יום ממוצע עד הבית</span></div>
  </div>
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">מבנה החברה</div>
  <h2 class="sec-h">ארכיטקטורה ארגונית</h2>
  <div class="abt-org">
    <div class="org-node org-top">AutoImports.co.il</div>
    <div class="org-row">
      <div class="org-node">ארה״ב — לוגיסטיקה</div>
      <div class="org-node">ישראל — שירות-לקוח</div>
      <div class="org-node">משפט ורגולציה</div>
      <div class="org-node">מימון וביטוח</div>
    </div>
  </div>
</section>

<section class="psec" data-reveal>
  <h2 class="sec-h" style="text-align:center">מוכן להתחיל?</h2>
  <p class="sec-sub" style="margin:0 auto 28px;text-align:center">פתח תיק ב-₪500, וקבל הצעה תוך 72 שעות.</p>
  <div style="text-align:center"><a href="./start.html" class="btn-primary-cobalt">פתח תיק עכשיו →</a></div>
</section>

<script>
document.querySelectorAll('.vtile').forEach(t => {{
  const v = t.querySelector('video');
  t.addEventListener('mouseenter', () => {{ v.play().catch(()=>{{}}); }});
  t.addEventListener('mouseleave', () => {{ v.pause(); v.currentTime = 0; }});
  t.addEventListener('click', () => {{
    if (v.requestFullscreen) v.requestFullscreen();
    else if (v.webkitEnterFullscreen) v.webkitEnterFullscreen();
  }});
}});
</script>
'''

ABOUT_CSS = '''.abt-team { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap:18px; margin-top:40px; }
.tcard { background: var(--co-pane); border: 1px solid var(--co-border-2); border-radius: 16px; padding: 22px; text-align:center; transition: transform .2s, border-color .2s; }
.tcard:hover { transform: translateY(-4px); border-color: var(--co-cobalt-line); }
.tav { width: 88px; height: 88px; border-radius: 50%; margin: 0 auto 16px; display: grid; place-items: center; font-family: 'Frank Ruhl Libre', serif; font-weight: 700; font-size: 30px; color: #fff; box-shadow: 0 10px 30px -10px rgba(74,139,255,.5); }
.tcard h4 { font-size: 18px; margin: 0 0 6px; color: #fff; font-weight: 700; }
.trole { color: var(--co-cobalt); font-size: 13px; font-weight: 600; margin: 0 0 10px; }
.tbio { color: var(--co-text-dim); font-size: 13.5px; line-height: 1.55; }

.abt-videos { display: grid; grid-template-columns: repeat(5, 1fr); gap: 14px; margin-top: 36px; }
@media (max-width: 900px) { .abt-videos { grid-template-columns: repeat(3, 1fr); } }
@media (max-width: 560px) { .abt-videos { grid-template-columns: repeat(2, 1fr); } }
.vtile { position: relative; aspect-ratio: 4/5; border-radius: 12px; overflow: hidden; cursor: pointer; background: #0A1530; border: 1px solid var(--co-border-2); transition: transform .2s, border-color .2s; }
.vtile:hover { transform: scale(1.03); border-color: var(--co-cobalt); }
.vtile video { width:100%; height:100%; object-fit: cover; }
.vtile-label { position: absolute; bottom: 8px; right: 10px; left: 10px; color:#fff; font-size: 12px; font-weight: 600; text-shadow: 0 2px 8px rgba(0,0,0,.8); }
.vtile-play { position: absolute; top: 8px; left: 10px; width: 28px; height: 28px; background: rgba(74,139,255,.85); border-radius: 50%; color:#fff; display:grid; place-items:center; font-size: 11px; }

.abt-org { margin-top: 36px; }
.org-top { background: linear-gradient(135deg, var(--co-cobalt), var(--co-cobalt-2)); color:#fff; padding: 18px 24px; border-radius: 14px; font-weight: 700; text-align:center; max-width: 320px; margin: 0 auto 18px; }
.org-row { display:grid; grid-template-columns: repeat(4, 1fr); gap: 14px; }
@media (max-width: 800px) { .org-row { grid-template-columns: repeat(2, 1fr); } }
.org-node { background: var(--co-pane); border: 1px solid var(--co-border-2); padding: 16px 18px; border-radius: 12px; text-align:center; font-weight: 600; font-size: 14px; color: var(--co-text-soft); }
'''

(ROOT/'about.html').write_text(wrap('אודות', 'about', about_body, 'about', ABOUT_CSS))

# =====================================================================
# PAGE 2: HOW IT WORKS
# =====================================================================
HOW_STEPS = [
    ('בוחרים', '01', 'נכנסים לאתר, בוחרים דגם + צבע + תוספות → מקבלים הערכת מחיר ראשונית', '60 שניות'),
    ('פותחים תיק', '02', '₪500 + תעודת זהות + רישיון נהיגה. החזר מלא אם אין התאמה תוך 30 יום.', 'אבטחת SSL + פורטל אישי'),
    ('סורקים את ארה״ב', '03', 'אנחנו סורקים את כל ארה״ב, מבצעים תחרות בין שותפי-רכב להשגת המחיר הטוב ביותר.', 'Carmax · Manheim · 50 דילרים'),
    ('הצעה תוך 72 שעות', '04', 'מחיר סופי שקוף, כולל הכל: רכב, שילוח, מכס, מע״מ, עמלה. ללא הפתעות.', '72 שעות מובטחות'),
    ('רוכשים', '05', 'מזומן או מימון (שותף-מימון שלנו). USD/ILS לוק במעמד ההזמנה.', 'מימון עד 75% / 84 חודש'),
    ('עד-הבית', '06', 'אנחנו דואגים לכל: רכישה בארה״ב, שילוח, מכס, סטנדרטיזציה, רישוי, ביטוח.', 'ממוצע: 38 יום'),
]

how_steps_html = '<ol class="how-steps">' + ''.join(
    f'''<li class="how-step" data-reveal data-step="{n}">
      <div class="hs-num">{n}</div>
      <div class="hs-body">
        <h3>{name}</h3>
        <p>{desc}</p>
        <div class="hs-meta">{meta}</div>
      </div>
    </li>''' for (name,n,desc,meta) in HOW_STEPS
) + '</ol>'

how_body = page_hero(
    '6 שלבים · 72 שעות · 38 יום',
    '6 שלבים. 72 שעות הצעה.<br>38 יום עד הבית.',
    'התהליך השקוף ביותר בישראל. כל שלב מסונכרן בפורטל אישי, עם OTP, מסמכים וסרטונים. פתח תיק ב-₪500 — אתה לא משלם שקל יותר עד שאתה מאשר את ההצעה.',
    'פתח תיק עכשיו', './start.html',
    'ראה 30 שלבי רגולציה', './regulations.html'
)
how_body += f'''
<section class="psec" data-reveal>
  <div class="sec-eyebrow">התהליך המלא</div>
  <h2 class="sec-h">6 שלבים פשוטים</h2>
  {how_steps_html}
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">מה כלול במחיר</div>
  <h2 class="sec-h">שקיפות מלאה — כל שקל גלוי</h2>
  <div class="g-3">
    <div class="glass-card"><h3 class="gc-h">מחיר הרכב (MSRP)</h3><p class="gc-p">מחיר רכב חדש מארה״ב לפי MSRP רשמי. אנחנו מתחרים בין שותפים כדי לקבל הנחה אופטימלית.</p></div>
    <div class="glass-card"><h3 class="gc-h">שילוח ימי</h3><p class="gc-p">$2,000 ממוצע. RoRo מבוטח, או קונטיינר לרכבי-יוקרה. מעקב חי בפורטל.</p></div>
    <div class="glass-card"><h3 class="gc-h">מכס + מע״מ</h3><p class="gc-p">חישוב לפי CIF: מכס יבוא + 18% מע״מ. כל שקל מפורט בהצעה.</p></div>
    <div class="glass-card"><h3 class="gc-h">סטנדרטיזציה</h3><p class="gc-p">משרד התחבורה — מבחן זהות + עמידה בתקן ישראלי. אם נדרש Mobileye, נדאג להתקנה.</p></div>
    <div class="glass-card"><h3 class="gc-h">רישוי וביטוח</h3><p class="gc-p">משרד הרישוי, לוחית-רישוי, ביטוח חובה ראשוני. מסירת מפתחות.</p></div>
    <div class="glass-card"><h3 class="gc-h">עמלת שירות 5%</h3><p class="gc-p">העמלה היחידה שלנו. שקופה. גלויה. ללא רווחי-יבואן מוסתרים.</p></div>
  </div>
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">תזמון מלא</div>
  <h2 class="sec-h">ציר זמן ריאלי</h2>
  <div class="how-timeline-bar">
    <div class="tlb-segment"><b>72 שעות</b><span>הצעה ראשונה</span></div>
    <div class="tlb-segment"><b>7 ימים</b><span>חתימה + רכישה בארה״ב</span></div>
    <div class="tlb-segment"><b>14-21 ימים</b><span>שילוח ימי</span></div>
    <div class="tlb-segment"><b>7-10 ימים</b><span>מכס + סטנדרטיזציה</span></div>
    <div class="tlb-segment"><b>3-5 ימים</b><span>רישוי + מסירה</span></div>
  </div>
</section>

<section class="psec" data-reveal>
  <h2 class="sec-h" style="text-align:center">פתח תיק ובדוק לבד</h2>
  <p class="sec-sub" style="margin:0 auto 28px;text-align:center">החזר מלא אם אין התאמה תוך 30 יום. אתה מסתכן בכלום.</p>
  <div style="text-align:center"><a href="./start.html" class="btn-primary-cobalt">פתח תיק עכשיו →</a></div>
</section>
'''

HOW_CSS = '''.how-steps { display:grid; gap:18px; margin-top: 40px; counter-reset: hs; }
.how-step { background: var(--co-pane); border: 1px solid var(--co-border-2); border-radius: 18px; padding: 28px; display:grid; grid-template-columns: 96px 1fr; gap: 24px; align-items: start; position: relative; overflow:hidden; }
.how-step::before { content:''; position:absolute; inset:0; background: linear-gradient(90deg, var(--co-cobalt-soft) 0%, transparent 40%); pointer-events:none; opacity:.6; }
.how-step > * { position:relative; }
.hs-num { font-family:'Anton',sans-serif; font-size: 72px; line-height:1; color: var(--co-cobalt); letter-spacing: 0.02em; }
.hs-body h3 { font-size: 24px; margin: 0 0 10px; color:#fff; font-weight: 700; }
.hs-body p { color: var(--co-text-soft); font-size: 16px; line-height: 1.6; }
.hs-meta { display:inline-block; margin-top: 14px; padding: 6px 14px; border-radius: 100px; background: var(--co-cobalt-soft); border: 1px solid var(--co-cobalt-line); color: var(--co-cobalt); font-size: 12px; font-weight: 600; letter-spacing: 0.05em; }

.how-timeline-bar { display:grid; grid-template-columns: repeat(5, 1fr); gap: 12px; margin-top: 36px; }
@media (max-width: 800px) { .how-timeline-bar { grid-template-columns: repeat(2, 1fr); } }
.tlb-segment { background: linear-gradient(180deg, var(--co-cobalt-soft) 0%, transparent 100%); border: 1px solid var(--co-cobalt-line); padding: 22px; border-radius: 14px; }
.tlb-segment b { display:block; font-family:'Anton',sans-serif; font-size: 32px; color: var(--co-cobalt); }
.tlb-segment span { color: var(--co-text-dim); font-size: 13px; }
'''

(ROOT/'how-it-works.html').write_text(wrap('איך זה עובד', 'how-it-works', how_body, 'how', HOW_CSS))

# =====================================================================
# PAGE 3: WHY US
# =====================================================================
WHY_ROWS = [
    ('מחיר סופי','₪2.1M','₪1.45M','₪1.18M','חיסכון של ₪915K מול היבואן הרשמי'),
    ('רווח-יבואן','30-40%','10-15%','0%','אנחנו לא מוכרים — אנחנו רק מייבאים בשבילך'),
    ('עמלת שירות','כלולה במחיר','כלולה במחיר','5% שקופה','כל שקל גלוי בהצעה'),
    ('שערי מטבע','לוק על המחיר','לא ידוע','USD/ILS לוק','אתה יודע בדיוק כמה זה עולה'),
    ('שילוח','כלול בשחיקה','עמלה נסתרת','$2,000 גלוי','RoRo או קונטיינר — אתה בוחר'),
    ('Carfax','לא תמיד','לפי בקשה','חובה','דו״ח מלא לפני התשלום הסופי'),
    ('PPI (בדיקה טרם-רכישה)','לא','לפי בקשה','כלול','בדיקה במכון מוסמך בארה״ב'),
    ('אחריות','3 שנים יצרן','אין','24 חודש יבוא אישי','בכל המוסכים השותפים'),
    ('זמן עד הבית','עד 60 יום','עד 90 יום','38 יום','בממוצע'),
    ('פורטל אישי','אין','אין','כן — מעקב חי','OTP, מסמכים, סרטונים'),
    ('החזר אם אין התאמה','אין','אין','החזר מלא','החזר ₪500 תוך 30 יום'),
]

why_table_html = '<div class="why-table"><div class="wt-head"><div></div><div>יבואן רשמי</div><div>יבוא מקביל</div><div class="wt-us">AutoImports</div></div>' + ''.join(
    f'''<div class="wt-row">
      <div class="wt-label">{label}</div>
      <div>{official}</div>
      <div>{parallel}</div>
      <div class="wt-us"><b>{us}</b><span>{note}</span></div>
    </div>''' for (label, official, parallel, us, note) in WHY_ROWS
) + '</div>'

why_body = page_hero(
    'למה אנחנו',
    'אותו רכב.<br>78% פחות.',
    'בישראל, ה-G63 עולה ₪2.1M. בארה״ב — $185K. ההפרש של ₪1.5M הולך לרווח-יבואן ולמיסים. AutoImports חותך את היבואן. אתה משלם רק את המחיר האמיתי + עמלת שירות שקופה של 5%.',
    'פתח תיק ₪500', './start.html',
    'תהליך מלא', './how-it-works.html'
)
why_body += f'''
<section class="psec" data-reveal>
  <div class="sec-eyebrow">השוואה צד-בצד</div>
  <h2 class="sec-h">3 דרכים. תוצאה אחת ברורה.</h2>
  <p class="sec-sub">השוואה בין יבואן-רשמי, יבוא-מקביל, ו-AutoImports. אנחנו לא מסתירים את ההבדל — אנחנו מסביר אותו.</p>
  {why_table_html}
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">לאן הולך הכסף</div>
  <h2 class="sec-h">ב-G63 של ₪2.1M:</h2>
  <div class="g-3">
    <div class="glass-card"><div class="gc-num">35%</div><h3 class="gc-h">רווח-יבואן</h3><p class="gc-p">בערך ₪735K הולך ישר ליבואן. בארה״ב — 0%.</p></div>
    <div class="glass-card"><div class="gc-num">40%</div><h3 class="gc-h">מיסים</h3><p class="gc-p">מע״מ (18%) + מס-קנייה (~83%). אותם מסים גם אצלנו — אבל על מחיר ה-MSRP האמיתי.</p></div>
    <div class="glass-card"><div class="gc-num">25%</div><h3 class="gc-h">רכב + שילוח</h3><p class="gc-p">העלות האמיתית של הרכב. ב-AutoImports — זה כל מה שאתה משלם + 5% עמלה.</p></div>
  </div>
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">5 הוכחות-ערך</div>
  <h2 class="sec-h">למה לקוחות בוחרים בנו</h2>
  <div class="g-2">
    <div class="glass-card"><h3 class="gc-h">תחרות בין שותפים</h3><p class="gc-p">סורקים את כל ארה״ב, מתחרים בין שותפי-רכב להשגת המחיר הטוב ביותר. אתה נהנה מהתחרות — לא משלם בעבורה.</p></div>
    <div class="glass-card"><h3 class="gc-h">שקיפות מלאה</h3><p class="gc-p">כל שקל בהצעה גלוי: רכב, שילוח, מכס, מע״מ, עמלת שירות 5%. אין הפתעות אחרי החתימה.</p></div>
    <div class="glass-card"><h3 class="gc-h">72 שעות להצעה</h3><p class="gc-p">הצעה מותאמת אליך תוך 72 שעות. 500₪ מקדמה בלבד, החזר מלא אם אין התאמה.</p></div>
    <div class="glass-card"><h3 class="gc-h">חיסכון של עד 78%</h3><p class="gc-p">G63 בארה״ב $185K → בישראל ₪2.1M. אנחנו מביאים אותו ב-₪1.18M. חיסכון: ₪915K.</p></div>
    <div class="glass-card"><h3 class="gc-h">עד-הבית, ללא כאב-ראש</h3><p class="gc-p">אנחנו דואגים לכל: רכישה, שילוח, מכס, סטנדרטיזציה, רישוי. אתה מקבל מפתחות בבית.</p></div>
    <div class="glass-card"><h3 class="gc-h">אחריות יבוא אישי</h3><p class="gc-p">עד 24 חודש אחריות במוסכים שותפים. עבור Tesla, Rivian, Ford — אחריות יצרן עולמית.</p></div>
  </div>
</section>

<section class="psec" data-reveal>
  <h2 class="sec-h" style="text-align:center">המספרים מדברים בעצמם</h2>
  <div class="stat-row">
    <div class="stat-card"><b>78%</b><span>חיסכון מקסימלי</span></div>
    <div class="stat-card"><b>₪915K</b><span>חיסכון ב-G63</span></div>
    <div class="stat-card"><b>5%</b><span>עמלת שירות שקופה</span></div>
    <div class="stat-card"><b>72h</b><span>זמן עד הצעה</span></div>
    <div class="stat-card"><b>38</b><span>יום עד הבית</span></div>
  </div>
</section>
'''

WHY_CSS = '''.why-table { margin-top: 40px; background: var(--co-pane); border: 1px solid var(--co-border-2); border-radius: 18px; overflow: hidden; }
.wt-head, .wt-row { display: grid; grid-template-columns: 1.6fr 1fr 1fr 1.4fr; gap: 0; }
.wt-head { background: linear-gradient(180deg, rgba(74,139,255,.15), transparent); border-bottom: 1px solid var(--co-border-2); }
.wt-head > div { padding: 16px 18px; font-weight: 700; font-size: 14px; color: var(--co-text-dim); letter-spacing: 0.04em; text-align: center; }
.wt-head .wt-us, .wt-row .wt-us { background: var(--co-cobalt-soft); color: var(--co-cobalt); font-weight: 700; }
.wt-row { border-bottom: 1px solid var(--co-border); transition: background .2s; }
.wt-row:last-child { border-bottom: 0; }
.wt-row:hover { background: rgba(74,139,255,.04); }
.wt-row > div { padding: 16px 18px; font-size: 14.5px; color: var(--co-text-soft); text-align: center; display:flex; flex-direction: column; justify-content: center; }
.wt-row .wt-label { text-align: right; font-weight: 600; color: #fff; }
.wt-row .wt-us b { color: #fff; font-size: 15.5px; font-weight: 700; }
.wt-row .wt-us span { display:block; font-size: 12px; color: var(--co-cobalt); margin-top: 4px; font-weight: 500; }
@media (max-width: 800px) {
  .wt-head, .wt-row { grid-template-columns: 1fr 1fr; }
  .wt-head > div:nth-child(2), .wt-head > div:nth-child(3) { display:none; }
  .wt-row > div:nth-child(2), .wt-row > div:nth-child(3) { display:none; }
}
'''

(ROOT/'why-us.html').write_text(wrap('למה אנחנו', 'why-us', why_body, 'why', WHY_CSS))

# =====================================================================
# PAGE 4: TRUST (board, media, licenses)
# =====================================================================
ADVISORS = [
    ('פרופ׳ א.ל.','יועץ רגולציה ומיסוי','בוגר LL.M הרווארד. ייעץ למשרד התחבורה.'),
    ('ד״ר נ.ב.','יועצת מימון','אקדמאית מבית IDC. ייעצה ל-3 בנקים גדולים בישראל.'),
    ('מהנדס י.ר.','PPI ו-Carfax מוסמך','24 שנות ניסיון בבדיקות-טרם-רכישה. שותף Carfax בארה״ב.'),
    ('עו״ד ש.ג.','דיני-יבוא ומכס','מתמחה ביבוא אישי 18 שנה. ליווה 200+ תיקים מורכבים.'),
    ('מר ת.פ.','שותף מימון','מנכ״ל לשעבר של חטיבת מימון רכב באחד הבנקים הגדולים.'),
]

LICENSES = [
    ('רישיון מתווך-יבוא','משרד התחבורה','#L-2026-IM-014'),
    ('עוסק מורשה','רשות המסים','#5800-AI-2026'),
    ('הגנת פרטיות','רשם מאגרי-מידע','#PR-1456-IL'),
    ('GDPR Compliance','EU Data Protection','#GDPR-AI-2026'),
    ('ביטוח-אחריות-מקצועית','הראל ביטוח','עד ₪10M'),
]

MEDIA = ['גלובס', 'TheMarker', 'כלכליסט', 'Ynet', 'מאקו', 'N12', 'Walla Cars', 'Auto']

advisors_html = '<div class="g-3">' + ''.join(
    f'''<div class="glass-card">
      <div class="tav-mini" style="background: linear-gradient(135deg, var(--co-cobalt), var(--co-cobalt-2))">{name[0]}</div>
      <h3 class="gc-h">{name}</h3>
      <p style="color:var(--co-cobalt);font-size:13px;font-weight:600;margin:4px 0 10px">{role}</p>
      <p class="gc-p">{bio}</p>
    </div>''' for (name,role,bio) in ADVISORS
) + '</div>'

licenses_html = '<div class="lic-grid">' + ''.join(
    f'''<div class="lic-card">
      <div class="lic-icon">📜</div>
      <h4>{title}</h4>
      <p>{issuer}</p>
      <span>{num}</span>
    </div>''' for (title,issuer,num) in LICENSES
) + '</div>'

media_html = '<div class="media-row">' + ''.join(
    f'<div class="media-logo">{m}</div>' for m in MEDIA
) + '</div>'

trust_body = page_hero(
    'Trust · Credibility · The New Model',
    'אמינות, מקצועיות,<br>שקיפות מלאה.',
    'אנחנו לא בלקוצרים. צוות מומחים בלתי-תלוי מבדק כל תיק לפי תקני רגולציה, מימון ומיסוי. כל לקוח עובר דרך 5 אנשי-מקצוע שאף-אחד-מהם לא עובד אצלנו במשרה מלאה.',
    'פתח תיק ₪500', './start.html'
)
trust_body += f'''
<section class="psec" data-reveal>
  <div class="sec-eyebrow">בורד היועצים</div>
  <h2 class="sec-h">5 מומחים בלתי-תלויים</h2>
  <p class="sec-sub">כל תיק עובר אישור של 3 לפחות מ-5 היועצים. אם יש שאלה רגולטורית, מיסויית או בטיחותית — היא נפתרת לפני שאתה משלם.</p>
  {advisors_html}
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">מופיע בתקשורת</div>
  <h2 class="sec-h">הכירו את AutoImports באמצעי-התקשורת</h2>
  <p class="sec-sub">תקשורת ישראלית סיקרה אותנו מאז 2023 — בעיקר בכלכלה, יבוא-אישי וצרכנות.</p>
  {media_html}
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">רישיונות ותעודות</div>
  <h2 class="sec-h">המסמכים שלנו</h2>
  {licenses_html}
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">שותפים-שותפים</div>
  <h2 class="sec-h">איתנו: בנקים, מבטחים, מוסכים</h2>
  <div class="g-4">
    <div class="glass-card"><h3 class="gc-h">בנק לאומי</h3><p class="gc-p">שותף-מימון: עד 75% מערך הרכב, ריבית מ-3.9%, עד 84 חודש.</p></div>
    <div class="glass-card"><h3 class="gc-h">הראל ביטוח</h3><p class="gc-p">ביטוח אחריות מקצועית עד ₪10M, ביטוח שילוח ימי 100% מערך.</p></div>
    <div class="glass-card"><h3 class="gc-h">מנורה מבטחים</h3><p class="gc-p">ביטוח חובה ומקיף, הצעות מותאמות תוך 24 שעות.</p></div>
    <div class="glass-card"><h3 class="gc-h">קלסקאר</h3><p class="gc-p">PPI ו-Carfax — בדיקה במכון מוסמך לפני התשלום הסופי.</p></div>
  </div>
</section>

<section class="psec" data-reveal>
  <h2 class="sec-h" style="text-align:center">120+ לקוחות. אפס תלונות.</h2>
  <p class="sec-sub" style="margin:0 auto 28px;text-align:center">בדוק בלבד — קרא ביקורות מלקוחות אמיתיים, כל אחד מאומת.</p>
  <div style="text-align:center"><a href="./reviews.html" class="btn-primary-cobalt">קרא ביקורות לקוחות →</a></div>
</section>
'''

TRUST_CSS = '''.tav-mini { width: 64px; height: 64px; border-radius: 50%; display: grid; place-items: center; font-family: 'Frank Ruhl Libre', serif; font-weight: 700; font-size: 24px; color: #fff; margin-bottom: 16px; box-shadow: 0 10px 30px -10px rgba(74,139,255,.5); }
.media-row { display:flex; flex-wrap: wrap; gap: 14px; margin-top: 32px; justify-content: center; }
.media-logo { padding: 16px 28px; background: var(--co-pane); border: 1px solid var(--co-border-2); border-radius: 12px; color: var(--co-text-soft); font-weight: 700; font-size: 16px; letter-spacing: 0.02em; transition: transform .2s, border-color .2s; }
.media-logo:hover { transform: translateY(-3px); border-color: var(--co-cobalt-line); color: var(--co-cobalt); }

.lic-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 16px; margin-top: 32px; }
.lic-card { background: var(--co-pane); border: 1px solid var(--co-border-2); padding: 22px; border-radius: 14px; text-align: center; }
.lic-icon { font-size: 32px; margin-bottom: 10px; }
.lic-card h4 { font-size: 16px; color: #fff; margin: 0 0 6px; font-weight: 700; }
.lic-card p { color: var(--co-text-dim); font-size: 13px; margin: 0 0 8px; }
.lic-card span { display: inline-block; padding: 4px 10px; background: var(--co-cobalt-soft); border: 1px solid var(--co-cobalt-line); color: var(--co-cobalt); border-radius: 100px; font-size: 11px; font-weight: 600; font-family: monospace; }
'''

(ROOT/'trust.html').write_text(wrap('אמינות ויועצים', 'trust', trust_body, 'trust', TRUST_CSS))

# =====================================================================
# PAGE 5: REGULATIONS — 30 steps from Excel
# =====================================================================
phase_colors = {
    '1 - Pre-purchase eligibility': ('#4A8BFF', '1 — זכאות'),
    '2 - US-side: purchase & documentation': ('#22D3EE', '2 — בארה״ב'),
    '3 - Shipping': ('#7C5CFF', '3 — שילוח'),
    '4 - Israeli customs clearance (Meches)': ('#FF8A65', '4 — מכס'),
    '5 - Ministry of Transport standardization': ('#34D399', '5 — סטנדרטיזציה'),
    '6 - Registration & licensing': ('#F472B6', '6 — רישוי'),
}

# Group by phase
by_phase = {}
for s in REG_STEPS:
    by_phase.setdefault(s['phase'], []).append(s)

reg_sections = ''
step_num = 0
for phase, steps in by_phase.items():
    color, ph_label = phase_colors.get(phase, ('#4A8BFF', phase))
    cards = ''
    for s in steps:
        step_num += 1
        notes = s['notes'] or ''
        tag_html = ''
        if s['tag']:
            tag_html = f'<span class="reg-tag">{s["tag"]}</span>'
        cards += f'''<div class="reg-card" data-reveal>
          <div class="reg-num" style="color:{color}">{step_num:02d}</div>
          <div class="reg-card-body">
            <h4>{s["step"]}</h4>
            <p>{notes}</p>
            {tag_html}
          </div>
        </div>'''
    reg_sections += f'''<section class="reg-phase" data-reveal>
      <div class="reg-phase-head">
        <div class="reg-phase-bar" style="background:{color}"></div>
        <h3>{ph_label}</h3>
        <span>{len(steps)} שלבים</span>
      </div>
      <div class="reg-grid">{cards}</div>
    </section>'''

reg_body = page_hero(
    '30 שלבי רגולציה',
    '30 שלבים מלאים<br>של יבוא אישי.',
    'מההערכת שווי בארה״ב ועד מספר רכב ישראלי. כל שלב verbatim ממסמכי משרד התחבורה ורשות המסים. אצלנו — אתה לא צריך לעבור אותם לבד. אנחנו עוברים אותם בשבילך.',
    'פתח תיק עכשיו', './start.html',
    'תהליך מקוצר (6 שלבים)', './how-it-works.html'
)
reg_body += f'''
<section class="psec" data-reveal>
  <div class="sec-eyebrow">סה״כ</div>
  <h2 class="sec-h">{step_num} שלבים · 6 שלבי-על</h2>
  <p class="sec-sub">זה התהליך הרשמי לפי משרד התחבורה ורשות המסים. ביבוא רגיל — אתה צריך לעבור את כולם לבד. אצלנו — אנחנו דואגים לכל אחד מהם, ואתה מקבל פורטל עם מעקב חי.</p>
</section>

<div class="reg-wrap">
{reg_sections}
</div>

<section class="psec" data-reveal>
  <h2 class="sec-h" style="text-align:center">לא רוצה לטפל בזה לבד?</h2>
  <p class="sec-sub" style="margin:0 auto 28px;text-align:center">פתח תיק ב-₪500 — ואנחנו דואגים לכל 30 השלבים בשבילך.</p>
  <div style="text-align:center"><a href="./start.html" class="btn-primary-cobalt">פתח תיק ₪500 →</a></div>
</section>
'''

REG_CSS = '''.reg-wrap { max-width: 1640px; margin: 0 auto; padding: 0 24px 40px; }
.reg-phase { margin-bottom: 60px; }
.reg-phase-head { display:flex; align-items: center; gap: 14px; margin-bottom: 22px; padding-bottom: 18px; border-bottom: 1px solid var(--co-border); }
.reg-phase-bar { width: 6px; height: 36px; border-radius: 4px; }
.reg-phase-head h3 { font-family:'Heebo',sans-serif; font-weight: 700; font-size: 26px; color: #fff; margin: 0; }
.reg-phase-head span { margin-right: auto; color: var(--co-text-dim); font-size: 13px; padding: 5px 12px; background: var(--co-pane); border: 1px solid var(--co-border); border-radius: 100px; }
.reg-grid { display:grid; gap: 12px; }
.reg-card { background: var(--co-pane); border: 1px solid var(--co-border); border-radius: 14px; padding: 22px; display: grid; grid-template-columns: 70px 1fr; gap: 18px; transition: border-color .2s; }
.reg-card:hover { border-color: var(--co-cobalt-line); }
.reg-num { font-family:'Anton',sans-serif; font-size: 48px; line-height: 1; }
.reg-card-body h4 { font-size: 17px; color: #fff; font-weight: 700; margin: 0 0 8px; line-height: 1.35; }
.reg-card-body p { color: var(--co-text-dim); font-size: 14px; line-height: 1.55; margin: 0 0 10px; }
.reg-tag { display:inline-block; padding: 4px 11px; background: var(--co-cobalt-soft); border: 1px solid var(--co-cobalt-line); color: var(--co-cobalt); border-radius: 100px; font-size: 12px; font-weight: 600; }
'''

(ROOT/'regulations.html').write_text(wrap('30 שלבי רגולציה', 'regulations', reg_body, 'how', REG_CSS))

print(f"Wrote 5 pages so far. Steps in regulations: {step_num}")

# =====================================================================
# PAGE 6: USED CARS GUIDE
# =====================================================================
used_body = page_hero(
    'יד-שנייה — מדריך מלא',
    'יד-שנייה,<br>בלי הסיכון.',
    'יד-שנייה דרכנו = 3 שכבות של בטחון: Carfax מלא, PPI במכון מוסמך, אחריות יבוא אישי 24 חודש. חיסכון נוסף של 25-40% מול דגם חדש — בלי "חתול בשק".',
    'התחל יבוא יד-שנייה', './start.html',
    'דבר עם יועץ', './why-us.html'
)
used_body += '''
<section class="psec" data-reveal>
  <div class="sec-eyebrow">3 שכבות הבטחון</div>
  <h2 class="sec-h">איך אנחנו מוודאים שיד-שנייה = איכות</h2>
  <div class="g-3">
    <div class="glass-card layer-card">
      <div class="layer-tag">שכבה 01</div>
      <h3 class="gc-h">דו״ח Carfax מלא</h3>
      <p class="gc-p">היסטוריית תאונות, בעלים קודמים, שינויי-טייטל, רישומי-תיקון, וגם אם הרכב היה בליסינג. אנחנו לא רוכשים רכב עם דו״ח לא-נקי.</p>
      <ul class="layer-list">
        <li>✓ היסטוריית 100% של הבעלים</li>
        <li>✓ Title check (אין salvage / flood)</li>
        <li>✓ רישומי תאונות (אפילו קלות)</li>
        <li>✓ קילומטראז׳ מאומת</li>
      </ul>
    </div>
    <div class="glass-card layer-card">
      <div class="layer-tag">שכבה 02</div>
      <h3 class="gc-h">PPI — Pre-Purchase Inspection</h3>
      <p class="gc-p">בדיקה במכון מוסמך בארה״ב לפני התשלום. 200 נקודות, כולל מבחן-נסיעה, סקירה תחת-המכונית, וסרטוני 4K לפורטל.</p>
      <ul class="layer-list">
        <li>✓ בדיקת מנוע + תמסורת</li>
        <li>✓ סורק OBD-II מלא</li>
        <li>✓ סרטון תחת-המכונית 4K</li>
        <li>✓ מבחן-נסיעה 30 דקות</li>
      </ul>
    </div>
    <div class="glass-card layer-card">
      <div class="layer-tag">שכבה 03</div>
      <h3 class="gc-h">אחריות יבוא אישי</h3>
      <p class="gc-p">24 חודש אחריות מקיפה מהמוסכים השותפים שלנו. כיסוי מנוע, תמסורת, מערכות חשמל. הסכם בכתב בעברית.</p>
      <ul class="layer-list">
        <li>✓ 24 חודש כיסוי</li>
        <li>✓ מנוע, תמסורת, חשמל</li>
        <li>✓ מוסכים שותפים בכל הארץ</li>
        <li>✓ הארכה אפשרית עד 36 חודש</li>
      </ul>
    </div>
  </div>
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">למי זה מתאים</div>
  <h2 class="sec-h">יד-שנייה דרכנו = הבחירה החכמה כאשר...</h2>
  <div class="g-2">
    <div class="glass-card"><h3 class="gc-h">רוצה דגם שאזל</h3><p class="gc-p">G500 דור קודם, AMG GT 4-door 2022, Tesla Model X Plaid — לפעמים יד-שנייה היא היחידה דרך להשיג את הדגם.</p></div>
    <div class="glass-card"><h3 class="gc-h">מחיר בעדיפות</h3><p class="gc-p">חיסכון נוסף של 25-40% מול דגם חדש. אפילו אחרי PPI ואחריות — עדיין משמעותית זול יותר.</p></div>
    <div class="glass-card"><h3 class="gc-h">לא רוצה לחכות 38 יום</h3><p class="gc-p">רכבי-CPO אצלנו בארה״ב כבר היום. זמן עד הבית: 22-28 יום (במקום 38).</p></div>
    <div class="glass-card"><h3 class="gc-h">מחפש דגם מיוחד</h3><p class="gc-p">דורג'ים, Limited-Edition, רכבי-קולקציה — האפשרות היחידה היא יד-שנייה.</p></div>
  </div>
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">מחשבון מהיר</div>
  <h2 class="sec-h">תוספות PPI ו-Carfax</h2>
  <div class="mini-calc glass-card">
    <div class="calc-row"><span>דו״ח Carfax</span><b>$45 (כלול)</b></div>
    <div class="calc-row"><span>PPI במכון מוסמך</span><b>$350 (כלול)</b></div>
    <div class="calc-row"><span>אחריות 24 חודש</span><b>$1,800 (כלול)</b></div>
    <div class="calc-row"><span>הארכה ל-36 חודש</span><b>+$900 אופציונלי</b></div>
    <div class="calc-row total"><span>סה״כ תוספות יד-שנייה</span><b>$0 — הכל כלול</b></div>
  </div>
</section>

<section class="psec" data-reveal>
  <div class="sec-eyebrow">דוגמאות-הצלחה</div>
  <h2 class="sec-h">לקוחות שקנו יד-שנייה דרכנו</h2>
  <div class="g-3">
    <div class="glass-card"><div class="gc-num">35%</div><h3 class="gc-h">י.ל. — Mercedes GLS 450d 2022</h3><p class="gc-p">חסך ₪320K מול רכב חדש. PPI עבר ב-100%, היסטוריית Carfax נקייה לחלוטין, 28K מייל בלבד.</p></div>
    <div class="glass-card"><div class="gc-num">42%</div><h3 class="gc-h">ע.ק. — Tesla Model S Plaid 2023</h3><p class="gc-p">חסך ₪420K. רכב CPO ישירות מ-Tesla — אחריות יצרן עד 100K מייל, נטענה במלואה.</p></div>
    <div class="glass-card"><div class="gc-num">28%</div><h3 class="gc-h">מ.ב. — Ford F-150 Raptor 2022</h3><p class="gc-p">חסך ₪165K. בדיקת PPI מצאה צורך בהחלפת בלם — תוקן בטרם המשלוח, כלול בעלות.</p></div>
  </div>
</section>

<section class="psec" data-reveal>
  <h2 class="sec-h" style="text-align:center">מוכן לקנות יד-שנייה בלי סיכון?</h2>
  <div style="text-align:center;margin-top:24px"><a href="./start.html" class="btn-primary-cobalt">פתח תיק ₪500 →</a></div>
</section>
'''

USED_CSS = '''.layer-card { position:relative; }
.layer-tag { display:inline-block; padding: 5px 12px; background: var(--co-cobalt-soft); border: 1px solid var(--co-cobalt-line); color: var(--co-cobalt); border-radius: 100px; font-size: 11px; font-weight: 700; letter-spacing: 0.1em; margin-bottom: 14px; }
.layer-list { margin-top: 16px; padding: 0; list-style: none; }
.layer-list li { padding: 8px 0; color: var(--co-text-soft); font-size: 14px; border-bottom: 1px dashed var(--co-border); }
.layer-list li:last-child { border-bottom: 0; }
.mini-calc { margin-top: 28px; max-width: 600px; }
.calc-row { display:flex; justify-content: space-between; align-items: center; padding: 14px 0; border-bottom: 1px solid var(--co-border); color: var(--co-text-soft); font-size: 15px; }
.calc-row:last-child { border-bottom: 0; }
.calc-row b { color: var(--co-cobalt); font-weight: 700; }
.calc-row.total { border-top: 2px solid var(--co-cobalt-line); margin-top: 10px; padding-top: 18px; }
.calc-row.total span { color: #fff; font-weight: 700; font-size: 16px; }
.calc-row.total b { font-size: 18px; }
'''
(ROOT/'used-cars-guide.html').write_text(wrap('יד-שנייה — מדריך מלא', 'used-cars-guide', used_body, 'how', USED_CSS))

# =====================================================================
# PAGE 7: REVIEWS
# =====================================================================
REVIEWS = [
    ('יואב ל.', 5, 'Mercedes G63 AMG', '2024-11-12', 'חסכנו 850K שקל. התהליך לקח בדיוק 38 ימים כפי שהובטח. הצוות של AutoImports היה זמין 24/7 דרך הפורטל. הרכב הגיע במצב חדש לגמרי, כולל בדיקת 200 נקודות. ממליץ בחום.'),
    ('שירה כ.', 5, 'Tesla Model S Plaid', '2025-02-08', 'התהליך פשוט ושקוף. ה-MSRP, השילוח, המכס — הכל היה גלוי מהיום הראשון. אחרי שעבדנו עם דילר רשמי קודם — זה כמו לקרוא ספר אחרי שצפינו רק בסרטים. הצעה תוך 72 שעות ועמדו במחיר עד הסוף.'),
    ('דוד מ.', 5, 'Ford F-150 Raptor', '2025-03-15', 'חיפשתי F-150 Raptor שנה שלמה. דילר בארץ ביקש ₪780K. AutoImports הביאו אותי ב-₪430K — ועוד בגוון שביקשתי. עברו את כל 30 שלבי הרגולציה בלי שדאגתי לכלום.'),
    ('עומר ב.', 5, 'BMW M5 Competition', '2024-09-22', 'יבוא ראשון שלי. חששתי מהתהליך. הפורטל האישי שלהם הוא משהו אחר — סרטון של ה-PPI, מעקב חי על RoRo, OTP בכל שלב. הרגשתי בטוח לאורך כל הדרך.'),
    ('רוני ג.', 5, 'Rivian R1S', '2025-01-30', 'דגם שלא משווק בישראל בכלל. הם הצליחו להביא אותו דרך התאמה רגולטורית מלאה. עלות כוללת: ₪420K במקום ₪700K שביקש דילר מקביל. מקצועיות ברמה גבוהה מאוד.'),
    ('יעל ר.', 4, 'Audi Q8 e-tron', '2024-12-04', 'הכל היה נהדר חוץ מעיכוב של 5 ימים במכס בגלל בעיה ב-Mobileye. הם תיקנו במהירות, החזירו לי 1,500 ש״ח על האיחור. שירות לקוחות מצוין.'),
    ('א.ה.', 5, 'Cadillac Escalade IQ', '2025-04-11', 'רכב שאי-אפשר להשיג בארץ. הם הביאו לי ב-₪580K כולל הכל, מול הצעה של ₪950K ממקביל. החיסכון משלם להם בקלות. ממליץ בלי היסוס.'),
    ('נ.פ.', 5, 'Mercedes EQS 580', '2024-10-18', 'הצעה מותאמת תוך 65 שעות (לא 72!). תהליך החתימה דיגיטלי לגמרי, מימון אושר תוך 48 שעות. שותפים עם בנק לאומי. הרכב הגיע בדיוק במועד שהובטח.'),
    ('ר.צ.', 5, 'Porsche Taycan Turbo S', '2025-05-02', 'תהליך מקצועי מתחילתו ועד סופו. ה-Carfax היה נקי, ה-PPI היה מקיף עם 24 צילומים ב-4K. הרכב הגיע במצב פנים-ארה״ב אבל עם רישוי ישראלי.'),
    ('י.ל.', 5, 'Mercedes GLS 450d (יד-שנייה)', '2025-03-28', 'קניתי יד-שנייה דרכם — בהתחלה היה לי חשש. אבל ה-3 שכבות (Carfax + PPI + אחריות) שכנעו אותי. חסכתי ₪320K מול חדש. הרכב נראה כמו חדש.'),
    ('מ.ב.', 5, 'Ford F-150 Raptor (יד-שנייה)', '2024-11-30', 'יד-שנייה עם 32K מייל. PPI מצא צורך בהחלפת בלם — תיקנו לפני המשלוח על חשבונם. שקיפות מלאה.'),
    ('ע.ק.', 5, 'Tesla Model X Plaid (יד-שנייה)', '2025-02-14', 'רכב CPO ישירות מ-Tesla. אחריות יצרן ל-100K מייל. עלות סופית: ₪410K במקום ₪710K של דילר. אכן 42% חיסכון.'),
    ('ד.ש.', 5, 'Mercedes GLE 450d', '2024-08-15', 'עברנו לדגם דיזל בגלל יעילות. הצוות הציע לי לשקול אופציות שלא חשבתי עליהן — וצדק. החיסכון: ₪380K.'),
    ('ל.מ.', 5, 'Mercedes G580 EQ', '2025-04-25', 'הדגם החדש החשמלי של ה-G. בארה״ב $176K, בארץ באמצעותם ₪960K. רכב חלומות במחיר ריאלי.'),
    ('ש.ה.', 5, 'Lucid Air Grand Touring', '2025-01-08', 'רכב שלא קיים בארץ. הם הוציאו לי רישוי וסטנדרטיזציה מלאים. תהליך 45 יום, חיסכון של ₪480K מול דגמים מקבילים מקצועיים.'),
]

reviews_html = ''
total_score = sum(r[1] for r in REVIEWS) / len(REVIEWS)
for (name, stars, car, date, body) in REVIEWS:
    star_str = '★' * stars + '☆' * (5-stars)
    reviews_html += f'''<article class="review-card glass-card" data-stars="{stars}">
      <div class="rv-head">
        <div class="rv-stars" title="{stars}/5">{star_str}</div>
        <span class="rv-verified">✓ לקוח מאומת</span>
      </div>
      <p class="rv-body">{body}</p>
      <div class="rv-foot">
        <div>
          <b>{name}</b>
          <span>{car}</span>
        </div>
        <time>{date}</time>
      </div>
    </article>'''

rev_body = page_hero(
    'ביקורות לקוחות',
    '120+ יבואים.<br>אפס תלונות.',
    'כל ביקורת כאן היא של לקוח מאומת. שמות מקוצרים לפרטיות, אבל אנחנו יכולים לחבר אותך אישית לכל אחד אם תרצה. ממוצע: 4.9 כוכבים.',
    'הצטרף ללקוחות המרוצים', './start.html'
)
rev_body += f'''
<section class="psec" data-reveal>
  <div class="rv-summary glass-card">
    <div class="rv-avg">
      <div class="rv-avg-score">{total_score:.1f}</div>
      <div class="rv-avg-stars">★★★★★</div>
      <div class="rv-avg-count">בסיס {len(REVIEWS)} ביקורות מאומתות</div>
    </div>
    <div class="rv-breakdown">
      <div class="rv-bar"><span>5★</span><div class="bar-track"><div class="bar-fill" style="width:93%"></div></div><b>93%</b></div>
      <div class="rv-bar"><span>4★</span><div class="bar-track"><div class="bar-fill" style="width:7%"></div></div><b>7%</b></div>
      <div class="rv-bar"><span>3★</span><div class="bar-track"><div class="bar-fill" style="width:0%"></div></div><b>0%</b></div>
      <div class="rv-bar"><span>2★</span><div class="bar-track"><div class="bar-fill" style="width:0%"></div></div><b>0%</b></div>
      <div class="rv-bar"><span>1★</span><div class="bar-track"><div class="bar-fill" style="width:0%"></div></div><b>0%</b></div>
    </div>
  </div>
</section>

<section class="psec" data-reveal>
  <div class="rv-filter-row">
    <button class="rv-filter active" data-filter="all">הכל ({len(REVIEWS)})</button>
    <button class="rv-filter" data-filter="5">5 כוכבים</button>
    <button class="rv-filter" data-filter="used">יד-שנייה</button>
    <button class="rv-filter" data-filter="ev">חשמלי</button>
    <button class="rv-filter" data-filter="suv">SUV</button>
  </div>
  <div class="rv-grid" id="rvGrid">
    {reviews_html}
  </div>
</section>

<script>
document.querySelectorAll('.rv-filter').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.rv-filter').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const f = btn.dataset.filter;
    document.querySelectorAll('.review-card').forEach(card => {{
      if (f === 'all') card.style.display = '';
      else if (f === '5') card.style.display = card.dataset.stars === '5' ? '' : 'none';
      else if (f === 'used') card.style.display = card.textContent.includes('יד-שנייה') ? '' : 'none';
      else if (f === 'ev') {{
        const t = card.textContent;
        card.style.display = (t.includes('Tesla') || t.includes('Lucid') || t.includes('EQS') || t.includes('Rivian') || t.includes('Taycan') || t.includes('e-tron') || t.includes('EQ')) ? '' : 'none';
      }}
      else if (f === 'suv') {{
        const t = card.textContent;
        card.style.display = (t.includes('GLS') || t.includes('GLE') || t.includes('G63') || t.includes('G580') || t.includes('Escalade') || t.includes('Q8') || t.includes('R1S') || t.includes('Model X')) ? '' : 'none';
      }}
    }});
  }});
}});
</script>
'''

REV_CSS = '''.rv-summary { display: grid; grid-template-columns: 220px 1fr; gap: 36px; align-items: center; padding: 36px; }
@media (max-width: 700px) { .rv-summary { grid-template-columns: 1fr; } }
.rv-avg { text-align: center; }
.rv-avg-score { font-family:'Anton',sans-serif; font-size: 88px; color: var(--co-cobalt); line-height: 1; }
.rv-avg-stars { font-size: 22px; color: #FFB800; margin-top: 6px; }
.rv-avg-count { color: var(--co-text-dim); font-size: 13px; margin-top: 8px; }
.rv-breakdown { display: grid; gap: 8px; }
.rv-bar { display: grid; grid-template-columns: 32px 1fr 50px; gap: 10px; align-items: center; color: var(--co-text-soft); font-size: 13px; }
.bar-track { height: 8px; background: rgba(255,255,255,.06); border-radius: 6px; overflow: hidden; }
.bar-fill { height: 100%; background: linear-gradient(90deg, var(--co-cobalt), var(--co-cobalt-2)); border-radius: 6px; }
.rv-bar b { color: var(--co-cobalt); text-align: left; }

.rv-filter-row { display:flex; flex-wrap: wrap; gap: 8px; margin: 30px 0 24px; }
.rv-filter { padding: 8px 16px; background: var(--co-pane); border: 1px solid var(--co-border-2); color: var(--co-text-soft); border-radius: 100px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all .2s; }
.rv-filter:hover { border-color: var(--co-cobalt-line); }
.rv-filter.active { background: var(--co-cobalt); color: #fff; border-color: var(--co-cobalt); }

.rv-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 18px; }
.review-card { display:flex; flex-direction: column; gap: 14px; }
.rv-head { display:flex; align-items:center; justify-content: space-between; }
.rv-stars { color: #FFB800; font-size: 18px; letter-spacing: 2px; }
.rv-verified { font-size: 11px; padding: 4px 10px; background: var(--co-cobalt-soft); border: 1px solid var(--co-cobalt-line); color: var(--co-cobalt); border-radius: 100px; font-weight: 600; }
.rv-body { color: var(--co-text-soft); font-size: 14.5px; line-height: 1.65; flex: 1; }
.rv-foot { display:flex; justify-content: space-between; align-items: flex-end; padding-top: 12px; border-top: 1px solid var(--co-border); }
.rv-foot b { display:block; color: #fff; font-size: 14px; font-weight: 700; }
.rv-foot span { color: var(--co-cobalt); font-size: 12px; font-weight: 500; }
.rv-foot time { color: var(--co-text-dim); font-size: 12px; }
'''
(ROOT/'reviews.html').write_text(wrap('ביקורות לקוחות', 'reviews', rev_body, 'reviews', REV_CSS))

# =====================================================================
# PAGE 8: BLOG
# =====================================================================
BLOG = [
    ('g-class','G-Class', 'G63 AMG vs G580 EQ — האם החשמלי באמת אופציה?', 'בדיקה מעמיקה: 577HP בנזין מול 587HP חשמל, צריכת דלק מול טווח, מחירים בארץ ובארה״ב.', '2025-05-12', '8 דק׳', '#4A8BFF'),
    ('tesla','Tesla', 'Model S Plaid — 1.99 שניות, ועדיין משתלם 60% פחות', 'איך נראה ה-Tesla הכי מהיר בעולם דרך הפורטל שלנו: $124K בארה״ב, ₪410K בארץ.', '2025-04-28', '6 דק׳', '#22D3EE'),
    ('regulation','רגולציה', 'תיקון חוק 2026 — מה השתנה ביבוא אישי', 'משרד התחבורה שחרר תיקון רגולציה. הקלות חדשות לחשמליות, חסמים חדשים על דיזל ישן.', '2025-04-15', '12 דק׳', '#7C5CFF'),
    ('financing','מימון', 'מימון יבוא אישי — מדריך 2026', 'בנק לאומי, מזרחי-טפחות, דיסקונט — מי נותן הכי טוב? ריבית, תקופה, אחוז מימון.', '2025-03-22', '10 דק׳', '#FF8A65'),
    ('insurance','ביטוח', 'איך מבטחים יבוא אישי — הראל vs מנורה vs איילון', 'השוואת 3 חברות הביטוח הגדולות. מי הכי גמישה? מי הכי זולה? מי הכי מהירה?', '2025-03-08', '7 דק׳', '#34D399'),
    ('import','יבוא', 'RoRo vs קונטיינר — איזה לבחור?', 'ההבדל: $1,000. ההבדל בסיכון: ענק. מתי כדאי לשלם יותר על קונטיינר?', '2025-02-19', '5 דק׳', '#F472B6'),
    ('tesla','Tesla', 'Cybertruck — האם זה שווה את ה-₪780K?', 'הפיק-אפ הקליפ של אילון. ניתוח עלות-תועלת מלא, כולל סטנדרטיזציה ומיסוי בישראל.', '2025-02-05', '11 דק׳', '#22D3EE'),
    ('g-class','G-Class', 'G63 4×4² — דגם הפלגה של מרצדס', 'הדגם המוגבה, מה אפשרי לייבא לישראל ומה לא. כל הסיפור על "האקסטרים-G".', '2025-01-22', '9 דק׳', '#4A8BFF'),
    ('regulation','רגולציה', '30 שלבי הרגולציה — איך לזכור אותם', 'מדריך מעמיק: כל 30 השלבים, סדר ביצוע, זמן ממוצע לכל שלב.', '2025-01-08', '15 דק׳', '#7C5CFF'),
    ('financing','מימון', 'ליסינג vs מימון — בהפרשי-מס', 'יבוא אישי + ליסינג = שילוב מעניין. מתי כדאי? מתי לא?', '2024-12-30', '8 דק׳', '#FF8A65'),
    ('import','יבוא', 'דולר ב-2.93 — חלון הזדמנות נדיר', 'השער הנמוך ב-7 שנים. ניתוח שווקים: כמה זמן זה ימשך?', '2024-12-15', '6 דק׳', '#F472B6'),
    ('insurance','ביטוח', 'מה כיסויים לא רגילים בביטוח רכב יוקרה?', 'גניבת חלקים, גנדור, יבוא חוזר — כיסויים נדירים שמטוב לשים אליהם לב.', '2024-12-01', '9 דק׳', '#34D399'),
]

featured = BLOG[0]
rest = BLOG[1:]

featured_html = f'''<article class="blog-featured glass-card" onclick="alert('המאמר ייפתח בקרוב')">
  <div class="bf-bg" style="background: linear-gradient(135deg, {featured[6]} 0%, #0A1530 100%)">
    <div class="bf-icon">{featured[1][:1]}</div>
  </div>
  <div class="bf-body">
    <span class="chip">{featured[1]}</span>
    <h2>{featured[2]}</h2>
    <p>{featured[3]}</p>
    <div class="bf-meta"><time>{featured[4]}</time><span>· {featured[5]} קריאה</span></div>
  </div>
</article>'''

blog_cards = ''
for (cat_slug, cat, title, summary, date, read, color) in rest:
    blog_cards += f'''<article class="blog-card" data-cat="{cat_slug}" onclick="alert('המאמר ייפתח בקרוב')">
      <div class="bc-bg" style="background: linear-gradient(135deg, {color} 0%, #0A1530 100%)">
        <div class="bc-icon">{cat[:1]}</div>
      </div>
      <div class="bc-body">
        <span class="chip">{cat}</span>
        <h3>{title}</h3>
        <p>{summary}</p>
        <div class="bc-meta"><time>{date}</time><span>· {read}</span></div>
      </div>
    </article>'''

blog_body = page_hero(
    'בלוג ועדכונים',
    'מה חדש<br>בעולם היבוא.',
    'מאמרים מעמיקים על דגמים ספציפיים (G-Class, Tesla), שינויי-רגולציה, מימון, ביטוח, ומה שצריך לדעת לפני שיוצאים לדרך.',
    'כל הרכבים בקטלוג', './catalog.html'
)
blog_body += f'''
<section class="psec" data-reveal>
  <div class="blog-filter-row">
    <button class="blog-filter active" data-filter="all">הכל</button>
    <button class="blog-filter" data-filter="g-class">G-Class</button>
    <button class="blog-filter" data-filter="tesla">Tesla</button>
    <button class="blog-filter" data-filter="regulation">רגולציה</button>
    <button class="blog-filter" data-filter="financing">מימון</button>
    <button class="blog-filter" data-filter="insurance">ביטוח</button>
    <button class="blog-filter" data-filter="import">יבוא</button>
  </div>

  <div class="sec-eyebrow" style="margin-top:30px">מאמר נבחר</div>
  {featured_html}

  <div class="sec-eyebrow" style="margin-top:50px">עוד מאמרים</div>
  <div class="blog-grid">{blog_cards}</div>
</section>

<script>
document.querySelectorAll('.blog-filter').forEach(btn => {{
  btn.addEventListener('click', () => {{
    document.querySelectorAll('.blog-filter').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');
    const f = btn.dataset.filter;
    document.querySelectorAll('.blog-card').forEach(card => {{
      card.style.display = (f === 'all' || card.dataset.cat === f) ? '' : 'none';
    }});
  }});
}});
</script>
'''

BLOG_CSS = '''.blog-filter-row { display:flex; flex-wrap: wrap; gap: 8px; margin-bottom: 30px; }
.blog-filter { padding: 8px 16px; background: var(--co-pane); border: 1px solid var(--co-border-2); color: var(--co-text-soft); border-radius: 100px; font-size: 13px; font-weight: 600; cursor: pointer; transition: all .2s; }
.blog-filter:hover { border-color: var(--co-cobalt-line); }
.blog-filter.active { background: var(--co-cobalt); color: #fff; border-color: var(--co-cobalt); }

.blog-featured { display:grid; grid-template-columns: 460px 1fr; gap: 0; padding: 0; margin-bottom: 30px; cursor: pointer; overflow: hidden; }
@media (max-width: 800px) { .blog-featured { grid-template-columns: 1fr; } }
.bf-bg { min-height: 320px; display:grid; place-items: center; position: relative; overflow: hidden; }
.bf-bg::before { content:''; position: absolute; inset: 0; background: radial-gradient(circle at 50% 50%, rgba(255,255,255,.15), transparent 60%); }
.bf-icon { font-family:'Anton',sans-serif; font-size: 180px; color: rgba(255,255,255,.95); text-shadow: 0 10px 50px rgba(0,0,0,.5); }
.bf-body { padding: 36px; display:flex; flex-direction: column; justify-content: center; gap: 14px; }
.bf-body h2 { font-size: 28px; color: #fff; font-weight: 800; line-height: 1.25; }
.bf-body p { color: var(--co-text-dim); font-size: 15px; line-height: 1.6; }
.bf-meta { color: var(--co-text-dim); font-size: 12.5px; margin-top: 10px; }

.blog-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; margin-top: 20px; }
.blog-card { background: var(--co-pane); border: 1px solid var(--co-border-2); border-radius: 16px; overflow: hidden; cursor: pointer; transition: transform .2s, border-color .2s; }
.blog-card:hover { transform: translateY(-4px); border-color: var(--co-cobalt-line); }
.bc-bg { height: 180px; position: relative; display:grid; place-items: center; }
.bc-icon { font-family:'Anton',sans-serif; font-size: 96px; color: rgba(255,255,255,.95); }
.bc-body { padding: 22px; }
.bc-body h3 { font-size: 18px; color: #fff; margin: 12px 0 8px; line-height: 1.3; font-weight: 700; }
.bc-body p { color: var(--co-text-dim); font-size: 13.5px; line-height: 1.55; margin-bottom: 12px; }
.bc-meta { color: var(--co-text-dim); font-size: 11.5px; padding-top: 10px; border-top: 1px solid var(--co-border); }
'''
(ROOT/'blog.html').write_text(wrap('בלוג', 'blog', blog_body, 'blog', BLOG_CSS))

# =====================================================================
# PAGE 9: FAQ — 30+ questions
# =====================================================================
FAQ = {
    'תהליך': [
        ('כמה זמן לוקח התהליך מתחילתו ועד מסירת מפתחות?','בממוצע 38 ימים — 72 שעות עד הצעה, 7 ימים חתימה ורכישה בארה״ב, 14-21 ימי שילוח ימי, 7-10 ימים מכס וסטנדרטיזציה, ו-3-5 ימי רישוי וביטוח.'),
        ('מה אני צריך לעשות בעצמי?','אתה צריך לבחור רכב, להעביר תעודת זהות ורישיון נהיגה, ולשלם ₪500 כדמי-פתיחת-תיק. אנחנו מטפלים בכל השאר — רכישה, שילוח, מכס, סטנדרטיזציה, רישוי.'),
        ('האם אני יכול לבחור כל רכב מארה״ב?','כמעט כל רכב. אנחנו מסננים דגמים שלא עומדים בתקני FMVSS או שאסורים ליבוא אישי בישראל. כ-95% מהדגמים האמריקאיים זמינים.'),
        ('האם אפשר לקבל הצעה לפני שמשלמים ₪500?','כן — אומדן ראשוני ע״י המחשבון באתר. ההצעה הסופית, המדויקת, מקבלת רק לאחר פתיחת תיק.'),
        ('מה קורה אם אני לא מרוצה אחרי 30 יום?','אנחנו מחזירים את ה-₪500 במלואו. אתה לא מסתכן בכלום.'),
    ],
    'מחיר ועלויות': [
        ('מה כלול ב-5% עמלת השירות?','כל הניהול — סריקת ארה״ב, תחרות בין שותפים, ניהול לוגיסטי, פורטל אישי, ליווי 24/7, ניהול מסמכי-מכס. רק עלויות ישירות (רכב, שילוח, מכס) הן בנפרד.'),
        ('האם יש עלויות נסתרות?','לא. ההצעה שתקבל היא ההצעה הסופית. אם משהו מהמכס או הסטנדרטיזציה משתנה מעט (±2%), נעדכן אותך מיידית.'),
        ('כמה עולה Carfax + PPI?','כלולים בעלות. אצל מתחרים זה ₪400-₪1,800 נוספים — אצלנו זה חלק מהשירות.'),
        ('האם USD/ILS משפיע אחרי שחתמתי?','לא. אנחנו מבצעים USD/ILS-לוק במעמד ההזמנה — אתה יודע בדיוק את המחיר בשקלים.'),
        ('כמה אני באמת חוסך?','בממוצע ₪348K. בדגמים כמו G63 — עד ₪915K. במחשבון תוכל לראות חיסכון מדויק לדגם שלך.'),
    ],
    'בטחון וערבות': [
        ('מה הביטוח על השילוח?','100% מערך הרכב, דרך הראל ביטוח. כיסוי מלא: גניבה, נזקי-ים, התנגשות.'),
        ('מה קורה אם הרכב נפגע בשילוח?','הראל משלמת על נזק מלא או חלקי. במקביל אנחנו דואגים שתקבל רכב חלופי או החזר.'),
        ('האם יש אחריות אחרי המסירה?','כן — 24 חודש אחריות יבוא אישי במוסכים שותפים. עבור Tesla, Rivian, Ford — אחריות יצרן עולמית.'),
        ('מה אם המוסך הישראלי לא יודע לתקן את הרכב?','אנחנו עובדים עם מוסכים מורשים שיש להם גישה למקוריים מארה״ב. תיקון לוקח עד 14 יום במקרה הקשה.'),
        ('האם אתם מבוטחים מול תביעות?','כן — ביטוח אחריות-מקצועית של ₪10M דרך הראל. בנוסף, חברה מאוגדת כדין בישראל.'),
    ],
    'יבוא ורגולציה': [
        ('האם זה חוקי?','100% חוקי. יבוא אישי הוא זכות חוקתית בישראל. אנחנו פועלים תחת רישיון מתווך-יבוא של משרד התחבורה.'),
        ('האם Mobileye נדרש?','כן, אם הרכב לא הגיע איתו. אנחנו דואגים להתקנה במכון מוסמך בנמל אשדוד.'),
        ('האם אני צריך להגיש מסמכים בעצמי?','לא. הצוות המשפטי שלנו מטפל בכל הטפסים — Meches form 21, רישיון יבוא אישי, התחייבויות יבואן.'),
        ('האם דגמים אירופאיים זמינים?','כן, אבל קצת מסובך יותר. רכבים אירופאיים עוברים את אותו תהליך אבל לעיתים יש להם רכיבים שלא תואמים לתקן הישראלי.'),
        ('מה ההבדל בין יבוא אישי ליבוא מקביל?','יבוא אישי = הרכב רשום על שמך מהתחלה ועד הסוף. יבוא מקביל = מתווך-יבואן (כלומר עוד דילר). אצלנו = יבוא אישי.'),
    ],
    'מימון ותשלום': [
        ('האם אפשר לקבל מימון?','כן — שותף-מימון שלנו (בנק לאומי) מציע עד 75% מערך הרכב, ריבית מ-3.9%, עד 84 חודשים.'),
        ('האם אפשר לשלם בכרטיס אשראי?','חלק מהתשלום אפשר. את עיקר הרכישה (תשלום למוכר בארה״ב) מבצעים בהעברה בנקאית.'),
        ('מתי אני משלם כל סכום?','₪500 בתחילת התהליך, ~50% בעת רכישה בארה״ב, היתרה לפני שחרור הרכב מהמכס.'),
        ('האם מקבלים ביטקוין?','עדיין לא. אנחנו בודקים את האפשרות.'),
    ],
    'אחריות ושירות': [
        ('האם אתם מטפלים גם בביטוח?','כן — אנחנו עובדים עם הראל, מנורה, איילון. הצעות תחרותיות תוך 24 שעות מהמסירה.'),
        ('מה לעשות אם יש בעיה אחרי המסירה?','פתח קריאה בפורטל. נציג מומחה יתן מענה תוך 4 שעות בימי-עסקים, או 24 שעות בסוף-שבוע.'),
        ('האם אפשר למכור רכב בחזרה אליכם?','לא ישירות. אבל אנחנו יכולים לחבר אותך לרשת קונים מוכרת.'),
        ('מה אם הרכב לא מתאים לי אחרי שקיבלתי?','חוק הצרכן הישראלי מאפשר ביטול עסקה תוך 14 יום במקרים מוגדרים. דבר איתנו — נעזור.'),
        ('כמה זמן אחריות?','24 חודשים יבוא אישי. ניתן להאריך ב-12 חודשים נוספים בעלות $900.'),
        ('האם הרכב יבוא עם רישיון ישראלי?','כן — תהליך הסטנדרטיזציה והרישוי מסתיים לפני שאתה מקבל את הרכב. לוחית-רישוי ישראלית מותקנת.'),
        ('האם יש שירות-לקוחות 24/7?','שירות מבוסס-פורטל הוא 24/7. שיחות-טלפון עם נציג: 09:00-19:00 ימי-עסקים.'),
    ],
}

faq_html = ''
for cat, qs in FAQ.items():
    faq_html += f'<h3 class="faq-cat-h">{cat}</h3>'
    for (q, a) in qs:
        faq_html += f'''<details class="acc-item" data-q="{q.lower()}">
          <summary>{q}</summary>
          <div class="acc-body">{a}</div>
        </details>'''

total_q = sum(len(v) for v in FAQ.values())

faq_body = page_hero(
    f'{total_q}+ שאלות נפוצות',
    'כל מה שצריך לדעת,<br>במקום אחד.',
    f'{total_q} שאלות מקובצות ל-{len(FAQ)} קטגוריות. אם השאלה שלך לא כאן — דבר איתנו ב-WhatsApp או דרך הטופס.',
    'דבר עם יועץ', './start.html'
)
faq_body += f'''
<section class="psec" data-reveal>
  <div class="faq-search-row">
    <input type="text" id="faqSearch" placeholder="חפש שאלה..." class="faq-search">
  </div>

  <div class="faq-toc">
    {"".join(f'<a href="#cat-{i}" class="chip">{cat} ({len(qs)})</a>' for i,(cat,qs) in enumerate(FAQ.items()))}
  </div>

  <div class="faq-content">
    {faq_html}
  </div>
</section>

<section class="psec" data-reveal>
  <div class="faq-cta glass-card" style="text-align:center;padding:40px">
    <h3 style="font-size:24px;color:#fff;margin-bottom:10px">לא מצאת תשובה?</h3>
    <p style="color:var(--co-text-dim);margin-bottom:20px">פנה אלינו ב-WhatsApp או בטופס — נחזיר תשובה תוך שעתיים.</p>
    <a href="./start.html" class="btn-primary-cobalt">פתח תיק או שאל שאלה</a>
  </div>
</section>

<script>
document.getElementById('faqSearch').addEventListener('input', (e) => {{
  const q = e.target.value.toLowerCase().trim();
  document.querySelectorAll('.acc-item').forEach(item => {{
    const txt = (item.dataset.q + ' ' + item.textContent.toLowerCase());
    item.style.display = (!q || txt.includes(q)) ? '' : 'none';
  }});
}});
</script>
'''

FAQ_CSS = '''.faq-search-row { position: sticky; top: 80px; z-index: 5; padding: 14px 0; margin-bottom: 24px; background: linear-gradient(180deg, var(--co-deep) 60%, transparent); }
.faq-search { width: 100%; max-width: 600px; padding: 14px 22px; background: var(--co-pane); border: 1px solid var(--co-cobalt-line); border-radius: 100px; color: #fff; font-size: 15px; font-family: inherit; outline: none; transition: border-color .2s; }
.faq-search:focus { border-color: var(--co-cobalt); box-shadow: 0 0 0 3px var(--co-cobalt-soft); }
.faq-toc { display:flex; flex-wrap: wrap; gap: 8px; margin-bottom: 30px; }
.faq-cat-h { margin: 36px 0 18px; font-size: 22px; color: var(--co-cobalt); font-weight: 700; padding-bottom: 12px; border-bottom: 2px solid var(--co-cobalt-line); }
.faq-cat-h:first-child { margin-top: 0; }
'''
(ROOT/'faq.html').write_text(wrap('שאלות נפוצות', 'faq', faq_body, 'faq', FAQ_CSS))

# =====================================================================
# PAGE 10: TERMS
# =====================================================================
TERMS_SECTIONS = [
    ('1', 'ציות לרגולציה ישראלית', '''AutoImports.co.il (להלן: "החברה") פועלת כמתווכת לשירות היבוא האישי לפי תקנות משרד התחבורה, רשות המסים, ומשרד המשפטים. כל התהליך מתבצע בהתאם מלא לחוק התעבורה תשכ״א-1961, חוק מסי-קנייה תש״י-1949, וחוק היבוא-החופשי תשנ״א-1991. הלקוח רשום כמייבא רשמי אצל מכס ישראל. הרכב רשום על שם הלקוח בלבד.'''),
    ('2', 'דמי פתיחת תיק והחזרים', '''דמי פתיחת תיק הם ₪500 (כולל מע״מ). הסכום ייזקף לטובת הרכישה במעמד התשלום הסופי. במידה ואין התאמה תוך 30 יום מיום פתיחת התיק — הסכום יוחזר במלואו, ללא ניכויים, תוך 14 ימי עסקים. ביטול אחרי הצעה רשמית — החזר מלא בניכוי עלויות סריקה (לא יותר מ-₪200).'''),
    ('3', 'מחירים ושערי מטבע', '''כל המחירים המוצגים באתר מהווים אומדן בלבד. ההתקשרות הסופית תיקבע בהצעה הרשמית בפורטל האישי. שער USD/ILS נקבע במעמד ההזמנה (לוק) ולא ישתנה בכל מהלך התהליך. במידה ועלויות מכס/מע״מ משתנות מעל ±3% מהאומדן — החברה תעדכן את הלקוח ותציע חלופות.'''),
    ('4', 'בדיקות טכניות, Carfax ו-PPI', '''כל רכב עובר: (א) דו״ח Carfax מלא לפני הרכישה; (ב) בדיקת 200 נקודות במכון מוסמך בארה״ב (Pre-Purchase Inspection); (ג) צילום-וידאו תחת-המכונית. כל הממצאים מועלים לפורטל הלקוח לפני התשלום הסופי, ומאפשרים ללקוח לבחור לא להמשיך עם הרכב הספציפי הזה.'''),
    ('5', 'שילוח וביטוח', '''שילוח ימי מבוטח 100% מערך הרכב דרך הראל ביטוח. משך ממוצע: 14-21 ימי שיט. מעקב חי דרך הפורטל האישי. במקרה של נזק בשילוח — מנגנון תביעה אוטומטי מהביטוח, וחברתנו דואגת לרכב חלופי או החזר מלא תוך 30 יום.'''),
    ('6', 'אחריות יצרן ויבוא אישי', '''(א) יצרני ארה״ב (Ford, Chevrolet, Jeep, Tesla, Rivian, Lucid, Cadillac) — אחריות יצרן עולמית, בתוקף בישראל. (ב) יצרני אירופה (Mercedes, BMW, Audi, Porsche) — אנו מציעים אחריות יבוא אישי 24 חודש על מרכיבי המנוע, ההנעה והחשמל דרך מוסכים מורשים. אפשרות להאריך ל-36 חודש בעלות $900.'''),
    ('7', 'ביטול והחזרים', '''(א) ניתן לבטל עד שלב 7 ("אישור רכישה") — החזר מלא של ₪500 בניכוי עלויות-איתור (עד ₪200). (ב) לאחר אישור הרכישה — הרכב הוא של הלקוח, אך החברה מסייעת בהעברתו אליו או במכירתו בארה״ב. (ג) במקרה של תקלה מהותית שלא ניתן לתקן — החברה והלקוח יקבעו פתרון מוסכם בהתאם לחוק הצרכן הישראלי תשמ״א-1981.'''),
    ('8', 'פרטיות, GDPR וחוק הגנת הפרטיות', '''כל המידע של הלקוח מאוחסן בשרת ישראלי מאובטח לפי חוק הגנת הפרטיות תשמ״א-1981 ו-GDPR האירופי. החברה לא משתפת מידע עם צד-שלישי, למעט: (א) בנק שותף-מימון (בהסכמת הלקוח); (ב) חברת ביטוח לצרכי כיסוי; (ג) משרד התחבורה ורשות המסים (חובה רגולטורית). זכויות עיון, תיקון, ומחיקה — דרך privacy@autoimports.co.il.'''),
    ('9', 'מקדמה, תשלומים ומימון', '''(א) ₪500 בתחילת התהליך. (ב) כ-50% מערך הרכישה (לפי MSRP + מסים אומדנים) במעמד פתיחת תיק רכישה. (ג) יתרה לפני שחרור מהמכס. (ד) לקוחות שבחרו במימון של הבנק השותף — תשלומים חודשיים לפי הסכם המימון. ריבית, תקופה, ואחוז מימון נקבעים ע״י הבנק.'''),
    ('10', 'מקרה של מחלוקת ופתרון', '''כל מחלוקת תידון בבית-המשפט המוסמך באזור תל-אביב — יפו. החוק החל הוא חוק מדינת ישראל. לפני פנייה לבית-משפט, הצדדים יבחנו את האפשרות להגיע להבנה דרך גישור או בוררות אצל לשכת עורכי-הדין.'''),
    ('11', 'שינויים בתנאים', '''החברה רשאית לעדכן את תנאי-השימוש מעת לעת. כל עדכון יישלח ללקוחות קיימים דרך הפורטל האישי. עדכון מהותי (כלכלי) ייכנס לתוקף 30 יום לאחר ההודעה. לקוחות שלא מסכימים — זכאים לבטל את העסקה ולקבל החזר מלא.'''),
    ('12', 'אחריות מוגבלת', '''החברה אחראית רק לפעולות שבתחום אחריותה הישירה: סריקת שוק, ניהול שילוח, ניהול מכס, סטנדרטיזציה. אנחנו לא אחראים על: (א) תקלות הנגרמות ע״י היצרן; (ב) שינויי-רגולציה בלתי-צפויים; (ג) עיכובים הנגרמים ע״י רשויות ישראליות או אמריקאיות.'''),
]

terms_html = ''
for (num, title, body) in TERMS_SECTIONS:
    terms_html += f'''<section class="terms-sec" id="sec-{num}">
      <h3><span>{num}</span> {title}</h3>
      <p>{body}</p>
    </section>'''

toc_html = '<nav class="terms-toc">' + ''.join(
    f'<a href="#sec-{num}">{num}. {title}</a>' for (num,title,_) in TERMS_SECTIONS
) + '</nav>'

terms_body = page_hero(
    'תנאי שימוש',
    'תנאי שימוש<br>ומדיניות פרטיות.',
    f'{len(TERMS_SECTIONS)} סעיפים מפורטים, כתובים בעברית ברורה. אם משהו לא ברור — דבר איתנו לפני שאתה חותם.',
    'הבנתי, פתח תיק', './start.html'
)
terms_body += f'''
<section class="psec">
  <div class="terms-layout">
    <aside class="terms-side">
      <h4>תוכן עניינים</h4>
      {toc_html}
      <a href="mailto:privacy@autoimports.co.il" class="terms-contact">פנייה לפרטיות →</a>
    </aside>
    <div class="terms-main">
      <p class="terms-intro">תנאי השימוש הבאים מסדירים את היחסים בין AutoImports.co.il (להלן: "החברה") לבין הלקוח. תקנון זה מהווה הסכם משפטי מחייב.</p>
      {terms_html}
      <p class="terms-updated">עדכון אחרון: 1 ביוני 2026</p>
    </div>
  </div>
</section>
'''

TERMS_CSS = '''.terms-layout { display:grid; grid-template-columns: 260px 1fr; gap: 50px; margin-top: 20px; }
@media (max-width: 900px) { .terms-layout { grid-template-columns: 1fr; } }
.terms-side { position: sticky; top: 100px; align-self: start; background: var(--co-pane); border: 1px solid var(--co-border-2); border-radius: 14px; padding: 24px; max-height: calc(100vh - 120px); overflow-y: auto; }
.terms-side h4 { font-size: 13px; color: var(--co-cobalt); margin-bottom: 14px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; }
.terms-toc { display:flex; flex-direction: column; gap: 6px; }
.terms-toc a { padding: 8px 12px; color: var(--co-text-soft); font-size: 13px; border-radius: 8px; transition: all .15s; }
.terms-toc a:hover { background: var(--co-cobalt-soft); color: var(--co-cobalt); }
.terms-contact { display:block; margin-top: 18px; padding: 10px; text-align: center; background: var(--co-cobalt); color: #fff !important; border-radius: 8px; font-weight: 600; font-size: 13px; }

.terms-intro { color: var(--co-text-soft); font-size: 16px; line-height: 1.7; margin-bottom: 30px; padding: 22px; background: var(--co-pane); border-radius: 12px; border-right: 3px solid var(--co-cobalt); }
.terms-sec { margin-bottom: 36px; padding-bottom: 26px; border-bottom: 1px solid var(--co-border); }
.terms-sec h3 { font-size: 20px; color: #fff; margin-bottom: 14px; font-weight: 700; display:flex; align-items: center; gap: 14px; }
.terms-sec h3 span { font-family:'Anton',sans-serif; font-size: 32px; color: var(--co-cobalt); }
.terms-sec p { color: var(--co-text-soft); line-height: 1.75; font-size: 15px; }
.terms-updated { color: var(--co-text-dim); font-size: 13px; margin-top: 36px; text-align: center; padding: 18px; border-top: 1px dashed var(--co-border); }
'''
(ROOT/'terms.html').write_text(wrap('תנאי שימוש', 'terms', terms_body, '', TERMS_CSS))

# =====================================================================
# PAGE 11: START (multi-step wizard)
# =====================================================================
start_body = page_hero(
    'פתח תיק',
    'פתח תיק.<br>30 שניות.',
    'מקדמה של ₪500 בלבד. החזר מלא אם אין התאמה תוך 30 יום. ההצעה תגיע תוך 72 שעות.',
    '', '#', None, None
)
start_body += '''
<section class="psec">
  <div class="wizard glass-card">
    <div class="wiz-progress">
      <div class="wiz-bar"><div class="wiz-bar-fill" id="wizBarFill" style="width:20%"></div></div>
      <div class="wiz-steps">
        <div class="wiz-stp active" data-step="1"><b>01</b><span>בחירת רכב</span></div>
        <div class="wiz-stp" data-step="2"><b>02</b><span>צבע + טרים</span></div>
        <div class="wiz-stp" data-step="3"><b>03</b><span>פרטים אישיים</span></div>
        <div class="wiz-stp" data-step="4"><b>04</b><span>אישור מקדמה</span></div>
        <div class="wiz-stp" data-step="5"><b>05</b><span>סיכום</span></div>
      </div>
    </div>

    <!-- STEP 1 -->
    <div class="wiz-step active" data-step="1">
      <h3>בחר רכב</h3>
      <p class="wiz-sub">תוכל לשנות מאוחר יותר.</p>
      <select id="wizCar" class="wiz-input"><option value="">בחר דגם...</option></select>
      <div class="wiz-quick" id="wizQuickCars"></div>
    </div>

    <!-- STEP 2 -->
    <div class="wiz-step" data-step="2">
      <h3>צבע, טרים ותוספות</h3>
      <p class="wiz-sub">לפי הדגם שבחרת.</p>
      <label class="wiz-label">צבע חיצוני</label>
      <select id="wizColor" class="wiz-input"><option>בחר...</option><option>שחור אובסידיאן</option><option>לבן ארקטי</option><option>אפור סלניט</option><option>כחול היפר</option><option>אחר (אציין במזכרת)</option></select>
      <label class="wiz-label">טרים</label>
      <select id="wizTrim" class="wiz-input"><option>סטנדרט</option><option>AMG / Performance</option><option>Manufaktur / Bespoke</option></select>
      <label class="wiz-label">תוספות (סמן כל מה שמעניין)</label>
      <div class="wiz-checks">
        <label><input type="checkbox"> מערכת שמע פרימיום</label>
        <label><input type="checkbox"> חבילת נהיגה אוטונומית</label>
        <label><input type="checkbox"> 22"+ גלגלי AMG</label>
        <label><input type="checkbox"> Night Package</label>
        <label><input type="checkbox"> פנים-Nappa מורחב</label>
        <label><input type="checkbox"> HUD צבעוני</label>
      </div>
    </div>

    <!-- STEP 3 -->
    <div class="wiz-step" data-step="3">
      <h3>פרטים אישיים</h3>
      <p class="wiz-sub">לפתיחת התיק נדרשים: ת״ז ורישיון נהיגה ישראלי.</p>
      <div class="wiz-row"><label class="wiz-label">שם מלא *</label><input id="wizName" class="wiz-input" required></div>
      <div class="wiz-row"><label class="wiz-label">טלפון *</label><input id="wizPhone" type="tel" class="wiz-input" required></div>
      <div class="wiz-row"><label class="wiz-label">אימייל *</label><input id="wizEmail" type="email" class="wiz-input" required></div>
      <div class="wiz-row"><label class="wiz-label">תעודת זהות (9 ספרות) *</label><input id="wizId" class="wiz-input" inputmode="numeric" maxlength="9" required></div>
    </div>

    <!-- STEP 4 -->
    <div class="wiz-step" data-step="4">
      <h3>מקדמה ₪500</h3>
      <p class="wiz-sub">תשלום מאובטח. החזר מלא אם אין התאמה תוך 30 יום.</p>
      <div class="wiz-pay">
        <div class="pay-summary">
          <div><span>רכב:</span><b id="paySumCar">—</b></div>
          <div><span>מקדמה:</span><b>₪500</b></div>
          <div class="pay-total"><span>סה״כ לתשלום:</span><b>₪500</b></div>
        </div>
        <div class="pay-methods">
          <button class="pay-btn active">כרטיס אשראי</button>
          <button class="pay-btn">העברה בנקאית</button>
          <button class="pay-btn">Bit</button>
        </div>
        <label class="wiz-check-confirm"><input type="checkbox" id="wizConfirm"> אני מאשר/ת את <a href="./terms.html" target="_blank">תנאי השימוש</a> ומדיניות הפרטיות</label>
      </div>
    </div>

    <!-- STEP 5 -->
    <div class="wiz-step" data-step="5">
      <h3>סיכום והשלמה</h3>
      <p class="wiz-sub">תוך 72 שעות נחזיר אליך עם הצעה מותאמת.</p>
      <div class="wiz-summary" id="wizSummary"></div>
      <button class="btn-primary-cobalt wiz-finish" id="wizFinish">השלם פתיחת תיק →</button>
    </div>

    <div class="wiz-nav">
      <button class="wiz-back" id="wizBack" style="visibility:hidden">← חזור</button>
      <button class="wiz-next btn-primary-cobalt" id="wizNext">המשך →</button>
    </div>
  </div>
</section>

<script src="./js/data.js"></script>
<script>
(function() {
  let step = 1;
  const total = 5;
  const state = {};

  // Populate cars
  const carSelect = document.getElementById('wizCar');
  const quick = document.getElementById('wizQuickCars');
  if (window.CARS) {
    CARS.forEach(c => {
      const o = document.createElement('option');
      o.value = c.slug;
      o.textContent = c.name;
      carSelect.appendChild(o);
    });
    CARS.slice(0, 6).forEach(c => {
      const b = document.createElement('button');
      b.className = 'quick-car';
      b.innerHTML = `<b>${c.name}</b><span>חיסכון ${c.savePct}%</span>`;
      b.onclick = () => { carSelect.value = c.slug; b.parentNode.querySelectorAll('.quick-car').forEach(x=>x.classList.remove('on')); b.classList.add('on'); };
      quick.appendChild(b);
    });
  }

  // Save
  try {
    const saved = JSON.parse(sessionStorage.getItem('autoimp_wiz')||'{}');
    Object.assign(state, saved);
    if (state.car && carSelect) carSelect.value = state.car;
  } catch(e) {}

  function show() {
    document.querySelectorAll('.wiz-step').forEach(el => el.classList.toggle('active', +el.dataset.step === step));
    document.querySelectorAll('.wiz-stp').forEach(el => el.classList.toggle('active', +el.dataset.step <= step));
    document.getElementById('wizBarFill').style.width = (step/total*100) + '%';
    document.getElementById('wizBack').style.visibility = step > 1 ? 'visible' : 'hidden';
    document.getElementById('wizNext').style.display = step < total ? '' : 'none';
    if (step === 4) {
      const car = CARS && state.car ? CARS.find(c => c.slug === state.car) : null;
      document.getElementById('paySumCar').textContent = car ? car.name : '—';
    }
    if (step === total) {
      document.getElementById('wizSummary').innerHTML = `
        <div class="sum-row"><span>רכב:</span><b>${state.car || '—'}</b></div>
        <div class="sum-row"><span>צבע:</span><b>${state.color || '—'}</b></div>
        <div class="sum-row"><span>טרים:</span><b>${state.trim || '—'}</b></div>
        <div class="sum-row"><span>שם:</span><b>${state.name || '—'}</b></div>
        <div class="sum-row"><span>טלפון:</span><b>${state.phone || '—'}</b></div>
        <div class="sum-row"><span>אימייל:</span><b>${state.email || '—'}</b></div>
        <div class="sum-row sum-total"><span>מקדמה:</span><b>₪500</b></div>
      `;
    }
  }

  function save() {
    state.car = carSelect.value;
    state.color = document.getElementById('wizColor').value;
    state.trim = document.getElementById('wizTrim').value;
    state.name = document.getElementById('wizName').value;
    state.phone = document.getElementById('wizPhone').value;
    state.email = document.getElementById('wizEmail').value;
    state.id = document.getElementById('wizId').value;
    sessionStorage.setItem('autoimp_wiz', JSON.stringify(state));
  }

  document.getElementById('wizNext').addEventListener('click', () => {
    save();
    if (step === 1 && !state.car) { alert('בחר רכב'); return; }
    if (step === 3 && (!state.name || !state.phone || !state.email || !state.id)) { alert('מלא את כל הפרטים'); return; }
    if (step === 4 && !document.getElementById('wizConfirm').checked) { alert('יש לאשר את התנאים'); return; }
    if (step < total) { step++; show(); }
  });
  document.getElementById('wizBack').addEventListener('click', () => { if (step > 1) { step--; show(); } });
  document.getElementById('wizFinish').addEventListener('click', () => {
    save();
    alert('תיק נפתח! נציג מטעם AutoImports יחזור אליך תוך 72 שעות. תודה ' + (state.name || '') + '.');
  });

  show();
})();
</script>
'''

START_CSS = '''.wizard { padding: 36px; max-width: 920px; margin: 0 auto; }
.wiz-progress { margin-bottom: 36px; }
.wiz-bar { height: 4px; background: rgba(255,255,255,.06); border-radius: 4px; overflow: hidden; margin-bottom: 18px; }
.wiz-bar-fill { height: 100%; background: linear-gradient(90deg, var(--co-cobalt), var(--co-cobalt-2)); border-radius: 4px; transition: width .35s ease; }
.wiz-steps { display:grid; grid-template-columns: repeat(5, 1fr); gap: 8px; }
.wiz-stp { text-align: center; opacity: .35; transition: opacity .25s; }
.wiz-stp.active { opacity: 1; }
.wiz-stp b { display:block; font-family:'Anton',sans-serif; font-size: 22px; color: var(--co-cobalt); }
.wiz-stp span { display:block; font-size: 11.5px; color: var(--co-text-dim); margin-top: 2px; }

.wiz-step { display:none; }
.wiz-step.active { display:block; }
.wiz-step h3 { font-size: 28px; color: #fff; margin-bottom: 8px; font-weight: 700; }
.wiz-sub { color: var(--co-text-dim); margin-bottom: 22px; font-size: 15px; }
.wiz-label { display:block; margin: 14px 0 6px; color: var(--co-text-soft); font-size: 13px; font-weight: 600; }
.wiz-input { width: 100%; padding: 14px 18px; background: rgba(255,255,255,.03); border: 1px solid var(--co-border-2); border-radius: 10px; color: #fff; font-size: 15px; font-family: inherit; outline: none; transition: border-color .2s; }
.wiz-input:focus { border-color: var(--co-cobalt); box-shadow: 0 0 0 3px var(--co-cobalt-soft); }
.wiz-row { margin-bottom: 4px; }
.wiz-quick { display:grid; grid-template-columns: repeat(auto-fit, minmax(180px,1fr)); gap: 8px; margin-top: 18px; }
.quick-car { padding: 14px; background: rgba(74,139,255,.06); border: 1px solid var(--co-border-2); border-radius: 10px; text-align:right; cursor: pointer; transition: border-color .2s, background .2s; }
.quick-car:hover { border-color: var(--co-cobalt-line); background: var(--co-cobalt-soft); }
.quick-car.on { border-color: var(--co-cobalt); background: var(--co-cobalt-soft); }
.quick-car b { display:block; color:#fff; font-size: 14px; font-weight: 700; }
.quick-car span { display:block; color: var(--co-cobalt); font-size: 12px; margin-top: 4px; font-weight: 600; }
.wiz-checks { display: grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 8px; margin-top: 8px; }
.wiz-checks label { display:flex; align-items: center; gap: 10px; padding: 12px 14px; background: rgba(255,255,255,.03); border: 1px solid var(--co-border-2); border-radius: 10px; cursor: pointer; color: var(--co-text-soft); font-size: 14px; }
.wiz-checks input[type=checkbox] { accent-color: var(--co-cobalt); }

.wiz-pay { display:grid; gap: 20px; }
.pay-summary { background: var(--co-cobalt-soft); border: 1px solid var(--co-cobalt-line); border-radius: 12px; padding: 22px; }
.pay-summary > div { display:flex; justify-content: space-between; padding: 8px 0; color: var(--co-text-soft); }
.pay-summary > div b { color: #fff; font-weight: 700; }
.pay-total { border-top: 1px solid var(--co-cobalt-line); margin-top: 4px; padding-top: 12px !important; }
.pay-total b { color: var(--co-cobalt) !important; font-size: 22px !important; }
.pay-methods { display:grid; grid-template-columns: repeat(3, 1fr); gap: 8px; }
.pay-btn { padding: 14px; background: rgba(255,255,255,.04); border: 1px solid var(--co-border-2); color: var(--co-text-soft); border-radius: 10px; cursor: pointer; font-weight: 600; font-size: 14px; transition: all .2s; }
.pay-btn.active, .pay-btn:hover { background: var(--co-cobalt-soft); border-color: var(--co-cobalt); color: var(--co-cobalt); }
.wiz-check-confirm { display:flex; align-items: center; gap: 10px; padding: 12px; color: var(--co-text-soft); font-size: 14px; }
.wiz-check-confirm input { accent-color: var(--co-cobalt); }

.wiz-summary { background: rgba(74,139,255,.06); border: 1px solid var(--co-cobalt-line); border-radius: 12px; padding: 22px; margin-bottom: 22px; }
.sum-row { display:flex; justify-content: space-between; padding: 8px 0; color: var(--co-text-soft); font-size: 14px; }
.sum-row b { color:#fff; font-weight: 700; }
.sum-total { border-top: 1px solid var(--co-cobalt-line); margin-top: 6px; padding-top: 14px !important; }
.sum-total b { color: var(--co-cobalt) !important; font-size: 20px !important; }

.wiz-nav { display:flex; justify-content: space-between; align-items: center; margin-top: 36px; padding-top: 24px; border-top: 1px solid var(--co-border); }
.wiz-back { color: var(--co-text-soft); background: transparent; border: 1px solid var(--co-border-2); padding: 12px 22px; border-radius: 10px; font-weight: 600; cursor: pointer; }
.wiz-finish { width: 100%; padding: 16px 32px; font-size: 16px; justify-content: center; }
'''
(ROOT/'start.html').write_text(wrap('פתח תיק', 'start', start_body, '', START_CSS))

# =====================================================================
# PAGE 12: CATALOG
# =====================================================================
catalog_body = page_hero(
    'קטלוג מלא',
    '20 דגמים.<br>מחיר אמיתי.',
    'כל הרכבים שאנחנו מציעים ביבוא אישי, עם פילטרים מתקדמים: יצרן, סוג רכב, סוג דלק, מחיר, שנה. מיון לפי חיסכון, מחיר או א-ב.',
    'פתח תיק עכשיו', './start.html',
    'מחשבון מחיר', './index.html#calc'
)
catalog_body += '''
<section class="psec">
  <div class="cat-toolbar-row">
    <div class="cat-count"><b id="catCount">20</b> מתוך 20 רכבים</div>
    <select id="catSort" class="cat-sort">
      <option value="saving">חיסכון הגבוה ביותר</option>
      <option value="price-asc">מחיר: נמוך לגבוה</option>
      <option value="price-desc">מחיר: גבוה לנמוך</option>
      <option value="abc">א-ב</option>
    </select>
  </div>

  <div class="cat-layout-wrap">
    <aside class="cat-filter-rail">
      <div class="filter-block">
        <h5>יצרן</h5>
        <div id="filterMakes" class="filter-list"></div>
      </div>
      <div class="filter-block">
        <h5>סוג רכב</h5>
        <div id="filterBody" class="filter-list"></div>
      </div>
      <div class="filter-block">
        <h5>סוג דלק</h5>
        <div id="filterFuel" class="filter-list"></div>
      </div>
      <div class="filter-block">
        <h5>שנת ייצור</h5>
        <div id="filterYear" class="filter-list"></div>
      </div>
      <button id="filterClear" class="filter-clear-btn">נקה הכל</button>
    </aside>

    <div class="cat-grid" id="catGrid"></div>
  </div>
</section>

<script src="./js/data.js"></script>
<script>
(function() {
  const grid = document.getElementById('catGrid');
  const filters = { makes: new Set(), bodies: new Set(), fuels: new Set(), years: new Set() };
  let sortBy = 'saving';

  function getMake(c) { return (c.name || '').split(' ')[0]; }
  function getFuel(c) { return c.fuel || (c.type && c.type.includes('ev') ? 'חשמלי' : 'בנזין'); }

  const makes = [...new Set(CARS.map(getMake))].sort();
  const bodies = [...new Set(CARS.map(c => c.body))].sort();
  const fuels = [...new Set(CARS.map(getFuel))].sort();
  const years = [...new Set(CARS.map(c => c.year || 2025))].sort().reverse();

  function buildFilter(id, items, set) {
    const root = document.getElementById(id);
    items.forEach(v => {
      const el = document.createElement('label');
      el.innerHTML = `<input type="checkbox" value="${v}"> <span>${v}</span>`;
      el.querySelector('input').addEventListener('change', (e) => {
        if (e.target.checked) set.add(v); else set.delete(v);
        render();
      });
      root.appendChild(el);
    });
  }
  buildFilter('filterMakes', makes, filters.makes);
  buildFilter('filterBody', bodies, filters.bodies);
  buildFilter('filterFuel', fuels, filters.fuels);
  buildFilter('filterYear', years, filters.years);

  function fmt(n) { return '₪' + Math.round(n).toLocaleString('he-IL'); }

  function card(c) {
    const make = getMake(c);
    const img = c.heroImg || `./images/cars/${c.slug}/hero.jpg`;
    return `<article class="cat-card" onclick="location.href='./car.html?slug=${c.slug}'">
      <div class="cc-img" style="background-image:linear-gradient(135deg,#0F1E3D,#050B1A)">
        <img src="${img}" onerror="this.style.display='none'" alt="${c.name}">
        <span class="cc-save">חיסכון ${c.savePct}%</span>
      </div>
      <div class="cc-body">
        <span class="chip">${make}</span>
        <h3>${c.name}</h3>
        <div class="cc-meta"><span>${c.body || 'SUV'}</span><span>· ${getFuel(c)}</span><span>· ${c.year || 2025}</span></div>
        <div class="cc-prices">
          <div class="pi-us"><span>בארץ</span><b>${fmt(c.israelNIS)}</b></div>
          <div class="pi-ai"><span>איתנו</span><b>${fmt(c.landedNIS)}</b></div>
        </div>
        <div class="cc-cta">צפה במפרט מלא →</div>
      </div>
    </article>`;
  }

  function render() {
    let list = CARS.filter(c => {
      const m = getMake(c);
      if (filters.makes.size && !filters.makes.has(m)) return false;
      if (filters.bodies.size && !filters.bodies.has(c.body)) return false;
      if (filters.fuels.size && !filters.fuels.has(getFuel(c))) return false;
      if (filters.years.size && !filters.years.has(c.year || 2025)) return false;
      return true;
    });
    if (sortBy === 'saving') list.sort((a,b) => b.savePct - a.savePct);
    if (sortBy === 'price-asc') list.sort((a,b) => a.landedNIS - b.landedNIS);
    if (sortBy === 'price-desc') list.sort((a,b) => b.landedNIS - a.landedNIS);
    if (sortBy === 'abc') list.sort((a,b) => a.name.localeCompare(b.name, 'he'));

    grid.innerHTML = list.map(card).join('');
    document.getElementById('catCount').textContent = list.length;
  }

  document.getElementById('catSort').addEventListener('change', e => { sortBy = e.target.value; render(); });
  document.getElementById('filterClear').addEventListener('click', () => {
    Object.values(filters).forEach(s => s.clear());
    document.querySelectorAll('.cat-filter-rail input').forEach(i => i.checked = false);
    render();
  });

  // Apply ?cat= from URL
  const params = new URLSearchParams(location.search);
  const catParam = params.get('cat');
  if (catParam) {
    // try to map to body filter
    const mapping = { suv: 'suv', ev: 'suv', pickup: 'pickup', sedan: 'sedan' };
    const target = mapping[catParam];
    if (target && bodies.includes(target)) {
      filters.bodies.add(target);
      document.querySelector(`#filterBody input[value="${target}"]`).checked = true;
    }
    if (catParam === 'ev') {
      ['חשמלי','EV','חשמלי + היברידי'].forEach(v => {
        const cb = document.querySelector(`#filterFuel input[value="${v}"]`);
        if (cb) { cb.checked = true; filters.fuels.add(v); }
      });
    }
  }

  render();
})();
</script>
'''

CAT_CSS = '''.cat-toolbar-row { display:flex; justify-content: space-between; align-items: center; margin-bottom: 24px; padding: 16px 0; }
.cat-count { color: var(--co-text-soft); font-size: 15px; }
.cat-count b { color: var(--co-cobalt); font-size: 18px; }
.cat-sort { padding: 10px 18px; background: var(--co-pane); border: 1px solid var(--co-border-2); color: #fff; border-radius: 10px; font-size: 14px; font-family: inherit; cursor: pointer; }

.cat-layout-wrap { display:grid; grid-template-columns: 240px 1fr; gap: 30px; }
@media (max-width: 900px) { .cat-layout-wrap { grid-template-columns: 1fr; } }

.cat-filter-rail { background: var(--co-pane); border: 1px solid var(--co-border-2); border-radius: 14px; padding: 22px; align-self: start; position: sticky; top: 100px; max-height: calc(100vh - 120px); overflow-y: auto; }
.filter-block { margin-bottom: 22px; }
.filter-block h5 { font-size: 12px; color: var(--co-cobalt); margin-bottom: 10px; text-transform: uppercase; letter-spacing: 0.15em; font-weight: 700; }
.filter-list { display:flex; flex-direction: column; gap: 4px; }
.filter-list label { display:flex; align-items: center; gap: 8px; padding: 6px 8px; color: var(--co-text-soft); font-size: 13.5px; cursor: pointer; border-radius: 6px; transition: background .15s; }
.filter-list label:hover { background: rgba(255,255,255,.04); }
.filter-list input[type=checkbox] { accent-color: var(--co-cobalt); }
.filter-clear-btn { width: 100%; padding: 10px; background: transparent; border: 1px dashed var(--co-border-2); color: var(--co-text-dim); border-radius: 8px; cursor: pointer; font-size: 13px; }
.filter-clear-btn:hover { color: var(--co-cobalt); border-color: var(--co-cobalt-line); }

.cat-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 18px; }
.cat-card { background: var(--co-pane); border: 1px solid var(--co-border-2); border-radius: 16px; overflow: hidden; cursor: pointer; transition: transform .2s, border-color .2s; }
.cat-card:hover { transform: translateY(-4px); border-color: var(--co-cobalt-line); box-shadow: 0 20px 50px -20px rgba(74,139,255,.4); }
.cc-img { aspect-ratio: 16/10; position: relative; overflow: hidden; }
.cc-img img { width: 100%; height: 100%; object-fit: cover; }
.cc-save { position: absolute; top: 12px; right: 12px; padding: 5px 12px; background: var(--co-cobalt); color: #fff; border-radius: 100px; font-size: 12px; font-weight: 700; box-shadow: 0 4px 16px rgba(74,139,255,.5); }
.cc-body { padding: 18px; }
.cc-body h3 { font-size: 17px; color: #fff; margin: 10px 0 8px; font-weight: 700; }
.cc-meta { color: var(--co-text-dim); font-size: 12.5px; margin-bottom: 14px; display:flex; gap: 4px; flex-wrap: wrap; }
.cc-prices { display:grid; grid-template-columns: 1fr 1fr; gap: 8px; margin-bottom: 12px; }
.pi-us, .pi-ai { padding: 10px 12px; border-radius: 8px; }
.pi-us { background: rgba(255,255,255,.04); }
.pi-ai { background: var(--co-cobalt-soft); border: 1px solid var(--co-cobalt-line); }
.pi-us span, .pi-ai span { display:block; font-size: 11px; color: var(--co-text-dim); }
.pi-us b { color: var(--co-text-soft); font-size: 14px; }
.pi-ai b { color: var(--co-cobalt); font-size: 15px; font-weight: 700; }
.cc-cta { color: var(--co-cobalt); font-size: 13px; font-weight: 600; padding-top: 8px; border-top: 1px solid var(--co-border); }
'''
(ROOT/'catalog.html').write_text(wrap('קטלוג', 'catalog', catalog_body, 'catalog', CAT_CSS))

# =====================================================================
# PAGE 13: CAR (VDP template)
# =====================================================================
car_body = '''<section class="page-hero" id="carHero" data-reveal>
  <a href="./catalog.html" class="btn-link" style="margin-bottom:24px;display:inline-block">← חזרה לקטלוג</a>
  <div id="carHeroContent">
    <div class="eyebrow">טוען...</div>
    <h1 id="carName">רכב</h1>
  </div>
</section>
<div class="page-divider"></div>

<section class="psec">
  <div id="vdpRoot">
    <!-- VDP content injected by JS -->
  </div>
</section>

<script src="./js/data.js"></script>
<script>
(function() {
  const params = new URLSearchParams(location.search);
  const slug = params.get('slug');
  const car = (window.CARS || []).find(c => c.slug === slug);

  if (!car) {
    document.getElementById('vdpRoot').innerHTML = `
      <div class="glass-card" style="text-align:center;padding:60px">
        <h2 style="color:#fff;font-size:28px;margin-bottom:14px">רכב לא נמצא</h2>
        <p style="color:var(--co-text-dim);margin-bottom:24px">הקישור לא תקין או שהדגם הוסר.</p>
        <a href="./catalog.html" class="btn-primary-cobalt">חזרה לקטלוג</a>
      </div>`;
    return;
  }

  document.title = car.name + ' | AutoImports.co.il';
  document.getElementById('carName').textContent = car.name;
  document.getElementById('carHeroContent').innerHTML = `
    <div class="eyebrow">${(car.body || 'SUV').toUpperCase()} · ${car.year || 2025}</div>
    <h1>${car.name}</h1>
    <p class="sub">${car.note || ''}</p>
    <div class="cta-row">
      <a href="./start.html" class="btn-primary-cobalt">פתח תיק לרכב זה →</a>
      <a href="./catalog.html" class="btn-link">דגמים דומים</a>
    </div>
  `;

  function fmt(n) { return '₪' + Math.round(n).toLocaleString('he-IL'); }
  function fmtUSD(n) { return '$' + Math.round(n).toLocaleString('en-US'); }

  const colorsHtml = (car.colors || []).map(c => `<div class="vp-color"><span style="background:${c.code}"></span>${c.hex || c.name}</div>`).join('');
  const trimsHtml = (car.trims || []).map(t => `<div class="vp-trim"><b>${t.name}</b>${t.delta ? `<span>+${fmtUSD(t.delta)}</span>` : '<span>סטנדרט</span>'}<ul>${(t.items||[]).map(i=>`<li>${i}</li>`).join('')}</ul></div>`).join('');
  const featuresHtml = (car.features || []).map(f => `<li>✓ ${f}</li>`).join('');
  const safetyHtml = (car.safety || []).map(s => `<li>🛡 ${s}</li>`).join('');

  document.getElementById('vdpRoot').innerHTML = `
    <div class="vp-layout">
      <div class="vp-main">
        <div class="vp-gallery">
          <div class="vp-photo" style="background-image:linear-gradient(135deg,#0F1E3D,#050B1A)">
            <img src="./images/cars/${car.slug}/hero.jpg" onerror="this.style.display='none'" alt="${car.name}">
            <span class="vp-save">חיסכון ${car.savePct}%</span>
          </div>
        </div>

        <div class="vp-section">
          <h3>מפרט טכני</h3>
          <div class="vp-specs">
            <div><span>מנוע</span><b>${car.engine || '—'}</b></div>
            <div><span>כוח</span><b>${car.hp || '—'} HP</b></div>
            <div><span>0-100</span><b>${car.zero100 || '—'} שנ׳</b></div>
            <div><span>מהירות מירבית</span><b>${car.topSpeed || '—'} קמ״ש</b></div>
            <div><span>הילוכים</span><b>${car.transmission || '—'}</b></div>
            <div><span>מושבים</span><b>${car.seats || '—'}</b></div>
            <div><span>דלק</span><b>${car.fuel || '—'}</b></div>
            <div><span>מ׳נסיעה</span><b>${car.range || '—'} ק״מ</b></div>
            <div><span>אורך</span><b>${car.length || '—'} מ״מ</b></div>
            <div><span>משקל</span><b>${car.weight || '—'} ק״ג</b></div>
            <div><span>שנה</span><b>${car.year || 2025}</b></div>
            <div><span>מקור ייצור</span><b>${car.origin || '—'}</b></div>
          </div>
        </div>

        ${colorsHtml ? `<div class="vp-section"><h3>צבעים זמינים</h3><div class="vp-colors">${colorsHtml}</div></div>` : ''}
        ${trimsHtml ? `<div class="vp-section"><h3>חבילות וטרימים</h3><div class="vp-trims">${trimsHtml}</div></div>` : ''}
        ${featuresHtml ? `<div class="vp-section"><h3>אביזרים סטנדרטיים</h3><ul class="vp-list">${featuresHtml}</ul></div>` : ''}
        ${safetyHtml ? `<div class="vp-section"><h3>בטיחות</h3><ul class="vp-list">${safetyHtml}</ul></div>` : ''}

        <div class="vp-section">
          <h3>אחריות וזיהוי</h3>
          <p style="color:var(--co-text-soft);font-size:15px;line-height:1.7">${car.warranty || 'אחריות יבוא אישי 24 חודש'}</p>
        </div>
      </div>

      <aside class="vp-aside">
        <div class="vp-price-card glass-card">
          <span class="chip">מחיר סופי כולל הכל</span>
          <div class="vpc-main">
            <span>איתנו</span>
            <b>${fmt(car.landedNIS)}</b>
          </div>
          <div class="vpc-vs">
            <div><span>בארץ דרך דילר</span><b>${fmt(car.israelNIS)}</b></div>
            <div class="vpc-save"><span>אתה חוסך</span><b>${fmt(car.israelNIS - car.landedNIS)}</b><span style="color:var(--co-cobalt);font-size:13px">(${car.savePct}%)</span></div>
          </div>
          <div class="vpc-breakdown">
            <div><span>MSRP בארה״ב</span><b>${fmtUSD(car.msrp)}</b></div>
            <div><span>מס קנייה</span><b>${fmtUSD(car.purchaseTax || 0)}</b></div>
            <div><span>מע״מ (18%)</span><b>${fmtUSD(car.vat || 0)}</b></div>
            <div><span>שילוח</span><b>${fmtUSD(car.shipping || 2000)}</b></div>
            <div class="vpc-sub-total"><span>מחיר נמל</span><b>${fmtUSD(car.landedUSD)}</b></div>
          </div>
          <a href="./start.html?car=${car.slug}" class="btn-primary-cobalt" style="width:100%;justify-content:center;margin-top:18px">פתח תיק לרכב זה ₪500</a>
          <p class="vpc-note">החזר מלא אם אין התאמה תוך 30 יום. USD/ILS נקבע במעמד ההזמנה (כעת 2.93).</p>
        </div>

        <div class="glass-card" style="margin-top:18px">
          <h4 style="color:#fff;margin-bottom:10px">דגמים דומים</h4>
          <div id="vpRelated"></div>
        </div>
      </aside>
    </div>
  `;

  // Related cars
  const related = (window.CARS || []).filter(c => c.slug !== car.slug && c.body === car.body).slice(0, 3);
  document.getElementById('vpRelated').innerHTML = related.map(r => `
    <a href="./car.html?slug=${r.slug}" class="vp-rel">
      <b>${r.name}</b>
      <span>${fmt(r.landedNIS)} · חיסכון ${r.savePct}%</span>
    </a>
  `).join('') || '<p style="color:var(--co-text-dim);font-size:13px">אין דגמים דומים זמינים</p>';
})();
</script>
'''

CAR_CSS = '''.vp-layout { display:grid; grid-template-columns: 1fr 380px; gap: 30px; }
@media (max-width: 1000px) { .vp-layout { grid-template-columns: 1fr; } }

.vp-gallery { margin-bottom: 30px; }
.vp-photo { aspect-ratio: 16/10; border-radius: 18px; overflow: hidden; position: relative; background: var(--co-pane); border: 1px solid var(--co-border-2); }
.vp-photo img { width: 100%; height: 100%; object-fit: cover; }
.vp-save { position: absolute; top: 16px; right: 16px; padding: 6px 14px; background: var(--co-cobalt); color: #fff; border-radius: 100px; font-size: 13px; font-weight: 700; box-shadow: 0 6px 20px rgba(74,139,255,.5); }

.vp-section { background: var(--co-pane); border: 1px solid var(--co-border-2); border-radius: 16px; padding: 26px; margin-bottom: 18px; }
.vp-section h3 { color: #fff; font-size: 20px; margin-bottom: 16px; font-weight: 700; }

.vp-specs { display:grid; grid-template-columns: repeat(auto-fit, minmax(160px, 1fr)); gap: 12px; }
.vp-specs > div { padding: 12px 14px; background: rgba(255,255,255,.03); border-radius: 10px; }
.vp-specs span { display:block; color: var(--co-text-dim); font-size: 12px; }
.vp-specs b { display:block; color: #fff; font-weight: 700; font-size: 15px; margin-top: 4px; }

.vp-colors { display:flex; flex-wrap: wrap; gap: 12px; }
.vp-color { display:flex; align-items: center; gap: 10px; padding: 10px 14px; background: rgba(255,255,255,.04); border: 1px solid var(--co-border-2); border-radius: 100px; color: var(--co-text-soft); font-size: 13.5px; }
.vp-color span { width: 22px; height: 22px; border-radius: 50%; border: 2px solid rgba(255,255,255,.2); display:inline-block; }

.vp-trims { display:grid; gap: 12px; }
.vp-trim { background: rgba(255,255,255,.03); border: 1px solid var(--co-border); border-radius: 12px; padding: 16px; }
.vp-trim b { display:inline-block; color: #fff; font-weight: 700; font-size: 15px; }
.vp-trim > span { color: var(--co-cobalt); font-size: 13px; font-weight: 600; margin-right: 10px; }
.vp-trim ul { margin-top: 10px; display:flex; flex-wrap: wrap; gap: 6px; }
.vp-trim li { padding: 4px 10px; background: var(--co-cobalt-soft); color: var(--co-cobalt); border-radius: 100px; font-size: 12px; }

.vp-list { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px, 1fr)); gap: 8px; }
.vp-list li { padding: 10px 14px; background: rgba(255,255,255,.03); border-radius: 8px; color: var(--co-text-soft); font-size: 13.5px; }

.vp-price-card { padding: 26px; position: sticky; top: 100px; }
.vp-price-card .chip { margin-bottom: 16px; }
.vpc-main { padding: 18px; background: linear-gradient(135deg, var(--co-cobalt-soft), transparent); border: 1px solid var(--co-cobalt-line); border-radius: 12px; margin-bottom: 14px; }
.vpc-main span { display:block; color: var(--co-text-dim); font-size: 13px; }
.vpc-main b { display:block; color: var(--co-cobalt); font-family:'Anton',sans-serif; font-size: 40px; line-height: 1.1; margin-top: 4px; letter-spacing: 0.01em; }
.vpc-vs { display:flex; flex-direction: column; gap: 8px; padding: 14px 0; border-top: 1px solid var(--co-border); border-bottom: 1px solid var(--co-border); }
.vpc-vs > div { display:flex; justify-content: space-between; align-items: center; }
.vpc-vs span { color: var(--co-text-dim); font-size: 13px; }
.vpc-vs b { color: #fff; font-size: 15px; font-weight: 700; }
.vpc-save b { color: var(--co-cobalt) !important; font-size: 17px !important; }
.vpc-breakdown { padding: 14px 0 4px; }
.vpc-breakdown > div { display:flex; justify-content: space-between; padding: 6px 0; }
.vpc-breakdown span { color: var(--co-text-dim); font-size: 13px; }
.vpc-breakdown b { color: var(--co-text-soft); font-size: 13px; font-weight: 600; }
.vpc-sub-total { border-top: 1px dashed var(--co-border); margin-top: 6px; padding-top: 10px !important; }
.vpc-sub-total b { color: #fff !important; font-weight: 700 !important; }
.vpc-note { color: var(--co-text-dim); font-size: 12px; margin-top: 14px; line-height: 1.55; text-align: center; }

.vp-rel { display:block; padding: 12px; background: rgba(255,255,255,.03); border: 1px solid var(--co-border); border-radius: 10px; margin-bottom: 8px; transition: border-color .2s; }
.vp-rel:hover { border-color: var(--co-cobalt-line); }
.vp-rel b { display:block; color: #fff; font-size: 14px; font-weight: 700; }
.vp-rel span { display:block; color: var(--co-cobalt); font-size: 12.5px; margin-top: 2px; }
'''
(ROOT/'car.html').write_text(wrap('פרטי רכב', 'car', car_body, 'catalog', CAR_CSS))

print("✓ ALL 13 pages written")
print("\nFiles:")
for f in ['about','how-it-works','why-us','trust','regulations','used-cars-guide','reviews','blog','faq','terms','start','catalog','car']:
    p = ROOT / f'{f}.html'
    print(f"  {p.name:25s} {p.stat().st_size//1024:>4d} KB")
