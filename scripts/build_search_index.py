#!/usr/bin/env python3
"""
Build assets/data/search-index.json: the flat array assets/js/search.js
fetches once and filters entirely client-side. Entry shape:
{ type, level, title, desc, url, keywords[] } — see search.js's
TYPE_LABEL map for valid `type` values (level, lesson, grammar, exercise,
mock, extra).

Usage:
    python3 scripts/build_search_index.py
"""
import json
import glob
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

LEVEL_ENTRIES = [
    ("Pre-A1", "pre-a1", "Survie", "L'alphabet et les sons, les salutations, les nombres, le vocabulaire essentiel de survie."),
    ("A1", "a1", "Débutant", "Être et avoir, genre et articles, présent de l'indicatif, salutations quotidiennes."),
    ("A2", "a2", "Élémentaire", "Passé composé et imparfait, verbes pronominaux, pronoms compléments d'objet direct."),
    ("B1", "b1", "Intermédiaire", "Présent du subjonctif, pronoms combinés, futur, conditionnel, impératif."),
    ("B2", "b2", "Intermédiaire avancé", "Subjonctif passé, phrases conditionnelles avec si, voix passive, discours indirect."),
    ("C1", "c1", "Avancé", "Subjonctif plus-que-parfait, conditionnelles complexes, nuances du subjonctif, registre formel."),
    ("C2", "c2", "Maîtrise", "Syntaxe complexe, registre littéraire, nuances lexicales, cohésion du discours."),
]

STATIC_ENTRIES = [
    {"type": "extra", "level": "", "title": "Exercices", "desc": "Pratique supplémentaire de lecture et de vocabulaire, indépendante du niveau.",
     "url": "exercises.html", "keywords": ["lecture", "pratique", "vocabulaire"]},
    {"type": "mock", "level": "", "title": "Examens Blancs", "desc": "Sections d'examen blanc dans le style DELF/DALF, avec feuille de réponses.",
     "url": "simulated-exams.html", "keywords": ["delf", "dalf", "tcf", "tef", "examen"]},
    {"type": "extra", "level": "", "title": "Extras", "desc": "Culture francophone, expressions courantes, et usage formel face à informel.",
     "url": "extras.html", "keywords": ["culture", "expressions", "tu", "vous", "formel", "informel"]},
    {"type": "grammar", "level": "", "title": "Dictionnaire et Référence", "desc": "Cherche n'importe quel mot français dans plusieurs dictionnaires monolingues.",
     "url": "dictionary.html", "keywords": ["larousse", "robert", "wiktionnaire", "academie"]},
    {"type": "grammar", "level": "", "title": "Verbes Irréguliers", "desc": "Tableau de référence des verbes irréguliers les plus courants du français.",
     "url": "irregular-verbs.html", "keywords": ["etre", "avoir", "aller", "faire", "conjugaison"]},
    {"type": "extra", "level": "", "title": "Test de Niveau", "desc": "Un test rapide pour découvrir à quel niveau du CECR commencer.",
     "url": "placement-test.html", "keywords": ["test de niveau", "quel est mon niveau"]},
    {"type": "extra", "level": "", "title": "Révision du Jour", "desc": "Révision par répétition espacée des items que tu as ratés auparavant.",
     "url": "today-review.html", "keywords": ["repetition espacee", "revision", "maitrise"]},
]


def main():
    entries = []
    for code, slug, name, desc in LEVEL_ENTRIES:
        entries.append({
            "type": "level", "level": code, "title": f"{code} — {name}",
            "desc": desc, "url": f"levels/{slug}.html", "keywords": [name.lower()],
        })
        entries.append({
            "type": "grammar", "level": code, "title": f"Teste-toi : {code}",
            "desc": f"Révision mixte de tous les points de grammaire de {code}, avec un retour instantané.",
            "url": f"levels/{slug}/test-yourself.html", "keywords": ["revision", "test"],
        })

    files = sorted(glob.glob(str(REPO_ROOT / "curriculum" / "*" / "*.json")))
    for fpath in files:
        lesson = json.loads(Path(fpath).read_text(encoding="utf-8"))
        level = lesson.get("level", "")
        slug = level.lower()
        prefix = slug + "-"
        lesson_id = lesson.get("id", "")
        file_slug = lesson_id[len(prefix):] if lesson_id.startswith(prefix) else lesson_id
        entries.append({
            "type": "lesson",
            "level": level,
            "title": lesson.get("title", ""),
            "desc": lesson.get("subtitle", ""),
            "url": f"levels/{slug}/{file_slug}.html",
            "keywords": [lesson.get("strand", ""), lesson.get("skill", "")],
        })

    entries.extend(STATIC_ENTRIES)

    out_path = REPO_ROOT / "assets" / "data" / "search-index.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(entries, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    print(f"Wrote {len(entries)} search entries -> {out_path.relative_to(REPO_ROOT)}")


if __name__ == "__main__":
    main()
