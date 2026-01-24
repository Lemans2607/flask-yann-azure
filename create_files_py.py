import os

print("=" * 60)
print("🦁 Création de Yann's Note - Version complète")
print("=" * 60)
print()

# Créer les dossiers
folders = [
    "templates",
    "static",
    "static/css",
    "static/js",
    "static/icons"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"✓ Dossier créé: {folder}")

print()

# base.html - EXACTEMENT comme le fichier original
base_html = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width,initial-scale=1" />
    <meta http-equiv="Permissions-Policy" content="camera=*, microphone=*, geolocation=*">
    <title>Yann's Note</title>
    <link rel="manifest" href="{{ url_for('static', filename='manifest.json') }}">
    <link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'%3E%3Ctext y='0.9em' font-size='90'%3E🦁%3C/text%3E%3C/svg%3E">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
  </head>
  <body>
    <header class="site-header">
      <div class="container header-inner">
        <h1 class="brand"><a href="/">Yann's Note</a></h1>
        <div class="controls">
          <button id="theme-toggle" aria-label="Toggle dark mode">🌙</button>
        </div>
      </div>
    </header>

    <main id="main">
      {% block content %}{% endblock %}
    </main>

    <footer class="site-footer">
      <div class="container footer-inner">
        <div class="socials">
          <a href="#" title="LinkedIn" aria-label="LinkedIn" class="social-link">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M4.98 3.5C4.98 4.88 3.88 6 2.5 6S0 4.88 0 3.5 1.12 1 2.5 1 4.98 2.12 4.98 3.5zM.5 8.5h4V24h-4V8.5zM9.5 8.5h3.84v2.07h.05c.54-1.02 1.86-2.07 3.83-2.07 4.1 0 4.86 2.7 4.86 6.22V24h-4v-7.5c0-1.8-.03-4.12-2.5-4.12-2.5 0-2.88 1.95-2.88 3.98V24h-4V8.5z"/></svg>
          </a>
          <a href="#" title="Facebook" aria-label="Facebook" class="social-link">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M22 12a10 10 0 10-11.5 9.9v-7H8v-2.9h2.5V9.5c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.4h-1.2c-1.2 0-1.6.8-1.6 1.6v1.9H19l-.4 2.9h-2.4v7A10 10 0 0022 12z"/></svg>
          </a>
          <a href="#" title="X (Twitter)" aria-label="X" class="social-link">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M24 4.6c-.9.4-1.9.7-2.9.8 1-0.6 1.7-1.6 2-2.8-1 .6-2.1 1-3.3 1.2C18.6 2 17.1 1.5 15.6 1.5c-2.7 0-4.8 2.2-4.8 4.8 0 .4 0 .9.1 1.3C6.6 7.3 3.5 5.4 1.5 2.7c-.4.7-.6 1.6-.6 2.5 0 1.7.9 3.2 2.2 4.1-.8 0-1.6-.2-2.3-.6v.1c0 2.4 1.7 4.4 3.9 4.8-.4.1-.8.1-1.2.1-.3 0-.5 0-.8-.1.5 1.6 2.1 2.8 3.9 2.8-1.4 1.1-3.3 1.8-5.2 1.8H3c1.9 1.2 4.1 1.9 6.4 1.9 7.6 0 11.7-6.5 11.7-12.1v-.5c.8-.6 1.5-1.3 2-2.1z"/></svg>
          </a>
        </div>
        <div class="copyright">© Yann's Note</div>
      </div>
    </footer>

    <script>
      window._INITIAL_DATA = {};
    </script>
    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
  </body>
</html>"""

# index.html - EXACTEMENT comme le fichier original
index_html = """{% extends "base.html" %}
{% block content %}
<section class="hero">
  <div class="container hero-inner">
    <h2 class="hero-title">Welcome to Yann's Note</h2>
    <p class="hero-sub">A minimal site demo converted to Flask with camera, microphone, and geolocation hooks.</p>

    <div class="hero-actions">
      <button id="btn-mic" class="btn">Use Microphone</button>
      <button id="btn-camera" class="btn">Use Camera</button>
      <button id="btn-geo" class="btn">Get Geolocation</button>
      <a class="btn" href="/admin">Go to Admin</a>
    </div>

    <div id="media-output" class="media-output" aria-live="polite"></div>
  </div>
