"""
Chrome partagé (head/header/nav/overlay de recherche/pied de page/panneau
du Professeur IA) pour chaque page du cours de français. Frère de
scripts/site_chrome.py du cours d'espagnol, du cours d'anglais et du
cours d'italien, combinant le meilleur des trois :

  1. Les 7 niveaux du cours d'anglais (Pre-A1 inclus), pas les 6 du
     cours d'italien.
  2. Le panneau du Professeur IA du cours d'anglais/espagnol, adapté
     à un prompt en français (voir worker/worker.js) — le cours
     italien ne l'a pas encore.
  3. Le principe "toute page générée par ce module" du cours italien :
     TOUTE page du site (pas seulement les leçons) passe par
     head()/header()/footer(), donc il n'existe qu'une seule copie du
     balisage d'en-tête/pied de page dans tout le dépôt.

REL est le préfixe de chemin relatif depuis le fichier généré jusqu'à
la racine du dépôt : "" pour les pages de premier niveau, "levels/"
pour levels/{niveau}.html, et "../../" pour levels/{niveau}/{leçon}.html.
"""

LEVELS = [
    ("Pre-A1", "Survie", "pre-a1"),
    ("A1", "Débutant", "a1"),
    ("A2", "Élémentaire", "a2"),
    ("B1", "Intermédiaire", "b1"),
    ("B2", "Intermédiaire avancé", "b2"),
    ("C1", "Avancé", "c1"),
    ("C2", "Maîtrise", "c2"),
]

# Fleur de lis — le brand mark et le motif décoratif de stars-row utilisent
# tous deux ce même emblème (construit à partir de formes symétriques
# simples : un pétale central en amande, deux pétales latéraux en volute
# mutuellement en miroir, un bandeau et une hampe) plutôt qu'un tracé
# hérité de bibliothèque d'icônes, pour rester lisible même minuscule
# (13px dans stars-row).
BRAND_MARK_SVG = (
    '<svg class="brand__mark" viewBox="0 0 40 40" aria-hidden="true">'
    '<circle cx="20" cy="20" r="18.4" fill="none" stroke="currentColor" stroke-width="1.6"/>'
    '<path d="M20,3 C25,8 26,15 20,20 C14,15 15,8 20,3 Z" fill="currentColor"/>'
    '<path d="M22,9 C30,7 36,13 33,20 C31,24 25,24 22,20 Z" fill="currentColor"/>'
    '<path d="M18,9 C10,7 4,13 7,20 C9,24 15,24 18,20 Z" fill="currentColor"/>'
    '<rect x="13" y="22" width="14" height="4" rx="2" fill="currentColor"/>'
    '<path d="M18.5,26 L21.5,26 L20.8,34 L19.2,34 Z" fill="currentColor"/>'
    "</svg>"
)

STAR = (
    '<svg class="stars-row__star" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">'
    '<path d="M12,1.8 C15,4.8 15.6,9 12,12 C8.4,9 9,4.8 12,1.8 Z"/>'
    '<path d="M13.2,5.4 C18,4.2 21.6,7.8 19.8,12 C18.6,14.4 15,14.4 13.2,12 Z"/>'
    '<path d="M10.8,5.4 C6,4.2 2.4,7.8 4.2,12 C5.4,14.4 9,14.4 10.8,12 Z"/>'
    '<rect x="7.8" y="13.2" width="8.4" height="2.4" rx="1.2"/>'
    '<path d="M11.1,15.6 L12.9,15.6 L12.5,20.4 L11.5,20.4 Z"/>'
    "</svg>"
)
STARS_ROW = f'<div class="stars-row stars-row--onlight" aria-hidden="true">{STAR * 11}</div>'
STARS_ROW_GOLD = f'<div class="stars-row stars-row--gold" aria-hidden="true">{STAR * 11}</div>'
CHECK_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m5 12 5 5L20 7"/></svg>'
ARROW_SVG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>'

# Endpoint du Worker du Professeur IA. worker/wrangler.toml doit nommer le
# Worker "ai-teacher-fr" ; ce site n'a PAS encore de Worker déployé (voir
# AI_TEACHER_ENABLED ci-dessous) — une fois worker/ déployé avec ta propre
# URL, remplace la valeur ci-dessous par celle imprimée par
# `wrangler deploy` (voir worker/README.md, étape 6) et reconstruis le site.
AI_TEACHER_WORKER_URL = "https://ai-teacher-fr.englishclasses.workers.dev"

