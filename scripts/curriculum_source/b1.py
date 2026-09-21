# -*- coding: utf-8 -*-
"""B1 — Données du curriculum de niveau intermédiaire. Voir curriculum/SCHEMA.md
pour la forme exacte du JSON vers lequel ceci est compilé (scripts/generate_curriculum.py
fait la compilation). Écrit en Python plutôt qu'en JSON à la main pour que le
HTML en ligne (rules[].body, content.explanation) et les guillemets dans le
texte puissent s'écrire naturellement."""

OVERVIEW = (
    "Le niveau B1 approfondit les nuances du passé avec le plus-que-parfait et "
    "le conditionnel passé, puis fait le grand saut vers le subjonctif présent "
    "— le mode du doute, de la volonté et de l'émotion — et sa confrontation "
    "avec l'indicatif. Tu apprendras aussi à rapporter les paroles de "
    "quelqu'un au discours indirect, à utiliser les pronoms relatifs (qui, "
    "que, où, dont), la voix passive, les principaux connecteurs logiques, le "
    "gérondif et le participe présent, les doubles pronoms, l'expression de "
    "l'hypothèse avec si, et les verbes suivis de à ou de devant un "
    "infinitif. À la fin de ce niveau, tu pourras utiliser le français de "
    "façon plus autonome, nuancer tes propos, raconter et rapporter des "
    "événements complexes, et construire des phrases beaucoup plus proches "
    "de celles d'un locuteur natif."
)

