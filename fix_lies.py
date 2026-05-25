#!/usr/bin/env python3
"""Remove all fabricated/exaggerated numbers and 'lifetime service' claims.
Keep ONLY facts that are not invented: 2023 founding, ₪500 deposit, 60-90 day process, 25-45% savings range (matches the catalog math).
"""
import re, os, glob

ROOT = os.path.dirname(os.path.abspath(__file__))

# Site-wide replacements (text-level)
REPLACEMENTS = [
    # Lifetime service - REMOVE
    ('שירות מתמשך לאורך הבעלות', 'תמיכה בשאלות לאחר המסירה'),
    ('שירות מתמשך', 'תמיכה לאחר מסירה'),
    ('מסירה + שירות מתמשך', 'מסירת המפתחות'),
    ('שירות מתמשך — תמיכה בכל שלב.', 'תמיכה זמינה בשאלות לאחר המסירה.'),
    # Fabricated stats - REMOVE
    ('500+ עסקאות', 'עשרות עסקאות'),
    ('500+ לקוחות', 'עשרות לקוחות'),
    ('500+', 'עשרות'),
    ('מאות עסקאות', 'עשרות עסקאות'),
    ('₪M-46', '—'),
    ('₪46M', '—'),
    ('46 מיליון ש"ח', '—'),
    ('46 מיליון', '—'),
    ('98% מהלקוחות שלנו ממליצים', 'לקוחות מרוצים'),
    ('98%', '—'),
    # Misleading day counts
    ('75 ימי תהליך ממוצע', '60-90 ימי תהליך'),
    ('בממוצע 75 ימים', 'בממוצע 60-90 ימים'),
    ('38 ימים בים', '30-45 ימים בים'),
    # Other fabrications
    ('12 שותפים בארה"ב', 'שותפים בארה"ב'),
    ('12 מדינות', 'מספר מדינות'),
    ('60+ דילרים מאומתים', 'דילרים מאומתים'),
    ('מובילים בתחום', 'פועלים בתחום'),
    ('מובילים בשוק', 'פועלים בשוק'),
]

# Files to scan
files = glob.glob(os.path.join(ROOT, '*.html'))
total = 0
for f in files:
    with open(f, 'r', encoding='utf-8') as fp:
        html = fp.read()
    orig = html
    for old, new in REPLACEMENTS:
        html = html.replace(old, new)
    if html != orig:
        with open(f, 'w', encoding='utf-8') as fp:
            fp.write(html)
        diff = sum(1 for o,n in REPLACEMENTS if o in orig and o not in html)
        total += diff
        print(f"FIXED {os.path.basename(f)}: {diff} replacements")

# Also fix the blog 46M article
blog_path = os.path.join(ROOT, 'blog.html')
with open(blog_path, 'r', encoding='utf-8') as fp:
    blog = fp.read()
blog = blog.replace('— חיסכון מצטבר ללקוחות', 'נקודת ציון: סיכום שנה')
blog = blog.replace('מאז שהקמנו את החברה, חסכנו ללקוחות שלנו יותר מ-— ש"ח. וזה רק ההתחלה.',
                    'סוקרים את עשרות העסקאות שבוצעו השנה והחיסכון המצטבר שיצרנו ללקוחות.')
with open(blog_path, 'w', encoding='utf-8') as fp:
    fp.write(blog)

print(f"\nDONE: {total} total replacements")
