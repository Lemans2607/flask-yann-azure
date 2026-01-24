import os

print("=" * 80)
print("🎨 CRÉATION DES FICHIERS FINAUX")
print("=" * 80)
print()

# BRAIN TEMPLATE
brain_html = """{% extends "base.html" %}
{% block title %}Cerveau Numérique IA - Yann's NOTE{% endblock %}

{% block content %}
<div class="brain-page">
    <div class="brain-layout">
        <!-- Sidebar -->
        <aside class="brain-sidebar glass">
            <h3>🗄️ Coffre-Fort Numérique</h3>
            
            <div class="stats">
                <div class="stat-item">
                    <span class="label">Documents Analysés</span>
                    <span class="value">24</span>
                </div>
                <div class="stat-item">
                    <span class="label">Audio Overviews</span>
                    <span class="value">8</span>
                </div>
                <div class="stat-item">
                    <span class="label">Status IA</span>
                    <span class="value connected">Connecté</span>
                </div>
            </div>

            <div class="storage-bar">
                <div class="storage-label">
                    <span>Stockage Data</span>
                    <span>42 MB / 1 GB</span>
                </div>
                <div class="progress-bar">
                    <div class="progress" style="width: 4%"></div>
                </div>
            </div>

            <button class="btn-upload">
                📤 Ajouter au Cerveau
            </button>

            <div class="info-box">
                <strong>Grounding :</strong> Les réponses sont ancrées sur le Web en temps réel 
                via Google Search pour garantir l'actualité des lois et news au Cameroun.
            </div>
        </aside>

        <!-- Chat Interface -->
        <div class="brain-chat glass">
            <div class="chat-header">
                <div class="chat-header-content">
                    <div class="brain-icon">🧠</div>
                    <div>
                        <h4>Yann's <span class="text-gold">Brain IA</span></h4>
                        <p class="subtitle">Expert en Clarté Contextuelle</p>
                    </div>
                </div>
            </div>

            <div class="chat-messages" id="chatMessages">
                {% for msg in messages %}
                <div class="message {{ msg.role }}">
                    <div class="message-content">{{ msg.text }}</div>
                    {% if msg.sources %}
                    <div class="sources">
                        <!-- Sources ici -->
                    </div>
                    {% endif %}
                </div>
                {% endfor %}
                
                {% if messages|length == 0 %}
                <div class="message ai">
                    <div class="message-content">
                        Bienvenue dans ton Cerveau Numérique. Je suis connecté à Google Search 
                        et à tes documents pour t'apporter une clarté totale sans hallucinations.
                    </div>
                </div>
                {% endif %}
            </div>

            <div class="chat-input">
                <input type="text" 
                       id="messageInput" 
                       placeholder="Poser une question stratégique..."
                       onkeypress="if(event.key==='Enter') sendMessage()">
                <button onclick="sendMessage()" class="btn-send">📤</button>
            </div>
            
            <p class="disclaimer">
                Yann's NOTE IA peut faire des erreurs. Vérifiez toujours les sources citées.
            </p>
        </div>
    </div>
</div>

<script>
async function sendMessage() {
    const input = document.getElementById('messageInput');
    const message = input.value.trim();
    if (!message) return;
    
    const messagesDiv = document.getElementById('chatMessages');
    
    // Add user message
    messagesDiv.innerHTML += `
        <div class="message user">
            <div class="message-content">${message}</div>
        </div>
    `;
    input.value = '';
    
    // Show typing indicator
    messagesDiv.innerHTML += `
        <div class="message ai typing">
            <div class="typing-indicator">
                <span></span><span></span><span></span>
            </div>
        </div>
    `;
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
    
    // Send to API
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({message})
        });
        const data = await response.json();
        
        // Remove typing indicator
        document.querySelector('.typing')?.remove();
        
        // Add AI response
        messagesDiv.innerHTML += `
            <div class="message ai">
                <div class="message-content">${data.text}</div>
            </div>
        `;
        messagesDiv.scrollTop = messagesDiv.scrollHeight;
    } catch (error) {
        console.error('Error:', error);
        document.querySelector('.typing')?.remove();
        messagesDiv.innerHTML += `
            <div class="message ai error">
                <div class="message-content">Erreur de connexion. Réessayez.</div>
            </div>
        `;
    }
}
</script>
{% endblock %}
"""

