const siteHeader = document.getElementById('site-header');
const siteFooter = document.getElementById('site-footer');

function showLoader() {
  if (document.querySelector('.page-loader')) return;
  const loader = document.createElement('div');
  loader.className = 'page-loader';
  loader.innerHTML = `
    <div class="loader-card futuristic" style="background: transparent; box-shadow: none; border: none; align-items: center;" role="status" aria-live="polite">
      <div class="loader-hexagon"></div>
      <div class="loader-title" style="color: #ffffff; letter-spacing: 2px;">LINKING BRIDGES TRANSPORTATION</div>
    </div>`;
  document.body.appendChild(loader);
  document.body.classList.add('is-loading');
  window.setTimeout(() => {
    loader.classList.add('is-hidden');
    document.body.classList.remove('is-loading');
    window.setTimeout(() => loader.remove(), 450);
  }, 1200);
}

const navItems = [
  { label: 'Home', href: '/index.html' },
  { label: 'About', href: '/pages/about.html' },
  { label: 'Our Fleet', href: '/pages/fleet.html' },
  { label: 'Operations', href: '/pages/operations.html' },
  { label: 'Services', href: '/pages/services.html', children: [
    { label: 'Customs Clearance', href: '/pages/customs-clearance.html' },
    { label: 'Transportation Services', href: '/pages/transportation-services.html' },
    { label: 'Warehousing Services', href: '/pages/warehousing-services.html' },
    { label: 'Packaging & Moving Services', href: '/pages/packaging-moving-services.html' },
    { label: 'Storage & Delivery Services', href: '/pages/storage-delivery-services.html' }
  ]},
  { label: 'Gallery', href: '/pages/gallery.html' },
  { label: 'Contact', href: '/pages/contact.html' }
];

function renderHeader() {
  if (!siteHeader) return;
  siteHeader.classList.add('site-header');
  const current = window.location.pathname.split('/').pop() || 'index.html';
  const navMarkup = navItems.map((item) => {
    const itemFile = item.href.split('/').pop();
    const active = current === itemFile ? 'active' : '';
    if (item.children) {
      return `
        <li class="dropdown">
          <a href="${item.href}" class="${active}">${item.label}</a>
          <div class="dropdown-menu">
            ${item.children.map((child) => `<a href="${child.href}">${child.label}</a>`).join('')}
          </div>
        </li>`;
    }
    return `<li><a href="${item.href}" class="${active}">${item.label}</a></li>`;
  }).join('');

  siteHeader.innerHTML = `
    <div class="container header-inner">
      <a class="brand" href="/index.html">
        <img class="brand-wordmark" src="/assets/images/logo/LBT_LOGO_h.png" alt="Linking Bridges Transportation Logo">
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span>
        <span></span>
        <span></span>
      </button>
      <ul class="nav-links" id="main-nav">
        ${navMarkup}
        <li><a class="btn btn-download" href="/assets/downloads/Linking-Bridges-Company-Profile.pdf" download><svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" style="margin-right:6px;vertical-align:middle;"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/><polyline points="7 10 12 15 17 10"/><line x1="12" y1="15" x2="12" y2="3"/></svg>Download Profile</a></li>
        <li><a class="btn btn-primary" href="/pages/contact.html">Request a Quote</a></li>
      </ul>
    </div>`;

  const toggle = siteHeader.querySelector('.nav-toggle');
  const nav = siteHeader.querySelector('.nav-links');
  toggle?.addEventListener('click', () => {
    const expanded = toggle.getAttribute('aria-expanded') === 'true';
    toggle.setAttribute('aria-expanded', String(!expanded));
    toggle.classList.toggle('open');
    nav.classList.toggle('open');
  });

  document.querySelectorAll('.dropdown').forEach((item) => {
    const mainLink = item.querySelector('a');
    if (mainLink) {
      mainLink.addEventListener('click', (event) => {
        if (window.innerWidth <= 1024) {
          event.preventDefault();
          item.classList.toggle('open');
        }
      });
    }
  });
}

