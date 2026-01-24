import os

print("=" * 80)
print("🎨 CRÉATION DES TEMPLATES ET STYLES")
print("=" * 80)
print()

# HOME TEMPLATE
home_html = """{% extends "base.html" %}
{% block title %}Yann's NOTE - Transformez le chaos en clarté{% endblock %}

{% block content %}
<div class="home-page">
    <!-- Hero Section -->
    <section class="hero-section">
        <div class="hero-badge">Hub de Clarté IA • Le Lion de la Tech</div>
        <h1 class="hero-title">
            Transformer le <span class="text-gold">chaos</span><br>
            en <span class="text-gold">clarté absolue.</span>
        </h1>
        <p class="hero-subtitle">
            Plus qu'un outil, un partenaire de réussite. L'IA de pointe ancrée dans les sources réelles 
            pour les leaders et étudiants du Cameroun.
        </p>
        <div class="hero-actions">
            <a href="/students" class="btn btn-primary">
                📚 Espace Étudiants
            </a>
            <a href="/business" class="btn btn-secondary">
                💼 Espace PME & Leaders
            </a>
        </div>
    </section>

    <!-- Services Section -->
    <section class="services-section">
        <div class="section-header">
            <h2>Nos Services Clés</h2>
            <div class="title-underline"></div>
        </div>
        <div class="services-grid">
            <div class="service-card">
                <div class="service-icon">🎙️</div>
                <h3>Podcast Express</h3>
                <p>Transformez vos documents en audio de 10 min.</p>
                <span class="service-tag">MP3 Zéro Data</span>
            </div>
            <div class="service-card">
                <div class="service-icon">🔍</div>
                <h3>Décodeur DAO</h3>
                <p>Analyse stratégique de vos appels d'offres.</p>
                <span class="service-tag">Expertise</span>
            </div>
            <div class="service-card">
                <div class="service-icon">📊</div>
                <h3>Pitch Deck 24h</h3>
                <p>Présentations percutantes livrées en un jour.</p>
                <span class="service-tag">Premium</span>
            </div>
            <div class="service-card">
                <div class="service-icon">📹</div>
                <h3>Résumé YouTube</h3>
                <p>L'essentiel des vidéos sans consommer de data.</p>
                <span class="service-tag">Zéro Data</span>
            </div>
            <div class="service-card">
                <div class="service-icon">🧠</div>
                <h3>Assistant Mémoire</h3>
                <p>Fiches de révision intelligentes et flashcards.</p>
                <span class="service-tag">Étudiants</span>
            </div>
        </div>
    </section>

    <!-- Value Props -->
    <section class="value-props">
        <div class="prop-card">
            <div class="prop-icon">🛡️</div>
            <h3>Preuve d'Exactitude</h3>
            <p>Chaque mot est ancré sur les sources. Nos rapports incluent des citations vérifiables.</p>
        </div>
        <div class="prop-card">
            <div class="prop-icon">⚡</div>
            <h3>Zéro Data (Optimisé)</h3>
            <p>Services MP3 et PDF ultra-légers. Apprenez n'importe où au Cameroun sans gaspiller.</p>
        </div>
        <div class="prop-card">
            <div class="prop-icon">🦁</div>
            <h3>Vitesse de Lion</h3>
            <p>Workflow hybride IA+Humain garantit des résultats premium en 24h.</p>
        </div>
    </section>

    <!-- Pricing -->
    <section class="pricing-section">
        <h2>Investissez dans votre <span class="text-gold">Clarté</span></h2>
        <p class="pricing-subtitle">Des tarifs justes, adaptés au marché camerounais.</p>
        
        <div class="pricing-grid">
            <div class="pricing-card">
                <h3>Pack Étudiant</h3>
                <div class="price">2 000 FCFA</div>
                <ul class="features">
                    <li>✓ Fiches audio illimitées</li>
                    <li>✓ Guide d'étude IA</li>
                    <li>✓ Badge Économe en Data</li>
                </ul>
                <button class="btn btn-outline">Démarrer</button>
            </div>
            
            <div class="pricing-card featured">
                <div class="badge">Recommandé</div>
                <h3>Pack PME</h3>
                <div class="price">50 000 FCFA</div>
                <ul class="features">
                    <li>✓ Audit de formalisation</li>
                    <li>✓ Pitch Deck de base</li>
                    <li>✓ Accès Cerveau Numérique</li>
                </ul>
                <button class="btn btn-primary">Démarrer</button>
            </div>
            
            <div class="pricing-card">
                <h3>Expert DAO</h3>
                <div class="price">120 000 FCFA</div>
                <ul class="features">
                    <li>✓ Gestion complète DAO</li>
                    <li>✓ Stratégie de réponse</li>
                    <li>✓ Citations sources garanties</li>
                </ul>
                <button class="btn btn-outline">Démarrer</button>
            </div>
        </div>
    </section>
</div>
{% endblock %}
"""

