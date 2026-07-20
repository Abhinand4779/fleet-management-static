import os

css = '''

/* ==============================================
   CRISP PREMIUM LIGHT THEME (SUBPAGES)
   ============================================== */

body.premium-light {
  background: #f8fafc; /* Very subtle cool off-white */
  color: #334155;
}

/* Ensure the hero section remains cinematic (dark background image needs white text) */
body.premium-light .cin-hero-content h1,
body.premium-light .page-hero h1 {
  color: #ffffff !important;
  text-shadow: 0 4px 25px rgba(0,0,0,0.5);
}

body.premium-light .cin-hero-sub,
body.premium-light .section-intro {
  color: rgba(255, 255, 255, 0.9) !important;
  text-shadow: 0 2px 10px rgba(0,0,0,0.5);
}

body.premium-light .breadcrumb,
body.premium-light .breadcrumb a {
  color: rgba(255, 255, 255, 0.8) !important;
}

body.premium-light .breadcrumb a:hover {
  color: #ffffff !important;
}

body.premium-light .cin-eyebrow,
body.premium-light .eyebrow {
  background: linear-gradient(135deg, #d6b86d, #b0914f) !important;
  color: #0b0e14 !important;
  box-shadow: 0 4px 15px rgba(214, 184, 109, 0.4) !important;
  border: none;
}

/* Typography on light background */
body.premium-light main h2,
body.premium-light .section-title,
body.premium-light .pdf-section-title {
  color: #0f172a;
  font-family: 'Poppins', sans-serif;
  font-weight: 800;
}

body.premium-light main h3 {
  color: #1e293b;
}

body.premium-light main p {
  color: #475569;
  line-height: 1.8;
}

body.premium-light main strong {
  color: #0f172a;
}

/* Premium White Cards */
body.premium-light .card,
body.premium-light .info-card,
body.premium-light .gallery-card,
body.premium-light .pdf-stat-box,
body.premium-light .quote-panel {
  background: #ffffff !important;
  border: 1px solid rgba(0, 0, 0, 0.05) !important;
  border-radius: var(--radius-lg) !important;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.04) !important;
  transition: all 0.4s cubic-bezier(0.2, 0.8, 0.2, 1) !important;
}

body.premium-light .card:hover,
body.premium-light .info-card:hover,
body.premium-light .pdf-stat-box:hover {
  transform: translateY(-5px) !important;
  box-shadow: 0 20px 50px rgba(0, 0, 0, 0.08) !important;
  border-color: rgba(0, 0, 0, 0.08) !important;
}

body.premium-light .info-card {
  border-top: 3px solid #d6b86d !important;
}

/* Service Grids */
body.premium-light .services-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2.5rem;
}

body.premium-light .svc-card {
  position: relative;
  display: block;
  background: #ffffff;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: var(--radius-lg);
  padding: 3rem 2.5rem;
  text-decoration: none;
  overflow: hidden;
  transition: all 0.5s var(--transition);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.03);
}

body.premium-light .svc-card::before {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(135deg, rgba(214, 184, 109, 0.05), transparent 60%);
  opacity: 0;
  transition: opacity 0.5s ease;
  z-index: 0;
}

body.premium-light .svc-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 40px rgba(0, 0, 0, 0.08), 0 0 20px rgba(214, 184, 109, 0.05);
  border-color: rgba(214, 184, 109, 0.2);
}

body.premium-light .svc-card:hover::before {
  opacity: 1;
}

body.premium-light .svc-card > * {
  position: relative;
  z-index: 1;
}

body.premium-light .svc-card-icon,
body.premium-light .card .icon {
  width: 64px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: #f8fafc;
  border: 1px solid rgba(0, 0, 0, 0.05);
  border-radius: 16px;
  color: #b0914f;
  margin-bottom: 2rem;
  transition: all 0.5s ease;
}

body.premium-light .svc-card:hover .svc-card-icon,
body.premium-light .card:hover .icon {
  background: rgba(214, 184, 109, 0.08);
  border-color: rgba(214, 184, 109, 0.2);
  transform: scale(1.05);
}

body.premium-light .svc-card-num {
  position: absolute;
  top: 2rem;
  right: 2rem;
  font-size: 4rem;
  font-weight: 800;
  color: rgba(0, 0, 0, 0.03);
  line-height: 1;
  transition: all 0.5s ease;
  font-family: 'Poppins', sans-serif;
  z-index: 0;
}

body.premium-light .svc-card:hover .svc-card-num {
  color: rgba(214, 184, 109, 0.1);
  transform: scale(1.1) translate(-10px, 10px);
}

body.premium-light .svc-card h3 {
  color: #0f172a;
  font-size: 1.5rem;
  font-weight: 700;
  font-family: 'Poppins', sans-serif;
  margin-bottom: 1rem;
}

body.premium-light .svc-card p {
  color: #475569;
  line-height: 1.7;
  font-size: 1.05rem;
  margin-bottom: 2.5rem;
}

body.premium-light .svc-card-link {
  display: inline-flex;
  align-items: center;
  color: #b0914f;
  font-weight: 700;
  font-size: 0.9rem;
  text-transform: uppercase;
  letter-spacing: 0.1em;
  transition: all 0.3s ease;
}

body.premium-light .svc-card:hover .svc-card-link {
  color: #0f172a;
  letter-spacing: 0.15em;
}

body.premium-light .gradient-text {
  background: linear-gradient(135deg, #b0914f, #d6b86d);
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

/* Forms (Contact Page) */
body.premium-light .quote-form {
  background: transparent !important;
  border: none !important;
  box-shadow: none !important;
  padding: 0 !important;
}

body.premium-light .quote-panel label {
  color: #334155 !important;
  font-weight: 600;
}

body.premium-light input,
body.premium-light textarea,
body.premium-light select {
  background: #f8fafc !important;
  border: 1px solid rgba(0,0,0,0.1) !important;
  color: #0f172a !important;
}

body.premium-light input:focus,
body.premium-light textarea:focus,
body.premium-light select:focus {
  border-color: #d6b86d !important;
  box-shadow: 0 0 0 3px rgba(214, 184, 109, 0.15) !important;
  background: #ffffff !important;
}

body.premium-light input::placeholder,
body.premium-light textarea::placeholder {
  color: #94a3b8 !important;
}

/* Gallery and Partner specific */
body.premium-light .caption {
  background: #ffffff !important;
  border-top: 1px solid rgba(0,0,0,0.05) !important;
}

body.premium-light .caption h3 {
  color: #0f172a !important;
}

body.premium-light .gallery-card img,
body.premium-light .pdf-partner-image img {
  border: 1px solid rgba(0,0,0,0.05);
  box-shadow: 0 10px 30px rgba(0,0,0,0.05);
}

/* Lists */
body.premium-light .list-check li {
  color: #475569;
  border-bottom: 1px solid rgba(0,0,0,0.05);
}

body.premium-light .list-check li strong {
  color: #0f172a;
}

body.premium-light .list-check li::marker {
  color: #b0914f;
}

/* Nav Toggle & Header overrides if needed */
body.premium-light .nav-toggle span {
  background: #0f172a !important;
}

/* Divider Lines */
body.premium-light .pdf-section-title::after,
body.premium-light .section-title::after {
  background: linear-gradient(90deg, #d6b86d, #b0914f);
}

body.premium-light section + section::before {
  content: '';
  position: absolute;
  top: -1rem;
  left: 50%;
  transform: translateX(-50%);
  width: 80px;
  height: 2px;
  background: rgba(214, 184, 109, 0.4);
}

/* Banners */
body.premium-light .banner {
  background: #ffffff !important;
  border: 1px solid rgba(0,0,0,0.05) !important;
  box-shadow: 0 15px 50px rgba(0,0,0,0.06) !important;
}

body.premium-light .banner strong {
  color: #0f172a !important;
}

body.premium-light .banner p {
  color: #475569 !important;
}

/* Footer on Light Pages */
body.premium-light .site-footer {
  background: #0f172a !important;
  border-top: none;
}
'''

with open('assets/css/styles.css', 'a', encoding='utf-8') as f:
    f.write(css)

print("Injected body.premium-light CSS")