function renderFooter() {
  if (!siteFooter) return;
  siteFooter.classList.add('site-footer');
  const year = new Date().getFullYear();
  siteFooter.innerHTML = `
    <div class="container footer-grid">
      <div>
        <a class="brand" href="/index.html" style="margin-bottom: 1.5rem; display:inline-flex; align-items:center;">
          <img class="brand-wordmark" src="/assets/images/logo/LBT_LOGO_h.png" alt="Linking Bridges Transportation Logo">
        </a>
        <p style="margin-bottom: 2rem;">Premium fleet management solutions with reliable transport, customs support, warehousing and delivery services tailored to demanding operations.</p>
        <div style="font-size:0.95rem; color:rgba(255,255,255,0.9);">
          <strong style="color: white; font-size: 1.1rem; text-transform: uppercase;">Head Office</strong>
          <div style="margin-top:0.5rem; line-height:1.6; color:#a0a0a0;">
            7831, Al Khaboub, Al Fadeylah District<br />Jeddah, 22543<br />Kingdom of Saudi Arabia
          </div>
        </div>
      </div>
      <div>
        <h4>Quick Links</h4>
        <ul>
          <li><a href="/pages/about.html">About</a></li>
          <li><a href="/pages/fleet.html">Our Fleet</a></li>
          <li><a href="/pages/operations.html">Operations</a></li>
          <li><a href="/pages/gallery.html">Gallery</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="/pages/customs-clearance.html">Customs Clearance</a></li>
          <li><a href="/pages/transportation-services.html">Transportation</a></li>
          <li><a href="/pages/warehousing-services.html">Warehousing</a></li>
          <li><a href="/pages/packaging-moving-services.html">Packaging & Moving</a></li>
          <li><a href="/pages/storage-delivery-services.html">Storage & Delivery</a></li>
        </ul>
      </div>
      <div>
        <h4>Stay Updated</h4>
        <p>Receive insights on fleet operations and service updates.</p>
        <form class="newsletter">
          <input type="email" placeholder="Email address" aria-label="Email address">
          <button class="btn btn-primary" type="submit" style="padding: 1rem 2rem;">JOIN</button>
        </form>
      </div>
    </div>
    <div class="container footer-bottom">
      <div class="contact-info">
        <p><strong>Email:</strong> <a href="mailto:info@linkingbridges.net">info@linkingbridges.net</a></p>
        <p><strong>Phone:</strong> <a href="tel:+966553311591">+966553311591</a></p>
      </div>
      <div class="copyright">
        <p>&copy; ${year} Linking Bridges. All rights reserved. ISO 9001 certified logistics operations.</p>
      </div>
    </div>`;
}

function revealOnScroll() {
  const items = document.querySelectorAll('.reveal');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.16 });
  items.forEach((item) => observer.observe(item));
}

function animateCounters() {
  const counters = document.querySelectorAll('.counter');
  const observer = new IntersectionObserver((entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        const el = entry.target;
        const target = Number(el.dataset.target || 0);
        const suffix = el.dataset.suffix || '';
        const duration = 1200;
        const start = performance.now();
        const step = (now) => {
          const progress = Math.min((now - start) / duration, 1);
          const value = Math.floor(progress * target);
          el.textContent = `${value}${suffix}`;
          if (progress < 1) requestAnimationFrame(step);
        };
        requestAnimationFrame(step);
        observer.unobserve(el);
      }
    });
  }, { threshold: 0.5 });
  counters.forEach((counter) => observer.observe(counter));
}

function handleForm() {
  const form = document.querySelector('.quote-form');
  if (!form) return;
  form.addEventListener('submit', (event) => {
    event.preventDefault();
    const button = form.querySelector('button[type="submit"]');
    if (button) {
      button.textContent = 'Request Sent';
      button.disabled = true;
    }
    const status = document.createElement('p');
    status.textContent = 'Thank you. Our team will respond within one business day.';
    status.style.color = 'var(--accent)';
    status.style.fontWeight = '700';
    form.appendChild(status);
  });
}

function renderWhatsAppButton() {
  const btn = document.createElement('a');
  btn.href = 'https://wa.me/966553311591';
  btn.target = '_blank';
  btn.className = 'whatsapp-float';
  btn.innerHTML = `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 448 512" width="35" height="35" fill="white"><path d="M380.9 97.1C339 55.1 283.2 32 223.9 32c-122.4 0-222 99.6-222 222 0 39.1 10.2 77.3 29.6 111L0 480l117.7-30.9c32.4 17.7 68.9 27 106.1 27h.1c122.3 0 224.1-99.6 224.1-222 0-59.3-25.2-115-67.1-157.1zm-157 341.6c-33.2 0-65.7-8.9-94-25.7l-6.7-4-69.8 18.3L72 359.2l-4.4-7c-18.5-29.4-28.2-63.3-28.2-98.2 0-101.7 82.8-184.5 184.6-184.5 49.3 0 95.6 19.2 130.4 54.1 34.8 34.9 56.2 81.2 56.1 130.5 0 101.8-84.9 184.6-186.6 184.6zm101.2-138.2c-5.5-2.8-32.8-16.2-37.9-18-5.1-1.9-8.8-2.8-12.5 2.8-3.7 5.6-14.3 18-17.6 21.8-3.2 3.7-6.5 4.2-12 1.4-32.6-16.3-54-29.1-75.5-66-5.7-9.8 5.7-9.1 16.3-30.3 1.8-3.7.9-6.9-.5-9.7-1.4-2.8-12.5-30.1-17.1-41.2-4.5-10.8-9.1-9.3-12.5-9.5-3.2-.2-6.9-.2-10.6-.2-3.7 0-9.7 1.4-14.8 6.9-5.1 5.6-19.4 19-19.4 46.3 0 27.3 19.9 53.7 22.6 57.4 2.8 3.7 39.1 59.7 94.8 83.8 35.2 15.2 49 16.5 66.6 13.9 10.7-1.6 32.8-13.4 37.4-26.4 4.6-13 4.6-24.1 3.2-26.4-1.3-2.5-5-3.9-10.5-6.6z"/></svg>`;
  document.body.appendChild(btn);
}

showLoader();
renderHeader();
renderFooter();
renderWhatsAppButton();
revealOnScroll();
animateCounters();
handleForm();

