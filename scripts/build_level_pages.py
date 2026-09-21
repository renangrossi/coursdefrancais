#!/usr/bin/env python3
"""
Construit levels/{niveau}.html : la page hub de chaque niveau du CECR —
résumé, grille ordonnée des cartes de leçon, appel à l'action vers
"Teste-toi" et une section compacte de Vocabulaire (deux tableaux de mots
par thème, chacun avec des exercices).

Seul Pre-A1 a du contenu Vocabulaire/Lecture/Écoute/Écriture/Conversation
rédigé pour l'instant (voir scripts/curriculum_source/pre-a1.py pour le
niveau complet) ; les six autres niveaux affichent un état "bientôt
disponible" à la place — voir has_extras() ci-dessous.

Usage :
    python3 scripts/build_level_pages.py
"""
import json
import sys
from pathlib import Path
from string import ascii_uppercase

sys.path.insert(0, str(Path(__file__).resolve().parent))
import site_chrome  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
REL = "../"

LEVEL_META = {
    "Pre-A1": ("Survie", "Premier contact avec le français — l'alphabet, les sons, les salutations et les premiers verbes pour survivre en classe."),
    "A1": ("Débutant", "Phrases de base et expressions quotidiennes pour des besoins immédiats — salutations, genre, être/avoir, le présent de l'indicatif."),
    "A2": ("Élémentaire", "Échanges simples et directs sur des sujets familiers — verbes irréguliers, le passé composé, verbes pronominaux, comparatifs."),
    "B1": ("Intermédiaire", "Français quotidien et autonome — l'imparfait, pronoms indirects et combinés, futur, conditionnel et impératif."),
    "B2": ("Intermédiaire Avancé", "Interaction fluide et spontanée — le subjonctif, phrases conditionnelles, discours indirect, la voix passive."),
    "C1": ("Avancé", "Langue flexible et efficace pour la vie professionnelle et académique — le système complet du subjonctif, registre et connecteurs."),
    "C2": ("Maîtrise", "Maîtrise précise et nuancée du français — syntaxe complexe, registre littéraire, nuances lexicales et la vraie diversité de la langue."),
}

# Deux thèmes de vocabulaire compacts par niveau : (titre du thème, [ (mot, catégorie, sens, exemple), ... ])
# Seul Pre-A1 est rédigé pour l'instant.
VOCAB = {
    "Pre-A1": [
        ("Salutations et Politesse", [
            ("bonjour / au revoir", "expression", "salutation d'arrivée / de départ", "Bonjour ! Comment ça va ?"),
            ("bonsoir", "expression", "salutation à partir du soir", "Bonsoir, professeur."),
            ("s'il vous plaît / merci", "expression", "demander poliment / remercier", "Un café, s'il vous plaît. Merci."),
            ("de rien", "expression", "réponse à un remerciement", "— Merci. — De rien."),
            ("pardon / excusez-moi", "expression", "s'excuser poliment", "Pardon, où sont les toilettes ?"),
            ("comment tu t'appelles ?", "expression", "demander le nom", "Comment tu t'appelles ? Je m'appelle Anna."),
            ("enchanté(e)", "expression", "en rencontrant quelqu'un", "Enchanté, je suis Charles."),
            ("oui / non", "adverbe", "affirmation / négation", "Tu parles français ? Oui, un peu."),
        ]),
        ("Objets de Classe", [
            ("le crayon", "nom", "instrument pour écrire à la mine", "J'ai besoin d'un crayon pour l'examen."),
            ("le cahier", "nom", "carnet pour écrire", "J'écris mes devoirs dans mon cahier."),
            ("le sac à dos", "nom", "sac pour transporter les livres", "Mon sac à dos est bleu et très grand."),
            ("le tableau", "nom", "surface pour écrire en classe", "Le professeur écrit au tableau."),
            ("le livre", "nom", "support de lecture ou d'étude", "Ce livre de français est très bon."),
            ("la chaise / la table", "nom", "meuble pour s'asseoir / pour travailler", "Pose le livre sur la table."),
            ("la fenêtre / la porte", "nom", "ouverture pour la lumière / pour entrer et sortir", "Ouvre la fenêtre, s'il te plaît."),
            ("le professeur / la professeure", "nom", "personne qui enseigne", "La professeure explique très bien."),
        ]),
    ],
}

