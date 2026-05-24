# AutoImports.co.il (GITA) — Audit Report
**תאריך**: 23 May 2026
**שופטים**: McKinsey ex-CMO + Awwwards Senior Judge
**URL חי**: https://gitteromri-ux.github.io/gita-cars/
**מקור-אמת**: `website-auto-8.xlsx` + `MESSAGING_BIBLE.md`
**מתודולוגיה**: Screenshot desktop + mobile (390px) + HTML/CSS/JS audit + 8-tab Excel cross-check + competitor benchmark (Cadillac, Audi, Tesla, Porsche, Lucid, Rivian).

> **TL;DR**: ציון סופי **6.4/10**. זה NOT אתר #1 בעולם. הקונספט והמודל יוצאי-דופן (78% חיסכון, 72h הצעה, 5% עמלת-שירות), אבל ה-Hero מתרסק (אין H1 גלוי בלי המתנה לאנימציה, לא כל הקופי מה-Messaging Bible מופיע, יש brand-confusion בין `AutoImports.co.il` ל-`GITA`/`GITA-CARS`), חוסר Social Proof אמיתי, וחוסר Advisory Board עם פנים אמיתיות. הפוטנציאל ל-Awwwards SOTD (8.0+) הוא מציאותי תוך 72 שעות עבודה ממוקדת.

---

## Part 1 — McKinsey Audit (ex-CMO Lens)

### 1.1 בהירות מסר — **5.5 / 10**

**ממצאים**:
- **ה-Hero מתרסק**: בצילום המסך הראשון (Desktop, אחרי טעינה) רואים רק תמונת רכב (Mercedes G580 EQ) + לוגו GITA. אין H1 גלוי, אין eyebrow, אין sub-headline, אין CTA. המילה "יבוא" לא מופיעה לפני שגוללים. המסר המשפיע "כל רכב מארה״ב. במחיר נמוך מבישראל. תוך 72 שעות הצעה" — קיים בקוד (`js/folds/hero.js:172-176`), אך מוסתר מאחורי `animation-delay` של 600ms + char-stagger של ~22ms/char × 50+ תווים = **כ-1.7-2 שניות** עד שה-H1 מופיע במלואו. ב-LCP זה אסון.
- **Brand identity מבולבל**: ה-task מדבר על "AutoImports.co.il", ה-Footer ומטה ה-Title אומרים "GITA — יבוא רכבי יוקרה מארה״ב", הלוגו הוא "G/GITA", ובצילום ישן קוראים לעצמם "GITA-CARS". לקוח לא יודע איך לקרוא לחברה.
- ה-CTA הראשי "פתח תיק ₪500" — חזק. ברור. ייחודי (לא "צור קשר").
- ה-Differentiation מהמתחרים (יבואנים רגילים): ברור — "אנחנו לא יבואן, אנחנו מתחרים בין יבואנים אמריקאים". אבל זה לא מוקרן ב-Above-the-fold.
- **5 שניות test**: כשל. גולש רואה רק רכב יפה ולוגו G. צריך לגלול כדי להבין מה האתר עושה.

**פעולה**: שנה את ה-Hero לטעינה **מיידית** של ה-H1 (`opacity:1; animation: none` ל-`.h-headline` ב-first paint, ואז fade-up עדין רק על קישוטים). הצג את ה-3 שורות במקום הצמצום הזה: `כל רכב מארה״ב.` / `במחיר נמוך מבישראל.` / `תוך 72 שעות הצעה.` — חייב להיראות ב-LCP < 1.5s. **החליטו על שם אחד** — אם זה AutoImports.co.il, החלף את GITA בכל מקום בלוגו, ב-Title, ב-Footer, ב-OG tags.

---

### 1.2 חוזק הצעת-ערך — **7.5 / 10**

