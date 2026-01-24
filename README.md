# 🦁 Yann's NOTE - Hub de Clarté IA

Application Flask complète - Version Python du site React original

## 🎯 Vue d'ensemble

Yann's NOTE est une plateforme SaaS camerounaise qui transforme le chaos informationnel en clarté absolue grâce à l'IA, dédiée aux étudiants et entrepreneurs.

### ✨ Fonctionnalités

- 🏠 **Page d'accueil** - Hero section, services, tarifs
- 📚 **Services Étudiants** - Upload de documents, génération de guides d'étude
- 💼 **Services Entreprises** - DAO, Pitch Decks, Audits
- 🧠 **Cerveau Numérique IA** - Chat avec Google Gemini AI + grounding
- 👨‍💼 **Dashboard Admin** - Gestion de contenu avec statistiques temps réel
- 🌍 **Multilingue** - Français / Anglais
- 💾 **Base de données** - SQLite avec Flask-SQLAlchemy
- 🎨 **Design** - Glassmorphism, palette or/bleu marine, responsive

## 🚀 Installation Rapide (3 Scripts)

### Méthode Automatique

```bash
# Script 1: Installation de base
python setup_yanns_note.py

# Script 2: Création des templates
python create_templates.py

# Script 3: Fichiers finaux (CSS, JS, Brain, Admin)
python create_final_files.py
```

### Méthode Manuelle

1. **Créez les 3 fichiers Python** :
   - `setup_yanns_note.py`
   - `create_templates.py`
   - `create_final_files.py`

2. **Exécutez-les dans l'ordre** :
   ```bash
   python setup_yanns_note.py
   python create_templates.py
   python create_final_files.py
   ```

## 📋 Prérequis

- Python 3.8+
- pip
- Connexion Internet (pour installer les packages)

## 🔧 Configuration

### 1. Configuration de Gemini API

1. Obtenez une clé API gratuite sur https://makersuite.google.com/app/apikey
2. Ouvrez le fichier `.env`
3. Remplacez `your_gemini_api_key_here` par votre vraie clé :

```env
GEMINI_API_KEY=AIzaSyD...votre_cle_ici
```

### 2. Installation des dépendances

```bash
pip install -r requirements.txt
```

Ou manuellement :
```bash
pip install Flask Flask-SQLAlchemy google-generativeai python-dotenv
```

## 🎮 Lancement

```bash
python app.py
```

L'application sera disponible sur :
- **http://localhost:5000**
- **http://127.0.0.1:5000**

## 📁 Structure du Projet

```
yanns-note/
│
├── app.py                    # Application principale Flask
├── .env                      # Configuration (clé API)
├── requirements.txt          # Dépendances Python
├── yanns_note.db            # Base de données SQLite (auto-créée)
│
├── templates/
│   ├── base.html            # Layout principal
│   ├── home.html            # Page d'accueil
│   ├── students.html        # Services étudiants
│   ├── business.html        # Services entreprises
│   ├── brain.html           # Chat IA
│   └── admin.html           # Dashboard admin
│
└── static/
    ├── css/
    │   └── styles.css       # Styles complets
    └── js/
        └── main.js          # JavaScript
```

## 🌐 Pages et Routes

| Route | Description | Fonctionnalités |
|-------|-------------|-----------------|
| `/` | Accueil | Hero, services, pricing |
| `/students` | Services Étudiants | Upload docs, génération guides |
| `/business` | Services Entreprises | DAO, pitch decks, audits |
| `/brain` | Cerveau Numérique | Chat IA avec Gemini |
| `/admin` | Dashboard Admin | Gestion contenu, stats |

## 🎨 Palette de Couleurs

```css
--yann-blue: #001F3F     /* Bleu marine principal */
--yann-gold: #D4AF37     /* Or/doré */
--yann-steel: #71797E    /* Gris acier */
```

## 🔌 API Endpoints

### `POST /api/set-lang`
Change la langue de l'interface

```javascript
{
  "lang": "fr" // ou "en"
}
```

### `GET /api/content`
Récupère tous les contenus

### `POST /api/content`
Ajoute un nouveau contenu

```javascript
{
  "title": "Titre",
  "description": "Description",
  "category": "🎙️ Audio Overviews",
  "url": "https://...",
  "isZeroData": true
}
```

### `DELETE /api/content`
Supprime un contenu

```javascript
{
  "id": 1
}
```

### `POST /api/chat`
Envoie un message au cerveau IA

