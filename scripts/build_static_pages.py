#!/usr/bin/env python3
"""
Construit chaque page indépendante de premier niveau : index.html,
exercises.html, extras.html, dictionary.html, irregular-verbs.html,
placement-test.html, progress.html, today-review.html,
simulated-exams.html.

Usage :
    python3 scripts/build_static_pages.py
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = ""

STAR = site_chrome.STAR
STARS_ROW = site_chrome.STARS_ROW
ARROW = site_chrome.ARROW_SVG
CHECK = site_chrome.CHECK_SVG


def ex_block(data):
    return f'<div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(data, ensure_ascii=False)}</script></div>'


def page_header(eyebrow, h1, lede):
    return f"""<div class="page-header">
        {STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">{eyebrow}</p>
                <h1>{h1}</h1>
                <p class="page-header__lede">{lede}</p>
            </div>
        </div>
    </div>"""


def write_page(path, title, description, body_sections, active_top=None, breadcrumb_label=None,
                extra_css=None, extra_scripts=None):
    breadcrumb = None
    if breadcrumb_label:
        breadcrumb = f'<li><a href="{REL}index.html">Accueil</a></li><li aria-current="page">{breadcrumb_label}</li>'
    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=extra_css))
    out.append(site_chrome.header(REL, None, breadcrumb, active_top=active_top))
    out.extend(body_sections)
    out.append(site_chrome.footer(REL, extra_scripts=extra_scripts))
    (REPO_ROOT / path).write_text("\n".join(out), encoding="utf-8")
    print(f"Built {path}")


# =======================================================================
# INDEX
# =======================================================================
def build_index():
    hero = f"""<section class="hero" id="mission">
        <div class="hero__inner">
            {STARS_ROW}
            <div class="hero__split">
                <div>
                    <p class="eyebrow hero__eyebrow">Bienvenue</p>
                    <h1>Bienvenue à l'Académie de Renan le Professeur</h1>
                    <p class="hero__lede">Un cours de français aligné sur le CECR, avec grammaire, vocabulaire et exercices — immersion totale : explications en français, exemples en français réel.<br>Commençons !</p>
                    <div class="hero__actions">
                        <a class="btn btn--accent" href="levels/pre-a1.html">Commence avec Pre-A1 {ARROW}</a>
                        <a class="btn btn--ghost-inverse" href="placement-test.html">Quel est mon niveau ?</a>
                    </div>
                </div>
            </div>
        </div>
    </section>
    <hr class="rule">"""

    level_grammar = {
        "Pre-A1": ["Alphabet et sons", "Salutations et présentations", "Nombres et l'heure", "Verbes de base"],
        "A1": ["Être &amp; avoir", "Genre &amp; articles", "Présent régulier et irrégulier", "Les verbes pronominaux"],
        "A2": ["Passé composé &amp; imparfait", "Verbes pronominaux", "Pronoms compléments", "L'impératif"],
        "B1": ["Présent du subjonctif", "Pronoms combinés", "Futur &amp; conditionnel", "Le discours indirect"],
        "B2": ["Subjonctif passé", "Conditionnelles avec si", "Voix passive", "Registre formel/informel"],
        "C1": ["Subjonctif plus-que-parfait", "Conditionnelles complexes", "Registre académique", "Variation dialectale"],
        "C2": ["Syntaxe complexe", "Registre littéraire", "Nuances lexicales", "Variation régionale"],
    }
    cards = []
    romans = ["I", "II", "III", "IV", "V", "VI", "VII"]
    for i, (code, topics) in enumerate(level_grammar.items()):
        roman = romans[i]
        items = "".join(f"<li>{t}</li>" for t in topics)
        level_name = {c: n for c, n, s in site_chrome.LEVELS}[code]
        cards.append(f"""<article class="lesson-card">
            <span class="lesson-card__index" aria-hidden="true">{roman}</span>
            <h3>{code} — {level_name}</h3>
            <ul style="color:var(--color-text-muted);font-size:var(--step--1);padding-left:1.1em;list-style:disc;display:flex;flex-direction:column;gap:0.25em;">{items}</ul>
            <div class="lesson-card__actions"><a class="btn btn--ghost btn--small" href="levels/{code.lower()}.html">Ouvrir {code} {ARROW}</a></div>
        </article>""")

    grammar_section = f"""<section id="grammaire" class="section section--surface" aria-labelledby="grammaire-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Grammaire</p>
                <h2 id="grammaire-heading">La feuille de route de grammaire française</h2>
                <p>Un parcours complet de la grammaire française à travers sept niveaux du CECR, de ton premier être et avoir jusqu'au registre littéraire — ouvre n'importe quel niveau pour voir tous les sujets et commencer à pratiquer.</p>
            </div>
            <div class="grid">{"".join(cards)}</div>
        </div>
    </section>"""

    ladder_items = []
    ladder_desc = {
        "Pre-A1": "Premier contact avec la langue : alphabet, sons et phrases minimales pour survivre en français.",
        "A1": "Phrases de base et expressions quotidiennes pour des besoins immédiats.",
        "A2": "Échanges simples et directs sur des sujets familiers et des questions routinières.",
        "B1": "Usage autonome du français pour le travail, les études et les voyages.",
        "B2": "Interaction fluide et spontanée, avec des arguments clairs et détaillés.",
        "C1": "Usage flexible et efficace de la langue pour la vie académique et professionnelle.",
        "C2": "Maîtrise précise et nuancée du français dans pratiquement n'importe quel contexte.",
    }
    for code, name, slug in site_chrome.LEVELS:
        code_cls = "ladder__code ladder__code--compact" if len(code) > 2 else "ladder__code"
        ladder_items.append(f"""<li class="ladder__rung">
            <span class="{code_cls}" aria-hidden="true">{code}</span>
            <div class="ladder__body">
                <h3>{name}</h3>
                <p>{ladder_desc[code]} <a class="ladder__link" href="levels/{slug}.html">Entre dans le niveau {ARROW}</a></p>
            </div>
        </li>""")

    cefr_section = f"""<section id="a-propos-cecr" class="section section--surface" aria-labelledby="cecr-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Le Cadre et Ton Parcours à Travers Lui</p>
                <h2 id="cecr-heading">À Propos du CECR</h2>
                <p>Le <strong>Cadre Européen Commun de Référence pour les Langues (CECR)</strong> est la norme internationale pour décrire le niveau de maîtrise d'une langue. Il organise ce cours en sept niveaux — entre dans n'importe lequel d'entre eux ci-dessous.</p>
            </div>
            <ol class="ladder">{"".join(ladder_items)}</ol>
        </div>
    </section>"""

    skills = [
        ("Grammaire", "index.html#grammaire", "M3 8 4 8v13a1 1 0 0 0 1 1h6", "Temps, formes et règles structurées, organisées par niveau du CECR et reliées à des exercices de pratique.", '<path d="M3 5.5C3 4.7 3.7 4 4.5 4H10a2 2 0 0 1 2 2v14a1.5 1.5 0 0 0-1.5-1.5H4.5A1.5 1.5 0 0 1 3 17V5.5Z"/><path d="M21 5.5c0-.8-.7-1.5-1.5-1.5H14a2 2 0 0 0-2 2v14a1.5 1.5 0 0 1 1.5-1.5h5.5a1.5 1.5 0 0 0 1.5-1.5V5.5Z"/>'),
        ("Vocabulaire", None, None, "Des listes de mots par thème qui grandissent avec la grammaire de chaque niveau, des premiers noms aux collocations plus précises.", '<path d="M4 19V6.5A2.5 2.5 0 0 1 6.5 4H8"/><path d="M4 13h4"/><path d="M14 19V6.5A2.5 2.5 0 0 1 16.5 4H20"/><path d="M14 13h4"/>'),
        ("Exercices", "exercises.html", None, "Pratique supplémentaire de lecture et de vocabulaire, indépendante du niveau, pour n'importe quel moment.", '<path d="M12 20h9"/><path d="M16.5 3.5a2.1 2.1 0 0 1 3 3L7 19l-4 1 1-4Z"/>'),
        ("Lecture", "exercises.html", None, "Des textes et dialogues de style authentique en français qui mettent en jeu la grammaire et le vocabulaire en contexte.", '<path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"/><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2Z"/>'),
        ("Écoute", "exercises.html", None, "Des transcriptions de dialogues et de monologues pour entraîner l'oreille au français parlé de façon naturelle.", '<path d="M3 18v-6a9 9 0 0 1 18 0v6"/><path d="M21 19a2 2 0 0 1-2 2h-1a2 2 0 0 1-2-2v-3a2 2 0 0 1 2-2h3Z"/><path d="M3 19a2 2 0 0 0 2 2h1a2 2 0 0 0 2-2v-3a2 2 0 0 0-2-2H3Z"/>'),
        ("Écriture", None, None, "Des activités d'écriture guidée qui grandissent, de phrases isolées à des paragraphes argumentatifs bien structurés.", '<path d="M2 22c4-1 8-3 10-5"/><path d="M22 2c-8 0-16 4-16 14 0 2 2 4 4 4C20 20 22 10 22 2Z"/>'),
        ("Conversation", None, None, "Des sujets de conversation pour pratiquer et débattre à chaque niveau.", '<path d="M12 15a3 3 0 0 0 3-3V6a3 3 0 0 0-6 0v6a3 3 0 0 0 3 3Z"/><path d="M19 11a7 7 0 0 1-14 0"/><path d="M12 18v3"/><path d="M9 21h6"/>'),
        ("Examens Blancs", "simulated-exams.html", None, "Des sections d'examen blanc dans le style DELF/DALF, avec corrigés, pour préparer la certification.", '<circle cx="12" cy="15" r="6"/><path d="m9 10-3-7"/><path d="m15 10 3-7"/><path d="M9.5 15.5 12 17l2.5-1.5"/>'),
    ]
    skill_cards = []
    for name, href, _, desc, icon in skills:
        tag_open = f'<a class="skill-card" href="{href}">' if href else '<div class="skill-card">'
        tag_close = "</a>" if href else "</div>"
        skill_cards.append(f'{tag_open}<svg class="skill-card__icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{icon}</svg><h3>{name}</h3><p>{desc}</p>{tag_close}')

    skills_section = f"""<section id="skills" class="section" aria-labelledby="skills-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Un Curriculum Complet</p>
                <h2 id="skills-heading">Toutes les compétences, couvertes</h2>
                <p>Chaque niveau du CECR travaille les mêmes compétences clés, pour ne rien laisser au hasard.</p>
            </div>
            <div class="grid grid--4">{"".join(skill_cards)}</div>
        </div>
    </section>"""

    why_section = f"""<section id="why-us" class="section section--surface" aria-labelledby="why-heading">
        <div class="section__inner">
            <div class="section__head section__head--center">
                <p class="eyebrow">Pourquoi Apprendre avec Nous</p>
                <h2 id="why-heading">Un cours conçu pour donner confiance</h2>
            </div>
            <div class="grid grid--3" style="max-width:70rem;margin:0 auto;">
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="m15 9-2 6-6 2 2-6 6-2Z"/></svg></span>
                    <h3>Organisé selon le CECR</h3>
                    <p>Chaque leçon est reliée au Cadre Européen Commun, donc tu sais toujours exactement où tu en es et ce qui vient ensuite.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 3"/></svg></span>
                    <h3>Apprends à ton propre rythme</h3>
                    <p>Avance niveau par niveau ou va directement aux exercices, au dictionnaire ou à la révision du jour quand tu as besoin de pratique supplémentaire.</p>
                </div>
                <div class="card card--feature">
                    <span class="card__icon"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="12" r="9"/><path d="M3 12h18"/><path d="M12 3c2.5 2.5 4 5.7 4 9s-1.5 6.5-4 9c-2.5-2.5-4-5.7-4-9s1.5-6.5 4-9Z"/></svg></span>
                    <h3>Basé sur du français réel</h3>
                    <p>Des exemples et des dialogues naturels, pas du remplissage artificiel de manuel — et chaque point de grammaire vient avec les erreurs courantes à éviter.</p>
                </div>
            </div>
        </div>
    </section>"""

    cta = f"""<section class="cta-band" aria-labelledby="cta-heading">
        {STARS_ROW}
        <p class="eyebrow" style="justify-content:center;">Commence quand tu veux</p>
        <h2 id="cta-heading">Profite du chemin — commence aujourd'hui à ton niveau.</h2>
        <p>Tu ne sais pas par où commencer ? Fais le test de niveau, ou commence simplement à Pre-A1 et avance pas à pas.</p>
        <div class="hero__actions">
            <a class="btn btn--accent" href="levels/pre-a1.html">Explore tous les niveaux {ARROW}</a>
            <a class="btn btn--ghost-inverse" href="placement-test.html">Quel est mon niveau ?</a>
        </div>
    </section>"""

    write_page(
        "index.html",
        "Renan le Professeur — Académie de Français",
        "Un cours de français aligné sur le CECR avec grammaire, vocabulaire, lecture, écoute, écriture, conversation et examens blancs, organisé niveau par niveau de Pre-A1 à C2.",
        [hero, grammar_section, cefr_section, skills_section, why_section, cta],
        active_top="home",
        extra_scripts=[],
    )


# =======================================================================
# EXERCISES
# =======================================================================
def build_exercises():
    header = page_header("Pratique Indépendante", "Exercices",
                          "Pratique supplémentaire de lecture et de vocabulaire, indépendante du niveau — viens quand tu veux.")

    items = [
        ("Pre-A1", "Un Message Texte", "<p>Salut, c'est Pierre. Je suis rue Mayor, près de la banque. Où es-tu, toi ? Moi, j'ai faim, on mange quelque chose ? Il y a un très bon restaurant ici. Je t'attends à deux heures.</p>",
         {"id": "ex-pa1-message", "type": "true-false", "title": "Vérification de Compréhension", "items": [
            {"id": "expa1a", "statement": "Pierre est près de la banque.", "answer": True, "explanation": "Le texte dit : « Je suis rue Mayor, près de la banque »."},
            {"id": "expa1b", "statement": "Pierre n'a pas faim.", "answer": False, "explanation": "Le texte dit : « j'ai faim »."},
            {"id": "expa1c", "statement": "Pierre attend l'autre personne à deux heures.", "answer": True, "explanation": "Le texte dit : « Je t'attends à deux heures »."},
         ]}),
        ("Pre-A1", "À la Cafétéria de l'Université", "<p>—Salut, qu'est-ce que tu veux boire ?<br>—Un café, s'il te plaît. Et toi ?<br>—Moi, je veux un thé au lait.<br>—Parfait, ça fait trois euros en tout.</p>",
         {"id": "ex-pa1-cafeteria", "type": "multiple-choice", "title": "Vérification de Compréhension", "items": [
            {"id": "expa1d", "prompt": "Que demande la première personne ?", "options": ["Un thé", "Un café", "Un jus"], "answerIndex": 1, "explanation": "Le texte dit : « Un café, s'il te plaît »."},
            {"id": "expa1e", "prompt": "Combien ça coûte en tout ?", "options": ["Deux euros", "Trois euros", "Quatre euros"], "answerIndex": 1, "explanation": "Le texte dit : « ça fait trois euros en tout »."},
         ]}),
        ("Pre-A1", "Numéros de Téléphone", "<p>—Quel est ton numéro de téléphone ?<br>—C'est le zéro, six, deux, quatre, huit, un, cinq, zéro, trois.<br>—Tu peux répéter, s'il te plaît ?<br>—Bien sûr : zéro, six, deux, quatre, huit, un, cinq, zéro, trois.</p>",
         {"id": "ex-pa1-telephone", "type": "true-false", "title": "Vérification de Compréhension", "items": [
            {"id": "expa1f1", "statement": "La personne répète le numéro deux fois.", "answer": True, "explanation": "Le texte montre le numéro dit, puis répété après la demande."},
            {"id": "expa1f2", "statement": "Le numéro commence par sept.", "answer": False, "explanation": "Le numéro commence par zéro."},
         ]}),
        ("Pre-A1", "À la Pharmacie", "<p>—Bonjour, j'ai besoin de quelque chose pour le mal de tête.<br>—Nous avons ces comprimés. Une allergie ?<br>—Non, aucune.<br>—Parfait, ça fait cinq euros.</p>",
         {"id": "ex-pa1-pharmacie", "type": "multiple-choice", "title": "Vérification de Compréhension", "items": [
            {"id": "expa1g1", "prompt": "De quoi la personne a-t-elle besoin ?", "options": ["De quelque chose pour dormir", "De quelque chose pour le mal de tête", "De vitamines"], "answerIndex": 1, "explanation": "Le texte dit : « j'ai besoin de quelque chose pour le mal de tête »."},
            {"id": "expa1g2", "prompt": "A-t-elle une allergie ?", "options": ["Oui", "Non"], "answerIndex": 1, "explanation": "Le texte dit : « Non, aucune »."},
         ]}),
    ]
    sections = [header]
    for level, title, passage, ex in items:
        sections.append(f"""<section class="section section--surface" aria-labelledby="ex-{ex['id']}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level}</p>
                <h2 id="ex-{ex['id']}-heading">{title}</h2>
                <div class="card"><div class="prose">{passage}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(ex)}</div>
            </div>
        </section>""")

    sections.append(f"""<section class="section section--tight" aria-labelledby="ex-more-heading">
        <div class="section__inner">
            <h2 id="ex-more-heading" class="visually-hidden">Plus à venir</h2>
            <p style="max-width:56ch;color:var(--color-text-muted);">D'autres textes de lecture, pour A1 et au-delà, arrivent au fur et à mesure que ces niveaux sont publiés. En attendant, retrouve tout le contenu déjà disponible sur la page <a href="levels/pre-a1.html">Pre-A1</a>.</p>
        </div>
    </section>""")

    write_page("exercises.html", "Exercices — Renan le Professeur · Cours de Français",
               "Pratique supplémentaire de lecture et de vocabulaire en français, indépendante du niveau, avec retour instantané.",
               sections, active_top="exercises", breadcrumb_label="Exercices",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


# =======================================================================
# EXTRAS
# =======================================================================
def build_extras():
    header = page_header("Au-delà de la Grammaire", "Extras",
                          "Expressions courantes, tu face à vous, situations quotidiennes, et courtes notes culturelles.")

    expressions = [
        ("D'accord !", "Entendu, c'est bon.", "Utilisé très fréquemment pour accepter quelque chose ou confirmer un plan."),
        ("N'importe quoi !", "Pas du tout ! / Tu dis n'importe quoi !", "Pour nier avec insistance quelque chose que quelqu'un vient de dire."),
        ("Aucune idée", "Je ne sais pas du tout.", "Réponse informelle, très courante entre amis."),
        ("Allez !", "Vas-y ! / Motive-toi !", "Encouragement ou invitation à agir, très utilisé en français parlé."),
        ("Pourvu que...", "J'espère bien, de tout cœur !", "Exprime un souhait intense, souvent suivi du subjonctif."),
        ("Ce n'est pas grave", "Il n'y a pas de problème, ne t'inquiète pas.", "Pour minimiser une erreur ou une excuse."),
        ("C'est trop cool !", "C'est génial !", "Familier et très courant ; au Québec on dit souvent « c'est le fun »."),
        ("Dis donc !", "Eh bien ! (expression de surprise)", "Marque la surprise ou attire l'attention ; s'utilise même en contexte assez informel."),
        ("Ça alors !", "Eh bien ! / Sans blague !", "Surprise ou incrédulité ; encourage aussi parfois quelqu'un à agir."),
        ("Être dans la lune", "Être distrait, ne pas faire attention.", "Expression imagée très courante dans toute situation informelle."),
    ]
    exp_rows = "".join(f"<tr><td><strong>{it}</strong></td><td>{sig}</td><td>{note}</td></tr>" for it, sig, note in expressions)

    expressions_section = f"""<section id="expressions" class="section section--surface" aria-labelledby="expr-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Sonne Plus Naturel</p>
                <h2 id="expr-heading">Expressions Courantes</h2>
                <p>Des phrases brèves et très fréquentes qui font sonner ton français de façon naturelle, pas comme un manuel.</p>
            </div>
            <div class="table-scroll"><table class="ref-table"><thead><tr><th>Expression</th><th>Signification</th><th>Note</th></tr></thead><tbody>{exp_rows}</tbody></table></div>
        </div>
    </section>"""

    formal_informal = f"""<section id="formal-informal" class="section section--tight" aria-labelledby="fi-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Registre</p>
                <h2 id="fi-heading">Tu, Vous… et les Nuances Régionales</h2>
                <p>Choisir tu ou vous n'est que le début — et l'usage varie aussi d'une région francophone à l'autre.</p>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>Informel (tu)</h3>
                    <ul class="rules-list">
                        <li>Salut, comment ça va ?</li>
                        <li>Excuse-moi, tu as une minute ?</li>
                        <li>Tu peux m'aider ?</li>
                        <li>Je voulais te demander quelque chose.</li>
                        <li>À bientôt ! / On se voit !</li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Formel (vous)</h3>
                    <ul class="rules-list">
                        <li>Bonjour, comment allez-vous ?</li>
                        <li>Excusez-moi, auriez-vous une minute ?</li>
                        <li>Pourriez-vous m'aider ?</li>
                        <li>Je voulais vous demander quelque chose.</li>
                        <li>Cordialement / Au revoir</li>
                    </ul>
                </div>
                <div class="card">
                    <h3>Variation régionale (Québec, Belgique, Suisse…)</h3>
                    <ul class="rules-list">
                        <li>Au Québec, on tutoie souvent plus vite, même avec un commerçant.</li>
                        <li>En Belgique et en Suisse, on entend septante (70) et nonante (90) au lieu de soixante-dix et quatre-vingt-dix.</li>
                        <li>En Afrique francophone, le vouvoiement reste très courant même en famille.</li>
                    </ul>
                </div>
            </div>
            <div class="notice mt-lg"><strong>Règle générale</strong><p>Utilise vous avec des inconnus, des personnes plus âgées, des autorités et dans tout contexte professionnel — jusqu'à ce qu'on t'invite à tutoyer. La frontière entre tu et vous varie aussi selon les générations et les régions francophones, alors observe et adapte-toi au contexte.</p></div>
        </div>
    </section>"""

    everyday = f"""<section id="everyday" class="section section--surface" aria-labelledby="everyday-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Situations Réelles</p>
                <h2 id="everyday-heading">Le Français de Tous les Jours</h2>
                <p>Des échanges brefs et pratiques pour des situations que tu vas vraiment rencontrer.</p>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>Dans un café</h3>
                    <p><em>Un café au lait, s'il vous plaît.</em></p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">En France, on s'assoit et le serveur prend la commande à table ; le service est généralement compris dans le prix.</p>
                </div>
                <div class="card">
                    <h3>Au marché</h3>
                    <p><em>Combien coûtent ces pommes ?</em></p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">Marchander est peu courant sur les marchés français, contrairement à d'autres régions du monde francophone.</p>
                </div>
                <div class="card">
                    <h3>Petite conversation</h3>
                    <p><em>Il fait chaud/froid aujourd'hui, non ?</em></p>
                    <p style="color:var(--color-text-muted);font-size:var(--step--1);">La météo est un sujet sûr et universel pour briser la glace, comme dans beaucoup d'autres langues.</p>
                </div>
            </div>
        </div>
    </section>"""

    culture = f"""<section id="culture" class="section section--tight" aria-labelledby="culture-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Notes Culturelles</p>
                <h2 id="culture-heading">Le Monde Francophone en Bref</h2>
            </div>
            <div class="grid grid--3">
                <div class="card">
                    <h3>Horaires des repas</h3>
                    <p>En France, on déjeune généralement entre midi et 14h et on dîne vers 19h30-20h30 ; au Québec, les repas sont souvent plus tôt, avec un souper dès 18h.</p>
                </div>
                <div class="card">
                    <h3>La bise</h3>
                    <p>Se faire la bise (s'embrasser sur les joues) est une salutation courante entre amis et famille en France, avec un nombre de bises qui varie selon la région — mieux vaut se laisser guider la première fois.</p>
                </div>
                <div class="card">
                    <h3>Une langue, plusieurs accents</h3>
                    <p>Le français est langue officielle dans une trentaine de pays, de la France au Québec, en passant par la Belgique, la Suisse et une grande partie de l'Afrique — chaque région a son propre vocabulaire, son intonation et ses expressions, et aucune variante n'est « plus correcte » qu'une autre.</p>
                </div>
            </div>
        </div>
    </section>"""

    write_page("extras.html", "Extras — Renan le Professeur · Cours de Français",
               "Expressions courantes, tu/vous, situations quotidiennes et courtes notes culturelles du monde francophone.",
               [header, expressions_section, formal_informal, everyday, culture],
               active_top="extras", breadcrumb_label="Extras", extra_css=["lessons"])


# =======================================================================
# DICTIONARY
# =======================================================================
def dict_card(name, desc, url_tmpl, sample_word, featured=True):
    cls = "card card--feature dict-card" if featured else "card dict-card"
    btn_cls = "btn btn--accent btn--small dict-card__link" if featured else "btn btn--accent btn--small dict-card__link"
    sample_url = url_tmpl.replace("{word}", sample_word)
    return f"""<div class="{cls}" data-url-template="{url_tmpl}">
        <h3>{name}</h3>
        <p>{desc}</p>
        <div class="card__foot">
            <a class="{btn_cls}" data-dict-link href="{sample_url}" target="_blank" rel="noopener"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M5 12h14"/><path d="m13 6 6 6-6 6"/></svg>Chercher</a>
        </div>
    </div>"""


def build_dictionary():
    header = page_header("Dictionnaire et Référence", "Cherche N'importe Quel Mot Français",
                          "Écris un mot une seule fois et ouvre-le directement dans n'importe lequel de ces dictionnaires en français, ou utilise les outils de prononciation ci-dessous.")

    input_section = f"""<section class="section section--surface" aria-labelledby="primary-dict-heading">
        <div class="section__inner">
            <h2 id="primary-dict-heading" class="visually-hidden">Dictionnaires Principaux</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-lg);">
                <label for="dict-word" class="eyebrow" style="margin-bottom:0.6em;display:block;">Ton mot</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="dict-word" class="dict-input" placeholder="Écris un mot, p. ex. « pourvu »" autocomplete="off" data-dict-word>
                </div>
                <p class="notice mt-lg"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Chaque carte ci-dessous se met à jour pendant que tu écris. Appuie sur Entrée pour aller directement vers l'un des quatre dictionnaires principaux, au hasard.</p>
            </div>
            <div class="grid">
                {dict_card("Larousse", "Le dictionnaire de référence de la langue française : définitions, grammaire, conjugaison et exemples d'usage.", "https://www.larousse.fr/dictionnaires/francais/{word}", "pourvu")}
                {dict_card("Wiktionnaire en français", "Dictionnaire collaboratif avec étymologie, exemples et variantes régionales de milliers de mots.", "https://fr.wiktionary.org/wiki/{word}", "pourvu")}
                {dict_card("Dictionnaire de l'Académie française", "La référence officielle et normative de la langue française, tenue par l'Académie française.", "https://www.dictionnaire-academie.fr/article/{word}", "pourvu")}
                {dict_card("Synonymes et Antonymes", "Trouve des synonymes et des antonymes pour enrichir ton vocabulaire et éviter les répétitions.", "https://www.cnrtl.fr/synonymie/{word}", "pourvu")}
            </div>
        </div>
    </section>"""

    more_section = f"""<section class="section" aria-labelledby="more-dict-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">Si Tu As Besoin de Plus</p>
                <h2 id="more-dict-heading">Plus de Dictionnaires et de Prononciation</h2>
                <p>Pour un second avis, conjuguer un verbe, ou entendre comment un mot se prononce réellement.</p>
            </div>
            <div class="grid">
                {dict_card("Le Conjugueur", "Tableaux complets de conjugaison pour n'importe quel verbe français, à tous les temps et modes.", "https://leconjugueur.lefigaro.fr/conjugaison/verbe/{word}.html", "parler", featured=False)}
                {dict_card("Forvo", "Prononciations réelles enregistrées par des locuteurs natifs du français de différents pays.", "https://forvo.com/word/{word}/#fr", "pourvu", featured=False)}
            </div>
        </div>
    </section>"""

    write_page("dictionary.html", "Dictionnaire et Référence — Renan le Professeur · Cours de Français",
               "Cherche n'importe quel mot français dans Larousse, le Wiktionnaire, l'Académie française et plus, avec des outils de synonymes, conjugaison et prononciation.",
               [header, input_section, more_section],
               active_top="dictionary", breadcrumb_label="Dictionnaire et Référence",
               extra_scripts=["dictionary.js"])


# =======================================================================
# IRREGULAR VERBS
# =======================================================================
IRREGULAR_VERBS = [
    ("être", "exister, avoir une identité ou une qualité permanente", "je suis", "j'ai été", "radical totalement irrégulier"),
    ("avoir", "posséder quelque chose ou exprimer l'âge", "j'ai", "j'ai eu", "radical totalement irrégulier"),
    ("aller", "se déplacer d'un endroit à un autre", "je vais", "je suis allé(e)", "radical totalement irrégulier"),
    ("faire", "réaliser ou produire quelque chose", "je fais", "j'ai fait", "radical irrégulier"),
    ("dire", "communiquer quelque chose avec des mots", "je dis", "j'ai dit", "2e personne du pluriel irrégulière (vous dites)"),
    ("pouvoir", "avoir la capacité de faire quelque chose", "je peux", "j'ai pu", "radical totalement irrégulier"),
    ("vouloir", "désirer quelque chose", "je veux", "j'ai voulu", "radical totalement irrégulier"),
    ("savoir", "connaître un fait ou avoir une information", "je sais", "j'ai su", "radical totalement irrégulier"),
    ("venir", "se déplacer vers le lieu où est le locuteur", "je viens", "je suis venu(e)", "radical irrégulier au pluriel (nous venons)"),
    ("prendre", "saisir ou utiliser quelque chose", "je prends", "j'ai pris", "radical irrégulier au pluriel (nous prenons)"),
    ("voir", "percevoir quelque chose avec les yeux", "je vois", "j'ai vu", "radical irrégulier au pluriel (nous voyons)"),
    ("devoir", "avoir une obligation", "je dois", "j'ai dû", "radical totalement irrégulier"),
    ("mettre", "placer quelque chose quelque part", "je mets", "j'ai mis", "participe passé irrégulier"),
    ("partir", "quitter un lieu", "je pars", "je suis parti(e)", "radical qui perd sa consonne finale (je pars, nous partons)"),
    ("sortir", "aller vers l'extérieur", "je sors", "je suis sorti(e)", "radical qui perd sa consonne finale (je sors, nous sortons)"),
    ("tenir", "avoir quelque chose en main, garder", "je tiens", "j'ai tenu", "radical irrégulier au pluriel (nous tenons)"),
    ("connaître", "être familier avec une personne ou une chose", "je connais", "j'ai connu", "accent circonflexe devant t (il connaît)"),
    ("croire", "penser que quelque chose est vrai", "je crois", "j'ai cru", "radical irrégulier au pluriel (nous croyons)"),
    ("boire", "avaler un liquide", "je bois", "j'ai bu", "radical irrégulier au pluriel (nous buvons)"),
    ("écrire", "tracer des mots pour communiquer", "j'écris", "j'ai écrit", "radical irrégulier au pluriel (nous écrivons)"),
    ("lire", "déchiffrer un texte", "je lis", "j'ai lu", "radical irrégulier au pluriel (nous lisons)"),
    ("mourir", "cesser de vivre", "je meurs", "je suis mort(e)", "changement de radical + participe passé irrégulier"),
    ("naître", "venir au monde", "je nais", "je suis né(e)", "accent circonflexe devant t (il naît)"),
    ("ouvrir", "faire en sorte que quelque chose ne soit plus fermé", "j'ouvre", "j'ai ouvert", "conjugué comme un verbe en -er au présent"),
    ("courir", "se déplacer rapidement à pied", "je cours", "j'ai couru", "radical irrégulier au futur (je courrai)"),
    ("envoyer", "faire parvenir quelque chose à quelqu'un", "j'envoie", "j'ai envoyé", "radical irrégulier au futur (j'enverrai)"),
    ("recevoir", "obtenir quelque chose qu'on nous donne", "je reçois", "j'ai reçu", "cédille + radical irrégulier au pluriel"),
    ("rire", "exprimer la joie ou l'amusement", "je ris", "j'ai ri", "deux i de suite à l'imparfait (nous riions)"),
    ("vivre", "être en vie, exister", "je vis", "j'ai vécu", "participe passé très irrégulier (vécu)"),
    ("suivre", "aller derrière quelqu'un ou quelque chose", "je suis", "j'ai suivi", "identique à je suis (être) au présent — attention au contexte"),
    ("plaire", "être agréable à quelqu'un", "je plais", "j'ai plu", "accent circonflexe devant t (il plaît)"),
    ("falloir", "être nécessaire (verbe impersonnel)", "il faut", "il a fallu", "seulement à la 3e personne du singulier"),
    ("pleuvoir", "tomber de la pluie (verbe impersonnel)", "il pleut", "il a plu", "seulement à la 3e personne du singulier"),
    ("battre", "frapper à plusieurs reprises", "je bats", "j'ai battu", "un seul t au singulier (je bats, il bat)"),
    ("mettre", "placer, poser quelque chose", "je mets", "j'ai mis", "participe passé en -is"),
    ("peindre", "appliquer de la peinture, représenter en peinture", "je peins", "j'ai peint", "radical en -ign au pluriel (nous peignons)"),
    ("craindre", "avoir peur de quelque chose", "je crains", "j'ai craint", "radical en -ign au pluriel (nous craignons)"),
    ("vaincre", "l'emporter sur quelqu'un", "je vaincs", "j'ai vaincu", "pas de t à la 3e personne (il vainc)"),
    ("conduire", "guider un véhicule", "je conduis", "j'ai conduit", "radical irrégulier au pluriel (nous conduisons)"),
    ("construire", "bâtir ou fabriquer quelque chose", "je construis", "j'ai construit", "radical irrégulier au pluriel (nous construisons)"),
    ("rendre", "redonner quelque chose", "je rends", "j'ai rendu", "conjugaison régulière en -re"),
    ("descendre", "aller vers le bas", "je descends", "je suis descendu(e)", "conjugaison régulière en -re"),
    ("acquérir", "obtenir quelque chose, souvent avec effort", "j'acquiers", "j'ai acquis", "radical très irrégulier"),
    ("cueillir", "récolter, ramasser", "je cueille", "j'ai cueilli", "conjugué comme un verbe en -er au présent"),
]


def build_irregular_verbs():
    header = page_header("Référence", "Verbes Irréguliers du Français",
                          "Les verbes irréguliers les plus courants, avec leur présent (je), passé composé (je) et type d'irrégularité — écris pour filtrer.")

    rows = "".join(
        f"<tr><td><strong>{inf}</strong></td><td>{meaning}</td><td>{pres}</td><td>{pret}</td><td class=\"text-muted\">{tipo}</td></tr>"
        for inf, meaning, pres, pret, tipo in IRREGULAR_VERBS
    )

    section = f"""<section class="section section--surface" aria-labelledby="verbs-heading">
        <div class="section__inner">
            <h2 id="verbs-heading" class="visually-hidden">Verbes Irréguliers</h2>
            <div class="section__inner--narrow" style="margin-bottom:var(--space-md);">
                <label for="verb-filter" class="eyebrow" style="margin-bottom:0.6em;display:block;">Filtrer</label>
                <div class="dict-input-row">
                    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/></svg>
                    <input type="text" id="verb-filter" class="dict-input" placeholder="Écris pour filtrer, p. ex. « avoir » ou « être »" autocomplete="off" data-verb-filter>
                </div>
                <p class="notice mt-lg" data-verb-count><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 3v4M12 17v4M3 12h4M17 12h4M6 6l2.5 2.5M15.5 15.5 18 18M6 18l2.5-2.5M15.5 8.5 18 6"/></svg>Affichage des {len(IRREGULAR_VERBS)} verbes.</p>
                <p class="notice mt-lg" data-verb-empty hidden>Aucun verbe trouvé correspondant à « <span data-verb-empty-term></span> ».</p>
            </div>
            <div class="table-scroll">
                <table class="ref-table">
                    <caption>Verbes irréguliers courants du français</caption>
                    <thead><tr><th>Infinitif</th><th>Définition</th><th>Présent (je)</th><th>Passé composé (je)</th><th>Type d'Irrégularité</th></tr></thead>
                    <tbody data-verb-tbody>{rows}</tbody>
                </table>
            </div>
        </div>
    </section>"""

    write_page("irregular-verbs.html", "Verbes Irréguliers du Français — Renan le Professeur · Cours de Français",
               "Tableau de référence des verbes irréguliers les plus courants du français : présent, passé composé et type d'irrégularité, avec filtre en direct.",
               [header, section], active_top="extras", breadcrumb_label="Verbes Irréguliers",
               extra_css=["lessons"], extra_scripts=["irregular-verbs.js"])


# =======================================================================
# PLACEMENT TEST
# =======================================================================
def build_placement_test():
    header = page_header("Trouve Ton Niveau", "Test de Niveau",
                          "28 questions, trois ou quatre par niveau de Pre-A1 à C2. Réponds à ce que tu peux — le point où ça commence à devenir difficile est le meilleur indice de ton niveau réel.")

    blocks = [
        ("Pre-A1", [
            {"id": "pt-prea1-1", "prompt": "Bonjour, comment ___-vous ?", "options": ["allez", "vas", "es"], "answerIndex": 0, "explanation": "Avec vous, on utilise la forme allez."},
            {"id": "pt-prea1-2", "prompt": "J'___ vingt ans.", "options": ["suis", "ai", "es"], "answerIndex": 1, "explanation": "L'âge s'exprime avec avoir : j'ai vingt ans."},
            {"id": "pt-prea1-3", "prompt": "Il est trois heures de l'après-midi. On dit : « ___, comment tu vas ? »", "options": ["Bonjour", "Bonsoir", "Bonne nuit"], "answerIndex": 0, "explanation": "Bonjour fonctionne toute la journée jusqu'au soir."},
            {"id": "pt-prea1-4", "prompt": "Je ___ étudiant.", "options": ["suis", "es", "est"], "answerIndex": 0, "explanation": "La première personne du verbe être est suis."},
        ]),
        ("A1", [
            {"id": "pt-a1-1", "prompt": "Paris ___ une très belle ville.", "options": ["est", "a", "sont"], "answerIndex": 0, "explanation": "Qualité permanente → être."},
            {"id": "pt-a1-2", "prompt": "___ fille est ma sœur.", "options": ["Le", "La", "Les"], "answerIndex": 1, "explanation": "Fille est féminin singulier → la."},
            {"id": "pt-a1-3", "prompt": "Nous ___ français tous les jours.", "options": ["parle", "parlons", "parlez"], "answerIndex": 1, "explanation": "Nous + verbe en -er = -ons : parlons."},
            {"id": "pt-a1-4", "prompt": "Je ___ tous les matins à sept heures. (se lever)", "options": ["lève", "me lève", "te lèves"], "answerIndex": 1, "explanation": "Se lever est pronominal : je me lève."},
        ]),
        ("A2", [
            {"id": "pt-a2-1", "prompt": "Hier, j'___ (manger) dans un très bon restaurant.", "options": ["ai mangé", "mange", "mangeais"], "answerIndex": 0, "explanation": "Action ponctuelle et terminée → passé composé."},
            {"id": "pt-a2-2", "prompt": "Quand j'étais petit, j'___ (habiter) dans un petit village.", "options": ["ai habité", "habitais", "avais habité"], "answerIndex": 1, "explanation": "Description d'une situation habituelle dans le passé → imparfait."},
            {"id": "pt-a2-3", "prompt": "Elle ___ (se lever) très tôt hier.", "options": ["s'est levée", "se levait", "se lève"], "answerIndex": 0, "explanation": "Action ponctuelle hier → passé composé, avec accord du participe (elle)."},
            {"id": "pt-a2-4", "prompt": "___ (Manger, tu) tous les légumes !", "options": ["Mange", "Manges", "Manger"], "answerIndex": 0, "explanation": "Impératif informel de manger : mange (sans s)."},
        ]),
        ("B1", [
            {"id": "pt-b1-1", "prompt": "J'espère que tu ___ (venir) à mon anniversaire.", "options": ["viens", "viennes", "viendras"], "answerIndex": 1, "explanation": "Espérer que peut être suivi du subjonctif à la forme négative/interrogative, mais ici le style soutenu l'utilise aussi à l'affirmative : viennes."},
            {"id": "pt-b1-2", "prompt": "Tu me prêtes ta voiture ? Oui, je ___ prête sans problème. (te + la)", "options": ["te la", "te le", "vous la"], "answerIndex": 0, "explanation": "Objet indirect (te) + direct féminin (la voiture → la) = te la."},
            {"id": "pt-b1-3", "prompt": "L'année prochaine, je ___ (terminer) mes études.", "options": ["terminerai", "termine", "terminais"], "answerIndex": 0, "explanation": "Projet futur → futur simple."},
            {"id": "pt-b1-4", "prompt": "En Belgique et en Suisse, au lieu de « soixante-dix », on dit : « ___ ».", "options": ["septante", "soixante-dix", "huitante"], "answerIndex": 0, "explanation": "Septante est la forme utilisée en Belgique et en Suisse pour 70."},
        ]),
        ("B2", [
            {"id": "pt-b2-1", "prompt": "Si j'___ (avoir) plus de temps libre, j'apprendrais la guitare.", "options": ["ai", "avais", "aurais"], "answerIndex": 1, "explanation": "Conditionnel hypothétique : si + imparfait de l'indicatif."},
            {"id": "pt-b2-2", "prompt": "Il faut qu'ils ___ (arriver) bientôt, il est déjà tard.", "options": ["arrivent", "arrivant", "arriveront"], "answerIndex": 0, "explanation": "Il faut que exige le subjonctif présent."},
            {"id": "pt-b2-3", "prompt": "La porte ___ ouverte quand je suis arrivé.", "options": ["est", "était", "a été"], "answerIndex": 1, "explanation": "Description d'un état dans le passé → imparfait."},
            {"id": "pt-b2-4", "prompt": "Le pont ___ (construire) au XIXe siècle.", "options": ["a été construit", "a construit", "construisait"], "answerIndex": 0, "explanation": "Voix passive : être + participe passé (accordé en genre et en nombre)."},
        ]),
        ("C1", [
            {"id": "pt-c1-1", "prompt": "Si je l'___ (savoir) avant, je t'aurais prévenu.", "options": ["avais su", "aurais su", "aie su"], "answerIndex": 0, "explanation": "Conditionnelle de type 3 (irréel du passé) : si + plus-que-parfait."},
            {"id": "pt-c1-2", "prompt": "Ça m'a étonné qu'ils ne ___ (arriver) pas encore à cette heure-là.", "options": ["soient pas arrivés", "sont pas arrivés", "arrivaient pas"], "answerIndex": 0, "explanation": "Subjonctif passé : action antérieure à un autre fait déjà passé."},
            {"id": "pt-c1-3", "prompt": "Quelle phrase appartient à un registre académique ?", "options": ["Il convient de souligner que les résultats obtenus confirment l'hypothèse.", "Dis donc, regarde ce que j'ai trouvé, c'est incroyable !", "C'était trop fou hier, non ?"], "answerIndex": 0, "explanation": "Le registre académique évite les tournures familières et utilise des constructions impersonnelles comme « il convient de »."},
            {"id": "pt-c1-4", "prompt": "Au Québec, « c'est plate » est une façon familière de dire...", "options": ["c'est ennuyeux/décevant", "c'est délicieux", "c'est cher"], "answerIndex": 0, "explanation": "C'est une expression très répandue en français québécois, équivalente à « c'est dommage/ennuyeux »."},
        ]),
        ("C2", [
            {"id": "pt-c2-1", "prompt": "Quelle phrase utilise une structure emphatique (phrase clivée) ?", "options": ["Le problème m'inquiète beaucoup.", "C'est le problème qui m'inquiète le plus.", "Je suis assez inquiet à propos du problème."], "answerIndex": 1, "explanation": "C'est une phrase clivée, qui met en relief « le problème » grâce à « c'est... qui »."},
            {"id": "pt-c2-2", "prompt": "Je dois ___ une décision importante.", "options": ["faire", "prendre", "donner"], "answerIndex": 1, "explanation": "La collocation fixe en français est « prendre une décision »."},
            {"id": "pt-c2-3", "prompt": "« Il est possible que » est généralement suivi de…", "options": ["l'indicatif", "le subjonctif", "l'impératif"], "answerIndex": 1, "explanation": "« Il est possible que » présente quelque chose d'incertain, ce qui exige le subjonctif."},
            {"id": "pt-c2-4", "prompt": "Je travaille beaucoup ___ gagner plus d'argent.", "options": ["par", "pour", "de"], "answerIndex": 1, "explanation": "Le but d'une action s'exprime avec pour."},
        ]),
    ]
    sections = [header]
    for level, items in blocks:
        level_slug = level.lower()
        sections.append(f"""<section class="section section--tight" aria-labelledby="pt-{level_slug}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level}</p>
                <h2 id="pt-{level_slug}-heading">Questions de Niveau {level}</h2>
                {ex_block({"id": f"pt-{level_slug}-block", "type": "multiple-choice", "title": f"Questions de Niveau {level}", "items": items})}
            </div>
        </section>""")

    guide = f"""<section class="section section--surface" aria-labelledby="pt-guide-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Comment Lire Tes Résultats</p>
            <h2 id="pt-guide-heading">Ce Que Signifie Ton Score</h2>
            <ul class="summary-list">
                <li>Même les questions de Pre-A1 t'ont posé problème → commence à <a href="levels/pre-a1.html">Pre-A1</a> et construis les bases depuis le début.</li>
                <li>À l'aise en Pre-A1, difficulté dès A1 → commence à <a href="levels/a1.html">A1</a>.</li>
                <li>À l'aise jusqu'à A2, difficulté dès B1 → commence à <a href="levels/b1.html">B1</a>.</li>
                <li>À l'aise jusqu'à B1, difficulté dès B2 → commence à <a href="levels/b2.html">B2</a>.</li>
                <li>À l'aise jusqu'à B2, difficulté dès C1 → commence à <a href="levels/c1.html">C1</a>.</li>
                <li>Tout juste, y compris C2 → révise les leçons de <a href="levels/c2.html">C2</a> pour peaufiner les détails, ou explore la page <a href="extras.html">Extras</a>.</li>
            </ul>
        </div>
    </section>"""
    sections.append(guide)

    write_page("placement-test.html", "Test de Niveau — Renan le Professeur · Cours de Français",
               "Un court test de niveau auto-évaluable pour découvrir à quel niveau du CECR commencer ton français, de Pre-A1 à C2.",
               sections, active_top=None, breadcrumb_label="Test de Niveau",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


# =======================================================================
# PROGRESS
# =======================================================================
def build_progress():
    header = page_header("Ton Parcours", "Ma Progression",
                          "XP, séries et badges, enregistrés uniquement sur cet appareil — rien n'est jamais envoyé à un serveur.")

    section = f"""<section class="section section--surface" aria-labelledby="progress-heading">
        <div class="section__inner">
            <h2 id="progress-heading" class="visually-hidden">Progression</h2>
            <div class="progress-panel__summary" id="progress-summary"></div>
        </div>
    </section>