# ADMIN TEMPLATE
admin_html = """{% extends "base.html" %}
{% block title %}Admin Dashboard - Yann's NOTE{% endblock %}

{% block content %}
<div class="admin-page">
    <div class="admin-layout">
        <!-- Sidebar -->
        <aside class="admin-sidebar">
            <button class="nav-btn active">📊 Dashboard</button>
            <button class="nav-btn">🗄️ Documents</button>
            <button class="nav-btn">⚙️ Configuration</button>
        </aside>

        <!-- Content -->
        <div class="admin-content">
            <div class="admin-header glass">
                <div>
                    <h1>Bienvenue, Admin</h1>
                    <p>🕐 {{ current_time }}</p>
                </div>
                <div class="activity-badge">
                    <span class="label">Activité Aujourd'hui</span>
                    <span class="count">{{ items_today }} item{{ 's' if items_today != 1 else '' }}</span>
                </div>
            </div>

            <div class="content-management">
                <div class="section-header">
                    <h2>Gestion du Contenu</h2>
                    <button class="btn btn-primary" onclick="showAddForm()">
                        ➕ Ajouter
                    </button>
                </div>

                <div id="addForm" class="add-form glass" style="display:none;">
                    <div class="form-grid">
                        <div class="form-group">
                            <label>Titre</label>
                            <input type="text" id="title" class="form-input">
                        </div>
                        <div class="form-group">
                            <label>Catégorie</label>
                            <select id="category" class="form-input">
                                <option>🎙️ Audio Overviews</option>
                                <option>🎬 Video Overviews</option>
                                <option>📊 Slide Decks</option>
                                <option>🎨 Infographies</option>
                            </select>
                        </div>
                        <div class="form-group full-width">
                            <label>URL du fichier</label>
                            <input type="text" id="url" class="form-input" placeholder="https://...">
                        </div>
                        <div class="form-group full-width">
                            <label>Description</label>
                            <textarea id="description" class="form-input" rows="3"></textarea>
                        </div>
                    </div>
                    <div class="form-actions">
                        <button onclick="hideAddForm()" class="btn btn-outline">Annuler</button>
                        <button onclick="saveContent()" class="btn btn-primary">💾 Enregistrer</button>
                    </div>
                </div>

                <div class="content-table glass">
                    <table>
                        <thead>
                            <tr>
                                <th>Titre</th>
                                <th>Catégorie</th>
                                <th>Status</th>
                                <th>Actions</th>
                            </tr>
                        </thead>
                        <tbody id="contentList">
                            {% if items|length == 0 %}
                            <tr>
                                <td colspan="4" class="empty">Aucun contenu pour le moment.</td>
                            </tr>
                            {% else %}
                            {% for item in items %}
                            <tr data-id="{{ item.id }}">
                                <td><strong>{{ item.title }}</strong></td>
                                <td>{{ item.category }}</td>
                                <td>
                                    {% if item.is_zero_data %}
                                    <span class="badge-zero">ZERO DATA</span>
                                    {% endif %}
                                </td>
                                <td class="actions">
                                    <button onclick="editItem({{ item.id }})" class="btn-icon">✏️</button>
                                    <button onclick="deleteItem({{ item.id }})" class="btn-icon delete">🗑️</button>
                                </td>
                            </tr>
                            {% endfor %}
                            {% endif %}
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
</div>

<script>
function showAddForm() {
    document.getElementById('addForm').style.display = 'block';
}

function hideAddForm() {
    document.getElementById('addForm').style.display = 'none';
    clearForm();
}

function clearForm() {
    document.getElementById('title').value = '';
    document.getElementById('description').value = '';
    document.getElementById('url').value = '';
}

async function saveContent() {
    const data = {
        title: document.getElementById('title').value,
        description: document.getElementById('description').value,
        category: document.getElementById('category').value,
        url: document.getElementById('url').value,
        isZeroData: true
    };
    
    const response = await fetch('/api/content', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data)
    });
    
    if (response.ok) {
        location.reload();
    }
}

async function deleteItem(id) {
    if (!confirm('Supprimer cet élément ?')) return;
    
    const response = await fetch('/api/content', {
        method: 'DELETE',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({id})
    });
    
    if (response.ok) {
        location.reload();
    }
}
</script>
{% endblock %}
"""