# STUDENTS TEMPLATE
students_html = """{% extends "base.html" %}
{% block title %}Services Étudiants - Yann's NOTE{% endblock %}

{% block content %}
<div class="students-page">
    <div class="page-header">
        <h1>Réussite Académique</h1>
        <p>Simplifiez vos révisions avec des fiches audio intelligentes et des guides d'étude.</p>
    </div>

    <section class="options-section glass">
        <h2>Générer mon Guide d'Étude</h2>
        
        <div class="options-grid">
            <div class="option-card" id="optionA">
                <div class="option-header">
                    <div class="option-icon">📄</div>
                    <h3>Option A : Mes propres cours</h3>
                </div>
                <p>Uploadez vos PDF ou photos de cahiers. Notre IA les analyse pour créer un guide structuré.</p>
                <div class="upload-zone" style="display:none;">
                    <input type="file" id="fileUpload" accept=".pdf,.png,.jpg,.jpeg" multiple>
                    <label for="fileUpload">
                        <div class="upload-icon">📤</div>
                        <p>PDF, PNG, JPG (Max 10MB)</p>
                    </label>
                </div>
            </div>
            
            <div class="option-card" id="optionB">
                <div class="option-header">
                    <div class="option-icon">💬</div>
                    <h3>Option B : Autre besoin</h3>
                </div>
                <p>Besoin de cours en ligne, d'une explication spécifique ou d'un coaching ? Discutez avec Yann.</p>
                <a href="https://wa.me/237676042996?text=Bonjour%20Yann,%20j'ai%20besoin%20d'aide%20pour%20mes%20révisions..." 
                   target="_blank" 
                   class="btn btn-whatsapp" 
                   style="display:none;">
                    💬 Discuter sur WhatsApp
                </a>
            </div>
        </div>
    </section>

    <section class="featured-services">
        <div class="feature-card glass">
            <span class="badge">Zéro Data</span>
            <div class="feature-icon">🎵</div>
            <h3>Audio Overviews</h3>
            <p>Transformez vos pavés de texte en podcasts digestes de 10 minutes. 
               Idéal pour réviser dans le taxi ou en marchant.</p>
            <button class="btn-link">Écouter un aperçu (30s) →</button>
        </div>
        
        <div class="feature-card glass">
            <div class="feature-icon">🃏</div>
            <h3>Flashcards IA</h3>
            <p>Générez automatiquement des questions/réponses basées sur les points clés 
               de votre cours pour tester votre mémoire.</p>
            <button class="btn-link">Voir un exemple →</button>
        </div>
    </section>
</div>

<script>
document.getElementById('optionA').addEventListener('click', function() {
    this.classList.add('active');
    document.getElementById('optionB').classList.remove('active');
    this.querySelector('.upload-zone').style.display = 'block';
    document.querySelector('#optionB .btn-whatsapp').style.display = 'none';
});

document.getElementById('optionB').addEventListener('click', function() {
    this.classList.add('active');
    document.getElementById('optionA').classList.remove('active');
    this.querySelector('.btn-whatsapp').style.display = 'flex';
    document.querySelector('#optionA .upload-zone').style.display = 'none';
});
</script>
{% endblock %}
"""

# BUSINESS TEMPLATE  
business_html = """{% extends "base.html" %}
{% block title %}Services Entreprises - Yann's NOTE{% endblock %}

{% block content %}
<div class="business-page">
    <div class="page-header">
        <h1>Formalisation & Croissance</h1>
        <p>Passez de l'informel au professionnel avec des documents de classe mondiale.</p>
    </div>

    <section class="business-services">
        <div class="service-card glass">
            <div class="service-icon-large">✅</div>
            <h3>Dossiers d'Appel d'Offres (DAO)</h3>
            <p>Rédaction stratégique et structuration de vos réponses aux appels d'offres publics et privés.</p>
            <ul class="feature-list">
                <li>🛡️ Analyse de conformité</li>
                <li>🛡️ Optimisation technique</li>
            </ul>
        </div>

        <div class="service-card glass">
            <div class="service-icon-large">📊</div>
            <h3>Pitch Decks & Business Plans</h3>
            <p>Documents visuels et financiers pour convaincre banques et investisseurs.</p>
            <div class="urgency-toggle">
                <label>
                    <input type="checkbox" id="urgentToggle">
                    <span>⏱️ Urgence 24h</span>
                </label>
            </div>
        </div>

        <div class="service-card glass">
            <div class="service-icon-large">🚀</div>
            <h3>Audit de Marque</h3>
            <p>Analyse de votre visibilité actuelle et recommandations de positionnement IA.</p>
            <button class="btn btn-primary">Lancer un audit</button>
        </div>
    </section>

    <section class="accuracy-section glass">
        <h2>La Preuve par la <span class="text-gold">Source</span></h2>
        <div class="accuracy-grid">
            <div class="accuracy-content">
                <p>Dans nos rapports de formalisation, chaque recommandation stratégique est liée 
                   à une citation directe des textes de loi camerounais ou de vos documents internes.</p>
                
                <div class="source-examples">
                    <div class="source-example">
                        <span class="source-tag">PDF</span>
                        <p class="source-text">"Conformément à l'article 12 du code OHADA... 
                           [Cliquer pour voir la source]"</p>
                    </div>
                    <div class="source-example">
                        <span class="source-tag">DAO</span>
                        <p class="source-text">"La capacité technique est justifiée par... 
                           [Cliquer pour voir la source]"</p>
                    </div>
                </div>
            </div>
            
            <div class="preview-mockup">
                <h4>Aperçu interactif</h4>
                <div class="mockup-lines">
                    <div class="line"></div>
                    <div class="line short"></div>
                    <div class="citation-block">[ BLOC DE CITATION SOURCE ]</div>
                    <div class="line medium"></div>
                </div>
            </div>
        </div>
    </section>
</div>
{% endblock %}
"""

# Écrire tous les templates
templates = {
    'templates/home.html': home_html,
    'templates/students.html': students_html,
    'templates/business.html': business_html
}

for filepath, content in templates.items():
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"✓ {filepath}")

print("\n✅ Templates de base créés!")
print("⏳ Création de brain.html et admin.html...")

# Continuer avec brain.html et admin.html dans la prochaine partie
input("\nAppuyez sur Entrée pour continuer...")