<section class="section section--tight" aria-labelledby="progress-levels-heading">
        <div class="section__inner">
            <p class="eyebrow">Par Niveau</p>
            <h2 id="progress-levels-heading">Progression par Niveau</h2>
            <div id="progress-levels"></div>
        </div>
    </section>
<section class="section section--surface" aria-labelledby="progress-badges-heading">
        <div class="section__inner">
            <p class="eyebrow">Réussites</p>
            <h2 id="progress-badges-heading">Badges</h2>
            <ul class="badge-grid" id="progress-badges"></ul>
        </div>
    </section>
<section class="section section--tight" aria-labelledby="progress-reset-heading">
        <div class="section__inner section__inner--narrow">
            <p class="eyebrow">Recommencer</p>
            <h2 id="progress-reset-heading">Réinitialiser la Progression</h2>
            <p style="color:var(--color-text-muted);">Ceci efface ton XP, ta série et tes badges sur cet appareil. L'historique de répétition espacée (Révision du Jour) est enregistré séparément et n'est pas affecté.</p>
            <button type="button" class="btn btn--ghost" id="progress-reset-btn">Réinitialiser XP et Badges</button>
        </div>
    </section>"""

    write_page("progress.html", "Ma Progression — Renan le Professeur · Cours de Français",
               "Suis ton XP, ta série et tes badges tout au long du cours de français, enregistrés de façon privée sur ton appareil.",
               [header, section], active_top=None, breadcrumb_label="Ma Progression")


# =======================================================================
# TODAY'S REVIEW
# =======================================================================
def build_today_review():
    header = page_header("Répétition Espacée", "Révision du Jour",
                          "Une courte révision quotidienne des exercices que tu as ratés auparavant — générée automatiquement à partir de ton propre historique.")

    section = f"""<section class="section section--surface" aria-labelledby="review-heading">
        <div class="section__inner">
            <h2 id="review-heading" class="visually-hidden">Révision</h2>
            <div id="review-status-box" class="notice"><p>Chargement de ta file de révision…</p></div>
            <div id="review-blocks" style="margin-top:var(--space-md);"></div>
        </div>
    </section>"""

    write_page("today-review.html", "Révision du Jour — Renan le Professeur · Cours de Français",
               "Une révision quotidienne par répétition espacée d'exercices de français que tu as ratés auparavant, générée automatiquement à partir de ton propre historique.",
               [header, section], active_top=None, breadcrumb_label="Révision du Jour",
               extra_css=["exercises"], extra_scripts=["exercises.js", "mastery.js", "today-review.js"])


# =======================================================================
# SIMULATED EXAMS
# =======================================================================
def build_simulated_exams():
    header = page_header("Pratique d'Examen", "Examens Blancs",
                          "Des sections de pratique dans le style des certifications officielles de français — DELF et DALF — avec corrigés.")

    intro = f"""<section class="section section--tight" aria-labelledby="exams-intro-heading">
        <div class="section__inner section__inner--narrow">
            <h2 id="exams-intro-heading" class="visually-hidden">À Propos de Ces Examens</h2>
            <p style="color:var(--color-text-muted);">Le français dispose de deux certifications internationales de référence en tant que langue étrangère : le <strong>DELF</strong> (Diplôme d'Études en Langue Française, niveaux A1 à B2) et le <strong>DALF</strong> (Diplôme Approfondi de Langue Française, niveaux C1 et C2), tous deux délivrés par le Ministère français de l'Éducation nationale via France Éducation international. Les deux évaluent les mêmes quatre compétences — compréhension écrite, compréhension orale, production écrite et production orale — selon les niveaux du CECR de A1 à C2. Les sections suivantes sont de la pratique dans ce style, pas de vrais examens officiels.</p>
        </div>
    </section>"""

    pa1_reading = ("<p>Salut, je m'appelle Sarah. Je suis française et j'ai vingt ans. J'étudie à l'université et j'habite avec deux colocataires. Le matin, je vais en cours, et l'après-midi, je travaille dans un café. Le week-end, j'aime sortir avec mes amies.</p>")
    pa1_reading_ex = {"id": "sim-prea1-reading", "type": "true-false", "title": "Lecture Style DELF/DALF — Pre-A1", "items": [
        {"id": "simpa1r1", "statement": "Sarah habite seule.", "answer": False, "explanation": "Le texte dit : « j'habite avec deux colocataires »."},
        {"id": "simpa1r2", "statement": "Sarah travaille dans un café l'après-midi.", "answer": True, "explanation": "Le texte dit : « l'après-midi, je travaille dans un café »."},
        {"id": "simpa1r3", "statement": "Sarah n'aime pas sortir avec ses amies.", "answer": False, "explanation": "Le texte dit : « j'aime sortir avec mes amies »."},
    ]}
    pa1_grammar_ex = {"id": "sim-prea1-grammar", "type": "multiple-choice", "title": "Grammaire Style DELF/DALF — Pre-A1",
                       "items": [
                           {"id": "simpa1g1", "prompt": "Je ___ étudiante.", "options": ["suis", "es", "est"], "answerIndex": 0, "explanation": "Je + être = suis."},
                           {"id": "simpa1g2", "prompt": "Comment tu t'___ ?", "options": ["appelles", "appelle", "appellent"], "answerIndex": 0, "explanation": "Question avec tu : comment tu t'appelles ?"},
                           {"id": "simpa1g3", "prompt": "Nous ___ du Mexique.", "options": ["suis", "sommes", "sont"], "answerIndex": 1, "explanation": "Nous + être = sommes."},
                       ]}

    a1_reading = ("<p>Ma routine quotidienne est assez simple. Je me lève à sept heures, je prends un petit-déjeuner rapide et je vais au travail en bus. À midi, je mange avec mes collègues. L'après-midi, j'étudie l'anglais pendant deux heures. Avant de dormir, je lis toujours un peu.</p>")
    a1_reading_ex = {"id": "sim-a1-reading", "type": "multiple-choice", "title": "Lecture Style DELF/DALF — A1", "items": [
        {"id": "sima1r1", "prompt": "Comment la personne va-t-elle au travail ?", "options": ["À pied", "En bus", "En voiture"], "answerIndex": 1, "explanation": "Le texte dit : « je vais au travail en bus »."},
        {"id": "sima1r2", "prompt": "Qu'étudie-t-elle l'après-midi ?", "options": ["Le français", "L'anglais", "L'espagnol"], "answerIndex": 1, "explanation": "Le texte dit : « j'étudie l'anglais pendant deux heures »."},
        {"id": "sima1r3", "prompt": "Que fait-elle avant de dormir ?", "options": ["Elle regarde la télévision", "Elle lit un peu", "Elle écoute de la musique"], "answerIndex": 1, "explanation": "Le texte dit : « je lis toujours un peu »."},
    ]}
    a1_grammar_ex = {"id": "sim-a1-grammar", "type": "fill-blank", "title": "Grammaire Style DELF/DALF — A1",
                      "instructions": "Complète chaque phrase.",
                      "items": [
                          {"id": "sima1g1", "prompt": "Elle ___ (avoir) vingt-cinq ans.", "answers": [["a"]], "explanation": "Elle + avoir = a."},
                          {"id": "sima1g2", "prompt": "Nous ___ (habiter) à Paris.", "answers": [["habitons"]], "explanation": "Nous + verbe en -er = -ons : habitons."},
                          {"id": "sima1g3", "prompt": "Combien de frères et sœurs ___ (tu - avoir) ?", "answers": [["as"]], "explanation": "Tu + avoir = as."},
                      ]}

    a2_reading = ("<p>L'été dernier, j'ai voyagé au Portugal avec ma famille. Nous avons visité Lisbonne et Porto, et nous avons mangé des plats délicieux dans chaque ville. Le temps était très agréable, ni trop chaud ni trop froid. C'était l'un des meilleurs voyages de ma vie, et nous prévoyons déjà d'y retourner l'année prochaine.</p>")
    a2_reading_ex = {"id": "sim-a2-reading", "type": "true-false", "title": "Lecture Style DELF/DALF — A2", "items": [
        {"id": "sima2r1", "statement": "Le voyage était au Portugal.", "answer": True, "explanation": "Le texte dit : « j'ai voyagé au Portugal avec ma famille »."},
        {"id": "sima2r2", "statement": "Le temps était très chaud.", "answer": False, "explanation": "Le texte dit que le temps « était très agréable, ni trop chaud ni trop froid »."},
        {"id": "sima2r3", "statement": "La famille prévoit de retourner au Portugal.", "answer": True, "explanation": "Le texte dit : « nous prévoyons déjà d'y retourner l'année prochaine »."},
    ]}
    a2_grammar_ex = {"id": "sim-a2-grammar", "type": "fill-blank", "title": "Grammaire Style DELF/DALF — A2",
                      "instructions": "Complète chaque phrase avec le passé composé ou l'imparfait selon le cas.",
                      "items": [
                          {"id": "sima2g1", "prompt": "Hier, j'___ (rendre visite) à mes grands-parents.", "answers": [["ai rendu visite"]], "explanation": "Marqueur de temps précis (hier) → passé composé."},
                          {"id": "sima2g2", "prompt": "Quand j'étais enfant, j'___ (vivre) à la campagne.", "answers": [["habitais"], ["vivais"]], "explanation": "Description d'une période du passé → imparfait."},
                          {"id": "sima2g3", "prompt": "L'année dernière, ils ___ (acheter) une nouvelle maison.", "answers": [["ont acheté"]], "explanation": "Marqueur de temps précis → passé composé."},
                      ]}

    b1_reading = ("<p>Ces dernières années, de plus en plus de personnes en France choisissent de travailler depuis chez elles au moins quelques jours par semaine. Selon une enquête récente, la majorité des salariés se déclarent plus satisfaits qu'avant, notamment grâce au temps économisé sur les trajets. Cependant, certains sondés signalent des difficultés à séparer vie personnelle et travail, et se plaignent de journées de travail plus longues que d'habitude.</p>")
    b1_reading_ex = {"id": "sim-b1-reading", "type": "true-false", "title": "Lecture Style DELF/DALF — B1", "items": [
        {"id": "simb1r1", "statement": "La majorité des salariés interrogés dit être plus satisfaite en travaillant depuis chez elle.", "answer": True, "explanation": "« La majorité des salariés se déclarent plus satisfaits. »"},
        {"id": "simb1r2", "statement": "Personne n'a mentionné d'inconvénient au télétravail.", "answer": False, "explanation": "Certains ont mentionné des difficultés à séparer travail et vie personnelle, et des journées plus longues."},
        {"id": "simb1r3", "statement": "L'économie de temps de trajet est une raison de la satisfaction.", "answer": True, "explanation": "Le texte dit : « notamment grâce au temps économisé sur les trajets »."},
    ]}
    b1_grammar_ex = {"id": "sim-b1-grammar", "type": "fill-blank", "title": "Grammaire Style DELF/DALF — B1",
                      "instructions": "Complète chaque phrase.",
                      "items": [
                          {"id": "simb1g1", "prompt": "Quand j'étais petit, je ___ (jouer) toujours dans la rue.", "answers": [["jouais"]], "explanation": "Action habituelle dans le passé → imparfait."},
                          {"id": "simb1g2", "prompt": "Demain, nous ___ (partir) très tôt.", "answers": [["partirons"]], "explanation": "Projet futur → futur simple."},
                          {"id": "simb1g3", "prompt": "___ (Pouvoir - vous) m'aider, s'il vous plaît ? (formel)", "answers": [["Pourriez"]], "explanation": "Demande formelle et polie → conditionnel."},
                          {"id": "simb1g4", "prompt": "J'espère que tu ___ (avoir) un bon voyage.", "answers": [["aies"]], "explanation": "Espérer que peut exiger le subjonctif présent en registre soutenu."},
                      ]}
    b1_listening = ("<p><strong>Réceptionniste :</strong> Hôtel Miramar, bonjour.<br><strong>Client :</strong> Bonjour, je voudrais réserver une chambre double pour le week-end.<br><strong>Réceptionniste :</strong> Bien sûr, pour combien de nuits ?<br><strong>Client :</strong> Deux nuits, vendredi et samedi.<br><strong>Réceptionniste :</strong> Parfait, nous avons de la disponibilité. À quel nom dois-je faire la réservation ?<br><strong>Client :</strong> Au nom d'Anne Roux.</p>")
    b1_listening_ex = {"id": "sim-b1-listening", "type": "multiple-choice", "title": "Compréhension Orale Style DELF/DALF — B1",
                        "instructions": "Lis ce script comme si c'était un audio et réponds.",
                        "items": [
                            {"id": "simb1l1", "prompt": "Quel type de chambre le client réserve-t-il ?", "options": ["Simple", "Double", "Familiale"], "answerIndex": 1, "explanation": "Le texte dit : « une chambre double »."},
                            {"id": "simb1l2", "prompt": "Combien de nuits reste-t-il ?", "options": ["Une nuit", "Deux nuits", "Trois nuits"], "answerIndex": 1, "explanation": "Le texte dit : « Deux nuits, vendredi et samedi »."},
                        ]}

    b2_reading = ("<p>Le débat sur l'intelligence artificielle dans le monde du travail continue de diviser les experts et l'opinion publique. Si d'un côté on souligne les avantages en termes d'efficacité, de l'autre grandit l'inquiétude quant à la perte d'emplois dans certains secteurs. Les économistes s'accordent cependant à dire que la formation continue sera déterminante pour affronter cette transition.</p>")
    b2_reading_ex = {"id": "sim-b2-reading", "type": "multiple-choice", "title": "Lecture Style DELF/DALF — B2", "items": [
        {"id": "simb2r1", "prompt": "Sur quoi les économistes s'accordent-ils ?", "options": ["L'IA devrait être interdite", "La formation continue sera essentielle", "La perte d'emplois est exagérée"], "answerIndex": 1, "explanation": "« La formation continue sera déterminante. »"},
        {"id": "simb2r2", "prompt": "Quel avantage de l'IA est souligné ?", "options": ["L'efficacité", "Le faible coût", "La simplicité"], "answerIndex": 0, "explanation": "Le texte dit : « on souligne les avantages en termes d'efficacité »."},
    ]}
    b2_grammar_ex = {"id": "sim-b2-grammar", "type": "fill-blank", "title": "Grammaire Style DELF/DALF — B2",
                      "instructions": "Complète chaque phrase.",
                      "items": [
                          {"id": "simb2g1", "prompt": "Si j'___ (avoir) plus de temps, j'étudierais davantage.", "answers": [["avais"]], "explanation": "Conditionnel hypothétique : si + imparfait."},
                          {"id": "simb2g2", "prompt": "Je doute qu'ils ___ (arriver) à l'heure.", "answers": [["arrivent"]], "explanation": "Douter que exige le subjonctif présent."},
                          {"id": "simb2g3", "prompt": "Si j'avais su la vérité, j'___ (agir) différemment.", "answers": [["aurais agi"]], "explanation": "Conditionnelle irréelle du passé : conséquence au conditionnel passé."},
                      ]}

    c1_reading = ("<p>La prolifération d'assistants virtuels fondés sur l'intelligence artificielle a ravivé un vieux débat philosophique : une machine, aussi sophistiquée soit sa capacité à générer du langage, peut-elle réellement comprendre le sens de ce qu'elle produit ? Tandis que certains chercheurs soutiennent qu'il s'agit d'une question purement technique, appelée à se résoudre avec le temps, d'autres insistent sur le fait que la compréhension véritable exige une expérience corporelle et contextuelle dont ces systèmes, par définition, sont dépourvus.</p>")
    c1_reading_ex = {"id": "sim-c1-reading", "type": "true-false", "title": "Lecture Style DELF/DALF — C1", "items": [
        {"id": "simc1r1", "statement": "Le texte se demande si une machine peut réellement comprendre le langage qu'elle génère.", "answer": True, "explanation": "Le texte dit : « une machine... peut-elle réellement comprendre le sens de ce qu'elle produit ? »."},
        {"id": "simc1r2", "statement": "Tous les chercheurs sont d'accord pour dire que c'est purement une question technique.", "answer": False, "explanation": "Le texte dit que « d'autres insistent sur le fait que la compréhension véritable exige une expérience corporelle et contextuelle »."},
        {"id": "simc1r3", "statement": "Selon certains, la compréhension véritable requiert une expérience corporelle et contextuelle.", "answer": True, "explanation": "Le texte le dit exactement dans la dernière phrase."},
    ]}
    c1_grammar_ex = {"id": "sim-c1-grammar", "type": "fill-blank", "title": "Grammaire Style DELF/DALF — C1",
                      "instructions": "Complète chaque phrase.",
                      "items": [
                          {"id": "simc1g1", "prompt": "Si j'étais arrivé plus tôt, j'___ (voir) mon frère.", "answers": [["aurais vu"]], "explanation": "Conditionnelle irréelle du passé."},
                          {"id": "simc1g2", "prompt": "Je ne connais personne qui ___ (savoir) autant sur ce sujet.", "answers": [["sache"]], "explanation": "Antécédent indéfini/inexistant (personne) → subjonctif."},
                          {"id": "simc1g3", "prompt": "Il conviendrait de ___ (reconsidérer) cette partie du projet.", "answers": [["reconsidérer"]], "explanation": "Il conviendrait de + infinitif, forme atténuée d'une suggestion."},
                      ]}
    c1_listening = ("<p><strong>Journaliste :</strong> Votre dernier livre aborde des sujets complexes comme la mémoire et l'exil. D'où vient ce choix ?<br><strong>Autrice :</strong> Il naît d'une question personnelle : que reste-t-il de nous quand on quitte l'endroit où on a grandi ? Je voulais l'explorer à travers une histoire, pas un essai.<br><strong>Journaliste :</strong> Y a-t-il quelque chose d'autobiographique dans le roman ?<br><strong>Autrice :</strong> Sans aucun doute, même si j'ai préféré le transformer par la fiction.</p>")
    c1_listening_ex = {"id": "sim-c1-listening", "type": "multiple-choice", "title": "Compréhension Orale Style DELF/DALF — C1",
                        "instructions": "Lis ce script comme si c'était un audio et réponds.",
                        "items": [
                            {"id": "simc1l1", "prompt": "Quels sujets aborde le dernier livre de l'autrice ?", "options": ["L'amour et l'aventure", "La mémoire et l'exil", "La science-fiction"], "answerIndex": 1, "explanation": "Le journaliste dit : « aborde des sujets complexes comme la mémoire et l'exil »."},
                            {"id": "simc1l2", "prompt": "Comment a-t-elle préféré traiter l'élément autobiographique ?", "options": ["Comme un essai direct", "Par la fiction", "Elle ne le mentionne pas"], "answerIndex": 1, "explanation": "L'autrice dit : « j'ai préféré le transformer par la fiction »."},
                        ]}

    c2_reading = ("<p>Il est pour le moins paradoxal que, à une époque définie par la surabondance informationnelle, la capacité de discernement critique semble s'être érodée en proportion inverse de la quantité de données disponibles. On pourrait arguer que la simple accumulation d'informations, loin de se traduire automatiquement en connaissance, exige en elle-même un appareil conceptuel capable de la hiérarchiser, de la contextualiser et, en dernière instance, de la remettre en question.</p>")
    c2_reading_ex = {"id": "sim-c2-reading", "type": "true-false", "title": "Lecture Style DELF/DALF — C2", "items": [
        {"id": "simc2r1", "statement": "Le texte affirme que plus d'information produit toujours plus de discernement critique.", "answer": False, "explanation": "Le texte dit que le discernement critique « semble s'être érodée » malgré la surabondance informationnelle."},
        {"id": "simc2r2", "statement": "Selon le texte, l'accumulation d'informations ne se traduit pas automatiquement en connaissance.", "answer": True, "explanation": "Le texte dit : « la simple accumulation d'informations... [ne] se traduit [pas] automatiquement en connaissance »."},
        {"id": "simc2r3", "statement": "Le texte suggère qu'un cadre conceptuel est nécessaire pour traiter l'information de façon critique.", "answer": True, "explanation": "Le texte dit qu'il faut « un appareil conceptuel capable de la hiérarchiser, de la contextualiser... de la remettre en question »."},
    ]}
    c2_grammar_ex = {"id": "sim-c2-grammar", "type": "multiple-choice", "title": "Grammaire Style DELF/DALF — C2",
                      "items": [
                          {"id": "simc2g1", "prompt": "« Ceux qui ___ (arriver) en retard ne pourront pas entrer. »", "options": ["arrivent", "arriveront", "arriveraient"], "answerIndex": 0, "explanation": "Ceux qui avec antécédent indéfini/générique peut exiger le présent ou le futur ; ici le présent générique est attendu, non le conditionnel."},
                          {"id": "simc2g2", "prompt": "« Il se peut que cela ___ (changer) bientôt. »", "options": ["change", "changera", "changerait"], "answerIndex": 0, "explanation": "Il se peut que exige le subjonctif."},
                          {"id": "simc2g3", "prompt": "« Quiconque ___ (enfreindre) cette règle sera sanctionné. » (registre juridique)", "options": ["enfreint", "enfreindra", "eût enfreint"], "answerIndex": 1, "explanation": "Le futur simple exprime ici une condition générale à venir, usage courant du registre juridique/réglementaire."},
                      ]}

    exam_sections = []
    levels_data = [
        ("Pre-A1", pa1_reading, pa1_reading_ex, pa1_grammar_ex, None, None),
        ("A1", a1_reading, a1_reading_ex, a1_grammar_ex, None, None),
        ("A2", a2_reading, a2_reading_ex, a2_grammar_ex, None, None),
        ("B1", b1_reading, b1_reading_ex, b1_grammar_ex, b1_listening, b1_listening_ex),
        ("B2", b2_reading, b2_reading_ex, b2_grammar_ex, None, None),
        ("C1", c1_reading, c1_reading_ex, c1_grammar_ex, c1_listening, c1_listening_ex),
        ("C2", c2_reading, c2_reading_ex, c2_grammar_ex, None, None),
    ]
    for level, reading, reading_ex, grammar_ex, listening, listening_ex in levels_data:
        level_slug = level.lower()
        listening_html = ""
        if listening and listening_ex:
            listening_html = f"""
                <p class="eyebrow" style="margin-top:var(--space-lg);">{level} · Compréhension Orale</p>
                <div class="card"><div class="prose">{listening}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(listening_ex)}</div>"""
        exam_sections.append(f"""<section class="section section--surface" aria-labelledby="sim-{level_slug}-heading">
            <div class="section__inner">
                <p class="eyebrow">{level} · Compréhension Écrite</p>
                <h2 id="sim-{level_slug}-heading">Examen Blanc {level}</h2>
                <div class="card"><div class="prose">{reading}</div></div>
                <div style="margin-top:var(--space-md);">{ex_block(reading_ex)}</div>
                <div style="margin-top:var(--space-md);">{ex_block(grammar_ex)}</div>{listening_html}
            </div>
        </section>""")

    write_page("simulated-exams.html", "Examens Blancs — Renan le Professeur · Cours de Français",
               "Des sections d'examen blanc dans le style DELF/DALF en français, avec compréhension écrite et grammaire, plus corrigés.",
               [header, intro] + exam_sections, active_top="exams", breadcrumb_label="Examens Blancs",
               extra_css=["exercises"], extra_scripts=["exercises.js"])


if __name__ == "__main__":
    build_index()
    build_exercises()
    build_extras()
    build_dictionary()
    build_irregular_verbs()
    build_placement_test()
    build_progress()
    build_today_review()
    build_simulated_exams()
