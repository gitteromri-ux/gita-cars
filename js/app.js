// ===== HERO ROTATION =====
(function() {
  const slides = document.querySelectorAll('.hero-slide');
  const dots = document.querySelectorAll('.hero-dot');
  let current = 0;

  function go(i) {
    slides[current].classList.remove('active');
    dots[current].classList.remove('active');
    current = i;
    slides[current].classList.add('active');
    dots[current].classList.add('active');
  }

  dots.forEach((d, i) => d.addEventListener('click', () => go(i)));
  setInterval(() => go((current + 1) % slides.length), 5000);
})();

// ===== CATALOG GRID =====
(function() {
  const grid = document.getElementById('catalog-grid');
  if (!grid) return;

  grid.innerHTML = CARS.map(c => `
    <article class="car-card" data-id="${c.id}">
      <div class="car-img-wrap">
        <img src="${c.img}" alt="${c.name}" loading="lazy">
      </div>
      <div class="car-info">
        <div class="car-eyebrow">${c.eyebrow}</div>
        <h3 class="car-name">${c.name}</h3>
        <div class="car-specs">
          <div class="car-spec">
            <div class="car-spec-val">${c.specs.accel}</div>
            <div class="car-spec-label">0-100</div>
          </div>
          <div class="car-spec">
            <div class="car-spec-val">${c.specs.hp}</div>
            <div class="car-spec-label">HP</div>
          </div>
          <div class="car-spec">
            <div class="car-spec-val">${c.specs.torque}</div>
            <div class="car-spec-label">${c.specs.engine === 'EV' ? 'Torque' : 'N·m'}</div>
          </div>
        </div>
        <div class="car-price-row">
          <div class="car-price-block">
            <div class="car-price-label">המחיר שלנו</div>
            <div class="car-price">₪${fmt(c.ourPrice)}</div>
            <div class="car-price-old">יבואן: ₪${fmt(c.dealerPrice)}</div>
          </div>
          <div class="car-save-badge">-${calcPct(c)}%</div>
        </div>
      </div>
    </article>
  `).join('');

  // Click handler
  grid.addEventListener('click', e => {
    const card = e.target.closest('.car-card');
    if (!card) return;
    openModal(parseInt(card.dataset.id));
  });
})();

// ===== MODAL =====
function openModal(id) {
  const car = CARS.find(c => c.id === id);
  if (!car) return;

  const modal = document.getElementById('car-modal');
  const content = document.getElementById('modal-content');

  const accel = car.specs.accel || '—';
  const hp = car.specs.hp || '—';
  const torque = car.specs.torque || '—';
  const range = car.specs.range || car.specs.mpg || '—';
  const rangeLabel = car.specs.range ? 'טווח' : 'צריכה';

  content.innerHTML = `
    <button class="modal-close" onclick="closeModal()">×</button>
    <div class="modal-hero">
      <img src="${car.img}" alt="${car.name}">
    </div>
    <div class="modal-body">
      <div class="modal-eyebrow">${car.eyebrow}</div>
      <h2 class="modal-name">${car.name}</h2>

      <div class="modal-specs">
        <div class="modal-spec">
          <div class="modal-spec-val">${accel}</div>
          <div class="modal-spec-label">0-100 קמ״ש</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-val">${hp}</div>
          <div class="modal-spec-label">הספק</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-val">${torque}</div>
          <div class="modal-spec-label">מומנט</div>
        </div>
        <div class="modal-spec">
          <div class="modal-spec-val">${range}</div>
          <div class="modal-spec-label">${rangeLabel}</div>
        </div>
      </div>

      <div class="modal-price-block">
        <div class="modal-price-cell">
          <div class="modal-price-cell-label">המחיר שלנו</div>
          <div class="modal-price-cell-val modal-price-cell-our">₪${fmt(car.ourPrice)}</div>
        </div>
        <div class="modal-price-cell">
          <div class="modal-price-cell-label">יבואן רשמי</div>
          <div class="modal-price-cell-val modal-price-cell-dealer">₪${fmt(car.dealerPrice)}</div>
        </div>
        <div class="modal-price-cell">
          <div class="modal-price-cell-label">החיסכון שלך</div>
          <div class="modal-price-cell-val modal-price-cell-save">-₪${fmt(calcSave(car))}</div>
        </div>
      </div>

      <h3 style="font-family:'Heebo'; font-size:18px; font-weight:500; margin-bottom:16px; letter-spacing:-0.01em;">מפרט וציוד</h3>
      <div class="modal-features-grid">
        ${car.features.map(f => `<div class="modal-feature">${f}</div>`).join('')}
      </div>

      <div class="modal-cta">
        <a href="#" class="btn-primary" style="flex:1; text-align:center;">פתח תיק רכישה — ₪500</a>
        <a href="#" class="btn-ghost" style="flex:1; text-align:center;">דבר עם נציג</a>
      </div>
    </div>
  `;

  modal.classList.add('open');
  document.body.style.overflow = 'hidden';
}

function closeModal() {
  document.getElementById('car-modal').classList.remove('open');
  document.body.style.overflow = '';
}

document.querySelector('.modal-overlay')?.addEventListener('click', closeModal);
document.addEventListener('keydown', e => { if (e.key === 'Escape') closeModal(); });
