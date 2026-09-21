# -*- coding: utf-8 -*-
"""A1 — Données du curriculum de niveau débutant. Voir curriculum/SCHEMA.md
pour la forme exacte du JSON vers lequel ceci est compilé (scripts/generate_curriculum.py
fait la compilation). Écrit en Python plutôt qu'en JSON à la main pour que le
HTML en ligne (rules[].body, content.explanation) et les guillemets dans le
texte puissent s'écrire naturellement."""

OVERVIEW = (
    "Le niveau A1 construit les vraies bases du français : la liaison et les "
    "groupes de lettres pour bien prononcer, le genre et le nombre des noms, "
    "les articles définis, indéfinis et contractés, la distinction entre il y "
    "a, c'est et il est, les pronoms sujets et toniques, et la conjugaison du "
    "présent — aussi bien les verbes réguliers en -er que les irréguliers les "
    "plus fréquents (aller, faire, prendre, pouvoir, devoir). Tu apprendras "
    "aussi à décrire des personnes et des choses avec des adjectifs, des "
    "possessifs et des démonstratifs, à situer dans l'espace et dans le temps "
    "avec les prépositions, à poser des questions, à exprimer tes goûts avec "
    "aimer/adorer/détester, et à parler de tes projets proches avec le futur "
    "proche. À la fin de ce niveau, tu pourras te présenter en détail, "
    "décrire ton entourage, poser des questions variées et parler de ce que "
    "tu vas faire bientôt."
)

