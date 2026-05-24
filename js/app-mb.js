// ============================================
// GITA — Mercedes-Benz grade app (mb)
// powers hero · stock board · catalog · VDP · FAQ · WhatsApp
// ============================================
(function () {
  'use strict';
  const $ = (s, c) => (c || document).querySelector(s);
  const $$ = (s, c) => Array.from((c || document).querySelectorAll(s));
  const fmtILS = n => '₪' + Math.round(n).toLocaleString('en-US');
  const fmtUSD = n => '$' + Math.round(n).toLocaleString('en-US');
  const FX = (typeof FX_USD_ILS !== 'undefined') ? FX_USD_ILS : 2.93;

  // ============================================================
  // VIDEOS pool — reused across hero/cards/VDP
  // ============================================================
  const VIDEOS = [
    './videos/hero-italy-road.mp4',
    './videos/neon-highway.mp4',
    './videos/smudge-highway.mp4',
    './videos/fast-sports-rural.mp4',
    './videos/sports-muscle-rural.mp4',
    './videos/rocky-terrain.mp4',
    './videos/drone-light-car-dark.mp4',
    './videos/windscreen-friends.mp4',
    './videos/ignition-button.mp4',
    './videos/garage-lift.mp4',
    './videos/auto-garage-up-lifting.mp4',
    './videos/happy-dealership.mp4',
    './videos/israel-mediterranean.mp4',
    './videos/container-dock-israel.mp4',
    './videos/drone-roro-shipping.mp4'
  ];
  const vidFor = (slug, i = 0) => {
    let h = 0;
    for (let k = 0; k < (slug || '').length; k++) h = (h * 31 + slug.charCodeAt(k)) >>> 0;
    return VIDEOS[(h + i) % VIDEOS.length];
  };

  // Cinematic gradient backdrops by body type
  const gradFor = (body, fuel) => {
    if (fuel === 'electric') return 'linear-gradient(135deg,#0a1426 0%,#001a2e 50%,#0a3d52 100%)';
    if (body === 'suv') return 'linear-gradient(135deg,#1a1410 0%,#2a1f15 50%,#0f0a05 100%)';
    if (body === 'pickup') return 'linear-gradient(135deg,#1a1a14 0%,#2e2a1a 50%,#0a0a05 100%)';
    if (body === 'sport') return 'linear-gradient(135deg,#1a0a0a 0%,#2e1014 50%,#0a0505 100%)';
    if (body === 'sedan') return 'linear-gradient(135deg,#0a0f1a 0%,#101a2e 50%,#05050a 100%)';
    return 'linear-gradient(135deg,#141414 0%,#1d1d1d 50%,#0a0a0a 100%)';
  };

  // ============================================================
  // CATEGORY normalize (from car.type/body)
  // ============================================================
  const catOf = (car) => {
    const t = (car.type || '').toLowerCase();
    const b = (car.body || '').toLowerCase();
    const cats = new Set();
    if (b === 'suv') cats.add('suv');
    if (t.includes('off-road') || /wrangler|bronco|g63|g500|g580/i.test(car.slug)) cats.add('off-road');
    if (t.includes('electric') || /tesla|lucid|rivian|cybertruck|ev9|g580/i.test(car.slug)) cats.add('ev');
    if (b === 'pickup' || /raptor|cybertruck/i.test(car.slug)) cats.add('pickup');
    if (b === 'coupe' || b === 'sport' || /mustang|amg-gt|corvette/i.test(car.slug)) cats.add('sport');
    if (b === 'sedan' || /lucid|s580|model-s/i.test(car.slug)) cats.add('sedan');
    return Array.from(cats);
  };
  const fuelOf = (car) => {
    const t = (car.type || '').toLowerCase();
    if (t.includes('electric')) return 'electric';
    if (t.includes('phev') || t.includes('plug-in') || t.includes('hybrid')) return 'phev';
    if (t.includes('diesel')) return 'diesel';
    return 'gas';
  };
  const fuelLabel = f => ({ electric: 'חשמלי', phev: 'היברידי נטען', diesel: 'דיזל', gas: 'בנזין' }[f] || 'בנזין');

  // ============================================================
  // HERO — alternating 5 models (Audi-style)
  // Bronco Raptor, Wrangler, Mustang GT, Land Cruiser substitute (G580 EQ - highest discount), G63
  // ============================================================
  const heroPicks = () => {
    const find = slug => CARS.find(c => c.slug === slug);
    return [
      find('ford-bronco-raptor'),                     // Bronco Raptor 2025
      find('jeep-wrangler-sport'),                    // Wrangler 2026
      find('mustang-gt-v8'),                          // Mustang GT
      find('mercedes-g580-eq'),                       // Land Cruiser substitute (highest discount)
      find('mercedes-g63-amg')                        // 5th hero - top absolute saving from MSRP
    ].filter(Boolean);
  };

  let heroIdx = 0;
  let heroTimer = null;
  function buildHero() {
    const stage = $('#heroStage');
    const content = $('#heroContent');
    const inds = $('#heroIndicators');
    const picks = heroPicks();
    if (!stage || !content || !picks.length) return;

    // Map each hero pick to its AI-generated image
    const heroImgMap = {
      'ford-bronco-raptor': './images/hero-bronco-raptor.jpg',
      'jeep-wrangler-sport': './images/hero-wrangler.jpg',
      'mustang-gt-v8': './images/hero-mustang.jpg',
      'mercedes-g580-eq': './images/hero-g580.jpg',
      'mercedes-g63-amg': './images/hero-g63.jpg'
    };
    // Hero ambient (content-agnostic) — single neutral video underlay across all slides
    const ambientVid = './videos/drone-light-car-dark.mp4';
    stage.innerHTML = picks.map((c, i) => {
      const carImg = `./images/car-${c.slug}.png`;
      return `
      <div class="hero-slide ${i === 0 ? 'active' : ''}" data-i="${i}">
        <div class="hero-bg" style="background:${gradFor(c.body, fuelOf(c))}"></div>
        <video class="hero-ambient" muted autoplay loop playsinline webkit-playsinline preload="${i===0?'auto':'metadata'}" src="${ambientVid}"></video>
        <div class="hero-particles" id="heroParticles-${i}"></div>
        <img class="hero-img hero-car-img" src="${carImg}" alt="${c.name}" loading="${i===0?'eager':'lazy'}" />
        <div class="hero-overlay"></div>
      </div>
    `;}).join('');

    inds.innerHTML = picks.map((_, i) => `<button class="hero-ind ${i === 0 ? 'active' : ''}" data-i="${i}" aria-label="slide ${i + 1}"></button>`).join('');

    renderHeroContent(picks, 0);

    $$('#heroIndicators .hero-ind').forEach(b => b.addEventListener('click', () => {
      heroIdx = +b.dataset.i;
      switchHero(picks);
      restartHeroTimer(picks);
    }));

    restartHeroTimer(picks);
  }

  function renderHeroContent(picks, i) {
    const c = picks[i];
    if (!c) return;
    const saveNIS = Math.round((c.israelNIS - c.landedNIS));
    $('#heroContent').innerHTML = `
      <div class="hero-eyebrow"><span class="dot"></span>דגם הדגל · #${c.rank} בחיסכון</div>
      <h1 class="hero-title">${c.name}</h1>
      <p class="hero-sub">${c.note || ''}</p>

      <div class="hero-pricecard">
        <div class="pc-col">
          <span class="pc-lbl">מחיר סופי בישראל</span>
          <span class="pc-val our">${fmtILS(c.landedNIS)}</span>
        </div>
        <div class="pc-divider"></div>
        <div class="pc-col">
          <span class="pc-lbl">מחיר יבואן</span>
          <span class="pc-val their">${fmtILS(c.israelNIS)}</span>
        </div>
        <div class="pc-divider"></div>
        <div class="pc-col">
          <span class="pc-lbl">חיסכון · ${c.savePct}%</span>
          <span class="pc-val save">${fmtILS(saveNIS)}</span>
        </div>
      </div>

      <div class="hero-ctas">
        <button class="btn-mb-primary" onclick="openVDP('${c.slug}')">צפה בפרטים מלאים →</button>
        <a class="btn-mb-ghost" href="#catalog">כל הדגמים</a>
      </div>
    `;
  }

  function switchHero(picks) {
    $$('#heroStage .hero-slide').forEach(s => s.classList.toggle('active', +s.dataset.i === heroIdx));
    $$('#heroIndicators .hero-ind').forEach(b => b.classList.toggle('active', +b.dataset.i === heroIdx));
    renderHeroContent(picks, heroIdx);
  }

  function restartHeroTimer(picks) {
    if (heroTimer) clearInterval(heroTimer);
    heroTimer = setInterval(() => {
      heroIdx = (heroIdx + 1) % picks.length;
      switchHero(picks);
    }, 6500);
  }

  // ============================================================
  // STOCK MARKET BOARD — ticker + 10-card live grid
  // ============================================================
  function buildBoard() {
    const top10 = [...CARS].sort((a, b) => b.saveUSD - a.saveUSD).slice(0, 10);
    const track = $('#tickerTrack');
    const grid = $('#boardGrid');
    if (!track || !grid) return;

    // Ticker — repeat twice so the marquee animation looks seamless
    const tickerHTML = top10.map((c, i) => {
      const sym = (c.nameEn || c.name).split(' ').slice(0, 2).map(w => w[0]).join('').toUpperCase().slice(0, 4) + (c.rank);
      const pct = c.savePct;
      return `
        <span class="tkr-item">
          <span class="tkr-sym">${sym}</span>
          <span class="tkr-name">${c.name}</span>
          <span class="tkr-px">${fmtILS(c.landedNIS)}</span>
          <span class="tkr-delta up">▲ ${pct}%</span>
        </span>`;
    }).join('');
    track.innerHTML = tickerHTML + tickerHTML; // double for seamless loop

    grid.innerHTML = top10.map((c, i) => {
      const saveNIS = Math.round(c.israelNIS - c.landedNIS);
      return `
      <article class="bcard" onclick="openVDP('${c.slug}')" data-magnet>
        <div class="bcard-rank">#${i + 1}</div>
        <div class="bcard-bg" style="background:${gradFor(c.body, fuelOf(c))}">
          <div class="bcard-glow"></div>
          <img class="bcard-img" src="./images/car-${c.slug}.png" alt="${c.name}" loading="lazy" />
          <span class="bcard-enter">לפרטים →</span>
        </div>
        <div class="bcard-body">
          <h3>${c.name}</h3>
          <div class="bcard-row">
            <span class="bcard-lbl">סופי</span>
            <span class="bcard-val">${fmtILS(c.landedNIS)}</span>
          </div>
          <div class="bcard-row strike">
            <span class="bcard-lbl">יבואן</span>
            <span class="bcard-val">${fmtILS(c.israelNIS)}</span>
          </div>
          <div class="bcard-save">
            <span>חיסכון</span>
            <b>${fmtILS(saveNIS)} · ${c.savePct}%</b>
          </div>
        </div>
      </article>`;
    }).join('');
  }

  // ============================================================
  // CATALOG — chips + filters + sort + grid
  // ============================================================
  const state = {
    cat: 'all',
    makes: new Set(),
    bodies: new Set(),
    fuels: new Set(),
    years: new Set(),
    pMin: null, pMax: null,
    sort: 'saving'
  };

  const makeOf = c => (c.nameEn || c.name).split(' ')[0];

  function buildFilters() {
    const makes = [...new Set(CARS.map(makeOf))].sort();
    const bodies = [...new Set(CARS.map(c => c.body).filter(Boolean))].sort();
    const fuels = [...new Set(CARS.map(fuelOf))];
    const years = [...new Set(CARS.map(c => c.year).filter(Boolean))].sort((a, b) => b - a);

    const bodyLbl = b => ({ suv: 'SUV', pickup: 'פיק-אפ', sedan: 'סדאן', coupe: 'קופה', sport: 'ספורט' }[b] || b);

    $('#filterMakes').innerHTML = makes.map(m =>
      `<li><label><input type="checkbox" data-f="make" value="${m}"><span>${m}</span></label></li>`).join('');
    $('#filterBody').innerHTML = bodies.map(b =>
      `<li><label><input type="checkbox" data-f="body" value="${b}"><span>${bodyLbl(b)}</span></label></li>`).join('');
    $('#filterFuel').innerHTML = fuels.map(f =>
      `<li><label><input type="checkbox" data-f="fuel" value="${f}"><span>${fuelLabel(f)}</span></label></li>`).join('');
    $('#filterYear').innerHTML = years.map(y =>
      `<li><label><input type="checkbox" data-f="year" value="${y}"><span>${y}</span></label></li>`).join('');

    $$('.filter-rail input[type=checkbox]').forEach(cb => cb.addEventListener('change', e => {
      const f = e.target.dataset.f, v = e.target.value;
      const set = f === 'make' ? state.makes : f === 'body' ? state.bodies : f === 'fuel' ? state.fuels : state.years;
      if (e.target.checked) set.add(f === 'year' ? +v : v); else set.delete(f === 'year' ? +v : v);
      renderCatalog();
    }));
    $('#priceMin').addEventListener('input', e => { state.pMin = +e.target.value || null; renderCatalog(); });
    $('#priceMax').addEventListener('input', e => { state.pMax = +e.target.value || null; renderCatalog(); });
    $('#filterClear').addEventListener('click', clearFilters);
    $('#catSort').addEventListener('change', e => { state.sort = e.target.value; renderCatalog(); });

    $$('#catChips .cat-chip').forEach(b => b.addEventListener('click', () => {
      $$('#catChips .cat-chip').forEach(x => x.classList.remove('active'));
      b.classList.add('active');
      state.cat = b.dataset.cat;
      renderCatalog();
    }));

    // Mobile filter open
    const mb = $('#filterBtnMobile');
    const rail = $('#filterRail');
    if (mb && rail) {
      mb.addEventListener('click', () => rail.classList.toggle('open'));
    }
  }

  function clearFilters() {
    state.makes.clear(); state.bodies.clear(); state.fuels.clear(); state.years.clear();
    state.pMin = null; state.pMax = null; state.cat = 'all';
    $$('.filter-rail input[type=checkbox]').forEach(cb => cb.checked = false);
    $('#priceMin').value = ''; $('#priceMax').value = '';
    $$('#catChips .cat-chip').forEach(x => x.classList.toggle('active', x.dataset.cat === 'all'));
    renderCatalog();
  }

  function applyFilters() {
    return CARS.filter(c => {
      if (state.cat !== 'all' && !catOf(c).includes(state.cat)) return false;
      if (state.makes.size && !state.makes.has(makeOf(c))) return false;
      if (state.bodies.size && !state.bodies.has(c.body)) return false;
      if (state.fuels.size && !state.fuels.has(fuelOf(c))) return false;
      if (state.years.size && !state.years.has(c.year)) return false;
      if (state.pMin && c.landedNIS < state.pMin) return false;
      if (state.pMax && c.landedNIS > state.pMax) return false;
      return true;
    });
  }

  function sortCars(arr) {
    const a = [...arr];
    if (state.sort === 'saving') a.sort((x, y) => y.saveUSD - x.saveUSD);
    else if (state.sort === 'price-asc') a.sort((x, y) => x.landedNIS - y.landedNIS);
    else if (state.sort === 'price-desc') a.sort((x, y) => y.landedNIS - x.landedNIS);
    else if (state.sort === 'newest') a.sort((x, y) => (y.year || 0) - (x.year || 0));
    return a;
  }

  function renderCatalog() {
    const filtered = sortCars(applyFilters());
    $('#resultsCount').textContent = filtered.length;
    const grid = $('#catGrid');
    if (!filtered.length) {
      grid.innerHTML = `<div class="cat-empty">לא נמצאו רכבים בפילטרים שנבחרו. <button onclick="window.gitaClearFilters()">נקה פילטרים</button></div>`;
      return;
    }
    grid.innerHTML = filtered.map((c, i) => {
      const saveNIS = Math.round(c.israelNIS - c.landedNIS);
      return `
      <article class="vcard" onclick="openVDP('${c.slug}')" data-magnet-parallax>
        <div class="vcard-media" style="background:${gradFor(c.body, fuelOf(c))}">
          <div class="vcard-glow"></div>
          <img class="vcard-img" src="./images/car-${c.slug}.png" alt="${c.name}" loading="lazy" data-parallax="1" />
          <div class="vcard-grain"></div>
          <span class="vcard-badge" data-parallax="0.5">חיסכון ${c.savePct}%</span>
        </div>
        <div class="vcard-body">
          <div class="vcard-make">${makeOf(c)} · ${c.year || ''}</div>
          <h3>${c.name}</h3>
          <div class="vcard-specs">
            <span>${fuelLabel(fuelOf(c))}</span>
            <span>${c.hp || '-'} כ"ס</span>
            <span>0-100: ${c.zero100 || '-'}s</span>
          </div>
          <div class="vcard-prices">
            <div class="vcard-landed">${fmtILS(c.landedNIS)}</div>
            <div class="vcard-strike">${fmtILS(c.israelNIS)}</div>
          </div>
          <div class="vcard-save">חוסך ${fmtILS(saveNIS)}</div>
          <button class="vcard-cta">צפה בפרטים מלאים</button>
        </div>
      </article>`;
    }).join('');
  }
  window.gitaClearFilters = clearFilters;

  // ============================================================
  // VDP — cars.com-grade vehicle detail page
  // ============================================================
  function openVDP(slug) {
    const c = CARS.find(x => x.slug === slug);
    if (!c) return;
    const ov = $('#vdpOverlay');
    const cont = $('#vdpContent');
    const saveNIS = Math.round(c.israelNIS - c.landedNIS);

    const colorChips = (c.colors || []).map(col =>
      `<button class="vdp-color" title="${col.hex}" style="background:${col.code}"><span>${col.hex}</span></button>`
    ).join('');

    const trimRows = (c.trims || []).map(t => `
      <div class="vdp-trim">
        <div class="vdp-trim-head">
          <h5>${t.name}</h5>
          <span>${t.delta ? '+' + fmtUSD(t.delta) : 'סטנדרט'}</span>
        </div>
        <ul>${(t.items || []).map(x => `<li>${x}</li>`).join('')}</ul>
      </div>`).join('');

    const pkgRows = (c.packages || []).map(p => `
      <div class="vdp-pkg">
        <div class="vdp-pkg-head">
          <h5>${p.name}</h5>
          <span>+${fmtUSD(p.price)}</span>
        </div>
        <ul>${(p.items || []).map(x => `<li>${x}</li>`).join('')}</ul>
      </div>`).join('');

    const featRows = (c.features || []).map(f => `<li>${f}</li>`).join('');
    const safetyRows = (c.safety || []).map(f => `<li>${f}</li>`).join('');

    cont.innerHTML = `
      <div class="vdp-hero">
        <div class="vdp-hero-bg" style="background:${gradFor(c.body, fuelOf(c))}">
          <div class="vdp-hero-glow"></div>
          <img class="vdp-hero-img" src="./images/car-${c.slug}.png" alt="${c.name}" />
        </div>
        <div class="vdp-hero-text">
          <div class="vdp-eyebrow">${makeOf(c)} · ${c.year || ''} · #${c.rank} בחיסכון</div>
          <h1>${c.name}</h1>
          <p>${c.nameEn}</p>
        </div>
      </div>

      <div class="vdp-layout">
        <div class="vdp-main">

          <!-- Quick specs strip -->
          <div class="vdp-quick">
            <div><span>הנעה</span><b>${c.drivetrain || '-'}</b></div>
            <div><span>מנוע</span><b>${c.engine || '-'}</b></div>
            <div><span>כ"ס</span><b>${c.hp || '-'}</b></div>
            <div><span>מומנט</span><b>${c.torque || '-'} Nm</b></div>
            <div><span>0-100</span><b>${c.zero100 || '-'}s</b></div>
            <div><span>מהירות מרבית</span><b>${c.topSpeed || '-'} קמ"ש</b></div>
            <div><span>ת. הילוכים</span><b>${c.transmission || '-'}</b></div>
            <div><span>מושבים</span><b>${c.seats || '-'}</b></div>
          </div>

          <!-- Description / note -->
          ${c.note ? `<div class="vdp-note">${c.note}</div>` : ''}

          <!-- Colors -->
          ${(c.colors && c.colors.length) ? `
          <section class="vdp-sec">
            <h3>צבעים זמינים <span class="vdp-count">${c.colors.length}</span></h3>
            <div class="vdp-colors">${colorChips}</div>
          </section>` : ''}

          <!-- Trims -->
          ${(c.trims && c.trims.length) ? `
          <section class="vdp-sec">
            <h3>גימור / Trim <span class="vdp-count">${c.trims.length}</span></h3>
            <div class="vdp-trims">${trimRows}</div>
          </section>` : ''}

          <!-- Packages -->
          ${(c.packages && c.packages.length) ? `
          <section class="vdp-sec">
            <h3>חבילות אופציונליות <span class="vdp-count">${c.packages.length}</span></h3>
            <div class="vdp-pkgs">${pkgRows}</div>
          </section>` : ''}

          <!-- Features -->
          ${(c.features && c.features.length) ? `
          <section class="vdp-sec">
            <h3>פיצ'רים סטנדרטיים <span class="vdp-count">${c.features.length}</span></h3>
            <ul class="vdp-feat">${featRows}</ul>
          </section>` : ''}

          <!-- Safety -->
          ${(c.safety && c.safety.length) ? `
          <section class="vdp-sec">
            <h3>בטיחות <span class="vdp-count">${c.safety.length}</span></h3>
            <ul class="vdp-feat safety">${safetyRows}</ul>
          </section>` : ''}

          <!-- Dimensions -->
          <section class="vdp-sec">
            <h3>מידות וביצועים</h3>
            <div class="vdp-dims">
              ${c.length ? `<div><span>אורך</span><b>${c.length} מ"מ</b></div>` : ''}
              ${c.width ? `<div><span>רוחב</span><b>${c.width} מ"מ</b></div>` : ''}
              ${c.height ? `<div><span>גובה</span><b>${c.height} מ"מ</b></div>` : ''}
              ${c.weight ? `<div><span>משקל</span><b>${c.weight} ק"ג</b></div>` : ''}
              ${c.cargo ? `<div><span>מטען</span><b>${c.cargo} L</b></div>` : ''}
              ${c.fuelTank ? `<div><span>מיכל</span><b>${c.fuelTank} L</b></div>` : ''}
              ${c.range ? `<div><span>טווח</span><b>${c.range} ק"מ</b></div>` : ''}
              ${c.towing ? `<div><span>גרירה</span><b>${c.towing} ק"ג</b></div>` : ''}
              ${c.mpg ? `<div><span>צריכה</span><b>${c.mpg} MPG</b></div>` : ''}
            </div>
          </section>

          <!-- Origin / source -->
          <section class="vdp-sec meta">
            ${c.origin ? `<div><span>מקור ייצור</span><b>${c.origin}</b></div>` : ''}
            ${c.warranty ? `<div><span>אחריות</span><b>${c.warranty}</b></div>` : ''}
            ${c.source ? `<div><span>מקור הצעה</span><b>${c.source}</b></div>` : ''}
          </section>

        </div>

        <!-- Sticky price box -->
        <aside class="vdp-aside">
          <div class="vdp-price-box">
            <div class="vdp-badge">חיסכון של ${c.savePct}%</div>
            <div class="vdp-price-main">${fmtILS(c.landedNIS)}</div>
            <div class="vdp-price-lbl">מחיר סופי בישראל — כולל הכל</div>

            <div class="vdp-price-strike">
              <span>מחיר יבואן רשמי</span>
              <b>${fmtILS(c.israelNIS)}</b>
            </div>
            <div class="vdp-price-save">
              חוסך <b>${fmtILS(saveNIS)}</b>
            </div>

            <div class="vdp-breakdown">
              <h6>פירוט עלויות</h6>
              <div class="vbl"><span>MSRP בארה"ב</span><b>${fmtUSD(c.msrp)}</b></div>
              <div class="vbl"><span>מס קנייה</span><b>${fmtILS(c.purchaseTax * FX)}</b></div>
              <div class="vbl"><span>מע"מ 18%</span><b>${fmtILS(c.vat * FX)}</b></div>
              <div class="vbl"><span>שילוח</span><b>${fmtUSD(c.shipping)}</b></div>
              <div class="vbl total"><span>סה"כ סופי</span><b>${fmtILS(c.landedNIS)}</b></div>
            </div>

            <button class="vdp-cta" onclick="window.gitaOpenWA('${c.slug}')">פתח תיק ₪500</button>
            <button class="vdp-cta ghost" onclick="window.gitaOpenWA('${c.slug}')">שאל שאלה בוואטסאפ</button>
            <p class="vdp-disclaimer">המחירים להמחשה. USD/ILS = ${FX}. החזר מלא של דמי פתיחה אם אין התאמה תוך 30 יום.</p>
          </div>
        </aside>
      </div>
    `;

    ov.classList.add('open');
    document.body.style.overflow = 'hidden';
  }
  function closeVDP() {
    $('#vdpOverlay').classList.remove('open');
    document.body.style.overflow = '';
  }
  window.openVDP = openVDP;
  window.closeVDP = closeVDP;

  // ============================================================
  // FAQ
  // ============================================================
  function buildFAQ() {
    const list = $('#faqList');
    if (!list || typeof FAQ === 'undefined') return;
    list.innerHTML = FAQ.map((f, i) => `
      <details class="faq-item" ${i === 0 ? 'open' : ''}>
        <summary>
          <span class="faq-q">${f.q}</span>
          <span class="faq-icon">+</span>
        </summary>
        <div class="faq-a">${f.a}</div>
      </details>
    `).join('');
  }

  // ============================================================
  // BLOG modal (USD/regulation/hidden)
  // ============================================================
  const blogs = {
    usd: {
      title: 'שיא של כל הזמנים — דולר ב-2.93 ₪',
      tag: 'שווקים',
      body: `
        <p>שער הדולר/שקל ירד אל 2.93 ₪ — הרמה הנמוכה ביותר זה כ-7 שנים — ופותח חלון הזדמנות חד-פעמי לרוכשי רכב פרטיים בישראל. רכישת רכב יוקרה מארה״ב, שעלה לפני שנה ב-3.45 ₪, חוסכת כיום עשרות אלפי שקלים נוספים מעבר לפער המסחרי הקיים.</p>
        <h4>איך זה משפיע בפועל?</h4>
        <ul>
          <li>רכב MSRP של $100,000 — עלות הרכישה יורדת מ-345K₪ ל-293K₪. חיסכון מיידי של ₪52K רק מהשער.</li>
          <li>מס הקנייה (43-101%) ומע"מ (18%) מחושבים גם הם על בסיס שווי דולרי נמוך יותר.</li>
          <li>סה"כ — רכב מחיר סופי שעלה בעבר ₪650K, עלול לעלות כעת ₪580K, חיסכון של ₪70K.</li>
        </ul>
        <h4>למה זה אולי לא יחזיק זמן רב?</h4>
        <p>תחזיות בנק ישראל ושוק האג"ח מצביעות על תיקון פוטנציאלי בחודשים הקרובים. הזדמנויות מהסוג הזה נסגרות מהר. אם יש לכם רכב בכוונת רכישה — זה הזמן לפתוח תיק ולנעול את השער הנוכחי.</p>
      `
    },
    regulation: {
      title: 'תיקון חוק היבוא 2026 — הקלות חדשות',
      tag: 'רגולציה',
      body: `
        <p>משרד התחבורה אישר במהלך 2026 תיקון משמעותי לתקנות היבוא האישי שמרחיב את אפשרויות הקונים, במיוחד בכל הנוגע לרכבי EV ו-PHEV.</p>
        <h4>השינויים העיקריים:</h4>
        <ul>
          <li><b>הקלת מס קנייה ל-EV:</b> ירידה מ-55% ל-45% עבור רכבים חשמליים מתחת ל-₪400K MSRP.</li>
          <li><b>הסרת חסם הגיל:</b> רכבי 2-3 שנים מאושרים כעת ליבוא במסלול אישי מואץ.</li>
          <li><b>הכרה דיגיטלית בדו"ח Carfax:</b> מקצר את תהליך הרישוי בכ-3 שבועות.</li>
          <li><b>תקני בטיחות חופפים:</b> רכבים שעומדים ב-FMVSS האמריקאי מקבלים פטור אוטומטי מתקני התאמה מסוימים.</li>
        </ul>
        <h4>למי זה רלוונטי?</h4>
        <p>קונים של Tesla, Lucid, Rivian, Kia EV9, BMW iX וכל רכב חשמלי תחת ₪400K — חוסכים בממוצע 8% נוספים על העלות הסופית. הצוות שלנו כבר עדכן את כל חישובי המס שלנו לתקנות החדשות.</p>
      `
    },
    hidden: {
      title: '3 דגמים שלא ראית בישראל — אבל זמינים דרכנו',
      tag: 'פנינים נסתרות',
      body: `
        <h4>1. Lucid Air Pure</h4>
        <p>הסדאן החשמלי שכבש את ארה״ב — 660 ק"מ טווח, פנים מינימליסטי, מסך 34" מעוקל. לא משווק בישראל. עלות מחיר סופי: כ-₪655K. מחיר יבואן רשמי לסדאן דומה (Tesla Model S Long Range): ₪800K+.</p>
        <h4>2. Rivian R1S Dual-Motor</h4>
        <p>SUV חשמלי 7 מקומות עם יכולות שטח אמיתיות, 540 כ"ס, 0-100 ב-3.4s. אינו זמין באופן רשמי בישראל. מחיר סופי: כ-₪745K. אלטרנטיבה אמריקאית ייחודית ל-G-Class או X7 ללא הפרמיה.</p>
        <h4>3. Cadillac Escalade IQ</h4>
        <p>דגל הדגלים החשמלי של GM — 7 מקומות, 750 כ"ס, מסך 55" צמוד. דגם 2025/2026. בישראל קיים רק Escalade בנזין דרך יבואן. דרכנו זמין במחיר סופי שמתחיל מ-₪780K, ביצועים ומותרות ברמה אחרת לגמרי.</p>
        <p style="margin-top:24px"><b>הצוות שלנו מתמחה ביבוא דגמים שאינם זמינים בארץ.</b> כל רכב נבדק פיזית, מתועד בסרטוני 4K, ומגיע עם דו"ח Carfax מלא.</p>
      `
    }
  };
  window.openBlog = (key) => {
    const b = blogs[key];
    if (!b) return;
    let m = $('#blogModal');
    if (!m) {
      m = document.createElement('div');
      m.id = 'blogModal';
      m.className = 'blog-modal';
      m.innerHTML = `<button class="blog-modal-x" onclick="document.getElementById('blogModal').classList.remove('open')">×</button><div class="blog-modal-body"></div>`;
      document.body.appendChild(m);
    }
    $('.blog-modal-body', m).innerHTML = `<span class="blog-modal-tag">${b.tag}</span><h2>${b.title}</h2>${b.body}`;
    m.classList.add('open');
  };

  // ============================================================
  // WHATSAPP CHATBOT — keyword-based, Excel constants
  // ============================================================
  const WA_KB = {
    'מחיר': 'המחירים שלנו שקופים לחלוטין. הנוסחה: MSRP בארה״ב × USD/ILS (2.93) + מס קנייה (43-101% לבנזין, 35-55% ל-EV) + מע״מ 18% + שילוח $2,000 + מכס ₪2,000 + עמלה 5% − הנחה בלעדית $3,000. בממוצע אנחנו חוסכים ללקוחות ₪348K מול היבואן הרשמי. רוצה לראות חישוב מלא לרכב ספציפי?',
    'תהליך': '6 שלבים פשוטים: 1) טופס קצר 60s, 2) פתיחת תיק ₪500 (החזר מלא אם אין התאמה), 3) הצעת רכב תוך 72h עם 3 חלופות, 4) בדיקת 200 נקודות + סרטון, 5) שילוח ימי 8-12 שבועות, 6) רישוי+מסירה בארץ. הכל מסונכרן בפורטל אישי.',
    'מיסים': 'בישראל יש 3 רכיבי מס: מס קנייה — 43-101% לבנזין, 35-55% ל-EV/PHEV (תלוי בזיהום וביצועים). מע"מ — 18% על הכל. ירידת ערך — מסילקה מהמדרגה הראשונה ברכבי 0 ק"מ. כל המסים מחושבים מראש בפורטל הלקוחות לפני שאתה מתחייב.',
    'יד שניה': 'אנחנו מתמחים גם ביד שניה איכותית מארה״ב. רכב 2-3 שנים בן 30,000 מייל = חיסכון של 25-40% נוסף לעומת חדש. כולל דו״ח Carfax מלא, בדיקת 200 נקודות, סרטוני בדיקה. רוב הלקוחות בוחרים יד שניה — זהו הסוד של היבוא האישי.',
    'זמן': 'מהזמנה למסירה: 8-12 שבועות בסה״כ. זמן קצר להצעת רכב, 2-3 שבועות לרכישה ובדיקות בארה״ב, 4-5 שבועות שילוח ימי, 1-2 שבועות לרישוי בארץ. הכל מתועד בפורטל בזמן אמת.',
    'אחריות': 'אחריות יצרן בינלאומית במידה והיא חלה. בנוסף — אחריות יבוא אישי שלנו ל-24 חודש על מרכיבי המנוע וההנעה. ביטוח שילוח 100%. החזר מלא של דמי פתיחת תיק (₪500) אם לא מצאנו רכב מתאים תוך 30 יום.',
    'מימון': 'אנחנו עובדים עם 4 חברות מימון בישראל המתמחות ביבוא אישי. ריבית החל מ-3.9%, מימון עד 75% מערך הרכב, תקופה עד 84 חודשים. אישור עקרוני תוך 48 שעות. ההון העצמי הנדרש: 25% + עלויות מס+רישוי.',
    'שילוח': 'שתי שיטות שילוח: RoRo (זול יותר, ~$2,500, רק לרכבים תקינים) או קונטיינר (~$3,800, מומלץ לרכבי יוקרה). ביטוח שילוח 100% מערך הרכב. מעקב חי בפורטל כל יום. נמלי יציאה: באלטימור / NJ / סבנה. יעד: חיפה.',
    'ev': 'רכבי EV נהנים מהטבת מס משמעותית — מס קנייה 35-55% במקום 43-101%. הדגמים החזקים שלנו: Tesla Model X (חוסך ₪300K+), Lucid Air, Rivian R1S, G580 EQ. שים לב: מטענים מתאימים לישראל כלולים בהתאמה לפני המסירה.',
    'g63': 'מרצדס G63 AMG — דגם הדגל שלנו. MSRP $184,900, מחיר יבואן בארץ ₪2.1M, מחיר המחיר הסופי שלנו ~₪1.18M. חיסכון של $312K (78%). V8 Bi-Turbo 577 כ"ס, 0-100 ב-4.5s. רוצה לפתוח תיק?',
    'g580': 'מרצדס G580 EQ — דגם החיסכון הגבוה בקטלוג. SUV חשמלי עם הופעת G-Class. חיסכון מוחלט של ₪900K+ מול היבואן. דגם 2025 חדש לגמרי, 587 כ"ס, 4 מנועים נפרדים לכל גלגל.',
    'ביטוח': 'אנחנו מסדרים ביטוח חובה ומקיף לפני המסירה. אנחנו עובדים עם הראל, מנורה, איילון — והמחירים זהים ליבואן הרשמי. שים לב: רכב יבוא אישי לעיתים זוכה לפרמיה דומה ולפעמים אפילו נמוכה יותר במקיף.',
    'סוכן': 'יש לנו צוות של 8 יועצי רכב מומחים, כל אחד עם 10+ שנות ניסיון בשוק האמריקאי. כל לקוח מקבל יועץ אישי שמלווה לאורך כל התהליך. רוצה לדבר עם יועץ? השאר טלפון ונחזור אליך תוך 4 שעות.'
  };

  const WA_QUICKS = ['💰 מחיר', '🚗 תהליך', '📊 מיסים', '⏱ זמן', '🔧 יד שניה', '⚡ EV', '🛡 אחריות', '💳 מימון', '🚢 שילוח'];

  function waReply(text) {
    const t = (text || '').toLowerCase();
    // keyword match
    for (const k of Object.keys(WA_KB)) {
      if (t.includes(k.toLowerCase())) return WA_KB[k];
    }
    if (/שלום|היי|הי|hello|hi/i.test(text)) return 'שלום וברוך הבא ל-GITA! אני הסוכן המומחה שלנו ליבוא רכבי יוקרה מארה״ב. במה אוכל לעזור? לחץ על אחת הכפתורים למטה או שאל שאלה.';
    if (/תודה|thanks/i.test(text)) return 'בכיף 😊 משהו נוסף? אם אתה רוצה לפתוח תיק ב-₪500 (החזר מלא אם אין התאמה) — פשוט כתוב "פתח תיק".';
    if (/פתח תיק/.test(text)) return 'מעולה! נשמח לפתוח לך תיק. אנא השאר: שם מלא + טלפון + רכב/קטגוריה רצויה + תקציב. יועץ מומחה יחזור אליך תוך 4 שעות עם הצעה מותאמת. או חייג ישירות: 050-000-0000';
    return 'אני מתמחה ביבוא אישי של רכבי יוקרה מארה״ב. נסה לשאול על: מחיר, תהליך, מיסים, יד שניה, EV, מימון, שילוח, או דגם ספציפי כמו G63 / G580 / Tesla / Bronco.';
  }

  function waAdd(role, text) {
    const body = $('#waBody');
    const bub = document.createElement('div');
    bub.className = 'wa-bub ' + role;
    bub.innerHTML = text;
    body.appendChild(bub);
    body.scrollTop = body.scrollHeight;
  }

  function buildWA() {
    const fab = $('#waFab');
    const panel = $('#waPanel');
    const quick = $('#waQuick');
    const input = $('#waInput');
    const send = $('#waSend');
    if (!fab || !panel) return;

    fab.addEventListener('click', () => {
      panel.classList.toggle('open');
      const badge = $('.wa-badge', fab);
      if (badge) badge.style.display = 'none';
      if (panel.classList.contains('open') && !panel.dataset.greeted) {
        panel.dataset.greeted = '1';
        setTimeout(() => waAdd('bot', 'שלום! אני הסוכן המומחה של GITA 🚗<br>במה אוכל לעזור היום?'), 200);
      }
    });

    quick.innerHTML = WA_QUICKS.map(q => `<button class="wa-qb" data-q="${q.replace(/^\S+\s/, '')}">${q}</button>`).join('');
    $$('#waQuick .wa-qb').forEach(b => b.addEventListener('click', () => {
      const q = b.dataset.q;
      waAdd('me', q);
      setTimeout(() => waAdd('bot', waReply(q)), 450);
    }));

    const doSend = () => {
      const v = input.value.trim();
      if (!v) return;
      waAdd('me', v);
      input.value = '';
      setTimeout(() => waAdd('bot', waReply(v)), 500);
    };
    send.addEventListener('click', doSend);
    input.addEventListener('keydown', e => { if (e.key === 'Enter') doSend(); });
  }

  // External openers (used by VDP)
  window.gitaOpenWA = (slug) => {
    const panel = $('#waPanel');
    panel.classList.add('open');
    const c = CARS.find(x => x.slug === slug);
    if (c && !panel.dataset['veh-' + slug]) {
      panel.dataset['veh-' + slug] = '1';
      setTimeout(() => waAdd('bot', `נראה שאתה מתעניין ב<b>${c.name}</b> — חיסכון של ${c.savePct}% (₪${Math.round((c.israelNIS - c.landedNIS) / 1000)}K). אשמח לעזור! שאל מה שתרצה או לחץ "פתח תיק".`), 300);
    }
  };

  // ============================================================
  // NAV — mobile burger
  // ============================================================
  function buildNav() {
    const burger = $('#burger');
    const links = $('.mb-nav-links');
    if (!burger || !links) return;
    burger.addEventListener('click', () => links.classList.toggle('open'));
    $$('.mb-nav-links a').forEach(a => a.addEventListener('click', () => links.classList.remove('open')));
  }

  // ============================================================
  // INIT
  // ============================================================
  document.addEventListener('DOMContentLoaded', () => {
    try { buildNav(); } catch (e) { console.error('nav', e); }
    try { buildHero(); } catch (e) { console.error('hero', e); }
    try { buildBoard(); } catch (e) { console.error('board', e); }
    try { buildFilters(); renderCatalog(); } catch (e) { console.error('catalog', e); }
    try { buildFAQ(); } catch (e) { console.error('faq', e); }
    try { buildWA(); } catch (e) { console.error('wa', e); }
  });
})();