# Texte de lecture, script d'écoute, consigne d'écriture et de conversation par niveau.
# Seul Pre-A1 est rédigé pour l'instant.
READING = {
    "Pre-A1": ("Une Salutation dans la Rue", "<p>—Bonjour ! Bonjour.</p><p>—Bonjour ! Comment ça va ?</p><p>—Très bien, merci. Et toi ?</p><p>—Bien aussi. Je m'appelle Sofia.</p><p>—Enchanté, Sofia. Moi, c'est David.</p><p>—Enchantée, David. À bientôt !</p><p>—Au revoir !</p>"),
}

LISTENING = {
    "Pre-A1": ("Au Café", "<p><strong>Serveur :</strong> Bonjour ! Qu'est-ce que je vous sers ?<br><strong>Client :</strong> Bonjour. Un café au lait, s'il vous plaît.<br><strong>Serveur :</strong> Très bien. Autre chose ?<br><strong>Client :</strong> Non, merci, ce sera tout. C'est combien ?<br><strong>Serveur :</strong> C'est deux euros.<br><strong>Client :</strong> Voilà. Merci, au revoir !<br><strong>Serveur :</strong> Merci à vous, bonne journée !</p>"),
}

WRITING = {
    "Pre-A1": "Écris 3-4 phrases très simples pour te présenter : ton prénom, ta nationalité et une formule de salutation. Utilise être et au moins un autre verbe.",
}

SPEAKING = {
    "Pre-A1": ["Présente-toi en trente secondes : ton prénom et d'où tu viens.", "Salue un camarade et demande-lui son prénom."],
}


def esc(s):
    import html
    return html.escape(s, quote=False)


def lesson_cards(level_slug, nav_list):
    cards = []
    for i, entry in enumerate(nav_list):
        idx = ascii_uppercase[i] if i < 26 else str(i + 1)
        lesson = json.loads((REPO_ROOT / "curriculum" / level_slug / f"{entry['slug']}.json").read_text(encoding="utf-8"))
        cards.append(f"""<article class="lesson-card">
            <span class="lesson-card__index" aria-hidden="true">{idx}</span>
            <h3><a class="lesson-card__title-link" href="{level_slug}/{entry['slug']}.html">{esc(lesson['title'])}</a></h3>
            <p>{esc(lesson['subtitle'])}</p>
        </article>""")
    return "".join(cards)


def vocab_section(level_code, level_slug):
    themes = VOCAB.get(level_code, [])
    if not themes:
        return ""
    blocks = []
    for ti, (theme_title, words) in enumerate(themes):
        rows = "".join(
            f"<tr><td><strong>{esc(w)}</strong></td><td class=\"text-muted\">{esc(pos)}</td><td>{esc(meaning)}</td><td><em>{esc(ex_sentence)}</em></td></tr>"
            for w, pos, meaning, ex_sentence in words
        )
        opts = [w for w, *_ in words][:6]
        items = []
        for i, (w, pos, meaning, ex_sentence) in enumerate(words[:4]):
            item_opts = opts if w in opts else opts + [w]
            items.append({
                "id": f"{level_slug}v{ti}i{i}",
                "prompt": f"Quel mot signifie « {meaning} » ?",
                "options": item_opts,
                "answerIndex": item_opts.index(w),
                "explanation": f"{w} signifie {meaning}.",
            })
        ex_block = {"id": f"{level_slug}-vocab-{ti}-mc", "type": "multiple-choice", "title": "Associe le Sens", "items": items}
        blocks.append(f"""<div class="card" style="margin-bottom:var(--space-lg);">
            <h3>{esc(theme_title)}</h3>
            <div class="table-scroll">
                <table class="ref-table">
                    <thead><tr><th>Mot</th><th>Catégorie</th><th>Sens</th><th>Exemple</th></tr></thead>
                    <tbody>{rows}</tbody>
                </table>
            </div>
            <div style="margin-top:var(--space-md);"><div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex_block, ensure_ascii=False)}</script></div></div>
        </div>""")
    return f"""<section id="vocabulary" class="section section--tight" aria-labelledby="vocabulary-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code}</p>
                <h2 id="vocabulary-heading">Vocabulaire</h2>
                <p>Des groupes de mots par thème pour des situations réelles, chacun avec des phrases d'exemple et une vérification rapide.</p>
            </div>
            {"".join(blocks)}
        </div>
    </section>"""


