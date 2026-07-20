import os

pages_dir = 'pages'
files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

for file in files:
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Swap dark-page to premium-light
    content = content.replace('class="dark-page"', 'class="premium-light"')
    
    # Just in case some files don't have it on the body tag properly
    content = content.replace('<body >', '<body>')
    content = content.replace('<body>', '<body class="premium-light">')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {file} to premium-light")
