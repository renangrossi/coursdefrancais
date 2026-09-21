# -*- coding: utf-8 -*-
"""C2 — Données du curriculum de niveau maîtrise. Voir curriculum/SCHEMA.md
pour la forme exacte du JSON vers lequel ceci est compilé
(scripts/generate_curriculum.py fait la compilation). Écrit en Python
plutôt qu'en JSON à la main pour que le HTML en ligne (rules[].body,
content.explanation) et les guillemets dans le texte puissent s'écrire
naturellement."""

OVERVIEW = (
    "Le niveau C2 est le sommet de ce cours : il ne s'agit plus d'apprendre "
    "une nouvelle grammaire, mais d'affiner une maîtrise déjà quasi complète. "
    "Tu travailleras la syntaxe complexe et la subordination multiple, le "
    "registre littéraire et ses procédés stylistiques, les nuances lexicales "
    "et les faux amis les plus subtils, la richesse de la variation "
    "régionale du français dans toute la francophonie, l'ironie et "
    "l'implicite, l'atténuation et la diplomatie dans le discours, les "
    "expressions idiomatiques avancées, l'analyse et la synthèse de "
    "documents complexes, la créativité lexicale, et la capacité à "
    "réécrire un même contenu dans n'importe quel registre. À la fin de ce "
    "niveau, tu auras une maîtrise du français pratiquement indissociable "
    "de celle d'un locuteur natif cultivé, dans presque tous les contextes "
    "imaginables."
)

