import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

good_header = """  <title>Linking Bridge Transportation | Premium Fleet Management</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Poppins:wght@600;700;800&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="/assets/css/styles.css" />
</head>

<body data-page="index">
  <header id="site-header"></header>

  <main>
    <section class="hero">
      <div class="hero-image">
        <img src="/assets/images/gallery/truck.jpg.jpeg" alt="Linking Bridges Transportation modern fleet in Saudi Arabia" />
      </div>
      <div class="hero-content reveal">
        <div class="eyebrow">Next-Generation Logistics & Fleet Management</div>
        <h1>Delivering Excellence, <br><span class="text-primary" style="color: var(--primary);">Delivering Tomorrow.</span></h1>
        <div class="hero-actions">
          <a class="btn btn-primary" href="/pages/contact.html">REQUEST A QUOTE &rarr;</a>
          <a class="btn btn-outline" href="/pages/services.html">OUR SERVICES &rarr;</a>
        </div>
        <div class="hero-badges">
          <span><i class="icon-clock"></i> 24/7 Live Tracking</span>
          <span><i class="icon-shield"></i> ISO-Certified</span>
          <span><i class="icon-truck"></i> Modern Fleet</span>
        </div>
      </div>
    </section>

    <section class="stat-strip">
      <div class="container stat-grid">
        <div class="stat-card reveal">
          <strong class="counter" data-target="500" data-suffix="+">0</strong>
          <span>Vehicles Managed</span>
        </div>
        <div class="stat-card reveal">
          <strong class="counter" data-target="24" data-suffix="/7">0</strong>
"""

html = re.sub(
    r'  <meta name="description"\n    content="Linking Bridge Transportation provides premium fleet management, customs clearance, warehousing, moving and delivery services." />\n          <span>Live Tracking</span>',
    '  <meta name="description" content="Linking Bridge Transportation provides premium fleet management, customs clearance, warehousing, moving and delivery services." />\n' + good_header + '          <span>Live Tracking</span>',
    html,
    flags=re.DOTALL
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
