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
    const active = current === item.href ? 'active' : '';
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
        <img class="brand-wordmark" src="/assets/images/logo/lbt_logo_transparent.png" alt="Linking Bridges Transportation Logo">
      </a>
      <button class="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
        <span></span>
        <span></span>
        <span></span>
      </button>
      <ul class="nav-links" id="main-nav">
        ${navMarkup}
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
    item.addEventListener('click', (event) => {
      if (window.innerWidth <= 760) {
        event.preventDefault();
        item.classList.toggle('open');
      }
    });
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
          <img class="brand-wordmark" src="/assets/images/logo/lbt_logo_transparent.png" alt="Linking Bridges Transportation Logo" style="filter: brightness(0) invert(1);">
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
          <li><a href="about.html">About</a></li>
          <li><a href="fleet.html">Our Fleet</a></li>
          <li><a href="operations.html">Operations</a></li>
          <li><a href="gallery.html">Gallery</a></li>
        </ul>
      </div>
      <div>
        <h4>Services</h4>
        <ul>
          <li><a href="customs-clearance.html">Customs Clearance</a></li>
          <li><a href="transportation-services.html">Transportation</a></li>
          <li><a href="warehousing-services.html">Warehousing</a></li>
          <li><a href="packaging-moving-services.html">Packaging & Moving</a></li>
          <li><a href="storage-delivery-services.html">Storage & Delivery</a></li>
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
        <p>© ${year} Linking Bridges. All rights reserved. ISO 9001 certified logistics operations.</p>
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

showLoader();
renderHeader();
renderFooter();
revealOnScroll();
animateCounters();
handleForm();

const hero = document.querySelector('.hero');
if (hero) {
  window.addEventListener('scroll', () => {
    const offset = window.scrollY * 0.12;
    hero.style.backgroundPositionY = `${offset}px`;
  }, { passive: true });
}