```javascript
{
  "message": "Votre question"
}
```

**Réponse** :
```javascript
{
  "text": "Réponse de l'IA",
  "sources": []
}
```

## 🗄️ Base de Données

### Modèle `ContentItem`

| Champ | Type | Description |
|-------|------|-------------|
| id | Integer | Clé primaire |
| title | String(200) | Titre du contenu |
| description | Text | Description |
| category | String(50) | Catégorie |
| url | String(500) | URL du fichier |
| is_zero_data | Boolean | Badge "Zéro Data" |
| created_at | DateTime | Date de création |

### Modèle `ChatMessage`

| Champ | Type | Description |
|-------|------|-------------|
| id | Integer | Clé primaire |
| role | String(20) | 'user' ou 'ai' |
| text | Text | Contenu du message |
| sources | Text | Sources JSON |
| created_at | DateTime | Date de création |

## 🤖 Intégration Gemini AI

L'application utilise Google Gemini Pro pour :
- Répondre aux questions des utilisateurs
- Analyser les documents uploadés
- Fournir des réponses contextuelles avec grounding

**Configuration système** :
```
Tu es Yann's NOTE IA, l'Assistant de Clarté par excellence au Cameroun. 
Ton rôle est de transformer le chaos informationnel en clarté absolue.
```

## ⚙️ Configuration Avancée

### Changer le Port

Dans `app.py` :
```python
app.run(debug=True, host='0.0.0.0', port=8080)  # Port personnalisé
```

### Mode Production

```python
app.run(debug=False, host='0.0.0.0', port=5000)
```

### Secret Key

Changez la `SECRET_KEY` dans `app.py` pour la production :
```python
app.config['SECRET_KEY'] = 'votre-cle-secrete-aleatoire'
```

## 🐛 Dépannage

### Erreur : Module 'flask' not found
```bash
pip install Flask
```

### Erreur : google.generativeai not found
```bash
pip install google-generativeai
```

### Erreur API Gemini
Vérifiez que :
1. Votre clé API est correcte dans `.env`
2. Vous avez activé l'API Gemini sur Google Cloud
3. Vous n'avez pas dépassé les quotas gratuits

### Base de données verrouillée
Supprimez `yanns_note.db` et relancez l'application

## 📊 Fonctionnalités par Page

### 🏠 Home
- Hero section animée
- 5 services clés en grille
- 3 propositions de valeur
- Grille tarifaire (3 plans)

### 📚 Students
- 2 options : Upload docs / Contact WhatsApp
- Cartes services (Audio, Flashcards)
- Upload de fichiers fonctionnel

### 💼 Business
- 3 services professionnels
- Toggle urgence 24h
- Section "Preuve par la Source"
- Preview mockup interactif

### 🧠 Brain
- Chat en temps réel avec IA
- Sidebar avec statistiques
- Barre de stockage
- Indicateur de frappe
- Citations de sources

### 👨‍💼 Admin
- Statistiques temps réel
- Table de gestion
- Formulaire d'ajout
- CRUD complet

## 🎓 Technologies Utilisées

- **Backend** : Flask 3.0+
- **Base de données** : SQLite + SQLAlchemy
- **IA** : Google Gemini Pro
- **Frontend** : Jinja2, CSS personnalisé, JavaScript Vanilla
- **Fonts** : Inter (Google Fonts)

## 📝 TODO / Améliorations Futures

- [ ] Upload réel de fichiers (actuellement simulé)
- [ ] Intégration WhatsApp API
- [ ] Export PDF des rapports
- [ ] Système d'authentification
- [ ] Paiement mobile money
- [ ] Analytics avancées
- [ ] Notifications push
- [ ] Mode hors-ligne (PWA)

## 📄 Licence

© 2025 Yann's NOTE - Tous droits réservés

## 🆘 Support

En cas de problème :
1. Vérifiez que tous les fichiers sont créés
2. Consultez les logs de Flask dans le terminal
3. Vérifiez votre fichier `.env`
4. Testez avec une clé API Gemini valide

## 🎉 Démarrage Rapide (Résumé)

```bash
# 1. Créer les fichiers
python setup_yanns_note.py
python create_templates.py
python create_final_files.py

# 2. Installer les dépendances
pip install -r requirements.txt

# 3. Configurer .env
# Ajoutez votre clé Gemini API

# 4. Lancer
python app.py

# 5. Ouvrir
# http://localhost:5000
```

---

**Fait avec ❤️ et Flask au Cameroun** 🦁