LESSONS = [
    {
        "id": "b1-le-plus-que-parfait",
        "level": "B1", "unit": "1", "order": 1, "skill": "grammar", "strand": "plus-que-parfait",
        "title": "Le Plus-que-parfait",
        "subtitle": "Comment former le plus-que-parfait, pour exprimer une action antérieure à une autre action passée.",
        "objectives": [
            "Former le plus-que-parfait avec l'imparfait de avoir ou être + participe passé.",
            "Employer le plus-que-parfait pour exprimer une action antérieure à un autre fait du passé.",
            "Distinguer le plus-que-parfait du passé composé et de l'imparfait dans un récit.",
        ],
        "content": {
            "intro": "Quand tu racontes une histoire au passé et que tu dois mentionner un événement encore plus ancien, le français utilise un temps supplémentaire : le plus-que-parfait — « le passé du passé ».",
            "explanation": "<p>Le plus-que-parfait se forme avec l'<strong>imparfait</strong> de <em>avoir</em> ou <em>être</em> + le participe passé, avec exactement les mêmes règles de choix d'auxiliaire et d'accord que pour le passé composé : <em>j'avais mangé, elle était partie, ils s'étaient levés</em>.</p><p>Il s'utilise pour une action terminée <strong>avant</strong> un autre moment du passé déjà exprimé au passé composé ou à l'imparfait : <em>Quand je suis arrivé, le film avait déjà commencé</em> — l'arrivée (passé composé) et le début du film (plus-que-parfait, antérieur) sont deux moments distincts.</p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>Imparfait de avoir/être + participe passé : <em>j'avais parlé, tu étais parti(e), nous avions fini</em>.</li></ul>"},
                {"heading": "b) Même auxiliaire, même accord", "body": "<ul><li>Le même choix d'auxiliaire et le même accord qu'au passé composé s'appliquent au plus-que-parfait.</li></ul>"},
                {"heading": "c) Emploi", "body": "<ul><li>Exprime une action antérieure à un autre fait passé : <em>Quand elle est arrivée, nous avions déjà mangé.</em></li></ul>"},
                {"heading": "d) Repères fréquents", "body": "<ul><li>Souvent introduit par <em>déjà, ne…pas encore, quand</em>.</li></ul>"},
            ],
            "examples": [
                "Quand je suis arrivé, le film avait déjà commencé.",
                "Elle avait fini ses devoirs avant de sortir.",
                "Nous étions partis quand tu as téléphoné.",
                "Il n'avait jamais vu la mer avant ce voyage.",
                "Ils s'étaient couchés tôt la veille.",
                "Tu avais déjà mangé quand je suis rentré.",
                "Elle n'avait pas encore fini quand nous sommes arrivés.",
            ],
            "commonMistakes": [
                {"wrong": "Quand je suis arrivé, le film a déjà commencé.", "right": "Quand je suis arrivé, le film avait déjà commencé.", "why": "L'action antérieure à un autre fait passé (le début du film) se met au plus-que-parfait, pas au passé composé."},
                {"wrong": "Elle avait finit ses devoirs.", "right": "Elle avait fini ses devoirs.", "why": "Le participe passé de finir est fini, sans t final."},
                {"wrong": "Ils s'avaient couchés tôt.", "right": "Ils s'étaient couchés tôt.", "why": "Les verbes pronominaux se conjuguent toujours avec être, jamais avoir, même au plus-que-parfait."},
            ],
        },
        "exercises": [
            {"id": "b1pqp-fill", "type": "fill-blank", "title": "Conjugue au Plus-que-parfait",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b1pqpf1", "prompt": "Quand nous sommes arrivés, le train ___ (partir) déjà.", "answers": [["était parti"]], "options": ["était parti", "avait parti", "est parti"], "explanation": "Partir se conjugue avec être ; plus-que-parfait : était parti."},
                {"id": "b1pqpf2", "prompt": "Elle ___ (finir) son repas avant notre arrivée.", "answers": [["avait fini"]], "options": ["avait fini", "était finie", "a fini"], "explanation": "Finir se conjugue avec avoir : avait fini."},
                {"id": "b1pqpf3", "prompt": "Je ne ___ (voir) jamais cette ville avant ce voyage.", "answers": [["avais vu"]], "options": ["avais vu", "ai vu", "étais vu"], "explanation": "Voir se conjugue avec avoir au plus-que-parfait."},
                {"id": "b1pqpf4", "prompt": "Ils ___ (se lever) tôt ce matin-là.", "answers": [["s'étaient levés"]], "options": ["s'étaient levés", "s'avaient levés", "se sont levés"], "explanation": "Les verbes pronominaux se conjuguent toujours avec être."},
             ]},
            {"id": "b1pqp-mc", "type": "multiple-choice", "title": "Le Plus-que-parfait",
             "items": [
                {"id": "b1pqpm1", "prompt": "Comment forme-t-on le plus-que-parfait ?", "options": ["imparfait de avoir/être + participe passé", "présent de avoir/être + participe passé", "futur de avoir/être + participe passé"], "answerIndex": 0, "explanation": "L'auxiliaire est à l'imparfait, pas au présent ni au futur."},
                {"id": "b1pqpm2", "prompt": "À quoi sert le plus-que-parfait ?", "options": ["exprimer une action antérieure à un autre fait passé", "décrire une habitude présente", "annoncer un projet futur"], "answerIndex": 0, "explanation": "Il marque toujours l'action la plus ancienne de deux faits passés."},
                {"id": "b1pqpm3", "prompt": "Quel auxiliaire utilise un verbe pronominal au plus-que-parfait ?", "options": ["être, toujours", "avoir, toujours", "cela dépend du sujet"], "answerIndex": 0, "explanation": "Les verbes pronominaux se conjuguent toujours avec être."},
                {"id": "b1pqpm4", "prompt": "Dans « Quand je suis arrivé, le film avait déjà commencé », quelle action est la plus ancienne ?", "options": ["le début du film", "mon arrivée", "aucune des deux"], "answerIndex": 0, "explanation": "Le plus-que-parfait marque toujours l'action la plus ancienne des deux."},
             ]},
            {"id": "b1pqp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1pqpc1", "incorrect": "Quand je suis arrivé, le film a déjà commencé.", "answer": ["Quand je suis arrivé, le film avait déjà commencé."], "explanation": "L'action antérieure se met au plus-que-parfait."},
                {"id": "b1pqpc2", "incorrect": "Elle avait finit ses devoirs.", "answer": ["Elle avait fini ses devoirs."], "explanation": "Le participe passé de finir est fini, sans t."},
                {"id": "b1pqpc3", "incorrect": "Ils s'avaient couchés tôt.", "answer": ["Ils s'étaient couchés tôt."], "explanation": "Les pronominaux se conjuguent toujours avec être."},
             ]},
        ],
        "summary": [
            "Le plus-que-parfait se forme avec l'imparfait de avoir/être + participe passé, avec les mêmes règles d'auxiliaire et d'accord que le passé composé.",
            "Il exprime une action terminée avant un autre moment du passé déjà exprimé au passé composé ou à l'imparfait.",
            "Les verbes pronominaux se conjuguent toujours avec être, même au plus-que-parfait.",
        ],
    },
    {
        "id": "b1-le-conditionnel-passe",
        "level": "B1", "unit": "1", "order": 2, "skill": "grammar", "strand": "conditionnel-passe",
        "title": "Le Conditionnel Passé",
        "subtitle": "Comment former le conditionnel passé, pour exprimer un regret ou une hypothèse non réalisée dans le passé.",
        "objectives": [
            "Former le conditionnel passé avec le conditionnel présent de avoir/être + participe passé.",
            "Exprimer un regret avec j'aurais dû / je n'aurais pas dû + infinitif.",
            "Distinguer le conditionnel passé du plus-que-parfait par leur sens.",
        ],
        "content": {
            "intro": "Le conditionnel passé sert à parler de ce qui aurait pu se passer mais qui ne s'est pas produit — le regret, le reproche, l'hypothèse manquée.",
            "explanation": "<p>Le conditionnel passé se forme avec le <strong>conditionnel présent</strong> de <em>avoir</em> ou <em>être</em> + le participe passé, avec les mêmes règles d'auxiliaire et d'accord que le passé composé : <em>j'aurais aimé, elle serait partie, nous nous serions levés</em>.</p><p>Il exprime un regret ou un reproche à propos du passé (<em>j'aurais dû l'appeler</em>), une action qui aurait eu lieu sous une condition non réalisée (<em>si j'avais su, je serais venu</em>), ou une information non confirmée dans un contexte journalistique.</p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>Conditionnel présent de avoir/être + participe passé.</li></ul>"},
                {"heading": "b) Regret ou reproche", "body": "<ul><li><em>j'aurais dû</em> + infinitif — regret d'une action non faite.</li><li><em>je n'aurais pas dû</em> + infinitif — regret d'une action faite.</li></ul>"},
                {"heading": "c) Hypothèse non réalisée", "body": "<ul><li><em>si</em> + plus-que-parfait, conditionnel passé — <em>Si j'avais su, je serais venu.</em></li></ul>"},
                {"heading": "d) Information non confirmée", "body": "<ul><li>Style journalistique : <em>Le président aurait démissionné</em> (information non confirmée).</li></ul>"},
            ],
            "examples": [
                "J'aurais dû t'appeler hier soir.",
                "Elle ne serait pas venue si elle avait su.",
                "Si j'avais su, je serais venu plus tôt.",
                "Nous aurions aimé visiter ce musée.",
                "Ils se seraient perdus sans le plan.",
                "Tu n'aurais pas dû dire ça.",
                "Le vol aurait été annulé, selon la radio.",
            ],
            "commonMistakes": [
                {"wrong": "J'aurais du t'appeler.", "right": "J'aurais dû t'appeler.", "why": "Dû prend un accent circonflexe pour se distinguer de du (article/préposition contractée)."},
                {"wrong": "Si j'avais su, je viendrais.", "right": "Si j'avais su, je serais venu.", "why": "Après si + plus-que-parfait, on utilise le conditionnel passé, pas le conditionnel présent."},
                {"wrong": "Elle aurait partie plus tôt.", "right": "Elle serait partie plus tôt.", "why": "Partir se conjugue avec être, même au conditionnel passé."},
            ],
        },
        "exercises": [
            {"id": "b1cpa-fill", "type": "fill-blank", "title": "Conjugue au Conditionnel Passé",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b1cpaf1", "prompt": "Je ___ (devoir) t'appeler hier soir.", "answers": [["aurais dû"]], "options": ["aurais dû", "avais dû", "aurai dû"], "explanation": "Regret : j'aurais dû + infinitif."},
                {"id": "b1cpaf2", "prompt": "Si j'avais su, je ___ (venir) plus tôt.", "answers": [["serais venu"]], "options": ["serais venu", "aurais venu", "viendrais"], "explanation": "Venir se conjugue avec être."},
                {"id": "b1cpaf3", "prompt": "Nous ___ (aimer) visiter ce musée.", "answers": [["aurions aimé"]], "options": ["aurions aimé", "aurions aimer", "avions aimé"], "explanation": "Conditionnel présent de avoir + participe passé."},
                {"id": "b1cpaf4", "prompt": "Ils ___ (se perdre) sans le plan.", "answers": [["se seraient perdus"]], "options": ["se seraient perdus", "se auraient perdus", "s'étaient perdus"], "explanation": "Pronominal → toujours être."},
             ]},
            {"id": "b1cpa-mc", "type": "multiple-choice", "title": "Le Conditionnel Passé",
             "items": [
                {"id": "b1cpam1", "prompt": "Comment forme-t-on le conditionnel passé ?", "options": ["conditionnel présent de avoir/être + participe passé", "imparfait de avoir/être + participe passé", "présent de avoir/être + participe passé"], "answerIndex": 0, "explanation": "L'auxiliaire est au conditionnel présent."},
                {"id": "b1cpam2", "prompt": "Que signifie « j'aurais dû l'appeler » ?", "options": ["un regret de ne pas l'avoir fait", "une obligation présente", "une prédiction future"], "answerIndex": 0, "explanation": "C'est l'expression classique du regret au passé."},
                {"id": "b1cpam3", "prompt": "Après si + plus-que-parfait, quel temps utilise-t-on dans la principale ?", "options": ["le conditionnel passé", "le conditionnel présent", "le futur simple"], "answerIndex": 0, "explanation": "L'hypothèse manquée dans le passé demande le conditionnel passé."},
                {"id": "b1cpam4", "prompt": "Pourquoi dû prend-il un accent circonflexe ?", "options": ["pour se distinguer de du", "c'est une règle sans raison", "pour marquer le pluriel"], "answerIndex": 0, "explanation": "L'accent distingue le participe passé dû de l'article/préposition contractée du."},
             ]},
            {"id": "b1cpa-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1cpac1", "incorrect": "J'aurais du t'appeler.", "answer": ["J'aurais dû t'appeler."], "explanation": "Dû prend un accent circonflexe."},
                {"id": "b1cpac2", "incorrect": "Si j'avais su, je viendrais.", "answer": ["Si j'avais su, je serais venu."], "explanation": "Après si + plus-que-parfait : conditionnel passé."},
                {"id": "b1cpac3", "incorrect": "Elle aurait partie plus tôt.", "answer": ["Elle serait partie plus tôt."], "explanation": "Partir se conjugue avec être."},
             ]},
        ],
        "summary": [
            "Le conditionnel passé se forme avec le conditionnel présent de avoir/être + participe passé.",
            "Il exprime un regret (j'aurais dû), un reproche, ou une hypothèse non réalisée après si + plus-que-parfait.",
            "On le trouve aussi à l'écrit journalistique pour une information non confirmée.",
        ],
    },
    {
        "id": "b1-le-subjonctif-present-formation",
        "level": "B1", "unit": "1", "order": 3, "skill": "grammar", "strand": "subjonctif-formation",
        "title": "Le Subjonctif Présent — Formation et Déclencheurs de Base",
        "subtitle": "Comment former le subjonctif présent, et les expressions de base qui l'imposent après que.",
        "objectives": [
            "Former le subjonctif présent régulier à partir du radical de ils au présent.",
            "Conjuguer les subjonctifs irréguliers les plus fréquents (être, avoir, aller, faire, pouvoir, vouloir, savoir).",
            "Reconnaître les déclencheurs de base qui imposent le subjonctif (il faut que, vouloir que, souhaiter que).",
        ],
        "content": {
            "intro": "Le subjonctif est le mode qui exprime ce qui n'est pas un fait certain — une volonté, une obligation, un souhait — et il commence toujours après que.",
            "explanation": "<p>Pour la majorité des verbes, le subjonctif présent se forme à partir du radical de la 3ᵉ personne du pluriel (<em>ils</em>) au présent de l'indicatif, en retirant <em>-ent</em>, puis en ajoutant les terminaisons <strong>-e, -es, -e, -ions, -iez, -ent</strong> : <em>ils parlent → que je parle</em> ; <em>ils finissent → que je finisse</em>.</p><p>Certains verbes très fréquents ont un subjonctif irrégulier à mémoriser : <em>être → que je sois, avoir → que j'aie, aller → que j'aille, faire → que je fasse, pouvoir → que je puisse, vouloir → que je veuille, savoir → que je sache</em>. Le subjonctif s'emploie après <em>que</em>, déclenché par des expressions d'obligation (<em>il faut que</em>) ou de volonté (<em>je veux que, je souhaite que</em>).</p>",
            "rules": [
                {"heading": "a) Formation régulière", "body": "<ul><li>Radical de ils au présent (sans -ent) + -e/-es/-e/-ions/-iez/-ent.</li></ul>"},
                {"heading": "b) Irréguliers fréquents", "body": "<ul><li><em>être → sois, avoir → aie, aller → aille, faire → fasse</em>.</li><li><em>pouvoir → puisse, vouloir → veuille, savoir → sache</em>.</li></ul>"},
                {"heading": "c) Déclencheurs de base", "body": "<ul><li><em>il faut que, il est nécessaire que, vouloir que, souhaiter que, aimer que</em>.</li></ul>"},
                {"heading": "d) Toujours après que", "body": "<ul><li>Le subjonctif n'est jamais employé seul, sans que.</li></ul>"},
            ],
            "examples": [
                "Il faut que tu finisses ce travail aujourd'hui.",
                "Je veux que vous soyez à l'heure.",
                "Elle souhaite que nous fassions attention.",
                "Il faut que j'aille chez le médecin.",
                "Mes parents veulent que je sache nager.",
                "Il est nécessaire que tu aies ton passeport.",
                "Nous voulons que vous puissiez venir.",
            ],
            "commonMistakes": [
                {"wrong": "Il faut que tu finis ce travail.", "right": "Il faut que tu finisses ce travail.", "why": "Après il faut que, on utilise le subjonctif, pas l'indicatif."},
                {"wrong": "Je veux que tu es content.", "right": "Je veux que tu sois content.", "why": "Être a un subjonctif irrégulier : que tu sois."},
                {"wrong": "Il faut que je vais au marché.", "right": "Il faut que j'aille au marché.", "why": "Aller a un subjonctif irrégulier : que j'aille, pas la forme de l'indicatif."},
            ],
        },
        "exercises": [
            {"id": "b1sbf-fill", "type": "fill-blank", "title": "Conjugue au Subjonctif Présent",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b1sbff1", "prompt": "Il faut que tu ___ (finir) ce travail.", "answers": [["finisses"]], "options": ["finisses", "finis", "finiras"], "explanation": "Il faut que impose le subjonctif : que tu finisses."},
                {"id": "b1sbff2", "prompt": "Je veux que vous ___ (être) à l'heure.", "answers": [["soyez"]], "options": ["soyez", "êtes", "serez"], "explanation": "Être a un subjonctif irrégulier : que vous soyez."},
                {"id": "b1sbff3", "prompt": "Il faut que j'___ (aller) chez le médecin.", "answers": [["aille"]], "options": ["aille", "vais", "irai"], "explanation": "Aller a un subjonctif irrégulier : que j'aille."},
                {"id": "b1sbff4", "prompt": "Mes parents veulent que je ___ (savoir) nager.", "answers": [["sache"]], "options": ["sache", "sais", "saurai"], "explanation": "Savoir a un subjonctif irrégulier : que je sache."},
             ]},
            {"id": "b1sbf-mc", "type": "multiple-choice", "title": "Le Subjonctif Présent",
             "items": [
                {"id": "b1sbfm1", "prompt": "À partir de quel radical forme-t-on le subjonctif présent régulier ?", "options": ["le radical de ils au présent", "l'infinitif", "le radical de je au présent"], "answerIndex": 0, "explanation": "On retire -ent du radical de ils au présent."},
                {"id": "b1sbfm2", "prompt": "Quel est le subjonctif de être pour je ?", "options": ["que je sois", "que je suis", "que je serai"], "answerIndex": 0, "explanation": "Être a un subjonctif irrégulier : que je sois."},
                {"id": "b1sbfm3", "prompt": "Quelle expression déclenche le subjonctif ?", "options": ["il faut que", "je pense que (affirmatif)", "je sais que"], "answerIndex": 0, "explanation": "Il faut que exprime une obligation, déclencheur classique du subjonctif."},
                {"id": "b1sbfm4", "prompt": "Le subjonctif peut-il s'employer sans que ?", "options": ["non, jamais", "oui, toujours", "seulement à l'écrit"], "answerIndex": 0, "explanation": "Le subjonctif est toujours introduit par que."},
             ]},
            {"id": "b1sbf-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1sbfc1", "incorrect": "Il faut que tu finis ce travail.", "answer": ["Il faut que tu finisses ce travail."], "explanation": "Il faut que impose le subjonctif."},
                {"id": "b1sbfc2", "incorrect": "Je veux que tu es content.", "answer": ["Je veux que tu sois content."], "explanation": "Être a un subjonctif irrégulier : sois."},
                {"id": "b1sbfc3", "incorrect": "Il faut que je vais au marché.", "answer": ["Il faut que j'aille au marché."], "explanation": "Aller a un subjonctif irrégulier : aille."},
             ]},
        ],
        "summary": [
            "Le subjonctif présent régulier se forme à partir du radical de ils au présent + -e/-es/-e/-ions/-iez/-ent.",
            "Des verbes fréquents ont un subjonctif irrégulier à mémoriser : être, avoir, aller, faire, pouvoir, vouloir, savoir.",
            "Il est déclenché par des expressions d'obligation ou de volonté suivies de que : il faut que, je veux que.",
        ],
    },
    {
        "id": "b1-subjonctif-vs-indicatif",
        "level": "B1", "unit": "1", "order": 4, "skill": "grammar", "strand": "subjonctif-indicatif",
        "title": "Subjonctif vs. Indicatif",
        "subtitle": "Quand utiliser le subjonctif (doute, émotion, volonté) et quand utiliser l'indicatif (certitude).",
        "objectives": [
            "Distinguer les expressions qui déclenchent l'indicatif de celles qui déclenchent le subjonctif.",
            "Employer le subjonctif après le doute, l'émotion et la volonté.",
            "Employer l'indicatif après la certitude et les verbes déclaratifs à la forme affirmative.",
        ],
        "content": {
            "intro": "Après que, le verbe qui suit peut être à l'indicatif ou au subjonctif selon le sens du verbe principal — un choix qui structure une grande partie de la grammaire avancée du français.",
            "explanation": "<p>On utilise l'<strong>indicatif</strong> après les verbes qui expriment la certitude ou une déclaration à la forme affirmative : <em>je pense que, je crois que, je sais que, il est certain que</em> + indicatif (<em>Je pense qu'il a raison</em>). Ces mêmes verbes, à la forme négative ou interrogative, basculent souvent au subjonctif, car la certitude disparaît : <em>Je ne pense pas qu'il ait raison.</em></p><p>On utilise le <strong>subjonctif</strong> après les verbes ou expressions de doute (<em>je doute que</em>), d'émotion (<em>je suis content que, j'ai peur que</em>) et de volonté (<em>je veux que</em>), parce qu'ils présentent l'action comme non certaine, souhaitée ou ressentie, jamais comme un fait objectif.</p>",
            "rules": [
                {"heading": "a) Indicatif", "body": "<ul><li>Certitude/déclaration affirmative : <em>je pense que, je sais que, il est vrai que</em> + indicatif.</li></ul>"},
                {"heading": "b) Subjonctif — doute", "body": "<ul><li><em>je doute que, il est possible que</em> + subjonctif.</li></ul>"},
                {"heading": "c) Subjonctif — émotion", "body": "<ul><li><em>je suis content que, j'ai peur que, c'est dommage que</em> + subjonctif.</li></ul>"},
                {"heading": "d) Attention", "body": "<ul><li>Penser/croire à la forme négative ou interrogative basculent souvent au subjonctif.</li></ul>"},
            ],
            "examples": [
                "Je pense qu'il a raison.",
                "Je ne pense pas qu'il ait raison.",
                "Je doute qu'elle vienne ce soir.",
                "Je suis content que tu sois là.",
                "Il est certain qu'elle réussira.",
                "Il est possible qu'il pleuve demain.",
                "J'ai peur que nous soyons en retard.",
            ],
            "commonMistakes": [
                {"wrong": "Je pense qu'il ait raison.", "right": "Je pense qu'il a raison.", "why": "Penser que à la forme affirmative exprime la certitude : indicatif, pas subjonctif."},
                {"wrong": "Je suis content que tu es là.", "right": "Je suis content que tu sois là.", "why": "Une émotion déclenche toujours le subjonctif."},
                {"wrong": "Il est certain qu'elle vienne.", "right": "Il est certain qu'elle viendra.", "why": "Il est certain que exprime une certitude : indicatif."},
            ],
        },
        "exercises": [
            {"id": "b1svi-fill", "type": "fill-blank", "title": "Subjonctif ou Indicatif ?",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b1svif1", "prompt": "Je pense qu'il ___ (avoir) raison.", "answers": [["a"]], "options": ["a", "ait", "aura"], "explanation": "Penser que affirmatif : indicatif."},
                {"id": "b1svif2", "prompt": "Je doute qu'elle ___ (venir) ce soir.", "answers": [["vienne"]], "options": ["vienne", "vient", "viendra"], "explanation": "Le doute déclenche le subjonctif."},
                {"id": "b1svif3", "prompt": "Je suis content que tu ___ (être) là.", "answers": [["sois"]], "options": ["sois", "es", "seras"], "explanation": "Une émotion déclenche le subjonctif."},
                {"id": "b1svif4", "prompt": "Il est certain qu'elle ___ (réussir).", "answers": [["réussira"]], "options": ["réussira", "réussisse", "réussit"], "explanation": "Il est certain que : indicatif (futur ici)."},
             ]},
            {"id": "b1svi-mc", "type": "multiple-choice", "title": "Subjonctif vs. Indicatif",
             "items": [
                {"id": "b1svim1", "prompt": "Quel mode suit « je pense que » à la forme affirmative ?", "options": ["l'indicatif", "le subjonctif", "l'impératif"], "answerIndex": 0, "explanation": "La certitude déclenche l'indicatif."},
                {"id": "b1svim2", "prompt": "Quel mode suit une expression d'émotion (je suis content que) ?", "options": ["le subjonctif", "l'indicatif", "le conditionnel"], "answerIndex": 0, "explanation": "L'émotion déclenche toujours le subjonctif."},
                {"id": "b1svim3", "prompt": "Que se passe-t-il souvent avec « je ne pense pas que » ?", "options": ["le verbe passe au subjonctif", "rien ne change", "le verbe passe à l'impératif"], "answerIndex": 0, "explanation": "La négation fait souvent disparaître la certitude."},
                {"id": "b1svim4", "prompt": "Quel mode suit « il est certain que » ?", "options": ["l'indicatif", "le subjonctif", "le futur uniquement"], "answerIndex": 0, "explanation": "La certitude déclenche l'indicatif."},
             ]},
            {"id": "b1svi-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1svic1", "incorrect": "Je pense qu'il ait raison.", "answer": ["Je pense qu'il a raison."], "explanation": "Penser que affirmatif : indicatif."},
                {"id": "b1svic2", "incorrect": "Je suis content que tu es là.", "answer": ["Je suis content que tu sois là."], "explanation": "L'émotion déclenche le subjonctif."},
                {"id": "b1svic3", "incorrect": "Il est certain qu'elle vienne.", "answer": ["Il est certain qu'elle viendra."], "explanation": "La certitude déclenche l'indicatif."},
             ]},
        ],
        "summary": [
            "L'indicatif suit les expressions de certitude et les verbes déclaratifs affirmatifs (je pense que, je sais que).",
            "Le subjonctif suit le doute, l'émotion et la volonté (je doute que, je suis content que, je veux que).",
            "À la forme négative ou interrogative, penser/croire basculent souvent vers le subjonctif.",
        ],
    },
    {
        "id": "b1-le-discours-indirect",
        "level": "B1", "unit": "1", "order": 5, "skill": "grammar", "strand": "discours-indirect",
        "title": "Le Discours Indirect",
        "subtitle": "Comment rapporter les paroles de quelqu'un, au présent et au passé, avec les changements de temps nécessaires.",
        "objectives": [
            "Transformer une phrase au discours direct en discours indirect au présent.",
            "Appliquer les changements de temps nécessaires quand le verbe introducteur est au passé.",
            "Adapter les pronoms et les expressions de temps/lieu au discours indirect.",
        ],
        "content": {
            "intro": "Rapporter les paroles de quelqu'un sans les citer directement demande d'ajuster la structure, les pronoms, et parfois le temps du verbe — un ensemble de règles logiques une fois qu'on en comprend le principe.",
            "explanation": "<p>Au discours indirect, on rapporte les paroles de quelqu'un avec un verbe introducteur (<em>dire, demander, expliquer, répondre</em>) suivi de <em>que</em> (déclaration) ou d'un mot interrogatif : <em>« Je suis fatigué », dit-il → Il dit qu'il est fatigué.</em> Si le verbe introducteur est au <strong>présent</strong>, le temps du verbe rapporté ne change pas.</p><p>Si le verbe introducteur est au <strong>passé</strong>, on applique un décalage temporel (la « concordance des temps ») : le présent devient imparfait, le passé composé devient plus-que-parfait, le futur simple devient conditionnel présent : <em>« Je viendrai », a-t-il dit → Il a dit qu'il viendrait.</em> Les indicateurs de temps/lieu changent aussi (<em>aujourd'hui → ce jour-là, demain → le lendemain</em>).</p>",
            "rules": [
                {"heading": "a) Verbe introducteur au présent", "body": "<ul><li>Aucun changement de temps : <em>Il dit qu'il est fatigué.</em></li></ul>"},
                {"heading": "b) Verbe introducteur au passé", "body": "<ul><li>présent→imparfait, passé composé→plus-que-parfait, futur simple→conditionnel présent.</li></ul>"},
                {"heading": "c) Questions", "body": "<ul><li><em>est-ce que → si ; qu'est-ce que → ce que</em> ; les mots interrogatifs (où, quand, pourquoi) restent identiques.</li></ul>"},
                {"heading": "d) Temps et lieu", "body": "<ul><li><em>aujourd'hui→ce jour-là, demain→le lendemain, hier→la veille</em>.</li></ul>"},
            ],
            "examples": [
                "« Je suis fatigué », dit-il. → Il dit qu'il est fatigué.",
                "« Je viendrai demain », a-t-il dit. → Il a dit qu'il viendrait le lendemain.",
                "« Où habites-tu ? », a-t-elle demandé. → Elle a demandé où j'habitais.",
                "« Est-ce que tu viens ? », a-t-il demandé. → Il a demandé si je venais.",
                "« J'ai fini », a-t-elle dit. → Elle a dit qu'elle avait fini.",
                "Il m'a expliqué qu'il ne pouvait pas venir.",
                "Elle a répondu qu'elle était d'accord.",
            ],
            "commonMistakes": [
                {"wrong": "Il a dit qu'il vient demain.", "right": "Il a dit qu'il viendrait le lendemain.", "why": "Verbe introducteur au passé : le futur devient conditionnel présent, et demain devient le lendemain."},
                {"wrong": "Elle a demandé si je viens.", "right": "Elle a demandé si je venais.", "why": "Concordance des temps : le présent devient imparfait après un verbe introducteur au passé."},
                {"wrong": "Il a demandé qu'est-ce que je voulais.", "right": "Il a demandé ce que je voulais.", "why": "Qu'est-ce que devient ce que au discours indirect."},
            ],
        },
        "exercises": [
            {"id": "b1dis-fill", "type": "fill-blank", "title": "Passe au Discours Indirect",
             "instructions": "Complète avec la forme correcte au discours indirect.",
             "items": [
                {"id": "b1disf1", "prompt": "« Je suis fatigué », dit-il. → Il dit qu'il ___ fatigué.", "answers": [["est"]], "options": ["est", "était", "soit"], "explanation": "Verbe introducteur au présent : aucun changement de temps."},
                {"id": "b1disf2", "prompt": "« Je viendrai demain », a-t-il dit. → Il a dit qu'il ___ le lendemain.", "answers": [["viendrait"]], "options": ["viendrait", "viendra", "venait"], "explanation": "Futur simple → conditionnel présent après un verbe introducteur au passé."},
                {"id": "b1disf3", "prompt": "« J'ai fini », a-t-elle dit. → Elle a dit qu'elle ___ fini.", "answers": [["avait"]], "options": ["avait", "a", "aurait"], "explanation": "Passé composé → plus-que-parfait après un verbe introducteur au passé."},
                {"id": "b1disf4", "prompt": "« Est-ce que tu viens ? », a-t-il demandé. → Il a demandé ___ je venais.", "answers": [["si"]], "options": ["si", "que", "est-ce que"], "explanation": "Est-ce que devient si au discours indirect."},
             ]},
            {"id": "b1dis-mc", "type": "multiple-choice", "title": "Le Discours Indirect",
             "items": [
                {"id": "b1dism1", "prompt": "Que devient le futur simple après un verbe introducteur au passé ?", "options": ["le conditionnel présent", "l'imparfait", "le subjonctif"], "answerIndex": 0, "explanation": "C'est le décalage propre à la concordance des temps."},
                {"id": "b1dism2", "prompt": "Que devient « qu'est-ce que » au discours indirect ?", "options": ["ce que", "que", "dont"], "answerIndex": 0, "explanation": "Qu'est-ce que devient ce que."},
                {"id": "b1dism3", "prompt": "Que devient « demain » quand le verbe introducteur est au passé ?", "options": ["le lendemain", "hier", "aujourd'hui"], "answerIndex": 0, "explanation": "Les repères temporels changent selon le contexte."},
                {"id": "b1dism4", "prompt": "Si le verbe introducteur est au présent, le temps du verbe rapporté...", "options": ["ne change pas", "change toujours", "devient toujours le subjonctif"], "answerIndex": 0, "explanation": "Seul un verbe introducteur au passé déclenche un changement de temps."},
             ]},
            {"id": "b1dis-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1disc1", "incorrect": "Il a dit qu'il vient demain.", "answer": ["Il a dit qu'il viendrait le lendemain."], "explanation": "Futur → conditionnel présent, demain → le lendemain."},
                {"id": "b1disc2", "incorrect": "Elle a demandé si je viens.", "answer": ["Elle a demandé si je venais."], "explanation": "Présent → imparfait après un verbe introducteur au passé."},
                {"id": "b1disc3", "incorrect": "Il a demandé qu'est-ce que je voulais.", "answer": ["Il a demandé ce que je voulais."], "explanation": "Qu'est-ce que devient ce que."},
             ]},
        ],
        "summary": [
            "Le discours indirect rapporte des paroles avec un verbe introducteur + que ou un mot interrogatif.",
            "Si ce verbe est au passé, on applique la concordance des temps (présent→imparfait, passé composé→plus-que-parfait, futur→conditionnel).",
            "Les expressions de temps et de lieu changent aussi selon le contexte (demain→le lendemain, ici→là).",
        ],
    },
    {
        "id": "b1-les-pronoms-relatifs",
        "level": "B1", "unit": "1", "order": 6, "skill": "grammar", "strand": "pronoms-relatifs",
        "title": "Les Pronoms Relatifs",
        "subtitle": "Qui, que, où et dont pour relier deux phrases sans répéter un nom déjà mentionné.",
        "objectives": [
            "Utiliser qui pour remplacer un sujet et que pour remplacer un complément d'objet direct.",
            "Utiliser où pour un complément de lieu ou de temps.",
            "Utiliser dont pour un complément introduit par de.",
        ],
        "content": {
            "intro": "Les pronoms relatifs relient deux phrases en évitant de répéter un nom déjà mentionné — une construction indispensable pour des phrases plus fluides et plus naturelles.",
            "explanation": "<p><strong>Qui</strong> remplace le sujet de la proposition relative (jamais suivi d'une élision) : <em>J'ai un ami qui habite à Paris.</em> <strong>Que</strong> remplace le complément d'objet direct (s'élide en qu' devant une voyelle) : <em>Le livre que je lis est passionnant.</em></p><p><strong>Où</strong> remplace un complément de lieu ou de temps : <em>La ville où j'habite est petite. Le jour où je suis né…</em> <strong>Dont</strong> remplace un complément introduit par <em>de</em> (parler de, avoir besoin de) : <em>Le livre dont je parle est excellent.</em></p>",
            "rules": [
                {"heading": "a) Qui", "body": "<ul><li>Remplace le sujet, jamais suivi d'élision : <em>L'homme qui parle est mon voisin.</em></li></ul>"},
                {"heading": "b) Que", "body": "<ul><li>Remplace le COD, s'élide devant une voyelle : <em>Le film que j'ai vu était bon.</em></li></ul>"},
                {"heading": "c) Où", "body": "<ul><li>Lieu ou temps : <em>La maison où je suis né.</em></li></ul>"},
                {"heading": "d) Dont", "body": "<ul><li>Complément introduit par de : <em>Le sujet dont on parle m'intéresse.</em></li></ul>"},
            ],
            "examples": [
                "J'ai un ami qui habite à Paris.",
                "Le livre que je lis est passionnant.",
                "La ville où j'habite est petite.",
                "Le livre dont je parle est excellent.",
                "C'est la femme qui m'a aidé hier.",
                "Voici la maison où j'ai grandi.",
                "C'est un sujet dont j'ai besoin de parler.",
            ],
            "commonMistakes": [
                {"wrong": "J'ai un ami que habite à Paris.", "right": "J'ai un ami qui habite à Paris.", "why": "Le sujet de la relative se remplace par qui, pas que."},
                {"wrong": "Le livre qui je lis est passionnant.", "right": "Le livre que je lis est passionnant.", "why": "Le complément d'objet direct se remplace par que, pas qui."},
                {"wrong": "Le livre que je parle est excellent.", "right": "Le livre dont je parle est excellent.", "why": "Parler de demande dont, pas que, car de introduit son complément."},
            ],
        },
        "exercises": [
            {"id": "b1rel-fill", "type": "fill-blank", "title": "Complète avec le Bon Pronom Relatif",
             "instructions": "Choisis qui, que, où ou dont.",
             "items": [
                {"id": "b1relf1", "prompt": "J'ai un ami ___ habite à Paris.", "answers": [["qui"]], "options": ["qui", "que", "dont"], "explanation": "Sujet de la relative : qui."},
                {"id": "b1relf2", "prompt": "Le livre ___ je lis est passionnant.", "answers": [["que"]], "options": ["que", "qui", "où"], "explanation": "Complément d'objet direct : que."},
                {"id": "b1relf3", "prompt": "La ville ___ j'habite est petite.", "answers": [["où"]], "options": ["où", "que", "dont"], "explanation": "Complément de lieu : où."},
                {"id": "b1relf4", "prompt": "Le livre ___ je parle est excellent.", "answers": [["dont"]], "options": ["dont", "que", "qui"], "explanation": "Parler de → dont."},
             ]},
            {"id": "b1rel-mc", "type": "multiple-choice", "title": "Les Pronoms Relatifs",
             "items": [
                {"id": "b1relm1", "prompt": "Quel pronom relatif remplace le sujet ?", "options": ["qui", "que", "dont"], "answerIndex": 0, "explanation": "Qui remplace toujours le sujet."},
                {"id": "b1relm2", "prompt": "Quel pronom relatif remplace un complément introduit par de ?", "options": ["dont", "que", "où"], "answerIndex": 0, "explanation": "Dont remplace un complément en de."},
                {"id": "b1relm3", "prompt": "Quel pronom relatif utilise-t-on pour un lieu ?", "options": ["où", "qui", "que"], "answerIndex": 0, "explanation": "Où marque le lieu ou le temps."},
                {"id": "b1relm4", "prompt": "Que remplace le pronom relatif que ?", "options": ["le complément d'objet direct", "le sujet", "un complément en de"], "answerIndex": 0, "explanation": "Que remplace toujours le COD."},
             ]},
            {"id": "b1rel-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1relc1", "incorrect": "J'ai un ami que habite à Paris.", "answer": ["J'ai un ami qui habite à Paris."], "explanation": "Le sujet se remplace par qui."},
                {"id": "b1relc2", "incorrect": "Le livre qui je lis est passionnant.", "answer": ["Le livre que je lis est passionnant."], "explanation": "Le COD se remplace par que."},
                {"id": "b1relc3", "incorrect": "Le livre que je parle est excellent.", "answer": ["Le livre dont je parle est excellent."], "explanation": "Parler de demande dont."},
             ]},
        ],
        "summary": [
            "Qui remplace le sujet, que remplace le complément d'objet direct.",
            "Où remplace un complément de lieu ou de temps.",
            "Dont remplace un complément introduit par de.",
        ],
    },
    {
        "id": "b1-la-voix-passive",
        "level": "B1", "unit": "1", "order": 7, "skill": "grammar", "strand": "voix-passive",
        "title": "La Voix Passive",
        "subtitle": "Comment former la voix passive avec être + participe passé, et quand le français la préfère à la voix active.",
        "objectives": [
            "Former la voix passive avec être + participe passé + par.",
            "Accorder le participe passé avec le sujet à la voix passive.",
            "Reconnaître quand le français préfère la voix passive, active, ou une construction avec on.",
        ],
        "content": {
            "intro": "La voix passive met en avant celui qui subit l'action plutôt que celui qui l'accomplit — une construction moins fréquente en français qu'en anglais, mais utile à reconnaître et à utiliser correctement.",
            "explanation": "<p>La voix passive se forme avec <strong>être</strong> (au temps voulu) + le <strong>participe passé</strong> du verbe, suivi de <em>par</em> + l'agent si on veut le préciser : <em>Le voleur a été arrêté par la police.</em> Le participe passé s'accorde toujours avec le sujet, comme un adjectif.</p><p>Seuls les verbes qui ont un complément d'objet direct peuvent se mettre au passif. Le français utilise la voix passive moins souvent que l'anglais : quand l'agent n'est pas important, on préfère souvent une construction avec <strong>on</strong> à la voix active : <em>On a construit ce pont en 1990</em>, plutôt que <em>Ce pont a été construit en 1990 par des ouvriers.</em></p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>être (au temps voulu) + participe passé + par + agent (optionnel).</li></ul>"},
                {"heading": "b) Accord", "body": "<ul><li>Le participe passé s'accorde toujours avec le sujet du passif.</li></ul>"},
                {"heading": "c) Verbes concernés", "body": "<ul><li>Seuls les verbes transitifs directs (avec COD) peuvent se mettre au passif.</li></ul>"},
                {"heading": "d) Préférence du français", "body": "<ul><li>On + voix active est souvent préféré au passif quand l'agent est inconnu ou peu important.</li></ul>"},
            ],
            "examples": [
                "Le voleur a été arrêté par la police.",
                "Cette maison a été construite en 1950.",
                "Les lettres sont envoyées chaque semaine.",
                "Le gâteau a été mangé par les enfants.",
                "On construit ce pont depuis deux ans.",
                "Ce roman a été traduit en dix langues.",
                "Les billets seront vendus demain.",
            ],
            "commonMistakes": [
                {"wrong": "Le voleur a été arrêter par la police.", "right": "Le voleur a été arrêté par la police.", "why": "Après être au passif, on utilise le participe passé (arrêté), pas l'infinitif."},
                {"wrong": "La maison a été construit en 1950.", "right": "La maison a été construite en 1950.", "why": "Le participe passé s'accorde avec le sujet féminin, maison : construite."},
                {"wrong": "On a été construit ce pont.", "right": "On a construit ce pont.", "why": "On + être + participe passé n'existe pas ; il faut choisir entre on + voix active, ou le sujet + être + participe passé au passif."},
            ],
        },
        "exercises": [
            {"id": "b1pas-fill", "type": "fill-blank", "title": "Mets à la Voix Passive",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b1pasf1", "prompt": "Le voleur ___ (arrêter) par la police.", "answers": [["a été arrêté"]], "options": ["a été arrêté", "a arrêté", "était arrêté"], "explanation": "Passif : être au temps voulu + participe passé."},
                {"id": "b1pasf2", "prompt": "Cette maison ___ (construire) en 1950.", "answers": [["a été construite"]], "options": ["a été construite", "a été construit", "a construit"], "explanation": "Accord du participe passé avec le sujet féminin, maison."},
                {"id": "b1pasf3", "prompt": "Les lettres ___ (envoyer) chaque semaine.", "answers": [["sont envoyées"]], "options": ["sont envoyées", "envoient", "ont envoyé"], "explanation": "Passif au présent, accord au féminin pluriel."},
                {"id": "b1pasf4", "prompt": "Ce roman ___ (traduire) en dix langues.", "answers": [["a été traduit"]], "options": ["a été traduit", "a traduit", "était traduit"], "explanation": "Passif au passé composé."},
             ]},
            {"id": "b1pas-mc", "type": "multiple-choice", "title": "La Voix Passive",
             "items": [
                {"id": "b1pasm1", "prompt": "Comment forme-t-on la voix passive ?", "options": ["être + participe passé (+ par + agent)", "avoir + participe passé", "être + infinitif"], "answerIndex": 0, "explanation": "C'est la formation classique du passif."},
                {"id": "b1pasm2", "prompt": "Avec quoi le participe passé s'accorde-t-il au passif ?", "options": ["le sujet", "l'agent", "l'auxiliaire"], "answerIndex": 0, "explanation": "L'accord se fait toujours avec le sujet, comme un adjectif."},
                {"id": "b1pasm3", "prompt": "Quels verbes peuvent se mettre au passif ?", "options": ["les verbes avec un complément d'objet direct", "tous les verbes", "seulement les verbes pronominaux"], "answerIndex": 0, "explanation": "Seuls les verbes transitifs directs ont un passif."},
                {"id": "b1pasm4", "prompt": "Que préfère souvent le français quand l'agent n'est pas important ?", "options": ["on + voix active", "le passif avec par", "l'impératif"], "answerIndex": 0, "explanation": "On + voix active est plus naturel dans ce cas."},
             ]},
            {"id": "b1pas-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1pasc1", "incorrect": "Le voleur a été arrêter par la police.", "answer": ["Le voleur a été arrêté par la police."], "explanation": "Le passif demande le participe passé, pas l'infinitif."},
                {"id": "b1pasc2", "incorrect": "La maison a été construit en 1950.", "answer": ["La maison a été construite en 1950."], "explanation": "Accord au féminin avec le sujet."},
                {"id": "b1pasc3", "incorrect": "On a été construit ce pont.", "answer": ["On a construit ce pont."], "explanation": "On ne se combine pas avec être + participe passé."},
             ]},
        ],
        "summary": [
            "La voix passive se forme avec être + participe passé, suivi de par + agent si nécessaire.",
            "Le participe passé s'accorde toujours avec le sujet du passif.",
            "Le français préfère souvent on + voix active à la voix passive quand l'agent est inconnu ou sans importance.",
        ],
    },
    {
        "id": "b1-les-connecteurs-logiques",
        "level": "B1", "unit": "1", "order": 8, "skill": "grammar", "strand": "connecteurs-logiques",
        "title": "Les Connecteurs Logiques",
        "subtitle": "Cause, conséquence, opposition et but : parce que, donc, mais, pour que, afin de.",
        "objectives": [
            "Exprimer la cause avec parce que, car, puisque.",
            "Exprimer la conséquence avec donc, alors, c'est pourquoi.",
            "Exprimer l'opposition et le but avec mais, pourtant, pour que, afin de.",
        ],
        "content": {
            "intro": "Les connecteurs logiques relient les idées d'un texte ou d'un discours et rendent l'argumentation claire — indispensables dès qu'on veut expliquer, justifier ou nuancer une idée.",
            "explanation": "<p>La <strong>cause</strong> s'exprime avec <em>parce que</em> (réponse à pourquoi, information nouvelle), <em>car</em> (surtout à l'écrit, jamais en début de phrase) et <em>puisque</em> (cause déjà connue de l'interlocuteur) : <em>Je reste chez moi parce qu'il pleut. Puisque tu es fatigué, repose-toi.</em> La <strong>conséquence</strong> s'exprime avec <em>donc, alors, c'est pourquoi</em>.</p><p>L'<strong>opposition</strong> s'exprime avec <em>mais</em> (simple), <em>pourtant/cependant</em> (plus soutenu). Le <strong>but</strong> s'exprime avec <em>pour que</em> + subjonctif (sujets différents) ou <em>afin de</em> + infinitif (même sujet) : <em>Je parle lentement pour que tu comprennes. J'étudie afin de réussir.</em></p>",
            "rules": [
                {"heading": "a) Cause", "body": "<ul><li><em>parce que</em> (réponse à pourquoi), <em>car</em> (écrit, jamais en tête de phrase), <em>puisque</em> (cause connue).</li></ul>"},
                {"heading": "b) Conséquence", "body": "<ul><li><em>donc, alors, c'est pourquoi</em>.</li></ul>"},
                {"heading": "c) Opposition", "body": "<ul><li><em>mais</em> (simple), <em>pourtant/cependant</em> (plus soutenu).</li></ul>"},
                {"heading": "d) But", "body": "<ul><li><em>pour que</em> + subjonctif (sujets différents), <em>afin de</em> + infinitif (même sujet).</li></ul>"},
            ],
            "examples": [
                "Je reste chez moi parce qu'il pleut.",
                "Puisque tu es fatigué, repose-toi.",
                "Il a beaucoup travaillé, donc il a réussi.",
                "Elle est timide, pourtant elle adore parler en public.",
                "Je parle lentement pour que tu comprennes.",
                "J'étudie afin de réussir mon examen.",
                "Il fait froid, alors je mets un manteau.",
            ],
            "commonMistakes": [
                {"wrong": "Car il pleut, je reste chez moi.", "right": "Je reste chez moi car il pleut.", "why": "Car ne s'utilise jamais en début de phrase, contrairement à parce que."},
                {"wrong": "Je parle lentement pour que tu comprends.", "right": "Je parle lentement pour que tu comprennes.", "why": "Pour que est toujours suivi du subjonctif."},
                {"wrong": "J'étudie afin de je réussisse.", "right": "J'étudie afin de réussir.", "why": "Afin de est suivi de l'infinitif quand le sujet est le même dans les deux propositions."},
            ],
        },
        "exercises": [
            {"id": "b1con-fill", "type": "fill-blank", "title": "Choisis le Bon Connecteur",
             "instructions": "Complète avec le connecteur logique correct.",
             "items": [
                {"id": "b1conf1", "prompt": "Je parle lentement ___ tu comprennes.", "answers": [["pour que"]], "options": ["pour que", "afin de", "parce que"], "explanation": "But avec sujets différents : pour que + subjonctif."},
                {"id": "b1conf2", "prompt": "J'étudie ___ réussir mon examen.", "answers": [["afin de"]], "options": ["afin de", "pour que", "puisque"], "explanation": "But avec le même sujet : afin de + infinitif."},
                {"id": "b1conf3", "prompt": "Il a beaucoup travaillé, ___ il a réussi.", "answers": [["donc"]], "options": ["donc", "car", "afin de"], "explanation": "Conséquence : donc."},
                {"id": "b1conf4", "prompt": "Elle est timide, ___ elle adore parler en public.", "answers": [["pourtant"]], "options": ["pourtant", "donc", "puisque"], "explanation": "Opposition soutenue : pourtant."},
             ]},
            {"id": "b1con-mc", "type": "multiple-choice", "title": "Les Connecteurs Logiques",
             "items": [
                {"id": "b1conm1", "prompt": "Quel connecteur ne s'utilise jamais en début de phrase ?", "options": ["car", "parce que", "puisque"], "answerIndex": 0, "explanation": "Car ne s'emploie jamais en tête de phrase."},
                {"id": "b1conm2", "prompt": "Quel connecteur exprime la conséquence ?", "options": ["donc", "mais", "afin de"], "answerIndex": 0, "explanation": "Donc introduit une conséquence."},
                {"id": "b1conm3", "prompt": "Que suit « pour que » ?", "options": ["le subjonctif", "l'infinitif", "l'indicatif"], "answerIndex": 0, "explanation": "Pour que est toujours suivi du subjonctif."},
                {"id": "b1conm4", "prompt": "Que suit « afin de » ?", "options": ["l'infinitif", "le subjonctif", "l'indicatif"], "answerIndex": 0, "explanation": "Afin de est suivi de l'infinitif."},
             ]},
            {"id": "b1con-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1conc1", "incorrect": "Car il pleut, je reste chez moi.", "answer": ["Je reste chez moi car il pleut."], "explanation": "Car ne s'utilise jamais en début de phrase."},
                {"id": "b1conc2", "incorrect": "Je parle lentement pour que tu comprends.", "answer": ["Je parle lentement pour que tu comprennes."], "explanation": "Pour que impose le subjonctif."},
                {"id": "b1conc3", "incorrect": "J'étudie afin de je réussisse.", "answer": ["J'étudie afin de réussir."], "explanation": "Afin de est suivi de l'infinitif quand le sujet est le même."},
             ]},
        ],
        "summary": [
            "La cause s'exprime avec parce que, car (jamais en tête de phrase) et puisque ; la conséquence avec donc, alors, c'est pourquoi.",
            "L'opposition s'exprime avec mais, ou pourtant/cependant en registre plus soutenu.",
            "Le but s'exprime avec pour que + subjonctif (sujets différents) ou afin de + infinitif (même sujet).",
        ],
    },
    {
        "id": "b1-le-gerondif-et-le-participe-present",
        "level": "B1", "unit": "1", "order": 9, "skill": "grammar", "strand": "gerondif-participe-present",
        "title": "Le Gérondif et le Participe Présent",
        "subtitle": "En + participe présent pour la simultanéité et la manière, et le participe présent employé seul.",
        "objectives": [
            "Former le gérondif (en + participe présent) et l'utiliser pour exprimer la simultanéité ou la manière.",
            "Former le participe présent régulier et connaître les trois exceptions.",
            "Distinguer le gérondif (toujours avec en) du participe présent employé seul.",
        ],
        "content": {
            "intro": "Le gérondif et le participe présent partagent la même forme verbale, mais jouent des rôles différents dans la phrase — l'un décrit comment ou quand une action se produit, l'autre fonctionne presque comme un adjectif.",
            "explanation": "<p>Le participe présent se forme à partir du radical de <em>nous</em> au présent + <strong>-ant</strong> : <em>nous parlons → parlant, nous finissons → finissant</em>. Trois verbes sont irréguliers : <em>être → étant, avoir → ayant, savoir → sachant</em>. Précédé de <strong>en</strong>, il devient le <strong>gérondif</strong>, qui exprime la simultanéité ou la manière : <em>Elle écoute de la musique en travaillant. Il a réussi en persévérant.</em></p><p>Le participe présent employé seul (sans <em>en</em>) fonctionne davantage comme un adjectif ou remplace une proposition relative, surtout à l'écrit : <em>une personne parlant plusieurs langues</em> (= qui parle plusieurs langues).</p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>Radical de nous au présent (sans -ons) + -ant.</li></ul>"},
                {"heading": "b) Trois irréguliers", "body": "<ul><li><em>être → étant, avoir → ayant, savoir → sachant</em>.</li></ul>"},
                {"heading": "c) Gérondif", "body": "<ul><li><em>en</em> + participe présent : exprime la simultanéité ou la manière.</li></ul>"},
                {"heading": "d) Participe présent seul", "body": "<ul><li>Sans en : fonctionne comme un adjectif, remplace souvent qui + verbe.</li></ul>"},
            ],
            "examples": [
                "Elle écoute de la musique en travaillant.",
                "Il a réussi en persévérant.",
                "En sortant, n'oublie pas tes clés.",
                "Une personne parlant plusieurs langues a un avantage.",
                "Sachant qu'il pleuvait, j'ai pris un parapluie.",
                "Nous avons appris beaucoup en voyageant.",
                "Ayant fini ses devoirs, elle est sortie jouer.",
            ],
            "commonMistakes": [
                {"wrong": "Elle écoute de la musique en travailler.", "right": "Elle écoute de la musique en travaillant.", "why": "Le gérondif utilise le participe présent (travaillant), pas l'infinitif."},
                {"wrong": "Il a réussi par persévérant.", "right": "Il a réussi en persévérant.", "why": "Le gérondif est toujours introduit par en, jamais par une autre préposition."},
                {"wrong": "Sachant que il pleuvait.", "right": "Sachant qu'il pleuvait.", "why": "Que s'élide toujours en qu' devant il."},
            ],
        },
        "exercises": [
            {"id": "b1ger-fill", "type": "fill-blank", "title": "Forme le Gérondif",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b1gerf1", "prompt": "Elle écoute de la musique en ___ (travailler).", "answers": [["travaillant"]], "options": ["travaillant", "travailler", "travaille"], "explanation": "Gérondif : en + participe présent."},
                {"id": "b1gerf2", "prompt": "Il a réussi en ___ (persévérer).", "answers": [["persévérant"]], "options": ["persévérant", "persévérer", "persévère"], "explanation": "Gérondif de persévérer."},
                {"id": "b1gerf3", "prompt": "___ (savoir) qu'il pleuvait, j'ai pris un parapluie.", "answers": [["Sachant"]], "options": ["Sachant", "Savant", "Sais"], "explanation": "Savoir a un participe présent irrégulier : sachant."},
                {"id": "b1gerf4", "prompt": "___ (avoir) fini ses devoirs, elle est sortie jouer.", "answers": [["Ayant"]], "options": ["Ayant", "Avant", "Avoir"], "explanation": "Avoir a un participe présent irrégulier : ayant."},
             ]},
            {"id": "b1ger-mc", "type": "multiple-choice", "title": "Le Gérondif et le Participe Présent",
             "items": [
                {"id": "b1germ1", "prompt": "Comment forme-t-on le participe présent régulier ?", "options": ["radical de nous au présent + -ant", "infinitif + -ant", "radical de je au présent + -ant"], "answerIndex": 0, "explanation": "On part du radical de nous, sans -ons."},
                {"id": "b1germ2", "prompt": "Quelle préposition introduit toujours le gérondif ?", "options": ["en", "par", "à"], "answerIndex": 0, "explanation": "Le gérondif est toujours en + participe présent."},
                {"id": "b1germ3", "prompt": "Quel est le participe présent de savoir ?", "options": ["sachant", "savant", "sachiez"], "answerIndex": 0, "explanation": "Savoir est l'un des trois irréguliers : sachant."},
                {"id": "b1germ4", "prompt": "Que peut remplacer un participe présent employé seul ?", "options": ["une proposition relative (qui + verbe)", "un adverbe", "un article"], "answerIndex": 0, "explanation": "Il fonctionne comme un adjectif ou une relative allégée."},
             ]},
            {"id": "b1ger-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1gerc1", "incorrect": "Elle écoute de la musique en travailler.", "answer": ["Elle écoute de la musique en travaillant."], "explanation": "Le gérondif utilise le participe présent."},
                {"id": "b1gerc2", "incorrect": "Il a réussi par persévérant.", "answer": ["Il a réussi en persévérant."], "explanation": "Le gérondif est toujours introduit par en."},
                {"id": "b1gerc3", "incorrect": "Sachant que il pleuvait.", "answer": ["Sachant qu'il pleuvait."], "explanation": "Que s'élide devant il."},
             ]},
        ],
        "summary": [
            "Le participe présent se forme avec le radical de nous au présent + -ant (trois irréguliers : étant, ayant, sachant).",
            "Le gérondif (en + participe présent) exprime la simultanéité ou la manière.",
            "Le participe présent seul, sans en, fonctionne comme un adjectif ou remplace une relative.",
        ],
    },
    {
        "id": "b1-les-doubles-pronoms",
        "level": "B1", "unit": "1", "order": 10, "skill": "grammar", "strand": "doubles-pronoms",
        "title": "Les Doubles Pronoms",
        "subtitle": "Comment combiner un pronom COD et un pronom COI dans le bon ordre, au présent, au passé composé et à l'impératif.",
        "objectives": [
            "Combiner un pronom COD et un pronom COI dans la même phrase.",
            "Appliquer le bon ordre des pronoms selon leur type et leur personne.",
            "Placer correctement les doubles pronoms au passé composé et à l'impératif affirmatif.",
        ],
        "content": {
            "intro": "Quand une phrase contient à la fois un complément d'objet direct et un complément d'objet indirect, les deux pronoms se combinent devant le verbe, dans un ordre précis à mémoriser.",
            "explanation": "<p>Quand on combine un pronom COD et un pronom COI, l'ordre dépend de leur personne : <strong>me/te/nous/vous</strong> se placent toujours avant <strong>le/la/les</strong> (<em>Il me le donne</em>), mais <strong>le/la/les</strong> se placent avant <strong>lui/leur</strong> (<em>Je le lui donne</em>). Les deux pronoms se placent ensemble avant le verbe conjugué, ou avant l'auxiliaire au passé composé : <em>Il me l'a donné.</em></p><p>À l'impératif affirmatif, les pronoms suivent le verbe et sont reliés par un trait d'union, dans l'ordre COD puis COI : <em>Donne-le-moi !</em> (et <em>me</em> devient <em>moi</em> en position finale). À l'impératif négatif, l'ordre habituel revient devant le verbe : <em>Ne me le donne pas.</em></p>",
            "rules": [
                {"heading": "a) me/te/nous/vous + le/la/les", "body": "<ul><li>Jamais l'inverse : <em>Il me le donne</em>, pas « il le me donne ».</li></ul>"},
                {"heading": "b) le/la/les + lui/leur", "body": "<ul><li>Jamais l'inverse : <em>Je le lui donne</em>, pas « je lui le donne ».</li></ul>"},
                {"heading": "c) Passé composé", "body": "<ul><li>Les deux pronoms se placent ensemble avant l'auxiliaire : <em>Il me l'a donné.</em></li></ul>"},
                {"heading": "d) Impératif affirmatif", "body": "<ul><li>Verbe + trait d'union + COD + COI (me→moi, te→toi) : <em>Donne-le-moi !</em> Négatif : ordre normal avant le verbe.</li></ul>"},
            ],
            "examples": [
                "Il me le donne.",
                "Je le lui donne.",
                "Elle nous les envoie.",
                "Tu me l'as dit hier.",
                "Donne-le-moi, s'il te plaît !",
                "Ne me le donne pas.",
                "Nous le leur avons expliqué.",
            ],
            "commonMistakes": [
                {"wrong": "Il le me donne.", "right": "Il me le donne.", "why": "Me/te/nous/vous se placent toujours avant le/la/les."},
                {"wrong": "Je lui le donne.", "right": "Je le lui donne.", "why": "Le/la/les se placent avant lui/leur."},
                {"wrong": "Donne-moi-le.", "right": "Donne-le-moi.", "why": "À l'impératif affirmatif, l'ordre est COD puis COI : le avant moi."},
            ],
        },
        "exercises": [
            {"id": "b1dbp-fill", "type": "fill-blank", "title": "Combine les Doubles Pronoms",
             "instructions": "Récris la partie de phrase avec les deux pronoms dans le bon ordre.",
             "items": [
                {"id": "b1dbpf1", "prompt": "Il ___ donne. (me + le)", "answers": [["me le"]], "options": ["me le", "le me", "me lui"], "explanation": "Me se place avant le."},
                {"id": "b1dbpf2", "prompt": "Je ___ donne. (le + lui)", "answers": [["le lui"]], "options": ["le lui", "lui le", "le leur"], "explanation": "Le se place avant lui."},
                {"id": "b1dbpf3", "prompt": "Tu ___ as dit hier. (me + l')", "answers": [["me l'"]], "options": ["me l'", "l'me", "le me"], "explanation": "Me se place avant l'."},
                {"id": "b1dbpf4", "prompt": "___, s'il te plaît ! (donne + le + moi, impératif)", "answers": [["Donne-le-moi"]], "options": ["Donne-le-moi", "Donne-moi-le", "Me le donne"], "explanation": "À l'impératif affirmatif : verbe + COD + COI."},
             ]},
            {"id": "b1dbp-mc", "type": "multiple-choice", "title": "Les Doubles Pronoms",
             "items": [
                {"id": "b1dbpm1", "prompt": "Quel ordre suivent me/te/nous/vous et le/la/les ensemble ?", "options": ["me/te/nous/vous avant le/la/les", "le/la/les avant me/te/nous/vous", "cela dépend du verbe"], "answerIndex": 0, "explanation": "C'est l'ordre fixe des doubles pronoms."},
                {"id": "b1dbpm2", "prompt": "Quel ordre suivent le/la/les et lui/leur ensemble ?", "options": ["le/la/les avant lui/leur", "lui/leur avant le/la/les", "cela dépend du temps"], "answerIndex": 0, "explanation": "Le/la/les précèdent toujours lui/leur."},
                {"id": "b1dbpm3", "prompt": "Où se placent les doubles pronoms à l'impératif affirmatif ?", "options": ["après le verbe, avec des traits d'union", "avant le verbe", "au milieu du verbe"], "answerIndex": 0, "explanation": "L'impératif affirmatif place les pronoms après le verbe."},
                {"id": "b1dbpm4", "prompt": "Que devient me en position finale à l'impératif affirmatif ?", "options": ["moi", "me", "m'"], "answerIndex": 0, "explanation": "Me devient moi en fin de mot à l'impératif affirmatif."},
             ]},
            {"id": "b1dbp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1dbpc1", "incorrect": "Il le me donne.", "answer": ["Il me le donne."], "explanation": "Me se place avant le."},
                {"id": "b1dbpc2", "incorrect": "Je lui le donne.", "answer": ["Je le lui donne."], "explanation": "Le se place avant lui."},
                {"id": "b1dbpc3", "incorrect": "Donne-moi-le.", "answer": ["Donne-le-moi."], "explanation": "L'ordre à l'impératif affirmatif est COD puis COI."},
             ]},
        ],
        "summary": [
            "Me/te/nous/vous se placent avant le/la/les ; le/la/les se placent avant lui/leur.",
            "Les deux pronoms se placent ensemble avant le verbe conjugué, ou avant l'auxiliaire au passé composé.",
            "À l'impératif affirmatif, l'ordre est verbe + COD + COI, relié par des traits d'union (me devient moi).",
        ],
    },
    {
        "id": "b1-lexpression-de-lhypothese-avec-si",
        "level": "B1", "unit": "1", "order": 11, "skill": "grammar", "strand": "hypothese-si",
        "title": "L'Expression de l'Hypothèse avec Si",
        "subtitle": "Si + présent, si + imparfait, si + plus-que-parfait : trois structures pour trois types d'hypothèses.",
        "objectives": [
            "Former une hypothèse réalisable avec si + présent, futur/impératif.",
            "Former une hypothèse non réelle dans le présent avec si + imparfait, conditionnel présent.",
            "Reconnaître la structure si + plus-que-parfait, conditionnel passé pour une hypothèse manquée dans le passé.",
        ],
        "content": {
            "intro": "Les phrases avec si permettent d'imaginer des situations, réelles ou non — et le temps utilisé après si détermine si l'hypothèse est réalisable, imaginaire, ou déjà manquée.",
            "explanation": "<p>Pour une hypothèse <strong>réalisable</strong>, on utilise <em>si</em> + <strong>présent</strong>, et le futur simple ou l'impératif dans la proposition principale : <em>Si tu viens, nous serons contents. Si tu as faim, mange !</em> Cette structure décrit une condition qui peut vraiment se réaliser.</p><p>Pour une hypothèse <strong>imaginaire</strong> dans le présent, on utilise <em>si</em> + <strong>imparfait</strong>, et le <strong>conditionnel présent</strong> dans la principale : <em>Si j'avais plus de temps, je voyagerais davantage.</em> Pour une hypothèse déjà <strong>manquée dans le passé</strong>, on utilise <em>si</em> + <strong>plus-que-parfait</strong>, et le <strong>conditionnel passé</strong> : <em>Si j'avais su, je serais venu.</em> Dans les trois cas, le verbe après <em>si</em> n'est jamais au futur ni au conditionnel.</p>",
            "rules": [
                {"heading": "a) Réalisable", "body": "<ul><li>si + présent, futur simple ou impératif : <em>Si tu viens, nous serons contents.</em></li></ul>"},
                {"heading": "b) Imaginaire (présent)", "body": "<ul><li>si + imparfait, conditionnel présent : <em>Si j'avais plus de temps, je voyagerais.</em></li></ul>"},
                {"heading": "c) Manquée (passé)", "body": "<ul><li>si + plus-que-parfait, conditionnel passé : <em>Si j'avais su, je serais venu.</em></li></ul>"},
                {"heading": "d) Règle d'or", "body": "<ul><li>Jamais de futur ni de conditionnel directement après si.</li></ul>"},
            ],
            "examples": [
                "Si tu viens, nous serons contents.",
                "Si tu as faim, mange quelque chose !",
                "Si j'avais plus de temps, je voyagerais davantage.",
                "Si elle parlait mieux anglais, elle trouverait un meilleur travail.",
                "Si j'avais su, je serais venu plus tôt.",
                "Si nous gagnions au loto, nous achèterions une maison.",
                "Si tu étudies, tu réussiras.",
            ],
            "commonMistakes": [
                {"wrong": "Si tu viendras, nous serons contents.", "right": "Si tu viens, nous serons contents.", "why": "Le verbe juste après si n'est jamais au futur, seulement au présent."},
                {"wrong": "Si j'aurais plus de temps, je voyagerais.", "right": "Si j'avais plus de temps, je voyagerais.", "why": "Après si pour une hypothèse imaginaire, on utilise l'imparfait, jamais le conditionnel."},
                {"wrong": "Si j'avais su, je viendrais.", "right": "Si j'avais su, je serais venu.", "why": "Après si + plus-que-parfait, la principale est au conditionnel passé, pas au conditionnel présent."},
            ],
        },
        "exercises": [
            {"id": "b1hyp-fill", "type": "fill-blank", "title": "Complète l'Hypothèse",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b1hypf1", "prompt": "Si tu ___ (venir), nous serons contents.", "answers": [["viens"]], "options": ["viens", "viendras", "venais"], "explanation": "Hypothèse réalisable : si + présent."},
                {"id": "b1hypf2", "prompt": "Si j'___ (avoir) plus de temps, je voyagerais.", "answers": [["avais"]], "options": ["avais", "aurais", "ai"], "explanation": "Hypothèse imaginaire : si + imparfait."},
                {"id": "b1hypf3", "prompt": "Si elle ___ (parler) mieux anglais, elle trouverait un meilleur travail.", "answers": [["parlait"]], "options": ["parlait", "parlerait", "parle"], "explanation": "Hypothèse imaginaire : si + imparfait."},
                {"id": "b1hypf4", "prompt": "Si tu ___ (étudier), tu réussiras.", "answers": [["étudies"]], "options": ["étudies", "étudieras", "étudiais"], "explanation": "Hypothèse réalisable : si + présent."},
             ]},
            {"id": "b1hyp-mc", "type": "multiple-choice", "title": "L'Hypothèse avec Si",
             "items": [
                {"id": "b1hypm1", "prompt": "Quel temps suit si pour une hypothèse réalisable ?", "options": ["le présent", "le futur", "l'imparfait"], "answerIndex": 0, "explanation": "Si + présent pour une hypothèse réalisable."},
                {"id": "b1hypm2", "prompt": "Quel temps utilise-t-on dans la principale pour une hypothèse imaginaire au présent ?", "options": ["le conditionnel présent", "le futur simple", "le conditionnel passé"], "answerIndex": 0, "explanation": "Si + imparfait, conditionnel présent."},
                {"id": "b1hypm3", "prompt": "Quel temps n'utilise-t-on jamais directement après si ?", "options": ["le futur ou le conditionnel", "le présent", "l'imparfait"], "answerIndex": 0, "explanation": "Le futur et le conditionnel sont exclus juste après si."},
                {"id": "b1hypm4", "prompt": "Quelle structure exprime une hypothèse déjà manquée dans le passé ?", "options": ["si + plus-que-parfait, conditionnel passé", "si + imparfait, conditionnel présent", "si + présent, futur"], "answerIndex": 0, "explanation": "C'est la structure du regret ou de l'occasion manquée."},
             ]},
            {"id": "b1hyp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1hypc1", "incorrect": "Si tu viendras, nous serons contents.", "answer": ["Si tu viens, nous serons contents."], "explanation": "Jamais de futur juste après si."},
                {"id": "b1hypc2", "incorrect": "Si j'aurais plus de temps, je voyagerais.", "answer": ["Si j'avais plus de temps, je voyagerais."], "explanation": "Jamais de conditionnel juste après si."},
                {"id": "b1hypc3", "incorrect": "Si j'avais su, je viendrais.", "answer": ["Si j'avais su, je serais venu."], "explanation": "Après si + plus-que-parfait : conditionnel passé."},
             ]},
        ],
        "summary": [
            "Si + présent, futur/impératif exprime une hypothèse réalisable.",
            "Si + imparfait, conditionnel présent exprime une hypothèse imaginaire dans le présent.",
            "Si + plus-que-parfait, conditionnel passé exprime une hypothèse déjà manquée dans le passé ; le verbe après si n'est jamais au futur ni au conditionnel.",
        ],
    },
    {
        "id": "b1-les-verbes-suivis-de-a-ou-de-infinitif",
        "level": "B1", "unit": "1", "order": 12, "skill": "grammar", "strand": "verbes-a-de-infinitif",
        "title": "Les Verbes Suivis de à ou de + Infinitif",
        "subtitle": "Commencer à, décider de, ou l'infinitif direct : trois constructions à mémoriser verbe par verbe.",
        "objectives": [
            "Reconnaître les verbes qui se construisent avec à + infinitif.",
            "Reconnaître les verbes qui se construisent avec de + infinitif.",
            "Distinguer ces verbes des verbes qui se construisent avec l'infinitif direct, sans préposition.",
        ],
        "content": {
            "intro": "Beaucoup de verbes français se combinent avec un deuxième verbe à l'infinitif, mais pas toujours de la même façon — certains demandent à, d'autres de, et d'autres aucune préposition du tout.",
            "explanation": "<p>Certains verbes très fréquents se construisent avec <strong>à</strong> + infinitif : <em>commencer à, réussir à, apprendre à, aider à, continuer à</em> : <em>Elle commence à comprendre.</em> D'autres se construisent avec <strong>de</strong> + infinitif : <em>décider de, essayer de, arrêter de, finir de, oublier de, avoir peur de</em> : <em>J'ai décidé de partir.</em></p><p>D'autres verbes très courants (souvent des verbes de modalité) prennent l'infinitif directement, sans aucune préposition : <em>vouloir, pouvoir, devoir, aimer, préférer, détester</em> : <em>Je veux partir. Il peut venir.</em> Il n'existe pas de règle générale pour prédire quelle préposition un verbe utilise : c'est un point de vocabulaire à mémoriser verbe par verbe.</p>",
            "rules": [
                {"heading": "a) Verbes + à + infinitif", "body": "<ul><li><em>commencer à, réussir à, apprendre à, aider à, continuer à</em>.</li></ul>"},
                {"heading": "b) Verbes + de + infinitif", "body": "<ul><li><em>décider de, essayer de, arrêter de, finir de, oublier de, avoir peur de</em>.</li></ul>"},
                {"heading": "c) Infinitif direct", "body": "<ul><li><em>vouloir, pouvoir, devoir, aimer, préférer, détester</em> — sans préposition.</li></ul>"},
                {"heading": "d) Pas de règle générale", "body": "<ul><li>Chaque verbe se mémorise avec sa propre construction.</li></ul>"},
            ],
            "examples": [
                "Elle commence à comprendre le français.",
                "J'ai décidé de partir plus tôt.",
                "Il a réussi à finir à temps.",
                "Nous essayons de trouver une solution.",
                "Tu veux venir avec nous ?",
                "Ils ont arrêté de fumer.",
                "Elle apprend à conduire.",
            ],
            "commonMistakes": [
                {"wrong": "Elle commence de comprendre.", "right": "Elle commence à comprendre.", "why": "Commencer se construit avec à, pas de."},
                {"wrong": "J'ai décidé à partir.", "right": "J'ai décidé de partir.", "why": "Décider se construit avec de, pas à."},
                {"wrong": "Je veux à partir.", "right": "Je veux partir.", "why": "Vouloir prend l'infinitif directement, sans préposition."},
            ],
        },
        "exercises": [
            {"id": "b1vsi-fill", "type": "fill-blank", "title": "Complète avec la Bonne Préposition",
             "instructions": "Choisis à, de, ou aucune préposition.",
             "items": [
                {"id": "b1vsif1", "prompt": "Elle commence ___ comprendre le français.", "answers": [["à"]], "options": ["à", "de", "(rien)"], "explanation": "Commencer à + infinitif."},
                {"id": "b1vsif2", "prompt": "J'ai décidé ___ partir plus tôt.", "answers": [["de"]], "options": ["de", "à", "(rien)"], "explanation": "Décider de + infinitif."},
                {"id": "b1vsif3", "prompt": "Ils ont arrêté ___ fumer.", "answers": [["de"]], "options": ["de", "à", "(rien)"], "explanation": "Arrêter de + infinitif."},
                {"id": "b1vsif4", "prompt": "Elle apprend ___ conduire.", "answers": [["à"]], "options": ["à", "de", "(rien)"], "explanation": "Apprendre à + infinitif."},
             ]},
            {"id": "b1vsi-mc", "type": "multiple-choice", "title": "Les Verbes et Leur Préposition",
             "items": [
                {"id": "b1vsim1", "prompt": "Quelle préposition suit « commencer » devant un infinitif ?", "options": ["à", "de", "aucune"], "answerIndex": 0, "explanation": "Commencer à + infinitif."},
                {"id": "b1vsim2", "prompt": "Quelle préposition suit « décider » devant un infinitif ?", "options": ["de", "à", "aucune"], "answerIndex": 0, "explanation": "Décider de + infinitif."},
                {"id": "b1vsim3", "prompt": "Quelle préposition suit « vouloir » devant un infinitif ?", "options": ["aucune, infinitif direct", "à", "de"], "answerIndex": 0, "explanation": "Vouloir prend l'infinitif direct."},
                {"id": "b1vsim4", "prompt": "Existe-t-il une règle générale pour prédire à ou de ?", "options": ["non, cela se mémorise verbe par verbe", "oui, toujours à", "oui, toujours de"], "answerIndex": 0, "explanation": "Chaque verbe a sa propre construction à mémoriser."},
             ]},
            {"id": "b1vsi-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b1vsic1", "incorrect": "Elle commence de comprendre.", "answer": ["Elle commence à comprendre."], "explanation": "Commencer se construit avec à."},
                {"id": "b1vsic2", "incorrect": "J'ai décidé à partir.", "answer": ["J'ai décidé de partir."], "explanation": "Décider se construit avec de."},
                {"id": "b1vsic3", "incorrect": "Je veux à partir.", "answer": ["Je veux partir."], "explanation": "Vouloir prend l'infinitif direct."},
             ]},
        ],
        "summary": [
            "Certains verbes prennent à + infinitif (commencer à, réussir à, apprendre à).",
            "D'autres prennent de + infinitif (décider de, essayer de, arrêter de).",
            "D'autres prennent l'infinitif directement, sans préposition (vouloir, pouvoir, devoir, aimer) ; il n'y a pas de règle générale, chaque verbe se mémorise.",
        ],
    },
]