/* ============================================
   SCROLL-DRIVEN TRUCK ANIMATION
   ============================================ */
const hero = document.querySelector('.hero');
const heroImg = document.querySelector('.hero-image img');

if (hero && heroImg) {
  if (window.innerWidth > 900) {
    const scrollIndicator = document.createElement('div');
    scrollIndicator.className = 'hero-scroll-indicator';
    scrollIndicator.innerHTML = '<span>Scroll</span>';
    hero.appendChild(scrollIndicator);
  }

  let ticking = false;
  window.addEventListener('scroll', () => {
    if (!ticking) {
      requestAnimationFrame(() => {
        const scrollY = window.scrollY;
        const heroHeight = hero.offsetHeight;
        const progress = Math.min(scrollY / heroHeight, 1);
        const translateX = progress * 30;
        const translateY = progress * -8;
        const scale = 1 + progress * 0.04;
        heroImg.style.transform = `translate(${translateX}px, ${translateY}px) scale(${scale})`;
        const indicator = document.querySelector('.hero-scroll-indicator');
        if (indicator) indicator.style.opacity = Math.max(0, 1 - progress * 3);
        ticking = false;
      });
      ticking = true;
    }
  }, { passive: true });
}

/* ============================================
   SERVICES PHOTO CAROUSEL
   ============================================ */
(function initServicesCarousel() {
  const wrapper = document.getElementById('servicesCarousel');
  if (!wrapper) return;

  const track = document.getElementById('carouselTrack');
  const dotsContainer = document.getElementById('scDots');
  const prevBtn = document.getElementById('scPrev');
  const nextBtn = document.getElementById('scNext');
  const slides = Array.from(track.querySelectorAll('.sc-slide'));
  const total = slides.length;
  let current = 0;
  let autoTimer = null;
  let dragStartX = 0;
  let isDragging = false;

  function getSlidesPerView() {
    return window.innerWidth >= 900 ? 3 : 1;
  }

  function getStepCount() {
    return Math.max(1, total - getSlidesPerView() + 1);
  }

  function buildDots() {
    dotsContainer.innerHTML = '';
    const steps = getStepCount();
    for (let i = 0; i < steps; i++) {
      const dot = document.createElement('button');
      dot.className = 'sc-dot' + (i === current ? ' is-active' : '');
      dot.setAttribute('aria-label', 'Slide group ' + (i + 1));
      dot.addEventListener('click', () => goTo(i));
      dotsContainer.appendChild(dot);
    }
  }

  function getSlideOffset() {
    const slideEl = slides[0];
    if (!slideEl) return 0;
    const gap = window.innerWidth >= 900 ? 24 : 0;
    return slideEl.offsetWidth + gap;
  }

  function updateUI() {
    const offset = getSlideOffset();
    track.style.transform = 'translateX(-' + (current * offset) + 'px)';
    const perView = getSlidesPerView();
    slides.forEach((s, i) => {
      s.classList.toggle('is-active', i >= current && i < current + perView);
    });
    dotsContainer.querySelectorAll('.sc-dot').forEach((d, i) => {
      d.classList.toggle('is-active', i === current);
    });
  }

  function goTo(index) {
    const maxStep = getStepCount() - 1;
    current = Math.max(0, Math.min(index, maxStep));
    updateUI();
    resetAuto();
  }

  function resetAuto() {
    clearInterval(autoTimer);
    autoTimer = setInterval(() => {
      const next = (current + 1) >= getStepCount() ? 0 : current + 1;
      goTo(next);
    }, 5000);
  }

  prevBtn.addEventListener('click', () => goTo(current - 1));
  nextBtn.addEventListener('click', () => goTo(current + 1));

  function onDragStart(x) {
    dragStartX = x;
    isDragging = true;
    track.classList.add('is-dragging');
    clearInterval(autoTimer);
  }

  function onDragEnd(x) {
    if (!isDragging) return;
    isDragging = false;
    track.classList.remove('is-dragging');
    const diff = dragStartX - x;
    if (Math.abs(diff) > 50) {
      goTo(diff > 0 ? current + 1 : current - 1);
    } else {
      resetAuto();
    }
  }

  track.addEventListener('mousedown', e => onDragStart(e.clientX));
  window.addEventListener('mouseup', e => onDragEnd(e.clientX));
  track.addEventListener('touchstart', e => onDragStart(e.touches[0].clientX), { passive: true });
  track.addEventListener('touchend', e => onDragEnd(e.changedTouches[0].clientX), { passive: true });

  wrapper.addEventListener('mouseenter', () => clearInterval(autoTimer));
  wrapper.addEventListener('mouseleave', resetAuto);

  wrapper.setAttribute('tabindex', '0');
  wrapper.addEventListener('keydown', e => {
    if (e.key === 'ArrowLeft') goTo(current - 1);
    if (e.key === 'ArrowRight') goTo(current + 1);
  });

  let resizeTimer;
  window.addEventListener('resize', () => {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(() => { current = 0; buildDots(); updateUI(); }, 200);
  });

  buildDots();
  updateUI();
  resetAuto();
})();