# CSS COMPLET
styles_css = """:root {
    --yann-blue: #001F3F;
    --yann-gold: #D4AF37;
    --yann-steel: #71797E;
    --yann-light: rgba(255, 255, 255, 0.05);
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Inter', sans-serif;
    background: var(--yann-blue);
    color: white;
    line-height: 1.6;
    min-height: 100vh;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 2rem;
}

.glass {
    background: rgba(255, 255, 255, 0.05);
    backdrop-filter: blur(10px);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 1.5rem;
}

/* HEADER */
.site-header {
    padding: 1.5rem 0;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.header-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 2rem;
}

.logo {
    display: flex;
    align-items: center;
    gap: 0.5rem;
    font-size: 1.5rem;
    font-weight: 800;
    color: white;
    text-decoration: none;
}

.lion-icon {
    font-size: 2rem;
}

.highlight {
    color: var(--yann-gold);
}

.main-nav {
    display: flex;
    gap: 2rem;
}

.main-nav a {
    color: rgba(255, 255, 255, 0.7);
    text-decoration: none;
    font-weight: 600;
    transition: color 0.3s;
}

.main-nav a:hover,
.main-nav a.active {
    color: var(--yann-gold);
}

.lang-toggle {
    display: flex;
    gap: 0.5rem;
}

.lang-btn {
    padding: 0.5rem 1rem;
    background: transparent;
    border: 2px solid rgba(255, 255, 255, 0.2);
    color: white;
    border-radius: 0.5rem;
    cursor: pointer;
    font-weight: 700;
    transition: all 0.3s;
}

.lang-btn:hover,
.lang-btn.active {
    background: var(--yann-gold);
    border-color: var(--yann-gold);
    color: var(--yann-blue);
}

/* MAIN CONTENT */
.main-content {
    padding: 4rem 0;
    min-height: 70vh;
}

/* BUTTONS */
.btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 0.5rem;
    padding: 1rem 2rem;
    border-radius: 0.75rem;
    font-weight: 700;
    text-decoration: none;
    transition: all 0.3s;
    border: none;
    cursor: pointer;
    font-size: 1rem;
}

.btn-primary {
    background: var(--yann-gold);
    color: var(--yann-blue);
}

.btn-primary:hover {
    transform: scale(1.05);
    box-shadow: 0 10px 30px rgba(212, 175, 55, 0.3);
}

.btn-secondary,
.btn-outline {
    background: transparent;
    color: var(--yann-gold);
    border: 2px solid var(--yann-gold);
}

.btn-secondary:hover,
.btn-outline:hover {
    background: var(--yann-gold);
    color: var(--yann-blue);
}

/* HOME PAGE */
.hero-section {
    text-align: center;
    padding: 6rem 0;
    position: relative;
}

.hero-badge {
    display: inline-block;
    padding: 0.5rem 1.5rem;
    background: rgba(212, 175, 55, 0.1);
    border: 1px solid var(--yann-gold);
    border-radius: 2rem;
    color: var(--yann-gold);
    font-size: 0.75rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.1em;
    margin-bottom: 2rem;
}

.hero-title {
    font-size: 4rem;
    font-weight: 900;
    line-height: 1.1;
    margin-bottom: 1.5rem;
}

.text-gold {
    color: var(--yann-gold);
}

.hero-subtitle {
    font-size: 1.25rem;
    color: var(--yann-steel);
    max-width: 800px;
    margin: 0 auto 3rem;
}

.hero-actions {
    display: flex;
    gap: 1rem;
    justify-content: center;
    flex-wrap: wrap;
}

.services-section,
.value-props,
.pricing-section {
    padding: 4rem 0;
}

.section-header {
    text-align: center;
    margin-bottom: 3rem;
}

.section-header h2 {
    font-size: 2.5rem;
    font-weight: 900;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    margin-bottom: 1rem;
}

.title-underline {
    width: 80px;
    height: 4px;
    background: var(--yann-gold);
    margin: 0 auto;
    border-radius: 2px;
}

.services-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.5rem;
}

.service-card {
    padding: 2rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 1.5rem;
    text-align: center;
    transition: all 0.3s;
}

.service-card:hover {
    border-color: var(--yann-gold);
    transform: translateY(-5px);
}

.service-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.service-card h3 {
    margin-bottom: 0.5rem;
    font-size: 1.1rem;
}

.service-card p {
    font-size: 0.9rem;
    color: var(--yann-steel);
    margin-bottom: 1rem;
}

.service-tag {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 1rem;
    font-size: 0.7rem;
    font-weight: 700;
    color: var(--yann-gold);
}

.value-props {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
    gap: 2rem;
}

.prop-card {
    padding: 2.5rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 1.5rem;
}

.prop-icon {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.prop-card h3 {
    margin-bottom: 1rem;
}

.prop-card p {
    color: var(--yann-steel);
}

.pricing-section {
    text-align: center;
}

.pricing-subtitle {
    color: var(--yann-steel);
    margin-bottom: 3rem;
}

.pricing-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: 2rem;
    max-width: 1000px;
    margin: 0 auto;
}

.pricing-card {
    padding: 2.5rem;
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 1.5rem;
    position: relative;
    transition: transform 0.3s;
}

.pricing-card:hover {
    transform: translateY(-10px);
}

.pricing-card.featured {
    border-color: var(--yann-gold);
    border-width: 2px;
    transform: scale(1.05);
}

.pricing-card .badge {
    position: absolute;
    top: 0;
    right: 0;
    background: var(--yann-gold);
    color: var(--yann-blue);
    padding: 0.5rem 1.5rem;
    border-radius: 0 1.5rem 0 1rem;
    font-size: 0.7rem;
    font-weight: 800;
    text-transform: uppercase;
}

.price {
    font-size: 2.5rem;
    font-weight: 900;
    color: var(--yann-gold);
    margin: 1rem 0 2rem;
}

.features {
    list-style: none;
    text-align: left;
    margin-bottom: 2rem;
}

.features li {
    padding: 0.5rem 0;
    color: var(--yann-steel);
}

/* BRAIN PAGE */
.brain-layout {
    display: grid;
    grid-template-columns: 300px 1fr;
    gap: 2rem;
}

.brain-sidebar {
    padding: 2rem;
}

.brain-sidebar h3 {
    margin-bottom: 2rem;
    font-size: 1rem;
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

.stats {
    margin-bottom: 2rem;
}

.stat-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
    font-size: 0.85rem;
}

.stat-item .label {
    color: var(--yann-steel);
}

.stat-item .value {
    font-weight: 700;
    color: var(--yann-gold);
}

.stat-item .connected {
    color: #22c55e;
}

.storage-bar {
    margin: 2rem 0;
}

.storage-label {
    display: flex;
    justify-content: space-between;
    font-size: 0.7rem;
    color: var(--yann-steel);
    margin-bottom: 0.5rem;
    font-weight: 700;
    text-transform: uppercase;
}

.progress-bar {
    height: 8px;
    background: rgba(255, 255, 255, 0.1);
    border-radius: 1rem;
    overflow: hidden;
}

.progress {
    height: 100%;
    background: var(--yann-gold);
    transition: width 0.3s;
}

.btn-upload {
    width: 100%;
    padding: 1.5rem;
    background: transparent;
    border: 2px dashed var(--yann-gold);
    color: var(--yann-gold);
    border-radius: 1.5rem;
    cursor: pointer;
    font-weight: 700;
    transition: all 0.3s;
}

.btn-upload:hover {
    background: rgba(212, 175, 55, 0.1);
}

.info-box {
    margin-top: 2rem;
    padding: 1rem;
    background: rgba(212, 175, 55, 0.1);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 1rem;
    font-size: 0.75rem;
    line-height: 1.5;
}

.brain-chat {
    display: flex;
    flex-direction: column;
    height: 700px;
}

.chat-header {
    padding: 1.5rem;
    border-bottom: 1px solid rgba(255, 255, 255, 0.1);
}

.chat-header-content {
    display: flex;
    align-items: center;
    gap: 1rem;
}

.brain-icon {
    font-size: 2.5rem;
}

.subtitle {
    font-size: 0.7rem;
    color: var(--yann-steel);
    text-transform: uppercase;
    font-weight: 700;
    letter-spacing: 0.1em;
}

.chat-messages {
    flex: 1;
    overflow-y: auto;
    padding: 2rem;
}

.message {
    margin-bottom: 1.5rem;
    display: flex;
    justify-content: flex-start;
}

.message.user {
    justify-content: flex-end;
}

.message-content {
    max-width: 80%;
    padding: 1rem 1.5rem;
    border-radius: 1rem;
    font-size: 0.95rem;
    line-height: 1.6;
}

.message.user .message-content {
    background: var(--yann-gold);
    color: var(--yann-blue);
    font-weight: 600;
}

.message.ai .message-content {
    background: rgba(255, 255, 255, 0.05);
    border: 1px solid rgba(255, 255, 255, 0.1);
}

.typing-indicator {
    display: flex;
    gap: 0.5rem;
}

.typing-indicator span {
    width: 8px;
    height: 8px;
    background: var(--yann-gold);
    border-radius: 50%;
    animation: bounce 1.4s infinite ease-in-out;
}

.typing-indicator span:nth-child(2) {
    animation-delay: 0.2s;
}

.typing-indicator span:nth-child(3) {
    animation-delay: 0.4s;
}

@keyframes bounce {
    0%, 80%, 100% { transform: scale(0); }
    40% { transform: scale(1); }
}

.chat-input {
    display: flex;
    gap: 1rem;
    padding: 1.5rem;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
}

.chat-input input {
    flex: 1;
    padding: 1rem 1.5rem;
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 1rem;
    color: white;
    font-size: 1rem;
}

.chat-input input:focus {
    outline: none;
    border-color: var(--yann-gold);
}

.btn-send {
    padding: 1rem 1.5rem;
    background: transparent;
    border: 1px solid var(--yann-gold);
    color: var(--yann-gold);
    border-radius: 1rem;
    cursor: pointer;
    transition: all 0.3s;
}

.btn-send:hover {
    background: var(--yann-gold);
    color: var(--yann-blue);
}

.disclaimer {
    padding: 0 1.5rem 1rem;
    text-align: center;
    font-size: 0.7rem;
    color: var(--yann-steel);
}

/* ADMIN PAGE */
.admin-layout {
    display: grid;
    grid-template-columns: 200px 1fr;
    gap: 2rem;
}

.admin-sidebar {
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.nav-btn {
    padding: 1rem;
    background: transparent;
    border: none;
    color: rgba(255, 255, 255, 0.7);
    text-align: left;
    border-radius: 0.75rem;
    cursor: pointer;
    font-weight: 600;
    transition: all 0.3s;
}

.nav-btn:hover,
.nav-btn.active {
    background: var(--yann-gold);
    color: var(--yann-blue);
}

.admin-header {
    padding: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.activity-badge {
    text-align: center;
    padding: 1rem 1.5rem;
    background: rgba(212, 175, 55, 0.1);
    border: 1px solid rgba(212, 175, 55, 0.3);
    border-radius: 1rem;
}

.activity-badge .label {
    display: block;
    font-size: 0.7rem;
    text-transform: uppercase;
    color: var(--yann-gold);
    font-weight: 700;
    margin-bottom: 0.25rem;
}

.activity-badge .count {
    font-size: 1.5rem;
    font-weight: 900;
}

.content-management {
    margin-top: 2rem;
}

.section-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.add-form {
    padding: 2rem;
    margin-bottom: 2rem;
}

.form-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 1.5rem;
    margin-bottom: 1.5rem;
}

.form-group.full-width {
    grid-column: span 2;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-size: 0.85rem;
    font-weight: 700;
    text-transform: uppercase;
    color: var(--yann-steel);
}

.form-input {
    width: 100%;
    padding: 0.75rem 1rem;
    background: rgba(0, 0, 0, 0.4);
    border: 1px solid rgba(255, 255, 255, 0.1);
    border-radius: 0.5rem;
    color: white;
    font-size: 0.95rem;
}

.form-input:focus {
    outline: none;
    border-color: var(--yann-gold);
}

.form-actions {
    display: flex;
    justify-content: flex-end;
    gap: 1rem;
}

.content-table {
    padding: 0;
    overflow: hidden;
}

.content-table table {
    width: 100%;
    border-collapse: collapse;
}

.content-table thead {
    background: rgba(255, 255, 255, 0.05);
}

.content-table th,
.content-table td {
    padding: 1rem 1.5rem;
    text-align: left;
}

.content-table th {
    font-size: 0.75rem;
    text-transform: uppercase;
    color: var(--yann-steel);
    font-weight: 700;
}

.content-table tbody tr {
    border-bottom: 1px solid rgba(255, 255, 255, 0.05);
    transition: background 0.3s;
}

.content-table tbody tr:hover {
    background: rgba(255, 255, 255, 0.02);
}

.content-table td.empty {
    text-align: center;
    padding: 3rem;
    color: var(--yann-steel);
}

.badge-zero {
    padding: 0.25rem 0.75rem;
    background: rgba(212, 175, 55, 0.2);
    color: var(--yann-gold);
    border-radius: 1rem;
    font-size: 0.7rem;
    font-weight: 700;
}

.actions {
    display: flex;
    gap: 0.5rem;
}

.btn-icon {
    padding: 0.5rem;
    background: transparent;
    border: none;
    cursor: pointer;
    transition: transform 0.2s;
}

.btn-icon:hover {
    transform: scale(1.2);
}

.btn-icon.delete:hover {
    filter: brightness(1.5);
}

/* FOOTER */
.site-footer {
    margin-top: auto;
    padding: 2rem 0;
    border-top: 1px solid rgba(255, 255, 255, 0.1);
    text-align: center;
    color: var(--yann-steel);
}

/* RESPONSIVE */
@media (max-width: 768px) {
    .brain-layout,
    .admin-layout {
        grid-template-columns: 1fr;
    }
    
    .hero-title {
        font-size: 2.5rem;
    }
    
    .main-nav {
        flex-direction: column;
        gap: 1rem;
    }
}
"""