LESSONS = [
    {
        "id": "c2-la-syntaxe-complexe-et-la-subordination-multiple",
        "level": "C2", "unit": "1", "order": 1, "skill": "grammar", "strand": "syntaxe-complexe",
        "title": "La Syntaxe Complexe et la Subordination Multiple",
        "subtitle": "Lire et écrire des phrases à plusieurs niveaux de subordination enchâssée sans perdre la clarté.",
        "objectives": [
            "Analyser une phrase longue à plusieurs propositions subordonnées enchâssées sans perdre le fil du sens.",
            "Maintenir une référence pronominale claire à travers plusieurs niveaux de subordination.",
            "Produire soi-même des phrases complexes structurées et lisibles, sans lourdeur inutile.",
        ],
        "content": {
            "intro": "Au niveau C2, la difficulté n'est plus la grammaire elle-même mais la gestion de phrases longues, où plusieurs propositions subordonnées s'enchâssent les unes dans les autres — un défi de lecture autant que d'écriture.",
            "explanation": "<p>Une phrase complexe peut enchâsser plusieurs niveaux de subordination : une relative dans une complétive, elle-même dans une circonstancielle. Par exemple : <em>Le rapport, que les experts qu'on avait consultés jugeaient incomplet, a été rejeté parce qu'il ne répondait pas aux exigences fixées.</em> Ici, une relative (<em>que... jugeaient incomplet</em>) s'enchâsse dans la phrase principale, qui contient elle-même une autre relative (<em>qu'on avait consultés</em>) et une circonstancielle de cause (<em>parce que...</em>). Pour suivre une telle phrase, il faut repérer le squelette — sujet, verbe, complément de la principale — avant de traiter chaque enchâssement séparément.</p><p>À l'écriture, la clarté prime toujours sur la longueur : chaque pronom (<em>qui, que, dont, lequel, celui-ci, ce dernier</em>) doit renvoyer sans ambiguïté à un seul antécédent possible. Quand plusieurs enchâssements rendent une phrase difficile à suivre, mieux vaut la scinder en deux phrases plus courtes, reliées par un connecteur, plutôt que de risquer la confusion du lecteur.</p>",
            "rules": [
                {"heading": "a) Repérer le squelette de la phrase", "body": "<ul><li>Isoler d'abord sujet, verbe et complément de la proposition principale avant d'analyser les subordonnées.</li></ul>"},
                {"heading": "b) Les niveaux d'enchâssement", "body": "<ul><li>Une relative peut contenir une autre relative ou une complétive, qui peut elle-même contenir une circonstancielle.</li></ul>"},
                {"heading": "c) La clarté référentielle", "body": "<ul><li>Chaque pronom doit renvoyer sans ambiguïté à un seul antécédent ; <em>celui-ci</em>/<em>ce dernier</em> distinguent deux antécédents proches.</li></ul>"},
                {"heading": "d) Scinder plutôt que surcharger", "body": "<ul><li>Une phrase à plus de trois niveaux d'enchâssement gagne souvent à être scindée en deux phrases reliées par un connecteur.</li></ul>"},
            ],
            "examples": [
                "Le rapport, que les experts qu'on avait consultés jugeaient incomplet, a été rejeté parce qu'il ne répondait pas aux exigences fixées.",
                "L'homme dont la fille, qui vit à l'étranger, venait justement de lui rendre visite, semblait particulièrement joyeux.",
                "Bien que la proposition qu'il avait soumise ait été accueillie avec enthousiasme, elle fut finalement écartée pour des raisons budgétaires.",
                "Ce que redoutaient ceux qui avaient suivi le dossier depuis le début finit par se produire.",
                "Le témoin, dont on savait qu'il avait tout vu, refusa néanmoins de répondre aux questions qu'on lui posait.",
                "La décision, qui avait été prise dans l'urgence, sans que personne n'ait pu l'anticiper, souleva une vague de critiques.",
                "Ce dernier point, sur lequel les avis divergeaient le plus, fut celui qui suscita le débat le plus vif.",
            ],
            "commonMistakes": [
                {"wrong": "Perdre le fil d'une phrase à plusieurs enchâssements en tentant de la lire d'une traite.", "right": "Repérer d'abord le squelette (sujet-verbe-complément) de la principale, puis traiter chaque subordonnée séparément.", "why": "Une lecture linéaire d'une phrase très enchâssée fait perdre le sens global ; l'analyse par niveaux le préserve."},
                {"wrong": "Utiliser « qui » pour renvoyer à un antécédent ambigu quand deux noms précèdent.", "right": "Employer « celui-ci »/« ce dernier » pour désigner sans ambiguïté le nom le plus proche.", "why": "Un pronom relatif simple peut renvoyer à plusieurs antécédents possibles ; ces formes lèvent l'ambiguïté."},
                {"wrong": "Écrire une phrase à quatre ou cinq niveaux d'enchâssement sans jamais la scinder.", "right": "Diviser une phrase trop chargée en deux phrases reliées par un connecteur logique.", "why": "Au-delà de trois niveaux, la lisibilité se dégrade même pour un lecteur expérimenté."},
            ],
        },
        "exercises": [
            {"id": "c2syn-mc", "type": "multiple-choice", "title": "Analyse la Structure",
             "items": [
                {"id": "c2synm1", "prompt": "Dans « Le rapport, que les experts qu'on avait consultés jugeaient incomplet, a été rejeté », combien de propositions relatives sont enchâssées ?", "options": ["Deux", "Une seule", "Trois"], "answerIndex": 0, "explanation": "« que... jugeaient incomplet » et « qu'on avait consultés » sont deux relatives enchâssées l'une dans l'autre."},
                {"id": "c2synm2", "prompt": "Que faut-il isoler en premier pour analyser une phrase complexe ?", "options": ["Le squelette sujet-verbe-complément de la principale", "La dernière subordonnée", "Le premier mot de la phrase"], "answerIndex": 0, "explanation": "C'est la méthode de lecture recommandée pour ne pas perdre le sens global."},
                {"id": "c2synm3", "prompt": "Quand vaut-il mieux scinder une phrase en deux ?", "options": ["Quand elle dépasse trois niveaux d'enchâssement", "Jamais, la longueur est un signe de style", "Uniquement à l'oral"], "answerIndex": 0, "explanation": "Au-delà, la clarté se dégrade même pour un lecteur avancé."},
                {"id": "c2synm4", "prompt": "Pourquoi utilise-t-on « ce dernier » plutôt que « il » dans une phrase à plusieurs antécédents ?", "options": ["Pour lever l'ambiguïté sur l'antécédent visé", "Par pure convention stylistique sans autre raison", "Parce que « il » est incorrect dans tous les cas"], "answerIndex": 0, "explanation": "« Ce dernier » désigne sans ambiguïté le nom le plus proche."},
             ]},
            {"id": "c2syn-fill", "type": "fill-blank", "title": "Complète avec le Pronom Adéquat",
             "instructions": "Choisis le pronom qui lève l'ambiguïté référentielle.",
             "items": [
                {"id": "c2synf1", "prompt": "Le directeur a reçu le client et son adjoint ; ___ semblait mécontent.", "answers": [["ce dernier"]], "options": ["ce dernier", "il", "celui"], "explanation": "Ce dernier désigne sans ambiguïté le nom le plus proche (l'adjoint)."},
                {"id": "c2synf2", "prompt": "Le témoin ___ on savait qu'il avait tout vu refusa de répondre.", "answers": [["dont"]], "options": ["dont", "que", "qui"], "explanation": "Dont introduit un complément construit avec de (on savait de lui qu'il avait tout vu)."},
                {"id": "c2synf3", "prompt": "Ce ___ redoutaient les experts finit par se produire.", "answers": [["que"]], "options": ["que", "qui", "dont"], "explanation": "Que reprend l'objet direct du verbe redouter."},
                {"id": "c2synf4", "prompt": "Le point sur ___ les avis divergeaient fut celui qui suscita le débat.", "answers": [["lequel"]], "options": ["lequel", "qui", "que"], "explanation": "Lequel s'impose après une préposition (sur) pour un antécédent de chose."},
             ]},
            {"id": "c2syn-correction", "type": "correction", "title": "Corrige l'Ambiguïté ou la Lourdeur",
             "items": [
                {"id": "c2sync1", "incorrect": "Le patron a parlé au client et à son fils et il a semblé satisfait.", "answer": ["Le patron a parlé au client et à son fils ; ce dernier a semblé satisfait."], "explanation": "Ce dernier lève l'ambiguïté sur qui a semblé satisfait."},
                {"id": "c2sync2", "incorrect": "La proposition que l'équipe que le directeur avait nommée qu'on avait longuement discutée fut finalement acceptée.", "answer": ["La proposition que l'équipe nommée par le directeur avait longuement discutée fut finalement acceptée."], "explanation": "Trois relatives enchâssées d'affilée surchargent la phrase ; on en réduit le nombre."},
                {"id": "c2sync3", "incorrect": "Il a dit qu'il viendrait et qu'il apporterait le dossier et qu'il faudrait le lire avant et qu'ensuite on déciderait.", "answer": ["Il a dit qu'il viendrait et apporterait le dossier. Il faudrait le lire avant de décider."], "explanation": "Une accumulation de complétives coordonnées se scinde pour plus de clarté."},
             ]},
        ],
        "summary": [
            "Une phrase complexe s'analyse en repérant d'abord le squelette de la principale, puis chaque niveau de subordination.",
            "Les pronoms de reprise (celui-ci, ce dernier) lèvent l'ambiguïté quand plusieurs antécédents sont possibles.",
            "Au-delà de trois niveaux d'enchâssement, il vaut mieux scinder la phrase pour préserver la clarté.",
        ],
    },
    {
        "id": "c2-le-registre-litteraire-et-les-procedes-stylistiques",
        "level": "C2", "unit": "1", "order": 2, "skill": "reading", "strand": "style-litteraire",
        "title": "Le Registre Littéraire et les Procédés Stylistiques",
        "subtitle": "Reconnaître le passé simple à la lecture et identifier les principaux procédés stylistiques du français littéraire.",
        "objectives": [
            "Reconnaître le passé simple à la lecture, y compris ses formes irrégulières les plus fréquentes.",
            "Identifier les procédés stylistiques courants : métaphore, anaphore, antithèse, gradation.",
            "Apprécier l'effet recherché par un procédé stylistique dans un texte littéraire donné.",
        ],
        "content": {
            "intro": "Le passé simple et les grandes figures de style appartiennent à un registre que l'on ne produit presque jamais à l'oral, mais qu'un lecteur de niveau C2 doit reconnaître sans effort dans un roman, un article de fond ou un discours soigné.",
            "explanation": "<p>Le <strong>passé simple</strong> exprime, comme le passé composé, une action ponctuelle et achevée, mais réservée à l'écrit narratif (roman, biographie, récit historique) : <em>il parla, elle finit, ils vinrent, nous eûmes</em>. Sa 3e personne du singulier suffit généralement à le reconnaître : <em>-a</em> pour les verbes en -er (<em>il parla</em>), <em>-it</em> pour beaucoup d'autres (<em>il finit, il prit</em>), <em>-ut</em> pour certains irréguliers (<em>il eut, il put, il voulut</em>), <em>-int</em> pour venir/tenir (<em>il vint, il tint</em>).</p><p>Parmi les procédés stylistiques les plus fréquents : la <strong>métaphore</strong> (comparaison implicite, sans <em>comme</em> : <em>le temps est un voleur</em>), l'<strong>anaphore</strong> (répétition d'un mot ou d'une structure en tête de plusieurs phrases ou vers, pour créer un effet d'insistance), l'<strong>antithèse</strong> (rapprochement de deux idées opposées dans une même phrase, pour souligner un contraste), et la <strong>gradation</strong> (une suite de termes de force croissante ou décroissante). Reconnaître ces procédés, c'est comprendre non seulement ce qu'un texte dit, mais l'effet qu'il vise à produire.</p>",
            "rules": [
                {"heading": "a) Le passé simple : reconnaissance, pas production", "body": "<ul><li>Réservé à l'écrit narratif ; jamais à l'oral, où le passé composé le remplace toujours.</li></ul>"},
                {"heading": "b) Terminaisons de la 3e personne du singulier", "body": "<ul><li><em>-a</em> (verbes en -er), <em>-it</em> (finir, prendre...), <em>-ut</em> (avoir, pouvoir, vouloir...), <em>-int</em> (venir, tenir).</li></ul>"},
                {"heading": "c) Métaphore et anaphore", "body": "<ul><li>Métaphore : comparaison implicite sans outil comparatif. Anaphore : répétition en tête de phrase ou de vers pour l'insistance.</li></ul>"},
                {"heading": "d) Antithèse et gradation", "body": "<ul><li>Antithèse : deux idées opposées rapprochées. Gradation : termes de force croissante ou décroissante.</li></ul>"},
            ],
            "examples": [
                "Il ouvrit la porte et s'arrêta net.",
                "Elle vint le voir un matin d'hiver et ne repartit jamais.",
                "Le temps est un voleur qui ne rend jamais rien.",
                "Je me souviens de ce jour, je me souviens de sa voix, je me souviens de tout.",
                "Il était riche de mots et pauvre de silences.",
                "Il hésita, puis douta, puis renonça tout à fait.",
                "Ils eurent peur, puis ils comprirent, et enfin ils partirent.",
            ],
            "commonMistakes": [
                {"wrong": "Employer le passé simple dans une conversation courante.", "right": "Réserver le passé simple à l'écrit narratif et employer le passé composé à l'oral.", "why": "Le passé simple a disparu de l'oral depuis longtemps ; l'y employer sonnerait affecté."},
                {"wrong": "Confondre « il parla » (passé simple) avec « il parlât » (subjonctif imparfait).", "right": "Distinguer les deux par contexte et par l'absence/présence d'un accent circonflexe à la 3e personne dans d'autres verbes.", "why": "Les deux formes littéraires se ressemblent mais n'appartiennent pas au même mode."},
                {"wrong": "Appeler « métaphore » toute comparaison, y compris celles avec « comme ».", "right": "Réserver métaphore aux comparaisons implicites, et comparaison à celles avec un outil comparatif explicite (comme, tel que).", "why": "La distinction technique importe pour analyser précisément un texte littéraire."},
            ],
        },
        "exercises": [
            {"id": "c2sty-mc", "type": "multiple-choice", "title": "Identifie le Procédé ou la Forme",
             "items": [
                {"id": "c2stym1", "prompt": "« Il vint, il vit, il vainquit » illustre quel procédé ?", "options": ["La gradation par répétition de structure (proche de l'anaphore)", "L'antithèse", "La litote"], "answerIndex": 0, "explanation": "La répétition de la structure sujet-verbe crée un effet de gradation rythmique."},
                {"id": "c2stym2", "prompt": "« Le temps est un voleur » est un exemple de quel procédé ?", "options": ["Une métaphore", "Une comparaison explicite", "Une antithèse"], "answerIndex": 0, "explanation": "Aucun outil comparatif (comme) n'est employé : c'est une métaphore."},
                {"id": "c2stym3", "prompt": "Quelle terminaison signale souvent un passé simple à la 3e personne du singulier pour un verbe comme venir ?", "options": ["-int (il vint)", "-a (il vena)", "-ait (il venait)"], "answerIndex": 0, "explanation": "Venir et tenir ont un passé simple en -int à la 3e personne du singulier."},
                {"id": "c2stym4", "prompt": "« Il était riche de mots et pauvre de silences » illustre quel procédé ?", "options": ["L'antithèse", "L'anaphore", "La gradation"], "answerIndex": 0, "explanation": "Riche et pauvre sont deux idées opposées rapprochées dans la même phrase."},
             ]},
            {"id": "c2sty-fill", "type": "fill-blank", "title": "Reconnais la Forme au Passé Simple",
             "instructions": "Complète avec la forme correcte au passé simple.",
             "items": [
                {"id": "c2styf1", "prompt": "Il ouvrit la porte et ___ (s'arrêter) net.", "answers": [["s'arrêta"]], "options": ["s'arrêta", "s'arrêtait", "s'est arrêté"], "explanation": "Passé simple des verbes en -er : radical + a."},
                {"id": "c2styf2", "prompt": "Elle ___ (prendre) son sac et partit sans un mot.", "answers": [["prit"]], "options": ["prit", "prenait", "a pris"], "explanation": "Prendre a un passé simple en -it à la 3e personne du singulier."},
                {"id": "c2styf3", "prompt": "Ils ___ (avoir) peur, puis ils comprirent.", "answers": [["eurent"]], "options": ["eurent", "avaient", "ont eu"], "explanation": "Avoir a un passé simple irrégulier : il eut, ils eurent."},
                {"id": "c2styf4", "prompt": "Nous ___ (vouloir) partir avant la nuit.", "answers": [["voulûmes"]], "options": ["voulûmes", "voulions", "avons voulu"], "explanation": "Vouloir a un passé simple en -us : je voulus, nous voulûmes."},
             ]},
            {"id": "c2sty-correction", "type": "correction", "title": "Identifie et Corrige",
             "instructions": "Chaque phrase confond deux procédés ou deux formes ; corrige l'erreur d'analyse.",
             "items": [
                {"id": "c2styc1", "incorrect": "« Le temps est un voleur » est une comparaison car il y a le mot « comme ».", "answer": ["« Le temps est un voleur » est une métaphore, car aucun outil comparatif n'est employé."], "explanation": "Il n'y a pas de « comme » dans cette phrase : c'est une métaphore, pas une comparaison."},
                {"id": "c2styc2", "incorrect": "« Il parlât » est la forme du passé simple de parler.", "answer": ["« Il parla » est la forme du passé simple de parler ; « il parlât » est le subjonctif imparfait."], "explanation": "L'accent circonflexe distingue le subjonctif imparfait du passé simple."},
                {"id": "c2styc3", "incorrect": "« Riche de mots et pauvre de silences » est un exemple d'anaphore.", "answer": ["« Riche de mots et pauvre de silences » est un exemple d'antithèse."], "explanation": "Ce sont deux idées opposées rapprochées, non une répétition en tête de phrase."},
             ]},
        ],
        "summary": [
            "Le passé simple s'utilise seulement à l'écrit narratif ; on le reconnaît surtout à sa 3e personne du singulier.",
            "La métaphore (comparaison implicite), l'anaphore (répétition), l'antithèse (opposition) et la gradation (progression) sont les procédés stylistiques les plus fréquents.",
            "Reconnaître un procédé, c'est comprendre l'effet qu'un texte cherche à produire, au-delà du simple sens littéral.",
        ],
    },
    {
        "id": "c2-les-nuances-lexicales-et-les-faux-amis-avances",
        "level": "C2", "unit": "1", "order": 3, "skill": "vocabulary", "strand": "faux-amis-avances",
        "title": "Les Nuances Lexicales et les Faux Amis Avancés",
        "subtitle": "Éviter les pièges anglais-français les plus subtils et choisir le mot juste parmi des synonymes proches.",
        "objectives": [
            "Identifier les faux amis anglais-français avancés qui piègent même des locuteurs très avancés.",
            "Distinguer des synonymes proches selon leur nuance exacte d'intensité ou de registre.",
            "Choisir, dans un contexte donné, le mot le plus précis parmi plusieurs quasi-synonymes.",
        ],
        "content": {
            "intro": "Aux niveaux avancés, l'anglais continue de tendre des pièges lexicaux discrets, et le vocabulaire français lui-même regorge de synonymes qui ne sont jamais totalement interchangeables.",
            "explanation": "<p>Certains <strong>faux amis</strong> anglais-français survivent même chez des locuteurs très avancés parce qu'ils se ressemblent à s'y méprendre tout en ayant un sens différent : <em>actuellement</em> signifie « en ce moment », pas « actually » (qui se traduit par <em>en fait</em>) ; <em>assister à</em> signifie « être présent à » (attend), pas « aider » (qui se dit <em>aider</em> ou <em>assister quelqu'un</em> dans un sens plus restreint) ; <em>éventuellement</em> signifie « peut-être, le cas échéant », pas « eventually » (qui se traduit par <em>finalement</em>) ; <em>sensible</em> signifie « émotif, facilement touché », pas « sensible » au sens de raisonnable (qui se dit <em>raisonnable</em> ou <em>sensé</em>).</p><p>Le français distingue aussi des nuances fines entre synonymes proches : <em>petit</em> (neutre), <em>menu</em> (petit et délicat), <em>minime</em> (négligeable en importance, pas en taille physique) ; <em>grand</em> (neutre), <em>vaste</em> (grande étendue, souvent spatiale), <em>immense</em> (extrême, hyperbolique). Choisir entre ces mots, c'est ajuster précisément l'intensité et le registre d'une phrase.</p>",
            "rules": [
                {"heading": "a) Actuellement / éventuellement", "body": "<ul><li><em>Actuellement</em> = en ce moment (jamais « actually », qui se dit <em>en fait</em>). <em>Éventuellement</em> = peut-être (jamais « eventually », qui se dit <em>finalement</em>).</li></ul>"},
                {"heading": "b) Assister / sensible", "body": "<ul><li><em>Assister à</em> = être présent (jamais « assist » au sens d'aider). <em>Sensible</em> = émotif (jamais « sensible » au sens de raisonnable, qui se dit <em>sensé</em>).</li></ul>"},
                {"heading": "c) Petit / menu / minime", "body": "<ul><li>Nuances de taille et d'importance : petit (neutre), menu (petit et délicat), minime (négligeable en importance).</li></ul>"},
                {"heading": "d) Grand / vaste / immense", "body": "<ul><li>Nuances d'intensité : grand (neutre), vaste (grande étendue), immense (extrême, hyperbolique).</li></ul>"},
            ],
            "examples": [
                "Actuellement, je travaille sur un nouveau projet.",
                "En fait, ce n'était pas du tout ce que je pensais.",
                "J'ai assisté à la conférence hier soir.",
                "Nous partirons éventuellement en vacances en juillet, si le budget le permet.",
                "Il a fini par accepter le poste, mais après de longues hésitations.",
                "Elle est très sensible : la moindre critique la blesse.",
                "C'est une décision tout à fait sensée, réfléchie et raisonnable.",
            ],
            "commonMistakes": [
                {"wrong": "Actuellement, il travaille sur ce dossier depuis trois heures et il vient de le finir.", "right": "En fait, il travaille sur ce dossier depuis trois heures et il vient de le finir.", "why": "Le sens visé ici est « actually » (en fait), pas « actuellement » (en ce moment), qui créerait un contresens temporel."},
                {"wrong": "Je vais assister mon collègue à porter ces cartons.", "right": "Je vais aider mon collègue à porter ces cartons.", "why": "Assister au sens d'aider physiquement est un anglicisme ; aider est le mot juste ici."},
                {"wrong": "C'est une remarque très sensible, bien pensée.", "right": "C'est une remarque très sensée, bien pensée.", "why": "Sensé (raisonnable) et sensible (émotif) sont deux mots distincts, souvent confondus par calque de l'anglais sensible."},
            ],
        },
        "exercises": [
            {"id": "c2fam-mc", "type": "multiple-choice", "title": "Choisis le Sens Correct",
             "items": [
                {"id": "c2famm1", "prompt": "Que signifie « actuellement » en français ?", "options": ["En ce moment", "En fait (actually)", "Finalement (eventually)"], "answerIndex": 0, "explanation": "C'est un faux ami classique de « actually »."},
                {"id": "c2famm2", "prompt": "Que signifie « éventuellement » en français ?", "options": ["Peut-être, le cas échéant", "Finalement, après un délai", "Immédiatement"], "answerIndex": 0, "explanation": "Faux ami de « eventually », qui se traduit par finalement."},
                {"id": "c2famm3", "prompt": "Que signifie « assister à une réunion » ?", "options": ["Être présent à cette réunion", "Aider à organiser cette réunion", "Annuler cette réunion"], "answerIndex": 0, "explanation": "Assister à = être présent, jamais aider au sens anglais."},
                {"id": "c2famm4", "prompt": "Quel mot signifie « raisonnable » et non « émotif » ?", "options": ["Sensé", "Sensible", "Sensitif"], "answerIndex": 0, "explanation": "Sensé (raisonnable) se distingue de sensible (émotif)."},
             ]},
            {"id": "c2fam-fill", "type": "fill-blank", "title": "Choisis le Mot Juste",
             "items": [
                {"id": "c2famf1", "prompt": "___, je travaille sur un nouveau projet passionnant.", "answers": [["Actuellement"]], "options": ["Actuellement", "Éventuellement", "Finalement"], "explanation": "En ce moment se dit actuellement en français."},
                {"id": "c2famf2", "prompt": "___, ce n'était pas du tout ce que je pensais au départ.", "answers": [["En fait"]], "options": ["En fait", "Actuellement", "Éventuellement"], "explanation": "« Actually » se traduit par en fait, jamais actuellement."},
                {"id": "c2famf3", "prompt": "Cette erreur est ___ ; elle ne change rien au résultat final.", "answers": [["minime"]], "options": ["minime", "menue", "petite"], "explanation": "Minime insiste sur la négligeabilité en importance, pas la taille physique."},
                {"id": "c2famf4", "prompt": "C'est une région d'une étendue ___, presque sans limites visibles.", "answers": [["immense"]], "options": ["immense", "menue", "minime"], "explanation": "Immense exprime une intensité extrême, hyperbolique."},
             ]},
            {"id": "c2fam-correction", "type": "correction", "title": "Corrige le Faux Ami",
             "items": [
                {"id": "c2famc1", "incorrect": "Actuellement, il a fini par accepter le poste après de longues hésitations.", "answer": ["Finalement, il a fini par accepter le poste après de longues hésitations."], "explanation": "« Eventually » se traduit par finalement, pas actuellement."},
                {"id": "c2famc2", "incorrect": "Je vais assister mon ami à déménager ce week-end.", "answer": ["Je vais aider mon ami à déménager ce week-end."], "explanation": "Assister au sens d'aider physiquement est un calque de l'anglais."},
                {"id": "c2famc3", "incorrect": "C'est une décision très sensible et réfléchie.", "answer": ["C'est une décision très sensée et réfléchie."], "explanation": "Sensé (raisonnable) est le mot juste ici, pas sensible (émotif)."},
             ]},
        ],
        "summary": [
            "Actuellement (= en ce moment) et éventuellement (= peut-être) restent des faux amis fréquents même à un niveau avancé.",
            "Assister à (= être présent) et sensé (= raisonnable, à ne pas confondre avec sensible) piègent aussi les locuteurs expérimentés.",
            "Des synonymes proches comme petit/menu/minime ou grand/vaste/immense expriment des nuances précises d'intensité et de registre.",
        ],
    },
    {
        "id": "c2-la-variation-regionale-du-francais",
        "level": "C2", "unit": "1", "order": 4, "skill": "vocabulary", "strand": "variation-regionale",
        "title": "La Variation Régionale du Français",
        "subtitle": "Reconnaître le vocabulaire propre au français de France, du Québec, de Belgique, de Suisse et d'Afrique francophone.",
        "objectives": [
            "Reconnaître un ensemble de mots et d'expressions typiques de plusieurs variétés régionales du français.",
            "Situer géographiquement l'origine probable d'une expression régionale donnée.",
            "Comprendre un texte contenant des régionalismes sans en être dérouté.",
        ],
        "content": {
            "intro": "Le français est parlé nativement sur plusieurs continents, et chaque grande région francophone a développé son propre vocabulaire : les reconnaître fait partie de la maîtrise complète de la langue, même si l'on ne les emploie pas soi-même.",
            "explanation": "<p>Au <strong>Québec</strong>, on dit <em>un chandail</em> pour un pull, <em>ma blonde/mon chum</em> pour ma copine/mon copain, <em>magasiner</em> pour faire du shopping, <em>dépanneur</em> pour une petite épicerie de quartier ouverte tard. En <strong>Belgique</strong> et en <strong>Suisse</strong>, les nombres suivent un système différent de celui de la France : <em>septante</em> (70) et <em>nonante</em> (90) remplacent <em>soixante-dix</em> et <em>quatre-vingt-dix</em> ; la Suisse ajoute <em>huitante</em> (80) dans certains cantons. En Belgique, <em>une drache</em> désigne une forte pluie, et <em>un essuie</em> une serviette.</p><p>En <strong>Afrique francophone</strong> (Sénégal, Côte d'Ivoire, RDC, entre autres), le français intègre des mots empruntés aux langues locales et des créations propres : <em>essencerie</em> (station-service, Côte d'Ivoire), <em>deuxième bureau</em> (maîtresse, expression ivoirienne), <em>go</em> (jeune fille, argot ivoirien). Comprendre ces variantes, sans nécessairement les employer, permet de suivre un film, un roman ou une conversation authentique venus de n'importe quelle région francophone.</p>",
            "rules": [
                {"heading": "a) Vocabulaire québécois courant", "body": "<ul><li><em>chandail</em> (pull), <em>blonde/chum</em> (copine/copain), <em>magasiner</em> (faire du shopping), <em>dépanneur</em> (épicerie de quartier).</li></ul>"},
                {"heading": "b) Les nombres en Belgique et en Suisse", "body": "<ul><li><em>septante</em> (70), <em>nonante</em> (90) ; <em>huitante</em> (80, dans certains cantons suisses) remplacent les formes composées françaises.</li></ul>"},
                {"heading": "c) Belgicismes courants", "body": "<ul><li><em>une drache</em> (forte pluie), <em>un essuie</em> (serviette), <em>une farde</em> (classeur/dossier).</li></ul>"},
                {"heading": "d) Africanismes francophones", "body": "<ul><li>Emprunts et créations locales variant selon le pays ; comprendre en contexte plutôt que mémoriser une liste fermée.</li></ul>"},
            ],
            "examples": [
                "Il fait froid, mets ton chandail avant de sortir.",
                "Je vais magasiner cet après-midi avec ma blonde.",
                "Passe au dépanneur, on n'a plus de lait.",
                "Il est né en mille neuf cent septante-deux.",
                "Le prix a augmenté de nonante euros ce mois-ci.",
                "Il y a eu une sacrée drache ce matin, j'étais trempé.",
                "Range ce document dans la farde bleue, s'il te plaît.",
            ],
            "commonMistakes": [
                {"wrong": "Croire que « soixante-dix » est incorrect parce que le Québec, la Belgique et la Suisse disent tous « septante ».", "right": "Reconnaître que soixante-dix (France) et septante (Belgique, Suisse) coexistent, chacun correct dans sa région.", "why": "Ce sont deux systèmes régionaux valides, non une forme correcte et une forme fautive."},
                {"wrong": "Employer « magasiner » ou « chandail » en pensant que c'est un mot familier de France.", "right": "Situer ces mots comme des québécismes, distincts du vocabulaire hexagonal (faire du shopping, pull).", "why": "Un francophone de France ne les emploie généralement pas, même s'il les comprend souvent grâce aux médias québécois."},
                {"wrong": "Penser que tous les francophones d'Afrique partagent exactement le même vocabulaire régional.", "right": "Comprendre que chaque pays africain francophone développe ses propres régionalismes, distincts d'un pays à l'autre.", "why": "Le français d'Afrique n'est pas une variété unique et homogène, mais un ensemble de variétés nationales."},
            ],
        },
        "exercises": [
            {"id": "c2var-mc", "type": "multiple-choice", "title": "Situe le Régionalisme",
             "items": [
                {"id": "c2varm1", "prompt": "« Magasiner » signifie faire du shopping dans quelle variété du français ?", "options": ["Le français québécois", "Le français de Belgique", "Le français de Suisse"], "answerIndex": 0, "explanation": "Magasiner est un québécisme courant."},
                {"id": "c2varm2", "prompt": "Quels pays disent « septante » pour 70 ?", "options": ["La Belgique et la Suisse", "Le Québec uniquement", "La France uniquement"], "answerIndex": 0, "explanation": "La France utilise soixante-dix ; septante est belge et suisse."},
                {"id": "c2varm3", "prompt": "Que signifie « une drache » en Belgique ?", "options": ["Une forte pluie", "Une petite épicerie", "Un classeur"], "answerIndex": 0, "explanation": "C'est un belgicisme désignant une averse importante."},
                {"id": "c2varm4", "prompt": "Que désigne « un dépanneur » au Québec ?", "options": ["Une petite épicerie de quartier ouverte tard", "Un mécanicien automobile", "Un policier"], "answerIndex": 0, "explanation": "C'est le sens québécois courant, distinct du sens français de « personne qui répare »."},
             ]},
            {"id": "c2var-fill", "type": "fill-blank", "title": "Complète avec le Mot Régional",
             "items": [
                {"id": "c2varf1", "prompt": "Au Québec, un pull se dit un ___.", "answers": [["chandail"]], "options": ["chandail", "essuie", "farde"], "explanation": "Chandail est le mot québécois pour pull."},
                {"id": "c2varf2", "prompt": "En Belgique, une serviette de toilette se dit un ___.", "answers": [["essuie"]], "options": ["essuie", "chandail", "dépanneur"], "explanation": "Essuie est le belgicisme courant pour serviette."},
                {"id": "c2varf3", "prompt": "En Suisse (certains cantons) et en Belgique, 90 se dit ___.", "answers": [["nonante"]], "options": ["nonante", "quatre-vingt-dix", "septante"], "explanation": "Nonante remplace quatre-vingt-dix dans ces régions."},
                {"id": "c2varf4", "prompt": "Au Québec, faire du shopping se dit ___.", "answers": [["magasiner"]], "options": ["magasiner", "dracher", "essuyer"], "explanation": "Magasiner est le verbe québécois pour faire du shopping."},
             ]},
            {"id": "c2var-correction", "type": "correction", "title": "Identifie la Région Correcte",
             "items": [
                {"id": "c2varc1", "incorrect": "« Septante » est un mot québécois pour 70.", "answer": ["« Septante » est un mot belge et suisse pour 70, pas québécois."], "explanation": "Le Québec utilise soixante-dix, comme la France."},
                {"id": "c2varc2", "incorrect": "« Chandail » et « magasiner » sont des mots de France courants dans tous les registres.", "answer": ["« Chandail » et « magasiner » sont des québécismes, peu employés en France."], "explanation": "Ce sont des mots typiquement québécois, non de l'usage hexagonal courant."},
                {"id": "c2varc3", "incorrect": "Le vocabulaire du français d'Afrique est identique dans tous les pays francophones du continent.", "answer": ["Le vocabulaire du français d'Afrique varie selon le pays (Sénégal, Côte d'Ivoire, RDC...)."], "explanation": "Chaque pays africain francophone a développé ses propres régionalismes."},
             ]},
        ],
        "summary": [
            "Le Québec a son propre vocabulaire courant (chandail, magasiner, dépanneur, blonde/chum), distinct du français de France.",
            "La Belgique et la Suisse utilisent septante/nonante (et huitante en Suisse) au lieu des formes composées françaises.",
            "Le français d'Afrique francophone varie selon les pays, avec des emprunts et créations locales propres à chacun.",
        ],
    },
    {
        "id": "c2-lironie-limplicite-et-les-sous-entendus",
        "level": "C2", "unit": "1", "order": 5, "skill": "reading", "strand": "implicite",
        "title": "L'Ironie, l'Implicite et les Sous-entendus",
        "subtitle": "Lire entre les lignes : litote, antiphrase ironique et sous-entendus culturels du français.",
        "objectives": [
            "Reconnaître l'ironie par antiphrase, où l'on dit le contraire de ce que l'on pense.",
            "Identifier la litote, qui atténue pour mieux souligner.",
            "Repérer les marqueurs de ton qui signalent qu'un énoncé ne doit pas être pris au premier degré.",
        ],
        "content": {
            "intro": "Une phrase française peut vouloir dire exactement le contraire de ce qu'elle affirme littéralement, ou suggérer beaucoup plus qu'elle ne dit : au niveau C2, savoir repérer ces effets devient aussi important que de comprendre le sens littéral.",
            "explanation": "<p>L'<strong>ironie par antiphrase</strong> consiste à dire le contraire de ce que l'on pense, pour se moquer ou critiquer avec légèreté : <em>Quelle belle journée !</em>, dit sous une pluie battante. À l'écrit, elle se signale souvent par le contexte ou par des guillemets ironiques ; à l'oral, par l'intonation. La <strong>litote</strong> fait l'inverse : elle atténue volontairement une affirmation pour, paradoxalement, en renforcer l'effet — <em>Ce n'est pas mauvais</em> pour dire que c'est très bon, <em>Je ne te déteste pas</em> pour suggérer une réelle affection.</p><p>Le français cultive aussi les <strong>sous-entendus</strong> culturels, où l'on suggère sans jamais affirmer directement — une politesse qui évite la confrontation frontale : <em>Il serait peut-être temps de penser à partir</em> peut signifier, selon le ton, « je veux que tu partes maintenant ». Repérer ces sous-entendus demande d'être attentif au contexte, au ton et à ce qui n'est pas dit autant qu'à ce qui l'est.</p>",
            "rules": [
                {"heading": "a) L'ironie par antiphrase", "body": "<ul><li>Dire le contraire de ce qu'on pense, signalé par le contexte ou l'intonation : <em>Quelle belle journée !</em> sous la pluie.</li></ul>"},
                {"heading": "b) La litote", "body": "<ul><li>Atténuer pour renforcer : <em>ce n'est pas mauvais</em> = c'est très bon.</li></ul>"},
                {"heading": "c) Les marqueurs de ton", "body": "<ul><li>Guillemets ironiques à l'écrit, intonation particulière à l'oral, contexte contradictoire avec l'énoncé littéral.</li></ul>"},
                {"heading": "d) Les sous-entendus culturels", "body": "<ul><li>Suggérer sans affirmer, souvent par politesse ou pour éviter la confrontation directe.</li></ul>"},
            ],
            "examples": [
                "Quelle belle journée ! (dit sous une pluie battante)",
                "Ce n'est pas mauvais du tout, ton gâteau.",
                "Je ne te déteste pas, tu sais.",
                "Il serait peut-être temps de penser à partir.",
                "Ah, bravo, vraiment bien joué ! (à quelqu'un qui vient de faire une bêtise)",
                "Ce n'est pas très malin, ce que tu as fait là.",
                "Tu pourrais peut-être faire un effort, de temps en temps.",
            ],
            "commonMistakes": [
                {"wrong": "Prendre au premier degré « Quelle belle journée ! » dit sous la pluie.", "right": "Reconnaître l'antiphrase ironique grâce à la contradiction évidente entre le contexte et l'énoncé.", "why": "Le sens ironique s'oppose délibérément au sens littéral ; le contexte donne toujours la clé."},
                {"wrong": "Croire que « ce n'est pas mauvais » signifie « c'est moyen ».", "right": "Comprendre que la litote atténue pour renforcer : « ce n'est pas mauvais » signifie souvent « c'est très bon ».", "why": "La litote fonctionne par understatement volontaire, pas par évaluation neutre."},
                {"wrong": "Répondre littéralement à un sous-entendu poli sans percevoir le message réel.", "right": "Repérer le sous-entendu (ex. « il serait temps de partir » = je veux que tu partes) et y répondre en conséquence.", "why": "La politesse française préfère souvent suggérer plutôt qu'affirmer directement une demande délicate."},
            ],
        },
        "exercises": [
            {"id": "c2iro-mc", "type": "multiple-choice", "title": "Identifie le Procédé Implicite",
             "items": [
                {"id": "c2irom1", "prompt": "« Quelle belle journée ! » dit sous une pluie battante illustre quel procédé ?", "options": ["L'ironie par antiphrase", "La litote", "Le sous-entendu poli"], "answerIndex": 0, "explanation": "On dit le contraire de ce qu'on pense, avec une intention moqueuse."},
                {"id": "c2irom2", "prompt": "Que signifie généralement « ce n'est pas mauvais » à propos d'un plat qu'on adore ?", "options": ["C'est très bon (litote)", "C'est moyen, sans plus", "C'est franchement mauvais"], "answerIndex": 0, "explanation": "La litote atténue pour renforcer l'effet positif."},
                {"id": "c2irom3", "prompt": "Que peut signifier « il serait peut-être temps de penser à partir » selon le ton employé ?", "options": ["Je veux que tu partes maintenant", "Tu as encore beaucoup de temps", "Rien de particulier"], "answerIndex": 0, "explanation": "C'est un sous-entendu poli qui évite la confrontation directe."},
                {"id": "c2irom4", "prompt": "Comment reconnaît-on souvent l'ironie à l'écrit ?", "options": ["Par une contradiction entre le contexte et l'énoncé, parfois des guillemets", "Par l'emploi systématique du conditionnel", "Par l'absence totale de ponctuation"], "answerIndex": 0, "explanation": "Le contexte contradictoire est le principal indice écrit de l'ironie."},
             ]},
            {"id": "c2iro-fill", "type": "fill-blank", "title": "Complète pour Créer l'Effet Voulu",
             "items": [
                {"id": "c2irof1", "prompt": "Face à un échec évident d'un collègue, dire ironiquement : « Ah, ___ joué ! »", "answers": [["bravo, vraiment bien"]], "options": ["bravo, vraiment bien", "vraiment mal", "quel dommage"], "explanation": "L'antiphrase ironique félicite en apparence pour critiquer en réalité."},
                {"id": "c2irof2", "prompt": "Pour dire poliment qu'un plat est délicieux, par litote : « Ce n'est pas ___. »", "answers": [["mauvais"]], "options": ["mauvais", "excellent", "fade"], "explanation": "La litote atténue le compliment pour, paradoxalement, le renforcer."},
                {"id": "c2irof3", "prompt": "Sous-entendre poliment qu'on veut que quelqu'un s'en aille : « Il serait peut-être temps de penser à ___. »", "answers": [["partir"]], "options": ["partir", "rester", "revenir"], "explanation": "Cette formule suggère la demande sans l'affirmer directement."},
                {"id": "c2irof4", "prompt": "Par litote, dire qu'on aime beaucoup quelqu'un : « Je ne te ___ pas, tu sais. »", "answers": [["déteste"]], "options": ["déteste", "aime", "connais"], "explanation": "La négation d'un sentiment fort suggère, par litote, une réelle affection."},
             ]},
            {"id": "c2iro-correction", "type": "correction", "title": "Corrige l'Interprétation",
             "items": [
                {"id": "c2iroc1", "incorrect": "« Quelle belle journée ! » sous la pluie signifie que la personne trouve vraiment la journée magnifique.", "answer": ["« Quelle belle journée ! » sous la pluie est une antiphrase ironique : la personne trouve la journée désagréable."], "explanation": "Le contexte (la pluie) contredit l'énoncé littéral, signalant l'ironie."},
                {"id": "c2iroc2", "incorrect": "« Ce n'est pas mauvais » à propos d'un plat qu'on adore signifie que le plat est simplement acceptable.", "answer": ["« Ce n'est pas mauvais » dans ce contexte signifie, par litote, que le plat est excellent."], "explanation": "La litote renforce l'appréciation en l'atténuant en apparence."},
                {"id": "c2iroc3", "incorrect": "« Il serait peut-être temps de penser à partir » est une simple observation neutre sur l'heure.", "answer": ["« Il serait peut-être temps de penser à partir » est souvent un sous-entendu poli pour demander à quelqu'un de partir."], "explanation": "Cette formule sert typiquement à suggérer une demande sans l'affirmer directement."},
             ]},
        ],
        "summary": [
            "L'ironie par antiphrase dit le contraire de ce qu'on pense ; le contexte révèle toujours la contradiction.",
            "La litote atténue une affirmation pour, paradoxalement, en renforcer l'effet.",
            "Les sous-entendus culturels suggèrent une demande ou un jugement sans l'affirmer directement, souvent par politesse.",
        ],
    },
    {
        "id": "c2-lattenuation-et-la-diplomatie-dans-le-discours",
        "level": "C2", "unit": "1", "order": 6, "skill": "functional", "strand": "attenuation",
        "title": "L'Atténuation et la Diplomatie dans le Discours",
        "subtitle": "Adoucir une critique, une demande ou un désaccord grâce aux stratégies d'atténuation du français soutenu.",
        "objectives": [
            "Employer le conditionnel de politesse et des formules impersonnelles pour adoucir un propos.",
            "Utiliser des expressions de nuance (dans une certaine mesure, il me semble que) pour éviter l'affirmation brutale.",
            "Reformuler une critique directe en une remarque diplomatique équivalente.",
        ],
        "content": {
            "intro": "Dans un contexte professionnel ou délicat, le français dispose de nombreuses stratégies pour dire une chose désagréable sans heurter — une compétence de niveau C2 aussi importante que la grammaire elle-même.",
            "explanation": "<p>Le <strong>conditionnel de politesse</strong>, déjà connu, s'étend ici à des tournures plus subtiles : <em>il me semblerait préférable de</em>, <em>je me permettrais de suggérer</em>, <em>auriez-vous l'obligeance de</em>. Les <strong>formules impersonnelles</strong> (<em>il conviendrait de, il serait souhaitable que</em> + subjonctif) évitent de désigner directement une personne responsable d'un problème. Des <strong>euphémismes</strong> adoucissent une réalité difficile : <em>des difficultés</em> plutôt que <em>des erreurs graves</em>, <em>perfectible</em> plutôt que <em>mauvais</em>.</p><p>Des marqueurs de nuance limitent la portée d'une affirmation pour la rendre moins tranchante : <em>dans une certaine mesure, il me semble que, on pourrait penser que, à première vue</em>. Une critique directe (<em>Ce rapport est mauvais</em>) se reformule ainsi en une remarque diplomatique (<em>Il me semble que ce rapport gagnerait à être retravaillé sur certains points</em>) — le sens critique reste présent, mais la forme préserve la relation avec l'interlocuteur.</p>",
            "rules": [
                {"heading": "a) Conditionnel de politesse étendu", "body": "<ul><li><em>Il me semblerait préférable de, je me permettrais de suggérer</em> — adoucissent une suggestion ou une demande.</li></ul>"},
                {"heading": "b) Formules impersonnelles", "body": "<ul><li><em>Il conviendrait de, il serait souhaitable que</em> + subjonctif — évitent de désigner un responsable direct.</li></ul>"},
                {"heading": "c) Euphémismes", "body": "<ul><li><em>Des difficultés</em> pour des erreurs graves, <em>perfectible</em> pour mauvais — adoucissent une réalité négative.</li></ul>"},
                {"heading": "d) Marqueurs de nuance", "body": "<ul><li><em>Dans une certaine mesure, il me semble que, à première vue</em> — limitent la portée d'une affirmation.</li></ul>"},
            ],
            "examples": [
                "Il me semblerait préférable de revoir ce point avant la présentation.",
                "Je me permettrais de suggérer une approche légèrement différente.",
                "Il conviendrait de clarifier certains éléments de ce dossier.",
                "Ce projet est perfectible sur plusieurs aspects.",
                "Il me semble, dans une certaine mesure, que ce choix mérite d'être reconsidéré.",
                "À première vue, ce plan présente quelques difficultés.",
                "Auriez-vous l'obligeance de revoir ce paragraphe avant demain ?",
            ],
            "commonMistakes": [
                {"wrong": "Ce rapport est mauvais et truffé d'erreurs (dans un contexte professionnel délicat).", "right": "Il me semble que ce rapport gagnerait à être retravaillé sur certains points.", "why": "La reformulation diplomatique préserve le sens critique tout en évitant une confrontation brutale."},
                {"wrong": "Tu dois corriger ça immédiatement.", "right": "Il conviendrait de corriger ce point dès que possible.", "why": "La formule impersonnelle atténue l'ordre direct en une recommandation plus douce."},
                {"wrong": "Employer un euphémisme si vague que le message critique disparaît totalement.", "right": "Choisir un euphémisme qui adoucit la forme sans effacer le fond du message.", "why": "L'atténuation doit rester compréhensible ; trop de vague nuit à la communication."},
            ],
        },
        "exercises": [
            {"id": "c2att-mc", "type": "multiple-choice", "title": "Choisis la Formule Diplomatique",
             "items": [
                {"id": "c2attm1", "prompt": "Quelle formule adoucit le mieux une critique directe ?", "options": ["Il me semble que ce rapport gagnerait à être retravaillé.", "Ce rapport est nul.", "Refais ce rapport, il est raté."], "answerIndex": 0, "explanation": "La formule impersonnelle et nuancée préserve la relation professionnelle."},
                {"id": "c2attm2", "prompt": "Que permet une formule impersonnelle comme « il conviendrait de » ?", "options": ["Éviter de désigner directement un responsable", "Accuser plus fermement quelqu'un", "Rendre le message incompréhensible"], "answerIndex": 0, "explanation": "C'est justement son rôle diplomatique."},
                {"id": "c2attm3", "prompt": "Quel euphémisme convient pour adoucir « mauvais » dans une évaluation ?", "options": ["Perfectible", "Excellent", "Génial"], "answerIndex": 0, "explanation": "Perfectible reconnaît un défaut tout en restant constructif."},
                {"id": "c2attm4", "prompt": "Quel marqueur limite la portée d'une affirmation ?", "options": ["Dans une certaine mesure", "Absolument", "Sans aucun doute"], "answerIndex": 0, "explanation": "Ce marqueur nuance l'affirmation plutôt que de la rendre catégorique."},
             ]},
            {"id": "c2att-fill", "type": "fill-blank", "title": "Complète avec la Tournure Atténuée",
             "items": [
                {"id": "c2attf1", "prompt": "Il me ___ préférable de revoir ce point avant la présentation.", "answers": [["semblerait"]], "options": ["semblerait", "semble", "sembla"], "explanation": "Le conditionnel de politesse adoucit la suggestion."},
                {"id": "c2attf2", "prompt": "Il ___ de clarifier certains éléments de ce dossier.", "answers": [["conviendrait"]], "options": ["conviendrait", "faut", "fallait"], "explanation": "Il conviendrait de est une formule impersonnelle diplomatique."},
                {"id": "c2attf3", "prompt": "Ce projet est ___ sur plusieurs aspects (au lieu de dire qu'il est mauvais).", "answers": [["perfectible"]], "options": ["perfectible", "nul", "raté"], "explanation": "Perfectible est l'euphémisme approprié."},
                {"id": "c2attf4", "prompt": "___ première vue, ce plan présente quelques difficultés.", "answers": [["À"]], "options": ["À", "En", "Sur"], "explanation": "L'expression figée est à première vue."},
             ]},
            {"id": "c2att-correction", "type": "correction", "title": "Reformule Diplomatiquement",
             "instructions": "Réécris chaque phrase directe en une formule plus diplomatique.",
             "items": [
                {"id": "c2attc1", "incorrect": "Ce rapport est mauvais et truffé d'erreurs.", "answer": ["Il me semble que ce rapport gagnerait à être retravaillé sur certains points."], "explanation": "La reformulation préserve le sens critique en une forme moins directe."},
                {"id": "c2attc2", "incorrect": "Tu dois corriger ça immédiatement.", "answer": ["Il conviendrait de corriger ce point dès que possible."], "explanation": "La formule impersonnelle adoucit l'ordre direct."},
                {"id": "c2attc3", "incorrect": "Cette idée est nulle.", "answer": ["Cette idée est perfectible et mériterait d'être retravaillée."], "explanation": "L'euphémisme perfectible adoucit le jugement sans le supprimer."},
             ]},
        ],
        "summary": [
            "Le conditionnel de politesse et les formules impersonnelles (il conviendrait de) adoucissent une demande ou une critique.",
            "Les euphémismes (perfectible pour mauvais) préservent le sens tout en évitant la brutalité.",
            "Les marqueurs de nuance (dans une certaine mesure, à première vue) limitent la portée d'une affirmation trop tranchante.",
        ],
    },
    {
        "id": "c2-les-expressions-idiomatiques-avancees",
        "level": "C2", "unit": "1", "order": 7, "skill": "vocabulary", "strand": "idiomes-avances",
        "title": "Les Expressions Idiomatiques Avancées",
        "subtitle": "Employer correctement, en contexte, un ensemble d'expressions idiomatiques riches et leur origine.",
        "objectives": [
            "Comprendre le sens figuré d'un ensemble d'expressions idiomatiques avancées.",
            "Situer l'origine ou la logique imagée d'une expression pour mieux la retenir.",
            "Employer ces expressions dans un contexte approprié, sans les prendre au sens littéral.",
        ],
        "content": {
            "intro": "Le français regorge d'expressions imagées qu'un locuteur natif cultivé emploie naturellement ; les comprendre et les utiliser à bon escient distingue un niveau C2 d'un niveau simplement avancé.",
            "explanation": "<p>Certaines expressions viennent d'images concrètes devenues abstraites : <em>avoir le cafard</em> (être triste, déprimé — de l'argot du XIXe siècle), <em>poser un lapin à quelqu'un</em> (ne pas venir à un rendez-vous), <em>être sur des charbons ardents</em> (être très impatient ou anxieux), <em>tirer les vers du nez à quelqu'un</em> (le faire parler indirectement), <em>avoir un poil dans la main</em> (être très paresseux), <em>mettre la charrue avant les bœufs</em> (faire les choses dans le mauvais ordre).</p><p>Chaque expression a un sens figuré fixe, indépendant de sa logique image d'origine — il ne faut jamais la traduire littéralement ni tenter de la moduler grammaticalement (on ne dit pas « poser des lapins » au pluriel avec le même sens, ni changer l'article). L'emploi correct dépend aussi du registre : ces expressions sont surtout orales et familières à soutenues selon le cas, rarement administratives.</p>",
            "rules": [
                {"heading": "a) Expressions liées à l'humeur", "body": "<ul><li><em>Avoir le cafard</em> (être triste), <em>être sur des charbons ardents</em> (être impatient/anxieux).</li></ul>"},
                {"heading": "b) Expressions liées à l'action sociale", "body": "<ul><li><em>Poser un lapin</em> (ne pas venir à un rendez-vous), <em>tirer les vers du nez</em> (faire parler indirectement).</li></ul>"},
                {"heading": "c) Expressions liées au comportement", "body": "<ul><li><em>Avoir un poil dans la main</em> (être paresseux), <em>mettre la charrue avant les bœufs</em> (agir dans le mauvais ordre).</li></ul>"},
                {"heading": "d) Fixité de la forme", "body": "<ul><li>Ces expressions ne se modulent pas grammaticalement (article, nombre) sans perdre leur sens figuré.</li></ul>"},
            ],
            "examples": [
                "Depuis quelques jours, j'ai un peu le cafard.",
                "Il m'a posé un lapin hier soir, je l'ai attendu une heure pour rien.",
                "Elle était sur des charbons ardents avant les résultats de l'examen.",
                "Arrête de tourner autour du pot, je vais finir par te tirer les vers du nez.",
                "Il a un poil dans la main, il ne lève jamais le petit doigt à la maison.",
                "Ne mets pas la charrue avant les bœufs, finis d'abord ce dossier.",
                "Je crois qu'on lui a posé un lapin plus d'une fois cette année.",
            ],
            "commonMistakes": [
                {"wrong": "Traduire littéralement « avoir le cafard » comme s'il s'agissait vraiment d'un insecte.", "right": "Comprendre que cette expression signifie simplement « être triste, déprimé ».", "why": "Le sens figuré s'est totalement détaché de l'image d'origine ; il faut le mémoriser tel quel."},
                {"wrong": "Dire « poser des lapins » au pluriel avec un sens différent, ou changer l'article.", "right": "Garder la forme fixe : poser un lapin à quelqu'un, sans variation grammaticale du sens figuré.", "why": "Les expressions idiomatiques sont figées ; les modifier casse leur sens conventionnel."},
                {"wrong": "Employer « mettre la charrue avant les bœufs » dans un contexte administratif très formel.", "right": "Réserver cette expression à un registre courant ou familier, à l'oral ou dans un écrit détendu.", "why": "C'est une expression imagée de registre courant, peu adaptée à un rapport officiel."},
            ],
        },
        "exercises": [
            {"id": "c2idi-mc", "type": "multiple-choice", "title": "Comprends le Sens Figuré",
             "items": [
                {"id": "c2idim1", "prompt": "Que signifie « avoir le cafard » ?", "options": ["Être triste, déprimé", "Être très occupé", "Être en retard"], "answerIndex": 0, "explanation": "C'est une expression figée signifiant la mélancolie."},
                {"id": "c2idim2", "prompt": "Que signifie « poser un lapin à quelqu'un » ?", "options": ["Ne pas venir à un rendez-vous prévu", "Offrir un cadeau surprise", "Raconter une blague"], "answerIndex": 0, "explanation": "C'est le sens figuré fixe de cette expression."},
                {"id": "c2idim3", "prompt": "Que signifie « mettre la charrue avant les bœufs » ?", "options": ["Faire les choses dans le mauvais ordre", "Travailler très efficacement", "Refuser de travailler"], "answerIndex": 0, "explanation": "L'image agricole illustre un ordre logique inversé."},
                {"id": "c2idim4", "prompt": "Que signifie « avoir un poil dans la main » ?", "options": ["Être très paresseux", "Être très habile de ses mains", "Avoir peur"], "answerIndex": 0, "explanation": "C'est une expression familière désignant la paresse."},
             ]},
            {"id": "c2idi-fill", "type": "fill-blank", "title": "Complète l'Expression Idiomatique",
             "items": [
                {"id": "c2idif1", "prompt": "Depuis son déménagement, elle a un peu le ___.", "answers": [["cafard"]], "options": ["cafard", "lapin", "poil"], "explanation": "Avoir le cafard = être triste."},
                {"id": "c2idif2", "prompt": "Il m'a posé un ___ hier soir, je l'ai attendu pour rien.", "answers": [["lapin"]], "options": ["lapin", "cafard", "charbon"], "explanation": "Poser un lapin = ne pas venir à un rendez-vous."},
                {"id": "c2idif3", "prompt": "Elle était sur des ___ ardents avant les résultats.", "answers": [["charbons"]], "options": ["charbons", "lapins", "poils"], "explanation": "Être sur des charbons ardents = être très impatient ou anxieux."},
                {"id": "c2idif4", "prompt": "Arrête de tourner autour du pot, je vais te tirer les ___ du nez.", "answers": [["vers"]], "options": ["vers", "lapins", "charbons"], "explanation": "Tirer les vers du nez = faire parler indirectement."},
             ]},
            {"id": "c2idi-correction", "type": "correction", "title": "Corrige l'Emploi de l'Expression",
             "items": [
                {"id": "c2idic1", "incorrect": "Il a vraiment un cafard dans son appartement, c'est dégoûtant.", "answer": ["Il a vraiment le cafard en ce moment, il traverse une période difficile."], "explanation": "Dans le sens figuré recherché ici, cafard = tristesse, pas l'insecte."},
                {"id": "c2idic2", "incorrect": "Elle a posé des lapins à son collègue, un rose et un blanc.", "answer": ["Elle a posé un lapin à son collègue, il l'a attendue en vain."], "explanation": "L'expression figée reste au singulier avec ce sens figuré."},
                {"id": "c2idic3", "incorrect": "Il faut mettre la charrue avant les bœufs pour bien réussir ce projet.", "answer": ["Il ne faut pas mettre la charrue avant les bœufs pour bien réussir ce projet."], "explanation": "L'expression désigne une erreur d'ordre à éviter, pas une méthode à suivre."},
             ]},
        ],
        "summary": [
            "Chaque expression idiomatique a un sens figuré fixe, indépendant de son image d'origine, à mémoriser tel quel.",
            "Ces expressions ne se modulent pas grammaticalement (article, nombre) sans perdre leur sens conventionnel.",
            "Leur registre est généralement courant à familier, rarement adapté à un écrit administratif très formel.",
        ],
    },
    {
        "id": "c2-lanalyse-et-la-synthese-de-documents-complexes",
        "level": "C2", "unit": "1", "order": 8, "skill": "reading", "strand": "analyse-synthese",
        "title": "L'Analyse et la Synthèse de Documents Complexes",
        "subtitle": "Extraire la thèse d'un texte dense, distinguer l'argument de l'exemple, et reformuler en un résumé condensé.",
        "objectives": [
            "Distinguer, dans un texte argumentatif dense, la thèse centrale des arguments et exemples qui la soutiennent.",
            "Reformuler l'essentiel d'un document complexe en un résumé condensé et fidèle.",
            "Identifier un présupposé implicite ou un biais dans un texte argumentatif.",
        ],
        "content": {
            "intro": "Au niveau C2, comprendre un texte ne suffit plus : il faut pouvoir en extraire la structure argumentative, distinguer l'essentiel de l'accessoire, et le reformuler fidèlement en un format condensé — une compétence centrale de l'épreuve DALF C2.",
            "explanation": "<p>Un texte argumentatif dense articule généralement une <strong>thèse</strong> (l'idée centrale défendue), des <strong>arguments</strong> (les raisons générales qui la soutiennent) et des <strong>exemples</strong> (illustrations concrètes de chaque argument). Pour analyser un tel texte, il faut d'abord repérer la thèse — souvent énoncée dès l'introduction ou reformulée en conclusion — puis relier chaque paragraphe à l'argument qu'il développe, en distinguant ce qui est une preuve générale de ce qui n'est qu'une illustration particulière.</p><p>La synthèse consiste ensuite à condenser cette structure en conservant la logique du raisonnement, sans en trahir la nuance ni y ajouter d'opinion personnelle : reformuler avec ses propres mots, réduire les exemples à leur fonction argumentative, et signaler les <strong>présupposés implicites</strong> (ce que l'auteur tient pour acquis sans le démontrer) quand ils orientent le raisonnement de façon significative.</p>",
            "rules": [
                {"heading": "a) Repérer la thèse", "body": "<ul><li>Souvent énoncée en introduction et reformulée en conclusion ; c'est l'idée que tout le texte défend.</li></ul>"},
                {"heading": "b) Distinguer argument et exemple", "body": "<ul><li>L'argument est une raison générale ; l'exemple l'illustre par un cas particulier, sans la remplacer.</li></ul>"},
                {"heading": "c) Reformuler fidèlement", "body": "<ul><li>Condenser avec ses propres mots, sans trahir la nuance ni ajouter une opinion personnelle absente du texte.</li></ul>"},
                {"heading": "d) Repérer les présupposés implicites", "body": "<ul><li>Identifier ce que l'auteur tient pour acquis sans le démontrer, quand cela oriente significativement le raisonnement.</li></ul>"},
            ],
            "examples": [
                "La thèse de l'auteur est que l'éducation à distance ne remplace jamais totalement l'enseignement en présentiel.",
                "Son premier argument repose sur l'importance de l'interaction sociale dans l'apprentissage.",
                "Il illustre cet argument par l'exemple d'une étude menée auprès de lycéens en 2020.",
                "Le texte présuppose, sans le démontrer, que tous les élèves ont un accès égal à internet.",
                "En résumé, l'auteur défend l'idée que la technologie complète l'enseignement traditionnel sans le remplacer.",
                "Cet exemple n'est qu'une illustration ponctuelle ; l'argument central reste plus général.",
                "Le raisonnement de l'auteur repose sur un présupposé culturel qui mériterait d'être questionné.",
            ],
            "commonMistakes": [
                {"wrong": "Confondre un exemple particulier avec un argument général dans un résumé.", "right": "Réduire l'exemple à sa fonction d'illustration et ne conserver que l'argument qu'il soutient.", "why": "Un résumé fidèle distingue le niveau général (argument) du niveau particulier (exemple)."},
                {"wrong": "Ajouter sa propre opinion personnelle en résumant la thèse d'un auteur.", "right": "Reformuler fidèlement la thèse de l'auteur, sans y mêler un jugement personnel non présent dans le texte.", "why": "La synthèse doit rester fidèle au texte source, sans déformation par le point de vue du lecteur."},
                {"wrong": "Ignorer un présupposé implicite qui oriente fortement l'argumentation.", "right": "Signaler ce présupposé quand il joue un rôle significatif dans le raisonnement de l'auteur.", "why": "Une analyse de niveau C2 va au-delà du texte explicite pour en révéler les fondements non dits."},
            ],
        },
        "exercises": [
            {"id": "c2ana-mc", "type": "multiple-choice", "title": "Analyse la Structure Argumentative",
             "items": [
                {"id": "c2anam1", "prompt": "Où trouve-t-on le plus souvent la thèse d'un texte argumentatif ?", "options": ["En introduction, reformulée en conclusion", "Uniquement dans le titre", "Toujours dans le dernier exemple"], "answerIndex": 0, "explanation": "C'est la structure la plus fréquente d'un texte argumentatif."},
                {"id": "c2anam2", "prompt": "Quelle est la différence entre un argument et un exemple ?", "options": ["L'argument est général, l'exemple l'illustre par un cas particulier", "Ce sont deux synonymes interchangeables", "L'exemple est toujours plus important que l'argument"], "answerIndex": 0, "explanation": "C'est la distinction centrale pour analyser un texte argumentatif."},
                {"id": "c2anam3", "prompt": "Qu'est-ce qu'un présupposé implicite ?", "options": ["Ce que l'auteur tient pour acquis sans le démontrer", "Un exemple explicite donné par l'auteur", "La conclusion du texte"], "answerIndex": 0, "explanation": "C'est un élément non démontré mais sous-jacent au raisonnement."},
                {"id": "c2anam4", "prompt": "Que doit éviter une bonne synthèse ?", "options": ["D'ajouter une opinion personnelle absente du texte source", "De reformuler avec ses propres mots", "De condenser le texte"], "answerIndex": 0, "explanation": "La fidélité au texte source exclut le jugement personnel du rédacteur de la synthèse."},
             ]},
            {"id": "c2ana-fill", "type": "fill-blank", "title": "Complète l'Analyse",
             "items": [
                {"id": "c2anaf1", "prompt": "La ___ de l'auteur est l'idée centrale que tout le texte défend.", "answers": [["thèse"]], "options": ["thèse", "exemple", "conclusion uniquement"], "explanation": "C'est le terme technique pour l'idée défendue."},
                {"id": "c2anaf2", "prompt": "Un ___ illustre un argument par un cas particulier, sans le remplacer.", "answers": [["exemple"]], "options": ["exemple", "présupposé", "titre"], "explanation": "L'exemple reste au niveau particulier, l'argument au niveau général."},
                {"id": "c2anaf3", "prompt": "Un ___ implicite est ce que l'auteur tient pour acquis sans le démontrer.", "answers": [["présupposé"]], "options": ["présupposé", "exemple", "résumé"], "explanation": "C'est un élément non démontré mais sous-jacent au texte."},
                {"id": "c2anaf4", "prompt": "Une bonne synthèse ___ le texte source avec ses propres mots, sans le trahir.", "answers": [["reformule"]], "options": ["reformule", "copie", "ignore"], "explanation": "La reformulation fidèle est la base de la synthèse."},
             ]},
            {"id": "c2ana-correction", "type": "correction", "title": "Corrige l'Analyse",
             "items": [
                {"id": "c2anac1", "incorrect": "Dans ce résumé, l'exemple de l'étude de 2020 est présenté comme la thèse principale du texte.", "answer": ["Dans ce résumé, l'exemple de l'étude de 2020 illustre un argument, mais n'est pas la thèse principale du texte."], "explanation": "Un exemple particulier ne doit pas être confondu avec la thèse générale."},
                {"id": "c2anac2", "incorrect": "Le résumé ajoute que l'auteur a tort, ce qui n'apparaît nulle part dans le texte original.", "answer": ["Le résumé se limite à reformuler fidèlement la thèse de l'auteur, sans jugement personnel absent du texte."], "explanation": "La synthèse doit rester fidèle, sans opinion ajoutée par le rédacteur."},
                {"id": "c2anac3", "incorrect": "Le texte ne contient aucun présupposé, seulement des faits démontrés.", "answer": ["Le texte contient un présupposé implicite (l'égal accès à internet) qui n'est jamais démontré."], "explanation": "Un texte argumentatif repose presque toujours sur au moins un présupposé non démontré."},
             ]},
        ],
        "summary": [
            "La thèse (l'idée centrale) se distingue des arguments (raisons générales) et des exemples (illustrations particulières).",
            "Une synthèse fidèle reformule avec ses propres mots, sans ajouter d'opinion personnelle absente du texte source.",
            "Repérer les présupposés implicites d'un texte révèle les fondements non démontrés de son raisonnement.",
        ],
    },
    {
        "id": "c2-la-creativite-lexicale-neologismes-et-jeux-de-mots",
        "level": "C2", "unit": "1", "order": 9, "skill": "vocabulary", "strand": "creativite-lexicale",
        "title": "La Créativité Lexicale : Néologismes et Jeux de Mots",
        "subtitle": "Reconnaître et former des néologismes par affixation, et comprendre les jeux de mots courants.",
        "objectives": [
            "Reconnaître les procédés productifs de formation de néologismes (préfixation, suffixation, mots-valises).",
            "Comprendre un calembour ou un jeu de mots fondé sur l'homophonie ou la polysémie.",
            "Créer soi-même un néologisme plausible à partir d'un procédé productif du français.",
        ],
        "content": {
            "intro": "Le français, comme toute langue vivante, crée sans cesse de nouveaux mots ; reconnaître les procédés qui les forment, et apprécier un bon jeu de mots, relève d'une maîtrise proche de celle d'un locuteur natif cultivé.",
            "explanation": "<p>Les néologismes se forment le plus souvent par des procédés productifs et prévisibles : la <strong>préfixation</strong> (<em>télétravailler, hyperconnecté, ultraconnecté</em>), la <strong>suffixation</strong> (<em>-iser</em> : <em>fiabiliser, sécuriser</em> ; <em>-esque</em> : <em>kafkaïesque</em> ; <em>-phobe/-phile</em> : <em>technophobe, europhile</em>), et le <strong>mot-valise</strong>, qui fusionne deux mots existants en un seul (<em>franglais</em> = français + anglais, <em>courriel</em> = courrier + électronique, <em>infox</em> = information + intox). Ces procédés permettent, même sans connaître un néologisme précis, d'en deviner le sens probable à partir de ses composants.</p><p>Le <strong>calembour</strong> (jeu de mots) exploite l'homophonie (deux mots qui se prononcent pareil mais s'écrivent différemment : <em>le maire et la mer</em>) ou la polysémie (un même mot à deux sens : <em>Les poules du couvent couvent</em>, où <em>couvent</em> est à la fois un nom et le verbe <em>couver</em> conjugué). Apprécier un calembour demande de percevoir simultanément les deux sens ou les deux mots en jeu — une compétence purement réceptive, rarement nécessaire à l'écrit formel.</p>",
            "rules": [
                {"heading": "a) Préfixation productive", "body": "<ul><li><em>télé-, hyper-, ultra-</em> + verbe/adjectif : <em>télétravailler, hyperconnecté</em>.</li></ul>"},
                {"heading": "b) Suffixation productive", "body": "<ul><li><em>-iser</em> (verbe), <em>-esque</em> (adjectif), <em>-phobe/-phile</em> (attitude) : <em>sécuriser, kafkaïesque, technophobe</em>.</li></ul>"},
                {"heading": "c) Le mot-valise", "body": "<ul><li>Fusion de deux mots existants en un seul : <em>franglais, courriel, infox</em>.</li></ul>"},
                {"heading": "d) Le calembour", "body": "<ul><li>Jeu sur l'homophonie (<em>le maire/la mer</em>) ou la polysémie (un mot à deux sens dans la même phrase).</li></ul>"},
            ],
            "examples": [
                "Le télétravail s'est généralisé depuis quelques années.",
                "Cette entreprise est particulièrement hyperconnectée à ses clients.",
                "Il faut sécuriser ce système avant de le déployer.",
                "Cette bureaucratie absurde a quelque chose de kafkaïesque.",
                "Le courriel a largement remplacé la lettre papier dans les échanges professionnels.",
                "Attention à l'infox qui circule sur les réseaux sociaux.",
                "Les poules du couvent couvent, disait la vieille énigme.",
            ],
            "commonMistakes": [
                {"wrong": "Croire qu'un néologisme comme « hyperconnecté » est forcément incorrect ou fautif.", "right": "Reconnaître qu'un néologisme formé par un procédé productif (préfixe hyper- + participe) est parfaitement légitime.", "why": "Le français crée régulièrement des mots nouveaux par des procédés réguliers et reconnus."},
                {"wrong": "Ne pas percevoir le double sens d'un calembour et le prendre au premier degré uniquement.", "right": "Repérer les deux sens simultanés (homophonie ou polysémie) qui créent l'effet comique ou spirituel.", "why": "Un calembour repose entièrement sur la perception du double sens ; sans elle, l'effet est perdu."},
                {"wrong": "Confondre un mot-valise (fusion de deux mots) avec un simple mot composé (deux mots juxtaposés avec un trait d'union).", "right": "Réserver mot-valise aux fusions qui tronquent et combinent des sons de deux mots (courriel), différent d'un composé classique (porte-monnaie).", "why": "Ce sont deux procédés de formation distincts, même s'ils produisent tous deux des mots nouveaux."},
            ],
        },
        "exercises": [
            {"id": "c2neo-mc", "type": "multiple-choice", "title": "Identifie le Procédé",
             "items": [
                {"id": "c2neom1", "prompt": "Comment se forme le mot « courriel » ?", "options": ["Par fusion (mot-valise) de courrier et électronique", "Par simple préfixation", "Par un emprunt direct à l'anglais"], "answerIndex": 0, "explanation": "C'est un mot-valise créé pour remplacer l'anglicisme e-mail."},
                {"id": "c2neom2", "prompt": "Quel suffixe forme un verbe à partir d'un adjectif comme « sécurisé » ?", "options": ["-iser (sécuriser)", "-esque", "-phile"], "answerIndex": 0, "explanation": "Le suffixe -iser forme des verbes à partir d'adjectifs ou de noms."},
                {"id": "c2neom3", "prompt": "« Les poules du couvent couvent » joue sur quel procédé ?", "options": ["La polysémie/homographie d'un même mot", "La préfixation", "Le mot-valise"], "answerIndex": 0, "explanation": "Couvent est à la fois un nom et une forme verbale, d'où l'effet de calembour."},
                {"id": "c2neom4", "prompt": "Que signifie le suffixe « -phile » dans « europhile » ?", "options": ["Qui aime, qui est favorable à", "Qui craint, qui rejette", "Qui étudie scientifiquement"], "answerIndex": 0, "explanation": "-phile marque l'attirance ou la sympathie, à l'inverse de -phobe."},
             ]},
            {"id": "c2neo-fill", "type": "fill-blank", "title": "Complète avec le Néologisme Approprié",
             "items": [
                {"id": "c2neof1", "prompt": "Le ___ s'est généralisé depuis la généralisation d'internet à haut débit.", "answers": [["télétravail"]], "options": ["télétravail", "franglais", "courriel"], "explanation": "Préfixe télé- + travail, désignant le travail à distance."},
                {"id": "c2neof2", "prompt": "Cette fausse information très répandue est un exemple d'___.", "answers": [["infox"]], "options": ["infox", "courriel", "kafkaïesque"], "explanation": "Infox est le mot-valise recommandé pour fake news."},
                {"id": "c2neof3", "prompt": "Une situation absurde et bureaucratique peut être qualifiée de ___.", "answers": [["kafkaïesque"]], "options": ["kafkaïesque", "technophobe", "hyperconnecté"], "explanation": "Le suffixe -esque, associé au nom Kafka, forme cet adjectif."},
                {"id": "c2neof4", "prompt": "Une personne qui craint ou rejette la technologie est ___.", "answers": [["technophobe"]], "options": ["technophobe", "technophile", "technoesque"], "explanation": "Le suffixe -phobe marque le rejet ou la crainte."},
             ]},
            {"id": "c2neo-correction", "type": "correction", "title": "Corrige l'Analyse du Néologisme",
             "items": [
                {"id": "c2neoc1", "incorrect": "« Courriel » est un emprunt direct de l'anglais « e-mail ».", "answer": ["« Courriel » est un mot-valise français, fusion de courrier et électronique."], "explanation": "C'est une création française destinée à remplacer l'anglicisme, pas un emprunt."},
                {"id": "c2neoc2", "incorrect": "« Hyperconnecté » est un mot incorrect qu'il faut éviter à l'écrit soigné.", "answer": ["« Hyperconnecté » est un néologisme légitime, formé par un procédé de préfixation productif."], "explanation": "Les néologismes formés régulièrement sont parfaitement acceptés en français contemporain."},
                {"id": "c2neoc3", "incorrect": "Le calembour « les poules du couvent couvent » ne joue sur aucun double sens particulier.", "answer": ["Le calembour « les poules du couvent couvent » joue sur la polysémie/homographie du mot couvent (nom et verbe)."], "explanation": "L'effet du calembour repose entièrement sur ce double sens perçu simultanément."},
             ]},
        ],
        "summary": [
            "Les néologismes se forment surtout par préfixation (hyper-, télé-), suffixation (-iser, -esque, -phobe/-phile) et mots-valises (courriel, infox).",
            "Un mot-valise fusionne deux mots existants, contrairement à un simple mot composé juxtaposé.",
            "Un calembour repose sur l'homophonie ou la polysémie, perçues simultanément par le lecteur ou l'auditeur.",
        ],
    },
    {
        "id": "c2-la-reecriture-stylistique-et-ladaptation-de-registre",
        "level": "C2", "unit": "1", "order": 10, "skill": "writing", "strand": "reecriture-stylistique",
        "title": "La Réécriture Stylistique et l'Adaptation de Registre",
        "subtitle": "Exercice de synthèse : transformer un même contenu à travers les registres administratif, courant, littéraire et familier.",
        "objectives": [
            "Identifier les marqueurs lexicaux et syntaxiques propres à chacun des grands registres du français.",
            "Réécrire un même contenu en préservant le sens mais en changeant intégralement de registre.",
            "Choisir le registre approprié à une situation de communication donnée.",
        ],
        "content": {
            "intro": "Cette dernière leçon du cours est un exercice de synthèse : elle mobilise la nominalisation et le style académique (B2-C1), les registres et la variation stylistique (C1), l'atténuation (C2) et les procédés stylistiques littéraires (C2) pour transformer délibérément un même message d'un registre à l'autre.",
            "explanation": "<p>Le registre <strong>administratif</strong> privilégie les formules figées de politesse et l'impersonnel (<em>Nous vous prions de bien vouloir prendre connaissance de ce document</em>). Le registre <strong>courant</strong> reste neutre et direct, sans figure de style ni familiarité (<em>Merci de lire ce document</em>). Le registre <strong>littéraire</strong> recherche l'image et le rythme, quitte à employer le passé simple ou une syntaxe travaillée (<em>Qu'il vous plaise de porter à ce document l'attention qu'il mérite</em>). Le registre <strong>familier</strong> se permet l'ellipse, le vocabulaire relâché et une syntaxe orale (<em>Jette un œil à ce document, tu veux ?</em>).</p><p>Réécrire un même contenu d'un registre à l'autre demande de repérer, dans le texte de départ, ce qui relève du <strong>sens</strong> (à conserver absolument) et ce qui relève de la <strong>forme</strong> (à transformer entièrement) : le vocabulaire, la syntaxe, les formules de politesse ou d'appel, et jusqu'au choix des temps verbaux changent, mais l'information transmise reste identique. C'est l'exercice ultime de maîtrise du français : parler la même langue dans des mondes différents.</p>",
            "rules": [
                {"heading": "a) Registre administratif", "body": "<ul><li>Formules figées, impersonnel : <em>Nous vous prions de bien vouloir...</em></li></ul>"},
                {"heading": "b) Registre courant", "body": "<ul><li>Neutre, direct, sans figure de style ni familiarité : <em>Merci de lire ce document.</em></li></ul>"},
                {"heading": "c) Registre littéraire", "body": "<ul><li>Recherche d'image et de rythme, syntaxe travaillée, parfois passé simple.</li></ul>"},
                {"heading": "d) Registre familier", "body": "<ul><li>Ellipse, vocabulaire relâché, syntaxe orale : <em>Jette un œil à ça, tu veux ?</em></li></ul>"},
            ],
            "examples": [
                "Nous vous prions de bien vouloir prendre connaissance de ce document dans les meilleurs délais. (administratif)",
                "Merci de lire ce document dès que possible. (courant)",
                "Qu'il vous plaise de porter à ce document l'attention qu'il mérite. (littéraire)",
                "Jette un œil à ce truc, tu veux ? (familier)",
                "Veuillez agréer, Madame, Monsieur, l'expression de mes salutations distinguées. (administratif)",
                "Cordialement. (courant)",
                "Reçois, ami lecteur, l'assurance de ma considération la plus sincère. (littéraire, ironique)",
            ],
            "commonMistakes": [
                {"wrong": "Modifier le sens du message en changeant de registre.", "right": "Conserver strictement l'information transmise en ne transformant que la forme (vocabulaire, syntaxe).", "why": "L'exercice de réécriture stylistique vise la forme, jamais le contenu informatif du message."},
                {"wrong": "Employer un registre familier dans une lettre administrative officielle.", "right": "Réserver le registre familier à des échanges informels, et l'administratif aux situations officielles.", "why": "Le choix du registre doit correspondre à la situation de communication réelle, sous peine d'inadéquation grave."},
                {"wrong": "Croire que le registre littéraire est toujours « supérieur » aux autres registres.", "right": "Comprendre que chaque registre est approprié à son contexte propre, sans hiérarchie de valeur absolue.", "why": "Un registre familier bien choisi dans un contexte informel est tout aussi maîtrisé qu'un registre soutenu en contexte formel."},
            ],
        },
        "exercises": [
            {"id": "c2ree-mc", "type": "multiple-choice", "title": "Identifie le Registre",
             "items": [
                {"id": "c2reem1", "prompt": "« Nous vous prions de bien vouloir prendre connaissance de ce document » relève de quel registre ?", "options": ["Administratif", "Familier", "Littéraire"], "answerIndex": 0, "explanation": "Formule figée et impersonnelle typique du registre administratif."},
                {"id": "c2reem2", "prompt": "« Jette un œil à ce truc, tu veux ? » relève de quel registre ?", "options": ["Familier", "Administratif", "Académique"], "answerIndex": 0, "explanation": "Vocabulaire relâché et syntaxe orale typiques du registre familier."},
                {"id": "c2reem3", "prompt": "Que doit-on impérativement conserver en changeant de registre ?", "options": ["Le sens, l'information transmise", "Le vocabulaire exact", "La longueur de la phrase"], "answerIndex": 0, "explanation": "Seule la forme change ; le contenu informatif reste identique."},
                {"id": "c2reem4", "prompt": "Pourquoi le registre familier serait-il inapproprié dans une lettre officielle ?", "options": ["Parce que le registre doit correspondre à la situation de communication", "Parce qu'il est grammaticalement incorrect", "Parce qu'il n'existe pas à l'écrit"], "answerIndex": 0, "explanation": "Ce n'est pas une question de correction grammaticale mais d'adéquation au contexte."},
             ]},
            {"id": "c2ree-fill", "type": "fill-blank", "title": "Identifie le Registre de Chaque Formule",
             "items": [
                {"id": "c2reef1", "prompt": "« Veuillez agréer l'expression de mes salutations distinguées » est du registre ___.", "answers": [["administratif"]], "options": ["administratif", "familier", "courant"], "explanation": "Formule de politesse figée typique des courriers officiels."},
                {"id": "c2reef2", "prompt": "« Merci de lire ce document dès que possible » est du registre ___.", "answers": [["courant"]], "options": ["courant", "littéraire", "administratif"], "explanation": "Formulation neutre, directe, sans marque de registre particulière."},
                {"id": "c2reef3", "prompt": "« Cordialement » en fin de message est du registre ___.", "answers": [["courant"]], "options": ["courant", "familier", "littéraire"], "explanation": "C'est une formule de politesse neutre, ni très formelle ni familière."},
                {"id": "c2reef4", "prompt": "« Qu'il vous plaise de porter à ce document l'attention qu'il mérite » est du registre ___.", "answers": [["littéraire"]], "options": ["littéraire", "familier", "courant"], "explanation": "Syntaxe travaillée et tournure recherchée, typique du registre littéraire."},
             ]},
            {"id": "c2ree-correction", "type": "correction", "title": "Reformule dans le Bon Registre",
             "instructions": "Réécris chaque phrase dans le registre demandé entre parenthèses, en conservant le sens.",
             "items": [
                {"id": "c2reec1", "incorrect": "Jette un œil à ce truc, tu veux ? (à reformuler en registre administratif)", "answer": ["Nous vous prions de bien vouloir prendre connaissance de ce document."], "explanation": "Même demande, formulée avec les formules figées et l'impersonnel du registre administratif."},
                {"id": "c2reec2", "incorrect": "Nous vous prions de bien vouloir nous faire parvenir votre réponse. (à reformuler en registre familier)", "answer": ["Réponds-nous vite, tu veux ?"], "explanation": "Même demande, en syntaxe orale relâchée et vocabulaire familier."},
                {"id": "c2reec3", "incorrect": "Merci de lire ce document. (à reformuler en registre littéraire)", "answer": ["Qu'il vous plaise de porter à ce document l'attention qu'il mérite."], "explanation": "Même demande, avec une syntaxe recherchée et une tournure élégante."},
             ]},
        ],
        "summary": [
            "Les registres administratif, courant, littéraire et familier se distinguent par leur vocabulaire, leur syntaxe et leurs formules propres.",
            "Réécrire d'un registre à l'autre exige de conserver strictement le sens tout en transformant entièrement la forme.",
            "Le choix du registre approprié à chaque situation de communication est la marque ultime d'une maîtrise proche du natif.",
        ],
    },
]