</section>
{% endblock %}"""

# admin.html - EXACTEMENT comme le fichier original
admin_html = """{% extends "base.html" %}
{% block content %}
<section class="admin container">
  <h2>Admin Dashboard</h2>
  <p class="welcome">Welcome! Current date and time: <strong>{{ current_time }}</strong></p>

  <div class="activity">
    <p>Recent activity overview: <strong>{{ items_added_today }}</strong> items added today.</p>
    <button id="btn-add-item" class="btn">Add demo item</button>
    <div id="activity-result" class="activity-result" aria-live="polite"></div>
  </div>

  <section class="recent container" aria-labelledby="recent-heading" style="margin-top:1.25rem">
    <h3 id="recent-heading">Recent items</h3>
    {% if recent_items %}
      <ul class="recent-list" style="padding-left:1rem">
        {% for item in recent_items %}
          <li>
            <strong>{{ item.created_at.strftime('%Y-%m-%d %H:%M:%S') }}</strong>
            - {{ item.note or '(no note)' }}
          </li>
        {% endfor %}
      </ul>
    {% else %}
      <p class="muted">No recent items yet.</p>
    {% endif %}
  </section>
</section>
{% endblock %}"""

# styles.css - EXACTEMENT comme le fichier original
styles_css = """:root{
  --bg: #ffffff;
  --text: #0f172a;
  --muted: #64748b;
  --accent: #0ea5a4;
  --hero-height: 60vh;
}

html.dark {
  --bg: #0b1220;
  --text: #e6eef6;
  --muted: #94a3b8;
  --accent: #34d399;
}

*{box-sizing:border-box}
body{
  margin:0;
  font-family:Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
  background:var(--bg);
  color:var(--text);
  -webkit-font-smoothing:antialiased;
  -moz-osx-font-smoothing:grayscale;
  min-height:100vh;
  display:flex;
  flex-direction:column;
}

.container{max-width:1100px;margin:0 auto;padding:1rem;}

.header-inner{display:flex;justify-content:space-between;align-items:center;padding:1rem;}
.brand a{color:var(--text);text-decoration:none;font-weight:600}
.controls button{background:none;border:1px solid transparent;padding:.4rem .6rem;border-radius:6px;cursor:pointer;color:var(--text)}

.site-footer{margin-top:auto;padding:1.5rem 0;border-top:1px solid rgba(0,0,0,0.06);color:var(--muted)}
.footer-inner{display:flex;justify-content:space-between;align-items:center}
.social-link{margin-right:.6rem;color:var(--muted);display:inline-flex;align-items:center}
.social-link:hover{color:var(--accent)}

.btn{display:inline-block;background:var(--accent);color:#fff;padding:.6rem .9rem;border-radius:8px;border:none;cursor:pointer;margin:.25rem;text-decoration:none}
.btn:active{transform:translateY(1px)}

.hero{
  position:relative;
  height:var(--hero-height);
  display:flex;
  align-items:center;
  overflow:hidden;
}

.hero::before{
  content:"";
  position:absolute;
  inset:0;
  z-index:0;
  background: linear-gradient(120deg, rgba(14,165,164,0.08), rgba(52,211,153,0.06), rgba(99,102,241,0.05));
  background-size: 200% 200%;
  animation: slowShift 18s ease-in-out infinite;
  filter: blur(30px) saturate(1.1);
  transform: translateZ(0);
  pointer-events:none;
}

@keyframes slowShift{
  0%{background-position:0% 50%}
  50%{background-position:100% 50%}
  100%{background-position:0% 50%}
}

.hero-inner{position:relative;z-index:1;padding:2rem}
.hero-title{font-size:clamp(1.6rem, 3.2vw, 3rem);margin:0 0 .5rem}
.hero-sub{color:var(--muted);margin:0 0 1rem}
.media-output{margin-top:1rem;color:var(--muted)}

.admin{padding:2rem}
.welcome{margin-bottom:1rem}
.activity-result{margin-top:1rem;color:var(--muted)}

html.dark .hero::before{
  background: linear-gradient(120deg, rgba(52,211,153,0.06), rgba(14,165,164,0.04), rgba(99,102,241,0.03));
}"""

# main.js - EXACTEMENT comme le fichier original
main_js = """// Dark mode toggle that respects system preference and persists to localStorage
(function() {
  const root = document.documentElement;
  const toggle = document.getElementById('theme-toggle');
  const storageKey = 'yn_theme';

  function applyTheme(theme) {
    if (theme === 'dark') {
      root.classList.add('dark');
      if (toggle) toggle.textContent = '☀️';
    } else {
      root.classList.remove('dark');
      if (toggle) toggle.textContent = '🌙';
    }
  }

  const saved = localStorage.getItem(storageKey);
  if (saved) {
    applyTheme(saved);
  } else {
    const prefersDark = window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches;
    applyTheme(prefersDark ? 'dark' : 'light');
  }

  if (toggle) {
    toggle.addEventListener('click', () => {
      const isDark = root.classList.contains('dark');
      const next = isDark ? 'light' : 'dark';
      applyTheme(next);
      localStorage.setItem(storageKey, next);
    });
  }

  window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', e => {
    const savedChoice = localStorage.getItem(storageKey);
    if (!savedChoice) {
      applyTheme(e.matches ? 'dark' : 'light');
    }
  });
})();