# MAIN JS
main_js = """// Language Toggle
async function setLang(lang) {
    await fetch('/api/set-lang', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({lang})
    });
    location.reload();
}

// Smooth scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        const target = document.querySelector(this.getAttribute('href'));
        if (target) {
            target.scrollIntoView({behavior: 'smooth'});
        }
    });
});

console.log('🦁 Yann\\'s NOTE - Powered by Flask & AI');
"""

# Écrire tous les fichiers
files = {
    'templates/brain.html': brain_html,
    'templates/admin.html': admin_html,
    'static/css/styles.css': styles_css,
    'static/js/main.js': main_js
}

for filepath, content in files.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

print("\n" + "=" * 80)
print("✅ TOUS LES FICHIERS ONT ÉTÉ CRÉÉS!")
print("=" * 80)
print()
print("📁 Structure complète:")
print("   yanns-note/")
print("   ├── app.py")
print("   ├── .env")
print("   ├── requirements.txt")
print("   ├── yanns_note.db (créée au démarrage)")
print("   ├── templates/")
print("   │   ├── base.html")
print("   │   ├── home.html")
print("   │   ├── students.html")
print("   │   ├── business.html")
print("   │   ├── brain.html")
print("   │   └── admin.html")
print("   └── static/")
print("       ├── css/styles.css")
print("       └── js/main.js")
print()
print("🚀 Prochaines étapes:")
print("   1. Installez les dépendances:")
print("      py -m pip install -r requirements.txt")
print()
print("   2. Configurez votre clé API Gemini dans .env:")
print("      GEMINI_API_KEY=votre_cle_ici")
print()
print("   3. Lancez l'application:")
print("      python app.py")
print()
print("   4. Ouvrez http://localhost:5000")
print()
print("=" * 80)
input("\nAppuyez sur Entrée pour terminer...")