# Le bouton/panneau du Professeur IA n'est généré que si ceci vaut True.
# Le Worker n'est pas encore déployé (AI_TEACHER_WORKER_URL est un
# placeholder) — le laisser à False tant que worker/ n'est pas réellement
# déployé, sinon le chat s'ouvre mais ne répond jamais. Mets-le à True une
# fois le Worker déployé avec ta propre URL, puis reconstruis le site.
AI_TEACHER_ENABLED = False


def nav_levels_html(rel, active_level_code):
    items = []
    for code, name, slug in LEVELS:
        current = ' aria-current="page"' if code.upper() == (active_level_code or "").upper() else ""
        items.append(
            f'<li><a href="{rel}levels/{slug}.html"{current}><span>{name}</span>'
            f'<span class="level-code">{code}</span></a></li>'
        )
    return "".join(items)


def head(rel, title, description, extra_css=None):
    extra = "".join(f'<link rel="stylesheet" href="{rel}assets/css/{c}.css">' for c in (extra_css or []))
    return f"""<!DOCTYPE html>
<html lang="fr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="Renan le Professeur — Académie de Français">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{description}">
<link rel="icon" href="{rel}assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{rel}assets/img/apple-touch-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400;0,9..144,600;0,9..144,700;1,9..144,500&family=Source+Sans+3:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{rel}assets/css/tokens.css">
<link rel="stylesheet" href="{rel}assets/css/base.css">
<link rel="stylesheet" href="{rel}assets/css/components.css">
<link rel="stylesheet" href="{rel}assets/css/layout.css">
<link rel="stylesheet" href="{rel}assets/css/dark-mode.css">
<link rel="stylesheet" href="{rel}assets/css/ai-teacher.css">
<link rel="stylesheet" href="{rel}assets/css/search.css">{extra}
<script>
(function(){{try{{var t=localStorage.getItem('theme');if(!t){{t=window.matchMedia('(prefers-color-scheme: dark)').matches?'dark':'light';}}document.documentElement.setAttribute('data-theme',t);}}catch(e){{}}}})();
</script>
</head>"""


def header(rel, active_level_code, breadcrumb_html=None, active_top=None):
    breadcrumb = (
        f"""<nav class="breadcrumbs" aria-label="Fil d'Ariane">
        <ol>
        {breadcrumb_html}
        </ol>
    </nav>"""
        if breadcrumb_html
        else ""
    )

    def top(label, href_suffix, id_=None):
        current = ' aria-current="page"' if id_ and id_ == active_top else ""
        return f'<li><a href="{rel}{href_suffix}"{current}>{label}</a></li>'

    return f"""<body class="" data-level-code="{active_level_code or ''}">
    <a class="skip-link" href="#main-content">Aller au contenu</a>
    <header class="site-header">
        <div class="site-header__bar">
            <a class="brand" href="{rel}index.html">
                {BRAND_MARK_SVG}
                <span class="brand__text">
                    <span class="brand__name">Renan le Professeur</span>
                    <span class="brand__tagline">Académie de Français</span>
                </span>
            </a>
            <nav class="primary-nav" id="primary-nav" role="navigation" aria-label="Navigation principale">
                <ul class="primary-nav__list">
                {top("Accueil", "index.html", "home")}
                {top("Grammaire", "index.html#grammaire", "grammar")}
                <li class="nav-drop">
                    <button type="button" class="nav-drop__toggle" aria-haspopup="true" aria-expanded="false">
                        Niveaux <span class="nav-drop__caret" aria-hidden="true"></span>
                    </button>
                    <ul class="nav-drop__menu" role="menu">
                    {nav_levels_html(rel, active_level_code)}
                    </ul>
                </li>
                {top("Exercices", "exercises.html", "exercises")}
                {top("Examens Blancs", "simulated-exams.html", "exams")}
                {top("Extras", "extras.html", "extras")}
                {top("Dictionnaire", "dictionary.html", "dictionary")}
                </ul>
            </nav>
            <div class="nav-utility">
                <button type="button" class="theme-toggle" data-search-toggle aria-label="Rechercher sur le site" aria-haspopup="dialog">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                </button>
                <button type="button" class="theme-toggle" data-theme-toggle aria-label="Passer en mode sombre">
                    <svg class="icon-sun" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>
                    <svg class="icon-moon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M20 14.5A8.5 8.5 0 1 1 9.5 4a7 7 0 0 0 10.5 10.5Z"/></svg>
                </button>
                <button type="button" class="nav-toggle" data-nav-toggle aria-label="Ouvrir le menu" aria-expanded="false" aria-controls="primary-nav">
                    <span class="nav-toggle__icon"></span>
                </button>
            </div>
        </div>
    </header>
    <div class="search-overlay" data-search-overlay hidden>
        <div class="search-modal" role="dialog" aria-modal="true" aria-label="Recherche sur le site" data-index-src="{rel}assets/data/search-index.json">
            <div class="search-modal__bar">
                <svg class="search-modal__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                <input type="search" class="search-modal__input" data-search-input placeholder="Cherche une leçon, un point de grammaire, du vocabulaire, un exercice&hellip;" aria-label="Rechercher">
                <button type="button" class="search-modal__close" data-search-close aria-label="Fermer la recherche"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="M6 6l12 12"/></svg></button>
            </div>
            <div class="search-modal__results" data-search-results>
                <p class="search-modal__hint">Tape au moins 2 caractères pour chercher dans tous les niveaux, leçons, points de grammaire et exercices.</p>
            </div>
        </div>
    </div>
    {breadcrumb}
    <main id="main-content" class="site-main">"""