// Media and geolocation handlers
document.addEventListener('DOMContentLoaded', function () {
  const btnMic = document.getElementById('btn-mic');
  const btnCamera = document.getElementById('btn-camera');
  const btnGeo = document.getElementById('btn-geo');
  const mediaOutput = document.getElementById('media-output');
  const btnAddItem = document.getElementById('btn-add-item');
  const activityResult = document.getElementById('activity-result');

  if (btnMic) {
    btnMic.addEventListener('click', async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
        stream.getTracks().forEach(t => t.stop());
        mediaOutput.textContent = 'Microphone access granted.';
      } catch (err) {
        mediaOutput.textContent = 'Microphone access denied or not available: ' + (err.message || err);
      }
    });
  }

  if (btnCamera) {
    btnCamera.addEventListener('click', async () => {
      try {
        const stream = await navigator.mediaDevices.getUserMedia({ video: true });
        const video = document.createElement('video');
        video.autoplay = true;
        video.muted = true;
        video.playsInline = true;
        video.width = 240;
        video.height = 160;
        video.srcObject = stream;
        mediaOutput.innerHTML = '';
        mediaOutput.appendChild(video);

        setTimeout(() => {
          stream.getTracks().forEach(t => t.stop());
          mediaOutput.textContent = 'Camera preview ended. Camera access was granted.';
        }, 3000);
      } catch (err) {
        mediaOutput.textContent = 'Camera access denied or not available: ' + (err.message || err);
      }
    });
  }

  if (btnGeo) {
    btnGeo.addEventListener('click', () => {
      if (!navigator.geolocation) {
        mediaOutput.textContent = 'Geolocation is not supported by this browser.';
        return;
      }
      mediaOutput.textContent = 'Requesting location…';
      navigator.geolocation.getCurrentPosition(
        (pos) => {
          mediaOutput.textContent = `Location: ${pos.coords.latitude.toFixed(6)}, ${pos.coords.longitude.toFixed(6)} (accuracy ${pos.coords.accuracy}m)`;
        },
        (err) => {
          mediaOutput.textContent = 'Geolocation error: ' + (err.message || err.code);
        },
        { enableHighAccuracy: false, timeout: 10000, maximumAge: 0 }
      );
    });
  }

  if (btnAddItem) {
    btnAddItem.addEventListener('click', async () => {
      try {
        btnAddItem.disabled = true;
        const resp = await fetch('/api/items', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ note: 'Demo item added from admin UI' })
        });
        const data = await resp.json();
        activityResult.textContent = `Item added — ${data.items_today} items added today.`;
      } catch (err) {
        activityResult.textContent = 'Failed to add item: ' + err;
      } finally {
        btnAddItem.disabled = false;
      }
    });
  }
});"""

# manifest.json - EXACTEMENT comme le fichier original
manifest_json = """{
  "name": "Yann's Note - Flask Demo",
  "short_name": "YannsNote",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#ffffff",
  "theme_color": "#0ea5a4",
  "icons": [
    {
      "src": "/static/icons/icon-192.png",
      "sizes": "192x192",
      "type": "image/png"
    },
    {
      "src": "/static/icons/icon-512.png",
      "sizes": "512x512",
      "type": "image/png"
    }
  ],
  "permissions": [
    "microphone",
    "camera",
    "geolocation"
  ],
  "description": "Le site python yann's note"
}"""

# Écrire tous les fichiers
files = {
    "templates/base.html": base_html,
    "templates/index.html": index_html,
    "templates/admin.html": admin_html,
    "static/css/styles.css": styles_css,
    "static/js/main.js": main_js,
    "static/manifest.json": manifest_json
}

for filepath, content in files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ Fichier créé: {filepath}")

print()
print("=" * 60)
print("✅ Tous les fichiers ont été créés!")
print("=" * 60)
print()
print("Structure finale:")
print("flask-yann-azure/")
print("├── app.py")
print("├── create_files.py")
print("├── templates/")
print("│   ├── base.html ✓")
print("│   ├── index.html ✓")
print("│   └── admin.html ✓")
print("└── static/")
print("    ├── manifest.json ✓")
print("    ├── css/")
print("    │   └── styles.css ✓")
print("    └── js/")
print("        └── main.js ✓")
print()
print("🚀 Prochaine étape:")
print("   py app.py")
print()
print("🌐 Puis ouvrez: http://localhost:5000")
print()
input("Appuyez sur Entrée pour continuer...")
