# -*- coding: utf-8 -*-
"""A2 — Données du curriculum de niveau élémentaire. Voir curriculum/SCHEMA.md
pour la forme exacte du JSON vers lequel ceci est compilé (scripts/generate_curriculum.py
fait la compilation). Écrit en Python plutôt qu'en JSON à la main pour que le
HTML en ligne (rules[].body, content.explanation) et les guillemets dans le
texte puissent s'écrire naturellement."""

OVERVIEW = (
    "Le niveau A2 te donne les outils pour parler du passé, du futur et faire "
    "des comparaisons, en plus de remplacer des noms par des pronoms pour "
    "sonner plus naturel. Tu apprendras le passé composé et l'imparfait — et "
    "surtout quand utiliser chacun —, le futur simple, les comparatifs et "
    "les superlatifs, les pronoms compléments d'objet direct et indirect, "
    "les verbes pronominaux, l'impératif pour donner des ordres et des "
    "instructions, le conditionnel présent, les indéfinis, les pronoms y et "
    "en, et les prépositions avec les pays et les villes. À la fin de ce "
    "niveau, tu pourras raconter ce que tu as fait hier, décrire comment "
    "était quelque chose dans le passé, faire des projets et donner des "
    "instructions simples."
)

LESSONS = [
    {
        "id": "a2-le-passe-compose",
        "level": "A2", "unit": "1", "order": 1, "skill": "grammar", "strand": "passe-compose",
        "title": "Le Passé Composé",
        "subtitle": "Comment former le passé composé avec avoir et avec être, et accorder le participe passé.",
        "objectives": [
            "Former le passé composé avec avoir pour la majorité des verbes.",
            "Reconnaître les verbes qui se conjuguent avec être (verbes de mouvement et quelques autres).",
            "Accorder le participe passé avec le sujet pour les verbes construits avec être.",
        ],
        "content": {
            "intro": "Le passé composé est le temps le plus utilisé à l'oral pour parler d'un événement terminé dans le passé — c'est la première étape indispensable pour raconter ce que tu as fait.",
            "explanation": "<p>La plupart des verbes forment leur passé composé avec l'auxiliaire <strong>avoir</strong> + participe passé : <em>j'ai parlé, tu as fini, il a vendu</em>. Un petit groupe de verbes, souvent appelés les verbes de la « maison d'être » (<em>aller/venir, arriver/partir, entrer/sortir, monter/descendre, naître/mourir, rester, tomber</em>, et leurs composés comme <em>revenir, rentrer</em>), utilisent <strong>être</strong> comme auxiliaire.</p><p>Avec être, le participe passé s'accorde en genre et en nombre avec le sujet, comme un adjectif : <em>elle est allée, ils sont partis, elles sont parties</em>. Avec avoir, le participe passé ne s'accorde pas avec le sujet à ce niveau.</p>",
            "rules": [
                {"heading": "a) Passé composé avec avoir", "body": "<ul><li>sujet + avoir (présent) + participe passé — <em>j'ai parlé, tu as fini, il a vendu</em>.</li></ul>"},
                {"heading": "b) Les verbes de la « maison d'être »", "body": "<ul><li><em>aller/venir, arriver/partir, entrer/sortir, monter/descendre, naître/mourir, rester, tomber</em>, et leurs composés (<em>revenir, rentrer, retourner</em>).</li></ul>"},
                {"heading": "c) Accord avec être", "body": "<ul><li>Le participe passé s'accorde avec le sujet : <em>elle est partie, ils sont venus, elles sont nées</em>.</li></ul>"},
                {"heading": "d) Formation du participe passé", "body": "<ul><li>-er → -é (<em>parlé</em>), -ir → -i (<em>fini</em>), -re → -u (<em>vendu</em>).</li><li>Irréguliers fréquents : <em>être → été, avoir → eu, faire → fait, prendre → pris</em>.</li></ul>"},
            ],
            "examples": [
                "J'ai mangé une pomme ce matin.",
                "Elle est allée au marché hier.",
                "Nous avons fini nos devoirs.",
                "Ils sont partis très tôt.",
                "Tu as pris le bus ce matin ?",
                "Elle est née à Lyon en 1998.",
                "Vous avez fait vos valises ?",
            ],
            "commonMistakes": [
                {"wrong": "Elle a née à Lyon.", "right": "Elle est née à Lyon.", "why": "Naître fait partie des verbes qui se conjuguent avec être, pas avoir."},
                {"wrong": "Ils sont allé au cinéma.", "right": "Ils sont allés au cinéma.", "why": "Avec être, le participe passé s'accorde avec le sujet ; ici, il faut le -s du pluriel."},
                {"wrong": "Nous avons parti tôt.", "right": "Nous sommes partis tôt.", "why": "Partir se conjugue avec être, pas avoir."},
            ],
        },
        "exercises": [
            {"id": "a2pc-fill", "type": "fill-blank", "title": "Conjugue au Passé Composé",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "a2pcf1", "prompt": "Hier, je ___ (manger) au restaurant.", "answers": [["ai mangé"]], "options": ["ai mangé", "suis mangé", "a mangé"], "explanation": "Manger se conjugue avec avoir : j'ai mangé."},
                {"id": "a2pcf2", "prompt": "Elle ___ (aller) à l'école à pied.", "answers": [["est allée"]], "options": ["est allée", "a allé", "est allé"], "explanation": "Aller se conjugue avec être, et le participe s'accorde au féminin : allée."},
                {"id": "a2pcf3", "prompt": "Nous ___ (finir) le projet hier soir.", "answers": [["avons fini"]], "options": ["avons fini", "sommes fini", "avons finit"], "explanation": "Finir se conjugue avec avoir : nous avons fini."},
                {"id": "a2pcf4", "prompt": "Ils ___ (partir) tôt ce matin.", "answers": [["sont partis"]], "options": ["sont partis", "ont parti", "sont parti"], "explanation": "Partir se conjugue avec être, et le participe s'accorde au masculin pluriel : partis."},
             ]},
            {"id": "a2pc-mc", "type": "multiple-choice", "title": "Avoir ou Être ?",
             "items": [
                {"id": "a2pcm1", "prompt": "Quel auxiliaire utilise-t-on avec aller ?", "options": ["être", "avoir", "les deux"], "answerIndex": 0, "explanation": "Aller fait partie des verbes de la « maison d'être »."},
                {"id": "a2pcm2", "prompt": "Comment accorde-t-on le participe passé avec être ?", "options": ["Comme un adjectif, selon le genre et le nombre du sujet", "Il ne s'accorde jamais", "Seulement au pluriel"], "answerIndex": 0, "explanation": "Avec être, le participe passé fonctionne comme un adjectif accordé au sujet."},
                {"id": "a2pcm3", "prompt": "Quel est le participe passé de faire ?", "options": ["fait", "faisé", "fais"], "answerIndex": 0, "explanation": "Faire a un participe passé irrégulier : fait."},
                {"id": "a2pcm4", "prompt": "Quelle phrase est correcte ?", "options": ["Elle est allée au marché.", "Elle a allée au marché.", "Elle est allé au marché."], "answerIndex": 0, "explanation": "Aller + être, avec accord féminin du participe : allée."},
             ]},
            {"id": "a2pc-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2pcc1", "incorrect": "Elle a née à Lyon.", "answer": ["Elle est née à Lyon."], "explanation": "Naître se conjugue avec être."},
                {"id": "a2pcc2", "incorrect": "Ils sont allé au cinéma.", "answer": ["Ils sont allés au cinéma."], "explanation": "Le participe passé s'accorde au pluriel avec être."},
                {"id": "a2pcc3", "incorrect": "Nous avons parti tôt.", "answer": ["Nous sommes partis tôt."], "explanation": "Partir se conjugue avec être, pas avoir."},
             ]},
        ],
        "summary": [
            "Le passé composé se forme avec avoir ou être (présent) + participe passé.",
            "Un petit groupe de verbes (la « maison d'être ») utilise être comme auxiliaire : aller, venir, arriver, partir, entrer, sortir, monter, descendre, naître, mourir, rester, tomber, et leurs composés.",
            "Avec être, le participe passé s'accorde en genre et en nombre avec le sujet ; avec avoir, il reste invariable à ce niveau.",
        ],
    },
    {
        "id": "a2-limparfait",
        "level": "A2", "unit": "1", "order": 2, "skill": "grammar", "strand": "imparfait",
        "title": "L'Imparfait",
        "subtitle": "Comment former l'imparfait à partir du radical de nous, et quand l'utiliser.",
        "objectives": [
            "Former l'imparfait à partir du radical de la première personne du pluriel au présent.",
            "Conjuguer être à l'imparfait, seule exception de radical.",
            "Reconnaître les emplois de l'imparfait : description, habitude, action en cours.",
        ],
        "content": {
            "intro": "L'imparfait sert à décrire le décor du passé — comment c'était, ce qu'on faisait d'habitude — et se construit d'une manière très régulière, à partir d'un temps que tu connais déjà : le présent.",
            "explanation": "<p>L'imparfait se forme à partir du radical de la première personne du pluriel (<em>nous</em>) au présent, en retirant <em>-ons</em>, puis en ajoutant les terminaisons <strong>-ais, -ais, -ait, -ions, -iez, -aient</strong>, identiques pour tous les verbes : <em>nous parlons → je parlais</em> ; <em>nous finissons → je finissais</em>. Seul <strong>être</strong> a un radical irrégulier : <em>ét-</em> (<em>j'étais, tu étais, il était…</em>).</p><p>L'imparfait sert à décrire une scène ou un état dans le passé (<em>il faisait beau, le ciel était bleu</em>), une habitude répétée (<em>quand j'étais petit, je jouais dehors tous les jours</em>), ou une action en cours interrompue par une autre (<em>je regardais la télé quand le téléphone a sonné</em>).</p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>Radical de nous au présent (sans -ons) + terminaisons -ais/-ais/-ait/-ions/-iez/-aient.</li><li><em>nous finissons → je finissais, tu finissais, il finissait, nous finissions, vous finissiez, ils finissaient</em>.</li></ul>"},
                {"heading": "b) Être, seule exception", "body": "<ul><li><em>j'étais, tu étais, il était, nous étions, vous étiez, ils étaient</em> — radical ét-, pas de radical présent en -ons.</li></ul>"},
                {"heading": "c) Emplois de l'imparfait", "body": "<ul><li>Description d'une scène ou d'un état : <em>il faisait beau, elle était fatiguée</em>.</li><li>Habitude répétée dans le passé : <em>nous jouions au foot tous les samedis</em>.</li><li>Action en cours interrompue par une autre : <em>je lisais quand le téléphone a sonné</em>.</li></ul>"},
            ],
            "examples": [
                "Quand j'étais enfant, j'habitais à la campagne.",
                "Il faisait beau ce jour-là.",
                "Nous jouions au foot tous les samedis.",
                "Elle lisait un livre quand le téléphone a sonné.",
                "Vous étiez fatigués après le voyage.",
                "Ils mangeaient toujours à la même heure.",
                "Tu avais quel âge en 2010 ?",
            ],
            "commonMistakes": [
                {"wrong": "Nous parliont le samedi.", "right": "Nous parlions le samedi.", "why": "La terminaison de nous est -ions, pas -iont."},
                {"wrong": "Il a fait beau, le ciel a été bleu.", "right": "Il faisait beau, le ciel était bleu.", "why": "Pour décrire une scène ou un état continu dans le passé, on utilise l'imparfait, pas le passé composé."},
                {"wrong": "Je étais content.", "right": "J'étais content.", "why": "Je s'élide toujours en j' devant une voyelle, y compris devant étais."},
            ],
        },
        "exercises": [
            {"id": "a2im-fill", "type": "fill-blank", "title": "Conjugue à l'Imparfait",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "a2imf1", "prompt": "Quand j'étais petit, je ___ (jouer) dehors tous les jours.", "answers": [["jouais"]], "options": ["jouais", "joue", "ai joué"], "explanation": "Habitude répétée dans le passé : imparfait."},
                {"id": "a2imf2", "prompt": "Il ___ (faire) très froid ce matin-là.", "answers": [["faisait"]], "options": ["faisait", "a fait", "fait"], "explanation": "Description d'un état météo continu : imparfait."},
                {"id": "a2imf3", "prompt": "Nous ___ (être) très jeunes à l'époque.", "answers": [["étions"]], "options": ["étions", "sommes", "avons été"], "explanation": "Être à l'imparfait a un radical irrégulier : ét-."},
                {"id": "a2imf4", "prompt": "Vous ___ (habiter) où avant de déménager ?", "answers": [["habitiez"]], "options": ["habitiez", "habitez", "avez habité"], "explanation": "Terminaison -iez pour vous à l'imparfait."},
             ]},
            {"id": "a2im-mc", "type": "multiple-choice", "title": "L'Imparfait : Formation et Emploi",
             "items": [
                {"id": "a2imm1", "prompt": "À partir de quel radical forme-t-on l'imparfait ?", "options": ["le radical de nous au présent", "l'infinitif", "le radical de je au présent"], "answerIndex": 0, "explanation": "On retire -ons du radical de nous au présent."},
                {"id": "a2imm2", "prompt": "Quel verbe a un radical irrégulier à l'imparfait ?", "options": ["être", "parler", "finir"], "answerIndex": 0, "explanation": "Être utilise le radical ét-, qui ne vient pas de la forme nous du présent."},
                {"id": "a2imm3", "prompt": "Quel emploi correspond à l'imparfait ?", "options": ["décrire une habitude passée", "annoncer un événement ponctuel terminé", "parler du futur"], "answerIndex": 0, "explanation": "L'imparfait décrit des habitudes, des descriptions et des actions en cours dans le passé."},
                {"id": "a2imm4", "prompt": "Quelle terminaison correspond à nous à l'imparfait ?", "options": ["-ions", "-iont", "-ons"], "answerIndex": 0, "explanation": "La terminaison de nous à l'imparfait est -ions."},
             ]},
            {"id": "a2im-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2imc1", "incorrect": "Nous parliont tous les jours.", "answer": ["Nous parlions tous les jours."], "explanation": "La terminaison correcte de nous est -ions."},
                {"id": "a2imc2", "incorrect": "Il a fait très beau ce jour-là, toute la journée.", "answer": ["Il faisait très beau ce jour-là, toute la journée."], "explanation": "Une description continue dans le passé utilise l'imparfait."},
                {"id": "a2imc3", "incorrect": "Je étais fatigué hier soir.", "answer": ["J'étais fatigué hier soir."], "explanation": "Je s'élide en j' devant une voyelle."},
             ]},
        ],
        "summary": [
            "L'imparfait se forme à partir du radical de nous au présent (sans -ons) + -ais/-ais/-ait/-ions/-iez/-aient.",
            "Être est la seule exception de radical : j'étais, tu étais, il était…",
            "L'imparfait décrit une scène, un état ou une habitude dans le passé, ou une action en cours interrompue par une autre.",
        ],
    },
    {
        "id": "a2-passe-compose-vs-imparfait",
        "level": "A2", "unit": "1", "order": 3, "skill": "grammar", "strand": "passe-compose-imparfait",
        "title": "Passé Composé vs. Imparfait",
        "subtitle": "Comment choisir entre les deux temps du passé selon le sens de la phrase.",
        "objectives": [
            "Distinguer une action ponctuelle et terminée (passé composé) d'une description ou d'une habitude (imparfait).",
            "Reconnaître le schéma classique : une scène à l'imparfait interrompue par un événement au passé composé.",
            "Employer les deux temps ensemble dans un même récit.",
        ],
        "content": {
            "intro": "C'est la question que se posent tous les débutants en racontant une histoire au passé : passé composé ou imparfait ? La réponse dépend toujours du sens que tu veux donner à l'action, jamais d'une règle de forme.",
            "explanation": "<p>Le <strong>passé composé</strong> raconte un événement ponctuel, terminé, qui fait avancer l'histoire : <em>Hier, je suis sorti, j'ai rencontré un ami, nous avons dîné ensemble.</em> Chaque verbe correspond à une étape précise de l'histoire. L'<strong>imparfait</strong>, lui, décrit le décor autour de ces événements : l'heure, le temps qu'il faisait, l'état d'esprit des personnes, une habitude.</p><p>Le schéma le plus fréquent combine les deux : une scène installée à l'imparfait, interrompue par un événement au passé composé — <em>Je dormais (imparfait) quand le téléphone a sonné (passé composé).</em> Dans ce type de phrase, imparfait et passé composé ne sont jamais interchangeables : chacun a un rôle précis.</p>",
            "rules": [
                {"heading": "a) Passé composé : l'action", "body": "<ul><li>Événement ponctuel, terminé, qui fait avancer le récit : <em>il est arrivé, elle a téléphoné, nous avons mangé</em>.</li></ul>"},
                {"heading": "b) Imparfait : le décor", "body": "<ul><li>Description, état, habitude, action en cours : <em>il faisait nuit, elle était contente, nous mangions toujours à huit heures</em>.</li></ul>"},
                {"heading": "c) Le schéma scène + interruption", "body": "<ul><li>Imparfait (scène/décor) + passé composé (événement soudain) : <em>Je dormais quand le téléphone a sonné.</em></li></ul>"},
                {"heading": "d) Un repère pratique", "body": "<ul><li>Si tu peux dire « à ce moment précis, il s'est passé quelque chose » → passé composé.</li><li>Si tu décris « comment c'était » ou « ce qu'on faisait d'habitude » → imparfait.</li></ul>"},
            ],
            "examples": [
                "Je dormais quand le téléphone a sonné.",
                "Il faisait beau, alors nous sommes sortis.",
                "Elle regardait la télé quand ses parents sont rentrés.",
                "Quand j'étais petit, nous allions à la plage chaque été.",
                "Hier, il a plu toute la journée.",
                "Nous étions fatigués, donc nous sommes rentrés tôt.",
                "Pendant qu'il cuisinait, elle a mis la table.",
            ],
            "commonMistakes": [
                {"wrong": "Je dormais quand le téléphone sonnait.", "right": "Je dormais quand le téléphone a sonné.", "why": "L'événement soudain qui interrompt la scène doit être au passé composé, pas à l'imparfait."},
                {"wrong": "Hier, il faisait très beau toute la journée, alors nous avons sorti à la plage. (les deux verbes à l'imparfait)", "right": "Hier, il a fait très beau toute la journée, alors nous sommes sortis à la plage.", "why": "Un fait ponctuel annoncé avec « hier » est souvent au passé composé, même s'il dure toute la journée."},
                {"wrong": "Quand j'étais petit, nous sommes allés à la plage chaque été.", "right": "Quand j'étais petit, nous allions à la plage chaque été.", "why": "Une habitude répétée (« chaque été ») se raconte à l'imparfait, pas au passé composé."},
            ],
        },
        "exercises": [
            {"id": "a2vi-fill", "type": "fill-blank", "title": "Choisis le Bon Temps",
             "instructions": "Complète avec le passé composé ou l'imparfait du verbe entre parenthèses.",
             "items": [
                {"id": "a2vif1", "prompt": "Je ___ (dormir) quand le téléphone a sonné.", "answers": [["dormais"]], "options": ["dormais", "ai dormi", "dors"], "explanation": "La scène en cours au moment de l'interruption est à l'imparfait."},
                {"id": "a2vif2", "prompt": "Hier soir, nous ___ (manger) au restaurant.", "answers": [["avons mangé"]], "options": ["avons mangé", "mangions", "mangeons"], "explanation": "Événement ponctuel terminé, daté par « hier soir » : passé composé."},
                {"id": "a2vif3", "prompt": "Quand j'étais enfant, je ___ (jouer) dehors tous les jours.", "answers": [["jouais"]], "options": ["jouais", "ai joué", "joue"], "explanation": "Habitude répétée dans le passé : imparfait."},
                {"id": "a2vif4", "prompt": "Il ___ (pleuvoir) quand nous sommes sortis.", "answers": [["pleuvait"]], "options": ["pleuvait", "a plu", "pleut"], "explanation": "Description du temps qu'il faisait au moment de l'action : imparfait."},
             ]},
            {"id": "a2vi-mc", "type": "multiple-choice", "title": "Passé Composé ou Imparfait ?",
             "items": [
                {"id": "a2vim1", "prompt": "Quel temps décrit le décor, l'état ou l'habitude ?", "options": ["l'imparfait", "le passé composé", "les deux également"], "answerIndex": 0, "explanation": "L'imparfait sert à décrire, pas à faire avancer l'action."},
                {"id": "a2vim2", "prompt": "Quel temps fait avancer les événements d'un récit ?", "options": ["le passé composé", "l'imparfait", "aucun des deux"], "answerIndex": 0, "explanation": "Le passé composé raconte les étapes successives d'une histoire."},
                {"id": "a2vim3", "prompt": "Dans « Je lisais quand elle est arrivée », quel verbe est l'événement soudain ?", "options": ["est arrivée", "lisais", "les deux"], "answerIndex": 0, "explanation": "L'arrivée est l'événement ponctuel qui interrompt la scène en cours."},
                {"id": "a2vim4", "prompt": "Comment raconter une habitude répétée dans le passé (« chaque été ») ?", "options": ["à l'imparfait", "au passé composé", "au futur"], "answerIndex": 0, "explanation": "Une répétition habituelle dans le passé se raconte à l'imparfait."},
             ]},
            {"id": "a2vi-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2vic1", "incorrect": "Je dormais quand le téléphone sonnait.", "answer": ["Je dormais quand le téléphone a sonné."], "explanation": "L'événement soudain doit être au passé composé."},
                {"id": "a2vic2", "incorrect": "Quand j'étais petit, nous sommes allés à la plage chaque été.", "answer": ["Quand j'étais petit, nous allions à la plage chaque été."], "explanation": "Une habitude répétée se raconte à l'imparfait."},
                {"id": "a2vic3", "incorrect": "Hier, nous mangions au restaurant.", "answer": ["Hier, nous avons mangé au restaurant."], "explanation": "Un événement ponctuel daté par « hier » est au passé composé."},
             ]},
        ],
        "summary": [
            "Le passé composé raconte des événements ponctuels et terminés qui font avancer le récit ; l'imparfait décrit le décor, l'état ou l'habitude.",
            "Le schéma le plus fréquent combine une scène à l'imparfait interrompue par un événement au passé composé.",
            "Le choix dépend toujours du sens voulu, jamais d'une règle de forme fixe.",
        ],
    },
    {
        "id": "a2-le-futur-simple",
        "level": "A2", "unit": "1", "order": 4, "skill": "grammar", "strand": "futur-simple",
        "title": "Le Futur Simple",
        "subtitle": "Comment former le futur simple, et les principaux radicaux irréguliers à connaître.",
        "objectives": [
            "Former le futur simple des verbes réguliers à partir de l'infinitif.",
            "Mémoriser les radicaux irréguliers des verbes les plus fréquents.",
            "Distinguer le futur simple du futur proche par leur usage.",
        ],
        "content": {
            "intro": "Le futur simple sert à parler de projets plus lointains, de promesses et de prédictions — un temps formé simplement, mais avec quelques radicaux irréguliers indispensables à mémoriser.",
            "explanation": "<p>Pour les verbes réguliers, le futur simple se forme en ajoutant les terminaisons <strong>-ai, -as, -a, -ons, -ez, -ont</strong> directement à l'infinitif (les verbes en -re perdent leur -e final) : <em>je parlerai, tu finiras, il vendra</em>. Ces terminaisons sont les mêmes pour tous les verbes, réguliers ou non.</p><p>Certains verbes très fréquents ont un radical irrégulier, à mémoriser directement : <em>être → ser-, avoir → aur-, aller → ir-, faire → fer-, pouvoir → pourr-, vouloir → voudr-, devoir → devr-, venir → viendr-</em>. Les terminaisons, elles, restent toujours régulières.</p>",
            "rules": [
                {"heading": "a) Formation régulière", "body": "<ul><li>Infinitif (verbes en -re : sans le -e final) + -ai/-as/-a/-ons/-ez/-ont.</li><li><em>je parlerai, tu finiras, il vendra, nous parlerons, vous finirez, ils vendront</em>.</li></ul>"},
                {"heading": "b) Radicaux irréguliers fréquents", "body": "<ul><li><em>être → ser-, avoir → aur-, aller → ir-, faire → fer-</em>.</li><li><em>pouvoir → pourr-, vouloir → voudr-, devoir → devr-, venir → viendr-</em>.</li></ul>"},
                {"heading": "c) Terminaisons toujours régulières", "body": "<ul><li>Même pour un radical irrégulier, les terminaisons ne changent jamais : <em>je serai, j'aurai, j'irai, je ferai</em>.</li></ul>"},
                {"heading": "d) Futur simple vs. futur proche", "body": "<ul><li>Futur proche (aller + infinitif) : projet proche ou décidé — <em>je vais partir demain</em>.</li><li>Futur simple : projet plus lointain, promesse, prédiction — <em>je partirai l'année prochaine</em>.</li></ul>"},
            ],
            "examples": [
                "Je parlerai avec elle demain.",
                "Tu finiras tes études l'année prochaine.",
                "Il sera médecin un jour.",
                "Nous irons en France cet été.",
                "Vous pourrez venir avec nous.",
                "Ils devront travailler plus.",
                "Elle viendra nous voir bientôt.",
            ],
            "commonMistakes": [
                {"wrong": "Je serais content de te voir. (confondu avec le futur simple je serai)", "right": "Je serai content de te voir.", "why": "Le futur simple (je serai) et le conditionnel (je serais) se prononcent presque pareil mais s'écrivent différemment ; ici, c'est une simple annonce future."},
                {"wrong": "Il vas venir demain.", "right": "Il viendra demain.", "why": "Le radical futur de venir est viendr-, pas une forme de aller."},
                {"wrong": "Nous ferons parlerons français ensemble. (mauvais radical)", "right": "Nous parlerons français ensemble.", "why": "Parler est un verbe régulier : le radical est l'infinitif complet, parler-."},
            ],
        },
        "exercises": [
            {"id": "a2fs-fill", "type": "fill-blank", "title": "Conjugue au Futur Simple",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "a2fsf1", "prompt": "Demain, je ___ (parler) avec le directeur.", "answers": [["parlerai"]], "options": ["parlerai", "parlerais", "parle"], "explanation": "Futur simple régulier : infinitif + -ai."},
                {"id": "a2fsf2", "prompt": "L'année prochaine, nous ___ (aller) en Italie.", "answers": [["irons"]], "options": ["irons", "allons", "irions"], "explanation": "Aller a un radical irrégulier au futur : ir-."},
                {"id": "a2fsf3", "prompt": "Elle ___ (être) très contente de te revoir.", "answers": [["sera"]], "options": ["sera", "serait", "est"], "explanation": "Être a un radical irrégulier au futur : ser-."},
                {"id": "a2fsf4", "prompt": "Vous ___ (pouvoir) m'aider samedi ?", "answers": [["pourrez"]], "options": ["pourrez", "pouvez", "pourriez"], "explanation": "Pouvoir a un radical irrégulier au futur : pourr-."},
             ]},
            {"id": "a2fs-mc", "type": "multiple-choice", "title": "Radicaux du Futur",
             "items": [
                {"id": "a2fsm1", "prompt": "Quel est le radical futur de faire ?", "options": ["fer-", "fais-", "fair-"], "answerIndex": 0, "explanation": "Faire a un radical futur irrégulier : fer-."},
                {"id": "a2fsm2", "prompt": "Quelles terminaisons utilise-t-on au futur simple ?", "options": ["-ai/-as/-a/-ons/-ez/-ont", "-e/-es/-e/-ons/-ez/-ent", "-ais/-ais/-ait/-ions/-iez/-aient"], "answerIndex": 0, "explanation": "Ce sont les terminaisons propres au futur simple, identiques pour tous les verbes."},
                {"id": "a2fsm3", "prompt": "Quel est le radical futur de venir ?", "options": ["viendr-", "venir-", "vien-"], "answerIndex": 0, "explanation": "Venir a un radical futur irrégulier : viendr-."},
                {"id": "a2fsm4", "prompt": "Quand utilise-t-on plutôt le futur simple que le futur proche ?", "options": ["pour un projet plus lointain ou une prédiction", "pour un projet déjà décidé pour demain", "seulement à l'écrit"], "answerIndex": 0, "explanation": "Le futur simple convient aux projets lointains, promesses et prédictions."},
             ]},
            {"id": "a2fs-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2fsc1", "incorrect": "Il vas venir demain.", "answer": ["Il viendra demain."], "explanation": "Venir a un radical futur irrégulier : viendr-."},
                {"id": "a2fsc2", "incorrect": "Nous aurrons le temps ce week-end.", "answer": ["Nous aurons le temps ce week-end."], "explanation": "Avoir a un seul r au radical futur : aur-."},
                {"id": "a2fsc3", "incorrect": "Elle sera contente si tu viens, elle disait.", "answer": ["Elle sera contente si tu viens, elle dit."], "explanation": "Ce mélange de temps n'est pas nécessaire ici ; garder le présent dit avec le futur sera."},
             ]},
        ],
        "summary": [
            "Le futur simple régulier ajoute -ai/-as/-a/-ons/-ez/-ont à l'infinitif (sans le -e final pour les verbes en -re).",
            "Des verbes très fréquents ont un radical futur irrégulier à mémoriser : être→ser-, avoir→aur-, aller→ir-, faire→fer-, pouvoir→pourr-, vouloir→voudr-, devoir→devr-, venir→viendr-.",
            "Le futur simple annonce des projets plus lointains, des promesses ou des prédictions ; le futur proche annonce des projets décidés et proches.",
        ],
    },
    {
        "id": "a2-les-comparatifs-et-superlatifs",
        "level": "A2", "unit": "1", "order": 5, "skill": "grammar", "strand": "comparatifs",
        "title": "Les Comparatifs et Superlatifs",
        "subtitle": "Plus...que, moins...que, aussi...que, le/la/les plus/moins, et les formes irrégulières meilleur/mieux.",
        "objectives": [
            "Former le comparatif de supériorité, d'infériorité et d'égalité.",
            "Former le superlatif avec le/la/les plus/moins.",
            "Utiliser les formes irrégulières bon → meilleur et bien → mieux.",
        ],
        "content": {
            "intro": "Comparer deux personnes, deux choses ou une chose à tout un groupe est une compétence essentielle du niveau A2, avec une structure simple et deux exceptions à retenir absolument.",
            "explanation": "<p>Pour comparer deux éléments, le français utilise <strong>plus…que</strong> (supériorité), <strong>moins…que</strong> (infériorité) et <strong>aussi…que</strong> (égalité), placés autour de l'adjectif ou de l'adverbe : <em>Paul est plus grand que Marie. Elle court aussi vite que lui.</em></p><p>Le <strong>superlatif</strong> se forme avec <em>le/la/les</em> + <em>plus/moins</em> + adjectif, accordé avec le nom : <em>C'est le plus grand bâtiment de la ville.</em> Deux formes sont irrégulières et ne suivent pas ce schéma : l'adjectif <strong>bon</strong> devient <strong>meilleur</strong> (jamais « plus bon »), et l'adverbe <strong>bien</strong> devient <strong>mieux</strong> (jamais « plus bien »).</p>",
            "rules": [
                {"heading": "a) Comparatif", "body": "<ul><li><strong>plus…que</strong> — supériorité : <em>plus grand que</em>.</li><li><strong>moins…que</strong> — infériorité : <em>moins cher que</em>.</li><li><strong>aussi…que</strong> — égalité : <em>aussi vite que</em>.</li></ul>"},
                {"heading": "b) Superlatif", "body": "<ul><li><em>le/la/les</em> + plus/moins + adjectif, accordé avec le nom : <em>la plus grande ville, les plus beaux jardins</em>.</li></ul>"},
                {"heading": "c) Formes irrégulières", "body": "<ul><li><strong>bon(ne)(s) → meilleur(e)(s)</strong> — <em>ce gâteau est meilleur</em> (jamais « plus bon »).</li><li><strong>bien → mieux</strong> (adverbe invariable) — <em>elle chante mieux</em> (jamais « plus bien »).</li></ul>"},
                {"heading": "d) Le groupe de comparaison", "body": "<ul><li>Avec un comparatif : introduit par <em>que</em> — <em>plus grand que Paul</em>.</li><li>Avec un superlatif : introduit par <em>de</em> — <em>le plus grand de la classe</em>.</li></ul>"},
            ],
            "examples": [
                "Paul est plus grand que Marie.",
                "Elle court aussi vite que lui.",
                "Ce restaurant est moins cher que l'autre.",
                "C'est le plus grand bâtiment de la ville.",
                "Ce gâteau est meilleur que le précédent.",
                "Tu chantes mieux que moi.",
                "C'est la meilleure idée de la réunion.",
            ],
            "commonMistakes": [
                {"wrong": "Ce gâteau est plus bon que l'autre.", "right": "Ce gâteau est meilleur que l'autre.", "why": "Bon a une forme comparative irrégulière, meilleur ; « plus bon » n'existe pas."},
                {"wrong": "Elle chante plus bien que moi.", "right": "Elle chante mieux que moi.", "why": "L'adverbe bien devient mieux au comparatif, jamais « plus bien »."},
                {"wrong": "Il est le plus grand de la classe que Paul.", "right": "Il est le plus grand de la classe.", "why": "Le superlatif introduit son groupe de comparaison avec de, pas avec que."},
            ],
        },
        "exercises": [
            {"id": "a2cs-fill", "type": "fill-blank", "title": "Complète la Comparaison",
             "instructions": "Choisis la forme correcte pour chaque espace.",
             "items": [
                {"id": "a2csf1", "prompt": "Ce gâteau est ___ que l'autre.", "answers": [["meilleur"]], "options": ["meilleur", "plus bon", "plus bien"], "explanation": "Bon a une forme comparative irrégulière : meilleur."},
                {"id": "a2csf2", "prompt": "Elle chante ___ que moi.", "answers": [["mieux"]], "options": ["mieux", "plus bien", "meilleur"], "explanation": "Bien (adverbe) devient mieux au comparatif."},
                {"id": "a2csf3", "prompt": "C'est ___ bâtiment de la ville.", "answers": [["le plus grand"]], "options": ["le plus grand", "plus grand", "le meilleur grand"], "explanation": "Superlatif : le + plus + adjectif."},
                {"id": "a2csf4", "prompt": "Marie court ___ vite que Paul.", "answers": [["aussi"]], "options": ["aussi", "plus", "meilleur"], "explanation": "Aussi...que exprime l'égalité."},
             ]},
            {"id": "a2cs-mc", "type": "multiple-choice", "title": "Comparatifs et Superlatifs",
             "items": [
                {"id": "a2csm1", "prompt": "Comment dit-on le comparatif irrégulier de bon ?", "options": ["meilleur", "plus bon", "bonnier"], "answerIndex": 0, "explanation": "Bon devient meilleur au comparatif."},
                {"id": "a2csm2", "prompt": "Quelle préposition introduit le groupe de comparaison du superlatif ?", "options": ["de", "que", "à"], "answerIndex": 0, "explanation": "Le superlatif utilise de : le plus grand de la classe."},
                {"id": "a2csm3", "prompt": "Comment exprime-t-on l'égalité ?", "options": ["aussi...que", "plus...que", "moins...que"], "answerIndex": 0, "explanation": "Aussi...que exprime l'égalité entre deux éléments."},
                {"id": "a2csm4", "prompt": "Quel est le comparatif irrégulier de l'adverbe bien ?", "options": ["mieux", "plus bien", "meilleur"], "answerIndex": 0, "explanation": "Bien devient mieux au comparatif ; meilleur est réservé à l'adjectif bon."},
             ]},
            {"id": "a2cs-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2csc1", "incorrect": "Ce gâteau est plus bon que l'autre.", "answer": ["Ce gâteau est meilleur que l'autre."], "explanation": "Bon a une forme irrégulière au comparatif : meilleur."},
                {"id": "a2csc2", "incorrect": "Elle chante plus bien que moi.", "answer": ["Elle chante mieux que moi."], "explanation": "Bien devient mieux au comparatif."},
                {"id": "a2csc3", "incorrect": "Il est le plus grand de la classe que Paul.", "answer": ["Il est le plus grand de la classe."], "explanation": "Le superlatif n'a pas besoin de que après de la classe."},
             ]},
        ],
        "summary": [
            "Le comparatif se forme avec plus/moins/aussi...que autour de l'adjectif ou de l'adverbe.",
            "Le superlatif se forme avec le/la/les plus/moins + adjectif, et son groupe de comparaison est introduit par de.",
            "Bon devient meilleur et bien devient mieux au comparatif comme au superlatif ; « plus bon » et « plus bien » n'existent pas.",
        ],
    },
    {
        "id": "a2-les-pronoms-cod",
        "level": "A2", "unit": "1", "order": 6, "skill": "grammar", "strand": "pronoms-cod",
        "title": "Les Pronoms Compléments d'Objet Direct (COD)",
        "subtitle": "Le/la/l'/les pour remplacer un complément d'objet direct, et leur place avant le verbe.",
        "objectives": [
            "Identifier le complément d'objet direct dans une phrase.",
            "Remplacer un COD par le/la/l'/les selon le genre et le nombre.",
            "Placer correctement le pronom COD avant le verbe conjugué, y compris au passé composé et à la négation.",
        ],
        "content": {
            "intro": "Pour éviter de répéter un nom déjà mentionné, le français le remplace par un petit pronom placé avant le verbe — une construction très différente de l'anglais, où le pronom suit le verbe.",
            "explanation": "<p>Le complément d'objet direct (COD) répond à la question <em>qui</em> ou <em>quoi</em> après le verbe, sans préposition : <em>Je vois le film</em> (je vois quoi ? le film) <em>→ Je le vois.</em> Le pronom COD (<strong>le, la, l', les</strong>) se place <strong>juste avant le verbe conjugué</strong>, jamais après.</p><p>Au passé composé, le pronom se place avant l'auxiliaire : <em>Je l'ai vu.</em> À la forme négative, <em>ne…pas</em> encadre le pronom et le verbe ensemble : <em>Je ne le vois pas. Je ne l'ai pas vu.</em></p>",
            "rules": [
                {"heading": "a) Formes", "body": "<ul><li><strong>le</strong> — masculin singulier ; <strong>la</strong> — féminin singulier.</li><li><strong>l'</strong> — devant une voyelle ou un h muet, masculin ou féminin.</li><li><strong>les</strong> — pluriel, masculin ou féminin.</li></ul>"},
                {"heading": "b) Position au présent", "body": "<ul><li>Avant le verbe conjugué : <em>Je le vois, tu la connais, nous les invitons</em>.</li></ul>"},
                {"heading": "c) Position au passé composé", "body": "<ul><li>Avant l'auxiliaire : <em>Je l'ai vu, elle l'a achetée</em>.</li></ul>"},
                {"heading": "d) Négation", "body": "<ul><li><em>ne</em> + pronom + verbe + <em>pas</em> : <em>Je ne le vois pas. Je ne l'ai pas vu.</em></li></ul>"},
            ],
            "examples": [
                "Je vois le film. → Je le vois.",
                "Tu aimes cette chanson ? → Tu l'aimes ?",
                "Nous invitons nos amis. → Nous les invitons.",
                "Elle a acheté la voiture. → Elle l'a achetée.",
                "Je ne le vois pas.",
                "Vous les connaissez bien ?",
            ],
            "commonMistakes": [
                {"wrong": "Je vois le.", "right": "Je le vois.", "why": "Le pronom COD se place avant le verbe conjugué, jamais après."},
                {"wrong": "Je ai le vu.", "right": "Je l'ai vu.", "why": "Devant une voyelle, le et la deviennent l', et le pronom précède l'auxiliaire."},
                {"wrong": "Elle a acheté la voiture, elle a acheté la.", "right": "Elle a acheté la voiture, elle l'a achetée.", "why": "On remplace un nom déjà mentionné par un pronom, placé avant le verbe, pour éviter la répétition."},
            ],
        },
        "exercises": [
            {"id": "a2cd-fill", "type": "fill-blank", "title": "Remplace par le Bon Pronom",
             "instructions": "Récris la phrase avec le pronom COD correct à la place de l'espace.",
             "items": [
                {"id": "a2cdf1", "prompt": "Tu vois le film ? — Oui, je ___ vois.", "answers": [["le"]], "options": ["le", "la", "les"], "explanation": "Le film est masculin singulier : le."},
                {"id": "a2cdf2", "prompt": "Tu connais cette chanson ? — Oui, je ___ connais.", "answers": [["la"]], "options": ["la", "le", "l'"], "explanation": "Cette chanson est féminin singulier, sans voyelle initiale au verbe : la."},
                {"id": "a2cdf3", "prompt": "Vous invitez vos amis ? — Oui, nous ___ invitons.", "answers": [["les"]], "options": ["les", "leur", "la"], "explanation": "Vos amis est pluriel : les."},
                {"id": "a2cdf4", "prompt": "Elle a acheté la voiture ? — Oui, elle ___ a achetée.", "answers": [["l'"]], "options": ["l'", "la", "le"], "explanation": "Devant le verbe commençant par une voyelle (a), la devient l'."},
             ]},
            {"id": "a2cd-mc", "type": "multiple-choice", "title": "Le Pronom COD",
             "items": [
                {"id": "a2cdm1", "prompt": "Où se place le pronom COD ?", "options": ["avant le verbe conjugué", "après le verbe conjugué", "à la fin de la phrase"], "answerIndex": 0, "explanation": "En français, le pronom complément précède toujours le verbe conjugué."},
                {"id": "a2cdm2", "prompt": "Quel pronom remplace un nom féminin pluriel ?", "options": ["les", "la", "leur"], "answerIndex": 0, "explanation": "Les est le pronom COD pluriel, masculin ou féminin."},
                {"id": "a2cdm3", "prompt": "Où se place le pronom au passé composé ?", "options": ["avant l'auxiliaire", "après le participe passé", "après l'auxiliaire"], "answerIndex": 0, "explanation": "Le pronom précède l'auxiliaire avoir/être au passé composé."},
                {"id": "a2cdm4", "prompt": "Comment nie-t-on « Je le vois » ?", "options": ["Je ne le vois pas.", "Je le vois ne pas.", "Je ne vois le pas."], "answerIndex": 0, "explanation": "Ne...pas encadre le pronom et le verbe ensemble."},
             ]},
            {"id": "a2cd-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2cdc1", "incorrect": "Je vois le.", "answer": ["Je le vois."], "explanation": "Le pronom se place avant le verbe conjugué."},
                {"id": "a2cdc2", "incorrect": "Je ai le vu.", "answer": ["Je l'ai vu."], "explanation": "Le devient l' devant une voyelle, et se place avant l'auxiliaire."},
                {"id": "a2cdc3", "incorrect": "Nous invitons les ne pas.", "answer": ["Nous ne les invitons pas."], "explanation": "Ne...pas encadre le pronom et le verbe ensemble, avant le verbe."},
             ]},
        ],
        "summary": [
            "Le COD répond à qui/quoi sans préposition, et se remplace par le/la/l'/les.",
            "Le pronom COD se place toujours avant le verbe conjugué, y compris avant l'auxiliaire au passé composé.",
            "À la négation, ne...pas encadre le pronom et le verbe ensemble.",
        ],
    },
    {
        "id": "a2-les-pronoms-coi",
        "level": "A2", "unit": "1", "order": 7, "skill": "grammar", "strand": "pronoms-coi",
        "title": "Les Pronoms Compléments d'Objet Indirect (COI)",
        "subtitle": "Lui et leur pour remplacer un complément introduit par à + personne.",
        "objectives": [
            "Identifier le complément d'objet indirect introduit par à + personne.",
            "Remplacer un COI par lui (singulier) ou leur (pluriel).",
            "Distinguer un verbe direct (COD) d'un verbe indirect (COI) selon sa construction.",
        ],
        "content": {
            "intro": "Certains verbes se construisent avec à devant la personne — parler à quelqu'un, téléphoner à quelqu'un — et ce à change le pronom qu'on utilise pour éviter de la répéter.",
            "explanation": "<p>Le complément d'objet indirect (COI) répond à la question <em>à qui</em> après le verbe. Il se remplace par <strong>lui</strong> (singulier, masculin ou féminin) ou <strong>leur</strong> (pluriel), placés avant le verbe conjugué, comme les pronoms COD : <em>Je parle à Marie → Je lui parle. Je téléphone à mes parents → Je leur téléphone.</em></p><p>Des verbes très fréquents se construisent avec <em>à</em> + personne, et prennent donc <em>lui/leur</em> : <em>parler à, téléphoner à, écrire à, donner à, dire à, demander à, répondre à</em>. D'autres verbes se construisent directement, sans <em>à</em>, et prennent donc <em>le/la/les</em> : <em>regarder, écouter, attendre, chercher</em>.</p>",
            "rules": [
                {"heading": "a) Formes", "body": "<ul><li><strong>lui</strong> — singulier, masculin ou féminin : <em>je lui parle</em>.</li><li><strong>leur</strong> — pluriel, masculin ou féminin : <em>je leur téléphone</em>.</li></ul>"},
                {"heading": "b) Verbes courants avec à + personne", "body": "<ul><li><em>parler à, téléphoner à, écrire à, donner à, dire à, demander à, répondre à</em>.</li></ul>"},
                {"heading": "c) Position", "body": "<ul><li>Avant le verbe conjugué, comme le COD : <em>Je lui parle. Je ne leur téléphone pas.</em></li></ul>"},
                {"heading": "d) COD ou COI ?", "body": "<ul><li>Vérifier la construction du verbe : avec à + personne → COI (lui/leur) ; sans préposition → COD (le/la/les).</li></ul>"},
            ],
            "examples": [
                "Je parle à Marie. → Je lui parle.",
                "Nous téléphonons à nos parents. → Nous leur téléphonons.",
                "Il écrit à sa sœur. → Il lui écrit.",
                "Vous répondez à vos clients ? → Vous leur répondez ?",
                "Je ne lui donne pas d'argent.",
                "Elle leur dit la vérité.",
            ],
            "commonMistakes": [
                {"wrong": "Je le parle.", "right": "Je lui parle.", "why": "Parler à quelqu'un est un verbe indirect : il prend lui/leur, pas le/la."},
                {"wrong": "Je téléphone lui.", "right": "Je lui téléphone.", "why": "Le pronom COI se place avant le verbe conjugué, jamais après."},
                {"wrong": "Nous leur regardons.", "right": "Nous les regardons.", "why": "Regarder se construit sans préposition : c'est un COD (les), pas un COI (leur)."},
            ],
        },
        "exercises": [
            {"id": "a2ci-fill", "type": "fill-blank", "title": "Remplace par Lui ou Leur",
             "instructions": "Récris la phrase avec le pronom COI correct à la place de l'espace.",
             "items": [
                {"id": "a2cif1", "prompt": "Tu parles à Marie ? — Oui, je ___ parle.", "answers": [["lui"]], "options": ["lui", "la", "leur"], "explanation": "À Marie (singulier) se remplace par lui."},
                {"id": "a2cif2", "prompt": "Vous téléphonez à vos parents ? — Oui, nous ___ téléphonons.", "answers": [["leur"]], "options": ["leur", "les", "lui"], "explanation": "À vos parents (pluriel) se remplace par leur."},
                {"id": "a2cif3", "prompt": "Il écrit à sa sœur ? — Oui, il ___ écrit.", "answers": [["lui"]], "options": ["lui", "la", "leur"], "explanation": "À sa sœur (singulier) se remplace par lui."},
                {"id": "a2cif4", "prompt": "Tu regardes tes amis ? — Oui, je ___ regarde.", "answers": [["les"]], "options": ["les", "leur", "lui"], "explanation": "Regarder est direct (sans à) : c'est donc un COD, les."},
             ]},
            {"id": "a2ci-mc", "type": "multiple-choice", "title": "COD ou COI ?",
             "items": [
                {"id": "a2cim1", "prompt": "Quel pronom remplace à + personne au pluriel ?", "options": ["leur", "les", "lui"], "answerIndex": 0, "explanation": "Leur remplace un COI pluriel."},
                {"id": "a2cim2", "prompt": "Quel verbe se construit avec à + personne ?", "options": ["téléphoner à", "regarder", "attendre"], "answerIndex": 0, "explanation": "Téléphoner à quelqu'un est un verbe indirect."},
                {"id": "a2cim3", "prompt": "Comment remplace-t-on à Marie ?", "options": ["lui", "elle", "la"], "answerIndex": 0, "explanation": "Lui remplace un COI singulier, masculin ou féminin."},
                {"id": "a2cim4", "prompt": "Écouter se construit-il avec à + personne ?", "options": ["non, directement", "oui, toujours", "cela dépend du sujet"], "answerIndex": 0, "explanation": "Écouter est direct : il prend un COD (le/la/les), pas lui/leur."},
             ]},
            {"id": "a2ci-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2cic1", "incorrect": "Je le parle tous les jours.", "answer": ["Je lui parle tous les jours."], "explanation": "Parler à quelqu'un demande lui/leur, pas le/la."},
                {"id": "a2cic2", "incorrect": "Je téléphone lui ce soir.", "answer": ["Je lui téléphone ce soir."], "explanation": "Le pronom COI se place avant le verbe conjugué."},
                {"id": "a2cic3", "incorrect": "Nous leur regardons jouer.", "answer": ["Nous les regardons jouer."], "explanation": "Regarder est un verbe direct : il prend un COD, pas un COI."},
             ]},
        ],
        "summary": [
            "Le COI répond à à qui, et se remplace par lui (singulier) ou leur (pluriel).",
            "Des verbes fréquents comme parler à, téléphoner à, écrire à, donner à se construisent avec à + personne et prennent donc lui/leur.",
            "Il faut vérifier la construction de chaque verbe pour choisir entre COD (le/la/les) et COI (lui/leur).",
        ],
    },
    {
        "id": "a2-les-verbes-pronominaux",
        "level": "A2", "unit": "1", "order": 8, "skill": "grammar", "strand": "pronominaux",
        "title": "Les Verbes Pronominaux",
        "subtitle": "Se lever, s'appeler, se laver : la conjugaison réfléchie au présent et au passé composé.",
        "objectives": [
            "Conjuguer un verbe pronominal au présent avec le bon pronom réfléchi.",
            "Utiliser des verbes pronominaux fréquents : se lever, s'appeler, se laver, se coucher.",
            "Former le passé composé d'un verbe pronominal avec être et l'accord du participe passé.",
        ],
        "content": {
            "intro": "Beaucoup d'actions quotidiennes se disent en français avec un verbe pronominal, construit avec un petit pronom réfléchi qui renvoie au sujet lui-même.",
            "explanation": "<p>Un verbe pronominal se conjugue avec un pronom réfléchi (<strong>me, te, se, nous, vous, se</strong>) qui correspond au sujet et se place juste avant le verbe : <em>je me lève, tu te lèves, il se lève, nous nous levons, vous vous levez, ils se lèvent</em>.</p><p>Au passé composé, tous les verbes pronominaux se conjuguent avec <strong>être</strong>, et le participe passé s'accorde généralement avec le sujet, comme pour les autres verbes en être : <em>elle s'est levée, ils se sont couchés</em>.</p>",
            "rules": [
                {"heading": "a) Pronoms réfléchis", "body": "<ul><li><em>me/te/se/nous/vous/se</em>, placés avant le verbe conjugué.</li></ul>"},
                {"heading": "b) Conjugaison au présent", "body": "<ul><li><em>je me lève, tu te lèves, il/elle se lève, nous nous levons, vous vous levez, ils/elles se lèvent</em>.</li></ul>"},
                {"heading": "c) Négation", "body": "<ul><li><em>ne</em> encadre le pronom réfléchi et le verbe : <em>je ne me lève pas</em>.</li></ul>"},
                {"heading": "d) Passé composé", "body": "<ul><li>Toujours avec être, participe passé généralement accordé avec le sujet : <em>elle s'est levée, ils se sont couchés</em>.</li></ul>"},
            ],
            "examples": [
                "Je me lève à sept heures.",
                "Comment tu t'appelles ?",
                "Nous nous couchons tard le week-end.",
                "Elle s'est levée très tôt ce matin.",
                "Ils se sont couchés après minuit.",
                "Vous vous lavez les mains avant de manger ?",
            ],
            "commonMistakes": [
                {"wrong": "Je lève à sept heures.", "right": "Je me lève à sept heures.", "why": "Un verbe pronominal a toujours besoin de son pronom réfléchi."},
                {"wrong": "Je ne lève pas me tôt.", "right": "Je ne me lève pas tôt.", "why": "Ne encadre ensemble le pronom réfléchi et le verbe : ne + me + lève + pas."},
                {"wrong": "Elle a levée tôt.", "right": "Elle s'est levée tôt.", "why": "Tous les verbes pronominaux utilisent être au passé composé, jamais avoir."},
            ],
        },
        "exercises": [
            {"id": "a2vp-fill", "type": "fill-blank", "title": "Conjugue le Verbe Pronominal",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "a2vpf1", "prompt": "Je ___ (se lever) à sept heures.", "answers": [["me lève"]], "options": ["me lève", "lève", "me levé"], "explanation": "Pronom réfléchi me + verbe conjugué au présent."},
                {"id": "a2vpf2", "prompt": "Comment tu ___ (s'appeler) ?", "answers": [["t'appelles"]], "options": ["t'appelles", "appelles", "t'appelle"], "explanation": "Pronom réfléchi te (t') + appeler conjugué à tu."},
                {"id": "a2vpf3", "prompt": "Elle ___ (se lever) très tôt hier.", "answers": [["s'est levée"]], "options": ["s'est levée", "a levée", "s'est levé"], "explanation": "Passé composé avec être, participe accordé au féminin."},
                {"id": "a2vpf4", "prompt": "Nous ___ (se coucher) tard le week-end.", "answers": [["nous couchons"]], "options": ["nous couchons", "couchons", "nous couché"], "explanation": "Pronom réfléchi nous + verbe conjugué au présent."},
             ]},
            {"id": "a2vp-mc", "type": "multiple-choice", "title": "Les Verbes Pronominaux",
             "items": [
                {"id": "a2vpm1", "prompt": "Quel auxiliaire utilise-t-on avec un verbe pronominal au passé composé ?", "options": ["être", "avoir", "les deux selon le verbe"], "answerIndex": 0, "explanation": "Tous les verbes pronominaux se conjuguent avec être."},
                {"id": "a2vpm2", "prompt": "Où se place le pronom réfléchi ?", "options": ["avant le verbe conjugué", "après le verbe conjugué", "à la fin de la phrase"], "answerIndex": 0, "explanation": "Le pronom réfléchi précède toujours le verbe conjugué."},
                {"id": "a2vpm3", "prompt": "Comment nie-t-on « je me lève » ?", "options": ["je ne me lève pas", "je me ne lève pas", "je ne lève me pas"], "answerIndex": 0, "explanation": "Ne encadre ensemble le pronom réfléchi et le verbe."},
                {"id": "a2vpm4", "prompt": "Comment le participe passé s'accorde-t-il en général avec un verbe pronominal ?", "options": ["avec le sujet", "il ne s'accorde jamais", "toujours au masculin"], "answerIndex": 0, "explanation": "Comme les autres verbes en être, le participe passé s'accorde généralement avec le sujet."},
             ]},
            {"id": "a2vp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2vpc1", "incorrect": "Je lève à sept heures.", "answer": ["Je me lève à sept heures."], "explanation": "Le pronom réfléchi me est obligatoire."},
                {"id": "a2vpc2", "incorrect": "Elle a levée tôt ce matin.", "answer": ["Elle s'est levée tôt ce matin."], "explanation": "Se lever se conjugue avec être au passé composé."},
                {"id": "a2vpc3", "incorrect": "Nous ne nous couchons tard pas.", "answer": ["Nous ne nous couchons pas tard."], "explanation": "Ne...pas encadre le pronom et le verbe ; tard reste après pas."},
             ]},
        ],
        "summary": [
            "Un verbe pronominal se conjugue avec un pronom réfléchi (me/te/se/nous/vous/se) placé avant le verbe.",
            "Au passé composé, tous les verbes pronominaux se conjuguent avec être.",
            "Le participe passé d'un verbe pronominal s'accorde généralement avec le sujet, comme pour les autres verbes en être.",
        ],
    },
    {
        "id": "a2-limperatif",
        "level": "A2", "unit": "1", "order": 9, "skill": "grammar", "strand": "imperatif",
        "title": "L'Impératif",
        "subtitle": "Donner un ordre ou un conseil, à l'affirmatif et au négatif, et placer les pronoms compléments.",
        "objectives": [
            "Former l'impératif affirmatif pour tu, nous et vous.",
            "Former l'impératif négatif et placer correctement les pronoms compléments.",
            "Reconnaître la particularité des verbes en -er à l'impératif (pas de -s à tu).",
        ],
        "content": {
            "intro": "L'impératif sert à donner un ordre, un conseil ou une instruction — et se construit à partir d'un temps que tu maîtrises déjà, le présent, sans aucun pronom sujet.",
            "explanation": "<p>L'impératif se forme à partir du <strong>présent de l'indicatif</strong>, sans pronom sujet, pour trois personnes seulement : <em>tu, nous, vous</em>. Les verbes en <strong>-er</strong> (et <em>ouvrir</em> et ses composés) perdent le <strong>-s</strong> final de <em>tu</em> : <em>tu parles → Parle !</em></p><p>À l'impératif affirmatif, le pronom complément se place <strong>après</strong> le verbe, relié par un trait d'union : <em>Mange-le ! Lève-toi !</em> (te devient toi après le verbe). À l'impératif négatif, il retourne <strong>avant</strong> le verbe, comme d'habitude : <em>Ne le mange pas ! Ne te lève pas !</em></p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>Présent de l'indicatif sans pronom sujet, pour tu/nous/vous : <em>Finis ! Finissons ! Finissez !</em></li></ul>"},
                {"heading": "b) Verbes en -er", "body": "<ul><li>Perdent le -s final à tu : <em>tu parles → Parle !</em> ; mais <em>Parlons ! Parlez !</em> gardent leur forme normale.</li></ul>"},
                {"heading": "c) Impératif affirmatif + pronom", "body": "<ul><li>Pronom après le verbe, avec un trait d'union : <em>Mange-le ! Lève-toi !</em></li></ul>"},
                {"heading": "d) Impératif négatif + pronom", "body": "<ul><li>Pronom avant le verbe, comme d'habitude : <em>Ne le mange pas ! Ne te lève pas !</em></li></ul>"},
            ],
            "examples": [
                "Parle plus fort, s'il te plaît !",
                "Finissons ce travail ensemble.",
                "Prenez le temps de réfléchir.",
                "Mange-le avant qu'il ne soit froid.",
                "Lève-toi, il est tard !",
                "Ne le mange pas, il est encore chaud.",
                "Ne vous inquiétez pas.",
            ],
            "commonMistakes": [
                {"wrong": "Parles plus fort.", "right": "Parle plus fort.", "why": "Les verbes en -er perdent leur -s final à l'impératif tu."},
                {"wrong": "Le mange !", "right": "Mange-le !", "why": "À l'impératif affirmatif, le pronom se place après le verbe, avec un trait d'union."},
                {"wrong": "Ne te lève pas te.", "right": "Ne te lève pas.", "why": "À la forme négative, le pronom se place une seule fois, devant le verbe."},
            ],
        },
        "exercises": [
            {"id": "a2ip-fill", "type": "fill-blank", "title": "Forme l'Impératif",
             "instructions": "Écris la forme correcte de l'impératif pour la personne indiquée.",
             "items": [
                {"id": "a2ipf1", "prompt": "(tu, parler) ___ plus fort !", "answers": [["Parle"]], "options": ["Parle", "Parles", "Parler"], "explanation": "Les verbes en -er perdent leur -s final à tu."},
                {"id": "a2ipf2", "prompt": "(nous, finir) ___ ce travail ensemble.", "answers": [["Finissons"]], "options": ["Finissons", "Finissez", "Finis"], "explanation": "Forme nous de l'impératif, identique au présent."},
                {"id": "a2ipf3", "prompt": "(tu, manger + le) ___ avant qu'il ne soit froid.", "answers": [["Mange-le"]], "options": ["Mange-le", "Le mange", "Manges-le"], "explanation": "Pronom après le verbe à l'impératif affirmatif, avec trait d'union."},
                {"id": "a2ipf4", "prompt": "(vous, ne pas s'inquiéter) ___.", "answers": [["Ne vous inquiétez pas"]], "options": ["Ne vous inquiétez pas", "Vous ne inquiétez pas", "N'inquiétez vous pas"], "explanation": "À la forme négative, le pronom reste devant le verbe."},
             ]},
            {"id": "a2ip-mc", "type": "multiple-choice", "title": "L'Impératif : Formation et Pronoms",
             "items": [
                {"id": "a2ipm1", "prompt": "Pour combien de personnes existe l'impératif ?", "options": ["trois : tu, nous, vous", "toutes les personnes", "seulement tu"], "answerIndex": 0, "explanation": "L'impératif n'existe qu'à tu, nous et vous."},
                {"id": "a2ipm2", "prompt": "Que perdent les verbes en -er à l'impératif tu ?", "options": ["le -s final", "le -e final", "rien"], "answerIndex": 0, "explanation": "Tu parles devient Parle !, sans -s."},
                {"id": "a2ipm3", "prompt": "Où se place le pronom à l'impératif affirmatif ?", "options": ["après le verbe, avec un trait d'union", "avant le verbe", "il disparaît"], "answerIndex": 0, "explanation": "Mange-le !, Lève-toi ! : pronom après le verbe."},
                {"id": "a2ipm4", "prompt": "Où se place le pronom à l'impératif négatif ?", "options": ["avant le verbe", "après le verbe", "à la fin de la phrase"], "answerIndex": 0, "explanation": "Ne le mange pas ! : le pronom retourne avant le verbe."},
             ]},
            {"id": "a2ip-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2ipc1", "incorrect": "Parles plus fort !", "answer": ["Parle plus fort !"], "explanation": "Les verbes en -er perdent leur -s final à l'impératif tu."},
                {"id": "a2ipc2", "incorrect": "Le mange avant qu'il ne soit froid !", "answer": ["Mange-le avant qu'il ne soit froid !"], "explanation": "À l'affirmatif, le pronom se place après le verbe."},
                {"id": "a2ipc3", "incorrect": "Ne te lève pas te.", "answer": ["Ne te lève pas."], "explanation": "Le pronom ne se répète pas ; il reste devant le verbe à la forme négative."},
             ]},
        ],
        "summary": [
            "L'impératif se forme à partir du présent, sans pronom sujet, pour tu/nous/vous ; les verbes en -er perdent leur -s final à tu.",
            "À l'impératif affirmatif, le pronom complément se place après le verbe, relié par un trait d'union.",
            "À l'impératif négatif, le pronom retourne devant le verbe, comme d'habitude.",
        ],
    },
    {
        "id": "a2-le-conditionnel-present",
        "level": "A2", "unit": "1", "order": 10, "skill": "grammar", "strand": "conditionnel",
        "title": "Le Conditionnel Présent",
        "subtitle": "Formation à partir du radical du futur, et usages pour la politesse, le conseil et le souhait.",
        "objectives": [
            "Former le conditionnel présent avec le radical du futur et les terminaisons de l'imparfait.",
            "Utiliser le conditionnel pour formuler une demande polie.",
            "Utiliser le conditionnel pour donner un conseil ou exprimer un souhait.",
        ],
        "content": {
            "intro": "Le conditionnel présent adoucit tout ce que tu dis : une demande devient polie, un ordre devient un conseil, une envie devient un souhait — et sa formation combine deux temps que tu connais déjà.",
            "explanation": "<p>Le conditionnel présent se forme avec le <strong>même radical que le futur simple</strong> + les terminaisons de l'<strong>imparfait</strong> (-ais, -ais, -ait, -ions, -iez, -aient) : <em>je parlerais, je serais, j'aurais, j'irais</em>. Les radicaux irréguliers sont exactement les mêmes qu'au futur : <em>être → ser-, avoir → aur-, aller → ir-, faire → fer-, pouvoir → pourr-, vouloir → voudr-, devoir → devr-</em>.</p><p>Au niveau A2, le conditionnel sert surtout à trois choses : la <strong>politesse</strong> (<em>je voudrais un café, pourriez-vous m'aider ?</em>), le <strong>conseil</strong> (<em>tu devrais te reposer</em>), et le <strong>souhait</strong> (<em>j'aimerais bien voyager</em>).</p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>Radical du futur + terminaisons de l'imparfait : <em>je parlerais, tu finirais, il vendrait, nous parlerions, vous finiriez, ils vendraient</em>.</li></ul>"},
                {"heading": "b) Radicaux irréguliers", "body": "<ul><li>Identiques au futur : <em>être → ser-, avoir → aur-, aller → ir-, faire → fer-, pouvoir → pourr-, vouloir → voudr-, devoir → devr-</em>.</li></ul>"},
                {"heading": "c) Politesse", "body": "<ul><li><em>Je voudrais…, pourriez-vous…, j'aimerais…</em> — plus poli qu'un présent ou un futur direct.</li></ul>"},
                {"heading": "d) Conseil et souhait", "body": "<ul><li><em>Tu devrais</em> + infinitif — conseil doux.</li><li><em>J'aimerais / je voudrais</em> + infinitif — souhait.</li></ul>"},
            ],
            "examples": [
                "Je voudrais un café, s'il vous plaît.",
                "Pourriez-vous m'aider ?",
                "Tu devrais te reposer un peu.",
                "Nous aimerions visiter Paris un jour.",
                "Elle serait ravie de venir.",
                "Vous pourriez répéter, s'il vous plaît ?",
            ],
            "commonMistakes": [
                {"wrong": "Je voudrai un café.", "right": "Je voudrais un café.", "why": "Le conditionnel de vouloir est je voudrais (avec s), différent du futur je voudrai."},
                {"wrong": "Pourrez-vous m'aider ?", "right": "Pourriez-vous m'aider ?", "why": "Pour une demande polie, on utilise le conditionnel, pas le futur simple."},
                {"wrong": "J'aimerai voyager plus tard.", "right": "J'aimerais voyager plus tard.", "why": "Le conditionnel prend les terminaisons de l'imparfait : -ais, pas -ai (futur)."},
            ],
        },
        "exercises": [
            {"id": "a2cp-fill", "type": "fill-blank", "title": "Conjugue au Conditionnel Présent",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "a2cpf1", "prompt": "Je ___ (vouloir) un café, s'il vous plaît.", "answers": [["voudrais"]], "options": ["voudrais", "voudrai", "veux"], "explanation": "Conditionnel de vouloir : radical voudr- + terminaison -ais."},
                {"id": "a2cpf2", "prompt": "___-vous (pouvoir) m'aider ?", "answers": [["Pourriez"]], "options": ["Pourriez", "Pourrez", "Pouvez"], "explanation": "Demande polie : conditionnel de pouvoir, pourr- + -iez."},
                {"id": "a2cpf3", "prompt": "Tu ___ (devoir) te reposer un peu.", "answers": [["devrais"]], "options": ["devrais", "devras", "dois"], "explanation": "Conseil au conditionnel : radical devr- + -ais."},
                {"id": "a2cpf4", "prompt": "Nous ___ (aimer) visiter Paris un jour.", "answers": [["aimerions"]], "options": ["aimerions", "aimerons", "aimons"], "explanation": "Souhait au conditionnel : radical futur aimer- + -ions."},
             ]},
            {"id": "a2cp-mc", "type": "multiple-choice", "title": "Le Conditionnel Présent",
             "items": [
                {"id": "a2cpm1", "prompt": "Quel radical utilise-t-on au conditionnel présent ?", "options": ["le radical du futur", "l'infinitif complet", "le radical de l'imparfait"], "answerIndex": 0, "explanation": "Le conditionnel reprend exactement le radical du futur simple."},
                {"id": "a2cpm2", "prompt": "Quelles terminaisons utilise le conditionnel ?", "options": ["celles de l'imparfait", "celles du futur", "celles du présent"], "answerIndex": 0, "explanation": "Les terminaisons du conditionnel sont identiques à celles de l'imparfait."},
                {"id": "a2cpm3", "prompt": "Quelle phrase exprime une demande polie ?", "options": ["Pourriez-vous m'aider ?", "Vous pouvez m'aider.", "Vous pourrez m'aider ?"], "answerIndex": 0, "explanation": "Le conditionnel adoucit une demande, la rendant polie."},
                {"id": "a2cpm4", "prompt": "Quel est le radical conditionnel de faire ?", "options": ["fer-", "fais-", "fait-"], "answerIndex": 0, "explanation": "Faire a le même radical irrégulier qu'au futur : fer-."},
             ]},
            {"id": "a2cp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2cpc1", "incorrect": "Je voudrai un café.", "answer": ["Je voudrais un café."], "explanation": "Le conditionnel prend -ais, pas -ai (futur)."},
                {"id": "a2cpc2", "incorrect": "Pourrez-vous m'aider, s'il vous plaît ?", "answer": ["Pourriez-vous m'aider, s'il vous plaît ?"], "explanation": "Une demande polie utilise le conditionnel, pas le futur."},
                {"id": "a2cpc3", "incorrect": "Tu devras te reposer un peu.", "answer": ["Tu devrais te reposer un peu."], "explanation": "Un conseil doux utilise le conditionnel devrais, pas le futur devras."},
             ]},
        ],
        "summary": [
            "Le conditionnel présent se forme avec le radical du futur + les terminaisons de l'imparfait.",
            "Les radicaux irréguliers sont les mêmes qu'au futur simple.",
            "Le conditionnel sert à la politesse, au conseil doux et au souhait.",
        ],
    },
    {
        "id": "a2-les-indefinis",
        "level": "A2", "unit": "1", "order": 11, "skill": "grammar", "strand": "indefinis",
        "title": "Les Indéfinis",
        "subtitle": "Quelqu'un/personne, quelque chose/rien, chaque, plusieurs, et l'accord de tout.",
        "objectives": [
            "Utiliser quelqu'un/personne et quelque chose/rien selon l'affirmation ou la négation.",
            "Utiliser chaque et plusieurs pour quantifier un nom.",
            "Accorder tout/tous/toute/toutes selon le genre et le nombre du nom.",
        ],
        "content": {
            "intro": "Ces petits mots permettent de parler de personnes ou de choses sans les préciser, ou de quantifier un groupe — indispensables dès qu'on veut parler de façon plus naturelle.",
            "explanation": "<p><strong>Quelqu'un</strong> (affirmatif) et <strong>personne</strong> (négatif, avec <em>ne</em>) servent à parler d'une personne indéterminée : <em>Il y a quelqu'un à la porte. / Il n'y a personne à la porte.</em> <strong>Quelque chose</strong> et <strong>rien</strong> fonctionnent de la même façon pour une chose : <em>J'ai quelque chose à te dire. / Je n'ai rien à te dire.</em></p><p><strong>Chaque</strong> (invariable) précède toujours un nom singulier : <em>chaque élève</em>. <strong>Plusieurs</strong> (invariable) précède toujours un nom pluriel : <em>plusieurs livres</em>. <strong>Tout</strong>, en revanche, s'accorde selon le nom qu'il précède : <em>tout le monde</em> (masculin singulier), <em>toute la classe</em> (féminin singulier), <em>tous les jours</em> (masculin pluriel), <em>toutes les semaines</em> (féminin pluriel).</p>",
            "rules": [
                {"heading": "a) Quelqu'un / personne", "body": "<ul><li><em>quelqu'un</em> (affirmatif) — <em>Il y a quelqu'un ici.</em></li><li><em>ne…personne</em> (négatif) — <em>Il n'y a personne ici.</em></li></ul>"},
                {"heading": "b) Quelque chose / rien", "body": "<ul><li><em>quelque chose</em> (affirmatif) — <em>J'ai quelque chose à dire.</em></li><li><em>ne…rien</em> (négatif) — <em>Je n'ai rien à dire.</em></li></ul>"},
                {"heading": "c) Chaque et plusieurs", "body": "<ul><li><strong>chaque</strong> (invariable) + nom singulier — <em>chaque élève</em>.</li><li><strong>plusieurs</strong> (invariable) + nom pluriel — <em>plusieurs livres</em>.</li></ul>"},
                {"heading": "d) Tout / tous / toute / toutes", "body": "<ul><li><em>tout le monde</em> (masc. sing.), <em>toute la classe</em> (fém. sing.).</li><li><em>tous les jours</em> (masc. plur.), <em>toutes les semaines</em> (fém. plur.).</li></ul>"},
            ],
            "examples": [
                "Il y a quelqu'un à la porte.",
                "Je n'ai rien à te dire.",
                "Chaque élève a son propre livre.",
                "Plusieurs personnes attendent dehors.",
                "Tout le monde est content.",
                "Nous travaillons tous les jours.",
                "Elle vient toutes les semaines.",
            ],
            "commonMistakes": [
                {"wrong": "Il n'y a pas quelqu'un.", "right": "Il n'y a personne.", "why": "À la forme négative, on utilise personne, jamais quelqu'un + pas."},
                {"wrong": "Chaques élèves ont un livre.", "right": "Chaque élève a un livre.", "why": "Chaque est invariable et s'utilise toujours avec un nom singulier."},
                {"wrong": "Toutes les jours, je travaille.", "right": "Tous les jours, je travaille.", "why": "Jours est masculin pluriel : il faut tous, pas toutes."},
            ],
        },
        "exercises": [
            {"id": "a2in-fill", "type": "fill-blank", "title": "Complète avec l'Indéfini Correct",
             "instructions": "Choisis la forme correcte pour chaque espace.",
             "items": [
                {"id": "a2inf1", "prompt": "Il n'y a ___ à la porte.", "answers": [["personne"]], "options": ["personne", "quelqu'un", "rien"], "explanation": "À la forme négative, on utilise personne pour une personne indéterminée."},
                {"id": "a2inf2", "prompt": "___ élève a son propre livre.", "answers": [["Chaque"]], "options": ["Chaque", "Chaques", "Plusieurs"], "explanation": "Chaque est invariable et précède un nom singulier."},
                {"id": "a2inf3", "prompt": "Nous travaillons ___ les jours.", "answers": [["tous"]], "options": ["tous", "toutes", "tout"], "explanation": "Jours est masculin pluriel : tous les jours."},
                {"id": "a2inf4", "prompt": "Je n'ai ___ à te dire.", "answers": [["rien"]], "options": ["rien", "quelque chose", "personne"], "explanation": "À la forme négative, on utilise rien pour une chose indéterminée."},
             ]},
            {"id": "a2in-mc", "type": "multiple-choice", "title": "Les Indéfinis",
             "items": [
                {"id": "a2inm1", "prompt": "Quel mot utilise-t-on à l'affirmatif pour une personne indéterminée ?", "options": ["quelqu'un", "personne", "rien"], "answerIndex": 0, "explanation": "Quelqu'un s'utilise dans une phrase affirmative."},
                {"id": "a2inm2", "prompt": "Chaque s'accorde-t-il en nombre ?", "options": ["non, il est invariable", "oui, au pluriel chaques", "seulement au féminin"], "answerIndex": 0, "explanation": "Chaque reste invariable et précède toujours un nom singulier."},
                {"id": "a2inm3", "prompt": "Comment accorde-t-on tout devant la classe ?", "options": ["toute la classe", "tout la classe", "tous la classe"], "answerIndex": 0, "explanation": "Classe est féminin singulier : toute la classe."},
                {"id": "a2inm4", "prompt": "Plusieurs précède-t-il un nom singulier ou pluriel ?", "options": ["pluriel", "singulier", "les deux"], "answerIndex": 0, "explanation": "Plusieurs s'utilise toujours avec un nom pluriel."},
             ]},
            {"id": "a2in-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2inc1", "incorrect": "Il n'y a pas quelqu'un dans la salle.", "answer": ["Il n'y a personne dans la salle."], "explanation": "La négation utilise personne, pas quelqu'un."},
                {"id": "a2inc2", "incorrect": "Chaques élèves ont un livre.", "answer": ["Chaque élève a un livre."], "explanation": "Chaque est invariable et précède un nom singulier."},
                {"id": "a2inc3", "incorrect": "Toutes les jours, je travaille.", "answer": ["Tous les jours, je travaille."], "explanation": "Jours est masculin pluriel : tous les jours."},
             ]},
        ],
        "summary": [
            "Quelqu'un/quelque chose s'utilisent à l'affirmatif ; personne/rien à la négatif, toujours avec ne.",
            "Chaque (+ singulier) et plusieurs (+ pluriel) sont invariables.",
            "Tout s'accorde en genre et en nombre avec le nom qu'il précède : tout/toute/tous/toutes.",
        ],
    },
    {
        "id": "a2-y-et-en",
        "level": "A2", "unit": "1", "order": 12, "skill": "grammar", "strand": "y-en",
        "title": "Y et En",
        "subtitle": "Deux pronoms pour remplacer à + lieu/chose et de + lieu/chose/quantité.",
        "objectives": [
            "Utiliser y pour remplacer à + lieu ou à + chose.",
            "Utiliser en pour remplacer de + lieu, de + chose, ou une quantité.",
            "Placer y et en avant le verbe conjugué, comme les autres pronoms.",
        ],
        "content": {
            "intro": "Y et en sont deux petits pronoms très fréquents à l'oral, qui remplacent tout un groupe introduit par à ou de, ou même une simple quantité, pour éviter de tout répéter.",
            "explanation": "<p><strong>Y</strong> remplace <em>à</em> + lieu (<em>J'habite à Paris → J'y habite</em>) ou <em>à</em> + chose (<em>Je pense à mon voyage → J'y pense</em>). <strong>En</strong> remplace <em>de</em> + lieu (<em>Je viens de Paris → J'en viens</em>), <em>de</em> + chose (<em>Je parle de mon travail → J'en parle</em>), ou une <strong>quantité</strong> (<em>J'ai deux chats → J'en ai deux ; Tu veux du pain ? → Oui, j'en veux</em>).</p><p>Comme les autres pronoms, <strong>y</strong> et <strong>en</strong> se placent avant le verbe conjugué, ou avant l'auxiliaire au passé composé : <em>J'y suis allé. J'en ai acheté.</em></p>",
            "rules": [
                {"heading": "a) Y", "body": "<ul><li>Remplace à + lieu ou à + chose : <em>j'y habite, j'y pense</em>.</li></ul>"},
                {"heading": "b) En", "body": "<ul><li>Remplace de + lieu/chose ou une quantité : <em>j'en viens, j'en parle, j'en ai deux</em>.</li></ul>"},
                {"heading": "c) Position", "body": "<ul><li>Avant le verbe conjugué (ou l'auxiliaire au passé composé) : <em>j'y vais, j'en ai acheté</em>.</li></ul>"},
                {"heading": "d) En + quantité", "body": "<ul><li>Le nombre ou l'expression de quantité reste souvent après le verbe : <em>j'en ai deux, j'en veux beaucoup</em>.</li></ul>"},
            ],
            "examples": [
                "J'habite à Paris. → J'y habite.",
                "Je pense souvent à mon voyage. → J'y pense souvent.",
                "Je viens de Lyon. → J'en viens.",
                "Tu as des frères ? — Oui, j'en ai deux.",
                "Elle parle de son travail. → Elle en parle.",
                "Nous y sommes allés hier.",
            ],
            "commonMistakes": [
                {"wrong": "J'habite y.", "right": "J'y habite.", "why": "Y se place avant le verbe conjugué, jamais après."},
                {"wrong": "J'ai des frères deux.", "right": "J'en ai deux.", "why": "Pour remplacer une quantité déjà mentionnée, il faut utiliser en, même si le nombre reste dans la phrase."},
                {"wrong": "Je viens de en.", "right": "J'en viens.", "why": "En remplace déjà de + lieu ; on ne répète pas de après en."},
            ],
        },
        "exercises": [
            {"id": "a2ye-fill", "type": "fill-blank", "title": "Remplace par Y ou En",
             "instructions": "Récris la phrase avec le pronom correct à la place de l'espace.",
             "items": [
                {"id": "a2yef1", "prompt": "Tu habites à Paris ? — Oui, j'___ habite.", "answers": [["y"]], "options": ["y", "en", "le"], "explanation": "Y remplace à + lieu."},
                {"id": "a2yef2", "prompt": "Tu viens de Lyon ? — Oui, j'___ viens.", "answers": [["en"]], "options": ["en", "y", "la"], "explanation": "En remplace de + lieu."},
                {"id": "a2yef3", "prompt": "Tu as des sœurs ? — Oui, j'___ ai une.", "answers": [["en"]], "options": ["en", "y", "la"], "explanation": "En remplace une quantité déjà mentionnée."},
                {"id": "a2yef4", "prompt": "Tu penses souvent à ton voyage ? — Oui, j'___ pense souvent.", "answers": [["y"]], "options": ["y", "en", "le"], "explanation": "Y remplace à + chose."},
             ]},
            {"id": "a2ye-mc", "type": "multiple-choice", "title": "Y ou En ?",
             "items": [
                {"id": "a2yem1", "prompt": "Que remplace y ?", "options": ["à + lieu ou à + chose", "de + lieu ou de + chose", "un COD"], "answerIndex": 0, "explanation": "Y remplace un groupe introduit par à."},
                {"id": "a2yem2", "prompt": "Que remplace en ?", "options": ["de + lieu/chose ou une quantité", "à + lieu", "un COI"], "answerIndex": 0, "explanation": "En remplace un groupe introduit par de, ou une quantité."},
                {"id": "a2yem3", "prompt": "Où se placent y et en ?", "options": ["avant le verbe conjugué", "après le verbe conjugué", "en fin de phrase"], "answerIndex": 0, "explanation": "Comme les autres pronoms, ils précèdent le verbe conjugué."},
                {"id": "a2yem4", "prompt": "Comment répond-on à « Tu as deux frères ? » avec en ?", "options": ["Oui, j'en ai deux.", "Oui, j'y ai deux.", "Oui, j'ai en deux."], "answerIndex": 0, "explanation": "En remplace la quantité, placé avant le verbe conjugué."},
             ]},
            {"id": "a2ye-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2yec1", "incorrect": "J'habite y depuis dix ans.", "answer": ["J'y habite depuis dix ans."], "explanation": "Y se place avant le verbe conjugué."},
                {"id": "a2yec2", "incorrect": "Je viens de en Espagne.", "answer": ["J'en viens."], "explanation": "En remplace déjà de + lieu ; on ne répète pas de."},
                {"id": "a2yec3", "incorrect": "J'ai des chats deux.", "answer": ["J'en ai deux."], "explanation": "Pour remplacer une quantité, il faut utiliser en."},
             ]},
        ],
        "summary": [
            "Y remplace à + lieu ou à + chose ; en remplace de + lieu, de + chose, ou une quantité.",
            "Comme les autres pronoms, y et en se placent avant le verbe conjugué, ou avant l'auxiliaire au passé composé.",
            "Avec une quantité, en s'utilise même si le nombre reste exprimé après le verbe : j'en ai deux.",
        ],
    },
    {
        "id": "a2-les-prepositions-avec-les-pays-et-les-villes",
        "level": "A2", "unit": "1", "order": 13, "skill": "grammar", "strand": "prepositions-pays",
        "title": "Les Prépositions avec les Pays et les Villes",
        "subtitle": "En/au/aux devant un pays selon son genre, à devant une ville, et venir de/du/des pour l'origine.",
        "objectives": [
            "Utiliser en/au/aux devant un pays selon son genre et son nombre.",
            "Utiliser à devant une ville, toujours sans article.",
            "Utiliser venir de/du/des pour exprimer l'origine.",
        ],
        "content": {
            "intro": "Parler d'un pays ou d'une ville en français demande de choisir la bonne préposition selon le genre du nom — une règle simple une fois les catégories bien identifiées.",
            "explanation": "<p>Devant un pays <strong>féminin</strong> (ou commençant par une voyelle), on utilise <strong>en</strong> : <em>en France, en Espagne, en Iran</em>. Devant un pays <strong>masculin</strong>, on utilise <strong>au</strong> : <em>au Japon, au Canada, au Brésil</em>. Devant un pays <strong>pluriel</strong>, on utilise <strong>aux</strong> : <em>aux États-Unis, aux Pays-Bas</em>. Devant une <strong>ville</strong>, on utilise toujours <strong>à</strong>, sans article : <em>à Paris, à Tokyo</em>.</p><p>Pour exprimer l'<strong>origine</strong> (venir de), la logique est similaire : <strong>de/d'</strong> devant un pays féminin ou une ville (<em>je viens de France, je viens de Paris</em>), <strong>du</strong> devant un pays masculin (<em>je viens du Japon</em>), <strong>des</strong> devant un pays pluriel (<em>je viens des États-Unis</em>).</p>",
            "rules": [
                {"heading": "a) En", "body": "<ul><li>Pays féminins ou commençant par une voyelle : <em>en France, en Espagne, en Iran</em>.</li></ul>"},
                {"heading": "b) Au / Aux", "body": "<ul><li><strong>au</strong> — pays masculin : <em>au Japon, au Brésil</em>.</li><li><strong>aux</strong> — pays pluriel : <em>aux États-Unis, aux Pays-Bas</em>.</li></ul>"},
                {"heading": "c) À + ville", "body": "<ul><li>Toujours à, sans article : <em>à Paris, à Rome, à Tokyo</em>.</li></ul>"},
                {"heading": "d) Venir de/du/des", "body": "<ul><li><em>de/d'</em> (féminin ou ville) — <em>de France, de Paris</em>.</li><li><em>du</em> (masculin) — <em>du Japon</em>.</li><li><em>des</em> (pluriel) — <em>des États-Unis</em>.</li></ul>"},
            ],
            "examples": [
                "Je passe mes vacances en Espagne.",
                "Il travaille au Japon.",
                "Ils habitent aux États-Unis.",
                "Nous visitons Paris cet été.",
                "Elle vient de France.",
                "Tu viens du Canada ?",
                "Ils viennent des Pays-Bas.",
            ],
            "commonMistakes": [
                {"wrong": "Je vis à France.", "right": "Je vis en France.", "why": "Devant un pays féminin, on utilise en ; à est réservé aux villes."},
                {"wrong": "Il habite en Japon.", "right": "Il habite au Japon.", "why": "Japon est un pays masculin : il faut au, pas en."},
                {"wrong": "Elle vient de Japon.", "right": "Elle vient du Japon.", "why": "Devant un pays masculin, l'origine s'exprime avec du, pas de seul."},
            ],
        },
        "exercises": [
            {"id": "a2pp-fill", "type": "fill-blank", "title": "Complète avec la Préposition Correcte",
             "instructions": "Choisis la forme correcte pour chaque espace.",
             "items": [
                {"id": "a2ppf1", "prompt": "Je passe mes vacances ___ Espagne.", "answers": [["en"]], "options": ["en", "au", "à"], "explanation": "Espagne est un pays féminin : en."},
                {"id": "a2ppf2", "prompt": "Il travaille ___ Japon.", "answers": [["au"]], "options": ["au", "en", "aux"], "explanation": "Japon est un pays masculin : au."},
                {"id": "a2ppf3", "prompt": "Ils habitent ___ États-Unis.", "answers": [["aux"]], "options": ["aux", "au", "en"], "explanation": "États-Unis est un pays pluriel : aux."},
                {"id": "a2ppf4", "prompt": "Elle vient ___ Canada.", "answers": [["du"]], "options": ["du", "de", "des"], "explanation": "Canada est masculin : origine avec du."},
             ]},
            {"id": "a2pp-mc", "type": "multiple-choice", "title": "Pays et Villes",
             "items": [
                {"id": "a2ppm1", "prompt": "Quelle préposition utilise-t-on devant une ville ?", "options": ["à", "en", "au"], "answerIndex": 0, "explanation": "On utilise toujours à devant une ville, sans article."},
                {"id": "a2ppm2", "prompt": "Quelle préposition utilise-t-on devant un pays féminin ?", "options": ["en", "au", "aux"], "answerIndex": 0, "explanation": "Les pays féminins (ou à voyelle initiale) prennent en."},
                {"id": "a2ppm3", "prompt": "Comment dit-on venir des Pays-Bas ?", "options": ["Je viens des Pays-Bas.", "Je viens du Pays-Bas.", "Je viens de Pays-Bas."], "answerIndex": 0, "explanation": "Pays-Bas est pluriel : origine avec des."},
                {"id": "a2ppm4", "prompt": "Quelle préposition utilise-t-on devant un pays pluriel comme les États-Unis ?", "options": ["aux", "au", "en"], "answerIndex": 0, "explanation": "Les pays pluriels prennent aux."},
             ]},
            {"id": "a2pp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a2ppc1", "incorrect": "Je vis à France.", "answer": ["Je vis en France."], "explanation": "Devant un pays féminin, on utilise en."},
                {"id": "a2ppc2", "incorrect": "Il habite en Japon.", "answer": ["Il habite au Japon."], "explanation": "Japon est masculin : au."},
                {"id": "a2ppc3", "incorrect": "Elle vient de Japon.", "answer": ["Elle vient du Japon."], "explanation": "Devant un pays masculin, l'origine s'exprime avec du."},
             ]},
        ],
        "summary": [
            "En précède un pays féminin, au un pays masculin, aux un pays pluriel ; à précède toujours une ville, sans article.",
            "L'origine suit la même logique : de/d' (féminin/ville), du (masculin), des (pluriel).",
            "Ces prépositions dépendent uniquement du genre et du nombre du pays, pas de règles arbitraires.",
        ],
    },
]

