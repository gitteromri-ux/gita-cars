// AutoImports v4 — Premium app logic
// Hero rotation, Stock board (.stock-row-ultra), Catalog (.car-card), Modal (Cars.com), WhatsApp bot

(function () {
  'use strict';

  const $ = (sel, ctx = document) => ctx.querySelector(sel);
  const $$ = (sel, ctx = document) => Array.from(ctx.querySelectorAll(sel));
  const fmt = (n) => '₪' + Math.round(n).toLocaleString('he-IL');
  const fmtShort = (n) => n >= 1000000 ? '₪' + (n / 1000000).toFixed(2) + 'M' : '₪' + (Math.round(n / 1000)) + 'K';

  // ===== Hero Rotation =====
  function initHeroRotation() {
    const slides = $$('.hero-slide');
    const dots = $$('.hero-dot');
    if (!slides.length) return;
    let i = 0;
    const go = (n) => {
      slides[i].classList.remove('active');
      if (dots[i]) dots[i].classList.remove('active');
      i = n % slides.length;
      slides[i].classList.add('active');
      if (dots[i]) dots[i].classList.add('active');
    };
    setInterval(() => go(i + 1), 5200);
    dots.forEach((d, idx) => d.addEventListener('click', () => go(idx)));
  }

  // ===== Sparkline SVG =====
  function sparklineSVG() {
    const pts = [];
    let y = 8;
    for (let x = 0; x <= 100; x += 8) {
      y += (Math.random() - 0.3) * 6;
      y = Math.min(36, Math.max(6, y));
      pts.push(`${x},${y.toFixed(1)}`);
    }
    const color = '#00d18f';
    return `<svg viewBox="0 0 100 44" preserveAspectRatio="none" style="width:100%;height:100%;">
      <polyline points="${pts.join(' ')}" fill="none" stroke="${color}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/>
      <polyline points="0,44 ${pts.join(' ')} 100,44" fill="${color}" fill-opacity="0.12"/>
    </svg>`;
  }

  // ===== Stock Board =====
  function initStockBoard() {
    const rows = $('#stock-rows');
    if (!rows || !window.STOCK_MODELS) return;
    rows.innerHTML = window.STOCK_MODELS.map((s, idx) => `
      <div class="stock-row-ultra" data-car="${s.id}">
        <div class="stock-rank-ultra">${String(idx + 1).padStart(2, '0')}</div>
        <div class="stock-name-ultra">${s.symbol} · ${s.name}</div>
        <div class="stock-dealer-ultra">${fmtShort(s.dealer)}</div>
        <div class="stock-our-ultra">${fmtShort(s.ours)}</div>
        <div class="stock-spark">${sparklineSVG()}</div>
        <div class="stock-save-ultra">−${fmtShort(Math.abs(s.change))}</div>
        <div class="stock-pct-ultra">${s.pct.toFixed(1)}%</div>
      </div>
    `).join('');

    // Refresh sparklines periodically (visual ticker)
    setInterval(() => {
      $$('.stock-row-ultra .stock-spark').forEach((sp) => { sp.innerHTML = sparklineSVG(); });
    }, 4200);

    // Click → open modal
    rows.addEventListener('click', (e) => {
      const row = e.target.closest('.stock-row-ultra');
      if (!row) return;
      const car = window.CARS.find((c) => c.id === row.dataset.car);
      if (car) openModal(car);
    });

    // Live time
    const t = $('#stock-time');
    if (t) {
      const update = () => {
        const d = new Date();
        t.textContent = d.toLocaleTimeString('he-IL', { hour: '2-digit', minute: '2-digit', second: '2-digit' });
      };
      update();
      setInterval(update, 1000);
    }
  }

  // ===== Catalog =====
  function initCatalog() {
    const grid = $('#catalog-grid');
    if (!grid || !window.CARS) return;
    grid.innerHTML = window.CARS.map((c) => {
      const saving = c.dealerPrice - c.ourPrice;
      const pct = Math.round((saving / c.dealerPrice) * 100);
      const parts = c.eyebrow.split(' · ');
      return `
        <article class="car-card" data-car="${c.id}">
          <div class="car-img-wrap">
            <img src="${c.image}" alt="${c.nameHe}" loading="lazy"/>
            <span class="car-badge-discount">−${pct}%</span>
            <div class="car-condition">${c.condition === 'certified' ? `<span class="cert-badge"><span class="cert-badge-seal"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="m9 11 3 3L22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg></span><span class="cert-badge-text"><strong>CERTIFIED</strong></span></span>` : `<span class="car-condition-new">חדש מהיצרן</span>`}</div>
          </div>
          <div class="car-info">
            <div class="car-eyebrow-row">
              <span>${parts[0] || ''}</span><span class="dot">·</span>
              <span>${parts[1] || ''}</span><span class="dot">·</span>
              <span>${parts[2] || ''}</span>
            </div>
            <h3 class="car-name">${c.name}</h3>
            <div class="car-specs-row">
              <div class="car-spec"><div class="car-spec-val">${c.accel}s</div><div class="car-spec-label">0-100</div></div>
              <div class="car-spec"><div class="car-spec-val">${c.hp}</div><div class="car-spec-label">HP</div></div>
              <div class="car-spec"><div class="car-spec-val">${c.nm}</div><div class="car-spec-label">N·M</div></div>
            </div>
            <div class="car-price-section">
              <div>
                <div class="car-price-our-label">מחיר ייבוא אישי</div>
                <div class="car-price-our">${fmt(c.ourPrice)}</div>
                <div class="car-price-old">${fmt(c.dealerPrice)}</div>
              </div>
              <div style="text-align:left">
                <div class="car-price-our-label">חיסכון</div>
                <div style="font-family:'Inter';font-weight:700;font-size:18px;color:var(--red);">${fmtShort(saving)}</div>
              </div>
            </div>
            <button class="car-cta-build">צפה במפרט מלא →</button>
          </div>
        </article>`;
    }).join('');

    grid.addEventListener('click', (e) => {
      const card = e.target.closest('.car-card');
      if (!card) return;
      const car = window.CARS.find((c) => c.id === card.dataset.car);
      if (car) openModal(car);
    });
  }

  // ===== Modal (Cars.com style) =====
  function priceBreakdown(car) {
    const usdBase = (car.ourPrice / 2.93) * 0.78;
    const shipping = window.FX.shippingUsd * window.FX.usdIls;
    const customs = window.FX.customsIls;
    const service = car.ourPrice * window.FX.servicePct;
    const vat = car.ourPrice * window.FX.vat / (1 + window.FX.vat);
    return [
      { lbl: 'מחיר רכב יבוא (FOB)', val: fmt(usdBase * 2.93) },
      { lbl: 'שילוח ימי ($2,000)', val: fmt(shipping) },
      { lbl: 'מכס וביטוח', val: fmt(customs) },
      { lbl: 'דמי שירות (5%)', val: fmt(service) },
      { lbl: 'מע"מ (18%)', val: fmt(vat) },
      { lbl: 'הנחת קבוצה ($3,000)', val: '−' + fmt(window.FX.discountUsd * window.FX.usdIls) },
      { lbl: 'פיקדון התחלתי', val: '₪500' }
    ];
  }

  function openModal(car) {
    const modal = $('#car-modal');
    const content = $('#modal-content');
    if (!modal || !content) return;
    const saving = car.dealerPrice - car.ourPrice;
    const pct = Math.round((saving / car.dealerPrice) * 100);

    content.innerHTML = `
      <button class="modal-close" id="modal-close-btn" aria-label="סגור">×</button>
      <div class="modal-gallery">
        <div class="modal-gallery-main">
          ${car.gallery.map((g, i) => `<img class="${i === 0 ? 'active' : ''}" src="${g}" alt="${car.nameHe} ${i + 1}" data-i="${i}"/>`).join('')}
          <div class="modal-gallery-arrows">
            <button id="mg-prev" aria-label="קודם">‹</button>
            <button id="mg-next" aria-label="הבא">›</button>
          </div>
        </div>
        <div class="modal-gallery-thumbs">
          ${car.gallery.map((g, i) => `<button class="modal-thumb ${i === 0 ? 'active' : ''}" data-i="${i}"><img src="${g}" alt=""/></button>`).join('')}
        </div>
      </div>
      <div class="modal-body">
        <div class="modal-head-row">
          <div class="modal-head-left">
            <div class="modal-eyebrow">${car.eyebrow}</div>
            <h2 class="modal-name">${car.name}</h2>
            <p style="margin-top:14px;color:#666;font-size:18px;">${car.nameHe} · ${car.engine} · ${car.transmission}</p>
          </div>
          <div class="modal-head-right">
            <div class="modal-price-block">
              <div class="modal-price-our-label">מחיר ייבוא אישי · הכל כלול</div>
              <div class="modal-price-our">${fmt(car.ourPrice)}</div>
              <div class="modal-price-dealer">יבואן רשמי: ${fmt(car.dealerPrice)}</div>
            </div>
            <span class="modal-savings-pill">חיסכון ${fmtShort(saving)} (${pct}%)</span>
          </div>
        </div>

        <div class="modal-tabs">
          <button class="modal-tab active" data-tab="overview">סקירה כללית</button>
          <button class="modal-tab" data-tab="specs">מפרט מלא</button>
          <button class="modal-tab" data-tab="features">תוספות וציוד</button>
          <button class="modal-tab" data-tab="pricing">פירוט מחיר</button>
        </div>

        <div class="modal-tab-content active" data-pane="overview">
          <div class="modal-specs-grid">
            <div class="modal-spec-card">
              <div class="modal-spec-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg></div>
              <div class="modal-spec-val-big">${car.accel}<span>s</span></div>
              <div class="modal-spec-label-big">0-100 קמ"ש</div>
            </div>
            <div class="modal-spec-card">
              <div class="modal-spec-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg></div>
              <div class="modal-spec-val-big">${car.hp}<span>HP</span></div>
              <div class="modal-spec-label-big">כוח סוס</div>
            </div>
            <div class="modal-spec-card">
              <div class="modal-spec-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/></svg></div>
              <div class="modal-spec-val-big">${car.nm}<span>N·m</span></div>
              <div class="modal-spec-label-big">מומנט</div>
            </div>
            <div class="modal-spec-card">
              <div class="modal-spec-icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M3 12h18M3 6h18M3 18h18"/></svg></div>
              <div class="modal-spec-val-big">${car.topSpeed}<span></span></div>
              <div class="modal-spec-label-big">מהירות שיא קמ"ש</div>
            </div>
          </div>
          <div class="spec-table">
            <h4>תיאור הרכב</h4>
            <p style="padding:20px 0;font-size:16px;line-height:1.7;color:#444;">
              <strong>${car.name}</strong> שנת ${car.year}, מצב ${car.history}. הרכב כולל מנוע ${car.engine} עם תיבת ${car.transmission} ומערכת הינע ${car.drive}.
              ${car.seats} מושבים, ${car.doors} דלתות, משקל ${car.weight} ק"ג. ${car.mpg}.
            </p>
          </div>
        </div>

        <div class="modal-tab-content" data-pane="specs">
          <div class="spec-table">
            <h4>מפרט טכני מלא</h4>
            <table>
              <tr><td>מנוע</td><td>${car.engine}</td></tr>
              <tr><td>הספק מקסימלי</td><td>${car.hp} כ"ס</td></tr>
              <tr><td>מומנט מקסימלי</td><td>${car.nm} N·m</td></tr>
              <tr><td>תאוצה 0-100 קמ"ש</td><td>${car.accel} שניות</td></tr>
              <tr><td>מהירות שיא</td><td>${car.topSpeed} קמ"ש</td></tr>
              <tr><td>תיבת הילוכים</td><td>${car.transmission}</td></tr>
              <tr><td>מערכת הינע</td><td>${car.drive}</td></tr>
              <tr><td>צריכה / טווח</td><td>${car.mpg}</td></tr>
              <tr><td>סוג דלק</td><td>${car.fuel}</td></tr>
              <tr><td>מספר מושבים</td><td>${car.seats}</td></tr>
              <tr><td>מספר דלתות</td><td>${car.doors}</td></tr>
              <tr><td>אורך</td><td>${car.length} מ"מ</td></tr>
              <tr><td>רוחב</td><td>${car.width} מ"מ</td></tr>
              <tr><td>גובה</td><td>${car.height} מ"מ</td></tr>
              <tr><td>משקל עצמי</td><td>${car.weight} ק"ג</td></tr>
              <tr><td>היסטוריה</td><td>${car.history}</td></tr>
            </table>
          </div>
        </div>

        <div class="modal-tab-content" data-pane="features">
          <h4 style="font-family:'Heebo';font-size:22px;font-weight:500;margin-bottom:24px;">תוספות וציוד כולל</h4>
          <div class="features-grid-modal">
            ${car.features.map((f) => `<div class="feature-row">${f}</div>`).join('')}
          </div>
        </div>

        <div class="modal-tab-content" data-pane="pricing">
          <div class="price-breakdown">
            <h4>פירוט מחיר מלא · 15 שלבי תהליך</h4>
            ${priceBreakdown(car).map((r) => `<div class="price-row"><span>${r.lbl}</span><span class="price-val">${r.val}</span></div>`).join('')}
            <div class="price-row total"><span>סה"כ ${car.nameHe}</span><span class="price-val">${fmt(car.ourPrice)}</span></div>
          </div>
          <p style="font-size:15px;line-height:1.7;color:#555;background:rgba(214,40,40,0.06);padding:20px;border-radius:12px;border-right:3px solid var(--red);">
            <strong>השוואה ליבואן רשמי:</strong> ${fmt(car.dealerPrice)} · <strong>החיסכון שלך:</strong> <span style="color:var(--red);font-weight:700;">${fmt(saving)} (${pct}%)</span>
          </p>
        </div>

        <div class="modal-cta-row">
          <a class="btn btn-primary" href="https://wa.me/972500000000?text=${encodeURIComponent('שלום, אני מעוניין ב-' + car.nameHe + ' (' + car.name + ')')}" target="_blank" style="background:#25D366;color:#fff;padding:18px 28px;border-radius:100px;font-family:'Heebo';font-weight:500;display:inline-flex;align-items:center;gap:10px;justify-content:center;">
            התחל תהליך בוואטסאפ
          </a>
          <a class="btn" href="#process" style="background:var(--carbon);color:#fff;padding:18px 28px;border-radius:100px;font-family:'Heebo';font-weight:500;display:inline-flex;align-items:center;gap:10px;justify-content:center;" onclick="document.getElementById('car-modal').classList.remove('open');document.body.style.overflow=''">
            צפה ב-15 שלבי התהליך
          </a>
        </div>
      </div>
    `;

    modal.classList.add('open');
    document.body.style.overflow = 'hidden';

    // Gallery thumb switching
    let currentIdx = 0;
    const imgs = $$('.modal-gallery-main img', content);
    const thumbs = $$('.modal-thumb', content);
    function showImg(i) {
      currentIdx = (i + imgs.length) % imgs.length;
      imgs.forEach((im) => im.classList.remove('active'));
      thumbs.forEach((t) => t.classList.remove('active'));
      imgs[currentIdx].classList.add('active');
      thumbs[currentIdx].classList.add('active');
    }
    thumbs.forEach((t, i) => t.addEventListener('click', () => showImg(i)));
    $('#mg-prev', content).addEventListener('click', () => showImg(currentIdx - 1));
    $('#mg-next', content).addEventListener('click', () => showImg(currentIdx + 1));

    // Tabs
    $$('.modal-tab', content).forEach((tab) => tab.addEventListener('click', () => {
      $$('.modal-tab', content).forEach((x) => x.classList.remove('active'));
      $$('.modal-tab-content', content).forEach((x) => x.classList.remove('active'));
      tab.classList.add('active');
      $(`.modal-tab-content[data-pane="${tab.dataset.tab}"]`, content).classList.add('active');
    }));

    // Close
    $('#modal-close-btn').addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
      if (e.target.classList && e.target.classList.contains('modal-overlay')) closeModal();
    });
  }

  function closeModal() {
    const modal = $('#car-modal');
    if (modal) {
      modal.classList.remove('open');
      document.body.style.overflow = '';
    }
  }

  // ===== WhatsApp Smart Bot =====
  function initWhatsappBot() {
    const fab = $('#wa-fab');
    const button = $('#wa-button');
    if (!fab || !button) return;
    button.addEventListener('click', (e) => {
      e.stopPropagation();
      fab.classList.toggle('open');
    });

    const input = $('#wa-input');
    const send = $('#wa-send');
    const messages = $('#wa-messages');
    if (!input || !send || !messages) return;

    function addMsg(text, who) {
      const el = document.createElement('div');
      el.className = `wa-msg ${who}`;
      const t = new Date().toLocaleTimeString('he-IL', { hour: '2-digit', minute: '2-digit' });
      el.innerHTML = `${text}<div class="wa-time">${t}</div>`;
      messages.appendChild(el);
      messages.scrollTop = messages.scrollHeight;
    }

    function botReply(userText) {
      const t = userText.toLowerCase();
      setTimeout(() => {
        if (/מחיר|כמה|עולה|cost|price/.test(t)) {
          addMsg('המחירים שלנו זולים ב-30%-60% מיבואן רשמי. למשל G63 AMG אצלנו ₪1.18M במקום ₪2.1M ביבואן. איזה רכב מעניין אותך?', 'bot');
        } else if (/g63|מרצדס|mercedes/.test(t)) {
          addMsg('Mercedes G63 AMG 2025 - V8 4.0L Biturbo, 577 כ"ס, 0-100 ב-4.5 שניות. אצלנו: ₪1.18M (חיסכון ₪920K). רוצה הצעת מחיר?', 'bot');
        } else if (/tesla|טסלה|cybertruck|model x/.test(t)) {
          addMsg('יש לנו Tesla Cybertruck AWD ב-₪429K, Model X LR ב-₪429K. שניהם 0 ק"מ עם אחריות מקורית. מה תרצה לראות?', 'bot');
        } else if (/חשמלי|ev/.test(t)) {
          addMsg('יש לנו 6 רכבים חשמליים: Tesla Cybertruck/Model X, Lucid Air, Kia EV9, Rivian R1S, Mercedes G580 EQ. מטווחים 473-660 ק"מ. איזה?', 'bot');
        } else if (/זמן|מתי|כמה זמן/.test(t)) {
          addMsg('תהליך 15 שלבים, סה"כ ~75 ימים מהזמנה עד מסירת מפתחות. כל שלב שקוף, אתה רואה התקדמות 24/7.', 'bot');
        } else if (/אחריות|warranty/.test(t)) {
          addMsg('אחריות יצרן מקורית 4 שנים (ב-G63, X7 וכו) + 8 שנים סוללה לחשמלי. כל הרכבים 0 ק"מ ויד ראשונה.', 'bot');
        } else if (/שלום|היי|hi|hello/.test(t)) {
          addMsg('שלום! איך אוכל לעזור? אפשר לשאול על מחיר, דגמים, חשמלי, תהליך, או אחריות.', 'bot');
        } else {
          addMsg('אעביר נציג אנושי תוך 2 דקות. בינתיים, איזה רכב מעניין אותך? G63? Tesla? Mustang?', 'bot');
        }
      }, 700);
    }

    function submit() {
      const v = input.value.trim();
      if (!v) return;
      addMsg(v, 'user');
      input.value = '';
      botReply(v);
    }
    send.addEventListener('click', submit);
    input.addEventListener('keydown', (e) => { if (e.key === 'Enter') submit(); });
  }

  // ===== Init =====
  document.addEventListener('DOMContentLoaded', () => {
    initHeroRotation();
    initStockBoard();
    initCatalog();
    initWhatsappBot();
  });
})();