LESSONS = [
    {
        "id": "a1-la-prononciation-avancee",
        "level": "A1", "unit": "1", "order": 1, "skill": "pronunciation", "strand": "liaison",
        "title": "La Prononciation Avancée : Liaisons, Groupes de Lettres et Intonation",
        "subtitle": "Comment les mots s'enchaînent à l'oral, comment prononcer ai/au/ou/oi/gn/ch/qu, et comment la voix marque une question.",
        "objectives": [
            "Distinguer la liaison obligatoire de la liaison interdite dans des exemples courants.",
            "Reconnaître la prononciation des principaux groupes de lettres (ai, au/eau, ou, oi, gn, ch, qu).",
            "Utiliser une intonation montante pour une question oui/non et descendante pour une affirmation.",
        ],
        "content": {
            "intro": "Après l'alphabet et les sons de base, il est temps d'aller plus loin : comment les mots s'enchaînent entre eux à l'oral, et comment la voix seule peut transformer une phrase en question.",
            "explanation": "<p>La <strong>liaison</strong> consiste à prononcer une consonne finale normalement muette quand le mot suivant commence par une voyelle. Elle est <strong>obligatoire</strong> après un article ou un déterminant (<em>les amis</em>), après un pronom sujet (<em>vous avez</em>), ou après certaines prépositions courtes (<em>chez eux</em>). Elle est en revanche <strong>interdite</strong> après <em>et</em> (<em>et elle</em>, jamais «&nbsp;ét-elle&nbsp;»), et devant un mot commençant par un <strong>h aspiré</strong> (<em>les / héros</em>, sans liaison, même si le h ne se prononce pas lui-même).</p><p>Certains groupes de lettres se prononcent toujours de la même façon en français, comme une seule unité : <strong>ai/ei</strong> → un son ouvert comme dans <em>fait</em> ; <strong>au/eau</strong> → un son fermé comme dans <em>chaud</em> ; <strong>ou</strong> → comme dans <em>vous</em> ; <strong>oi</strong> → comme dans <em>moi</em> ; <strong>gn</strong> → comme dans <em>montagne</em> ; <strong>ch</strong> → comme dans <em>chat</em> ; <strong>qu</strong> → comme un k, comme dans <em>qui</em>. Enfin, à l'oral, une question sans mot interrogatif (<em>Tu viens ?</em>) se reconnaît surtout à l'<strong>intonation montante</strong> à la fin de la phrase ; une affirmation garde une intonation descendante.</p>",
            "rules": [
                {"heading": "a) La liaison obligatoire", "body": "<ul><li>Article/déterminant + nom : <em>les amis, un enfant, mes amis</em>.</li><li>Pronom sujet + verbe : <em>vous avez, ils ont, nous en avons</em>.</li><li>Préposition courte + mot : <em>chez eux, dans un sac, sous un arbre</em>.</li></ul>"},
                {"heading": "b) La liaison interdite", "body": "<ul><li>Après <em>et</em> : <em>et elle</em> (jamais de liaison après <em>et</em>).</li><li>Devant un h aspiré : <em>les / héros, les / haricots</em>.</li><li>Après un nom singulier, avant un adjectif : généralement pas de liaison à ce niveau.</li></ul>"},
                {"heading": "c) Groupes de lettres fréquents", "body": "<ul><li><strong>ai/ei</strong> → <em>fait, treize</em>.</li><li><strong>au/eau</strong> → <em>chaud, gâteau</em>.</li><li><strong>ou</strong> → <em>vous, rouge</em>.</li><li><strong>oi</strong> → <em>moi, voiture</em>.</li><li><strong>gn</strong> → <em>montagne, champagne</em>.</li><li><strong>ch</strong> → <em>chat, chien</em>.</li><li><strong>qu</strong> → <em>qui, quatre</em> (jamais «&nbsp;kw&nbsp;»).</li></ul>"},
                {"heading": "d) L'intonation", "body": "<ul><li>Question oui/non sans mot interrogatif : la voix <strong>monte</strong> à la fin — <em>Tu viens ?</em></li><li>Affirmation ou question avec mot interrogatif : la voix <strong>descend</strong> à la fin — <em>Tu viens avec nous.</em> / <em>Où est-ce que tu vas ?</em></li></ul>"},
            ],
            "examples": [
                "Les amis arrivent bientôt.",
                "Vous avez de la chance.",
                "Les héros ne sont pas des surhommes.",
                "Le gâteau est encore chaud.",
                "Je voudrais un peu d'eau, s'il vous plaît.",
                "Le chien s'appelle Champagne.",
                "Tu viens avec nous ?",
                "Où est-ce que tu habites ?",
            ],
            "commonMistakes": [
                {"wrong": "Faire la liaison entre les et héros.", "right": "Ne pas faire de liaison devant un h aspiré : les / héros.", "why": "Le h aspiré bloque la liaison, même s'il ne se prononce pas lui-même."},
                {"wrong": "Prononcer au et eau comme deux sons séparés.", "right": "Prononcer au/eau comme un seul son fermé, proche du o.", "why": "Ce sont des digraphes : une seule unité sonore, pas la somme de leurs lettres."},
                {"wrong": "Garder une intonation plate pour poser une question oui/non.", "right": "Faire monter la voix à la fin de la question : Tu viens ?", "why": "À l'oral, l'intonation montante est souvent le seul signal qu'une phrase est une question sans mot interrogatif."},
            ],
        },
        "exercises": [
            {"id": "a1pr-fill", "type": "fill-blank", "title": "Complète avec le Bon Mot",
             "instructions": "Choisis l'orthographe correcte pour chaque espace.",
             "items": [
                {"id": "a1prf1", "prompt": "Il fait ___ chaud aujourd'hui.", "answers": [["beaucoup"]], "options": ["beaucoup", "boucoup", "beaucou"], "explanation": "Beaucoup se termine par -oup, avec un p final muet."},
                {"id": "a1prf2", "prompt": "Je voudrais un peu d'___, s'il vous plaît.", "answers": [["eau"]], "options": ["eau", "au", "ault"], "explanation": "Le son [o] s'écrit eau dans ce mot."},
                {"id": "a1prf3", "prompt": "As-tu vu les ___ dans le jardin ?", "answers": [["oiseaux"]], "options": ["oiseaux", "oizeaux", "oiseau"], "explanation": "Oiseaux combine oi et eau, et prend un x au pluriel."},
                {"id": "a1prf4", "prompt": "Le ___ de la voisine aboie beaucoup.", "answers": [["chien"]], "options": ["chien", "chien s", "shien"], "explanation": "Ch se prononce toujours [ʃ], jamais comme le sh anglais à l'écrit."},
             ]},
            {"id": "a1pr-mc", "type": "multiple-choice", "title": "Prononciation et Liaison",
             "items": [
                {"id": "a1prm1", "prompt": "Quelle phrase contient une liaison obligatoire ?", "options": ["Les amis arrivent.", "Les héros arrivent.", "Et elle arrive."], "answerIndex": 0, "explanation": "Article pluriel + nom commençant par une voyelle : liaison obligatoire."},
                {"id": "a1prm2", "prompt": "Comment se prononce le groupe oi dans moi ?", "options": ["wa", "o-i séparés", "un o long"], "answerIndex": 0, "explanation": "Oi se prononce toujours [wa] en français."},
                {"id": "a1prm3", "prompt": "Quel son fait le groupe gn dans montagne ?", "options": ["comme ni (ɲ)", "comme un g dur", "comme un n simple"], "answerIndex": 0, "explanation": "Gn correspond au son [ɲ], proche du ni de oignon."},
                {"id": "a1prm4", "prompt": "Une question comme « Tu viens ? » sans mot interrogatif se reconnaît surtout par…", "options": ["l'intonation montante à la fin", "l'ordre des mots", "un accent écrit"], "answerIndex": 0, "explanation": "À l'oral, la montée de la voix signale la question."},
             ]},
            {"id": "a1pr-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1prc1", "incorrect": "Je voudrais un peu d'au.", "answer": ["Je voudrais un peu d'eau."], "explanation": "Le son [o] de ce mot s'écrit eau, pas au."},
                {"id": "a1prc2", "incorrect": "Il y a un chien qui s'apelle Bruno.", "answer": ["Il y a un chien qui s'appelle Bruno."], "explanation": "S'appeler prend deux p."},
                {"id": "a1prc3", "incorrect": "Ou est la gare, s'il vous plaît ?", "answer": ["Où est la gare, s'il vous plaît ?"], "explanation": "Où (lieu) prend un accent grave ; sans accent, ou signifie « ou bien »."},
             ]},
        ],
        "summary": [
            "La liaison relie une consonne finale muette à la voyelle du mot suivant dans des contextes précis (article+nom, pronom+verbe) ; elle est bloquée devant un h aspiré et après et.",
            "Les groupes ai/au/eau/ou/oi/gn/ch/qu correspondent chacun à un seul son fixe, à mémoriser comme des unités.",
            "L'intonation montante marque une question oui/non ; l'intonation descendante marque une affirmation ou une question avec mot interrogatif.",
        ],
    },
    {
        "id": "a1-le-genre-et-le-nombre-des-noms",
        "level": "A1", "unit": "1", "order": 2, "skill": "grammar", "strand": "genre-nombre",
        "title": "Le Genre et le Nombre des Noms",
        "subtitle": "Comment reconnaître le masculin et le féminin d'un nom, et comment former le pluriel.",
        "objectives": [
            "Reconnaître des terminaisons typiquement masculines ou féminines.",
            "Former le pluriel régulier des noms et reconnaître les pluriels irréguliers les plus courants.",
            "Éviter les pièges des noms qui semblent féminins mais sont masculins, et inversement.",
        ],
        "content": {
            "intro": "En français, chaque nom a un genre — masculin ou féminin — et ce genre influence l'article, l'adjectif et parfois le pronom qui l'accompagnent : c'est une information à apprendre dès le premier jour, en même temps que le mot lui-même.",
            "explanation": "<p>Il n'existe pas de règle universelle pour deviner le genre d'un nom, mais certaines <strong>terminaisons</strong> sont de bons indices : les mots en <em>-tion, -sion, -té, -ette, -ance</em> sont presque toujours féminins ; les mots en <em>-eau, -age, -ment, -isme</em> sont presque toujours masculins. Il faut cependant apprendre chaque nom avec son article dès le début, car il existe de nombreuses exceptions (<em>le problème</em>, <em>la page</em>).</p><p>Le <strong>pluriel</strong> se forme le plus souvent en ajoutant un <strong>-s</strong> final, qui reste muet à l'oral (<em>un livre → des livres</em>). Les noms terminés en <em>-eau, -eu</em> prennent un <strong>-x</strong> (<em>un bateau → des bateaux</em>), et beaucoup de noms en <em>-al</em> deviennent <em>-aux</em> (<em>un cheval → des chevaux</em>). Quelques pluriels sont irréguliers et doivent être mémorisés directement, comme <em>un œil → des yeux</em>.</p>",
            "rules": [
                {"heading": "a) Indices de genre", "body": "<ul><li>Souvent féminins : <em>-tion</em> (la nation), <em>-té</em> (la beauté), <em>-ette</em> (la fourchette).</li><li>Souvent masculins : <em>-eau</em> (le bureau), <em>-age</em> (le fromage), <em>-ment</em> (le moment).</li><li>Exceptions courantes à mémoriser : <em>le problème, la page, le silence</em>.</li></ul>"},
                {"heading": "b) Le pluriel régulier", "body": "<ul><li>Cas général : ajouter -s — <em>un livre → des livres</em> (le -s ne se prononce pas).</li><li>Noms en -eau/-eu : ajouter -x — <em>un bateau → des bateaux, un jeu → des jeux</em>.</li><li>Noms déjà en -s, -x, -z : ne changent pas — <em>un pays → des pays</em>.</li></ul>"},
                {"heading": "c) Le pluriel irrégulier", "body": "<ul><li>Beaucoup de noms en -al → -aux : <em>un cheval → des chevaux, un journal → des journaux</em>.</li><li>Quelques pluriels totalement irréguliers : <em>un œil → des yeux</em>.</li><li>Un œuf [œf] se prononce différemment au pluriel des œufs [ø], bien que l'orthographe suive la règle générale (+s).</li></ul>"},
            ],
            "examples": [
                "Le bureau est grand ; les bureaux sont neufs.",
                "La beauté de ce jardin est incroyable.",
                "Un cheval blanc ; des chevaux blancs.",
                "J'ai mal à un œil ; elle a de beaux yeux.",
                "Le problème, c'est le prix.",
                "Des livres et des journaux sont sur la table.",
            ],
            "commonMistakes": [
                {"wrong": "Dire la problème, en pensant que -ème est féminin.", "right": "Dire le problème : ce nom est masculin malgré sa terminaison en -e.", "why": "La terminaison -e n'indique pas fiablement le genre ; le problème fait partie des exceptions à mémoriser."},
                {"wrong": "Dire des chevals au pluriel.", "right": "Dire des chevaux.", "why": "Les noms en -al forment souvent leur pluriel en -aux, pas en -als."},
                {"wrong": "Prononcer le -s final du pluriel dans des livres.", "right": "Ne pas prononcer le -s final : des livres se prononce comme livre.", "why": "Le -s du pluriel est presque toujours muet à l'oral en français ; c'est l'article (le/les) qui marque le nombre à l'oreille."},
            ],
        },
        "exercises": [
            {"id": "a1gn-fill", "type": "fill-blank", "title": "Forme le Pluriel",
             "instructions": "Écris la forme correcte pour chaque espace.",
             "items": [
                {"id": "a1gnf1", "prompt": "Un cheval, des ___.", "answers": [["chevaux"]], "options": ["chevaux", "chevals", "chevaus"], "explanation": "Les noms en -al font souvent leur pluriel en -aux."},
                {"id": "a1gnf2", "prompt": "Un bateau, des ___.", "answers": [["bateaux"]], "options": ["bateaux", "bateaus", "bateax"], "explanation": "Les noms en -eau prennent un x au pluriel."},
                {"id": "a1gnf3", "prompt": "Un œil, des ___.", "answers": [["yeux"]], "options": ["yeux", "œils", "oeuils"], "explanation": "Œil a un pluriel totalement irrégulier : yeux."},
                {"id": "a1gnf4", "prompt": "Un pays, des ___.", "answers": [["pays"]], "options": ["pays", "payes", "pais"], "explanation": "Les noms déjà terminés en -s ne changent pas au pluriel."},
             ]},
            {"id": "a1gn-mc", "type": "multiple-choice", "title": "Masculin ou Féminin ?",
             "items": [
                {"id": "a1gnm1", "prompt": "Quel est le genre de nation ?", "options": ["féminin", "masculin", "les deux"], "answerIndex": 0, "explanation": "Les noms en -tion sont presque toujours féminins."},
                {"id": "a1gnm2", "prompt": "Quel est le genre de problème ?", "options": ["masculin", "féminin", "les deux"], "answerIndex": 0, "explanation": "Problème fait partie des exceptions masculines malgré sa terminaison en -e."},
                {"id": "a1gnm3", "prompt": "Comment se forme le pluriel de journal ?", "options": ["journaux", "journals", "journales"], "answerIndex": 0, "explanation": "Journal suit la règle -al → -aux."},
                {"id": "a1gnm4", "prompt": "Le -s du pluriel de livres se prononce-t-il ?", "options": ["Non, il est muet", "Oui, comme un s", "Oui, comme un z"], "answerIndex": 0, "explanation": "Le -s du pluriel est muet à l'oral dans la grande majorité des cas."},
             ]},
            {"id": "a1gn-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1gnc1", "incorrect": "La problème est difficile.", "answer": ["Le problème est difficile."], "explanation": "Problème est masculin malgré sa terminaison en -e."},
                {"id": "a1gnc2", "incorrect": "Des chevals courent dans le champ.", "answer": ["Des chevaux courent dans le champ."], "explanation": "Le pluriel de cheval est chevaux, pas chevals."},
                {"id": "a1gnc3", "incorrect": "Un bureaux est dans la salle.", "answer": ["Un bureau est dans la salle."], "explanation": "Au singulier, c'est bureau, sans x ; le x n'apparaît qu'au pluriel."},
             ]},
        ],
        "summary": [
            "Le genre d'un nom se devine parfois par sa terminaison (-tion/-té féminins, -eau/-age masculins), mais il faut apprendre chaque nom avec son article, car les exceptions sont nombreuses.",
            "Le pluriel régulier ajoute -s (muet à l'oral) ; les noms en -eau/-eu ajoutent -x, et beaucoup de noms en -al deviennent -aux.",
            "Quelques pluriels sont irréguliers et doivent être mémorisés directement, comme œil → yeux.",
        ],
    },
    {
        "id": "a1-les-articles-definis-indefinis-et-contractes",
        "level": "A1", "unit": "1", "order": 3, "skill": "grammar", "strand": "articles",
        "title": "Les Articles Définis, Indéfinis et Contractés",
        "subtitle": "Le/la/l'/les, un/une/des, et les contractions au/aux/du/des avec à et de.",
        "objectives": [
            "Utiliser le/la/l'/les et un/une/des selon le genre, le nombre et la lettre initiale du nom.",
            "Former et utiliser les articles contractés avec à (au/à la/à l'/aux) et de (du/de la/de l'/des).",
            "Distinguer l'article défini (chose connue ou catégorie générale) de l'article indéfini (chose non précisée).",
        ],
        "content": {
            "intro": "Les articles accompagnent presque tous les noms en français, et leur forme change selon le genre, le nombre, et même selon la préposition qui les précède.",
            "explanation": "<p>L'article <strong>défini</strong> (<em>le, la, l', les</em>) désigne une chose déjà connue ou une catégorie générale : <em>Le café est excellent ici</em>. L'article <strong>indéfini</strong> (<em>un, une, des</em>) désigne une chose non précisée : <em>J'ai un chat</em>. Devant une voyelle ou un h muet, <em>le</em> et <em>la</em> deviennent toujours <strong>l'</strong> : <em>l'école, l'homme</em>.</p><p>Après les prépositions <strong>à</strong> et <strong>de</strong>, les articles <em>le</em> et <em>les</em> se contractent obligatoirement : <em>à + le → au</em>, <em>à + les → aux</em>, <em>de + le → du</em>, <em>de + les → des</em>. En revanche, <em>à la, à l', de la, de l'</em> ne changent jamais de forme.</p>",
            "rules": [
                {"heading": "a) Articles définis", "body": "<ul><li><strong>le</strong> (masculin singulier) — <em>le café</em>.</li><li><strong>la</strong> (féminin singulier) — <em>la piscine</em>.</li><li><strong>l'</strong> (devant voyelle ou h muet) — <em>l'école, l'homme</em>.</li><li><strong>les</strong> (pluriel) — <em>les enfants</em>.</li></ul>"},
                {"heading": "b) Articles indéfinis", "body": "<ul><li><strong>un</strong> (masculin) — <em>un chat</em>.</li><li><strong>une</strong> (féminin) — <em>une chienne</em>.</li><li><strong>des</strong> (pluriel) — <em>des amis</em>.</li></ul>"},
                {"heading": "c) Contractions avec à", "body": "<ul><li>à + le → <strong>au</strong> — <em>au cinéma</em>.</li><li>à + les → <strong>aux</strong> — <em>aux toilettes</em>.</li><li>à + la / à + l' ne changent pas — <em>à la piscine, à l'école</em>.</li></ul>"},
                {"heading": "d) Contractions avec de", "body": "<ul><li>de + le → <strong>du</strong> — <em>du pain</em>.</li><li>de + les → <strong>des</strong> — <em>des enfants du quartier</em>.</li><li>de + la / de + l' ne changent pas — <em>de la confiture, de l'eau</em>.</li></ul>"},
            ],
            "examples": [
                "Je vais au cinéma ce soir.",
                "Elle boit de l'eau fraîche.",
                "Nous parlons des enfants du quartier.",
                "J'ai un chat et une chienne.",
                "Le café est excellent ici.",
                "Les élèves aiment l'école.",
            ],
            "commonMistakes": [
                {"wrong": "Je vais à le cinéma.", "right": "Je vais au cinéma.", "why": "à + le se contracte toujours en au ; « à le » n'existe jamais en français."},
                {"wrong": "la eau", "right": "l'eau", "why": "le et la deviennent toujours l' devant une voyelle ou un h muet."},
                {"wrong": "J'aime un café le matin, en général.", "right": "J'aime le café, en général.", "why": "Pour parler d'une catégorie générale ou d'une préférence, le français utilise l'article défini, pas l'indéfini."},
            ],
        },
        "exercises": [
            {"id": "a1ar-fill", "type": "fill-blank", "title": "Complète avec l'Article Correct",
             "instructions": "Choisis la forme correcte pour chaque espace.",
             "items": [
                {"id": "a1arf1", "prompt": "Je vais ___ cinéma ce soir.", "answers": [["au"]], "options": ["au", "à le", "a"], "explanation": "à + le se contracte obligatoirement en au."},
                {"id": "a1arf2", "prompt": "Elle boit ___ eau fraîche.", "answers": [["de l'"]], "options": ["de l'", "de la", "du"], "explanation": "de + l' ne change pas devant une voyelle."},
                {"id": "a1arf3", "prompt": "Nous parlons ___ enfants du quartier.", "answers": [["des"]], "options": ["des", "de les", "de le"], "explanation": "de + les se contracte obligatoirement en des."},
                {"id": "a1arf4", "prompt": "___ élèves aiment l'école.", "answers": [["Les"]], "options": ["Les", "Le", "La"], "explanation": "Article défini pluriel devant un nom au pluriel."},
             ]},
            {"id": "a1ar-mc", "type": "multiple-choice", "title": "Articles et Contractions",
             "items": [
                {"id": "a1arm1", "prompt": "Comment dit-on à + les ?", "options": ["aux", "à les", "als"], "answerIndex": 0, "explanation": "à + les se contracte toujours en aux."},
                {"id": "a1arm2", "prompt": "Quel article utilise-t-on devant un nom féminin commençant par une voyelle ?", "options": ["l'", "la", "le"], "answerIndex": 0, "explanation": "la devient l' devant une voyelle ou un h muet."},
                {"id": "a1arm3", "prompt": "Pour parler d'une catégorie générale (« Le café est bon »), on utilise…", "options": ["l'article défini", "l'article indéfini", "aucun article"], "answerIndex": 0, "explanation": "Une catégorie générale ou une préférence prend l'article défini en français."},
                {"id": "a1arm4", "prompt": "Comment dit-on de + le ?", "options": ["du", "de le", "del"], "answerIndex": 0, "explanation": "de + le se contracte obligatoirement en du."},
             ]},
            {"id": "a1ar-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1arc1", "incorrect": "Je vais à le cinéma.", "answer": ["Je vais au cinéma."], "explanation": "à + le devient toujours au."},
                {"id": "a1arc2", "incorrect": "Elle boit la eau.", "answer": ["Elle boit de l'eau."], "explanation": "L'article se contracte en l' devant une voyelle : de l'eau, pas la eau."},
                {"id": "a1arc3", "incorrect": "Nous parlons de les enfants.", "answer": ["Nous parlons des enfants."], "explanation": "de + les devient toujours des."},
             ]},
        ],
        "summary": [
            "Les articles définis (le/la/l'/les) désignent une chose connue ou une catégorie générale ; les indéfinis (un/une/des) désignent une chose non précisée.",
            "à + le devient au, à + les devient aux ; de + le devient du, de + les devient des — des contractions obligatoires.",
            "Devant une voyelle ou un h muet, le et la deviennent toujours l'.",
        ],
    },
    {
        "id": "a1-il-y-a-cest-et-il-est",
        "level": "A1", "unit": "1", "order": 4, "skill": "grammar", "strand": "identification",
        "title": "Il y a, C'est et Il est",
        "subtitle": "Comment affirmer l'existence, identifier une personne ou une chose, et décrire une caractéristique.",
        "objectives": [
            "Utiliser il y a pour affirmer l'existence ou la présence de quelque chose.",
            "Utiliser c'est pour identifier une personne, une chose, ou donner une opinion générale.",
            "Utiliser il/elle est pour décrire une caractéristique ou une profession, sans article.",
        ],
        "content": {
            "intro": "Ces trois structures se traduisent parfois par le même mot dans d'autres langues, mais elles ont chacune un usage précis en français, et les confondre est l'une des erreurs les plus fréquentes des débutants.",
            "explanation": "<p><strong>Il y a</strong> affirme l'existence ou la présence de quelque chose et reste toujours invariable, même au pluriel : <em>Il y a un chat</em> / <em>Il y a des chats</em> (c'est le nom qui prend la marque du pluriel, pas <em>il y a</em>).</p><p><strong>C'est</strong> sert à identifier une personne ou une chose (toujours suivi d'un nom avec son article) ou à donner une opinion générale : <em>C'est mon frère. C'est une bonne idée.</em> <strong>Il/elle est</strong> sert plutôt à décrire, avec un adjectif seul ou une profession <em>sans article</em> : <em>Il est fatigué. Elle est professeure.</em> Avec <em>c'est</em>, en revanche, la profession reprend son article : <em>C'est un professeur très patient.</em></p>",
            "rules": [
                {"heading": "a) Il y a", "body": "<ul><li>Forme fixe, jamais accordée : <em>Il y a un problème / Il y a des problèmes</em>.</li><li>Sert à affirmer l'existence ou la présence de quelque chose.</li></ul>"},
                {"heading": "b) C'est + nom", "body": "<ul><li>Identifie qui ou quoi c'est : <em>C'est mon frère. C'est une bonne idée.</em></li><li>Le nom garde toujours son article : <em>C'est un professeur</em>.</li></ul>"},
                {"heading": "c) Il/elle est + adjectif ou profession", "body": "<ul><li>Décrit une caractéristique : <em>Il est fatigué. Elle est intelligente.</em></li><li>Profession sans article : <em>Elle est professeure</em> (jamais « elle est une professeure »).</li></ul>"},
                {"heading": "d) Le piège de la profession", "body": "<ul><li>Avec <em>il/elle est</em> : pas d'article — <em>Il est médecin</em>.</li><li>Avec <em>c'est</em> : article obligatoire — <em>C'est un médecin</em>.</li></ul>"},
            ],
            "examples": [
                "Il y a un chat sur le canapé.",
                "Il y a beaucoup de monde ici.",
                "C'est mon frère Paul.",
                "C'est une bonne idée.",
                "Il est fatigué aujourd'hui.",
                "Elle est professeure de mathématiques.",
                "C'est un professeur très patient.",
            ],
            "commonMistakes": [
                {"wrong": "Il y a des problème.", "right": "Il y a des problèmes.", "why": "Le nom prend la marque du pluriel même si il y a reste toujours invariable."},
                {"wrong": "Elle est une professeure.", "right": "Elle est professeure. (ou : C'est une professeure.)", "why": "Il/elle est + profession ne prend jamais d'article ; c'est un professeur, en revanche, en prend un."},
                {"wrong": "C'est fatigué.", "right": "Il est fatigué.", "why": "Un adjectif seul décrivant un sujet déjà connu utilise il/elle est, pas c'est, qui s'utilise surtout avec un nom."},
            ],
        },
        "exercises": [
            {"id": "a1ie-fill", "type": "fill-blank", "title": "Il y a, C'est ou Il est ?",
             "instructions": "Choisis l'expression correcte pour chaque espace.",
             "items": [
                {"id": "a1ief1", "prompt": "___ beaucoup de monde dans la rue.", "answers": [["Il y a"]], "options": ["Il y a", "C'est", "Il est"], "explanation": "Il y a affirme la présence de quelque chose."},
                {"id": "a1ief2", "prompt": "___ un professeur très patient.", "answers": [["C'est"]], "options": ["C'est", "Il y a", "Il est"], "explanation": "C'est identifie une personne avec un nom accompagné de son article."},
                {"id": "a1ief3", "prompt": "___ fatigué après le travail.", "answers": [["Il est"]], "options": ["Il est", "C'est", "Il y a"], "explanation": "Il est + adjectif seul décrit une caractéristique."},
                {"id": "a1ief4", "prompt": "___ des problèmes à résoudre.", "answers": [["Il y a"]], "options": ["Il y a", "C'est", "Il est"], "explanation": "Il y a affirme l'existence de plusieurs choses."},
             ]},
            {"id": "a1ie-mc", "type": "multiple-choice", "title": "Identifier ou Décrire ?",
             "items": [
                {"id": "a1iem1", "prompt": "Comment dit-on « there are many books » ?", "options": ["Il y a beaucoup de livres.", "C'est beaucoup de livres.", "Il est beaucoup de livres."], "answerIndex": 0, "explanation": "Il y a exprime l'existence de plusieurs choses."},
                {"id": "a1iem2", "prompt": "Quelle phrase est correcte pour une profession sans article ?", "options": ["Il est médecin.", "Il est un médecin.", "C'est médecin."], "answerIndex": 0, "explanation": "Il/elle est + profession n'a jamais d'article."},
                {"id": "a1iem3", "prompt": "Quelle phrase identifie une personne ?", "options": ["C'est Marie.", "Il y a Marie.", "Elle y a Marie."], "answerIndex": 0, "explanation": "C'est + nom propre identifie qui c'est."},
                {"id": "a1iem4", "prompt": "Quelle forme reste toujours invariable, même au pluriel ?", "options": ["Il y a", "C'est", "Il est"], "answerIndex": 0, "explanation": "Seul le nom qui suit il y a change au pluriel, jamais il y a lui-même."},
             ]},
            {"id": "a1ie-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1iec1", "incorrect": "Il y a des problème.", "answer": ["Il y a des problèmes."], "explanation": "Le nom prend le -s du pluriel, même après il y a."},
                {"id": "a1iec2", "incorrect": "Elle est une professeure.", "answer": ["Elle est professeure.", "C'est une professeure."], "explanation": "Pas d'article après il/elle est ; l'article revient avec c'est."},
                {"id": "a1iec3", "incorrect": "C'est fatigué.", "answer": ["Il est fatigué."], "explanation": "Un adjectif seul décrivant un sujet connu utilise il/elle est."},
             ]},
        ],
        "summary": [
            "Il y a affirme l'existence de quelque chose et reste toujours invariable ; c'est le nom qui prend la marque du pluriel.",
            "C'est + nom (avec article) identifie une personne, une chose, ou donne une opinion générale.",
            "Il/elle est + adjectif ou profession (sans article) décrit une caractéristique ; avec c'est, la profession reprend son article.",
        ],
    },
    {
        "id": "a1-les-pronoms-sujets-et-toniques",
        "level": "A1", "unit": "1", "order": 5, "skill": "grammar", "strand": "pronoms",
        "title": "Les Pronoms Sujets et Toniques",
        "subtitle": "Je/tu/il/elle/on/nous/vous/ils/elles, et leurs équivalents toniques moi/toi/lui/elle/nous/vous/eux/elles.",
        "objectives": [
            "Utiliser correctement les pronoms sujets je/tu/il/elle/on/nous/vous/ils/elles.",
            "Utiliser les pronoms toniques (moi/toi/lui/elle/nous/vous/eux/elles) après une préposition ou pour insister.",
            "Employer on comme équivalent familier de nous, conjugué comme il/elle.",
        ],
        "content": {
            "intro": "Le français a deux familles de pronoms personnels selon leur position dans la phrase : les pronoms sujets, toujours devant le verbe, et les pronoms toniques, utilisés seuls ou après une préposition.",
            "explanation": "<p>Les <strong>pronoms sujets</strong> (<em>je, tu, il, elle, on, nous, vous, ils, elles</em>) précèdent toujours le verbe conjugué. <strong>On</strong> est très fréquent à l'oral comme équivalent informel de <em>nous</em>, mais il se conjugue toujours comme <em>il/elle</em> (troisième personne du singulier) : <em>On va au cinéma</em>, pas « on vont ».</p><p>Les <strong>pronoms toniques</strong> (<em>moi, toi, lui, elle, nous, vous, eux, elles</em>) s'utilisent après une préposition (<em>avec moi, chez toi, pour lui</em>), pour insister sur le sujet (<em>Moi, je pense que…</em>), ou seuls dans une réponse courte (<em>— Et toi ? — Moi aussi.</em>).</p>",
            "rules": [
                {"heading": "a) Pronoms sujets", "body": "<ul><li><em>je, tu</em> — 1re et 2e personne du singulier.</li><li><em>il, elle</em> — personnes ou choses ; <em>ils, elles</em> au pluriel.</li><li><em>nous, vous</em> — 1re et 2e personne du pluriel (vous aussi formel de politesse).</li></ul>"},
                {"heading": "b) On", "body": "<ul><li>Équivalent familier de nous à l'oral : <em>On va au cinéma</em> = <em>Nous allons au cinéma</em>.</li><li>Se conjugue toujours comme il/elle, même s'il signifie nous.</li></ul>"},
                {"heading": "c) Pronoms toniques", "body": "<ul><li>Après une préposition : <em>avec moi, chez toi, pour eux</em>.</li><li>Pour insister sur le sujet : <em>Moi, je suis étudiant.</em></li><li>Seuls, dans une réponse courte : <em>— Et vous ? — Nous aussi.</em></li></ul>"},
                {"heading": "d) Ils ou elles ?", "body": "<ul><li><strong>Ils</strong> — groupe masculin ou mixte (même un seul homme parmi des femmes).</li><li><strong>Elles</strong> — groupe entièrement féminin.</li></ul>"},
            ],
            "examples": [
                "Moi, je suis étudiant.",
                "Tu viens avec moi ?",
                "On va au cinéma ce soir.",
                "Ils sont canadiens ; elles sont françaises.",
                "C'est pour toi.",
                "Et vous, vous venez ?",
            ],
            "commonMistakes": [
                {"wrong": "Je viens avec je.", "right": "Je viens avec moi.", "why": "Après une préposition comme avec, on utilise le pronom tonique, jamais le pronom sujet."},
                {"wrong": "On vont au cinéma.", "right": "On va au cinéma.", "why": "On se conjugue toujours comme il/elle (3e personne du singulier), même s'il signifie nous."},
                {"wrong": "Ils sont très gentilles. (pour un groupe entièrement féminin)", "right": "Elles sont très gentilles.", "why": "Un groupe entièrement féminin utilise elles ; ils ne s'utilise que pour un groupe masculin ou mixte."},
            ],
        },
        "exercises": [
            {"id": "a1pn-fill", "type": "fill-blank", "title": "Complète avec le Bon Pronom",
             "instructions": "Choisis le pronom correct pour chaque espace.",
             "items": [
                {"id": "a1pnf1", "prompt": "___, je suis étudiant.", "answers": [["Moi"]], "options": ["Moi", "Je", "Me"], "explanation": "Pronom tonique en début de phrase pour insister sur le sujet."},
                {"id": "a1pnf2", "prompt": "Tu viens avec ___ ?", "answers": [["moi"]], "options": ["moi", "je", "me"], "explanation": "Après une préposition, on utilise le pronom tonique."},
                {"id": "a1pnf3", "prompt": "___ va au cinéma ce soir (forme familière de nous).", "answers": [["On"]], "options": ["On", "Nous", "Ils"], "explanation": "On est l'équivalent familier de nous, conjugué comme il/elle."},
                {"id": "a1pnf4", "prompt": "C'est pour ___ (toi, forme tonique).", "answers": [["toi"]], "options": ["toi", "tu", "te"], "explanation": "Forme tonique après la préposition pour."},
             ]},
            {"id": "a1pn-mc", "type": "multiple-choice", "title": "Pronoms Sujets et Toniques",
             "items": [
                {"id": "a1pnm1", "prompt": "Quel pronom tonique correspond à il ?", "options": ["lui", "le", "il"], "answerIndex": 0, "explanation": "Lui est la forme tonique de il."},
                {"id": "a1pnm2", "prompt": "Comment se conjugue le verbe après on ?", "options": ["comme il/elle (3e personne du singulier)", "comme nous", "comme ils"], "answerIndex": 0, "explanation": "On est toujours suivi d'un verbe à la 3e personne du singulier."},
                {"id": "a1pnm3", "prompt": "Quel pronom utiliser pour un groupe entièrement féminin ?", "options": ["elles", "ils", "eux"], "answerIndex": 0, "explanation": "Elles ne s'utilise que pour un groupe entièrement féminin."},
                {"id": "a1pnm4", "prompt": "Quel pronom utiliser après une préposition comme avec ou pour ?", "options": ["le pronom tonique (moi, toi, lui…)", "le pronom sujet (je, tu, il…)", "aucun pronom"], "answerIndex": 0, "explanation": "Le pronom tonique s'utilise toujours après une préposition."},
             ]},
            {"id": "a1pn-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1pnc1", "incorrect": "Je viens avec je.", "answer": ["Je viens avec moi."], "explanation": "Pronom tonique obligatoire après une préposition."},
                {"id": "a1pnc2", "incorrect": "On vont au cinéma.", "answer": ["On va au cinéma."], "explanation": "On se conjugue comme il/elle, pas comme ils."},
                {"id": "a1pnc3", "incorrect": "Ils sont très gentilles. (à propos d'un groupe entièrement féminin)", "answer": ["Elles sont très gentilles."], "explanation": "Un groupe entièrement féminin utilise elles, pas ils."},
             ]},
        ],
        "summary": [
            "Les pronoms sujets (je/tu/il/elle/on/nous/vous/ils/elles) précèdent toujours le verbe conjugué ; on se conjugue comme il/elle même s'il signifie nous.",
            "Les pronoms toniques (moi/toi/lui/elle/nous/vous/eux/elles) s'utilisent après une préposition, pour insister, ou seuls dans une réponse courte.",
            "Ils s'utilise pour un groupe masculin ou mixte ; elles seulement pour un groupe entièrement féminin.",
        ],
    },
    {
        "id": "a1-le-present-verbes-reguliers-en-er",
        "level": "A1", "unit": "1", "order": 6, "skill": "grammar", "strand": "verbes-er",
        "title": "Le Présent — Verbes Réguliers en -ER",
        "subtitle": "Les terminaisons du premier groupe, et les petites modifications orthographiques de verbes comme manger et appeler.",
        "objectives": [
            "Conjuguer au présent un verbe régulier du premier groupe (-er).",
            "Reconnaître les terminaisons -e, -es, -e, -ons, -ez, -ent.",
            "Identifier les modifications orthographiques de verbes comme manger et appeler.",
        ],
        "content": {
            "intro": "Les verbes en -er forment le groupe le plus large et le plus régulier du français : une fois leur schéma maîtrisé, il s'applique à des centaines de verbes.",
            "explanation": "<p>Pour conjuguer un verbe régulier en <strong>-er</strong> comme <em>parler</em>, on retire la terminaison <em>-er</em> de l'infinitif et on ajoute : <em>-e, -es, -e, -ons, -ez, -ent</em>. Les trois premières formes du singulier (<em>je, tu, il/elle/on</em>) se prononcent toutes de façon identique à l'oral, malgré leur orthographe différente.</p><p>Quelques verbes en -er ont une petite modification orthographique pour garder le même son. Les verbes en <strong>-ger</strong> comme <em>manger</em> gardent un <strong>e</strong> devant <em>-ons</em> (<em>nous mangeons</em>), pour que le g garde son son doux. Des verbes comme <strong>appeler</strong> doublent leur consonne finale devant une terminaison muette (<em>j'appelle, tu appelles, il appelle, ils appellent</em>), sauf aux formes <em>nous</em> et <em>vous</em> (<em>nous appelons</em>).</p>",
            "rules": [
                {"heading": "a) Terminaisons régulières", "body": "<ul><li><strong>je</strong> -e, <strong>tu</strong> -es, <strong>il/elle/on</strong> -e — <em>je parle, tu parles, il parle</em>.</li><li><strong>nous</strong> -ons, <strong>vous</strong> -ez, <strong>ils/elles</strong> -ent — <em>nous parlons, vous parlez, ils parlent</em>.</li></ul>"},
                {"heading": "b) Verbes en -ger", "body": "<ul><li>Gardent un e devant -ons pour garder le son doux du g : <em>nous mangeons, nous voyageons</em>.</li><li>Les autres formes suivent la règle normale : <em>je mange, tu manges, ils mangent</em>.</li></ul>"},
                {"heading": "c) Verbes comme appeler", "body": "<ul><li>Doublent leur consonne devant une terminaison muette (-e, -es, -ent) : <em>j'appelle, tu appelles, ils appellent</em>.</li><li>Une seule consonne aux formes nous et vous : <em>nous appelons, vous appelez</em>.</li></ul>"},
            ],
            "examples": [
                "Je parle français.",
                "Tu manges une pomme.",
                "Nous mangeons ensemble.",
                "Ils travaillent beaucoup.",
                "Elle appelle sa mère.",
                "Vous voyagez souvent.",
            ],
            "commonMistakes": [
                {"wrong": "Nous mangons.", "right": "Nous mangeons.", "why": "Il faut garder le e après le g devant -ons pour conserver le son doux du g."},
                {"wrong": "Elle apelle sa mère.", "right": "Elle appelle sa mère.", "why": "Appeler double le l devant une terminaison muette, sauf aux formes nous et vous."},
                {"wrong": "Il parles français.", "right": "Il parle français.", "why": "La terminaison de il/elle/on est -e, pas -es, qui est réservée à tu."},
            ],
        },
        "exercises": [
            {"id": "a1er-fill", "type": "fill-blank", "title": "Conjugue le Verbe",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "a1erf1", "prompt": "Je ___ (parler) français.", "answers": [["parle"]], "options": ["parle", "parles", "parlons"], "explanation": "Terminaison -e pour je."},
                {"id": "a1erf2", "prompt": "Nous ___ (manger) ensemble.", "answers": [["mangeons"]], "options": ["mangeons", "mangons", "mangeont"], "explanation": "Nous mangeons garde le e pour le son doux du g."},
                {"id": "a1erf3", "prompt": "Elle ___ (appeler) sa mère.", "answers": [["appelle"]], "options": ["appelle", "apelle", "appele"], "explanation": "Appeler double le l devant une terminaison muette."},
                {"id": "a1erf4", "prompt": "Vous ___ (voyager) souvent.", "answers": [["voyagez"]], "options": ["voyagez", "voyagiez", "voyageez"], "explanation": "Terminaison régulière -ez pour vous."},
             ]},
            {"id": "a1er-mc", "type": "multiple-choice", "title": "Les Terminaisons du Présent",
             "items": [
                {"id": "a1erm1", "prompt": "Quelle est la terminaison de nous au présent des verbes en -er ?", "options": ["-ons", "-ez", "-ent"], "answerIndex": 0, "explanation": "Nous prend toujours -ons au présent."},
                {"id": "a1erm2", "prompt": "Comment conjugue-t-on manger avec nous ?", "options": ["nous mangeons", "nous mangons", "nous mangeont"], "answerIndex": 0, "explanation": "Le e se garde devant -ons pour le son doux du g."},
                {"id": "a1erm3", "prompt": "Quelle est la terminaison de il/elle/on ?", "options": ["-e", "-es", "-ons"], "answerIndex": 0, "explanation": "Il/elle/on prend -e, comme je."},
                {"id": "a1erm4", "prompt": "Comment conjugue-t-on appeler avec je ?", "options": ["j'appelle", "j'apelle", "j'appele"], "answerIndex": 0, "explanation": "Appeler double le l devant une terminaison muette comme -e."},
             ]},
            {"id": "a1er-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1erc1", "incorrect": "Nous mangons à midi.", "answer": ["Nous mangeons à midi."], "explanation": "Il faut garder le e devant -ons."},
                {"id": "a1erc2", "incorrect": "Il parles très bien.", "answer": ["Il parle très bien."], "explanation": "Il/elle/on prend la terminaison -e, pas -es."},
                {"id": "a1erc3", "incorrect": "Elle apelle son ami.", "answer": ["Elle appelle son ami."], "explanation": "Appeler double le l sauf aux formes nous et vous."},
             ]},
        ],
        "summary": [
            "Les verbes réguliers en -er suivent les terminaisons -e/-es/-e/-ons/-ez/-ent.",
            "Les verbes en -ger gardent un e devant -ons (nous mangeons) pour conserver le son doux du g.",
            "Des verbes comme appeler doublent leur consonne finale devant une terminaison muette, sauf aux formes nous et vous.",
        ],
    },
    {
        "id": "a1-le-present-verbes-irreguliers-courants",
        "level": "A1", "unit": "1", "order": 7, "skill": "grammar", "strand": "verbes-irreguliers",
        "title": "Le Présent — Verbes Irréguliers Courants",
        "subtitle": "Aller, faire, prendre, pouvoir et devoir — cinq verbes indispensables au présent.",
        "objectives": [
            "Conjuguer aller et faire au présent, deux verbes irréguliers très fréquents.",
            "Conjuguer prendre, pouvoir et devoir au présent.",
            "Utiliser ces verbes dans des phrases simples de la vie quotidienne.",
        ],
        "content": {
            "intro": "Ces cinq verbes reviennent dans presque toutes les conversations, et leur conjugaison irrégulière doit être mémorisée directement, sans règle générale.",
            "explanation": "<p><strong>Aller</strong> (je vais, tu vas, il va, nous allons, vous allez, ils vont) est totalement irrégulier et essentiel — il sert aussi à former le futur proche. <strong>Faire</strong> (je fais, tu fais, il fait, nous faisons, vous faites, ils font) apparaît dans de nombreuses expressions, comme <em>il fait beau</em> ou <em>faire du sport</em>.</p><p><strong>Prendre</strong> (je prends, tu prends, il prend, nous prenons, vous prenez, ils prennent) perd son d aux formes nous/vous/ils. <strong>Pouvoir</strong> (je peux, tu peux, il peut, nous pouvons, vous pouvez, ils peuvent) et <strong>devoir</strong> (je dois, tu dois, il doit, nous devons, vous devez, ils doivent) sont suivis directement d'un infinitif, sans préposition : <em>je peux venir, tu dois partir</em>.</p>",
            "rules": [
                {"heading": "a) Aller", "body": "<ul><li>je vais, tu vas, il/elle/on va.</li><li>nous allons, vous allez, ils/elles vont.</li></ul>"},
                {"heading": "b) Faire", "body": "<ul><li>je fais, tu fais, il/elle/on fait.</li><li>nous faisons, vous faites, ils/elles font.</li></ul>"},
                {"heading": "c) Prendre", "body": "<ul><li>je prends, tu prends, il/elle/on prend.</li><li>nous prenons, vous prenez, ils/elles prennent (double n).</li></ul>"},
                {"heading": "d) Pouvoir et devoir + infinitif", "body": "<ul><li><em>Je peux venir.</em> — capacité ou permission.</li><li><em>Tu dois partir.</em> — obligation.</li><li>Toujours suivis directement d'un verbe à l'infinitif, sans préposition.</li></ul>"},
            ],
            "examples": [
                "Je vais à l'école tous les jours.",
                "Il fait beau aujourd'hui.",
                "Nous prenons le train ce matin.",
                "Elle peut parler trois langues.",
                "Vous devez arriver à l'heure.",
                "Ils vont au marché ensemble.",
            ],
            "commonMistakes": [
                {"wrong": "Je vas à l'école.", "right": "Je vais à l'école.", "why": "Aller a une conjugaison totalement irrégulière : je vais, pas je vas."},
                {"wrong": "Nous prendons le train.", "right": "Nous prenons le train.", "why": "Prendre perd son d aux formes nous/vous/ils : prenons, prenez, prennent."},
                {"wrong": "Vous faisez du sport.", "right": "Vous faites du sport.", "why": "Faire a une forme irrégulière à vous : faites, pas faisez."},
            ],
        },
        "exercises": [
            {"id": "a1ir-fill", "type": "fill-blank", "title": "Conjugue le Verbe",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "a1irf1", "prompt": "Je ___ (aller) à l'école tous les jours.", "answers": [["vais"]], "options": ["vais", "vas", "va"], "explanation": "Je vais est la forme irrégulière de aller."},
                {"id": "a1irf2", "prompt": "Il ___ (faire) beau aujourd'hui.", "answers": [["fait"]], "options": ["fait", "fais", "faisont"], "explanation": "Il fait est la forme correcte de faire."},
                {"id": "a1irf3", "prompt": "Nous ___ (prendre) le train ce matin.", "answers": [["prenons"]], "options": ["prenons", "prendons", "prennons"], "explanation": "Prendre perd son d aux formes nous/vous/ils."},
                {"id": "a1irf4", "prompt": "Vous ___ (devoir) arriver à l'heure.", "answers": [["devez"]], "options": ["devez", "devont", "doivez"], "explanation": "Vous devez est la forme correcte de devoir."},
             ]},
            {"id": "a1ir-mc", "type": "multiple-choice", "title": "Verbes Irréguliers du Présent",
             "items": [
                {"id": "a1irm1", "prompt": "Comment conjugue-t-on aller avec je ?", "options": ["je vais", "je vas", "j'aille"], "answerIndex": 0, "explanation": "Je vais est la forme correcte et irrégulière."},
                {"id": "a1irm2", "prompt": "Comment conjugue-t-on faire avec vous ?", "options": ["vous faites", "vous faisez", "vous faisont"], "answerIndex": 0, "explanation": "Vous faites est une forme irrégulière à mémoriser."},
                {"id": "a1irm3", "prompt": "Comment conjugue-t-on prendre avec ils ?", "options": ["ils prennent", "ils prendent", "ils prenent"], "answerIndex": 0, "explanation": "Prendre double le n aux formes ils/elles."},
                {"id": "a1irm4", "prompt": "Quel verbe utilise-t-on pour exprimer une capacité (je peux) ?", "options": ["pouvoir", "devoir", "vouloir"], "answerIndex": 0, "explanation": "Pouvoir exprime la capacité ou la permission."},
             ]},
            {"id": "a1ir-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1irc1", "incorrect": "Je vas au marché.", "answer": ["Je vais au marché."], "explanation": "Aller est totalement irrégulier : je vais, pas je vas."},
                {"id": "a1irc2", "incorrect": "Nous prendons le bus.", "answer": ["Nous prenons le bus."], "explanation": "Prendre perd son d aux formes nous/vous/ils."},
                {"id": "a1irc3", "incorrect": "Vous faisez attention.", "answer": ["Vous faites attention."], "explanation": "Faire a une forme irrégulière à vous : faites."},
             ]},
        ],
        "summary": [
            "Aller (je vais, tu vas, il va, nous allons, vous allez, ils vont) et faire (je fais, tu fais, il fait, nous faisons, vous faites, ils font) sont deux verbes irréguliers essentiels.",
            "Prendre perd son d aux formes nous/vous/ils : nous prenons, ils prennent.",
            "Pouvoir et devoir sont suivis directement d'un infinitif, sans préposition : je peux venir, tu dois partir.",
        ],
    },
    {
        "id": "a1-les-adjectifs-qualificatifs-et-laccord",
        "level": "A1", "unit": "1", "order": 8, "skill": "grammar", "strand": "adjectifs",
        "title": "Les Adjectifs Qualificatifs et l'Accord",
        "subtitle": "Comment accorder un adjectif en genre et en nombre, et où le placer dans la phrase.",
        "objectives": [
            "Accorder un adjectif en genre et en nombre avec le nom qu'il qualifie.",
            "Reconnaître les formations féminines régulières et quelques irrégulières fréquentes.",
            "Placer correctement les adjectifs avant ou après le nom.",
        ],
        "content": {
            "intro": "En français, l'adjectif s'adapte toujours au nom qu'il décrit : il change de forme selon que ce nom est masculin ou féminin, singulier ou pluriel.",
            "explanation": "<p>La règle générale est d'ajouter un <strong>-e</strong> au féminin (<em>grand → grande</em>) et un <strong>-s</strong> au pluriel (<em>grand → grands, grande → grandes</em>). Les adjectifs déjà terminés par <em>-e</em> au masculin ne changent pas au féminin : <em>jeune, rouge, facile</em>.</p><p>Certains féminins sont irréguliers et doivent être mémorisés : <em>beau → belle, nouveau → nouvelle, blanc → blanche, heureux → heureuse, gentil → gentille</em>. Côté position, la plupart des adjectifs se placent <strong>après</strong> le nom (<em>une voiture rouge</em>), mais une courte liste d'adjectifs courts et très fréquents se place <strong>avant</strong> : <em>grand, petit, bon, beau, jeune, vieux, nouveau, joli</em> (<em>un beau jardin</em>).</p>",
            "rules": [
                {"heading": "a) Accord régulier", "body": "<ul><li>Masculin + -e = féminin : <em>grand → grande</em>.</li><li>+ -s = pluriel : <em>grand → grands, grande → grandes</em>.</li></ul>"},
                {"heading": "b) Adjectifs déjà en -e", "body": "<ul><li>Ne changent pas au féminin : <em>un livre jeune → une histoire jeune</em>, <em>rouge, facile</em>.</li></ul>"},
                {"heading": "c) Féminins irréguliers fréquents", "body": "<ul><li><em>beau → belle</em>, <em>nouveau → nouvelle</em>, <em>blanc → blanche</em>.</li><li><em>heureux → heureuse</em>, <em>gentil → gentille</em>.</li></ul>"},
                {"heading": "d) Position dans la phrase", "body": "<ul><li>La plupart des adjectifs se placent après le nom : <em>une voiture rouge</em>.</li><li>Une courte liste se place avant : <em>grand, petit, bon, beau, jeune, vieux, nouveau, joli</em> — <em>un beau jardin</em>.</li></ul>"},
            ],
            "examples": [
                "Elle a une voiture rouge.",
                "C'est un beau jardin.",
                "Ils sont très heureux.",
                "Ma sœur est gentille.",
                "Les enfants sont petits.",
                "Nous avons une nouvelle maison.",
            ],
            "commonMistakes": [
                {"wrong": "une jardin beau", "right": "un beau jardin", "why": "Jardin est masculin (un, pas une), et beau se place avant le nom, comme les autres adjectifs courts fréquents."},
                {"wrong": "Elle est heureux.", "right": "Elle est heureuse.", "why": "Heureux devient heureuse au féminin (x → se)."},
                {"wrong": "Les enfants sont petit.", "right": "Les enfants sont petits.", "why": "L'adjectif doit s'accorder en nombre avec le nom pluriel."},
            ],
        },
        "exercises": [
            {"id": "a1aj-fill", "type": "fill-blank", "title": "Accorde l'Adjectif",
             "instructions": "Écris la forme correcte de l'adjectif entre parenthèses.",
             "items": [
                {"id": "a1ajf1", "prompt": "Elle a une voiture ___ (rouge).", "answers": [["rouge"]], "options": ["rouge", "rouges", "rougee"], "explanation": "Rouge se termine déjà par -e ; il ne change pas au féminin."},
                {"id": "a1ajf2", "prompt": "C'est un ___ (beau) jardin.", "answers": [["beau"]], "options": ["beau", "belle", "beaux"], "explanation": "Beau, masculin singulier, s'accorde avec jardin."},
                {"id": "a1ajf3", "prompt": "Ma sœur est très ___ (gentil).", "answers": [["gentille"]], "options": ["gentille", "gentil", "gentils"], "explanation": "Gentil devient gentille au féminin."},
                {"id": "a1ajf4", "prompt": "Les enfants sont ___ (petit).", "answers": [["petits"]], "options": ["petits", "petit", "petites"], "explanation": "Petit s'accorde au masculin pluriel avec enfants."},
             ]},
            {"id": "a1aj-mc", "type": "multiple-choice", "title": "Genre, Nombre et Position",
             "items": [
                {"id": "a1ajm1", "prompt": "Comment forme-t-on le féminin de heureux ?", "options": ["heureuse", "heureux", "heureuxe"], "answerIndex": 0, "explanation": "Heureux devient heureuse au féminin."},
                {"id": "a1ajm2", "prompt": "Où se place généralement l'adjectif beau ?", "options": ["avant le nom", "après le nom", "les deux sont impossibles"], "answerIndex": 0, "explanation": "Beau fait partie des adjectifs courts qui précèdent le nom."},
                {"id": "a1ajm3", "prompt": "Comment accorde-t-on grand au féminin pluriel ?", "options": ["grandes", "grands", "grande"], "answerIndex": 0, "explanation": "Féminin (+e) puis pluriel (+s) : grandes."},
                {"id": "a1ajm4", "prompt": "Quel adjectif ne change pas entre masculin et féminin ?", "options": ["jeune", "blanc", "heureux"], "answerIndex": 0, "explanation": "Jeune se termine déjà par -e au masculin."},
             ]},
            {"id": "a1aj-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1ajc1", "incorrect": "une jardin beau", "answer": ["un beau jardin"], "explanation": "Jardin est masculin et beau se place avant le nom."},
                {"id": "a1ajc2", "incorrect": "Elle est heureux.", "answer": ["Elle est heureuse."], "explanation": "Accord féminin obligatoire : heureux → heureuse."},
                {"id": "a1ajc3", "incorrect": "Les enfants sont petit.", "answer": ["Les enfants sont petits."], "explanation": "Accord pluriel obligatoire avec enfants."},
             ]},
        ],
        "summary": [
            "L'adjectif s'accorde toujours en genre et en nombre avec le nom : -e au féminin, -s au pluriel, -es au féminin pluriel.",
            "Certains féminins sont irréguliers : beau→belle, blanc→blanche, heureux→heureuse, gentil→gentille.",
            "La plupart des adjectifs se placent après le nom, mais quelques adjectifs courts et fréquents (grand, petit, beau, bon, jeune, nouveau) se placent avant.",
        ],
    },
    {
        "id": "a1-les-possessifs",
        "level": "A1", "unit": "1", "order": 9, "skill": "grammar", "strand": "possessifs",
        "title": "Les Possessifs",
        "subtitle": "Mon/ma/mes, ton/ta/tes, son/sa/ses, notre/nos, votre/vos, leur/leurs.",
        "objectives": [
            "Utiliser mon/ma/mes, ton/ta/tes, son/sa/ses selon le genre et le nombre du nom possédé.",
            "Utiliser notre/nos, votre/vos, leur/leurs.",
            "Appliquer la règle mon/ton/son devant un nom féminin commençant par une voyelle.",
        ],
        "content": {
            "intro": "Contrairement à l'anglais, le possessif français s'accorde avec l'objet possédé, pas avec le genre de la personne qui possède.",
            "explanation": "<p><strong>Mon/ma/mes, ton/ta/tes, son/sa/ses</strong> s'accordent avec le nom qui suit : <em>mon livre</em> (masculin), <em>ma maison</em> (féminin), <em>mes livres</em> (pluriel). <em>Son livre</em> peut signifier « son livre à lui » ou « à elle » — le mot lui-même ne précise pas le genre du possesseur, seulement celui de l'objet possédé.</p><p><strong>Notre/nos</strong> et <strong>votre/vos</strong> ont une seule forme au singulier (<em>notre maison, notre livre</em>) et une au pluriel (<em>nos maisons</em>). <strong>Leur</strong> devient <strong>leurs</strong> devant un nom pluriel : <em>leur maison</em>, mais <em>leurs enfants</em>. Enfin, devant un nom féminin commençant par une voyelle ou un h muet, <em>ma/ta/sa</em> deviennent <strong>mon/ton/son</strong> pour faciliter la prononciation : <em>mon amie</em>, jamais « ma amie ».</p>",
            "rules": [
                {"heading": "a) Mon/ma/mes, ton/ta/tes, son/sa/ses", "body": "<ul><li>Masculin : <em>mon livre, ton frère, son père</em>.</li><li>Féminin : <em>ma maison, ta sœur, sa mère</em>.</li><li>Pluriel : <em>mes livres, tes amis, ses enfants</em>.</li></ul>"},
                {"heading": "b) L'ambiguïté de son/sa/ses", "body": "<ul><li>Son livre = le livre de lui OU le livre d'elle.</li><li>Le contexte précise à qui appartient l'objet, pas le mot lui-même.</li></ul>"},
                {"heading": "c) Notre/nos, votre/vos, leur/leurs", "body": "<ul><li><em>notre maison</em> (sing.) → <em>nos maisons</em> (plur.).</li><li><em>votre livre</em> (sing.) → <em>vos livres</em> (plur.).</li><li><em>leur maison</em> (sing.) → <em>leurs maisons</em> (plur.).</li></ul>"},
                {"heading": "d) Mon/ton/son devant une voyelle", "body": "<ul><li>Devant un nom féminin commençant par une voyelle ou un h muet : <em>mon amie, ton école, son adresse</em> (jamais « ma amie »).</li></ul>"},
            ],
            "examples": [
                "C'est mon livre préféré.",
                "Voici ma maison.",
                "Ce sont mes amis.",
                "Elle aime son frère.",
                "Nous adorons notre quartier.",
                "Ils cherchent leurs clés.",
                "C'est mon amie Sophie.",
            ],
            "commonMistakes": [
                {"wrong": "ma amie", "right": "mon amie", "why": "Devant une voyelle, ma devient mon, même pour un nom féminin."},
                {"wrong": "Penser que son signifie toujours « à lui ».", "right": "Reconnaître que son livre peut aussi signifier « à elle ».", "why": "En français, l'accord du possessif se fait avec l'objet possédé, pas avec le genre du possesseur."},
                {"wrong": "Ils cherchent leur clés.", "right": "Ils cherchent leurs clés.", "why": "Leur prend un s au pluriel devant un nom pluriel, comme les autres possessifs."},
            ],
        },
        "exercises": [
            {"id": "a1po-fill", "type": "fill-blank", "title": "Complète avec le Bon Possessif",
             "instructions": "Choisis la forme correcte pour chaque espace.",
             "items": [
                {"id": "a1pof1", "prompt": "C'est ___ livre préféré.", "answers": [["mon"]], "options": ["mon", "ma", "mes"], "explanation": "Livre est masculin singulier : mon livre."},
                {"id": "a1pof2", "prompt": "Voici ___ maison.", "answers": [["ma"]], "options": ["ma", "mon", "mes"], "explanation": "Maison est féminin singulier : ma maison."},
                {"id": "a1pof3", "prompt": "C'est ___ amie Sophie.", "answers": [["mon"]], "options": ["mon", "ma", "ta"], "explanation": "Devant une voyelle, ma devient mon, même pour un nom féminin."},
                {"id": "a1pof4", "prompt": "Ils cherchent ___ clés.", "answers": [["leurs"]], "options": ["leurs", "leur", "leures"], "explanation": "Leur prend un s devant un nom pluriel."},
             ]},
            {"id": "a1po-mc", "type": "multiple-choice", "title": "Les Possessifs",
             "items": [
                {"id": "a1pom1", "prompt": "Comment dit-on « my friend » (féminin) devant une voyelle ?", "options": ["mon amie", "ma amie", "ta amie"], "answerIndex": 0, "explanation": "Mon remplace ma devant une voyelle, pour la prononciation."},
                {"id": "a1pom2", "prompt": "Que peut signifier son livre ?", "options": ["son livre à lui ou à elle", "seulement à lui", "seulement à elle"], "answerIndex": 0, "explanation": "Le possessif s'accorde avec l'objet, pas avec le possesseur."},
                {"id": "a1pom3", "prompt": "Quelle est la forme correcte de notre au pluriel ?", "options": ["nos", "notre", "nôtres"], "answerIndex": 0, "explanation": "Notre devient nos au pluriel."},
                {"id": "a1pom4", "prompt": "Comment accorder leur devant un nom pluriel ?", "options": ["leurs", "leur", "leures"], "answerIndex": 0, "explanation": "Leur prend un s devant un nom pluriel."},
             ]},
            {"id": "a1po-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1poc1", "incorrect": "C'est ma amie Sophie.", "answer": ["C'est mon amie Sophie."], "explanation": "Devant une voyelle, ma devient mon."},
                {"id": "a1poc2", "incorrect": "Ils cherchent leur clés.", "answer": ["Ils cherchent leurs clés."], "explanation": "Leur prend un s devant un nom pluriel."},
                {"id": "a1poc3", "incorrect": "Nous adorons nos quartier.", "answer": ["Nous adorons notre quartier."], "explanation": "Notre (singulier) pour un seul quartier ; nos est réservé au pluriel."},
             ]},
        ],
        "summary": [
            "Les possessifs s'accordent avec l'objet possédé, pas avec le genre de la personne qui possède : son livre peut signifier « à lui » ou « à elle ».",
            "Notre/votre ont une seule forme au singulier (notre, votre) et une au pluriel (nos, vos) ; leur devient leurs devant un nom pluriel.",
            "Devant un nom féminin commençant par une voyelle ou un h muet, ma/ta/sa deviennent mon/ton/son : mon amie, pas ma amie.",
        ],
    },
    {
        "id": "a1-les-demonstratifs",
        "level": "A1", "unit": "1", "order": 10, "skill": "grammar", "strand": "demonstratifs",
        "title": "Les Démonstratifs",
        "subtitle": "Ce, cet, cette et ces — comment désigner précisément une personne ou une chose.",
        "objectives": [
            "Utiliser ce, cet, cette et ces selon le genre, le nombre et la lettre initiale du nom.",
            "Distinguer cet (masculin devant voyelle) de cette (féminin).",
            "Employer les démonstratifs pour désigner une personne ou une chose précise.",
        ],
        "content": {
            "intro": "Les démonstratifs pointent vers une personne ou une chose précise, présente ou déjà mentionnée dans la conversation.",
            "explanation": "<p><strong>Ce</strong> s'utilise devant un nom masculin singulier commençant par une consonne (<em>ce livre, ce garçon</em>), et devient <strong>cet</strong> devant une voyelle ou un h muet (<em>cet homme, cet ami</em>) pour faciliter la prononciation. <strong>Cette</strong> s'utilise devant tout nom féminin singulier, quelle que soit sa première lettre (<em>cette maison, cette amie</em>).</p><p>Au pluriel, une seule forme sert pour les deux genres : <strong>ces</strong> (<em>ces livres, ces maisons</em>). Pour insister sur la proximité ou l'éloignement, on peut ajouter <em>-ci</em> ou <em>-là</em> après le nom : <em>ce livre-ci</em> (celui-ci, proche) contre <em>ce livre-là</em> (celui-là, plus loin).</p>",
            "rules": [
                {"heading": "a) Ce", "body": "<ul><li>Masculin singulier devant consonne : <em>ce livre, ce garçon</em>.</li></ul>"},
                {"heading": "b) Cet", "body": "<ul><li>Masculin singulier devant voyelle ou h muet : <em>cet homme, cet ami</em>.</li></ul>"},
                {"heading": "c) Cette", "body": "<ul><li>Tout nom féminin singulier : <em>cette maison, cette amie</em>.</li></ul>"},
                {"heading": "d) Ces et -ci/-là", "body": "<ul><li>Pluriel, masculin ou féminin : <em>ces livres, ces maisons</em>.</li><li>-ci (proche) / -là (loin) pour préciser : <em>ce livre-ci</em> vs <em>ce livre-là</em>.</li></ul>"},
            ],
            "examples": [
                "Ce livre est très intéressant.",
                "Cet homme travaille avec moi.",
                "Cette maison est magnifique.",
                "Ces enfants sont très polis.",
                "J'aime cet appartement.",
                "Regarde cette photo !",
            ],
            "commonMistakes": [
                {"wrong": "ce homme", "right": "cet homme", "why": "Devant une voyelle ou un h muet, ce devient cet, même si le nom reste masculin."},
                {"wrong": "cet maison", "right": "cette maison", "why": "Maison est féminin, donc cette ; cet est réservé au masculin."},
                {"wrong": "ce livres", "right": "ces livres", "why": "Au pluriel, on utilise toujours ces, quel que soit le genre du nom."},
            ],
        },
        "exercises": [
            {"id": "a1de-fill", "type": "fill-blank", "title": "Complète avec le Bon Démonstratif",
             "instructions": "Choisis la forme correcte pour chaque espace.",
             "items": [
                {"id": "a1def1", "prompt": "___ livre est très intéressant.", "answers": [["Ce"]], "options": ["Ce", "Cet", "Cette"], "explanation": "Livre est masculin et commence par une consonne : ce livre."},
                {"id": "a1def2", "prompt": "___ homme travaille avec moi.", "answers": [["Cet"]], "options": ["Cet", "Ce", "Cette"], "explanation": "Homme est masculin et commence par une voyelle : cet homme."},
                {"id": "a1def3", "prompt": "___ maison est magnifique.", "answers": [["Cette"]], "options": ["Cette", "Ce", "Cet"], "explanation": "Maison est féminin : cette maison."},
                {"id": "a1def4", "prompt": "___ enfants sont très polis.", "answers": [["Ces"]], "options": ["Ces", "Ce", "Cette"], "explanation": "Enfants est pluriel : ces enfants."},
             ]},
            {"id": "a1de-mc", "type": "multiple-choice", "title": "Les Démonstratifs",
             "items": [
                {"id": "a1dem1", "prompt": "Quel démonstratif utiliser devant un nom masculin commençant par une voyelle ?", "options": ["cet", "ce", "cette"], "answerIndex": 0, "explanation": "Cet remplace ce devant une voyelle pour faciliter la prononciation."},
                {"id": "a1dem2", "prompt": "Quel démonstratif utiliser au pluriel ?", "options": ["ces", "ce", "cette"], "answerIndex": 0, "explanation": "Ces est la seule forme du pluriel, pour le masculin comme le féminin."},
                {"id": "a1dem3", "prompt": "Comment dit-on « this house » ?", "options": ["cette maison", "ce maison", "cet maison"], "answerIndex": 0, "explanation": "Maison est féminin : cette maison."},
                {"id": "a1dem4", "prompt": "Que signifie cet dans cet ami ?", "options": ["ce, masculin devant voyelle", "cette au féminin", "ces au pluriel"], "answerIndex": 0, "explanation": "Cet est la forme de ce utilisée devant une voyelle ou un h muet."},
             ]},
            {"id": "a1de-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1dec1", "incorrect": "Ce homme travaille avec moi.", "answer": ["Cet homme travaille avec moi."], "explanation": "Devant une voyelle, ce devient cet."},
                {"id": "a1dec2", "incorrect": "Cet maison est magnifique.", "answer": ["Cette maison est magnifique."], "explanation": "Maison est féminin, donc cette."},
                {"id": "a1dec3", "incorrect": "Ce livres sont intéressants.", "answer": ["Ces livres sont intéressants."], "explanation": "Le pluriel utilise toujours ces."},
             ]},
        ],
        "summary": [
            "Ce s'utilise devant un nom masculin singulier commençant par une consonne ; cet devant une voyelle ou un h muet.",
            "Cette s'utilise devant tout nom féminin singulier, quelle que soit sa première lettre.",
            "Ces s'utilise au pluriel, pour le masculin comme pour le féminin.",
        ],
    },
    {
        "id": "a1-les-prepositions-de-lieu-et-de-temps",
        "level": "A1", "unit": "1", "order": 11, "skill": "grammar", "strand": "prepositions",
        "title": "Les Prépositions de Lieu et de Temps",
        "subtitle": "À, en, au, dans, sur, sous, devant, derrière, depuis — situer dans l'espace et dans le temps.",
        "objectives": [
            "Utiliser les prépositions de lieu à, en, au selon le type de lieu (ville, pays féminin, pays masculin).",
            "Utiliser dans, sur, sous, devant, derrière pour des relations spatiales concrètes.",
            "Utiliser à, en, de…à et depuis pour situer dans le temps.",
        ],
        "content": {
            "intro": "Les prépositions de lieu et de temps sont parmi les mots les plus fréquents du français, mais leur choix dépend de règles précises qu'il faut mémoriser dès le début.",
            "explanation": "<p>Pour les <strong>lieux</strong> : <strong>à</strong> s'utilise devant une ville (<em>à Paris</em>), <strong>en</strong> devant un pays féminin (<em>en France</em>), et <strong>au</strong> devant un pays masculin (<em>au Japon</em>) — <strong>aux</strong> au pluriel (<em>aux États-Unis</em>). Pour des relations spatiales plus concrètes, on utilise <em>dans, sur, sous, devant, derrière</em>.</p><p>Pour le <strong>temps</strong> : <strong>à</strong> précède une heure précise (<em>à huit heures</em>), <strong>en</strong> précède un mois ou une année (<em>en janvier, en 2024</em>). <strong>De…à</strong> délimite une plage horaire (<em>de neuf heures à midi</em>), et <strong>depuis</strong> exprime une durée commencée dans le passé et qui continue au présent (<em>j'habite ici depuis deux ans</em>).</p>",
            "rules": [
                {"heading": "a) À, en, au pour les lieux", "body": "<ul><li><strong>à</strong> + ville — <em>à Paris, à Lyon</em>.</li><li><strong>en</strong> + pays féminin — <em>en France, en Espagne</em>.</li><li><strong>au</strong> + pays masculin, <strong>aux</strong> + pays pluriel — <em>au Japon, aux États-Unis</em>.</li></ul>"},
                {"heading": "b) Prépositions spatiales concrètes", "body": "<ul><li><em>dans le sac, sur la table, sous le lit, devant la maison, derrière l'école</em>.</li></ul>"},
                {"heading": "c) À et en pour le temps précis", "body": "<ul><li><strong>à</strong> + heure — <em>à huit heures</em>.</li><li><strong>en</strong> + mois/année — <em>en janvier, en 2024</em>.</li></ul>"},
                {"heading": "d) De…à et depuis", "body": "<ul><li><strong>de…à</strong> délimite une plage horaire — <em>de neuf heures à midi</em>.</li><li><strong>depuis</strong> exprime une durée commencée dans le passé, encore vraie maintenant — <em>depuis deux ans</em>.</li></ul>"},
            ],
            "examples": [
                "J'habite à Paris.",
                "Elle vit en France.",
                "Ils voyagent au Japon.",
                "Le chat dort sous la table.",
                "Le musée est devant la gare.",
                "Nous travaillons de neuf heures à midi.",
                "Il habite ici depuis deux ans.",
            ],
            "commonMistakes": [
                {"wrong": "Je vis à France.", "right": "Je vis en France.", "why": "Les pays féminins utilisent en, pas à."},
                {"wrong": "Ils voyagent en Japon.", "right": "Ils voyagent au Japon.", "why": "Les pays masculins utilisent au, pas en."},
                {"wrong": "J'habite ici pendant deux ans.", "right": "J'habite ici depuis deux ans.", "why": "Depuis exprime une action commencée dans le passé et qui continue maintenant ; pendant décrit une durée totale, sans lien avec le présent."},
            ],
        },
        "exercises": [
            {"id": "a1pp-fill", "type": "fill-blank", "title": "Complète avec la Bonne Préposition",
             "instructions": "Choisis la préposition correcte pour chaque espace.",
             "items": [
                {"id": "a1ppf1", "prompt": "J'habite ___ Paris.", "answers": [["à"]], "options": ["à", "en", "au"], "explanation": "à précède le nom d'une ville."},
                {"id": "a1ppf2", "prompt": "Elle vit ___ France.", "answers": [["en"]], "options": ["en", "au", "à"], "explanation": "en précède un pays féminin."},
                {"id": "a1ppf3", "prompt": "Le chat dort ___ la table.", "answers": [["sous"]], "options": ["sous", "sur", "devant"], "explanation": "Sous exprime une position en dessous de quelque chose."},
                {"id": "a1ppf4", "prompt": "Il habite ici ___ deux ans.", "answers": [["depuis"]], "options": ["depuis", "pendant", "dans"], "explanation": "Depuis marque une durée commencée dans le passé et qui continue."},
             ]},
            {"id": "a1pp-mc", "type": "multiple-choice", "title": "Prépositions de Lieu et de Temps",
             "items": [
                {"id": "a1ppm1", "prompt": "Quelle préposition pour un pays féminin comme la France ?", "options": ["en", "au", "à"], "answerIndex": 0, "explanation": "Les pays féminins prennent en."},
                {"id": "a1ppm2", "prompt": "Quelle préposition pour un pays masculin comme le Japon ?", "options": ["au", "en", "à"], "answerIndex": 0, "explanation": "Les pays masculins prennent au."},
                {"id": "a1ppm3", "prompt": "Quelle préposition exprime une action commencée dans le passé et continuant maintenant ?", "options": ["depuis", "pendant", "dans"], "answerIndex": 0, "explanation": "Depuis relie le passé au présent."},
                {"id": "a1ppm4", "prompt": "Quelle préposition pour une ville ?", "options": ["à", "en", "au"], "answerIndex": 0, "explanation": "à précède toujours le nom d'une ville."},
             ]},
            {"id": "a1pp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1ppc1", "incorrect": "Je vis à France.", "answer": ["Je vis en France."], "explanation": "Les pays féminins utilisent en."},
                {"id": "a1ppc2", "incorrect": "Ils voyagent en Japon.", "answer": ["Ils voyagent au Japon."], "explanation": "Les pays masculins utilisent au."},
                {"id": "a1ppc3", "incorrect": "J'habite ici pendant deux ans.", "answer": ["J'habite ici depuis deux ans."], "explanation": "Depuis exprime une durée commencée dans le passé et continuant au présent."},
             ]},
        ],
        "summary": [
            "Les prépositions de lieu changent selon le type de lieu : à pour une ville, en pour un pays féminin, au pour un pays masculin.",
            "Dans, sur, sous, devant, derrière situent précisément un objet dans l'espace.",
            "Depuis exprime une durée commencée dans le passé et qui continue au présent ; de…à délimite une plage horaire précise.",
        ],
    },
    {
        "id": "a1-les-mots-interrogatifs-et-poser-des-questions",
        "level": "A1", "unit": "1", "order": 12, "skill": "functional", "strand": "questions",
        "title": "Les Mots Interrogatifs et Poser des Questions",
        "subtitle": "Qui, que/quoi, où, quand, comment, pourquoi, combien — et comment former une question avec est-ce que.",
        "objectives": [
            "Utiliser les principaux mots interrogatifs (qui, que/quoi, où, quand, comment, pourquoi, combien).",
            "Former une question avec est-ce que.",
            "Reconnaître, sans forcément l'utiliser encore, la question avec inversion.",
        ],
        "content": {
            "intro": "Poser une question est l'une des compétences les plus utiles pour communiquer dès les premiers échanges en français.",
            "explanation": "<p>Les principaux <strong>mots interrogatifs</strong> sont : <em>qui</em> (une personne), <em>que/quoi</em> (une chose), <em>où</em> (un lieu), <em>quand</em> (un moment), <em>comment</em> (une manière), <em>pourquoi</em> (une raison), <em>combien</em> (une quantité ou un prix).</p><p>Au niveau A1, la façon la plus simple de poser une question est de garder l'ordre normal de la phrase et d'ajouter <strong>est-ce que</strong> : <em>Est-ce que tu viens ?</em> (oui/non), ou <em>mot interrogatif + est-ce que + sujet + verbe</em> : <em>Où est-ce que tu habites ?</em>. Une question oui/non peut aussi se former par la seule <strong>intonation</strong> montante, sans changer l'ordre des mots : <em>Tu viens ?</em>. Il existe aussi une forme plus formelle avec inversion du sujet et du verbe (<em>Où habites-tu ?</em>) — à reconnaître pour l'instant, sans devoir encore la maîtriser.</p>",
            "rules": [
                {"heading": "a) Les mots interrogatifs", "body": "<ul><li><em>qui</em> — une personne ; <em>que/quoi</em> — une chose.</li><li><em>où</em> — un lieu ; <em>quand</em> — un moment.</li><li><em>comment</em> — une manière ; <em>pourquoi</em> — une raison ; <em>combien</em> — une quantité ou un prix.</li></ul>"},
                {"heading": "b) Question oui/non", "body": "<ul><li>Par l'intonation seule : <em>Tu viens ?</em></li><li>Avec est-ce que : <em>Est-ce que tu viens ?</em></li></ul>"},
                {"heading": "c) Question avec mot interrogatif", "body": "<ul><li>Ordre : mot interrogatif + est-ce que + sujet + verbe — <em>Où est-ce que tu habites ?</em></li></ul>"},
                {"heading": "d) L'inversion (à reconnaître)", "body": "<ul><li>Forme plus formelle : sujet et verbe inversés — <em>Où habites-tu ?</em></li><li>Pas encore à maîtriser à ce niveau, mais utile à reconnaître à l'écrit.</li></ul>"},
            ],
            "examples": [
                "Qui est cette personne ?",
                "Qu'est-ce que tu fais ce soir ?",
                "Où est-ce que tu habites ?",
                "Quand est-ce que tu arrives ?",
                "Comment tu t'appelles ?",
                "Pourquoi tu es en retard ?",
                "Combien ça coûte ?",
            ],
            "commonMistakes": [
                {"wrong": "Qui est-ce que tu fais ce soir ?", "right": "Qu'est-ce que tu fais ce soir ?", "why": "Qui interroge sur une personne ; que/qu'est-ce que interroge sur une chose."},
                {"wrong": "Où tu es-ce que vas ?", "right": "Où est-ce que tu vas ?", "why": "L'ordre correct est mot interrogatif + est-ce que + sujet + verbe."},
                {"wrong": "Quand tu arrives est-ce que ?", "right": "Quand est-ce que tu arrives ?", "why": "Est-ce que suit directement le mot interrogatif, jamais à la fin de la phrase."},
            ],
        },
        "exercises": [
            {"id": "a1iq-fill", "type": "fill-blank", "title": "Complète avec le Bon Mot Interrogatif",
             "instructions": "Choisis le mot correct pour chaque espace.",
             "items": [
                {"id": "a1iqf1", "prompt": "___ est cette personne ?", "answers": [["Qui"]], "options": ["Qui", "Que", "Où"], "explanation": "Qui interroge sur une personne."},
                {"id": "a1iqf2", "prompt": "___ est-ce que tu habites ?", "answers": [["Où"]], "options": ["Où", "Quand", "Qui"], "explanation": "Où interroge sur un lieu."},
                {"id": "a1iqf3", "prompt": "___ est-ce que tu arrives ?", "answers": [["Quand"]], "options": ["Quand", "Comment", "Pourquoi"], "explanation": "Quand interroge sur un moment."},
                {"id": "a1iqf4", "prompt": "___ ça coûte ?", "answers": [["Combien"]], "options": ["Combien", "Comment", "Que"], "explanation": "Combien interroge sur un prix ou une quantité."},
             ]},
            {"id": "a1iq-mc", "type": "multiple-choice", "title": "Poser des Questions",
             "items": [
                {"id": "a1iqm1", "prompt": "Quel mot interrogatif interroge sur une personne ?", "options": ["qui", "que", "où"], "answerIndex": 0, "explanation": "Qui s'utilise pour une personne."},
                {"id": "a1iqm2", "prompt": "Quel mot interrogatif interroge sur le prix ou la quantité ?", "options": ["combien", "comment", "quand"], "answerIndex": 0, "explanation": "Combien s'utilise pour un prix ou une quantité."},
                {"id": "a1iqm3", "prompt": "Quel est l'ordre correct pour une question avec mot interrogatif ?", "options": ["mot interrogatif + est-ce que + sujet + verbe", "sujet + verbe + est-ce que + mot interrogatif", "est-ce que + mot interrogatif + sujet"], "answerIndex": 0, "explanation": "Le mot interrogatif précède toujours est-ce que."},
                {"id": "a1iqm4", "prompt": "Comment demande-t-on « why » en français ?", "options": ["pourquoi", "comment", "combien"], "answerIndex": 0, "explanation": "Pourquoi interroge sur une raison."},
             ]},
            {"id": "a1iq-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1iqc1", "incorrect": "Qui est-ce que tu fais ce soir ?", "answer": ["Qu'est-ce que tu fais ce soir ?"], "explanation": "Que/qu'est-ce que interroge sur une chose, pas qui."},
                {"id": "a1iqc2", "incorrect": "Où tu es-ce que vas ?", "answer": ["Où est-ce que tu vas ?"], "explanation": "Ordre correct : mot interrogatif + est-ce que + sujet + verbe."},
                {"id": "a1iqc3", "incorrect": "Quand tu arrives est-ce que ?", "answer": ["Quand est-ce que tu arrives ?"], "explanation": "Est-ce que suit directement le mot interrogatif."},
             ]},
        ],
        "summary": [
            "Les principaux mots interrogatifs sont qui, que/quoi, où, quand, comment, pourquoi et combien.",
            "Une question oui/non se forme par l'intonation seule ou avec est-ce que + phrase normale.",
            "Une question avec mot interrogatif suit l'ordre : mot interrogatif + est-ce que + sujet + verbe.",
        ],
    },
    {
        "id": "a1-aimer-adorer-detester-et-exprimer-ses-gouts",
        "level": "A1", "unit": "1", "order": 13, "skill": "functional", "strand": "gouts",
        "title": "Aimer, Adorer, Détester et Exprimer ses Goûts",
        "subtitle": "Comment parler de ses préférences, avec l'article défini pour une catégorie générale.",
        "objectives": [
            "Exprimer ses goûts avec aimer, adorer, détester et ne pas aimer.",
            "Utiliser l'article défini pour parler d'une catégorie générale (j'aime le café).",
            "Nuancer ses goûts avec des adverbes (beaucoup, un peu, vraiment, pas du tout).",
        ],
        "content": {
            "intro": "Exprimer ses goûts est l'une des toutes premières choses qu'on apprend à dire dans une nouvelle langue, et le français a sa propre logique à ce sujet.",
            "explanation": "<p>Les verbes <strong>aimer, adorer, détester</strong> se conjuguent comme des verbes réguliers en -er. Pour parler d'une <strong>catégorie générale</strong>, ils sont suivis de l'article <strong>défini</strong> : <em>j'aime le café, elle déteste les épinards</em> — jamais de l'article indéfini dans ce sens. Pour parler d'une <strong>activité</strong>, ils sont directement suivis d'un <strong>infinitif</strong>, sans préposition : <em>j'adore voyager</em>.</p><p>On peut nuancer ses goûts avec des adverbes : <em>aimer beaucoup, aimer un peu, adorer vraiment, ne pas aimer du tout</em>. Attention à ne pas confondre <em>j'aime le café</em> (préférence générale, article défini) avec <em>je voudrais un café</em> (une tasse précise que l'on demande, article indéfini).</p>",
            "rules": [
                {"heading": "a) + article défini + nom (catégorie générale)", "body": "<ul><li><em>j'aime le chocolat, elle déteste les épinards</em>.</li></ul>"},
                {"heading": "b) + infinitif (activité)", "body": "<ul><li><em>j'adore voyager, nous détestons attendre</em> — jamais de préposition avant l'infinitif.</li></ul>"},
                {"heading": "c) Nuancer ses goûts", "body": "<ul><li><em>aimer beaucoup / un peu</em>, <em>adorer vraiment</em>, <em>ne pas aimer du tout</em>.</li></ul>"},
                {"heading": "d) Le piège : j'aime le café vs je voudrais un café", "body": "<ul><li><em>J'aime le café</em> — préférence générale, article défini.</li><li><em>Je voudrais un café</em> — une tasse précise demandée, article indéfini.</li></ul>"},
            ],
            "examples": [
                "J'aime le café le matin.",
                "Elle adore voyager.",
                "Nous détestons attendre.",
                "Il n'aime pas beaucoup les légumes.",
                "Tu aimes vraiment ce film ?",
                "Je voudrais un café, s'il vous plaît.",
            ],
            "commonMistakes": [
                {"wrong": "J'aime un café, en général.", "right": "J'aime le café, en général.", "why": "Une catégorie générale prend l'article défini, pas l'indéfini."},
                {"wrong": "J'aime à voyager.", "right": "J'aime voyager.", "why": "Aimer + infinitif ne prend jamais de préposition en français."},
                {"wrong": "Je aime pas le café.", "right": "Je n'aime pas le café.", "why": "La négation ne…pas encadre le verbe ; ne s'élide en n' devant une voyelle."},
            ],
        },
        "exercises": [
            {"id": "a1am-fill", "type": "fill-blank", "title": "Complète pour Exprimer un Goût",
             "instructions": "Choisis la forme correcte pour chaque espace.",
             "items": [
                {"id": "a1amf1", "prompt": "J'aime ___ café le matin.", "answers": [["le"]], "options": ["le", "un", "du"], "explanation": "Catégorie générale : article défini le."},
                {"id": "a1amf2", "prompt": "Elle adore ___ (voyager).", "answers": [["voyager"]], "options": ["voyager", "à voyager", "de voyager"], "explanation": "Adorer + infinitif, sans préposition."},
                {"id": "a1amf3", "prompt": "Il n'aime pas beaucoup ___ légumes.", "answers": [["les"]], "options": ["les", "des", "un"], "explanation": "Catégorie générale au pluriel : article défini les."},
                {"id": "a1amf4", "prompt": "Je ___ un café, s'il vous plaît.", "answers": [["voudrais"]], "options": ["voudrais", "aime", "adore"], "explanation": "Voudrais demande une tasse précise, pas une préférence générale."},
             ]},
            {"id": "a1am-mc", "type": "multiple-choice", "title": "Exprimer ses Goûts",
             "items": [
                {"id": "a1amm1", "prompt": "Comment dit-on « I love coffee » (en général) ?", "options": ["J'aime le café.", "J'aime un café.", "J'aime café."], "answerIndex": 0, "explanation": "La préférence générale prend l'article défini."},
                {"id": "a1amm2", "prompt": "Quelle forme suit directement aimer pour une activité ?", "options": ["l'infinitif", "à + infinitif", "de + infinitif"], "answerIndex": 0, "explanation": "Aimer + infinitif, sans préposition."},
                {"id": "a1amm3", "prompt": "Comment demander une tasse précise ?", "options": ["Je voudrais un café.", "J'aime le café.", "Je déteste le café."], "answerIndex": 0, "explanation": "Je voudrais + article indéfini demande une chose précise."},
                {"id": "a1amm4", "prompt": "Où se place ne dans la négation ?", "options": ["avant le verbe (ne/n')", "après le verbe seulement", "à la fin de la phrase"], "answerIndex": 0, "explanation": "Ne (ou n') précède toujours le verbe conjugué."},
             ]},
            {"id": "a1am-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1amc1", "incorrect": "J'aime un café, en général.", "answer": ["J'aime le café, en général."], "explanation": "Catégorie générale = article défini."},
                {"id": "a1amc2", "incorrect": "J'aime à voyager.", "answer": ["J'aime voyager."], "explanation": "Aimer + infinitif sans préposition."},
                {"id": "a1amc3", "incorrect": "Je aime pas le café.", "answer": ["Je n'aime pas le café."], "explanation": "Ne s'élide en n' et encadre le verbe avec pas."},
             ]},
        ],
        "summary": [
            "Aimer/adorer/détester + article défini + nom expriment une préférence générale : j'aime le café.",
            "Aimer/adorer/détester + infinitif (sans préposition) expriment une préférence pour une activité : j'adore voyager.",
            "Je voudrais + article indéfini demande une chose précise, à ne pas confondre avec j'aime + article défini, qui exprime une préférence générale.",
        ],
    },
    {
        "id": "a1-le-futur-proche",
        "level": "A1", "unit": "1", "order": 14, "skill": "grammar", "strand": "futur-proche",
        "title": "Le Futur Proche",
        "subtitle": "Aller (au présent) + infinitif — pour parler de projets et d'actions proches dans le temps.",
        "objectives": [
            "Former le futur proche avec aller (au présent) + infinitif.",
            "Utiliser le futur proche pour parler de projets ou d'actions proches dans le temps.",
            "Placer correctement la négation autour du verbe aller conjugué.",
        ],
        "content": {
            "intro": "Le futur proche est la façon la plus courante de parler de l'avenir à l'oral en français, bien plus fréquente que le futur simple dans une conversation quotidienne.",
            "explanation": "<p>Le futur proche se forme avec <strong>aller</strong> conjugué au présent, suivi directement d'un verbe à l'<strong>infinitif</strong> : <em>je vais manger, tu vas partir, elle va téléphoner</em>. Il s'utilise pour parler de projets, de décisions ou d'actions qui vont bientôt se produire, souvent accompagné de marqueurs temporels comme <em>demain, ce soir, bientôt, la semaine prochaine</em>.</p><p>À la forme négative, <strong>ne…pas</strong> encadre uniquement le verbe <em>aller</em> conjugué, jamais l'infinitif qui le suit : <em>je ne vais pas sortir</em> (et non « je ne vais sortir pas »).</p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>aller (présent) + infinitif : <em>je vais, tu vas, il/elle/on va, nous allons, vous allez, ils/elles vont</em> + verbe à l'infinitif.</li></ul>"},
                {"heading": "b) Usage", "body": "<ul><li>Projets, décisions, prévisions proches : <em>Je vais téléphoner à ma mère.</em></li></ul>"},
                {"heading": "c) Négation", "body": "<ul><li>Ne…pas encadre uniquement aller conjugué : <em>Je ne vais pas sortir ce soir.</em></li></ul>"},
                {"heading": "d) Marqueurs temporels fréquents", "body": "<ul><li><em>demain, ce soir, bientôt, la semaine prochaine, dans une heure</em>.</li></ul>"},
            ],
            "examples": [
                "Je vais manger dans dix minutes.",
                "Tu vas partir demain ?",
                "Elle va téléphoner à sa mère.",
                "Nous allons visiter le musée.",
                "Vous allez adorer ce film.",
                "Ils ne vont pas venir ce soir.",
            ],
            "commonMistakes": [
                {"wrong": "Je vais à manger.", "right": "Je vais manger.", "why": "Aller + infinitif ne prend jamais de préposition entre les deux verbes."},
                {"wrong": "Je ne vais manger pas.", "right": "Je ne vais pas manger.", "why": "La négation encadre uniquement le verbe conjugué (vais), pas l'infinitif."},
                {"wrong": "Elle va téléphones à sa mère.", "right": "Elle va téléphoner à sa mère.", "why": "Le deuxième verbe reste toujours à l'infinitif, jamais conjugué."},
            ],
        },
        "exercises": [
            {"id": "a1fp-fill", "type": "fill-blank", "title": "Conjugue au Futur Proche",
             "instructions": "Écris la forme correcte de aller pour chaque espace.",
             "items": [
                {"id": "a1fpf1", "prompt": "Je ___ (aller) manger dans dix minutes.", "answers": [["vais"]], "options": ["vais", "va", "vas"], "explanation": "Je vais est la forme correcte pour je."},
                {"id": "a1fpf2", "prompt": "Tu ___ (aller) partir demain ?", "answers": [["vas"]], "options": ["vas", "va", "vais"], "explanation": "Tu vas est la forme correcte pour tu."},
                {"id": "a1fpf3", "prompt": "Nous ___ (aller) visiter le musée.", "answers": [["allons"]], "options": ["allons", "allez", "vont"], "explanation": "Nous allons est la forme correcte pour nous."},
                {"id": "a1fpf4", "prompt": "Ils ne ___ pas venir ce soir.", "answers": [["vont"]], "options": ["vont", "va", "allons"], "explanation": "Ils vont est la forme correcte pour ils."},
             ]},
            {"id": "a1fp-mc", "type": "multiple-choice", "title": "Le Futur Proche",
             "items": [
                {"id": "a1fpm1", "prompt": "Comment se forme le futur proche ?", "options": ["aller au présent + infinitif", "aller au présent + participe passé", "avoir au présent + infinitif"], "answerIndex": 0, "explanation": "Le futur proche combine aller et un infinitif."},
                {"id": "a1fpm2", "prompt": "Quelle phrase est correcte ?", "options": ["Je vais manger.", "Je vais à manger.", "Je vais mange."], "answerIndex": 0, "explanation": "Aucune préposition entre aller et l'infinitif."},
                {"id": "a1fpm3", "prompt": "Où se place la négation avec le futur proche ?", "options": ["autour du verbe aller conjugué", "autour de l'infinitif", "à la fin de la phrase"], "answerIndex": 0, "explanation": "Ne…pas encadre uniquement aller conjugué."},
                {"id": "a1fpm4", "prompt": "Quel marqueur temporel accompagne souvent le futur proche ?", "options": ["demain", "hier", "avant"], "answerIndex": 0, "explanation": "Demain marque une action future proche."},
             ]},
            {"id": "a1fp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "a1fpc1", "incorrect": "Je vais à manger.", "answer": ["Je vais manger."], "explanation": "Aucune préposition entre aller et l'infinitif."},
                {"id": "a1fpc2", "incorrect": "Je ne vais manger pas.", "answer": ["Je ne vais pas manger."], "explanation": "La négation encadre uniquement aller conjugué."},
                {"id": "a1fpc3", "incorrect": "Elle va téléphones à sa mère.", "answer": ["Elle va téléphoner à sa mère."], "explanation": "Le deuxième verbe reste toujours à l'infinitif."},
             ]},
        ],
        "summary": [
            "Le futur proche se forme avec aller au présent + un verbe à l'infinitif : je vais manger.",
            "Il s'utilise pour parler de projets ou d'actions proches dans le temps, souvent avec des marqueurs comme demain, ce soir, bientôt.",
            "La négation encadre uniquement le verbe aller conjugué (ne vais pas), jamais l'infinitif.",
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
    "a1-la-prononciation-avancee": [
        {"id": "a1prx-reading", "type": "reading-comprehension", "title": "Lecture : Le Matin chez Léa",
         "passage": "<p>Léa habite avec ses amis dans un petit appartement à Lyon. Le matin, elle dit : « Vous avez bien dormi ? » Ses amis répondent en souriant. Dans la cuisine, il y a un gâteau au chocolat et de l'eau fraîche. Le chien de la voisine, qui s'appelle Champagne, aboie dans le jardin. Léa demande : « Tu viens avec nous au marché ? »</p>",
         "items": [
            {"id": "a1prxr1", "prompt": "Où habite Léa ?", "options": ["À Lyon", "À Paris", "À Lille"], "answerIndex": 0, "explanation": "Le texte dit : « Léa habite … à Lyon »."},
            {"id": "a1prxr2", "prompt": "Que demande Léa le matin ?", "options": ["Vous avez bien dormi ?", "Vous avez faim ?", "Vous avez froid ?"], "answerIndex": 0, "explanation": "Le texte cite exactement cette question."},
            {"id": "a1prxr3", "prompt": "Comment s'appelle le chien de la voisine ?", "options": ["Champagne", "Chocolat", "Château"], "answerIndex": 0, "explanation": "Le texte dit : « le chien … qui s'appelle Champagne »."},
            {"id": "a1prxr4", "prompt": "Qu'y a-t-il dans la cuisine ?", "options": ["Un gâteau au chocolat et de l'eau fraîche", "Du pain et du fromage", "Rien du tout"], "answerIndex": 0, "explanation": "Le texte le mentionne directement."},
         ]},
        {"id": "a1prx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1prxo1", "prompt": "Remets les mots en ordre.", "words": ["Vous", "avez", "bien", "dormi"], "explanation": "Pronom sujet + verbe avoir avec liaison à l'oral."},
            {"id": "a1prxo2", "prompt": "Remets les mots en ordre.", "words": ["Le", "chien", "aboie", "dans", "le", "jardin"], "explanation": "Sujet + verbe + complément de lieu."},
         ]},
    ],
    "a1-le-genre-et-le-nombre-des-noms": [
        {"id": "a1gnx-reading", "type": "reading-comprehension", "title": "Lecture : Ma Chambre",
         "passage": "<p>Dans ma chambre, il y a un grand bureau et une petite table. Sur le bureau, il y a des livres et des journaux. Au mur, il y a un tableau avec des chevaux blancs. Le vrai problème, c'est qu'il n'y a pas assez de place pour tous mes objets.</p>",
         "items": [
            {"id": "a1gnxr1", "prompt": "Qu'y a-t-il sur le bureau ?", "options": ["Des livres et des journaux", "Des chevaux", "Un tableau"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a1gnxr2", "prompt": "Que représente le tableau au mur ?", "options": ["Des chevaux blancs", "Un bureau", "Une table"], "answerIndex": 0, "explanation": "Le texte dit : « un tableau avec des chevaux blancs »."},
            {"id": "a1gnxr3", "prompt": "Quel est le vrai problème, selon le texte ?", "options": ["Pas assez de place", "Pas assez de livres", "Pas assez de lumière"], "answerIndex": 0, "explanation": "Le texte se termine sur ce manque de place."},
            {"id": "a1gnxr4", "prompt": "Le mot problème est-il masculin dans ce texte ?", "options": ["Oui", "Non"], "answerIndex": 0, "explanation": "Le texte utilise « le vrai problème », donc masculin."},
         ]},
        {"id": "a1gnx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1gnxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "y", "a", "un", "grand", "bureau"], "explanation": "Il y a + article + adjectif + nom."},
            {"id": "a1gnxo2", "prompt": "Remets les mots en ordre.", "words": ["Le", "problème", "est", "le", "manque", "de", "place"], "explanation": "Sujet masculin (le problème) + être + attribut."},
         ]},
    ],
    "a1-les-articles-definis-indefinis-et-contractes": [
        {"id": "a1arx-reading", "type": "reading-comprehension", "title": "Lecture : Le Samedi au Marché",
         "passage": "<p>Le samedi, je vais souvent au marché avec ma sœur. Nous achetons du pain, de la confiture et des légumes frais. Ensuite, nous allons à la piscine, puis nous rentrons à la maison. Le soir, on parle des enfants du quartier qui jouent dans la rue.</p>",
         "items": [
            {"id": "a1arxr1", "prompt": "Où va la personne le samedi, en premier ?", "options": ["Au marché", "À la piscine", "À la maison"], "answerIndex": 0, "explanation": "Le texte dit : « je vais souvent au marché »."},
            {"id": "a1arxr2", "prompt": "Qu'achète-t-elle au marché ?", "options": ["Du pain, de la confiture et des légumes", "Seulement du pain", "Des livres"], "answerIndex": 0, "explanation": "Le texte liste ces trois achats."},
            {"id": "a1arxr3", "prompt": "Où va-t-elle ensuite ?", "options": ["À la piscine", "Au cinéma", "À l'école"], "answerIndex": 0, "explanation": "Le texte dit : « nous allons à la piscine »."},
            {"id": "a1arxr4", "prompt": "De qui parle-t-on le soir ?", "options": ["Des enfants du quartier", "Des voisins", "Des amis de l'école"], "answerIndex": 0, "explanation": "Le texte se termine sur ce sujet."},
         ]},
        {"id": "a1arx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1arxo1", "prompt": "Remets les mots en ordre.", "words": ["Je", "vais", "au", "marché"], "explanation": "à + le se contracte en au."},
            {"id": "a1arxo2", "prompt": "Remets les mots en ordre.", "words": ["Nous", "achetons", "de", "la", "confiture"], "explanation": "Article partitif de la devant un nom féminin."},
         ]},
    ],
    "a1-il-y-a-cest-et-il-est": [
        {"id": "a1iex-reading", "type": "reading-comprehension", "title": "Lecture : Notre Classe",
         "passage": "<p>Dans notre classe, il y a vingt-cinq élèves. C'est une classe très sympathique. Il y a aussi un nouveau professeur : c'est Monsieur Dubois. Il est très patient et il est toujours souriant. Il y a beaucoup de livres sur son bureau.</p>",
         "items": [
            {"id": "a1iexr1", "prompt": "Combien d'élèves y a-t-il dans la classe ?", "options": ["Vingt-cinq", "Quinze", "Trente"], "answerIndex": 0, "explanation": "Le texte dit : « il y a vingt-cinq élèves »."},
            {"id": "a1iexr2", "prompt": "Comment s'appelle le nouveau professeur ?", "options": ["Monsieur Dubois", "Monsieur Martin", "Monsieur Petit"], "answerIndex": 0, "explanation": "Le texte dit : « c'est Monsieur Dubois »."},
            {"id": "a1iexr3", "prompt": "Comment est le professeur ?", "options": ["Patient et souriant", "Sévère et sérieux", "Fatigué"], "answerIndex": 0, "explanation": "Le texte dit : « il est très patient et … toujours souriant »."},
            {"id": "a1iexr4", "prompt": "Qu'y a-t-il sur son bureau ?", "options": ["Beaucoup de livres", "Un ordinateur", "Rien"], "answerIndex": 0, "explanation": "Le texte le mentionne directement."},
         ]},
        {"id": "a1iex-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1iexo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "y", "a", "vingt-cinq", "élèves"], "explanation": "Il y a + nombre + nom au pluriel."},
            {"id": "a1iexo2", "prompt": "Remets les mots en ordre.", "words": ["C'est", "Monsieur", "Dubois"], "explanation": "C'est + nom propre pour identifier une personne."},
         ]},
    ],
    "a1-les-pronoms-sujets-et-toniques": [
        {"id": "a1pnx-reading", "type": "reading-comprehension", "title": "Lecture : Ma Famille et Mes Amis",
         "passage": "<p>Moi, je m'appelle Sami. Toi, tu es ma meilleure amie. Elle, c'est ma sœur Nora. Nous, on habite ensemble depuis un an. Eux, ce sont nos voisins ; ils sont très gentils. Et vous, vous habitez où ?</p>",
         "items": [
            {"id": "a1pnxr1", "prompt": "Comment s'appelle la personne qui parle ?", "options": ["Sami", "Nora", "Eux"], "answerIndex": 0, "explanation": "Le texte commence par « Moi, je m'appelle Sami »."},
            {"id": "a1pnxr2", "prompt": "Qui est Nora ?", "options": ["La sœur de Sami", "La voisine", "L'amie"], "answerIndex": 0, "explanation": "Le texte dit : « Elle, c'est ma sœur Nora »."},
            {"id": "a1pnxr3", "prompt": "Depuis combien de temps habitent-ils ensemble ?", "options": ["Un an", "Deux ans", "Six mois"], "answerIndex": 0, "explanation": "Le texte dit : « on habite ensemble depuis un an »."},
            {"id": "a1pnxr4", "prompt": "Comment sont les voisins, selon le texte ?", "options": ["Très gentils", "Très sérieux", "Très occupés"], "answerIndex": 0, "explanation": "Le texte dit : « ils sont très gentils »."},
         ]},
        {"id": "a1pnx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1pnxo1", "prompt": "Remets les mots en ordre.", "words": ["Nous", "on", "habite", "ensemble"], "explanation": "On remplace nous à l'oral, conjugué comme il/elle."},
            {"id": "a1pnxo2", "prompt": "Remets les mots en ordre.", "words": ["Ils", "sont", "très", "gentils"], "explanation": "Pronom sujet pluriel + adjectif accordé au masculin pluriel."},
         ]},
    ],
    "a1-le-present-verbes-reguliers-en-er": [
        {"id": "a1erx-reading", "type": "reading-comprehension", "title": "Lecture : Une Journée de Travail",
         "passage": "<p>Chaque matin, je parle avec mes collègues au bureau. Nous mangeons ensemble à midi, dans un petit restaurant. L'après-midi, elle appelle souvent ses clients, et ils voyagent beaucoup pour leur travail. Le week-end, nous mangeons chez mes parents.</p>",
         "items": [
            {"id": "a1erxr1", "prompt": "Avec qui la personne parle-t-elle chaque matin ?", "options": ["Ses collègues", "Ses parents", "Ses clients"], "answerIndex": 0, "explanation": "Le texte dit : « je parle avec mes collègues au bureau »."},
            {"id": "a1erxr2", "prompt": "Où mangent-ils à midi ?", "options": ["Dans un petit restaurant", "Au bureau", "Chez les parents"], "answerIndex": 0, "explanation": "Le texte dit : « Nous mangeons ensemble à midi, dans un petit restaurant »."},
            {"id": "a1erxr3", "prompt": "Que fait-elle souvent l'après-midi ?", "options": ["Elle appelle ses clients", "Elle mange", "Elle voyage"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a1erxr4", "prompt": "Où mangent-ils le week-end ?", "options": ["Chez les parents", "Au restaurant", "Au bureau"], "answerIndex": 0, "explanation": "Le texte dit : « nous mangeons chez mes parents »."},
         ]},
        {"id": "a1erx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1erxo1", "prompt": "Remets les mots en ordre.", "words": ["Nous", "mangeons", "ensemble", "à", "midi"], "explanation": "Nous + verbe en -ger avec e devant -ons."},
            {"id": "a1erxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "appelle", "souvent", "ses", "clients"], "explanation": "Elle + appeler avec doublement du l."},
         ]},
    ],
    "a1-le-present-verbes-irreguliers-courants": [
        {"id": "a1irx-reading", "type": "reading-comprehension", "title": "Lecture : Un Voyage à Paris",
         "passage": "<p>Demain, je vais à Paris avec mon frère. Nous prenons le train à huit heures. Il fait souvent froid en hiver, donc nous devons prendre des vêtements chauds. Mon frère peut parler un peu anglais, ça peut aider pendant le voyage. À Paris, nous allons visiter la tour Eiffel.</p>",
         "items": [
            {"id": "a1irxr1", "prompt": "Où va la personne demain ?", "options": ["À Paris", "À Lyon", "À Nice"], "answerIndex": 0, "explanation": "Le texte dit : « je vais à Paris »."},
            {"id": "a1irxr2", "prompt": "À quelle heure prennent-ils le train ?", "options": ["À huit heures", "À neuf heures", "À sept heures"], "answerIndex": 0, "explanation": "Le texte dit : « Nous prenons le train à huit heures »."},
            {"id": "a1irxr3", "prompt": "Pourquoi doivent-ils prendre des vêtements chauds ?", "options": ["Parce qu'il fait souvent froid en hiver", "Parce qu'il pleut", "Parce qu'il neige beaucoup"], "answerIndex": 0, "explanation": "Le texte donne cette raison directement."},
            {"id": "a1irxr4", "prompt": "Que vont-ils visiter à Paris ?", "options": ["La tour Eiffel", "Le Louvre", "Notre-Dame"], "answerIndex": 0, "explanation": "Le texte se termine sur cette visite prévue."},
         ]},
        {"id": "a1irx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1irxo1", "prompt": "Remets les mots en ordre.", "words": ["Nous", "prenons", "le", "train", "à", "huit", "heures"], "explanation": "Prendre conjugué avec nous."},
            {"id": "a1irxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "fait", "souvent", "froid", "en", "hiver"], "explanation": "Faire dans une expression météorologique."},
         ]},
    ],
    "a1-les-adjectifs-qualificatifs-et-laccord": [
        {"id": "a1ajx-reading", "type": "reading-comprehension", "title": "Lecture : Ma Maison et Mes Voisins",
         "passage": "<p>J'ai une petite maison blanche avec un beau jardin. Mes voisins sont très gentils et toujours heureux. Ma voiture est rouge et un peu vieille, mais elle marche bien. Le week-end, nous invitons de nouveaux amis pour un grand déjeuner.</p>",
         "items": [
            {"id": "a1ajxr1", "prompt": "Comment est la maison ?", "options": ["Petite et blanche", "Grande et bleue", "Vieille et noire"], "answerIndex": 0, "explanation": "Le texte dit : « une petite maison blanche »."},
            {"id": "a1ajxr2", "prompt": "Comment sont les voisins ?", "options": ["Très gentils et heureux", "Très sérieux", "Très occupés"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a1ajxr3", "prompt": "Comment est la voiture ?", "options": ["Rouge et un peu vieille", "Verte et neuve", "Noire et rapide"], "answerIndex": 0, "explanation": "Le texte dit : « Ma voiture est rouge et un peu vieille »."},
            {"id": "a1ajxr4", "prompt": "Que font-ils le week-end ?", "options": ["Ils invitent de nouveaux amis pour un grand déjeuner", "Ils travaillent", "Ils voyagent"], "answerIndex": 0, "explanation": "Le texte se termine sur cette activité."},
         ]},
        {"id": "a1ajx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1ajxo1", "prompt": "Remets les mots en ordre.", "words": ["J'ai", "une", "petite", "maison", "blanche"], "explanation": "Adjectifs avant et après le nom, accordés au féminin."},
            {"id": "a1ajxo2", "prompt": "Remets les mots en ordre.", "words": ["Mes", "voisins", "sont", "toujours", "heureux"], "explanation": "Accord pluriel de l'adjectif heureux."},
         ]},
    ],
    "a1-les-possessifs": [
        {"id": "a1pox-reading", "type": "reading-comprehension", "title": "Lecture : Ma Famille",
         "passage": "<p>Voici ma famille. C'est mon père, et voici sa voiture. Ma sœur adore son chat. Nous adorons notre quartier, et nos voisins sont très sympathiques. Mes amis viennent souvent chez moi avec leurs enfants.</p>",
         "items": [
            {"id": "a1poxr1", "prompt": "De qui parle-t-on au début du texte ?", "options": ["Du père", "De la mère", "Du frère"], "answerIndex": 0, "explanation": "Le texte dit : « C'est mon père »."},
            {"id": "a1poxr2", "prompt": "Qu'aime la sœur ?", "options": ["Son chat", "Son chien", "Sa voiture"], "answerIndex": 0, "explanation": "Le texte dit : « Ma sœur adore son chat »."},
            {"id": "a1poxr3", "prompt": "Comment sont les voisins ?", "options": ["Très sympathiques", "Très sérieux", "Très occupés"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "a1poxr4", "prompt": "Qui vient souvent chez la personne ?", "options": ["Ses amis avec leurs enfants", "Sa famille", "Ses collègues"], "answerIndex": 0, "explanation": "Le texte se termine sur cette visite."},
         ]},
        {"id": "a1pox-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1poxo1", "prompt": "Remets les mots en ordre.", "words": ["C'est", "mon", "père"], "explanation": "Possessif masculin singulier devant un nom masculin."},
            {"id": "a1poxo2", "prompt": "Remets les mots en ordre.", "words": ["Nos", "voisins", "sont", "très", "sympathiques"], "explanation": "Possessif pluriel nos devant un nom pluriel."},
         ]},
    ],
    "a1-les-demonstratifs": [
        {"id": "a1dex-reading", "type": "reading-comprehension", "title": "Lecture : Une Photo de Famille",
         "passage": "<p>Regarde cette photo ! C'est ma famille. Cet homme, c'est mon oncle, et cette femme, c'est ma tante. Ces enfants sont mes cousins. Ce jardin, c'est celui de mes grands-parents.</p>",
         "items": [
            {"id": "a1dexr1", "prompt": "Que montre la personne ?", "options": ["Une photo de famille", "Une carte", "Un livre"], "answerIndex": 0, "explanation": "Le texte commence par « Regarde cette photo ! C'est ma famille »."},
            {"id": "a1dexr2", "prompt": "Qui est cet homme ?", "options": ["L'oncle", "Le père", "Le frère"], "answerIndex": 0, "explanation": "Le texte dit : « Cet homme, c'est mon oncle »."},
            {"id": "a1dexr3", "prompt": "Qui sont ces enfants ?", "options": ["Les cousins", "Les voisins", "Les amis"], "answerIndex": 0, "explanation": "Le texte dit : « Ces enfants sont mes cousins »."},
            {"id": "a1dexr4", "prompt": "À qui appartient ce jardin ?", "options": ["Aux grands-parents", "Aux voisins", "À l'oncle"], "answerIndex": 0, "explanation": "Le texte se termine sur ce jardin des grands-parents."},
         ]},
        {"id": "a1dex-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1dexo1", "prompt": "Remets les mots en ordre.", "words": ["Regarde", "cette", "photo"], "explanation": "Cette devant un nom féminin singulier."},
            {"id": "a1dexo2", "prompt": "Remets les mots en ordre.", "words": ["Cet", "homme", "c'est", "mon", "oncle"], "explanation": "Cet devant un nom masculin commençant par une voyelle."},
         ]},
    ],
    "a1-les-prepositions-de-lieu-et-de-temps": [
        {"id": "a1ppx-reading", "type": "reading-comprehension", "title": "Lecture : Le Travail de Marc",
         "passage": "<p>Marc habite à Lyon, mais il travaille en Suisse. Il voyage souvent au Japon pour son travail. Dans son bureau, ses dossiers sont sur la table, sous une pile de livres. Il travaille de huit heures à dix-sept heures, et il vit dans cette ville depuis cinq ans.</p>",
         "items": [
            {"id": "a1ppxr1", "prompt": "Où habite Marc ?", "options": ["À Lyon", "En Suisse", "Au Japon"], "answerIndex": 0, "explanation": "Le texte dit : « Marc habite à Lyon »."},
            {"id": "a1ppxr2", "prompt": "Où travaille-t-il ?", "options": ["En Suisse", "À Lyon", "Au Japon"], "answerIndex": 0, "explanation": "Le texte dit : « il travaille en Suisse »."},
            {"id": "a1ppxr3", "prompt": "Où sont ses dossiers ?", "options": ["Sur la table, sous une pile de livres", "Dans un tiroir", "Sur une chaise"], "answerIndex": 0, "explanation": "Le texte le décrit précisément."},
            {"id": "a1ppxr4", "prompt": "Depuis combien de temps vit-il dans cette ville ?", "options": ["Cinq ans", "Deux ans", "Dix ans"], "answerIndex": 0, "explanation": "Le texte dit : « depuis cinq ans »."},
         ]},
        {"id": "a1ppx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1ppxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "vit", "en", "Suisse"], "explanation": "En devant un pays féminin."},
            {"id": "a1ppxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "travaille", "de", "huit", "heures", "à", "dix-sept", "heures"], "explanation": "De…à pour délimiter une plage horaire."},
         ]},
    ],
    "a1-les-mots-interrogatifs-et-poser-des-questions": [
        {"id": "a1iqx-reading", "type": "reading-comprehension", "title": "Lecture : Ma Collègue Sarah",
         "passage": "<p>— Qui est cette personne là-bas ? — C'est ma collègue Sarah. — Où est-ce qu'elle travaille ? — Elle travaille dans mon bureau. — Quand est-ce qu'elle arrive le matin ? — Elle arrive à huit heures. — Pourquoi elle est en retard aujourd'hui ? — Parce qu'il y a beaucoup de circulation.</p>",
         "items": [
            {"id": "a1iqxr1", "prompt": "Qui est Sarah ?", "options": ["Une collègue", "Une voisine", "Une amie"], "answerIndex": 0, "explanation": "Le texte dit : « C'est ma collègue Sarah »."},
            {"id": "a1iqxr2", "prompt": "Où travaille Sarah ?", "options": ["Dans le même bureau", "À la maison", "Dans un magasin"], "answerIndex": 0, "explanation": "Le texte dit : « Elle travaille dans mon bureau »."},
            {"id": "a1iqxr3", "prompt": "À quelle heure arrive-t-elle d'habitude ?", "options": ["À huit heures", "À neuf heures", "À sept heures"], "answerIndex": 0, "explanation": "Le texte dit : « Elle arrive à huit heures »."},
            {"id": "a1iqxr4", "prompt": "Pourquoi est-elle en retard aujourd'hui ?", "options": ["Beaucoup de circulation", "Elle est malade", "Elle a oublié"], "answerIndex": 0, "explanation": "Le texte donne cette raison directement."},
         ]},
        {"id": "a1iqx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1iqxo1", "prompt": "Remets les mots en ordre.", "words": ["Où", "est-ce", "qu'elle", "travaille"], "explanation": "Ordre mot interrogatif + est-ce que."},
            {"id": "a1iqxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "arrive", "à", "huit", "heures"], "explanation": "Préposition à devant une heure précise."},
         ]},
    ],
    "a1-aimer-adorer-detester-et-exprimer-ses-gouts": [
        {"id": "a1amx-reading", "type": "reading-comprehension", "title": "Lecture : Les Goûts de ma Famille",
         "passage": "<p>Ma famille adore la cuisine française. Mon père aime beaucoup le fromage, mais il déteste les épinards. Ma mère adore vraiment voyager, et elle aime lire des romans le soir. Moi, je n'aime pas du tout me lever tôt, mais j'adore le café du matin.</p>",
         "items": [
            {"id": "a1amxr1", "prompt": "Qu'aime beaucoup le père ?", "options": ["Le fromage", "Les épinards", "Le café"], "answerIndex": 0, "explanation": "Le texte dit : « Mon père aime beaucoup le fromage »."},
            {"id": "a1amxr2", "prompt": "Que déteste le père ?", "options": ["Les épinards", "Le fromage", "Voyager"], "answerIndex": 0, "explanation": "Le texte dit : « il déteste les épinards »."},
            {"id": "a1amxr3", "prompt": "Qu'adore vraiment la mère ?", "options": ["Voyager", "Lire", "Cuisiner"], "answerIndex": 0, "explanation": "Le texte dit : « Ma mère adore vraiment voyager »."},
            {"id": "a1amxr4", "prompt": "Qu'est-ce que la personne n'aime pas du tout ?", "options": ["Se lever tôt", "Le café", "Voyager"], "answerIndex": 0, "explanation": "Le texte dit : « je n'aime pas du tout me lever tôt »."},
         ]},
        {"id": "a1amx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1amxo1", "prompt": "Remets les mots en ordre.", "words": ["Mon", "père", "aime", "beaucoup", "le", "fromage"], "explanation": "Aimer + article défini pour une catégorie générale."},
            {"id": "a1amxo2", "prompt": "Remets les mots en ordre.", "words": ["J'adore", "le", "café", "du", "matin"], "explanation": "Adorer + article défini."},
         ]},
    ],
    "a1-le-futur-proche": [
        {"id": "a1fpx-reading", "type": "reading-comprehension", "title": "Lecture : Mon Week-End",
         "passage": "<p>Ce week-end, je vais rester à la maison. Demain, mes amis vont venir chez moi, et nous allons regarder un film. Ma sœur va préparer le dîner, et après, on va jouer à des jeux de société. Je ne vais pas sortir ce soir, parce que je suis fatigué.</p>",
         "items": [
            {"id": "a1fpxr1", "prompt": "Où la personne va-t-elle rester ce week-end ?", "options": ["À la maison", "Chez des amis", "En voyage"], "answerIndex": 0, "explanation": "Le texte dit : « je vais rester à la maison »."},
            {"id": "a1fpxr2", "prompt": "Que vont faire les amis demain ?", "options": ["Venir chez elle et regarder un film", "Aller au cinéma", "Faire du sport"], "answerIndex": 0, "explanation": "Le texte le décrit directement."},
            {"id": "a1fpxr3", "prompt": "Qui va préparer le dîner ?", "options": ["La sœur", "La mère", "Un ami"], "answerIndex": 0, "explanation": "Le texte dit : « Ma sœur va préparer le dîner »."},
            {"id": "a1fpxr4", "prompt": "Pourquoi ne va-t-elle pas sortir ce soir ?", "options": ["Parce qu'elle est fatiguée", "Parce qu'il pleut", "Parce qu'elle travaille"], "answerIndex": 0, "explanation": "Le texte se termine sur cette raison."},
         ]},
        {"id": "a1fpx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "a1fpxo1", "prompt": "Remets les mots en ordre.", "words": ["Nous", "allons", "regarder", "un", "film"], "explanation": "Futur proche avec nous."},
            {"id": "a1fpxo2", "prompt": "Remets les mots en ordre.", "words": ["Je", "ne", "vais", "pas", "sortir", "ce", "soir"], "explanation": "Négation autour du verbe aller conjugué."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