def reading_section(level_code, level_slug):
    entry = READING.get(level_code)
    if not entry:
        return ""
    title, passage = entry
    ex = {
        "id": f"{level_slug}-reading-mc", "type": "true-false", "title": "Vérifie ta Compréhension",
        "instructions": "D'après le texte ci-dessus, indique si chaque affirmation est vraie ou fausse.",
        "items": [
            {"id": f"{level_slug}rd1", "statement": "Le texte est écrit à la première personne ou comme un dialogue direct entre personnes.", "answer": True, "explanation": "Le texte utilise des formes de je/nous ou un échange direct entre les locuteurs."},
        ],
    }
    return f"""<section id="reading" class="section section--surface" aria-labelledby="reading-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code} &middot; Lecture</p>
                <h2 id="reading-heading">{esc(title)}</h2>
            </div>
            <div class="card"><div class="prose">{passage}</div></div>
            <div style="margin-top:var(--space-md);"><div class="exercise-block"><script type="application/json" class="exercise-data">{json.dumps(ex, ensure_ascii=False)}</script></div></div>
        </div>
    </section>"""


def listening_section(level_code):
    entry = LISTENING.get(level_code)
    if not entry:
        return ""
    title, script = entry
    return f"""<section id="listening" class="section section--tight" aria-labelledby="listening-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code} &middot; Écoute (script)</p>
                <h2 id="listening-heading">{esc(title)}</h2>
                <p>Il n'y a pas encore d'enregistrement audio &mdash; lis cet échange comme un dialogue d'écoute et imagine le rythme de la parole réelle.</p>
            </div>
            <div class="card"><div class="prose">{script}</div></div>
        </div>
    </section>"""


def writing_speaking_section(level_code):
    prompt = WRITING.get(level_code)
    topics = SPEAKING.get(level_code)
    if not prompt or not topics:
        return ""
    speaking_items = "".join(f"<li>{esc(p)}</li>" for p in topics)
    return f"""<section id="writing" class="section section--surface" aria-labelledby="writing-heading">
        <div class="section__inner split">
            <div>
                <p class="eyebrow">{level_code} &middot; Écriture</p>
                <h2 id="writing-heading">Activité d'Écriture Guidée</h2>
                <p style="max-width:56ch;">{esc(prompt)}</p>
            </div>
            <div class="card card--feature" id="speaking">
                <p class="eyebrow">{level_code} &middot; Conversation</p>
                <h3 style="font-size:var(--step-0);">Sujets de Conversation</h3>
                <ul class="summary-list">{speaking_items}</ul>
            </div>
        </div>
    </section>"""


