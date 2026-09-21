# Schéma de données du curriculum

Source unique de vérité pour le contenu des leçons. Chaque leçon est un
fichier JSON dans `curriculum/{niveau}/{leçon-id}.json`, généré depuis des
données Python écrites à la main dans `scripts/curriculum_source/{niveau}.py`
par `scripts/generate_curriculum.py` — modifie le Python, pas le JSON
directement (une régénération l'écraserait). `curriculum/index.json` liste
les leçons de chaque niveau dans l'ordre et est aussi généré, pas édité à la
main.

Ce schéma est le frère de `curriculum/SCHEMA.md` du cours d'espagnol, du
cours d'anglais et du cours d'italien, avec une différence délibérée : les
exemples sont des **strings simples en français**, pas des objets bilingues
`{"it": ..., "en": ...}` comme dans le cours italien. Ce cours est
d'immersion totale — l'étudiant ne voit jamais une traduction comme béquille
dans le contenu de la leçon ; le sens se transmet par des paraphrases plus
simples en français, le contexte et les exercices eux-mêmes. En cela, il
coïncide avec le cours d'anglais et le cours d'espagnol (également
monolingues). Comme le cours italien, il n'existe pas non plus de
`prerequisites`/`related`/`sourceMaterial` (pas de matériel source en
docx/pdf pour ce cours — chaque leçon a été écrite directement), et tous les
niveaux (Pre-A1 inclus) passent par le même pipeline — il n'y a pas
d'exception de HTML écrit à la main pour aucun niveau.

## Forme du JSON d'une leçon

```jsonc
{
  "id": "b1-subjonctif-present-formation",  // correspond au nom du fichier généré
  "level": "B1",
  "unit": "1",                        // unité de curriculum/index.json à laquelle elle appartient (toujours "1" pour l'instant — une unité par niveau)
  "order": 6,                         // position au sein du niveau
  "skill": "grammar",                 // grammar | vocabulary | pronunciation | reading
                                       // | listening | speaking | writing | functional
  "strand": "subjonctif",             // regroupement libre, uniquement informatif
  "title": "Le Présent du Subjonctif — Formation",
  "subtitle": "Comment se forme le mode qui exprime le souhait, le doute et l'émotion en français.",
  "objectives": ["...", "..."],
  "content": {
    "intro": "Un court paragraphe, à côté de la carte des objectifs.",
    "explanation": "<p>...</p>",      // optionnel ; HTML en ligne (strong/em/p), affiché tel quel (fiable)
    "rules": [ { "heading": "a) ...", "body": "<p>...</p> ou <ul>...</ul>" }, ... ],  // affiché tel quel (fiable)
    "table": "<div class=\"table-scroll\">...</div>",  // optionnel, un bloc de tableau de référence complet, tel quel
    "examples": [ "J'espère que tu passes une bonne journée.", "..." ],  // strings simples en français, avec échappement HTML
    "commonMistakes": [ { "wrong": "...", "right": "...", "why": "..." }, ... ]
  },
  "exercises": [ /* objets conformes au schéma de assets/js/exercises.js — voir le commentaire d'en-tête de ce fichier pour le schéma complet par type */ ],
  "summary": ["Une idée clé par ligne", "..."]
}
```

`rules[].body`, `content.explanation` et `content.table` sont du HTML fiable,
sans échappement (n'y mets rien que tu n'aies pas écrit toi-même), en suivant
les balises déjà stylées par exercises.js/lessons.css (`<p>`, `<ul>/<li>`,
`<strong>`, `<em>`, `<div class="table-scroll"><table class="ref-table">`).
Tout le reste (title, subtitle, objectives, examples, commonMistakes,
summary) reçoit un échappement HTML automatique dans
`scripts/build_lesson.py` — utilise du texte brut là, y compris des
caractères Unicode littéraux comme `→` ou `—` plutôt que des entités HTML
comme `&rarr;`/`&mdash;` (une entité dans un champ échappé serait encodée
deux fois et apparaîtrait littéralement comme `&rarr;` sur la page).

## Forme de `curriculum/index.json`

```jsonc
{
  "levels": {
    "B1": {
      "overview": "Un paragraphe affiché sur la page hub de B1.",
      "units": [
        { "id": "1", "title": "Grammaire B1", "lessons": [ { "id": "b1-subjonctif-present-formation", "status": "published" }, ... ] }
      ]
    }
  }
}
```

## Schéma des items de `exercises` (contrat exact de `assets/js/exercises.js`)

Chaque bloc d'exercice : `{ "id", "type", "title", "instructions"?, "passage"?, "items": [...] }`.
`type` est l'un de `multiple-choice`, `true-false`, `fill-blank`, `matching`,
`ordering`, `correction`, `typing`, `reading-comprehension`, `vocabulary`,
`writing`. La forme de chaque `item` selon le `type` du bloc :

- **multiple-choice / vocabulary / reading-comprehension** : `{ "id", "prompt", "options": [...], "answerIndex", "explanation" }`
- **true-false** : `{ "id", "statement", "answer": true|false, "explanation" }`
- **fill-blank** : `{ "id", "prompt" (utilise `___` pour chaque espace), "answers": [["rép1","rép2"], ...] (un tableau par espace, avec les variantes acceptées), "options"? (tableau d'options par espace, pour afficher un `<select>`), "explanation" }`
- **correction** : `{ "id", "incorrect", "answer": ["..."], "explanation" }`
- **typing** : `{ "id", "prompt", "answer"?: ["..."] (si omis, autoévaluation sans notation), "modelAnswer"?, "explanation" }`
- **matching** : `{ "id", "prompt"?, "pairs": [ {"left":"...", "right":"..."}, ... ], "explanation" }`
- **ordering** : `{ "id", "prompt", "words": [...] (ordre correct), "explanation" }`
- **writing** : `{ "id", "prompt" }` — autoévaluation uniquement, sans notation automatique.

`explanation` s'affiche toujours après la notation, que la réponse soit
correcte ou non — écris-la comme une règle ou une courte raison dont
l'étudiant peut apprendre, pas seulement « Bonne réponse. »

## Build

```bash
python3 scripts/build_all.py
```

Exécute le pipeline complet dans l'ordre : `generate_curriculum.py` (Python →
JSON) → `build_nav_map.py` → `build_lesson.py` (chaque JSON de leçon → sa
page HTML, en réutilisant le chrome partagé de `scripts/site_chrome.py`) →
`build_level_pages.py` (les sept pages hub de niveau) →
`build_test_yourself.py` (pages de révision mixte par niveau) →
`build_exercise_index.py` (recherche d'items pour la répétition espacée) →
`build_search_index.py` (recherche du site) → `build_static_pages.py`
(accueil, exercices, extras, dictionnaire, verbes irréguliers, test de
niveau, progression, révision du jour, examens blancs).
