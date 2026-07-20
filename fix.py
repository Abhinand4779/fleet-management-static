import os
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Fix H1 in pdf-hero
    content = re.sub(r'(<div class="pdf-hero-content reveal">[\s\S]*?)<h1>', r'\1<h1 class="pdf-hero-headline">', content)
    
    # 2. Fix cin-hero-sub
    content = content.replace('class="cin-hero-sub"', 'style="font-size: 1.2rem; margin-bottom: 2rem; opacity: 0.9;"')
    
    # 3. Fix pdf-partner content div
    content = re.sub(r'<section class="pdf-partner">\s*<div class="reveal">', r'<section class="pdf-partner">\n      <div class="pdf-partner-content reveal">', content)
    content = re.sub(r'<section class="pdf-partner">\s*<div class="pdf-partner-content">\s*<div class="reveal">', r'<section class="pdf-partner">\n      <div class="pdf-partner-content reveal">', content)
    
    # 4. Fix section-title
    content = content.replace('class="section-title"', 'class="pdf-section-title"')

    # 5. Fix form section (contact page) to use pdf-trust classes if possible, or just keep it responsive
    # The contact page has a form, it might be fine.
    
    # Update if content changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed {filepath}")
    else:
        print(f"No changes for {filepath}")

pages_dir = 'pages'
files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

for file in files:
    process_file(os.path.join(pages_dir, file))
