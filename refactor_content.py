import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Content Grids & Info Cards ONLY. No Hero changes!
    content = content.replace('class="grid-2 section-sm"', 'class="pdf-partner"')
    content = content.replace('class="grid-3 section-sm"', 'class="pdf-trust-features"')
    
    # Update visuals wrapper inside grid-2 (now pdf-partner)
    content = content.replace('class="about-visual reveal"', 'class="pdf-partner-image reveal"')
    
    # Update the text wrapper inside pdf-partner
    content = content.replace('<div class="reveal">', '<div class="pdf-partner-content reveal">')
    
    # Info cards -> pdf-stat-box
    content = content.replace('class="card info-card reveal"', 'class="pdf-stat-box glass-light reveal"')
    content = content.replace('class="card info-card dark reveal"', 'class="pdf-stat-box dark reveal"')
    
    # Section titles
    content = content.replace('class="section-title"', 'class="pdf-section-title"')
    
    # Form input styling inside contact forms if any
    content = content.replace('class="form-control"', 'class="form-control" style="border:1px solid rgba(255,255,255,0.2); background:rgba(0,0,0,0.5); color:white;"')
    
    # Update if content changed
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated content sections for {filepath}")
    else:
        print(f"No changes for {filepath}")

pages_dir = 'pages'
files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

for file in files:
    process_file(os.path.join(pages_dir, file))
