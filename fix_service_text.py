with open('assets/css/styles.css', 'a', encoding='utf-8') as f:
    f.write('''

/* ==============================================
   DARK PAGE: SERVICE PAGE HERO & CONTENT FIXES
   ============================================== */

/* Page hero text — these pages use .page-hero, .hero-copy, .eyebrow */
body.dark-page .page-hero h1 {
  color: #ffffff !important;
  text-shadow: 0 2px 20px rgba(0,0,0,0.3);
}

body.dark-page .hero-copy p,
body.dark-page .section-intro {
  color: #94a3b8 !important;
}

body.dark-page .eyebrow {
  background: linear-gradient(135deg, #b0914f, #d6b86d) !important;
  color: #0b0e14 !important;
  box-shadow: 0 4px 15px rgba(214, 184, 109, 0.2);
  border: none;
}

body.dark-page .page-hero-image img {
  border-radius: var(--radius-lg);
  border: 1px solid rgba(255, 255, 255, 0.06);
  box-shadow: 0 16px 50px rgba(0, 0, 0, 0.4);
}

/* Content paragraphs and h3s in service detail pages */
body.dark-page .pdf-partner-content p,
body.dark-page .section-sm p {
  color: #94a3b8 !important;
  line-height: 1.7;
}

body.dark-page .pdf-partner-content h3,
body.dark-page .section-sm h3 {
  color: #ffffff !important;
  letter-spacing: 0.05em;
}

/* List items in service detail pages */
body.dark-page .list-check li {
  color: #cbd5e1;
  padding: 0.75rem 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.04);
}

body.dark-page .list-check li strong {
  color: #ffffff;
}

/* List check bullet styling */
body.dark-page .list-check li::marker {
  color: #d6b86d;
}

/* Banner CTA section at bottom */
body.dark-page .banner {
  background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%) !important;
  border: 1px solid rgba(255, 255, 255, 0.06) !important;
}

body.dark-page .banner strong {
  color: #ffffff;
  font-size: 1.3rem;
}

body.dark-page .banner p {
  color: #94a3b8 !important;
}

/* Responsive fix for page-hero on mobile */
@media (max-width: 768px) {
  body.dark-page .page-hero {
    grid-template-columns: 1fr;
    gap: 2rem;
    padding: 4rem 0 2rem;
  }
}

''')

print('Appended service page text visibility fixes')