**ממצאים**:
- ה-Hook הוא **חזק במיוחד** ברגע שמגלים אותו: "G63 בארה״ב $185K → בישראל ₪2.1M. אנחנו מביאים אותו ב-₪1.18M = חיסכון 78%". זה McKinsey-class storytelling — מספר עצום + השוואה קונקרטית.
- **5 הוכחות-ערך מה-Bible** (תחרות בין שותפים / שקיפות 5% / 72 שעות / 78% / עד-הבית) — חלקן מופיעות בטריוויאלי (`trust-bar`: 348K, 72h, 8-12 שבועות, 100% החזר) אבל לא במבנה שיווקי-משכנע.
- ה-`לוח דילים חי` (`#board`) עם 10 השוואות + ticker — **חזק מאוד**. זו מטאפורה מקורית של בורסה לעולם רכב. אבל ה-headline שלו "פערי המחירים הגדולים..." רכרוכי. צריך לכתוב כמו וול-סטריט: `"שורט על היבואנים: דילים הכי חמים שלנו"` או `"לוח דילים חי · עודכן עכשיו · עד 159% חיסכון"`.
- **Social Proof — חסר אמיתי**: "120+ לקוחות, 4.9★, אפס תלונות" — אבל אין שמות-לקוחות, אין תמונות, אין case-studies. זה stat-claim ללא הוכחה. מקצוען-לוקח-לקוחות-פרימיום לא יבטח רכב של ₪2M בלי לראות פנים.

**פעולה**: הוסף **3 case-studies קונקרטיות** עם תמונת-לקוח (גם אם stock), שם, רכב שהביא, וציטוט: "הביאו לי G580 EQ ב-₪1.18M. היבואן הרשמי ביקש ₪1.7M. לא האמנתי עד שראיתי את הרכב מול הבית." — זה מה שמייצר אמון אצל לקוח פרימיום.

---

### 1.3 Funnel + Conversion Path — **7 / 10**

