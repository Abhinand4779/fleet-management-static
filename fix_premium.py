import re

with open('assets/css/styles.css', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove the old "PREMIUM SUBPAGE HERO OVERRIDES" block we added earlier
content = re.sub(
    r'/\* === PREMIUM SUBPAGE HERO OVERRIDES === \*/.*?transform: translateY\(-5px\) !important;\s*\}',
    '',
    content,
    flags=re.DOTALL
)

# Remove the old "PREMIUM DARK SUBPAGE THEME WITH BLUE STROKES" block
content = re.sub(
    r'/\* =+\s*PREMIUM DARK SUBPAGE THEME WITH BLUE STROKES\s*=+ \*/.*$',
    '',
    content,
    flags=re.DOTALL
)

# Now append the new, properly balanced premium CSS
new_css = '''

/* ==============================================
   PREMIUM DARK SUBPAGE THEME
   ============================================== */

/* Dark page base */
body.dark-page {
  background: #0a0e17;
  color: #cbd5e1;
  position: relative;
}

/* Subtle background texture - thin diagonal strokes, NOT overwhelming */
body.dark-page::before {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background:
    repeating-linear-gradient(
      135deg,
      transparent,
      transparent 100px,
      rgba(59, 130, 246, 0.025) 100px,
      rgba(59, 130, 246, 0.025) 101px
    ),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 150px,
      rgba(59, 130, 246, 0.018) 150px,
      rgba(59, 130, 246, 0.018) 151px
    ),
    radial-gradient(ellipse 800px 600px at 15% 10%, rgba(30, 64, 175, 0.06), transparent),
    radial-gradient(ellipse 600px 400px at 85% 70%, rgba(30, 58, 138, 0.04), transparent);
}

body.dark-page > * {
  position: relative;
  z-index: 1;
}

/* ---- NAV TOGGLE FIX (hamburger invisible on dark) ---- */
body.dark-page .nav-toggle span {
  background: #ffffff !important;
}

body.dark-page .nav-links a {
  color: #e2e8f0;
}

/* ---- HERO TEXT FIX — WHITE, not blue ---- */
body.dark-page .cin-hero-content h1 {
  color: #ffffff !important;
  background: none !important;
  -webkit-background-clip: unset !important;
  -webkit-text-fill-color: #ffffff !important;
  background-clip: unset !important;
  text-shadow: 0 4px 30px rgba(0,0,0,0.5) !important;
}

body.dark-page .cin-hero-sub {
  color: rgba(255,255,255,0.8);
}

body.dark-page .breadcrumb {
  color: rgba(255,255,255,0.6) !important;
}

body.dark-page .breadcrumb a {
  color: rgba(255,255,255,0.8) !important;
}

body.dark-page .breadcrumb a:hover {
  color: #ffffff !important;
}

body.dark-page .cin-eyebrow {
  background: linear-gradient(135deg, #b0914f, #d6b86d) !important;
  color: #0b0e14 !important;
  box-shadow: 0 4px 20px rgba(214, 184, 109, 0.2) !important;
}

/* ---- SECTION TITLES — clean white with gold accent ---- */
body.dark-page .pdf-section-title,
body.dark-page .section-title,
body.dark-page main h2 {
  color: #ffffff;
}

body.dark-page .pdf-section-title::after,
body.dark-page .section-title::after {
  content: '';
  display: block;
  width: 50px;
  height: 3px;
  background: linear-gradient(90deg, #d6b86d, #b0914f);
  margin-top: 0.75rem;
  border-radius: 2px;
}

body.dark-page main h3 {
  color: #f1f5f9;
}

body.dark-page main p {
  color: #94a3b8;
}

body.dark-page main strong {
  color: #e2e8f0;
}

/* ---- CARDS — dark glass, subtle borders, NO heavy blue ---- */
body.dark-page .card {
  background: rgba(15, 23, 42, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  padding: 2rem;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  transition: all 0.4s var(--transition);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}

body.dark-page .card:hover {
  background: rgba(15, 23, 42, 0.7);
  border-color: rgba(255, 255, 255, 0.12);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
  transform: translateY(-4px);
}

body.dark-page .card h3 {
  color: #ffffff;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
}

body.dark-page .card p {
  color: #94a3b8;
}

/* Service card icons — subtle, not neon */
body.dark-page .card .icon {
  width: 60px;
  height: 60px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(214, 184, 109, 0.08);
  border: 1px solid rgba(214, 184, 109, 0.15);
  border-radius: 14px;
  margin-bottom: 1.5rem;
  color: #d6b86d;
  transition: all 0.3s ease;
}

body.dark-page .card:hover .icon {
  background: rgba(214, 184, 109, 0.12);
  border-color: rgba(214, 184, 109, 0.3);
}

/* Gallery cards */
body.dark-page .gallery-card {
  background: rgba(15, 23, 42, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  overflow: hidden;
  padding: 0;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
}

body.dark-page .gallery-card img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  transition: transform 0.6s var(--transition);
}

body.dark-page .gallery-card:hover img {
  transform: scale(1.05);
}

body.dark-page .gallery-card .caption {
  padding: 1.5rem;
}

body.dark-page .gallery-card .caption h3 {
  color: #ffffff;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  margin-bottom: 0.5rem;
}

body.dark-page .gallery-card .caption p {
  color: #94a3b8;
  font-size: 0.95rem;
}

/* Gradient link text — gold accent, not blue */
body.dark-page .gradient-text {
  background: linear-gradient(135deg, #d6b86d, #e8cc85);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
  font-size: 0.9rem;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  display: inline-block;
  margin-top: 1rem;
  transition: opacity 0.3s ease;
}

body.dark-page .gradient-text:hover {
  opacity: 0.8;
}

/* pdf-stat-box on dark pages */
body.dark-page .pdf-stat-box {
  background: rgba(15, 23, 42, 0.5) !important;
  border: 1px solid rgba(255, 255, 255, 0.06) !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25) !important;
  backdrop-filter: blur(8px) !important;
  -webkit-backdrop-filter: blur(8px) !important;
  border-radius: var(--radius-lg) !important;
  padding: 2rem !important;
  transition: all 0.4s var(--transition) !important;
}

body.dark-page .pdf-stat-box:hover {
  background: rgba(15, 23, 42, 0.7) !important;
  border-color: rgba(255, 255, 255, 0.12) !important;
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4) !important;
  transform: translateY(-4px) !important;
}

body.dark-page .pdf-stat-box h3 {
  color: #ffffff;
  font-family: 'Poppins', sans-serif;
}

body.dark-page .pdf-stat-box p {
  color: #94a3b8;
}

/* Partner section images */
body.dark-page .pdf-partner-content h2 {
  color: #ffffff;
}

body.dark-page .pdf-partner-content p {
  color: #94a3b8;
}

body.dark-page .pdf-partner-image img {
  border-radius: var(--radius-lg);
  border: 1px solid rgba(255, 255, 255, 0.06);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.35);
}

/* Forms (contact page) */
body.dark-page .quote-form {
  background: rgba(15, 23, 42, 0.5);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.25);
}

body.dark-page input,
body.dark-page textarea,
body.dark-page select {
  background: rgba(10, 14, 23, 0.7) !important;
  border: 1px solid rgba(255, 255, 255, 0.08) !important;
  color: #e2e8f0 !important;
  border-radius: var(--radius) !important;
  padding: 0.85rem 1.2rem !important;
  transition: border-color 0.3s ease;
}

body.dark-page input:focus,
body.dark-page textarea:focus,
body.dark-page select:focus {
  border-color: rgba(214, 184, 109, 0.3) !important;
  box-shadow: 0 0 0 3px rgba(214, 184, 109, 0.08) !important;
  outline: none;
}

body.dark-page input::placeholder,
body.dark-page textarea::placeholder {
  color: #64748b;
}

body.dark-page label {
  color: #cbd5e1;
  font-weight: 600;
  font-size: 0.9rem;
}

/* Gallery images */
body.dark-page .gallery-grid img {
  border-radius: var(--radius);
  border: 1px solid rgba(255, 255, 255, 0.05);
  transition: all 0.4s ease;
}

body.dark-page .gallery-grid img:hover {
  border-color: rgba(255, 255, 255, 0.12);
  box-shadow: 0 8px 30px rgba(0, 0, 0, 0.35);
}

/* Section divider — subtle golden line */
body.dark-page section + section::before {
  content: '';
  position: absolute;
  top: -1rem;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 1px;
  background: linear-gradient(90deg, transparent, rgba(214, 184, 109, 0.3), transparent);
}

/* Lists */
body.dark-page ul, body.dark-page ol {
  color: #94a3b8;
}

/* Footer on dark page */
body.dark-page .site-footer {
  background: #060911 !important;
  border-top: 1px solid rgba(255, 255, 255, 0.04);
}

/* Mobile nav on dark pages */
@media (max-width: 1024px) {
  body.dark-page .nav-links {
    background: #0f172a !important;
    border: 1px solid rgba(255, 255, 255, 0.06);
  }

  body.dark-page .nav-links a {
    color: #e2e8f0 !important;
    border-bottom: 1px solid rgba(255, 255, 255, 0.04);
  }

  body.dark-page .nav-links a:hover,
  body.dark-page .nav-links a.active {
    color: #d6b86d !important;
  }

  body.dark-page .dropdown-menu {
    background: #1e293b !important;
  }

  body.dark-page .dropdown-menu a {
    color: #cbd5e1 !important;
  }
}

/* Responsive */
@media (max-width: 768px) {
  body.dark-page .card {
    padding: 1.5rem;
  }

  body.dark-page .pdf-stat-box {
    padding: 1.5rem !important;
  }

  body.dark-page .quote-form {
    padding: 1.5rem;
  }

  body.dark-page .gallery-card img {
    height: 180px;
  }
}

'''

content = content.rstrip() + new_css

with open('assets/css/styles.css', 'w', encoding='utf-8') as f:
    f.write(content)

print('Replaced premium CSS - fixed toggle, removed excess blue, applied gold accents')