# =======================================================================
# EXTRA_EXERCISES — blocs de lecture et de remise en ordre fusionnés dans
# chaque leçon par id, pour enrichir la page Teste-toi sans toucher au
# contenu pédagogique déjà écrit ci-dessus. Voir la boucle de fusion à la
# fin de ce fichier.
# =======================================================================
EXTRA_EXERCISES = {
    "a2-le-passe-compose": [
        {"id": "a2pcx-reading", "type": "reading-comprehension", "title": "Lecture : Une Journée au Marché",
         "passage": "<p>Hier, je suis allé au marché. J'ai acheté des légumes et j'ai vu mon ami Marc. Il est arrivé en retard, mais nous avons bien mangé ensemble. Après le déjeuner, je suis rentré à la maison.</p>",
         "items": [
            {"id": "a2pcxr1", "prompt": "Où est allée la personne hier ?", "options": ["Au marché", "Au restaurant", "À l'école"], "answerIndex": 0, "explanation": "Le texte dit : « je suis allé au marché »."},
            {"id": "a2pcxr2", "prompt": "Qui a-t-elle vu ?", "options": ["Son ami Marc", "Sa sœur", "Sa collègue"], "answerIndex": 0, "explanation": "Le texte dit : « j'ai vu mon ami Marc »."},
            {"id": "a2pcxr3", "prompt": "Comment Marc est-il arrivé ?", "options": ["En retard", "À l'heure", "En avance"], "answerIndex": 0, "explanation": "Le texte dit : « Il est arrivé en retard »."},
            {"id": "a2pcxr4", "prompt": "Qu'a fait la personne après le déjeuner ?", "options": ["Elle est rentrée à la maison", "Elle est allée au travail", "Elle a fait les courses"], "answerIndex": 0, "explanation": "Le texte se termine par « je suis rentré à la maison »."},
         ]},
        {"id": "a2pcx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2pcxo1", "prompt": "Remets les mots en ordre.", "words": ["Je", "suis", "allé", "au", "marché", "hier"], "explanation": "Passé composé avec être + participe accordé."},
            {"id": "a2pcxo2", "prompt": "Remets les mots en ordre.", "words": ["Nous", "avons", "bien", "mangé", "ensemble"], "explanation": "Passé composé avec avoir, participe invariable."},
         ]},
    ],
    "a2-limparfait": [
        {"id": "a2imx-reading", "type": "reading-comprehension", "title": "Lecture : Mon Enfance au Village",
         "passage": "<p>Quand j'étais enfant, j'habitais dans un petit village. Il faisait toujours calme le matin. Mes parents travaillaient dans les champs, et moi, je jouais avec mes cousins tous les jours. Nous étions très heureux.</p>",
         "items": [
            {"id": "a2imxr1", "prompt": "Où habitait la personne enfant ?", "options": ["Dans un petit village", "Dans une grande ville", "À la montagne"], "answerIndex": 0, "explanation": "Le texte dit : « j'habitais dans un petit village »."},
            {"id": "a2imxr2", "prompt": "Comment était le matin ?", "options": ["Toujours calme", "Très bruyant", "Toujours pluvieux"], "answerIndex": 0, "explanation": "Le texte dit : « Il faisait toujours calme le matin »."},
            {"id": "a2imxr3", "prompt": "Que faisaient les parents ?", "options": ["Ils travaillaient dans les champs", "Ils travaillaient en ville", "Ils voyageaient"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2imxr4", "prompt": "Comment étaient-ils, selon le texte ?", "options": ["Très heureux", "Très fatigués", "Très occupés"], "answerIndex": 0, "explanation": "Le texte se termine par « Nous étions très heureux »."},
         ]},
        {"id": "a2imx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2imxo1", "prompt": "Remets les mots en ordre.", "words": ["J'habitais", "dans", "un", "petit", "village"], "explanation": "Imparfait pour décrire une situation passée."},
            {"id": "a2imxo2", "prompt": "Remets les mots en ordre.", "words": ["Nous", "étions", "très", "heureux"], "explanation": "Être à l'imparfait, radical irrégulier ét-."},
         ]},
    ],
    "a2-passe-compose-vs-imparfait": [
        {"id": "a2vix-reading", "type": "reading-comprehension", "title": "Lecture : L'Arrivée à l'Hôtel",
         "passage": "<p>Il faisait nuit quand nous sommes arrivés à l'hôtel. La réceptionniste dormait presque, mais elle nous a souri gentiment. Nous étions fatigués après le long voyage, alors nous sommes montés directement dans notre chambre.</p>",
         "items": [
            {"id": "a2vixr1", "prompt": "Quand sont-ils arrivés à l'hôtel ?", "options": ["Il faisait nuit", "Il faisait jour", "Il faisait beau"], "answerIndex": 0, "explanation": "Le texte dit : « Il faisait nuit quand nous sommes arrivés »."},
            {"id": "a2vixr2", "prompt": "Que faisait la réceptionniste ?", "options": ["Elle dormait presque", "Elle lisait un livre", "Elle mangeait"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2vixr3", "prompt": "Pourquoi sont-ils montés directement dans la chambre ?", "options": ["Parce qu'ils étaient fatigués", "Parce qu'il pleuvait", "Parce que l'hôtel fermait"], "answerIndex": 0, "explanation": "Le texte dit : « Nous étions fatigués … alors nous sommes montés directement »."},
            {"id": "a2vixr4", "prompt": "Comment la réceptionniste les a-t-elle accueillis ?", "options": ["Avec un sourire", "Avec froideur", "Sans un mot"], "answerIndex": 0, "explanation": "Le texte dit : « elle nous a souri gentiment »."},
         ]},
        {"id": "a2vix-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2vixo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "faisait", "nuit", "quand", "nous", "sommes", "arrivés"], "explanation": "Imparfait (décor) + passé composé (événement)."},
            {"id": "a2vixo2", "prompt": "Remets les mots en ordre.", "words": ["Nous", "sommes", "montés", "directement", "dans", "la", "chambre"], "explanation": "Passé composé avec être, action ponctuelle."},
         ]},
    ],
    "a2-le-futur-simple": [
        {"id": "a2fsx-reading", "type": "reading-comprehension", "title": "Lecture : Mes Projets à Montréal",
         "passage": "<p>L'année prochaine, je partirai étudier à Montréal. Je vivrai avec ma cousine, et nous irons à l'université ensemble. Mes parents viendront me voir pendant les vacances. Ce sera une grande aventure.</p>",
         "items": [
            {"id": "a2fsxr1", "prompt": "Où partira la personne l'année prochaine ?", "options": ["À Montréal", "À Paris", "À Londres"], "answerIndex": 0, "explanation": "Le texte dit : « je partirai étudier à Montréal »."},
            {"id": "a2fsxr2", "prompt": "Avec qui vivra-t-elle ?", "options": ["Sa cousine", "Ses parents", "Une amie"], "answerIndex": 0, "explanation": "Le texte dit : « Je vivrai avec ma cousine »."},
            {"id": "a2fsxr3", "prompt": "Qui viendra la voir pendant les vacances ?", "options": ["Ses parents", "Ses amis", "Son professeur"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2fsxr4", "prompt": "Comment sera cette expérience, selon le texte ?", "options": ["Une grande aventure", "Assez ennuyeuse", "Très difficile"], "answerIndex": 0, "explanation": "Le texte se termine par « Ce sera une grande aventure »."},
         ]},
        {"id": "a2fsx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2fsxo1", "prompt": "Remets les mots en ordre.", "words": ["Je", "partirai", "étudier", "à", "Montréal"], "explanation": "Futur simple, radical irrégulier de partir."},
            {"id": "a2fsxo2", "prompt": "Remets les mots en ordre.", "words": ["Mes", "parents", "viendront", "me", "voir"], "explanation": "Futur simple de venir, radical viendr-."},
         ]},
    ],
    "a2-les-comparatifs-et-superlatifs": [
        {"id": "a2csx-reading", "type": "reading-comprehension", "title": "Lecture : Deux Restaurants du Quartier",
         "passage": "<p>Le restaurant italien est plus cher que le restaurant chinois, mais la nourriture y est meilleure. C'est le meilleur restaurant du quartier, selon mes amis. Moi, je trouve que le service est aussi rapide dans les deux.</p>",
         "items": [
            {"id": "a2csxr1", "prompt": "Quel restaurant est plus cher ?", "options": ["Le restaurant italien", "Le restaurant chinois", "Les deux, pareil"], "answerIndex": 0, "explanation": "Le texte dit : « Le restaurant italien est plus cher »."},
            {"id": "a2csxr2", "prompt": "Comment est la nourriture italienne, comparée à l'autre ?", "options": ["Meilleure", "Moins bonne", "Identique"], "answerIndex": 0, "explanation": "Le texte dit : « la nourriture y est meilleure »."},
            {"id": "a2csxr3", "prompt": "Quel restaurant est le meilleur du quartier, selon les amis ?", "options": ["L'italien", "Le chinois", "Aucun des deux"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2csxr4", "prompt": "Comment est le service dans les deux restaurants ?", "options": ["Aussi rapide", "Très différent", "Très lent"], "answerIndex": 0, "explanation": "Le texte dit : « le service est aussi rapide dans les deux »."},
         ]},
        {"id": "a2csx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2csxo1", "prompt": "Remets les mots en ordre.", "words": ["C'est", "le", "meilleur", "restaurant", "du", "quartier"], "explanation": "Superlatif irrégulier de bon : meilleur."},
            {"id": "a2csxo2", "prompt": "Remets les mots en ordre.", "words": ["Le", "service", "est", "aussi", "rapide"], "explanation": "Comparatif d'égalité : aussi...que."},
         ]},
    ],
    "a2-les-pronoms-cod": [
        {"id": "a2cdx-reading", "type": "reading-comprehension", "title": "Lecture : La Nouvelle Robe de Marie",
         "passage": "<p>Marie a acheté une nouvelle robe. Elle l'a mise pour la fête de samedi. Ses amis l'ont beaucoup complimentée. Elle les a remerciés avec un grand sourire.</p>",
         "items": [
            {"id": "a2cdxr1", "prompt": "Qu'a acheté Marie ?", "options": ["Une nouvelle robe", "Un manteau", "Des chaussures"], "answerIndex": 0, "explanation": "Le texte dit : « Marie a acheté une nouvelle robe »."},
            {"id": "a2cdxr2", "prompt": "Quand l'a-t-elle mise ?", "options": ["Pour la fête de samedi", "Pour aller travailler", "Pour un mariage"], "answerIndex": 0, "explanation": "Le texte dit : « Elle l'a mise pour la fête de samedi »."},
            {"id": "a2cdxr3", "prompt": "Qu'ont fait ses amis ?", "options": ["Ils l'ont complimentée", "Ils ont ri", "Ils n'ont rien dit"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2cdxr4", "prompt": "Comment a-t-elle remercié ses amis ?", "options": ["Avec un grand sourire", "Avec un cadeau", "Elle ne les a pas remerciés"], "answerIndex": 0, "explanation": "Le texte se termine par « avec un grand sourire »."},
         ]},
        {"id": "a2cdx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2cdxo1", "prompt": "Remets les mots en ordre.", "words": ["Elle", "l'a", "mise", "pour", "la", "fête"], "explanation": "Pronom COD l' devant l'auxiliaire, accord au féminin."},
            {"id": "a2cdxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "les", "a", "remerciés", "avec", "un", "sourire"], "explanation": "Pronom COD les devant l'auxiliaire, accord au pluriel."},
         ]},
    ],
    "a2-les-pronoms-coi": [
        {"id": "a2cix-reading", "type": "reading-comprehension", "title": "Lecture : Un Problème d'Ordinateur",
         "passage": "<p>Paul a un problème avec son ordinateur. Il téléphone à son frère, qui travaille en informatique. Son frère lui explique la solution patiemment. Ensuite, Paul lui dit merci et raccroche.</p>",
         "items": [
            {"id": "a2cixr1", "prompt": "Quel est le problème de Paul ?", "options": ["Avec son ordinateur", "Avec sa voiture", "Avec son téléphone"], "answerIndex": 0, "explanation": "Le texte dit : « Paul a un problème avec son ordinateur »."},
            {"id": "a2cixr2", "prompt": "À qui téléphone-t-il ?", "options": ["À son frère", "À un ami", "À un technicien"], "answerIndex": 0, "explanation": "Le texte dit : « Il téléphone à son frère »."},
            {"id": "a2cixr3", "prompt": "Que fait le frère ?", "options": ["Il lui explique la solution", "Il vient réparer l'ordinateur", "Il ne peut pas aider"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2cixr4", "prompt": "Que dit Paul à son frère à la fin ?", "options": ["Merci", "Au revoir seulement", "Rien"], "answerIndex": 0, "explanation": "Le texte dit : « Paul lui dit merci et raccroche »."},
         ]},
        {"id": "a2cix-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2cixo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "téléphone", "à", "son", "frère"], "explanation": "Verbe indirect téléphoner à + personne."},
            {"id": "a2cixo2", "prompt": "Remets les mots en ordre.", "words": ["Son", "frère", "lui", "explique", "la", "solution"], "explanation": "Pronom COI lui devant le verbe conjugué."},
         ]},
    ],
    "a2-les-verbes-pronominaux": [
        {"id": "a2vpx-reading", "type": "reading-comprehension", "title": "Lecture : Le Matin de Léo",
         "passage": "<p>Chaque matin, je me réveille à six heures. Je me lave rapidement, puis je m'habille. Mon frère, lui, se lève toujours plus tard. Hier soir, nous nous sommes couchés très tard après le film.</p>",
         "items": [
            {"id": "a2vpxr1", "prompt": "À quelle heure se réveille la personne ?", "options": ["À six heures", "À sept heures", "À huit heures"], "answerIndex": 0, "explanation": "Le texte dit : « je me réveille à six heures »."},
            {"id": "a2vpxr2", "prompt": "Que fait-elle après s'être lavée ?", "options": ["Elle s'habille", "Elle se recouche", "Elle mange"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2vpxr3", "prompt": "Comment se lève le frère ?", "options": ["Plus tard", "Plus tôt", "À la même heure"], "answerIndex": 0, "explanation": "Le texte dit : « se lève toujours plus tard »."},
            {"id": "a2vpxr4", "prompt": "Quand se sont-ils couchés très tard ?", "options": ["Hier soir, après le film", "Ce matin", "La semaine dernière"], "answerIndex": 0, "explanation": "Le texte se termine par « Hier soir … après le film »."},
         ]},
        {"id": "a2vpx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2vpxo1", "prompt": "Remets les mots en ordre.", "words": ["Je", "me", "réveille", "à", "six", "heures"], "explanation": "Pronom réfléchi me devant le verbe conjugué."},
            {"id": "a2vpxo2", "prompt": "Remets les mots en ordre.", "words": ["Nous", "nous", "sommes", "couchés", "très", "tard"], "explanation": "Passé composé pronominal avec être, accord au sujet."},
         ]},
    ],
    "a2-limperatif": [
        {"id": "a2ipx-reading", "type": "reading-comprehension", "title": "Lecture : Départ en Taxi",
         "passage": "<p>Écoute bien les instructions. Prends ton sac et n'oublie pas ton passeport. Ne t'inquiète pas, tout va bien se passer. Allons-y, le taxi nous attend !</p>",
         "items": [
            {"id": "a2ipxr1", "prompt": "Que faut-il écouter ?", "options": ["Les instructions", "La radio", "Le téléphone"], "answerIndex": 0, "explanation": "Le texte commence par « Écoute bien les instructions »."},
            {"id": "a2ipxr2", "prompt": "Qu'est-ce qu'il ne faut pas oublier ?", "options": ["Le passeport", "Le téléphone", "Les clés"], "answerIndex": 0, "explanation": "Le texte dit : « n'oublie pas ton passeport »."},
            {"id": "a2ipxr3", "prompt": "Que dit-on pour rassurer la personne ?", "options": ["Ne t'inquiète pas", "Dépêche-toi", "Attends ici"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2ipxr4", "prompt": "Qui attend, selon le texte ?", "options": ["Le taxi", "L'avion", "Le train"], "answerIndex": 0, "explanation": "Le texte se termine par « le taxi nous attend »."},
         ]},
        {"id": "a2ipx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2ipxo1", "prompt": "Remets les mots en ordre.", "words": ["Prends", "ton", "sac", "et", "ton", "passeport"], "explanation": "Impératif tu, verbe en -re, sans -s."},
            {"id": "a2ipxo2", "prompt": "Remets les mots en ordre.", "words": ["Ne", "t'inquiète", "pas"], "explanation": "Impératif négatif, pronom devant le verbe."},
         ]},
    ],
    "a2-le-conditionnel-present": [
        {"id": "a2cpx-reading", "type": "reading-comprehension", "title": "Lecture : Un Rêve de Voyage",
         "passage": "<p>Je voudrais visiter le Japon un jour. Ce serait un rêve pour moi. Mes amis aimeraient venir aussi, et nous pourrions découvrir Tokyo ensemble. Ça serait vraiment formidable.</p>",
         "items": [
            {"id": "a2cpxr1", "prompt": "Que voudrait faire la personne ?", "options": ["Visiter le Japon", "Visiter la Chine", "Visiter l'Italie"], "answerIndex": 0, "explanation": "Le texte dit : « Je voudrais visiter le Japon »."},
            {"id": "a2cpxr2", "prompt": "Que serait ce voyage pour elle ?", "options": ["Un rêve", "Une obligation", "Un problème"], "answerIndex": 0, "explanation": "Le texte dit : « Ce serait un rêve pour moi »."},
            {"id": "a2cpxr3", "prompt": "Que voudraient faire ses amis ?", "options": ["Venir aussi", "Rester à la maison", "Aller ailleurs"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2cpxr4", "prompt": "Comment serait l'expérience, selon le texte ?", "options": ["Formidable", "Fatigante", "Compliquée"], "answerIndex": 0, "explanation": "Le texte se termine par « Ça serait vraiment formidable »."},
         ]},
        {"id": "a2cpx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2cpxo1", "prompt": "Remets les mots en ordre.", "words": ["Je", "voudrais", "visiter", "le", "Japon"], "explanation": "Conditionnel de souhait, radical irrégulier voudr-."},
            {"id": "a2cpxo2", "prompt": "Remets les mots en ordre.", "words": ["Nous", "pourrions", "découvrir", "Tokyo", "ensemble"], "explanation": "Conditionnel de pouvoir, radical pourr-."},
         ]},
    ],
    "a2-les-indefinis": [
        {"id": "a2inx-reading", "type": "reading-comprehension", "title": "Lecture : La Fête chez Nous",
         "passage": "<p>Il y a quelqu'un à la porte ; va voir qui c'est. Chaque invité a apporté quelque chose à manger. Plusieurs amis sont déjà arrivés. Tout le monde est content d'être ici ce soir.</p>",
         "items": [
            {"id": "a2inxr1", "prompt": "Que faut-il faire quand quelqu'un frappe ?", "options": ["Aller voir qui c'est", "Ne pas répondre", "Attendre"], "answerIndex": 0, "explanation": "Le texte dit : « va voir qui c'est »."},
            {"id": "a2inxr2", "prompt": "Qu'a apporté chaque invité ?", "options": ["Quelque chose à manger", "Une boisson seulement", "Rien du tout"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a2inxr3", "prompt": "Combien d'amis sont déjà arrivés ?", "options": ["Plusieurs", "Un seul", "Aucun"], "answerIndex": 0, "explanation": "Le texte dit : « Plusieurs amis sont déjà arrivés »."},
            {"id": "a2inxr4", "prompt": "Comment est tout le monde, selon le texte ?", "options": ["Content", "Fatigué", "Inquiet"], "answerIndex": 0, "explanation": "Le texte se termine par « Tout le monde est content »."},
         ]},
        {"id": "a2inx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2inxo1", "prompt": "Remets les mots en ordre.", "words": ["Chaque", "invité", "a", "apporté", "quelque", "chose"], "explanation": "Chaque, invariable, devant un nom singulier."},
            {"id": "a2inxo2", "prompt": "Remets les mots en ordre.", "words": ["Tout", "le", "monde", "est", "content"], "explanation": "Tout le monde, masculin singulier invariable dans cette expression."},
         ]},
    ],
    "a2-y-et-en": [
        {"id": "a2yex-reading", "type": "reading-comprehension", "title": "Lecture : Léa à Paris",
         "passage": "<p>Léa adore Paris ; elle y habite depuis cinq ans. Elle vient de Marseille, mais elle n'y retourne pas souvent. Elle a deux frères là-bas, et elle en parle avec tendresse. Elle en a de beaux souvenirs.</p>",
         "items": [
            {"id": "a2yexr1", "prompt": "Depuis quand Léa habite-t-elle à Paris ?", "options": ["Cinq ans", "Deux ans", "Dix ans"], "answerIndex": 0, "explanation": "Le texte dit : « elle y habite depuis cinq ans »."},
            {"id": "a2yexr2", "prompt": "D'où vient Léa ?", "options": ["De Marseille", "De Lyon", "De Nice"], "answerIndex": 0, "explanation": "Le texte dit : « Elle vient de Marseille »."},
            {"id": "a2yexr3", "prompt": "Combien de frères a-t-elle ?", "options": ["Deux", "Un", "Trois"], "answerIndex": 0, "explanation": "Le texte dit : « Elle a deux frères là-bas »."},
            {"id": "a2yexr4", "prompt": "Comment parle-t-elle de sa famille ?", "options": ["Avec tendresse", "Avec indifférence", "Avec tristesse"], "answerIndex": 0, "explanation": "Le texte dit : « elle en parle avec tendresse »."},
         ]},
        {"id": "a2yex-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2yexo1", "prompt": "Remets les mots en ordre.", "words": ["Elle", "y", "habite", "depuis", "cinq", "ans"], "explanation": "Y remplace à Paris, placé avant le verbe."},
            {"id": "a2yexo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "en", "parle", "avec", "tendresse"], "explanation": "En remplace de ses frères, placé avant le verbe."},
         ]},
    ],
    "a2-les-prepositions-avec-les-pays-et-les-villes": [
        {"id": "a2ppx-reading", "type": "reading-comprehension", "title": "Lecture : Le Parcours de Sarah",
         "passage": "<p>Sarah vit à Berlin, en Allemagne, depuis deux ans. Avant, elle habitait au Portugal, dans la ville de Porto. Elle vient d'une grande famille, originaire des Philippines. Cet été, elle ira aux Pays-Bas pour les vacances.</p>",
         "items": [
            {"id": "a2ppxr1", "prompt": "Où vit Sarah actuellement ?", "options": ["À Berlin, en Allemagne", "À Porto, au Portugal", "Aux Pays-Bas"], "answerIndex": 0, "explanation": "Le texte dit : « Sarah vit à Berlin, en Allemagne »."},
            {"id": "a2ppxr2", "prompt": "Où habitait-elle avant ?", "options": ["Au Portugal, à Porto", "En Allemagne", "Aux Philippines"], "answerIndex": 0, "explanation": "Le texte dit : « elle habitait au Portugal, dans la ville de Porto »."},
            {"id": "a2ppxr3", "prompt": "D'où vient sa famille, à l'origine ?", "options": ["Des Philippines", "Du Portugal", "De Berlin"], "answerIndex": 0, "explanation": "Le texte dit : « originaire des Philippines »."},
            {"id": "a2ppxr4", "prompt": "Où ira-t-elle cet été ?", "options": ["Aux Pays-Bas", "Au Portugal", "En Allemagne"], "answerIndex": 0, "explanation": "Le texte se termine par « elle ira aux Pays-Bas »."},
         ]},
        {"id": "a2ppx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a2ppxo1", "prompt": "Remets les mots en ordre.", "words": ["Elle", "vit", "à", "Berlin", "en", "Allemagne"], "explanation": "À devant une ville, en devant un pays féminin."},
            {"id": "a2ppxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "ira", "aux", "Pays-Bas", "cet", "été"], "explanation": "Aux devant un pays pluriel."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
