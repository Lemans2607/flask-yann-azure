import os
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
            system_prompt = """Tu es Yann's NOTE IA, l'Assistant de Clarté par excellence au Cameroun. 
Ton rôle est de transformer le chaos informationnel en clarté absolue. 
Utilise un ton professionnel, encourageant et cite toujours tes sources. 
Réponds en français ou anglais selon la demande. Pas d'hallucinations."""
            
            response = model.generate_content(f"{system_prompt}\n\nQuestion: {user_message}")
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
