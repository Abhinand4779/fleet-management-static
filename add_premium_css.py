import os

premium_css = '''

/* ==============================================
   PREMIUM DARK SUBPAGE THEME WITH BLUE STROKES
   ============================================== */

/* Dark page background with decorative blue strokes */
body.dark-page {
  background: #0a0e17;
  color: #e2e8f0;
  position: relative;
}

body.dark-page::before {
  content: '';
  position: fixed;
  inset: 0;
  z-index: 0;
  pointer-events: none;
  background:
    /* Diagonal blue stroke lines */
    repeating-linear-gradient(
      135deg,
      transparent,
      transparent 80px,
      rgba(30, 64, 175, 0.04) 80px,
      rgba(30, 64, 175, 0.04) 81px
    ),
    repeating-linear-gradient(
      45deg,
      transparent,
      transparent 120px,
      rgba(59, 130, 246, 0.03) 120px,
      rgba(59, 130, 246, 0.03) 121px
    ),
    /* Subtle radial glow accents */
    radial-gradient(ellipse 600px 400px at 10% 20%, rgba(30, 64, 175, 0.08), transparent),
    radial-gradient(ellipse 500px 500px at 90% 60%, rgba(59, 130, 246, 0.06), transparent),
    radial-gradient(ellipse 400px 300px at 50% 90%, rgba(30, 58, 138, 0.05), transparent);
}

body.dark-page > * {
  position: relative;
  z-index: 1;
}

/* Main content area styling */
body.dark-page .container.section {
  color: #e2e8f0;
}

body.dark-page main {
  position: relative;
}

/* Premium blue stroke decorative borders on sections */
body.dark-page main::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 1px;
  height: 80px;
  background: linear-gradient(to bottom, rgba(59, 130, 246, 0.5), transparent);
}

/* Section titles on dark pages */
body.dark-page .pdf-section-title,
body.dark-page .section-title,
body.dark-page h2 {
  color: #ffffff;
  position: relative;
}

body.dark-page .pdf-section-title::after,
body.dark-page .section-title::after {
  content: '';
  display: block;
  width: 60px;
  height: 3px;
  background: linear-gradient(90deg, #3b82f6, #1e40af);
  margin-top: 0.75rem;
  border-radius: 2px;
}

body.dark-page h3 {
  color: #f1f5f9;
}

body.dark-page p {
  color: #94a3b8;
}

/* Card styling for dark pages - service cards */
body.dark-page .card {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(59, 130, 246, 0.12);
  border-radius: var(--radius-lg);
  padding: 2rem;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  transition: all 0.4s var(--transition);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

body.dark-page .card:hover {
  background: rgba(15, 23, 42, 0.8);
  border-color: rgba(59, 130, 246, 0.3);
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.5), 0 0 30px rgba(59, 130, 246, 0.08);
  transform: translateY(-5px);
}

body.dark-page .card h3 {
  color: #ffffff;
  font-family: 'Poppins', sans-serif;
  font-weight: 700;
  margin-bottom: 0.75rem;
}

body.dark-page .card p {
  color: #94a3b8;
  line-height: 1.7;
}

/* Service card icons */
body.dark-page .card .icon {
  width: 64px;
  height: 64px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.15), rgba(30, 64, 175, 0.1));
  border: 1px solid rgba(59, 130, 246, 0.2);
  border-radius: 16px;
  margin-bottom: 1.5rem;
  color: #3b82f6;
  transition: all 0.3s ease;
}

body.dark-page .card:hover .icon {
  background: linear-gradient(135deg, rgba(59, 130, 246, 0.25), rgba(30, 64, 175, 0.2));
  border-color: rgba(59, 130, 246, 0.4);
  box-shadow: 0 0 20px rgba(59, 130, 246, 0.15);
}

/* Gallery cards on dark pages */
body.dark-page .gallery-card {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(59, 130, 246, 0.1);
  border-radius: var(--radius-lg);
  overflow: hidden;
  padding: 0;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
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

/* Gradient text links */
body.dark-page .gradient-text {
  background: linear-gradient(135deg, #3b82f6, #60a5fa);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
  font-size: 0.9rem;
  letter-spacing: 0.03em;
  text-transform: uppercase;
  display: inline-block;
  margin-top: 1rem;
  transition: all 0.3s ease;
}

body.dark-page .gradient-text:hover {
  background: linear-gradient(135deg, #60a5fa, #93c5fd);
  -webkit-background-clip: text;
  background-clip: text;
}

/* pdf-stat-box on dark pages */
body.dark-page .pdf-stat-box {
  background: rgba(15, 23, 42, 0.6) !important;
  border: 1px solid rgba(59, 130, 246, 0.12) !important;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3) !important;
  backdrop-filter: blur(12px) !important;
  -webkit-backdrop-filter: blur(12px) !important;
  border-radius: var(--radius-lg) !important;
  padding: 2rem !important;
  transition: all 0.4s var(--transition) !important;
}

body.dark-page .pdf-stat-box:hover {
  background: rgba(15, 23, 42, 0.8) !important;
  border-color: rgba(59, 130, 246, 0.3) !important;
  box-shadow: 0 16px 48px rgba(0, 0, 0, 0.5), 0 0 30px rgba(59, 130, 246, 0.08) !important;
  transform: translateY(-5px) !important;
}

body.dark-page .pdf-stat-box h3 {
  color: #ffffff;
  font-family: 'Poppins', sans-serif;
}

body.dark-page .pdf-stat-box p {
  color: #94a3b8;
}

/* pdf-partner section */
body.dark-page .pdf-partner-content h2 {
  color: #ffffff;
}

body.dark-page .pdf-partner-content p {
  color: #94a3b8;
}

body.dark-page .pdf-partner-image img {
  border-radius: var(--radius-lg);
  border: 1px solid rgba(59, 130, 246, 0.12);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
}

/* Quote form styling for contact page */
body.dark-page .quote-form {
  background: rgba(15, 23, 42, 0.6);
  border: 1px solid rgba(59, 130, 246, 0.12);
  border-radius: var(--radius-lg);
  padding: 2.5rem;
  backdrop-filter: blur(12px);
  -webkit-backdrop-filter: blur(12px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
}

body.dark-page input,
body.dark-page textarea,
body.dark-page select {
  background: rgba(15, 23, 42, 0.8) !important;
  border: 1px solid rgba(59, 130, 246, 0.15) !important;
  color: #e2e8f0 !important;
  border-radius: var(--radius) !important;
  padding: 0.85rem 1.2rem !important;
  transition: border-color 0.3s ease, box-shadow 0.3s ease;
}

body.dark-page input:focus,
body.dark-page textarea:focus,
body.dark-page select:focus {
  border-color: rgba(59, 130, 246, 0.4) !important;
  box-shadow: 0 0 0 3px rgba(59, 130, 246, 0.1) !important;
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
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

/* Gallery grid on dark pages */
body.dark-page .gallery-grid {
  gap: 1.5rem;
}

body.dark-page .gallery-grid img {
  border-radius: var(--radius);
  border: 1px solid rgba(59, 130, 246, 0.1);
  transition: all 0.4s ease;
}

body.dark-page .gallery-grid img:hover {
  border-color: rgba(59, 130, 246, 0.3);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
}

/* Blue stroke decorative dividers */
body.dark-page section + section {
  position: relative;
  margin-top: 1rem;
}

body.dark-page section + section::before {
  content: '';
  position: absolute;
  top: -1rem;
  left: 50%;
  transform: translateX(-50%);
  width: 120px;
  height: 2px;
  background: linear-gradient(90deg, transparent, rgba(59, 130, 246, 0.4), transparent);
}

/* pdf-trust-features on dark pages */
body.dark-page .pdf-trust-features {
  gap: 1.5rem;
}

/* Breadcrumb on dark bg */
body.dark-page .breadcrumb a {
  color: #3b82f6;
  transition: color 0.3s ease;
}

body.dark-page .breadcrumb a:hover {
  color: #60a5fa;
}

/* Cinematic hero tweaks for dark pages */
body.dark-page .cin-eyebrow {
  background: linear-gradient(135deg, #1e40af, #3b82f6) !important;
  color: #ffffff !important;
  box-shadow: 0 4px 20px rgba(59, 130, 246, 0.25) !important;
}

body.dark-page .cin-hero-content h1 {
  background: linear-gradient(135deg, #ffffff 30%, #3b82f6) !important;
  -webkit-background-clip: text !important;
  -webkit-text-fill-color: transparent !important;
  background-clip: text !important;
  text-shadow: none !important;
}

/* Operations-specific list styling */
body.dark-page ul, body.dark-page ol {
  color: #94a3b8;
}

body.dark-page li {
  margin-bottom: 0.5rem;
}

body.dark-page strong {
  color: #e2e8f0;
}

/* Horizontal blue stroke at top of main content */
body.dark-page main.container.section::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 200px;
  height: 2px;
  background: linear-gradient(90deg, transparent, #3b82f6, transparent);
}

/* Footer override to ensure it sits on dark bg */
body.dark-page .site-footer {
  background: #060911 !important;
  border-top: 1px solid rgba(59, 130, 246, 0.1);
}

/* Responsive adjustments for dark pages */
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

with open('assets/css/styles.css', 'a', encoding='utf-8') as f:
    f.write(premium_css)

print('Appended premium dark page CSS with blue strokes')
