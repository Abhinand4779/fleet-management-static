import os
import re

pages_dir = 'pages'
service_pages = [
    'customs-clearance.html',
    'transportation-services.html',
    'warehousing-services.html',
    'packaging-moving-services.html',
    'storage-delivery-services.html'
]

for file in service_pages:
    filepath = os.path.join(pages_dir, file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # Remove inline color: #333 from paragraphs
    content = content.replace('color: #333; ', '')
    
    # Remove inline color: #000 from h3
    content = content.replace('color: #000; ', '')

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed inline colors in {file}")
    else:
        print(f"No changes for {file}")