EXTRA_EXERCISES = {
    "c2-la-syntaxe-complexe-et-la-subordination-multiple": [
        {"id": "c2synx-reading", "type": "reading-comprehension", "title": "Lecture : Un Dossier Contesté",
         "passage": "<p>Le dossier, que la commission qu'on avait spécialement nommée jugeait insuffisant, fut renvoyé pour révision. Ce que redoutaient ceux qui suivaient l'affaire depuis le début finit par arriver : les conclusions, qui avaient été rédigées à la hâte, sans que personne n'ait pu les vérifier sérieusement, furent largement contestées.</p>",
         "items": [
            {"id": "c2synxr1", "prompt": "Pourquoi le dossier fut-il renvoyé ?", "options": ["La commission le jugeait insuffisant", "Il était trop long", "Il avait été perdu"], "answerIndex": 0, "explanation": "Le texte le dit directement, via une relative enchâssée."},
            {"id": "c2synxr2", "prompt": "Qui avait nommé la commission ?", "options": ["Le texte ne le précise pas explicitement", "Le gouvernement", "Les journalistes"], "answerIndex": 0, "explanation": "Le texte dit seulement « qu'on avait spécialement nommée », sans préciser qui."},
            {"id": "c2synxr3", "prompt": "Comment les conclusions avaient-elles été rédigées ?", "options": ["À la hâte, sans vérification sérieuse", "Avec beaucoup de soin", "Par plusieurs experts indépendants"], "answerIndex": 0, "explanation": "Le texte le précise dans une incise enchâssée."},
            {"id": "c2synxr4", "prompt": "Que finit par arriver, selon le texte ?", "options": ["Ce que redoutaient ceux qui suivaient l'affaire", "Une bonne nouvelle inattendue", "Rien de particulier"], "answerIndex": 0, "explanation": "Le texte le dit dès la deuxième phrase."},
         ]},
        {"id": "c2synx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2synxo1", "prompt": "Remets les mots en ordre.", "words": ["Le", "dossier", "fut", "renvoyé", "pour", "révision"], "explanation": "Squelette simple : sujet, verbe, complément."},
            {"id": "c2synxo2", "prompt": "Remets les mots en ordre.", "words": ["Les", "conclusions", "furent", "largement", "contestées"], "explanation": "Structure passive, sujet-verbe-attribut."},
         ]},
    ],
    "c2-le-registre-litteraire-et-les-procedes-stylistiques": [
        {"id": "c2styx-reading", "type": "reading-comprehension", "title": "Lecture : Un Extrait Narratif",
         "passage": "<p>Il ouvrit la porte, hésita, puis entra. Le temps, ce voleur impitoyable, avait tout changé : les murs, autrefois blancs, autrefois vivants, autrefois pleins de voix, n'étaient plus que silence et poussière. Il eut soudain envie de partir, mais il resta.</p>",
         "items": [
            {"id": "c2styxr1", "prompt": "À quel temps le texte est-il principalement écrit ?", "options": ["Le passé simple", "Le présent", "L'imparfait seul"], "answerIndex": 0, "explanation": "« ouvrit, hésita, entra, eut, resta » sont des formes de passé simple."},
            {"id": "c2styxr2", "prompt": "Quel procédé illustre « le temps, ce voleur impitoyable » ?", "options": ["Une métaphore", "Une litote", "Une antithèse"], "answerIndex": 0, "explanation": "C'est une comparaison implicite, sans outil comparatif."},
            {"id": "c2styxr3", "prompt": "Quel procédé illustre la répétition de « autrefois » ?", "options": ["Une anaphore", "Un mot-valise", "Un calembour"], "answerIndex": 0, "explanation": "La répétition en tête de plusieurs segments crée un effet d'insistance."},
            {"id": "c2styxr4", "prompt": "Que fait le personnage à la fin de l'extrait ?", "options": ["Il reste, malgré son envie de partir", "Il part immédiatement", "Il s'endort"], "answerIndex": 0, "explanation": "Le texte se termine sur cette décision contradictoire avec son envie."},
         ]},
        {"id": "c2styx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2styxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "ouvrit", "la", "porte,", "hésita,", "puis", "entra"], "explanation": "Trois verbes au passé simple en succession, effet de gradation narrative."},
            {"id": "c2styxo2", "prompt": "Remets les mots en ordre.", "words": ["Le", "temps", "avait", "tout", "changé"], "explanation": "Structure simple sujet-verbe-complément, plus-que-parfait."},
         ]},
    ],
    "c2-les-nuances-lexicales-et-les-faux-amis-avances": [
        {"id": "c2famx-reading", "type": "reading-comprehension", "title": "Lecture : Un Malentendu de Traduction",
         "passage": "<p>Le traducteur avait écrit « actuellement » pour rendre « actually », créant un contresens complet. En fait, l'auteur voulait dire qu'il n'était pas du tout d'accord. De même, « éventuellement » avait remplacé « eventually », alors qu'il fallait écrire « finalement ». Ces erreurs, bien que minimes en apparence, changeaient totalement le sens du passage.</p>",
         "items": [
            {"id": "c2famxr1", "prompt": "Pourquoi y avait-il un contresens dans la traduction ?", "options": ["« Actuellement » a été confondu avec « actually »", "Le traducteur ne connaissait pas le français", "Le texte original était mal écrit"], "answerIndex": 0, "explanation": "Le texte l'explique directement en ouverture."},
            {"id": "c2famxr2", "prompt": "Que voulait réellement dire l'auteur, selon le texte ?", "options": ["Qu'il n'était pas du tout d'accord", "Qu'il était tout à fait d'accord", "Qu'il n'avait pas d'opinion"], "answerIndex": 0, "explanation": "Le texte le précise avec « en fait »."},
            {"id": "c2famxr3", "prompt": "Par quel mot fallait-il remplacer « éventuellement » ?", "options": ["Finalement", "Peut-être", "Immédiatement"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "c2famxr4", "prompt": "Comment le texte qualifie-t-il ces erreurs ?", "options": ["Minimes en apparence, mais changeant totalement le sens", "Sans aucune importance", "Impossibles à corriger"], "answerIndex": 0, "explanation": "Le texte se termine sur ce constat nuancé."},
         ]},
        {"id": "c2famx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2famxo1", "prompt": "Remets les mots en ordre.", "words": ["En", "fait,", "il", "n'était", "pas", "d'accord"], "explanation": "En fait traduit correctement actually, en tête de phrase."},
            {"id": "c2famxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "fallait", "écrire", "finalement,", "pas", "éventuellement"], "explanation": "Finalement traduit eventually ; éventuellement signifie autre chose."},
         ]},
    ],
    "c2-la-variation-regionale-du-francais": [
        {"id": "c2varx-reading", "type": "reading-comprehension", "title": "Lecture : Un Voyage Francophone",
         "passage": "<p>À Montréal, mon ami m'a dit d'aller magasiner avant que le dépanneur ne ferme. À Bruxelles, on m'a proposé septante euros pour la chambre, et on m'a prêté un essuie pour la douche. À Dakar, un jeune m'a présenté sa « go » avant de m'inviter à l'essencerie du coin.</p>",
         "items": [
            {"id": "c2varxr1", "prompt": "Que signifie « magasiner » dans ce contexte montréalais ?", "options": ["Faire du shopping", "Ranger des affaires", "Chercher un magasin fermé"], "answerIndex": 0, "explanation": "C'est le sens québécois courant de ce verbe."},
            {"id": "c2varxr2", "prompt": "Combien d'euros a-t-on proposé à Bruxelles ?", "options": ["Septante, soit soixante-dix", "Soixante-dix-sept", "Dix-sept"], "answerIndex": 0, "explanation": "Septante est le mot belge et suisse pour 70."},
            {"id": "c2varxr3", "prompt": "Que lui a-t-on prêté pour la douche à Bruxelles ?", "options": ["Un essuie, c'est-à-dire une serviette", "Un chandail", "Une farde"], "answerIndex": 0, "explanation": "Essuie est le belgicisme pour serviette."},
            {"id": "c2varxr4", "prompt": "Que signifie « go » dans le contexte dakarois du texte ?", "options": ["Une jeune fille (argot local)", "Une voiture", "Un plat traditionnel"], "answerIndex": 0, "explanation": "C'est un régionalisme ouest-africain pour désigner une jeune fille."},
         ]},
        {"id": "c2varx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2varxo1", "prompt": "Remets les mots en ordre.", "words": ["Va", "magasiner", "avant", "que", "le", "dépanneur", "ferme"], "explanation": "Vocabulaire québécois courant."},
            {"id": "c2varxo2", "prompt": "Remets les mots en ordre.", "words": ["On", "m'a", "proposé", "septante", "euros"], "explanation": "Nombre belge/suisse pour 70."},
         ]},
    ],
    "c2-lironie-limplicite-et-les-sous-entendus": [
        {"id": "c2irox-reading", "type": "reading-comprehension", "title": "Lecture : Une Réunion Tendue",
         "passage": "<p>« Quelle présentation extraordinaire », lança-t-il, alors que la salle entière avait somnolé pendant une heure. « Ce n'est pas inintéressant », ajouta sa collègue, du bout des lèvres. Plus tard, le directeur glissa : « Il serait peut-être temps de repenser notre approche pour la prochaine fois. » Personne n'osa répondre directement, mais tout le monde avait compris.</p>",
         "items": [
            {"id": "c2iroxr1", "prompt": "Que suggère la phrase « Quelle présentation extraordinaire » ?", "options": ["Le contraire, par ironie : la présentation était ennuyeuse", "Que la présentation était vraiment excellente", "Que personne n'a d'avis"], "answerIndex": 0, "explanation": "Le contexte (la salle qui somnole) contredit l'énoncé, signalant l'ironie."},
            {"id": "c2iroxr2", "prompt": "Que signifie « ce n'est pas inintéressant » dans ce contexte ?", "options": ["C'était plutôt ennuyeux, dit par litote polie", "C'était passionnant", "La collègue n'a pas d'opinion"], "answerIndex": 0, "explanation": "La double négation atténuée suggère un jugement plutôt négatif."},
            {"id": "c2iroxr3", "prompt": "Que sous-entend le directeur avec sa remarque sur « repenser notre approche » ?", "options": ["Que la présentation n'a pas convaincu et doit changer", "Qu'il faut refaire exactement la même chose", "Qu'il n'y aura pas de prochaine fois"], "answerIndex": 0, "explanation": "C'est un sous-entendu poli critiquant indirectement la présentation."},
            {"id": "c2iroxr4", "prompt": "Comment réagit la salle à cette remarque ?", "options": ["Personne ne répond directement, mais tous comprennent", "Tout le monde proteste vivement", "Personne n'a rien compris"], "answerIndex": 0, "explanation": "Le texte le dit dans sa dernière phrase."},
         ]},
        {"id": "c2irox-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2iroxo1", "prompt": "Remets les mots en ordre.", "words": ["Quelle", "présentation", "extraordinaire,", "lança-t-il"], "explanation": "Antiphrase ironique, dite avec un ton contraire au sens littéral."},
            {"id": "c2iroxo2", "prompt": "Remets les mots en ordre.", "words": ["Ce", "n'est", "pas", "inintéressant,", "ajouta-t-elle"], "explanation": "Litote polie atténuant une critique."},
         ]},
    ],
    "c2-lattenuation-et-la-diplomatie-dans-le-discours": [
        {"id": "c2attx-reading", "type": "reading-comprehension", "title": "Lecture : Un Courriel Diplomatique",
         "passage": "<p>Il me semblerait préférable de revoir certains passages de votre rapport avant sa publication. Il conviendrait notamment de clarifier la partie consacrée aux résultats, qui reste, dans une certaine mesure, perfectible. Auriez-vous l'obligeance d'y apporter ces quelques ajustements avant la fin de la semaine ?</p>",
         "items": [
            {"id": "c2attxr1", "prompt": "Que suggère l'auteur du courriel concernant le rapport ?", "options": ["De revoir certains passages avant publication", "De ne rien changer", "De le supprimer entièrement"], "answerIndex": 0, "explanation": "Le texte le dit directement, avec une formule atténuée."},
            {"id": "c2attxr2", "prompt": "Quelle partie du rapport est jugée perfectible ?", "options": ["La partie consacrée aux résultats", "L'introduction", "La bibliographie"], "answerIndex": 0, "explanation": "Le texte le précise directement."},
            {"id": "c2attxr3", "prompt": "Que signifie « perfectible » dans ce contexte ?", "options": ["Qui pourrait être amélioré (euphémisme pour imparfait)", "Absolument excellent", "Totalement inutilisable"], "answerIndex": 0, "explanation": "C'est un euphémisme diplomatique pour dire que le texte a des défauts."},
            {"id": "c2attxr4", "prompt": "Que demande finalement l'auteur ?", "options": ["D'apporter des ajustements avant la fin de la semaine", "De ne jamais republier ce rapport", "De changer complètement de sujet"], "answerIndex": 0, "explanation": "Le texte se termine sur cette demande formulée poliment."},
         ]},
        {"id": "c2attx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2attxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "conviendrait", "de", "clarifier", "cette", "partie"], "explanation": "Formule impersonnelle diplomatique."},
            {"id": "c2attxo2", "prompt": "Remets les mots en ordre.", "words": ["Cette", "partie", "reste", "perfectible"], "explanation": "Euphémisme atténuant une critique."},
         ]},
    ],
    "c2-les-expressions-idiomatiques-avancees": [
        {"id": "c2idix-reading", "type": "reading-comprehension", "title": "Lecture : Une Soirée Ratée",
         "passage": "<p>Elle avait le cafard depuis une semaine, et ce soir-là n'arrangeait rien : son ami lui avait posé un lapin sans même s'excuser. Sur des charbons ardents toute la soirée, elle finit par appeler sa sœur pour lui tirer les vers du nez sur ce qui s'était vraiment passé. Elle comprit alors qu'il avait, comme toujours, mis la charrue avant les bœufs.</p>",
         "items": [
            {"id": "c2idixr1", "prompt": "Comment se sentait-elle depuis une semaine ?", "options": ["Triste, elle avait le cafard", "Très heureuse", "En colère"], "answerIndex": 0, "explanation": "Le texte le dit directement en ouverture."},
            {"id": "c2idixr2", "prompt": "Qu'a fait son ami ce soir-là ?", "options": ["Il lui a posé un lapin, sans venir au rendez-vous", "Il est venu en avance", "Il lui a offert un cadeau"], "answerIndex": 0, "explanation": "Le texte le précise directement."},
            {"id": "c2idixr3", "prompt": "Que fait-elle pour comprendre la situation ?", "options": ["Elle tire les vers du nez à sa sœur", "Elle appelle la police", "Elle part en voyage"], "answerIndex": 0, "explanation": "Elle cherche à faire parler sa sœur indirectement."},
            {"id": "c2idixr4", "prompt": "Que comprend-elle finalement à propos de son ami ?", "options": ["Qu'il a agi dans le mauvais ordre, comme toujours", "Qu'il est très organisé", "Qu'il n'a rien fait de mal"], "answerIndex": 0, "explanation": "Le texte se termine sur cette conclusion, avec l'expression mettre la charrue avant les bœufs."},
         ]},
        {"id": "c2idix-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2idixo1", "prompt": "Remets les mots en ordre.", "words": ["Elle", "avait", "le", "cafard", "depuis", "une", "semaine"], "explanation": "Avoir le cafard = être triste."},
            {"id": "c2idixo2", "prompt": "Remets les mots en ordre.", "words": ["Son", "ami", "lui", "avait", "posé", "un", "lapin"], "explanation": "Poser un lapin = ne pas venir à un rendez-vous."},
         ]},
    ],
    "c2-lanalyse-et-la-synthese-de-documents-complexes": [
        {"id": "c2anax-reading", "type": "reading-comprehension", "title": "Lecture : Un Extrait d'Essai",
         "passage": "<p>L'auteur défend l'idée que la technologie ne remplace jamais totalement l'interaction humaine directe. Il s'appuie d'abord sur une étude menée en 2020 auprès de lycéens, qu'il ne présente que comme une illustration parmi d'autres. Son raisonnement repose sur un présupposé rarement questionné : que tous les élèves disposent d'un accès égal aux outils numériques. Il conclut que la technologie doit compléter, et non remplacer, l'enseignement traditionnel.</p>",
         "items": [
            {"id": "c2anaxr1", "prompt": "Quelle est la thèse défendue par l'auteur ?", "options": ["La technologie ne remplace jamais totalement l'interaction humaine directe", "La technologie doit remplacer complètement l'enseignement traditionnel", "Les lycéens n'apprennent rien avec la technologie"], "answerIndex": 0, "explanation": "Le texte l'énonce dès la première phrase."},
            {"id": "c2anaxr2", "prompt": "Comment l'étude de 2020 est-elle utilisée dans le texte ?", "options": ["Comme une simple illustration parmi d'autres", "Comme l'unique preuve de la thèse", "Elle n'est pas mentionnée"], "answerIndex": 0, "explanation": "Le texte précise que ce n'est qu'un exemple, pas l'argument central."},
            {"id": "c2anaxr3", "prompt": "Quel présupposé implicite repère le texte dans le raisonnement de l'auteur ?", "options": ["Que tous les élèves ont un accès égal aux outils numériques", "Que la technologie coûte cher", "Que les lycéens n'aiment pas la technologie"], "answerIndex": 0, "explanation": "Le texte le signale explicitement comme un présupposé rarement questionné."},
            {"id": "c2anaxr4", "prompt": "Quelle est la conclusion de l'auteur ?", "options": ["La technologie doit compléter, non remplacer, l'enseignement traditionnel", "Il faut supprimer toute technologie des écoles", "Le sujet ne mérite pas d'être étudié"], "answerIndex": 0, "explanation": "Le texte se termine sur cette conclusion nuancée."},
         ]},
        {"id": "c2anax-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2anaxo1", "prompt": "Remets les mots en ordre.", "words": ["La", "technologie", "doit", "compléter", "l'enseignement"], "explanation": "Thèse condensée en une phrase simple."},
            {"id": "c2anaxo2", "prompt": "Remets les mots en ordre.", "words": ["Ce", "présupposé", "est", "rarement", "questionné"], "explanation": "Phrase simple sur le présupposé implicite du texte."},
         ]},
    ],
    "c2-la-creativite-lexicale-neologismes-et-jeux-de-mots": [
        {"id": "c2neox-reading", "type": "reading-comprehension", "title": "Lecture : Le Langage de Demain",
         "passage": "<p>Avec la généralisation du télétravail, de nouveaux mots hyperconnectés sont apparus : on parle désormais de « zoomer » une réunion ou d'être « visio-fatigué ». Certains dénoncent l'infox qui circule sur ces sujets, tandis que d'autres plaisantent : « Le télétravailleur, lui, ne travaille pas à l'œil ! », jouant sur la double lecture de cette expression.</p>",
         "items": [
            {"id": "c2neoxr1", "prompt": "Quel phénomène a favorisé l'apparition de nouveaux mots, selon le texte ?", "options": ["La généralisation du télétravail", "Une réforme de l'orthographe", "L'apparition d'une nouvelle langue"], "answerIndex": 0, "explanation": "Le texte le dit directement en ouverture."},
            {"id": "c2neoxr2", "prompt": "Que dénoncent certains, selon le texte ?", "options": ["L'infox qui circule sur ces sujets", "Le prix des ordinateurs", "L'absence de télétravail"], "answerIndex": 0, "explanation": "Le texte le précise directement."},
            {"id": "c2neoxr3", "prompt": "Sur quoi joue la plaisanterie finale du texte ?", "options": ["Une double lecture possible de l'expression", "Une simple erreur de frappe", "Un mot totalement inventé sans logique"], "answerIndex": 0, "explanation": "Le texte le signale explicitement comme un jeu de mots."},
            {"id": "c2neoxr4", "prompt": "Que signifie « visio-fatigué », d'après sa formation ?", "options": ["Fatigué par les visioconférences (néologisme par composition)", "Qui n'aime pas la vidéo", "Qui travaille de nuit"], "answerIndex": 0, "explanation": "C'est un néologisme composé, formé sur le modèle de préfixation/composition du texte."},
         ]},
        {"id": "c2neox-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2neoxo1", "prompt": "Remets les mots en ordre.", "words": ["De", "nouveaux", "mots", "hyperconnectés", "sont", "apparus"], "explanation": "Néologisme formé par préfixation (hyper-)."},
            {"id": "c2neoxo2", "prompt": "Remets les mots en ordre.", "words": ["L'infox", "circule", "beaucoup", "sur", "internet"], "explanation": "Mot-valise (information + intox) en position sujet."},
         ]},
    ],
    "c2-la-reecriture-stylistique-et-ladaptation-de-registre": [
        {"id": "c2reex-reading", "type": "reading-comprehension", "title": "Lecture : Trois Réponses à un Même Message",
         "passage": "<p>Le professeur a annoncé un contrôle surprise. Un élève très formel a écrit à ses parents : « Je vous informe qu'un contrôle surprise a été annoncé ce jour. » Un autre a texté un ami : « Grosse interro surprise, la loose ! » Un troisième, plus poétique, a noté dans son journal : « Ainsi tomba sur nous, tel un couperet, l'annonce redoutée. »</p>",
         "items": [
            {"id": "c2reexr1", "prompt": "Quel événement les trois élèves rapportent-ils ?", "options": ["L'annonce d'un contrôle surprise", "Une sortie scolaire", "Un changement d'emploi du temps"], "answerIndex": 0, "explanation": "Le texte le dit en ouverture."},
            {"id": "c2reexr2", "prompt": "Quel registre utilise l'élève qui écrit à ses parents ?", "options": ["Courant à soutenu, formel", "Familier", "Littéraire"], "answerIndex": 0, "explanation": "« Je vous informe que » est une formule neutre et formelle."},
            {"id": "c2reexr3", "prompt": "Quel registre utilise l'élève qui texte son ami ?", "options": ["Familier", "Administratif", "Littéraire"], "answerIndex": 0, "explanation": "Le vocabulaire relâché (« la loose ») signale le registre familier."},
            {"id": "c2reexr4", "prompt": "Quel procédé emploie le troisième élève dans son journal ?", "options": ["Une métaphore littéraire (le couperet)", "Un néologisme", "Un régionalisme"], "answerIndex": 0, "explanation": "« Tel un couperet » est une comparaison à visée littéraire, dans un registre soigné."},
         ]},
        {"id": "c2reex-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c2reexo1", "prompt": "Remets les mots en ordre.", "words": ["Je", "vous", "informe", "qu'un", "contrôle", "aura", "lieu"], "explanation": "Registre formel/administratif, structure impersonnelle."},
            {"id": "c2reexo2", "prompt": "Remets les mots en ordre.", "words": ["Ainsi", "tomba", "sur", "nous", "l'annonce", "redoutée"], "explanation": "Registre littéraire, inversion stylistique après ainsi."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
