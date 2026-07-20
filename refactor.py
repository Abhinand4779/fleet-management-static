import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Replace Hero Container wrapper
    # From: <div class="container" style="padding-top: 0; padding-bottom: 0;">\n    <div class="cin-hero reveal">
    # To: <section class="pdf-hero">
    content = re.sub(
        r'<div class="container" style="padding-top: 0; padding-bottom: 0;">\s*<div class="cin-hero[^"]*">',
        r'<section class="pdf-hero">',
        content
    )
    
    # 2. Convert .cin-hero-bg to .pdf-hero-bg
    content = content.replace('class="cin-hero-bg"', 'class="pdf-hero-bg"')
    
    # 3. Add .pdf-hero-truck to the img inside pdf-hero-bg
    content = re.sub(
        r'(<div class="pdf-hero-bg">\s*<img src="[^"]*" alt="[^"]*")',
        r'\1 class="pdf-hero-truck"',
        content
    )
    
    # 4. Convert .cin-hero-content to .pdf-hero-content
    content = content.replace('class="cin-hero-content"', 'class="pdf-hero-content reveal"')
    
    # 5. Convert breadcrumb and eyebrow to pdf-section-label-light
    content = content.replace('class="breadcrumb"', 'class="pdf-section-label-light"')
    content = content.replace('class="cin-eyebrow"', 'class="pdf-section-label-light"')
    
    # 6. Convert h1 inside hero
    # This is tricky without regex context, but we can do a targeted replace.
    # Looking for <h1> inside the hero block
    hero_match = re.search(r'<div class="pdf-hero-content reveal">([\s\S]*?)</div>', content)
    if hero_match:
        hero_inner = hero_match.group(1)
        new_hero_inner = re.sub(r'<h1>', r'<h1 class="pdf-hero-headline">', hero_inner)
        new_hero_inner = new_hero_inner.replace('class="cin-hero-sub"', 'style="font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9;"')
        content = content.replace(hero_inner, new_hero_inner)

    # 7. Close section instead of 2 divs. 
    # The old structure ended with:
    #       </div>
    #     </div>
    #   </div>
    #   <main
    # Since we replaced the top 2 divs with 1 section, we have an extra </div>.
    content = re.sub(r'      </div>\s*</div>\s*</div>\s*<main', r'      </div>\n    </section>\n\n  <main', content)
    
    # 8. Content Grids & Info Cards
    content = content.replace('class="grid-2 section-sm"', 'class="pdf-partner"')
    content = content.replace('class="grid-3 section-sm"', 'class="pdf-trust-features"')
    content = content.replace('class="about-visual reveal"', 'class="pdf-partner-image reveal"')
    
    # Info cards -> pdf-stat-box
    content = content.replace('class="card info-card reveal"', 'class="pdf-stat-box glass-light reveal"')
    content = content.replace('class="card info-card dark reveal"', 'class="pdf-stat-box dark reveal"')
    
    # Update if content changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"No changes for {filepath}")

pages_dir = 'pages'
files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

for file in files:
    process_file(os.path.join(pages_dir, file))
