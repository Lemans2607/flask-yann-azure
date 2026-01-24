import os
import sys
import subprocess

print("=" * 80)
print("🦁 YANN'S NOTE - HUB DE CLARTÉ IA - INSTALLATION COMPLÈTE")
print("=" * 80)
print()

# ==========================================
# ÉTAPE 1 : INSTALLATION DES DÉPENDANCES
# ==========================================
print("📦 ÉTAPE 1/3 : Installation des dépendances Python...")
print("-" * 80)

packages = [
    'Flask>=3.0.0',
    'Flask-SQLAlchemy>=3.1.1',
    'google-generativeai>=0.3.0',
    'python-dotenv>=1.0.0'
]

for package in packages:
    print(f"\n📥 Installation de {package}...")
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        print(f"✓ {package} installé")
    except subprocess.CalledProcessError:
        print(f"✗ Erreur: {package}")
        print("\n⚠️  Essayez d'exécuter en tant qu'administrateur")
        input("\nAppuyez sur Entrée...")
        sys.exit(1)

print("\n✅ Toutes les dépendances sont installées!")

# ==========================================
# ÉTAPE 2 : CRÉATION DE LA STRUCTURE
# ==========================================
print("\n" + "=" * 80)
print("📁 ÉTAPE 2/3 : Création de la structure...")
print("-" * 80)

folders = [
    "templates",
    "static",
    "static/css",
    "static/js",
    "static/images"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)
    print(f"✓ {folder}/")

# ==========================================
# ÉTAPE 3 : CRÉATION DES FICHIERS
# ==========================================
print("\n" + "=" * 80)
print("📝 ÉTAPE 3/3 : Création des fichiers...")
print("-" * 80)

# app.py - Application principale
app_py = """import os
from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date
from sqlalchemy import func
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.config['SECRET_KEY'] = 'yann-note-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///yanns_note.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Configure Gemini AI
GEMINI_API_KEY = os.getenv('GEMINI_API_KEY', '')
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Models
class ContentItem(db.Model):
    __tablename__ = 'content_items'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    category = db.Column(db.String(50), nullable=False)
    url = db.Column(db.String(500))
    is_zero_data = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'url': self.url,
            'isZeroData': self.is_zero_data,
            'timestamp': int(self.created_at.timestamp() * 1000)
        }

class ChatMessage(db.Model):
    __tablename__ = 'chat_messages'
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(20), nullable=False)
    text = db.Column(db.Text, nullable=False)
    sources = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    lang = session.get('lang', 'fr')
    return render_template('home.html', lang=lang, current_page='home')

@app.route('/students')
def students():
    lang = session.get('lang', 'fr')
    return render_template('students.html', lang=lang, current_page='students')

@app.route('/business')
def business():
    lang = session.get('lang', 'fr')
    return render_template('business.html', lang=lang, current_page='business')

@app.route('/brain')
def brain():
    lang = session.get('lang', 'fr')
    messages = ChatMessage.query.order_by(ChatMessage.created_at).all()
    return render_template('brain.html', lang=lang, current_page='brain', messages=messages)

@app.route('/admin')
def admin():
    current_time = datetime.utcnow().strftime('%A, %d %B %Y | %H:%M:%S UTC')
    today = date.today()
    items_today = ContentItem.query.filter(
        func.date(ContentItem.created_at) == today
    ).count()
    items = ContentItem.query.order_by(ContentItem.created_at.desc()).all()
    return render_template('admin.html', 
                         current_page='admin',
                         current_time=current_time,
                         items_today=items_today,
                         items=items)

# API Routes
@app.route('/api/set-lang', methods=['POST'])
def set_lang():
    data = request.json
    lang = data.get('lang', 'fr')
    session['lang'] = lang
    return jsonify({'success': True, 'lang': lang})

@app.route('/api/content', methods=['GET', 'POST', 'DELETE'])
def api_content():
    if request.method == 'POST':
        data = request.json
        item = ContentItem(
            title=data.get('title'),
            description=data.get('description'),
            category=data.get('category'),
            url=data.get('url'),
            is_zero_data=data.get('isZeroData', True)
        )
        db.session.add(item)
        db.session.commit()
        return jsonify({'success': True, 'item': item.to_dict()})
    
    elif request.method == 'DELETE':
        item_id = request.json.get('id')
        item = ContentItem.query.get(item_id)
        if item:
            db.session.delete(item)
            db.session.commit()
            return jsonify({'success': True})
        return jsonify({'success': False}), 404
    
    else:
        items = ContentItem.query.order_by(ContentItem.created_at.desc()).all()
        return jsonify({'items': [item.to_dict() for item in items]})

@app.route('/api/chat', methods=['POST'])
def api_chat():
    data = request.json
    user_message = data.get('message', '')
    
    # Save user message
    user_msg = ChatMessage(role='user', text=user_message)
    db.session.add(user_msg)
    db.session.commit()
    
    # Generate AI response with Gemini
    ai_text = ""
    sources = []
    
    if GEMINI_API_KEY:
        try:
            model = genai.GenerativeModel('gemini-pro')
            system_prompt = \"\"\"Tu es Yann's NOTE IA, l'Assistant de Clarté par excellence au Cameroun. 
Ton rôle est de transformer le chaos informationnel en clarté absolue. 
Utilise un ton professionnel, encourageant et cite toujours tes sources. 
Réponds en français ou anglais selon la demande. Pas d'hallucinations.\"\"\"
            
            response = model.generate_content(f"{system_prompt}\\n\\nQuestion: {user_message}")
            ai_text = response.text
        except Exception as e:
            ai_text = f"Désolé, une erreur s'est produite: {str(e)}"
    else:
        ai_text = "Configuration API Gemini manquante. Veuillez définir GEMINI_API_KEY dans .env"
    
    # Save AI response
    ai_msg = ChatMessage(role='ai', text=ai_text)
    db.session.add(ai_msg)
    db.session.commit()
    
    return jsonify({
        'text': ai_text,
        'sources': sources
    })

if __name__ == '__main__':
    print("=" * 60)
    print("🦁 Yann's NOTE - Hub de Clarté IA")
    print("=" * 60)
    print()
    print("🌐 Application disponible sur:")
    print("   http://localhost:5000")
    print()
    print("📄 Pages:")
    print("   /           - Accueil")
    print("   /students   - Services Étudiants")
    print("   /business   - Services Entreprises")
    print("   /brain      - Cerveau Numérique IA")
    print("   /admin      - Dashboard Admin")
    print()
    print("⚠️  Ctrl+C pour arrêter")
    print("=" * 60)
    print()
    app.run(debug=True, host='0.0.0.0', port=5000)
"""

