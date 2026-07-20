import os

# Add dark page class to all subpages (not index.html!)
pages_dir = 'pages'
files = [f for f in os.listdir(pages_dir) if f.endswith('.html')]

for file in files:
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Add class "dark-page" to body tag (only if not already there)
    if 'class="dark-page"' not in content:
        content = content.replace('<body>', '<body class="dark-page">')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added dark-page class to {file}")
    else:
        print(f"Already has dark-page class: {file}")