**ממצאים**:
- ה-CTA הראשי `פתח תיק ₪500` קבוע ב-Nav, מודגש בצבע (cobalt), מוביל ל-#catalog/#intake.
- ה-"Soft conversion" קיים: מקדמה סמלית ₪500 + החזר מלא תוך 30 יום. **מבריק מבחינה כלכלית-התנהגותית** — מוריד friction מ-$0 לרק-₪500 ויוצר commitment ראשוני.
- ה-Path: Land → Hero (text broken) → Board (live) → Who → Calc → Catalog → How (8 steps) → Reviews → Advisors → Intake → FAQ → Blog → Terms → Footer. זה **13 פולדים — ארוך מדי**. גולש פרימיום מתעצבן.
- ה-Calculator (#calc) — מצוין כעיקרון, אבל מבוסס בעיקר על MSRP slider; לפי הקיים `gita-audit.md` חסר בו עלות-Shipping נכונה ($2,500 במקום $2,000 בעין-Excel), חסרות שורות $3K-Discount ו-₪2K customs.
- ה-Intake Form (#intake) — 8 שדות. סביר, אבל ה-friction יכול להיות נמוך יותר אם השדה היחיד-החובה הוא **טלפון**.

**פעולה**: הוסף **2 CTAs sticky** למטה במובייל ("פתח תיק ₪500" + "WhatsApp"), ופתח את ה-Catalog ב-snap-scroll מהירה אחרי 1 גלילה ב-Hero. צמצם את הטופס ל-3 שדות חובה (שם, טלפון, תקציב). השאר אופציונלי.

---

### 1.4 Trust / Credibility — **5 / 10**

**ממצאים**:
- ✅ "החזר מלא של ₪500 אם אין התאמה תוך 30 יום" — guarantee קונקרטי. מעולה.
- ✅ "200 נקודות בדיקה + Carfax מלא + ביטוח שילוח 100%" — מקצועי.
- ✅ "ציות לרגולציה ישראלית · פרטיות GDPR" — תנאי-שימוש קיימים (8 חלקים).
- ❌ **Advisory Board ריק**: `#advisors` exists בקוד אבל לא הצלחתי לראות פנים אמיתיות. ה-Excel מציין שמות ספציפיים (גרופר, וולט מנכ״ל, חנן סילונסון) — לא מופיעים.
- ❌ **Press logos `גלובס · Ynet · דה-מרקר · כלכליסט · מאקו · N12`** — מוצגות כטקסט בלבד, לא כלוגואים אמיתיים. זה נראה כמו טענה ריקה.
- ❌ **חוסר רישוי בולט**: היכן רישיון מתווך-יבוא? איפה מספר ח״פ? אין רגישות בולטת לאמינות-תאגיד.
- ❌ אין בנק-שותף מצוין שמית (Excel מדבר על מרכנתיל/יהב).
- **לקוח-פרימיום-של-₪2M לא יסמוך** ללא לוגואים אמיתיים + פנים + רישיון.

**פעולה**: הוסף 5 פנים אמיתיות של יועצים (שמות + תפקיד + LinkedIn) + לוגואים אמיתיים של ערוצי-תקשורת (גם אם זו "הופענו ב-" mockup) + מספר ח״פ ורישיון יבוא בולט ב-Footer.

---

### 1.5 Storytelling — **6.5 / 10**

**ממצאים**:
- יש **conceptual arc** טוב: כאב (יבואן רוצח אותך) → פתרון (אנחנו חותכים את היבואן) → הוכחה (78%) → תהליך (8 שלבים) → אמון (אדוויזורים).
- ה-`#who` יש לו `eyebrow + h-display + italic + lede` — קופי איכותי: "המודל החדש *ליבוא יוקרה*. נולדנו מתוך תסכול על מחירי היבואן..." — זה Apple-class.
- ה-`#intake` headline `ראשון — *ספר לנו על החלום.*` — נהדר. רגשי. RTL טיפוגרפי איטלי.
- ❌ **חסר Founder Story** — מי גיתאי? מי "אנחנו"? אין פנים, אין שם, אין סיפור אישי. גולש פרימיום קונה אנשים, לא מודלים.
- ❌ הקופי בכמה מקומות נכנס ל"Hebrew SEO" rambly: "ייעוץ ויבוא אישי של רכבי יוקרה מארצות הברית. שקיפות מלאה, מחיר משתלם ב-78%, מסירה תוך 8-12 שבועות." — שורה זו ב-Title-tag וב-Footer גם. צריך לדבר רגשי, לא תיאורי.
- העברית עקבית. ה-eyebrow ב-uppercase Hebrew (`הרכב שתמיד רצית`) — הראינו בצילום ישן — היה מעולה. בנוסח הנוכחי זה ירד.

**פעולה**: הוסף Section `#founder` קצר (300 מילים + פנים + ציטוט) של מנכ״ל/מייסד. הסבר למה התחיל את זה. זה ההבדל בין "אתר יפה" ל-"מותג שאני סומך עליו עם ₪2M".

---

### 1.6 Brand Strength — **6 / 10**

**ממצאים**:
- ❌ **המשבר העיקרי**: שם המותג לא קונסיסטנטי. `AutoImports.co.il` (task brief) ≠ `GITA` (לוגו) ≠ `GITA-CARS` (build ישן) ≠ `GITA.cars` (privacy email). זה משבר branding בסיסי.
- הזהות הוויזואלית — Cobalt midnight + Frank Ruhl Libre serif + Heebo sans + JetBrains Mono — **חזקה ועקבית**. אסתטיקה ברמת Audi/Porsche.
- העברית — אחידה. הטון מקצועי-מפויס. RTL מטופל היטב.
- ה-Marquee עם `GITA · 2026 · USD/ILS 2.93` — חזק. נותן תחושת "live newsroom".
- חסרים: Brand promise חרוט (Tagline אחד-משפט-לכל-החיים). ה-`Trust. Credibility. The New Model.` ב-Bible הוא טוב — אבל לא מופיע בולט.

**פעולה**: בחרו **שם אחד** (אני ממליץ `AutoImports.co.il` — תיאורי, ישראלי, אמין יותר). שנו את הלוגו, ה-`<title>`, ה-OG-tags, ה-Footer, ה-Privacy email. הוסיפו את ה-Tagline `המודל החדש ליבוא יוקרה` תחת הלוגו ב-Nav.

---

### Part 1 — Sub-total:

| # | קטגוריה | ציון |
|---|---|---|
| 1.1 | בהירות מסר | 5.5 |
| 1.2 | חוזק הצעת-ערך | 7.5 |
| 1.3 | Funnel + Conversion | 7.0 |
| 1.4 | Trust / Credibility | 5.0 |
| 1.5 | Storytelling | 6.5 |
| 1.6 | Brand Strength | 6.0 |
| **Avg** | **McKinsey Score** | **6.25 / 10** |

---

## Part 2 — Awwwards Score (Judge Lens)

| # | קטגוריה | ניקוד | הערות |
|---|---|---|---|
| 1 | **Design** | **7.5** | אסתטיקה מצוינת: cobalt midnight + Three.js particles + drop-shadow מותאם לרכב + film-grain overlay + Frank Ruhl Libre serif italic. ברמת Audi 2026. אבל ה-content empty-state ב-Hero (40% מסך משמאל ריק) מבטל חצי מהציון. |
| 2 | **Usability** | **6.5** | Nav RTL עובד, smooth-scroll (Lenis) עובד, חלוקה לפולדים ברורה. אבל: a11y חסר (אין `aria-label` על הרכב-תמונה בעברית, ה-`.h-headline` עם `aria-label` כפול-ספירה גורם screen-reader confusion), כפתורים `data-tilt` קטנים מ-44px touch-target, vertically scrolling 13 sections עייפים. |
| 3 | **Creativity** | **8.0** | מטאפורת ה-Stock Market Board ל-Live דילים = **רעיון מקורי**. ticker עם דילים live · 5% עמלת-שירות כ-USP · "AutoImports cuts the importer" קונספט. ה-Three.js particles + Cobalt drop-shadow על רכב = audi-grade. ה-`hero-bigtype` (מהיבואן הרשמי / אל המקור) — surprise-moment חזק. |
| 4 | **Content** | **6.5** | קופי איכותי בכמה מקומות (`#who`, `#intake`) — Apple/Audi class. אבל חוסר case-studies אמיתיים, חוסר Founder-story, וחוסר שמות-אנשים (advisors) מורידים. ה-FAQ עם 14 פריטים — חיובי. ה-Terms 8 פריטים — חיובי. |
| 5 | **Mobile (390px)** | **6.0** | בצילום `mq-1-hero.png` המובייל מציג קופי "Ford Bronco Raptor · LANDED ₪464,435 · חיסכון 73%" — זה טוב לכרטיס. אבל ה-Hero MAIN headline ("כל רכב מארה״ב") לא מופיע. WhatsApp FAB מצוין. ה-burger menu עובד. כפתורים sticky חסרים. |
| 6 | **Animation / Interaction** | **7.5** | Lenis smooth-scroll + GSAP ScrollTrigger + CSS char-stagger + Three.js particles + drop-shadow + tilt-cards + 5-slide alternating hero. אבל: האנימציות **ארוכות מדי** (~1.7s עד שה-H1 מופיע) → פוגעות ב-LCP. צריך 30% faster. |
| 7 | **Performance** | **5.5** | Three.js + 8 videos (.mp4) ב-`#how` עם autoplay loop muted = bandwidth-heavy. אין דיווח Lighthouse אבל ההערכה: LCP > 3s, TBT > 300ms, CLS > 0.1 (ה-`heroContent` נכנס מעולמה ריקה). Videos ב-`preload="metadata"` עוזר אבל לא מספיק. |
| **Total Avg** | | **6.79** | |

**Total Awwwards Score: 6.8 / 10**

> **SOTD threshold**: 8.0+. **המרחק**: 1.2 נקודות. **ריאליסטי תוך 72 שעות** אם מטפלים ב-LCP (animation reduction), Hero content visibility (immediate paint), case-studies real, ו-advisor faces.

---

## Part 3 — השוואה למובילים בעולם 2026

### **vs. Cadillac.com** (Lyriq/Escalade IQ)
- **טוב יותר**: Cadillac חזק ב-CGI cinematography של רכב + clear "Build & Price" CTA כל הזמן. ה-IA פשוטה: Models / Inventory / Pre-Order. אין shop-by-deal — שמה GITA מנצח.
- **פחות טוב**: Cadillac מנצח רק רכב אחד-מותג; GITA מנצח את **כל ה-shopping list** הישראלי.
- **איפה GITA יכול לנצח**: על concept ייחודי "stock market of imports" — אף יצרן OEM לא יעשה זאת.

### **vs. Audi.com**
- **טוב יותר**: Audi מצוין ב-Hero alternating + serif/sans contrast + black-on-color typography. ה-build הזה (`hero-mb` עם 5 alternating slides) — מושפע ישירות מ-Audi, ואכן מנסה לחקות. אבל Audi עושה זאת **מהר יותר ועם content immediate**.
- **פחות טוב**: Audi לא מציע מחיר/חיסכון, הוא לא marketplace, ולא מציע ROI.
- **איפה GITA יכול לנצח**: בשילוב Audi-aesthetic + e-commerce-class price comparison (G63 vs Israel = ₪915K saving). ייחודי בעולם.

### **vs. Tesla.com**
- **טוב יותר**: Tesla = utility-minimalism. Click-to-buy ב-3 שלבים. CTA bold. אין fluff.
- **פחות טוב**: Tesla *משעמם*. אין סטוריטלינג, אין רגש, ה-imagery generic.
- **איפה GITA יכול לנצח**: Tesla-speed (3-click buy) + Audi-emotion (cinematic) + Bloomberg-data (live deals board). אם 3-Click intake form יהיה (שם, טלפון, רכב), זה ינצח את Tesla ב-friction.

### **vs. Porsche.com**
- **טוב יותר**: Porsche = הסטנדרט. cinematography ברמת פילם. configurator unique. brand-craft. Site of the Day פעמים רבות.
- **פחות טוב**: Porsche דורש $150K כדי בכלל לדבר.
- **איפה GITA יכול לנצח**: GITA מציע **את אותה Porsche** ב-43% פחות. אבל זה חייב להיות ב-Hero ולא מוסתר.

### **vs. Lucid.com (Gravity)**
- **טוב יותר**: Lucid מנצחת ב-Hero-video full-bleed + storytelling cinematic + animation 60fps + serif typography + spacing-luxury. הם הזוכים של World Luxury Car 2026 ([Lucid IR](https://ir.lucidmotors.com/news-releases/news-release-details/lucid-gravity-suv-recognized-2026-world-luxury-car-year)).
- **פחות טוב**: Lucid אין shopping = אין conversion-fast.
- **איפה GITA יכול לנצח**: Lucid-class cinematography + GITA-class conversion. אם Hero יציג video-full-bleed של G63 ברחוב ת״א + headline immediate + "פתח תיק ₪500" CTA = SOTD potential.

### **vs. Rivian.com**
- **טוב יותר**: Rivian = adventure-storytelling + cohesive brand (R1T/R1S/Amazon vans). UI נקי.
- **פחות טוב**: Rivian = US-only narrative, לא רלוונטי לישראלי.
- **איפה GITA יכול לנצח**: Israeli-relevance + multi-brand catalog + 78% savings. Rivian-aesthetic on Israeli substance.

---

## Part 4 — Top 10 לתקן ב-72 שעות

### 🔴 P0 — Critical (24h)

1. **תקן את ה-Hero**: הצג את ה-H1 (`כל רכב מארה״ב. במחיר נמוך מבישראל. תוך 72h הצעה.`) ב-LCP < 1.5s. אל תסתיר אותו מאחורי 1.7s char-stagger. שמור על האנימציה הקלה רק על eyebrow + rule + sub-line. הלוגיקה: `opacity:1` כברירת-מחדל, אנימציה רק כ-progressive-enhancement.

2. **החלט על שם אחד**: `AutoImports.co.il` או `GITA`. החלף אחיד בכל המקומות (logo, `<title>`, footer, OG, email). מומלץ `AutoImports.co.il` — תיאורי, אמין, ישראלי.

3. **תקן את ה-Shipping mismatch**: Excel `Price breakdown!B7` אומר $2,000, האתר ו-chatbot אומרים $2,500. תקן בכל המקומות (3 קבצים: `js/data.js`, `js/chatbot.js`, `index.html` calc default).

### 🟠 P1 — High (48h)

4. **הוסף 3 Case Studies אמיתיות** עם תמונת-לקוח (stock), שם, ציטוט, ורכב. למשל: "דניאל כ., 41, ת״א — הביא G63 ב-₪1.18M, חסך ₪915K". הצב ב-section חדש בין `#who` ל-`#calc`.

5. **Advisory Board עם פנים אמיתיות** (5 כרטיסים): שם, תפקיד, חברה-קודמת, LinkedIn, תמונה. כפי שמופיע ב-Excel `משימות` (גרופר, וולט מנכ״ל, חנן סילונסון). זה הופך את האתר ל"חברה אמיתית".

6. **Trust strip בולט ב-Footer**: ח״פ + רישיון יבוא + כתובת רשמית + טלפון + שעות-פעילות. ללא זה — אין trust ל-₪2M deal.

### 🟡 P2 — Medium (72h)

7. **קצר את ה-Intake Form**: 8 שדות → 3 חובה (שם, טלפון, תקציב). השאר אופציונלי. **כפתור one-click `שלח דרך WhatsApp`** במקום אימייל-form-submit.

8. **לוגואי תקשורת אמיתיים**: ה-`adv-outlets` מציג טקסט בלבד. הוסף SVG-mockup-logos של גלובס/Ynet/כלכליסט. גם אם זה "as featured in"-style.

9. **Sticky Mobile CTA**: bottom-bar ב-mobile עם 2 כפתורים — "פתח תיק ₪500" + "WhatsApp". כרגע ה-WhatsApp FAB לבד.

10. **Lighthouse Performance < 90 ⟶ 90+**: דחה video preload (lazy load בעמדת `IntersectionObserver`), שקול להסיר את ה-Three.js במובייל לטובת ה-`h-particles-fallback` (כבר קיים אבל לא מופעל). יעד: LCP < 2.5s, CLS < 0.1, TBT < 200ms.

---

## Part 5 — מסקנה

### האם זה אתר #1 בעולם ב-2026?
**לא.**

### מה החסר?
1. **Hero broken** — המסר הראשי לא נראה בלי המתנה
2. **Brand confusion** — AutoImports vs GITA vs GITA-CARS
3. **Trust gaps** — אין פנים אמיתיות, אין רישיון בולט, אין case-studies
4. **Performance** — 8 videos + Three.js פוגעים ב-LCP

עם זאת — **הקונספט והמודל יוצאי-דופן**: מטאפורת stock-market-of-imports, 5% transparent service fee, ₪500 reversible deposit, 200-point inspection, ו-78% saving claim על נתונים-של-אקסל-אמיתי = זה הבסיס לאתר #1 בעולם. צריך 72 שעות של ביצוע ממוקד.

### הציון הסופי: **6.4 / 10**
(ממוצע משוקלל: McKinsey 6.25 × 0.4 + Awwwards 6.79 × 0.6 = 6.57. אבל בגלל ה-Hero broken המוריד את ה-5-second-test ל-כשל, אני מוריד 0.15 ל-**6.4**.)

### דירוג נוכחי מול המובילים (2026):

| # | אתר | ציון משוער (Awwwards-style) |
|---|---|---|
| 1 | Porsche.com | 9.2 |
| 2 | Lucid.com (Gravity) | 9.0 |
| 3 | Audi.com | 8.8 |
| 4 | Rivian.com | 8.5 |
| 5 | Cadillac.com | 7.8 |
| 6 | Tesla.com | 7.5 |
| **7** | **AutoImports.co.il (GITA)** | **6.4** |

**אחרי 72 שעות של ביצוע הרשימה לעיל** — היעד הריאלי: **8.2 / 10**, ודירוג **#4-5** מול המובילים, ועם Awwwards Site of the Day **בהישג-יד**.

---

## נספח א׳ — מקורות ומתודולוגיה

- **Live URL audited**: [gitteromri-ux.github.io/gita-cars](https://gitteromri-ux.github.io/gita-cars/) (screenshot taken 2026-05-23, see `current_session_context/tool_calls/screenshot/`)
- **Excel source of truth**: `website-auto-8.xlsx` (8 tabs, cross-checked via existing `gita-audit.md`)
- **Messaging Bible**: `gita-v2/MESSAGING_BIBLE.md` (10 sections, Hebrew-only spec)
- **Code review**: `gita-v2/index.html` (569 lines), `js/folds/hero.js` (text injection 1.7s delay confirmed), `css/folds/hero.css` (cobalt midnight palette, char-stagger animation), `js/app-mb.js` (data layer + reviews/advisors injection)
- **Competitor reference**: [Awwwards SOTD criteria](https://www.awwwards.com/websites/sites_of_the_day/) — Design, Usability, Creativity, Content, Mobile, Animation, Performance (7 criteria, avg ≥ 8.0 for SOTD)
- **Lucid 2026 award**: [Lucid Gravity = World Luxury Car of the Year 2026](https://ir.lucidmotors.com/news-releases/news-release-details/lucid-gravity-suv-recognized-2026-world-luxury-car-year) — reference benchmark for "luxury web" in 2026

---

**Auditor signature**: McKinsey ex-CMO + Awwwards Senior Judge
**Verdict**: זה אתר בעל פוטנציאל-עצום שכרגע מבזבז את-עצמו על Hero broken ו-brand-confusion. תקנו 10 דברים → תהפכו ל-Site-of-the-Day. תשאירו כפי שזה → תישארו #7.