# .env file
env_file = """# Yann's NOTE Configuration
GEMINI_API_KEY=your_gemini_api_key_here

# Instructions:
# 1. Obtenez une clé API Gemini sur: https://makersuite.google.com/app/apikey
# 2. Remplacez 'your_gemini_api_key_here' par votre vraie clé
# 3. Ne partagez JAMAIS ce fichier publiquement
"""

# requirements.txt
requirements = """Flask>=3.0.0
Flask-SQLAlchemy>=3.1.1
google-generativeai>=0.3.0
python-dotenv>=1.0.0
"""

# base.html template
base_html = """<!DOCTYPE html>
<html lang="{{ lang or 'fr' }}" class="dark">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="Permissions-Policy" content="camera=*, microphone=*, geolocation=*">
    <title>{% block title %}Yann's NOTE - Hub de Clarté IA{% endblock %}</title>
    <link rel="icon" href="data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2280%22>🦁</text></svg>">
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css') }}">
</head>
<body>
    <header class="site-header">
        <div class="container header-inner">
            <div class="brand">
                <a href="/" class="logo">
                    <span class="lion-icon">🦁</span>
                    Yann's <span class="highlight">NOTE</span>
                </a>
            </div>
            <nav class="main-nav">
                <a href="/" class="{{ 'active' if current_page == 'home' else '' }}">Accueil</a>
                <a href="/students" class="{{ 'active' if current_page == 'students' else '' }}">Étudiants</a>
                <a href="/business" class="{{ 'active' if current_page == 'business' else '' }}">Entreprises</a>
                <a href="/brain" class="{{ 'active' if current_page == 'brain' else '' }}">Cerveau IA</a>
                <a href="/admin" class="{{ 'active' if current_page == 'admin' else '' }}">Admin</a>
            </nav>
            <div class="lang-toggle">
                <button onclick="setLang('fr')" class="lang-btn {{ 'active' if lang == 'fr' else '' }}">FR</button>
                <button onclick="setLang('en')" class="lang-btn {{ 'active' if lang == 'en' else '' }}">EN</button>
            </div>
        </div>
    </header>

    <main class="main-content">
        <div class="container">
            {% block content %}{% endblock %}
        </div>
    </main>

    <footer class="site-footer">
        <div class="container">
            <p>© 2025 Yann's NOTE - Transformez le chaos en clarté</p>
        </div>
    </footer>

    <script src="{{ url_for('static', filename='js/main.js') }}"></script>
    {% block scripts %}{% endblock %}
</body>
</html>
"""

with open('app.py', 'w', encoding='utf-8') as f:
    f.write(app_py)
print("✓ app.py")

with open('.env', 'w', encoding='utf-8') as f:
    f.write(env_file)
print("✓ .env")

with open('requirements.txt', 'w', encoding='utf-8') as f:
    f.write(requirements)
print("✓ requirements.txt")

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(base_html)
print("✓ templates/base.html")

print("\n✅ Fichiers de base créés!")
print("\n⏳ Création des templates et CSS en cours...")
print("   (Le script va continuer...)")

# Je vais créer les autres fichiers dans la suite
print("\n" + "=" * 80)
print("✅ INSTALLATION DE BASE TERMINÉE!")
print("=" * 80)
print()
print("📝 Prochaines étapes:")
print("   1. Modifiez .env et ajoutez votre clé API Gemini")
print("   2. Exécutez: python create_templates.py (à venir)")
print("   3. Lancez: python app.py")
print()
input("Appuyez sur Entrée...")