def build(level_code, level_slug):
    name, blurb = LEVEL_META[level_code]
    nav_map = json.loads((REPO_ROOT / "scripts" / "lesson_nav_map.json").read_text(encoding="utf-8"))
    nav_list = nav_map.get(level_slug, [])
    index = json.loads((REPO_ROOT / "curriculum" / "index.json").read_text(encoding="utf-8"))
    overview = index["levels"][level_code.upper()]["overview"]

    title = f"{level_code} — {name} — Renan le Professeur · Cours de Français"
    description = f"{level_code} {name} : {blurb}"[:300]
    breadcrumb = (
        f'<li><a href="{REL}index.html">Accueil</a></li>'
        f'<li aria-current="page">Niveaux</li>'
        f'<li aria-current="page">{level_code} {name}</li>'
    )
    page_header = f"""<div class="page-header">
        {site_chrome.STARS_ROW}
        <div class="page-header__inner">
            <div class="page-header__text">
                <p class="eyebrow hero__eyebrow">Au programme</p>
                <h1>{level_code} &mdash; {esc(name)}</h1>
                <p class="page-header__lede">{esc(blurb)}</p>
            </div>
        </div>
    </div>"""

    has_vocab = bool(VOCAB.get(level_code))
    has_reading = level_code in READING
    has_listening = level_code in LISTENING
    has_writing = level_code in WRITING and level_code in SPEAKING

    toc_links = ['<a href="#lessons">Leçons</a>', '<a href="#test-yourself">Teste-toi</a>']
    if has_vocab:
        toc_links.append('<a href="#vocabulary">Vocabulaire</a>')
    if has_reading:
        toc_links.append('<a href="#reading">Lecture</a>')
    if has_listening:
        toc_links.append('<a href="#listening">Écoute</a>')
    if has_writing:
        toc_links.append('<a href="#writing">Écriture</a>')
        toc_links.append('<a href="#speaking">Conversation</a>')
    toc = f'<div class="level-toc" data-scrollspy><div class="level-toc__inner">{"".join(toc_links)}</div></div>'

    overview_section = f"""<section class="section section--tight" aria-labelledby="overview-heading">
        <div class="section__inner">
            <h2 id="overview-heading" class="visually-hidden">Résumé</h2>
            <p style="max-width:62ch;font-size:var(--step-0);color:var(--color-text-muted);">{esc(overview)}</p>
        </div>
    </section>"""

    if nav_list:
        lessons_body = f'<div class="grid">{lesson_cards(level_slug, nav_list)}</div>'
        lessons_intro = f"{len(nav_list)} leçons, dans l'ordre &mdash; chacune s'appuie sur la précédente."
    else:
        lessons_body = '<p style="max-width:56ch;color:var(--color-text-muted);">Ce niveau n\'a pas encore de leçons publiées &mdash; il arrive bientôt. En attendant, commence par le niveau <a href="pre-a1.html">Pre-A1</a>, déjà disponible en entier.</p>'
        lessons_intro = "Bientôt disponible."

    lessons_section = f"""<section id="lessons" class="section section--surface" aria-labelledby="grammar-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code}</p>
                <h2 id="grammar-heading">Leçons</h2>
                <p>{lessons_intro}</p>
            </div>
            {lessons_body}
        </div>
    </section>"""

    if nav_list:
        ty_body = f'<a class="btn btn--accent" href="{level_slug}/test-yourself.html"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><circle cx="12" cy="15" r="6"/><path d="m9 10-3-7"/><path d="m15 10 3-7"/><path d="M9.5 15.5 12 17l2.5-1.5"/></svg>Commencer la révision</a>'
        ty_intro = f"Une révision unique et complète de tous les points de grammaire de {level_code} &mdash; tous les exercices de toutes les leçons, mélangés."
    else:
        ty_body = ""
        ty_intro = "Disponible une fois que les leçons de ce niveau seront publiées."

    ty_section = f"""<section id="test-yourself" class="section section--tight" aria-labelledby="ty-heading">
        <div class="section__inner">
            <div class="section__head">
                <p class="eyebrow">{level_code}</p>
                <h2 id="ty-heading">Teste-toi</h2>
                <p>{ty_intro}</p>
            </div>
            {ty_body}
        </div>
    </section>"""

    out = []
    out.append(site_chrome.head(REL, title, description, extra_css=["exercises", "lessons"]))
    out.append(site_chrome.header(REL, level_code, breadcrumb, active_top="levels"))
    out.append(page_header)
    out.append(toc)
    out.append(overview_section)
    out.append(lessons_section)
    out.append(ty_section)
    out.append(vocab_section(level_code, level_slug))
    out.append(reading_section(level_code, level_slug))
    out.append(listening_section(level_code))
    out.append(writing_speaking_section(level_code))
    out.append(site_chrome.footer(REL, extra_scripts=["exercises.js", "mastery.js"]))

    out_path = REPO_ROOT / "levels" / f"{level_slug}.html"
    out_path.write_text("\n".join(out), encoding="utf-8")
    print(f"Built {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    for code, slug in [("Pre-A1", "pre-a1"), ("A1", "a1"), ("A2", "a2"), ("B1", "b1"), ("B2", "b2"), ("C1", "c1"), ("C2", "c2")]:
        build(code, slug)