EXTRA_EXERCISES = {
    "b1-le-plus-que-parfait": [
        {"id": "b1pqpx-reading", "type": "reading-comprehension", "title": "Lecture : Le Train Manqué",
         "passage": "<p>Quand Léa est arrivée à la gare, le train était déjà parti. Elle avait couru pendant dix minutes, mais ce n'était pas assez. Ses amis l'avaient attendue un moment, puis ils étaient montés dans le train sans elle. Heureusement, elle avait gardé son billet pour le train suivant.</p>",
         "items": [
            {"id": "b1pqpxr1", "prompt": "Qu'est-ce qui s'était passé quand Léa est arrivée ?", "options": ["Le train était déjà parti", "Le train était en retard", "Le train n'était pas encore là"], "answerIndex": 0, "explanation": "Le texte dit : « le train était déjà parti »."},
            {"id": "b1pqpxr2", "prompt": "Qu'avait-elle fait pendant dix minutes ?", "options": ["Elle avait couru", "Elle avait attendu", "Elle avait téléphoné"], "answerIndex": 0, "explanation": "Le texte dit : « Elle avait couru pendant dix minutes »."},
            {"id": "b1pqpxr3", "prompt": "Qu'avaient fait ses amis ?", "options": ["Ils étaient montés dans le train sans elle", "Ils l'avaient attendue toute la journée", "Ils étaient repartis chez eux"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1pqpxr4", "prompt": "Qu'avait-elle gardé ?", "options": ["Son billet pour le train suivant", "Son sac", "Son téléphone"], "answerIndex": 0, "explanation": "Le texte se termine par « elle avait gardé son billet »."},
         ]},
        {"id": "b1pqpx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1pqpxo1", "prompt": "Remets les mots en ordre.", "words": ["Le", "train", "était", "déjà", "parti"], "explanation": "Plus-que-parfait avec être, accord au masculin."},
            {"id": "b1pqpxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "avait", "couru", "pendant", "dix", "minutes"], "explanation": "Plus-que-parfait avec avoir."},
         ]},
    ],
    "b1-le-conditionnel-passe": [
        {"id": "b1cpax-reading", "type": "reading-comprehension", "title": "Lecture : Le Regret de Camille",
         "passage": "<p>Si Camille avait révisé plus, elle aurait réussi son examen. Elle se dit qu'elle aurait dû commencer plus tôt. Ses amis lui avaient proposé de l'aide, mais elle avait refusé. Maintenant, elle regrette de ne pas avoir accepté.</p>",
         "items": [
            {"id": "b1cpaxr1", "prompt": "Qu'aurait fait Camille si elle avait révisé plus ?", "options": ["Elle aurait réussi son examen", "Elle aurait échoué quand même", "Elle n'aurait rien changé"], "answerIndex": 0, "explanation": "Le texte dit : « elle aurait réussi son examen »."},
            {"id": "b1cpaxr2", "prompt": "Que se dit-elle maintenant ?", "options": ["Qu'elle aurait dû commencer plus tôt", "Qu'elle a bien fait", "Qu'elle recommencera l'année prochaine"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1cpaxr3", "prompt": "Qu'avaient proposé ses amis ?", "options": ["De l'aide", "De l'argent", "Un livre"], "answerIndex": 0, "explanation": "Le texte dit : « Ses amis lui avaient proposé de l'aide »."},
            {"id": "b1cpaxr4", "prompt": "Que regrette-t-elle maintenant ?", "options": ["De ne pas avoir accepté l'aide", "D'avoir accepté l'aide", "D'avoir trop étudié"], "answerIndex": 0, "explanation": "Le texte se termine par « elle regrette de ne pas avoir accepté »."},
         ]},
        {"id": "b1cpax-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1cpaxo1", "prompt": "Remets les mots en ordre.", "words": ["Elle", "aurait", "dû", "commencer", "plus", "tôt"], "explanation": "Conditionnel passé de devoir : regret."},
            {"id": "b1cpaxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "aurait", "réussi", "son", "examen"], "explanation": "Conditionnel passé, hypothèse non réalisée."},
         ]},
    ],
    "b1-le-subjonctif-present-formation": [
        {"id": "b1sbfx-reading", "type": "reading-comprehension", "title": "Lecture : Les Consignes du Professeur",
         "passage": "<p>Le professeur dit : « Il faut que vous finissiez vos exercices avant vendredi. Je veux que tout le monde soit prêt pour l'examen. Il faut aussi que chacun sache les verbes irréguliers. » Les étudiants promettent de faire de leur mieux.</p>",
         "items": [
            {"id": "b1sbfxr1", "prompt": "Que faut-il finir avant vendredi ?", "options": ["Les exercices", "Le livre", "Le projet"], "answerIndex": 0, "explanation": "Le texte dit : « il faut que vous finissiez vos exercices »."},
            {"id": "b1sbfxr2", "prompt": "Que veut le professeur pour l'examen ?", "options": ["Que tout le monde soit prêt", "Que personne ne vienne", "Que l'examen soit reporté"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1sbfxr3", "prompt": "Que faut-il savoir ?", "options": ["Les verbes irréguliers", "Le vocabulaire de la cuisine", "L'histoire de France"], "answerIndex": 0, "explanation": "Le texte dit : « il faut aussi que chacun sache les verbes irréguliers »."},
            {"id": "b1sbfxr4", "prompt": "Que promettent les étudiants ?", "options": ["De faire de leur mieux", "De ne rien faire", "De changer de classe"], "answerIndex": 0, "explanation": "Le texte se termine ainsi."},
         ]},
        {"id": "b1sbfx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1sbfxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "faut", "que", "vous", "finissiez", "vos", "exercices"], "explanation": "Subjonctif après il faut que."},
            {"id": "b1sbfxo2", "prompt": "Remets les mots en ordre.", "words": ["Je", "veux", "que", "tout", "le", "monde", "soit", "prêt"], "explanation": "Subjonctif irrégulier de être après vouloir que."},
         ]},
    ],
    "b1-subjonctif-vs-indicatif": [
        {"id": "b1svix-reading", "type": "reading-comprehension", "title": "Lecture : Avant le Match",
         "passage": "<p>Marc pense que son équipe va gagner le match. Mais son ami doute qu'elle réussisse, car les joueurs sont fatigués. Marc est content que le match ait lieu ce soir. Il est certain que ce sera un bon spectacle.</p>",
         "items": [
            {"id": "b1svixr1", "prompt": "Que pense Marc de son équipe ?", "options": ["Qu'elle va gagner", "Qu'elle va perdre", "Qu'elle ne jouera pas"], "answerIndex": 0, "explanation": "Le texte dit : « Marc pense que son équipe va gagner »."},
            {"id": "b1svixr2", "prompt": "De quoi doute son ami ?", "options": ["Qu'elle réussisse", "Qu'elle soit fatiguée", "Que le match ait lieu"], "answerIndex": 0, "explanation": "Le texte dit : « son ami doute qu'elle réussisse »."},
            {"id": "b1svixr3", "prompt": "De quoi Marc est-il content ?", "options": ["Que le match ait lieu ce soir", "Que les joueurs soient fatigués", "Que le match soit annulé"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1svixr4", "prompt": "De quoi est-il certain ?", "options": ["Que ce sera un bon spectacle", "Que son équipe perdra", "Que le match sera annulé"], "answerIndex": 0, "explanation": "Le texte se termine ainsi."},
         ]},
        {"id": "b1svix-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1svixo1", "prompt": "Remets les mots en ordre.", "words": ["Marc", "pense", "que", "son", "équipe", "va", "gagner"], "explanation": "Indicatif après penser que affirmatif."},
            {"id": "b1svixo2", "prompt": "Remets les mots en ordre.", "words": ["Son", "ami", "doute", "qu'elle", "réussisse"], "explanation": "Subjonctif après douter que."},
         ]},
    ],
    "b1-le-discours-indirect": [
        {"id": "b1disx-reading", "type": "reading-comprehension", "title": "Lecture : Paul Est Malade",
         "passage": "<p>Paul a dit qu'il était malade et qu'il ne pouvait pas venir au bureau. Il a expliqué qu'il avait de la fièvre depuis la veille. Sa collègue lui a demandé s'il avait vu un médecin. Il a répondu qu'il irait le lendemain.</p>",
         "items": [
            {"id": "b1disxr1", "prompt": "Qu'a dit Paul ?", "options": ["Qu'il était malade", "Qu'il était en vacances", "Qu'il avait déménagé"], "answerIndex": 0, "explanation": "Le texte dit : « Paul a dit qu'il était malade »."},
            {"id": "b1disxr2", "prompt": "Depuis quand avait-il de la fièvre ?", "options": ["Depuis la veille", "Depuis une semaine", "Depuis le matin même"], "answerIndex": 0, "explanation": "Le texte dit : « il avait de la fièvre depuis la veille »."},
            {"id": "b1disxr3", "prompt": "Que lui a demandé sa collègue ?", "options": ["S'il avait vu un médecin", "S'il voulait démissionner", "S'il avait mangé"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1disxr4", "prompt": "Qu'a-t-il répondu ?", "options": ["Qu'il irait le lendemain", "Qu'il n'irait jamais", "Qu'il était déjà allé chez le médecin"], "answerIndex": 0, "explanation": "Le texte se termine ainsi."},
         ]},
        {"id": "b1disx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1disxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "a", "dit", "qu'il", "était", "malade"], "explanation": "Concordance des temps : présent → imparfait."},
            {"id": "b1disxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "a", "répondu", "qu'il", "irait", "le", "lendemain"], "explanation": "Futur → conditionnel présent au discours indirect passé."},
         ]},
    ],
    "b1-les-pronoms-relatifs": [
        {"id": "b1relx-reading", "type": "reading-comprehension", "title": "Lecture : Un Collègue Polyglotte",
         "passage": "<p>J'ai un collègue qui parle quatre langues. Le projet que nous préparons est très important. Le bureau où je travaille est au troisième étage. C'est un sujet dont nous parlons souvent en réunion.</p>",
         "items": [
            {"id": "b1relxr1", "prompt": "Combien de langues parle le collègue ?", "options": ["Quatre", "Deux", "Trois"], "answerIndex": 0, "explanation": "Le texte dit : « qui parle quatre langues »."},
            {"id": "b1relxr2", "prompt": "Comment est le projet qu'ils préparent ?", "options": ["Très important", "Sans intérêt", "Presque terminé"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1relxr3", "prompt": "Où est le bureau ?", "options": ["Au troisième étage", "Au rez-de-chaussée", "Au dernier étage"], "answerIndex": 0, "explanation": "Le texte dit : « au troisième étage »."},
            {"id": "b1relxr4", "prompt": "De quoi parlent-ils souvent en réunion ?", "options": ["D'un sujet important", "De la météo", "De leurs vacances"], "answerIndex": 0, "explanation": "Le texte se termine par « un sujet dont nous parlons souvent »."},
         ]},
        {"id": "b1relx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1relxo1", "prompt": "Remets les mots en ordre.", "words": ["J'ai", "un", "collègue", "qui", "parle", "quatre", "langues"], "explanation": "Qui remplace le sujet."},
            {"id": "b1relxo2", "prompt": "Remets les mots en ordre.", "words": ["Le", "projet", "que", "nous", "préparons", "est", "important"], "explanation": "Que remplace le complément d'objet direct."},
         ]},
    ],
    "b1-la-voix-passive": [
        {"id": "b1pasx-reading", "type": "reading-comprehension", "title": "Lecture : Un Tableau Célèbre",
         "passage": "<p>Ce tableau a été peint par un artiste célèbre. Il a été vendu très cher l'année dernière. Aujourd'hui, il est exposé dans un grand musée. On dit qu'il sera bientôt prêté à une exposition internationale.</p>",
         "items": [
            {"id": "b1pasxr1", "prompt": "Par qui ce tableau a-t-il été peint ?", "options": ["Par un artiste célèbre", "Par un inconnu", "Par plusieurs artistes"], "answerIndex": 0, "explanation": "Le texte dit : « peint par un artiste célèbre »."},
            {"id": "b1pasxr2", "prompt": "Quand a-t-il été vendu très cher ?", "options": ["L'année dernière", "Le mois dernier", "Il y a dix ans"], "answerIndex": 0, "explanation": "Le texte dit : « vendu très cher l'année dernière »."},
            {"id": "b1pasxr3", "prompt": "Où est-il exposé aujourd'hui ?", "options": ["Dans un grand musée", "Chez un collectionneur privé", "Dans une galerie fermée"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1pasxr4", "prompt": "Que dit-on à son sujet ?", "options": ["Qu'il sera bientôt prêté à une exposition", "Qu'il sera vendu à nouveau", "Qu'il sera détruit"], "answerIndex": 0, "explanation": "Le texte se termine ainsi."},
         ]},
        {"id": "b1pasx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1pasxo1", "prompt": "Remets les mots en ordre.", "words": ["Ce", "tableau", "a", "été", "peint", "par", "un", "artiste"], "explanation": "Passif : être + participe passé + par."},
            {"id": "b1pasxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "est", "exposé", "dans", "un", "grand", "musée"], "explanation": "Passif au présent."},
         ]},
    ],
    "b1-les-connecteurs-logiques": [
        {"id": "b1conx-reading", "type": "reading-comprehension", "title": "Lecture : Léo et Son Projet",
         "passage": "<p>Léo est fatigué, pourtant il continue à travailler. Il travaille beaucoup parce qu'il veut finir le projet à temps. Il a donc peu de temps libre. Il fait des efforts afin de réussir avant la date limite.</p>",
         "items": [
            {"id": "b1conxr1", "prompt": "Que fait Léo malgré sa fatigue ?", "options": ["Il continue à travailler", "Il arrête de travailler", "Il se repose"], "answerIndex": 0, "explanation": "Le texte dit : « pourtant il continue à travailler »."},
            {"id": "b1conxr2", "prompt": "Pourquoi travaille-t-il beaucoup ?", "options": ["Parce qu'il veut finir le projet à temps", "Parce qu'il s'ennuie", "Parce qu'on l'y oblige"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1conxr3", "prompt": "Quelle est la conséquence de son travail ?", "options": ["Il a peu de temps libre", "Il a beaucoup de temps libre", "Il ne travaille plus du tout"], "answerIndex": 0, "explanation": "Le texte dit : « Il a donc peu de temps libre »."},
            {"id": "b1conxr4", "prompt": "Dans quel but fait-il des efforts ?", "options": ["Afin de réussir avant la date limite", "Afin de gagner plus d'argent", "Afin de changer de projet"], "answerIndex": 0, "explanation": "Le texte se termine ainsi."},
         ]},
        {"id": "b1conx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1conxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "travaille", "beaucoup", "parce", "qu'il", "veut", "finir", "le", "projet"], "explanation": "Cause avec parce que."},
            {"id": "b1conxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "fait", "des", "efforts", "afin", "de", "réussir"], "explanation": "But avec afin de + infinitif."},
         ]},
    ],
    "b1-le-gerondif-et-le-participe-present": [
        {"id": "b1gerx-reading", "type": "reading-comprehension", "title": "Lecture : Le Roman de Sophie",
         "passage": "<p>En travaillant tous les soirs, Sophie a fini son roman. Sachant que le temps pressait, elle a écrit vite. Elle a réussi en persévérant, même les jours difficiles. Ayant terminé, elle a célébré avec ses amis.</p>",
         "items": [
            {"id": "b1gerxr1", "prompt": "Comment Sophie a-t-elle fini son roman ?", "options": ["En travaillant tous les soirs", "En dormant beaucoup", "En arrêtant souvent"], "answerIndex": 0, "explanation": "Le texte dit : « En travaillant tous les soirs »."},
            {"id": "b1gerxr2", "prompt": "Pourquoi a-t-elle écrit vite ?", "options": ["Parce qu'elle savait que le temps pressait", "Parce qu'elle s'ennuyait", "Parce qu'on le lui a demandé"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1gerxr3", "prompt": "Comment a-t-elle réussi ?", "options": ["En persévérant", "Par chance", "Sans effort"], "answerIndex": 0, "explanation": "Le texte dit : « Elle a réussi en persévérant »."},
            {"id": "b1gerxr4", "prompt": "Qu'a-t-elle fait après avoir terminé ?", "options": ["Elle a célébré avec ses amis", "Elle a recommencé un autre roman", "Elle s'est reposée seule"], "answerIndex": 0, "explanation": "Le texte se termine ainsi."},
         ]},
        {"id": "b1gerx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1gerxo1", "prompt": "Remets les mots en ordre.", "words": ["En", "travaillant", "tous", "les", "soirs", "elle", "a", "fini"], "explanation": "Gérondif : simultanéité."},
            {"id": "b1gerxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "a", "réussi", "en", "persévérant"], "explanation": "Gérondif : manière."},
         ]},
    ],
    "b1-les-doubles-pronoms": [
        {"id": "b1dbpx-reading", "type": "reading-comprehension", "title": "Lecture : Le Livre Rendu",
         "passage": "<p>Marie a demandé son livre à Paul. Il le lui a rendu tout de suite. Ensuite, elle lui a redonné son stylo : elle le lui a redonné avec un sourire. « Donne-le-moi », avait-elle dit au début, en riant.</p>",
         "items": [
            {"id": "b1dbpxr1", "prompt": "Qu'a fait Paul avec le livre ?", "options": ["Il l'a rendu tout de suite", "Il l'a gardé", "Il l'a perdu"], "answerIndex": 0, "explanation": "Le texte dit : « Il le lui a rendu tout de suite »."},
            {"id": "b1dbpxr2", "prompt": "Qu'a fait Marie avec le stylo ?", "options": ["Elle l'a redonné", "Elle l'a jeté", "Elle l'a gardé"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1dbpxr3", "prompt": "Comment l'a-t-elle redonné ?", "options": ["Avec un sourire", "En colère", "Sans un mot"], "answerIndex": 0, "explanation": "Le texte dit : « avec un sourire »."},
            {"id": "b1dbpxr4", "prompt": "Qu'avait-elle dit au début ?", "options": ["« Donne-le-moi »", "« Garde-le »", "« Je n'en veux pas »"], "answerIndex": 0, "explanation": "Le texte se termine ainsi."},
         ]},
        {"id": "b1dbpx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1dbpxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "le", "lui", "a", "rendu", "tout", "de", "suite"], "explanation": "Doubles pronoms : COD avant COI."},
            {"id": "b1dbpxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "le", "lui", "a", "redonné", "avec", "un", "sourire"], "explanation": "Doubles pronoms au passé composé."},
         ]},
    ],
    "b1-lexpression-de-lhypothese-avec-si": [
        {"id": "b1hypx-reading", "type": "reading-comprehension", "title": "Lecture : Des Projets et des Regrets",
         "passage": "<p>Si tu viens ce soir, nous serons ravis. Si j'avais plus de temps libre, je ferais du sport tous les jours. Si elle avait su la vérité plus tôt, elle aurait réagi différemment. Nous espérons vraiment que tu pourras venir.</p>",
         "items": [
            {"id": "b1hypxr1", "prompt": "Que se passera-t-il si tu viens ce soir ?", "options": ["Nous serons ravis", "Nous serons déçus", "Rien de particulier"], "answerIndex": 0, "explanation": "Le texte dit : « nous serons ravis »."},
            {"id": "b1hypxr2", "prompt": "Que ferait la personne si elle avait plus de temps ?", "options": ["Du sport tous les jours", "Rien du tout", "Elle travaillerait plus"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1hypxr3", "prompt": "Qu'aurait fait la personne si elle avait su la vérité plus tôt ?", "options": ["Elle aurait réagi différemment", "Elle n'aurait rien changé", "Elle serait partie"], "answerIndex": 0, "explanation": "Le texte dit : « elle aurait réagi différemment »."},
            {"id": "b1hypxr4", "prompt": "Qu'espèrent-ils ?", "options": ["Que tu pourras venir", "Que tu ne viendras pas", "Qu'il fera beau"], "answerIndex": 0, "explanation": "Le texte se termine ainsi."},
         ]},
        {"id": "b1hypx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1hypxo1", "prompt": "Remets les mots en ordre.", "words": ["Si", "tu", "viens", "ce", "soir", "nous", "serons", "ravis"], "explanation": "Hypothèse réalisable : si + présent."},
            {"id": "b1hypxo2", "prompt": "Remets les mots en ordre.", "words": ["Si", "j'avais", "plus", "de", "temps", "je", "ferais", "du", "sport"], "explanation": "Hypothèse imaginaire : si + imparfait."},
         ]},
    ],
    "b1-les-verbes-suivis-de-a-ou-de-infinitif": [
        {"id": "b1vsix-reading", "type": "reading-comprehension", "title": "Lecture : Emma Apprend le Piano",
         "passage": "<p>Emma a décidé d'apprendre le piano. Elle a commencé à prendre des cours le mois dernier. Elle essaie de pratiquer chaque jour. Elle espère réussir à jouer un morceau entier bientôt.</p>",
         "items": [
            {"id": "b1vsixr1", "prompt": "Qu'a décidé Emma ?", "options": ["D'apprendre le piano", "D'arrêter la musique", "D'apprendre la guitare"], "answerIndex": 0, "explanation": "Le texte dit : « Emma a décidé d'apprendre le piano »."},
            {"id": "b1vsixr2", "prompt": "Quand a-t-elle commencé les cours ?", "options": ["Le mois dernier", "Il y a un an", "Hier"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b1vsixr3", "prompt": "Que fait-elle chaque jour ?", "options": ["Elle essaie de pratiquer", "Elle regarde des vidéos", "Elle ne fait rien"], "answerIndex": 0, "explanation": "Le texte dit : « Elle essaie de pratiquer chaque jour »."},
            {"id": "b1vsixr4", "prompt": "Qu'espère-t-elle bientôt ?", "options": ["Réussir à jouer un morceau entier", "Arrêter le piano", "Changer d'instrument"], "answerIndex": 0, "explanation": "Le texte se termine ainsi."},
         ]},
        {"id": "b1vsix-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b1vsixo1", "prompt": "Remets les mots en ordre.", "words": ["Elle", "a", "commencé", "à", "prendre", "des", "cours"], "explanation": "Commencer à + infinitif."},
            {"id": "b1vsixo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "essaie", "de", "pratiquer", "chaque", "jour"], "explanation": "Essayer de + infinitif."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