def footer(rel, extra_scripts=None):
    extra = "".join(f'<script src="{rel}assets/js/{s}"></script>' for s in (extra_scripts or []))
    ai_teacher_widget = f"""<button type="button" class="ai-teacher-toggle" data-ai-teacher-toggle aria-label="Poser une question au Professeur IA" aria-expanded="false" aria-haspopup="dialog">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 10-10-5L2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.5 2.5 3 6 3s6-1.5 6-3v-5"/><path d="M22 10v6"/></svg>
        <span class="ai-teacher-toggle__label">Professeur IA</span>
    </button>
    <div class="ai-teacher-panel" data-ai-teacher-panel hidden role="dialog" aria-label="Chat avec le Professeur IA de Français" aria-modal="false">
        <div class="ai-teacher-panel__bar">
            <div class="ai-teacher-panel__brand">
                <svg class="ai-teacher-panel__brand-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 10-10-5L2 10l10 5 10-5Z"/><path d="M6 12v5c0 1.5 2.5 3 6 3s6-1.5 6-3v-5"/><path d="M22 10v6"/></svg>
                <div>
                    <strong>Professeur IA de Français</strong>
                    <span>Pose une question sur la grammaire, le vocabulaire ou les exercices</span>
                </div>
            </div>
            <button type="button" class="ai-teacher-panel__close" data-ai-teacher-close aria-label="Fermer le Professeur IA"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="M6 6l12 12"/></svg></button>
        </div>
        <div class="ai-teacher-panel__messages" data-ai-teacher-messages role="log" aria-live="polite">
            <div class="ai-teacher-msg ai-teacher-msg--bot">
                <p>Bonjour ! Je peux t'aider avec le français. Pose-moi une question sur la grammaire, le vocabulaire ou les exercices.<br>Par exemple : <em>&laquo; Explique-moi le passé composé &raquo;</em> ou <em>&laquo; Donne-moi un exercice sur le subjonctif. &raquo;</em></p>
            </div>
        </div>
        <form class="ai-teacher-panel__form" data-ai-teacher-form>
            <label for="ai-teacher-input" class="visually-hidden">Ta question</label>
            <textarea id="ai-teacher-input" data-ai-teacher-input rows="1" maxlength="600" placeholder="Écris ta question&hellip;" required></textarea>
            <button type="submit" class="ai-teacher-panel__send" data-ai-teacher-send aria-label="Envoyer la question"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m22 2-7 20-4-9-9-4Z"/><path d="M22 2 11 13"/></svg></button>
        </form>
        <p class="ai-teacher-panel__hint" data-ai-teacher-hint>Les réponses viennent d'un modèle d'IA et peuvent parfois se tromper &mdash; compare-les toujours avec le contenu de ta leçon. Rien de ce que tu écris n'est conservé à la fermeture de cette fenêtre.</p>
    </div>
    <script src="{rel}assets/js/ai-teacher.js" data-ai-endpoint="{AI_TEACHER_WORKER_URL}"></script>""" if AI_TEACHER_ENABLED else ""
    return f"""<button type="button" class="dict-widget-toggle" data-dict-widget-toggle aria-label="Ouvrir le dictionnaire rapide" aria-expanded="false" aria-haspopup="dialog">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/></svg>
    </button>
    <div class="dict-widget-panel" data-dict-widget-panel hidden>
        <div class="dict-widget__bar">
            <input type="text" data-dict-widget-input placeholder="Cherche un mot français…" aria-label="Chercher un mot français">
            <button type="button" class="dict-widget__close" data-dict-widget-close aria-label="Fermer le dictionnaire"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M18 6 6 18"/><path d="M6 6l12 12"/></svg></button>
        </div>
        <div class="dict-widget__result" data-dict-widget-result>
            <p class="dict-widget__hint">Écris un mot pour voir sa signification sans quitter cette page.</p>
        </div>
        <div class="dict-widget__links" data-dict-widget-links></div>
    </div>
    </main>
    <footer class="site-footer">
        <div class="site-footer__inner">
            <div>
                <a class="brand" href="{rel}index.html">
                    {BRAND_MARK_SVG}
                    <span class="brand__text">
                        <span class="brand__name">Renan le Professeur</span>
                        <span class="brand__tagline">Académie de Français</span>
                    </span>
                </a>
                <p class="site-footer__blurb">Un cours de français aligné sur le CECR, construit leçon par leçon, relu avec soin et honnêteté &mdash; depuis ton premier &laquo; bonjour &raquo; jusqu'à une vraie aisance.</p>
            </div>
            <div class="footer-col">
                <h4>Niveaux</h4>
                <ul>
                    <li><a href="{rel}levels/pre-a1.html">Pre-A1 &mdash; Survie</a></li>
                    <li><a href="{rel}levels/a1.html">A1 &mdash; Débutant</a></li>
                    <li><a href="{rel}levels/a2.html">A2 &mdash; Élémentaire</a></li>
                    <li><a href="{rel}levels/b1.html">B1 &mdash; Intermédiaire</a></li>
                    <li><a href="{rel}levels/b2.html">B2 &mdash; Intermédiaire avancé</a></li>
                    <li><a href="{rel}levels/c1.html">C1 &mdash; Avancé</a></li>
                    <li><a href="{rel}levels/c2.html">C2 &mdash; Maîtrise</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Pratique</h4>
                <ul>
                    <li><a href="{rel}index.html#grammaire">Feuille de Route de Grammaire</a></li>
                    <li><a href="{rel}exercises.html">Lecture et Exercices</a></li>
                    <li><a href="{rel}simulated-exams.html">Examens Blancs</a></li>
                    <li><a href="{rel}dictionary.html">Dictionnaire et Référence</a></li>
                    <li><a href="{rel}irregular-verbs.html">Verbes Irréguliers</a></li>
                    <li><a href="{rel}extras.html">Extras</a></li>
                </ul>
            </div>
            <div class="footer-col">
                <h4>Ta Progression</h4>
                <ul>
                    <li><a href="{rel}placement-test.html">Test de Niveau</a></li>
                    <li><a href="{rel}progress.html">Ma Progression</a></li>
                    <li><a href="{rel}today-review.html">Révision du Jour</a></li>
                    <li><a href="{rel}index.html#a-propos-cecr">Qu'est-ce que le CECR ?</a></li>
                </ul>
            </div>
        </div>
        <div class="site-footer__bottom">
            <p>&copy; 2026 Renan le Professeur &mdash; Cours de Français. Tous droits réservés.</p>
        </div>
    </footer>
    <button type="button" class="back-to-top back-to-top--with-dict" data-back-to-top aria-label="Retour en haut">
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5"/><path d="m5 12 7-7 7 7"/></svg>
    </button>
    {ai_teacher_widget}
    <script src="{rel}assets/js/main.js"></script>
    <script src="{rel}assets/js/search.js"></script>
    <script src="{rel}assets/js/dict-widget.js"></script>
    <script src="{rel}assets/js/progress.js"></script>{extra}
</body>
</html>
"""
