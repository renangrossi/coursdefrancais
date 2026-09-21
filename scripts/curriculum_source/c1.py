# -*- coding: utf-8 -*-
"""C1 — Données du curriculum de niveau avancé. Voir curriculum/SCHEMA.md
pour la forme exacte du JSON vers lequel ceci est compilé
(scripts/generate_curriculum.py fait la compilation). Écrit en Python
plutôt qu'en JSON à la main pour que le HTML en ligne (rules[].body,
content.explanation) et les guillemets dans le texte puissent s'écrire
naturellement."""

OVERVIEW = (
    "Le niveau C1 quitte le terrain de la grammaire nouvelle pour entrer dans "
    "celui de la nuance et du registre : reconnaître le subjonctif imparfait "
    "et plus-que-parfait de la littérature classique, maîtriser les quatre "
    "types de phrases conditionnelles complexes, affiner l'emploi du "
    "subjonctif selon le degré de certitude, construire des mises en relief "
    "littéraires, écrire dans un style académique nominalisé et impersonnel, "
    "rapporter un discours avec toute la concordance des temps, employer des "
    "locutions prépositives soutenues, organiser un texte argumentatif "
    "cohérent, distinguer les registres à l'écrit, et exprimer la "
    "restriction et l'exception avec précision. À la fin de ce niveau, tu "
    "liras et écriras un français proche du natif, dans n'importe quel "
    "registre."
)

LESSONS = [
    {
        "id": "c1-le-subjonctif-imparfait-et-plus-que-parfait",
        "level": "C1", "unit": "1", "order": 1, "skill": "grammar", "strand": "subjonctif-litteraire",
        "title": "Le Subjonctif Imparfait et le Subjonctif Plus-que-parfait",
        "subtitle": "Reconnaître les formes littéraires du subjonctif, aujourd'hui réservées à l'écrit très soutenu.",
        "objectives": [
            "Reconnaître la formation du subjonctif imparfait à partir du radical du passé simple.",
            "Reconnaître la formation du subjonctif plus-que-parfait comme équivalent littéraire du conditionnel passé.",
            "Situer ces formes dans leur contexte d'usage réel : littérature classique et registre très soutenu, jamais à l'oral.",
        ],
        "content": {
            "intro": "Le français littéraire conserve deux temps du subjonctif que la langue courante a abandonnés depuis longtemps : les reconnaître à la lecture est une compétence C1, les produire à l'oral serait une erreur de registre.",
            "explanation": "<p>Le <strong>subjonctif imparfait</strong> se forme sur le radical du passé simple + des terminaisons propres (<em>que je parlasse, que tu finisses, qu'il parlât, que nous eussions</em>). Sa marque la plus reconnaissable est l'<strong>accent circonflexe</strong> à la troisième personne du singulier : <em>qu'il fût, qu'il eût, qu'il parlât</em> — sans cet accent, on aurait la forme du passé simple (<em>il fut, il eut, il parla</em>).</p><p>Le <strong>subjonctif plus-que-parfait</strong> se forme avec le subjonctif imparfait de <em>avoir</em>/<em>être</em> + participe passé : <em>qu'il eût parlé, qu'elle fût partie</em>. Dans la prose classique, il remplace souvent le conditionnel passé après <em>si</em> : <em>Si j'eusse su, je ne serais pas venu</em> équivaut à <em>Si j'avais su, je ne serais pas venu</em>. Aujourd'hui, ces deux temps sont vivants uniquement à l'écrit littéraire soutenu ; la langue courante, même très correcte, les remplace par le subjonctif présent et le subjonctif passé.</p>",
            "rules": [
                {"heading": "a) Formation du subjonctif imparfait", "body": "<ul><li>Radical du passé simple + terminaisons : <em>que je parlasse, qu'il parlât, que nous parlassions</em>.</li></ul>"},
                {"heading": "b) Formation du subjonctif plus-que-parfait", "body": "<ul><li>Subjonctif imparfait de avoir/être + participe passé : <em>qu'il eût fini, qu'elle fût venue</em>.</li></ul>"},
                {"heading": "c) La marque de la 3e personne du singulier", "body": "<ul><li>L'accent circonflexe distingue le subjonctif du passé simple : <em>qu'il fût</em> (subjonctif) contre <em>il fut</em> (passé simple).</li></ul>"},
                {"heading": "d) Usage réel aujourd'hui", "body": "<ul><li>Littérature classique, concordance des temps littéraire, style très soutenu — jamais à l'oral ni à l'écrit courant.</li></ul>"},
            ],
            "examples": [
                "Il fallait qu'il partît avant l'aube.",
                "Bien qu'elle fût fatiguée, elle continua son chemin.",
                "Il eût fallu que nous fussions plus prudents.",
                "Quoiqu'il eût terminé son travail, il resta au bureau.",
                "Elle souhaitait qu'il vînt la voir avant son départ.",
                "Il semblait que la situation se fût aggravée pendant la nuit.",
                "Si j'eusse su, je ne serais jamais venu.",
            ],
            "commonMistakes": [
                {"wrong": "Dire « il fallait qu'il parte » avec « qu'il partît » dans une conversation ordinaire.", "right": "Réserver « qu'il partît » à la lecture ou à l'écriture littéraire, et dire « qu'il parte » à l'oral.", "why": "Employer le subjonctif imparfait dans une conversation courante sonnerait artificiel, presque comique — ce n'est plus une forme vivante à l'oral."},
                {"wrong": "Confondre « qu'il parla » et « qu'il parlât ».", "right": "Repérer l'accent circonflexe : « il parla » est un passé simple, « qu'il parlât » un subjonctif imparfait.", "why": "Seul l'accent circonflexe distingue les deux formes à la troisième personne du singulier."},
                {"wrong": "Croire que le subjonctif plus-que-parfait a disparu de tout usage écrit.", "right": "Le reconnaître dans les textes classiques et dans certains styles littéraires soutenus contemporains.", "why": "Il reste vivant à l'écrit très soutenu et dans la littérature, même s'il a disparu de l'oral et de l'écrit courant."},
            ],
        },
        "exercises": [
            {"id": "c1sil-fill", "type": "fill-blank", "title": "Reconnais la Forme Littéraire",
             "instructions": "Choisis la forme correspondante en français courant.",
             "items": [
                {"id": "c1silf1", "prompt": "« Il fallait qu'il partît » se dit en français courant : « Il fallait qu'il ___ ».", "answers": [["parte"]], "options": ["parte", "partît", "partit"], "explanation": "Le subjonctif présent remplace le subjonctif imparfait à l'oral moderne."},
                {"id": "c1silf2", "prompt": "« Bien qu'elle fût fatiguée » se dit en français courant : « Bien qu'elle ___ fatiguée ».", "answers": [["soit"]], "options": ["soit", "fût", "était"], "explanation": "Le subjonctif présent de être est soit."},
                {"id": "c1silf3", "prompt": "« Si j'eusse su » se dit en français courant : « Si j'___ su ».", "answers": [["avais"]], "options": ["avais", "eusse", "aurais"], "explanation": "Le plus-que-parfait de l'indicatif remplace le subjonctif plus-que-parfait après si."},
                {"id": "c1silf4", "prompt": "Quelle marque distingue « qu'il fût » du passé simple « il fut » ?", "answers": [["l'accent circonflexe"]], "options": ["l'accent circonflexe", "le u final", "aucune marque"], "explanation": "L'accent circonflexe est la seule différence graphique."},
             ]},
            {"id": "c1sil-mc", "type": "multiple-choice", "title": "Le Subjonctif Imparfait et Plus-que-parfait",
             "items": [
                {"id": "c1silm1", "prompt": "Sur quel radical se forme le subjonctif imparfait ?", "options": ["le radical du passé simple", "le radical du présent", "le radical du futur"], "answerIndex": 0, "explanation": "C'est le radical du passé simple qui sert de base."},
                {"id": "c1silm2", "prompt": "Comment se forme le subjonctif plus-que-parfait ?", "options": ["subjonctif imparfait de avoir/être + participe passé", "subjonctif présent de avoir/être + participe passé", "imparfait de avoir/être + participe passé"], "answerIndex": 0, "explanation": "L'auxiliaire est au subjonctif imparfait."},
                {"id": "c1silm3", "prompt": "Où rencontre-t-on aujourd'hui ces deux temps ?", "options": ["dans la littérature classique et le style très soutenu", "dans les conversations quotidiennes", "uniquement dans les SMS"], "answerIndex": 0, "explanation": "Ce sont des formes littéraires, disparues de l'oral."},
                {"id": "c1silm4", "prompt": "Que remplace souvent le subjonctif plus-que-parfait après si, en style classique ?", "options": ["le conditionnel passé", "le futur antérieur", "le subjonctif présent"], "answerIndex": 0, "explanation": "« Si j'eusse su » équivaut à « si j'avais su »."},
             ]},
            {"id": "c1sil-correction", "type": "correction", "title": "Modernise la Phrase",
             "instructions": "Réécris chaque phrase littéraire en français courant, au subjonctif présent ou passé.",
             "items": [
                {"id": "c1silc1", "incorrect": "Il fallait qu'il partît avant l'aube.", "answer": ["Il fallait qu'il parte avant l'aube."], "explanation": "Le subjonctif présent remplace le subjonctif imparfait à l'oral."},
                {"id": "c1silc2", "incorrect": "Quoiqu'il eût terminé son travail, il resta au bureau.", "answer": ["Quoiqu'il ait terminé son travail, il resta au bureau."], "explanation": "Le subjonctif passé remplace le subjonctif plus-que-parfait."},
                {"id": "c1silc3", "incorrect": "Elle souhaitait qu'il vînt la voir.", "answer": ["Elle souhaitait qu'il vienne la voir."], "explanation": "Le subjonctif présent remplace le subjonctif imparfait."},
             ]},
        ],
        "summary": [
            "Le subjonctif imparfait se forme sur le radical du passé simple ; sa 3e personne du singulier porte un accent circonflexe distinctif.",
            "Le subjonctif plus-que-parfait (auxiliaire au subjonctif imparfait + participe passé) remplace parfois le conditionnel passé en style classique.",
            "Ces deux temps ne survivent qu'à l'écrit littéraire très soutenu ; la langue courante emploie le subjonctif présent et passé à leur place.",
        ],
    },
    {
        "id": "c1-les-quatre-types-de-phrases-conditionnelles-complexes",
        "level": "C1", "unit": "1", "order": 2, "skill": "grammar", "strand": "conditionnelles-complexes",
        "title": "Les Quatre Types de Phrases Conditionnelles Complexes",
        "subtitle": "Réel, potentiel, irréel du passé, et hypothèse mixte : le système complet de si en français.",
        "objectives": [
            "Distinguer les quatre combinaisons de temps possibles après si.",
            "Reconnaître l'hypothèse mixte, où la cause est passée et la conséquence présente.",
            "Éviter les mélanges de temps interdits après si (jamais de conditionnel juste après si).",
        ],
        "content": {
            "intro": "Le système conditionnel français, déjà vu en partie aux niveaux précédents, se complète ici avec un quatrième cas : l'hypothèse à temps mixtes, essentielle pour exprimer des liens complexes entre passé et présent.",
            "explanation": "<p>Le <strong>réel</strong> (si + présent → présent/futur/impératif) exprime une condition réalisable : <em>Si tu viens, nous mangerons ensemble.</em> Le <strong>potentiel</strong> (si + imparfait → conditionnel présent) exprime une hypothèse présente ou future non réalisée : <em>Si j'avais le temps, je viendrais.</em> L'<strong>irréel du passé</strong> (si + plus-que-parfait → conditionnel passé) exprime une hypothèse passée, définitivement non réalisée : <em>Si j'avais su, je serais venu.</em></p><p>Le quatrième cas, l'<strong>hypothèse mixte</strong>, combine si + plus-que-parfait avec un conditionnel <strong>présent</strong> (et non passé) dans la principale, quand la cause est passée mais la conséquence porte sur le présent : <em>Si j'avais réussi mon examen l'an dernier, je serais médecin aujourd'hui</em> — l'échec est passé, mais la conséquence (ne pas être médecin) dure encore aujourd'hui. Dans tous les cas, la règle absolue reste : <strong>jamais de conditionnel juste après si</strong>.</p>",
            "rules": [
                {"heading": "a) Réel", "body": "<ul><li>Si + présent → présent, futur ou impératif : <em>Si tu peux, appelle-moi.</em></li></ul>"},
                {"heading": "b) Potentiel", "body": "<ul><li>Si + imparfait → conditionnel présent : <em>Si j'avais le temps, je viendrais.</em></li></ul>"},
                {"heading": "c) Irréel du passé", "body": "<ul><li>Si + plus-que-parfait → conditionnel passé : <em>Si j'avais su, je serais venu.</em></li></ul>"},
                {"heading": "d) Hypothèse mixte", "body": "<ul><li>Si + plus-que-parfait → conditionnel <strong>présent</strong>, quand la conséquence porte sur le présent : <em>Si j'avais économisé, j'aurais assez d'argent aujourd'hui.</em></li></ul>"},
            ],
            "examples": [
                "Si tu viens ce soir, nous mangerons ensemble.",
                "Si j'avais le temps, je voyagerais davantage.",
                "Si elle avait étudié, elle aurait réussi son examen.",
                "Si nous avions déménagé plus tôt, nous vivrions déjà dans notre nouvelle maison.",
                "Si j'avais pris cette décision à l'époque, ma vie serait différente aujourd'hui.",
                "S'il fait beau demain, nous irons à la plage.",
                "Si tu avais écouté mes conseils, tu ne serais pas dans cette situation maintenant.",
            ],
            "commonMistakes": [
                {"wrong": "Si j'aurais su, je serais venu.", "right": "Si j'avais su, je serais venu.", "why": "On n'emploie jamais le conditionnel directement après si ; c'est le plus-que-parfait qui s'impose ici."},
                {"wrong": "Si j'avais économisé, j'aurais eu assez d'argent aujourd'hui (pour une conséquence présente).", "right": "Si j'avais économisé, j'aurais assez d'argent aujourd'hui.", "why": "Une conséquence portant sur le présent demande le conditionnel présent, pas le conditionnel passé — c'est l'hypothèse mixte."},
                {"wrong": "Si tu viendrais ce soir, nous mangerions ensemble.", "right": "Si tu viens ce soir, nous mangerons ensemble.", "why": "Une condition réalisable (réel) se construit avec si + présent, jamais avec un conditionnel dans la subordonnée."},
            ],
        },
        "exercises": [
            {"id": "c1cond-fill", "type": "fill-blank", "title": "Complète la Phrase Conditionnelle",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "c1condf1", "prompt": "Si j'avais économisé, j'___ (avoir) assez d'argent aujourd'hui.", "answers": [["aurais"]], "options": ["aurais", "aurai", "aurais eu"], "explanation": "Hypothèse mixte : cause passée, conséquence présente → conditionnel présent."},
                {"id": "c1condf2", "prompt": "Si elle avait étudié, elle ___ (réussir) son examen.", "answers": [["aurait réussi"]], "options": ["aurait réussi", "réussirait", "réussira"], "explanation": "Irréel du passé : cause et conséquence passées → conditionnel passé."},
                {"id": "c1condf3", "prompt": "Si tu ___ (venir), nous mangerons ensemble.", "answers": [["viens"]], "options": ["viens", "viendrais", "viendras"], "explanation": "Réel : si + présent."},
                {"id": "c1condf4", "prompt": "Si j'avais le temps, je ___ (voyager) davantage.", "answers": [["voyagerais"]], "options": ["voyagerais", "voyage", "aurais voyagé"], "explanation": "Potentiel : si + imparfait → conditionnel présent."},
             ]},
            {"id": "c1cond-mc", "type": "multiple-choice", "title": "Les Quatre Types de Conditionnelles",
             "items": [
                {"id": "c1condm1", "prompt": "Quel temps suit toujours si dans une hypothèse mixte (cause passée, conséquence présente) ?", "options": ["le plus-que-parfait", "l'imparfait", "le conditionnel"], "answerIndex": 0, "explanation": "La subordonnée reste au plus-que-parfait ; c'est la principale qui change de temps."},
                {"id": "c1condm2", "prompt": "Quel temps de la principale distingue l'hypothèse mixte de l'irréel du passé classique ?", "options": ["le conditionnel présent au lieu du conditionnel passé", "le futur au lieu du présent", "le subjonctif au lieu de l'indicatif"], "answerIndex": 0, "explanation": "C'est la seule différence entre les deux structures."},
                {"id": "c1condm3", "prompt": "Quel temps ne peut jamais suivre si directement ?", "options": ["le conditionnel", "le présent", "le plus-que-parfait"], "answerIndex": 0, "explanation": "Le conditionnel n'apparaît jamais dans la subordonnée introduite par si."},
                {"id": "c1condm4", "prompt": "Quelle combinaison correspond au type « potentiel » ?", "options": ["si + imparfait → conditionnel présent", "si + présent → futur", "si + plus-que-parfait → conditionnel passé"], "answerIndex": 0, "explanation": "C'est la définition du potentiel."},
             ]},
            {"id": "c1cond-ordering", "type": "ordering", "title": "Remets la Phrase en Ordre",
             "items": [
                {"id": "c1condo1", "prompt": "Remets les mots en ordre.", "words": ["Si", "j'avais", "su,", "je", "serais", "venu"], "explanation": "Irréel du passé : si + plus-que-parfait → conditionnel passé."},
                {"id": "c1condo2", "prompt": "Remets les mots en ordre.", "words": ["Si", "j'avais", "économisé,", "j'aurais", "de", "l'argent", "aujourd'hui"], "explanation": "Hypothèse mixte : cause passée, conséquence présente."},
                {"id": "c1condo3", "prompt": "Remets les mots en ordre.", "words": ["Si", "tu", "viens,", "nous", "mangerons", "ensemble"], "explanation": "Réel : si + présent → futur."},
             ]},
        ],
        "summary": [
            "Le réel (si + présent), le potentiel (si + imparfait → conditionnel présent) et l'irréel du passé (si + plus-que-parfait → conditionnel passé) forment le système de base.",
            "L'hypothèse mixte combine si + plus-que-parfait avec un conditionnel présent quand la conséquence porte sur le présent.",
            "Dans tous les cas, le conditionnel n'apparaît jamais directement après si.",
        ],
    },
    {
        "id": "c1-les-nuances-du-subjonctif",
        "level": "C1", "unit": "1", "order": 3, "skill": "grammar", "strand": "nuances-subjonctif",
        "title": "Les Nuances du Subjonctif : Perception, Négation et Degrés de Certitude",
        "subtitle": "Comment la négation, l'interrogation et le degré de certitude font basculer un verbe entre indicatif et subjonctif.",
        "objectives": [
            "Reconnaître que les verbes de perception et de déclaration basculent au subjonctif quand ils sont niés ou interrogés.",
            "Distinguer les degrés de certitude qui déclenchent ou non le subjonctif (il est certain que / il se peut que).",
            "Manier ces nuances pour exprimer un jugement précis sur la réalité d'un fait.",
        ],
        "content": {
            "intro": "Le choix entre indicatif et subjonctif n'est pas toujours fixé par la conjonction elle-même — il dépend souvent du degré de certitude que le locuteur veut exprimer, une nuance typique du niveau C1.",
            "explanation": "<p>Les verbes de perception et de déclaration (<em>penser, croire, trouver, dire, sembler</em>) prennent l'<strong>indicatif</strong> à la forme affirmative, car ils expriment une certitude : <em>Je pense qu'il a raison.</em> À la forme <strong>négative</strong> ou <strong>interrogative</strong>, la certitude s'affaiblit et le <strong>subjonctif</strong> devient possible, voire préféré à l'écrit soutenu : <em>Je ne pense pas qu'il ait raison</em>, <em>Penses-tu qu'il ait raison ?</em> À l'oral courant, l'indicatif reste toutefois fréquent même à la forme négative.</p><p>Le <strong>degré de certitude</strong> de l'expression elle-même compte aussi : <em>il est certain que, il est évident que, il est clair que</em> gardent l'indicatif (certitude totale), tandis que <em>il est possible que, il se peut que, il n'est pas certain que</em> imposent le subjonctif (incertitude). Entre les deux, <em>il est probable que</em> garde l'indicatif (probabilité forte), mais <em>il est peu probable que</em> bascule au subjonctif (incertitude renforcée par la négation).</p>",
            "rules": [
                {"heading": "a) Affirmatif : indicatif", "body": "<ul><li><em>penser, croire, trouver, dire</em> affirmatifs + indicatif : <em>Je crois qu'il vient.</em></li></ul>"},
                {"heading": "b) Négatif/interrogatif : subjonctif possible", "body": "<ul><li>La certitude s'affaiblit : <em>Je ne crois pas qu'il vienne.</em></li></ul>"},
                {"heading": "c) Certitude totale : indicatif", "body": "<ul><li><em>il est certain/évident/clair que</em> + indicatif.</li></ul>"},
                {"heading": "d) Incertitude : subjonctif", "body": "<ul><li><em>il est possible/il se peut/il n'est pas certain que</em> + subjonctif ; <em>il est peu probable que</em> + subjonctif.</li></ul>"},
            ],
            "examples": [
                "Je pense qu'il a raison.",
                "Je ne pense pas qu'il ait raison.",
                "Crois-tu qu'elle vienne ce soir ?",
                "Il est certain qu'elle réussira.",
                "Il est possible qu'elle échoue.",
                "Il est peu probable qu'il pleuve demain.",
                "Il est évident que ce projet fonctionne.",
            ],
            "commonMistakes": [
                {"wrong": "Je ne pense pas qu'il a raison (dans un contexte soutenu).", "right": "Je ne pense pas qu'il ait raison.", "why": "À l'écrit soutenu, la négation d'un verbe d'opinion favorise le subjonctif, car la certitude disparaît."},
                {"wrong": "Il est possible qu'elle échoue (au subjonctif) confondu avec « il est probable qu'elle échouera » (à l'indicatif).", "right": "Il est possible qu'elle échoue / Il est probable qu'elle échouera.", "why": "Possible exprime une simple éventualité (subjonctif) ; probable exprime une forte probabilité (indicatif)."},
                {"wrong": "Il est certain qu'elle réussisse.", "right": "Il est certain qu'elle réussira.", "why": "Certain exprime une certitude totale, donc l'indicatif, jamais le subjonctif."},
            ],
        },
        "exercises": [
            {"id": "c1nuan-fill", "type": "fill-blank", "title": "Choisis le Mode Selon le Degré de Certitude",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "c1nuanf1", "prompt": "Il est certain qu'elle ___ (réussir).", "answers": [["réussira"]], "options": ["réussira", "réussisse", "réussirait"], "explanation": "Certitude totale : indicatif."},
                {"id": "c1nuanf2", "prompt": "Il est possible qu'elle ___ (échouer).", "answers": [["échoue"]], "options": ["échoue", "échouera", "échouerait"], "explanation": "Simple possibilité : subjonctif."},
                {"id": "c1nuanf3", "prompt": "Je ne crois pas qu'il ___ (venir) ce soir.", "answers": [["vienne"]], "options": ["vienne", "vient", "viendra"], "explanation": "Négation d'un verbe d'opinion : subjonctif à l'écrit soutenu."},
                {"id": "c1nuanf4", "prompt": "Il est peu probable qu'il ___ (pleuvoir) demain.", "answers": [["pleuve"]], "options": ["pleuve", "pleuvra", "pleut"], "explanation": "Peu probable renforce l'incertitude : subjonctif."},
             ]},
            {"id": "c1nuan-mc", "type": "multiple-choice", "title": "Les Nuances du Subjonctif",
             "items": [
                {"id": "c1nuanm1", "prompt": "Quel mode suit « il est évident que » ?", "options": ["l'indicatif", "le subjonctif", "le conditionnel"], "answerIndex": 0, "explanation": "Évident exprime une certitude totale."},
                {"id": "c1nuanm2", "prompt": "Que se passe-t-il quand on nie un verbe d'opinion comme penser ?", "options": ["le subjonctif devient possible, la certitude s'affaiblit", "rien ne change", "le verbe passe au futur"], "answerIndex": 0, "explanation": "La négation introduit un doute."},
                {"id": "c1nuanm3", "prompt": "Quel mode suit « il est peu probable que » ?", "options": ["le subjonctif", "l'indicatif", "l'impératif"], "answerIndex": 0, "explanation": "La négation de probable renforce l'incertitude."},
                {"id": "c1nuanm4", "prompt": "Quel mode suit « il est probable que » (sans négation) ?", "options": ["l'indicatif", "le subjonctif", "le conditionnel"], "answerIndex": 0, "explanation": "Une forte probabilité garde l'indicatif."},
             ]},
            {"id": "c1nuan-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "c1nuanc1", "incorrect": "Il est certain qu'elle réussisse.", "answer": ["Il est certain qu'elle réussira."], "explanation": "Certitude totale : indicatif, jamais subjonctif."},
                {"id": "c1nuanc2", "incorrect": "Il est possible qu'elle échouera.", "answer": ["Il est possible qu'elle échoue."], "explanation": "Possible exprime l'incertitude : subjonctif."},
                {"id": "c1nuanc3", "incorrect": "Crois-tu qu'elle vient ce soir ? (dans un contexte soutenu)", "answer": ["Crois-tu qu'elle vienne ce soir ?"], "explanation": "L'interrogation d'un verbe d'opinion favorise le subjonctif à l'écrit soutenu."},
             ]},
        ],
        "summary": [
            "Penser/croire/dire basculent souvent au subjonctif quand ils sont niés ou interrogés, la certitude s'affaiblissant.",
            "Certain/évident/clair gardent l'indicatif (certitude totale) ; possible/il se peut/peu probable imposent le subjonctif (incertitude).",
            "Probable garde l'indicatif, mais peu probable bascule au subjonctif : la négation renforce le doute.",
        ],
    },
    {
        "id": "c1-les-constructions-emphatiques-avancees",
        "level": "C1", "unit": "1", "order": 4, "skill": "grammar", "strand": "emphase-avancee",
        "title": "Les Constructions Emphatiques et de Mise en Relief Avancées",
        "subtitle": "Au-delà de c'est... qui/que : l'inversion littéraire et la dislocation pour un style percutant.",
        "objectives": [
            "Construire une inversion du sujet à valeur stylistique dans une proposition non interrogative.",
            "Utiliser la dislocation (reprise pronominale) pour mettre en avant un élément de la phrase.",
            "Combiner ces procédés avec les tournures c'est... qui/que déjà connues, pour un style plus littéraire.",
        ],
        "content": {
            "intro": "Au niveau C1, la mise en relief dépasse c'est... qui/que : le français littéraire dispose de procédés supplémentaires — l'inversion stylistique et la dislocation — pour souligner un élément ou créer un effet de style.",
            "explanation": "<p>L'<strong>inversion stylistique</strong> place le sujet après le verbe dans une phrase déclarative, souvent après un complément en tête de phrase, pour un effet littéraire : <em>Ainsi parlait le vieux sage</em>, <em>Peut-être viendra-t-il demain</em> (après <em>peut-être</em> en tête de phrase, l'inversion est même obligatoire à l'écrit soutenu). La <strong>dislocation</strong> détache un élément en tête ou en fin de phrase et le reprend par un pronom, pour le mettre en valeur à l'oral comme à l'écrit : <em>Ce livre, je l'ai adoré</em>, <em>Je l'ai adoré, ce livre.</em></p><p>Ces procédés se combinent avec les tournures déjà connues (<em>c'est... qui/que, ce qui/ce que... c'est</em>) pour construire un style riche et nuancé, typique de la presse d'opinion, de l'essai et de la littérature : <em>C'est précisément ce détail, et lui seul, qui a tout changé.</em></p>",
            "rules": [
                {"heading": "a) Inversion après un adverbe en tête de phrase", "body": "<ul><li><em>peut-être, sans doute, aussi</em> (« c'est pourquoi ») en tête → inversion : <em>Peut-être a-t-il raison.</em></li></ul>"},
                {"heading": "b) Inversion littéraire narrative", "body": "<ul><li>Effet de style après un complément : <em>Ainsi commença son aventure.</em></li></ul>"},
                {"heading": "c) Dislocation à gauche", "body": "<ul><li>Élément détaché en tête, repris par un pronom : <em>Ce livre, je l'ai adoré.</em></li></ul>"},
                {"heading": "d) Dislocation à droite", "body": "<ul><li>Élément détaché en fin de phrase, annoncé par un pronom : <em>Je l'ai adoré, ce livre.</em></li></ul>"},
            ],
            "examples": [
                "Peut-être viendra-t-il demain.",
                "Sans doute a-t-elle raison.",
                "Ainsi commença cette longue aventure.",
                "Ce projet, nous y croyons vraiment.",
                "Je ne lui fais plus confiance, à cet homme.",
                "C'est précisément ce détail qui a tout changé.",
                "Aussi décida-t-il de partir sur-le-champ.",
            ],
            "commonMistakes": [
                {"wrong": "Peut-être il viendra demain.", "right": "Peut-être viendra-t-il demain.", "why": "Peut-être en tête de phrase déclarative impose l'inversion du sujet à l'écrit soutenu."},
                {"wrong": "Aussi il décida de partir (avec aussi signifiant « c'est pourquoi »).", "right": "Aussi décida-t-il de partir.", "why": "Aussi en tête de phrase, avec le sens de conséquence, impose aussi l'inversion."},
                {"wrong": "Ce livre je l'ai adoré (sans virgule ni pause).", "right": "Ce livre, je l'ai adoré.", "why": "La dislocation détache l'élément en tête par une virgule, marquant une pause à l'oral."},
            ],
        },
        "exercises": [
            {"id": "c1emp-fill", "type": "fill-blank", "title": "Complète avec l'Inversion Stylistique",
             "instructions": "Réordonne mentalement et choisis la forme correcte.",
             "items": [
                {"id": "c1empf1", "prompt": "Peut-être ___ (avoir)-t-il raison.", "answers": [["a"]], "options": ["a", "il a", "aura"], "explanation": "Peut-être en tête impose l'inversion : peut-être a-t-il raison."},
                {"id": "c1empf2", "prompt": "Sans doute ___ (être)-elle en retard.", "answers": [["est"]], "options": ["est", "elle est", "serait"], "explanation": "Sans doute en tête impose l'inversion."},
                {"id": "c1empf3", "prompt": "Ce projet, nous y ___ (croire) vraiment.", "answers": [["croyons"]], "options": ["croyons", "croyions", "croirons"], "explanation": "Dislocation à gauche, reprise par y, verbe au présent."},
                {"id": "c1empf4", "prompt": "Aussi ___ (décider)-t-il de partir sur-le-champ.", "answers": [["décida"]], "options": ["décida", "il décida", "décidait"], "explanation": "Aussi (= c'est pourquoi) en tête impose l'inversion, ici au passé simple littéraire."},
             ]},
            {"id": "c1emp-mc", "type": "multiple-choice", "title": "Les Constructions Emphatiques Avancées",
             "items": [
                {"id": "c1empm1", "prompt": "Quel adverbe en tête de phrase impose l'inversion du sujet à l'écrit soutenu ?", "options": ["peut-être", "souvent", "maintenant"], "answerIndex": 0, "explanation": "Peut-être, sans doute et aussi (= c'est pourquoi) imposent cette inversion."},
                {"id": "c1empm2", "prompt": "Qu'est-ce que la dislocation à gauche ?", "options": ["un élément détaché en tête, repris par un pronom", "une inversion du sujet", "une négation renforcée"], "answerIndex": 0, "explanation": "C'est la définition de la dislocation à gauche."},
                {"id": "c1empm3", "prompt": "Dans « Je l'ai adoré, ce livre », quel est le procédé ?", "options": ["la dislocation à droite", "l'inversion stylistique", "le subjonctif"], "answerIndex": 0, "explanation": "L'élément est détaché en fin de phrase."},
                {"id": "c1empm4", "prompt": "Dans quels contextes ces procédés sont-ils fréquents ?", "options": ["la presse d'opinion, l'essai, la littérature", "les SMS uniquement", "les formulaires administratifs"], "answerIndex": 0, "explanation": "Ce sont des procédés de style écrit soigné."},
             ]},
            {"id": "c1emp-ordering", "type": "ordering", "title": "Remets la Phrase en Ordre",
             "items": [
                {"id": "c1empo1", "prompt": "Remets les mots en ordre.", "words": ["Peut-être", "a-t-il", "raison"], "explanation": "Inversion obligatoire après peut-être en tête de phrase."},
                {"id": "c1empo2", "prompt": "Remets les mots en ordre.", "words": ["Ce", "livre,", "je", "l'ai", "adoré"], "explanation": "Dislocation à gauche : élément détaché repris par le pronom l'."},
             ]},
        ],
        "summary": [
            "Peut-être, sans doute et aussi (= c'est pourquoi) en tête de phrase imposent l'inversion du sujet à l'écrit soutenu.",
            "La dislocation détache un élément (à gauche ou à droite) et le reprend par un pronom pour le mettre en valeur.",
            "Ces procédés se combinent avec c'est... qui/que pour un style riche, typique de l'essai et de la presse d'opinion.",
        ],
    },
    {
        "id": "c1-la-nominalisation-et-le-style-academique",
        "level": "C1", "unit": "1", "order": 5, "skill": "writing", "strand": "style-academique",
        "title": "La Nominalisation et le Style Académique",
        "subtitle": "Écrire dans un registre impersonnel et nominalisé, celui des rapports, mémoires et articles académiques.",
        "objectives": [
            "Construire des phrases impersonnelles pour effacer la présence du locuteur.",
            "Enchaîner des idées avec les connecteurs propres à l'écrit académique.",
            "Combiner nominalisation, passif et constructions impersonnelles pour un style objectif et condensé.",
        ],
        "content": {
            "intro": "Le style académique français vise l'objectivité : il évite autant que possible le « je », préfère les tournures impersonnelles et nominalisées, et enchaîne ses idées avec des connecteurs précis.",
            "explanation": "<p>Pour éviter le <strong>« je »</strong>, l'écrit académique utilise des constructions <strong>impersonnelles</strong> (<em>il convient de, il importe de, il s'agit de</em>) et le <strong>passif</strong> ou le <strong>pronominal de sens passif</strong> : <em>Cette hypothèse sera examinée</em> plutôt que <em>Nous examinerons cette hypothèse</em> ; <em>Ce phénomène s'explique par…</em> plutôt que <em>On explique ce phénomène par…</em>. La nominalisation (déjà vue au niveau B2) reste l'outil central de ce style : <em>l'analyse des données révèle</em> plutôt que <em>quand on analyse les données, on voit</em>.</p><p>Les connecteurs académiques structurent le raisonnement avec précision : <em>dans un premier temps / dans un second temps</em> pour organiser, <em>il convient de noter que</em> pour introduire une nuance, <em>ce constat amène à s'interroger sur</em> pour enchaîner une nouvelle question, <em>il ressort de cette analyse que</em> pour conclure.</p>",
            "rules": [
                {"heading": "a) Construction impersonnelle", "body": "<ul><li><em>il convient de, il importe de, il s'agit de</em> — évitent le sujet « je ».</li></ul>"},
                {"heading": "b) Passif et pronominal de sens passif", "body": "<ul><li><em>être examiné(e)</em> ou <em>s'expliquer par</em> — effacent l'agent.</li></ul>"},
                {"heading": "c) Nominalisation condensée", "body": "<ul><li><em>l'analyse révèle</em> plutôt qu'une phrase verbale avec « quand on analyse ».</li></ul>"},
                {"heading": "d) Connecteurs académiques", "body": "<ul><li><em>dans un premier temps, il convient de noter que, il ressort de cette analyse que</em>.</li></ul>"},
            ],
            "examples": [
                "Il convient d'examiner cette hypothèse avec prudence.",
                "Cette question sera traitée dans la deuxième partie.",
                "Ce phénomène s'explique par plusieurs facteurs convergents.",
                "L'analyse des données révèle une tendance nette.",
                "Dans un premier temps, il s'agit de définir les termes du débat.",
                "Il ressort de cette étude que les résultats confirment l'hypothèse initiale.",
                "Ce constat amène à s'interroger sur les causes profondes du phénomène.",
            ],
            "commonMistakes": [
                {"wrong": "Je pense que cette hypothèse est vraie (dans un mémoire académique).", "right": "Il apparaît que cette hypothèse se vérifie.", "why": "L'écrit académique évite le « je » et préfère une formulation impersonnelle ou nominalisée."},
                {"wrong": "Quand on analyse les données, on voit une tendance.", "right": "L'analyse des données révèle une tendance.", "why": "La nominalisation condense la phrase verbale en une construction plus formelle et impersonnelle."},
                {"wrong": "On va traiter cette question dans la deuxième partie.", "right": "Cette question sera traitée dans la deuxième partie.", "why": "Le passif efface l'agent (« on ») et convient mieux au registre académique."},
            ],
        },
        "exercises": [
            {"id": "c1acad-fill", "type": "fill-blank", "title": "Reformule au Style Académique",
             "instructions": "Choisis la formulation la plus académique.",
             "items": [
                {"id": "c1acadf1", "prompt": "« On va traiter cette question » se reformule : « Cette question ___ traitée. »", "answers": [["sera"]], "options": ["sera", "va être", "serait"], "explanation": "Le passif au futur convient au style académique."},
                {"id": "c1acadf2", "prompt": "« Quand on analyse les données, on voit une tendance » se reformule : « ___ des données révèle une tendance. »", "answers": [["L'analyse"]], "options": ["L'analyse", "Analyser", "En analysant"], "explanation": "La nominalisation condense la phrase verbale."},
                {"id": "c1acadf3", "prompt": "« Je pense qu'il faut examiner cette hypothèse » se reformule : « Il ___ d'examiner cette hypothèse. »", "answers": [["convient"]], "options": ["convient", "pense", "faut"], "explanation": "Il convient de est une tournure impersonnelle typique du style académique."},
                {"id": "c1acadf4", "prompt": "« Ça s'explique par plusieurs facteurs » se reformule : « Ce phénomène ___ par plusieurs facteurs. »", "answers": [["s'explique"]], "options": ["s'explique", "s'expliquerait", "explique"], "explanation": "Le pronominal de sens passif efface l'agent."},
             ]},
            {"id": "c1acad-mc", "type": "multiple-choice", "title": "Le Style Académique",
             "items": [
                {"id": "c1acadm1", "prompt": "Que cherche à effacer le style académique ?", "options": ["la présence explicite du locuteur (le « je »)", "toute forme de subjonctif", "les accords grammaticaux"], "answerIndex": 0, "explanation": "L'objectivité passe par l'effacement du locuteur."},
                {"id": "c1acadm2", "prompt": "Quelle construction remplace souvent « on » ou « je » à l'écrit académique ?", "options": ["le passif ou le pronominal de sens passif", "l'impératif", "le futur simple seul"], "answerIndex": 0, "explanation": "Ces constructions effacent l'agent de l'action."},
                {"id": "c1acadm3", "prompt": "Quel outil grammatical condense une phrase verbale en style plus formel ?", "options": ["la nominalisation", "la négation", "l'interrogation"], "answerIndex": 0, "explanation": "C'est l'outil central du style académique."},
                {"id": "c1acadm4", "prompt": "Que signale un connecteur comme « il ressort de cette analyse que » ?", "options": ["une conclusion tirée d'une analyse", "une simple opinion personnelle", "une hypothèse non vérifiée"], "answerIndex": 0, "explanation": "C'est un connecteur de conclusion typique de l'écrit académique."},
             ]},
            {"id": "c1acad-correction", "type": "correction", "title": "Corrige le Registre",
             "items": [
                {"id": "c1acadc1", "incorrect": "Je pense que cette hypothèse est vraie (dans un mémoire).", "answer": ["Il apparaît que cette hypothèse se vérifie."], "explanation": "L'écrit académique évite le « je »."},
                {"id": "c1acadc2", "incorrect": "On va traiter cette question dans la deuxième partie.", "answer": ["Cette question sera traitée dans la deuxième partie."], "explanation": "Le passif convient mieux au style académique."},
                {"id": "c1acadc3", "incorrect": "Quand on analyse les données, on voit une tendance nette.", "answer": ["L'analyse des données révèle une tendance nette."], "explanation": "La nominalisation condense la phrase."},
             ]},
        ],
        "summary": [
            "L'écrit académique évite le « je » avec des constructions impersonnelles (il convient de) et le passif ou le pronominal de sens passif.",
            "La nominalisation condense une phrase verbale en expression nominale plus formelle.",
            "Des connecteurs précis (dans un premier temps, il ressort que) structurent le raisonnement académique.",
        ],
    },
    {
        "id": "c1-le-discours-rapporte-et-la-concordance-des-temps-avancee",
        "level": "C1", "unit": "1", "order": 6, "skill": "grammar", "strand": "discours-rapporte-avance",
        "title": "Le Discours Rapporté et la Concordance des Temps Avancée",
        "subtitle": "Rapporter un conditionnel, un subjonctif, ou un discours situé loin dans le passé — et changer les repères de temps et de lieu.",
        "objectives": [
            "Rapporter au passé un énoncé contenant un conditionnel ou un subjonctif.",
            "Appliquer la concordance des temps complète (présent, passé composé, futur, imparfait, plus-que-parfait, conditionnel).",
            "Changer correctement les repères de temps et de lieu (hier → la veille, ici → là) en rapportant un discours au passé.",
        ],
        "content": {
            "intro": "Le discours rapporté vu au niveau B1 couvrait le présent et le passé composé ; au niveau C1, il faut savoir rapporter n'importe quel énoncé, y compris un conditionnel ou un subjonctif, avec tous les changements de repères que cela implique.",
            "explanation": "<p>La concordance des temps complète, quand le verbe introducteur est au <strong>passé</strong> : le présent devient <strong>imparfait</strong>, le passé composé devient <strong>plus-que-parfait</strong>, le futur simple devient <strong>conditionnel présent</strong>, le futur antérieur devient <strong>conditionnel passé</strong>. Le <strong>conditionnel</strong> et le <strong>subjonctif</strong> de l'énoncé original, eux, ne changent pas de forme au discours rapporté : <em>« Je viendrais si je pouvais »</em> devient <em>Il a dit qu'il viendrait s'il pouvait</em> (le conditionnel reste conditionnel).</p><p>Les repères de temps et de lieu changent aussi quand on rapporte un discours à un moment différent : <em>aujourd'hui → ce jour-là, hier → la veille, demain → le lendemain, la semaine prochaine → la semaine suivante, ici → là</em>. Ces changements, souvent négligés même par des locuteurs avancés, sont indispensables à un récit rapporté cohérent.</p>",
            "rules": [
                {"heading": "a) Présent → imparfait, passé composé → plus-que-parfait", "body": "<ul><li><em>« Je pars » → il a dit qu'il partait. « J'ai fini » → il a dit qu'il avait fini.</em></li></ul>"},
                {"heading": "b) Futur → conditionnel présent, futur antérieur → conditionnel passé", "body": "<ul><li><em>« Je viendrai » → il a dit qu'il viendrait.</em></li></ul>"},
                {"heading": "c) Conditionnel et subjonctif inchangés", "body": "<ul><li><em>« Je viendrais si je pouvais » → il a dit qu'il viendrait s'il pouvait.</em></li></ul>"},
                {"heading": "d) Repères de temps et de lieu", "body": "<ul><li><em>hier → la veille, demain → le lendemain, ici → là, aujourd'hui → ce jour-là</em>.</li></ul>"},
            ],
            "examples": [
                "Il a dit qu'il partait le lendemain.",
                "Elle a expliqué qu'elle avait fini son travail la veille.",
                "Ils ont annoncé qu'ils viendraient dès que possible.",
                "Il m'a confié qu'il aurait terminé avant la fin du mois.",
                "Elle a dit qu'elle viendrait si elle pouvait.",
                "Il a précisé qu'il fallait qu'on parte tôt.",
                "Elle a raconté qu'elle habitait là depuis deux ans.",
            ],
            "commonMistakes": [
                {"wrong": "Il a dit qu'il vient demain.", "right": "Il a dit qu'il venait le lendemain.", "why": "Le verbe introducteur au passé impose l'imparfait, et demain devient le lendemain."},
                {"wrong": "Elle a expliqué qu'elle finirait le rapport hier.", "right": "Elle a expliqué qu'elle avait fini le rapport la veille.", "why": "Une action déjà accomplie au moment du rapport se met au plus-que-parfait, et hier devient la veille."},
                {"wrong": "Il a dit qu'il viendra s'il pourrait.", "right": "Il a dit qu'il viendrait s'il pouvait.", "why": "Le conditionnel de l'énoncé original reste conditionnel ; seul le si + imparfait ne change pas non plus."},
            ],
        },
        "exercises": [
            {"id": "c1disc-fill", "type": "fill-blank", "title": "Rapporte le Discours au Passé",
             "instructions": "Complète avec la forme correcte au discours rapporté.",
             "items": [
                {"id": "c1discf1", "prompt": "« Je pars demain » → Il a dit qu'il ___ (partir) le lendemain.", "answers": [["partait"]], "options": ["partait", "part", "partira"], "explanation": "Présent → imparfait, demain → le lendemain."},
                {"id": "c1discf2", "prompt": "« J'ai fini hier » → Elle a expliqué qu'elle ___ (finir) la veille.", "answers": [["avait fini"]], "options": ["avait fini", "a fini", "finissait"], "explanation": "Passé composé → plus-que-parfait, hier → la veille."},
                {"id": "c1discf3", "prompt": "« Je viendrai » → Ils ont annoncé qu'ils ___ (venir).", "answers": [["viendraient"]], "options": ["viendraient", "viendront", "venaient"], "explanation": "Futur simple → conditionnel présent."},
                {"id": "c1discf4", "prompt": "« Je viendrais si je pouvais » → Elle a dit qu'elle ___ (venir) si elle pouvait.", "answers": [["viendrait"]], "options": ["viendrait", "vient", "était venue"], "explanation": "Le conditionnel original reste conditionnel."},
             ]},
            {"id": "c1disc-mc", "type": "multiple-choice", "title": "Le Discours Rapporté Avancé",
             "items": [
                {"id": "c1discm1", "prompt": "Que devient le futur simple au discours rapporté passé ?", "options": ["le conditionnel présent", "l'imparfait", "le plus-que-parfait"], "answerIndex": 0, "explanation": "C'est la transformation classique du futur au discours rapporté."},
                {"id": "c1discm2", "prompt": "Que devient un conditionnel de l'énoncé original au discours rapporté ?", "options": ["il reste conditionnel", "il devient indicatif", "il devient subjonctif"], "answerIndex": 0, "explanation": "Le conditionnel ne change pas de forme."},
                {"id": "c1discm3", "prompt": "Que devient « hier » au discours rapporté passé ?", "options": ["la veille", "le lendemain", "ce jour-là"], "answerIndex": 0, "explanation": "C'est le changement de repère temporel correspondant."},
                {"id": "c1discm4", "prompt": "Que devient « ici » au discours rapporté ?", "options": ["là", "ici (inchangé)", "là-bas uniquement"], "answerIndex": 0, "explanation": "Le repère de lieu change en là quand on rapporte ailleurs."},
             ]},
            {"id": "c1disc-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "c1discc1", "incorrect": "Il a dit qu'il vient demain.", "answer": ["Il a dit qu'il venait le lendemain."], "explanation": "Imparfait + changement de repère temporel."},
                {"id": "c1discc2", "incorrect": "Elle a expliqué qu'elle finirait le rapport hier.", "answer": ["Elle a expliqué qu'elle avait fini le rapport la veille."], "explanation": "Plus-que-parfait pour une action déjà accomplie."},
                {"id": "c1discc3", "incorrect": "Il a dit qu'il viendra s'il pourrait.", "answer": ["Il a dit qu'il viendrait s'il pouvait."], "explanation": "Le conditionnel reste conditionnel ; si + imparfait ne change pas."},
             ]},
        ],
        "summary": [
            "Au discours rapporté passé : présent → imparfait, passé composé → plus-que-parfait, futur → conditionnel présent.",
            "Le conditionnel et le subjonctif de l'énoncé original ne changent pas de forme.",
            "Les repères de temps et de lieu changent aussi : hier → la veille, demain → le lendemain, ici → là.",
        ],
    },
    {
        "id": "c1-les-locutions-prepositives-nuancees",
        "level": "C1", "unit": "1", "order": 7, "skill": "vocabulary", "strand": "locutions-prepositives",
        "title": "Les Locutions Prépositives Nuancées",
        "subtitle": "Malgré, en dépit de, au sein de, à l'égard de : les expressions prépositives du registre soutenu et leurs nuances précises.",
        "objectives": [
            "Employer malgré/en dépit de pour la concession, avec la nuance de registre entre les deux.",
            "Employer au sein de, à l'égard de, en vertu de, au regard de dans leur sens précis.",
            "Choisir la locution prépositive adaptée au sens exact voulu, sans les confondre.",
        ],
        "content": {
            "intro": "Le français soutenu dispose d'un vaste répertoire de locutions prépositives qui remplacent des prépositions simples pour un effet plus précis ou plus formel — les maîtriser distingue un niveau C1 d'un niveau B2.",
            "explanation": "<p><strong>Malgré</strong> et <strong>en dépit de</strong> expriment tous deux la concession (« malgré la pluie » = « en dépit de la pluie »), mais <em>en dépit de</em> est plus soutenu et littéraire que <em>malgré</em>, qui reste d'usage courant. <strong>Au sein de</strong> signifie « à l'intérieur de » un groupe ou une organisation (<em>au sein de l'entreprise</em>), plus formel que <em>dans</em>. <strong>À l'égard de</strong> signifie « envers » (<em>une attitude bienveillante à l'égard des nouveaux employés</em>).</p><p><strong>En vertu de</strong> introduit un fondement légal ou logique (<em>en vertu de la loi</em>), tandis que <strong>au regard de</strong> introduit un point de comparaison ou un critère d'évaluation (<em>au regard des résultats obtenus</em>). Ces locutions, fréquentes dans la presse, les rapports et les discours officiels, permettent de nuancer précisément un rapport de cause, de comparaison ou d'attitude.</p>",
            "rules": [
                {"heading": "a) Concession", "body": "<ul><li><em>malgré</em> (courant) et <em>en dépit de</em> (plus soutenu) — même sens.</li></ul>"},
                {"heading": "b) Appartenance à un groupe", "body": "<ul><li><em>au sein de</em> — plus formel que « dans ».</li></ul>"},
                {"heading": "c) Attitude envers quelqu'un", "body": "<ul><li><em>à l'égard de</em> — équivaut à « envers ».</li></ul>"},
                {"heading": "d) Fondement et comparaison", "body": "<ul><li><em>en vertu de</em> (fondement légal/logique) ; <em>au regard de</em> (point de comparaison).</li></ul>"},
            ],
            "examples": [
                "Malgré la pluie, le match a eu lieu.",
                "En dépit de nombreuses difficultés, l'équipe a atteint son objectif.",
                "Des tensions existent au sein de l'entreprise depuis quelques mois.",
                "Il a toujours montré de la bienveillance à l'égard de ses collègues.",
                "En vertu de la nouvelle loi, cette pratique est désormais interdite.",
                "Au regard des résultats obtenus, la stratégie semble efficace.",
                "Au sein de la famille, chacun jouait un rôle précis.",
            ],
            "commonMistakes": [
                {"wrong": "En vertu des résultats obtenus, la stratégie semble efficace.", "right": "Au regard des résultats obtenus, la stratégie semble efficace.", "why": "Au regard de introduit un critère d'évaluation ; en vertu de introduit un fondement légal ou logique, pas un critère de comparaison."},
                {"wrong": "Il a montré de la bienveillance au sein de ses collègues.", "right": "Il a montré de la bienveillance à l'égard de ses collègues.", "why": "À l'égard de exprime une attitude envers quelqu'un ; au sein de exprime l'appartenance à un groupe."},
                {"wrong": "Des tensions existent à l'égard de l'entreprise depuis quelques mois (pour dire « à l'intérieur de »).", "right": "Des tensions existent au sein de l'entreprise depuis quelques mois.", "why": "Au sein de exprime l'intériorité à un groupe, pas une attitude envers quelque chose."},
            ],
        },
        "exercises": [
            {"id": "c1loc-fill", "type": "fill-blank", "title": "Choisis la Locution Prépositive Correcte",
             "items": [
                {"id": "c1locf1", "prompt": "___ la pluie, le match a eu lieu.", "answers": [["Malgré"]], "options": ["Malgré", "Au sein de", "En vertu de"], "explanation": "Malgré exprime la concession."},
                {"id": "c1locf2", "prompt": "Des tensions existent ___ l'entreprise depuis quelques mois.", "answers": [["au sein de"]], "options": ["au sein de", "à l'égard de", "au regard de"], "explanation": "Au sein de exprime l'intériorité à un groupe."},
                {"id": "c1locf3", "prompt": "Il a toujours montré de la bienveillance ___ ses collègues.", "answers": [["à l'égard de"]], "options": ["à l'égard de", "en vertu de", "au sein de"], "explanation": "À l'égard de exprime une attitude envers quelqu'un."},
                {"id": "c1locf4", "prompt": "___ la nouvelle loi, cette pratique est interdite.", "answers": [["En vertu de"]], "options": ["En vertu de", "Au regard de", "Malgré"], "explanation": "En vertu de introduit un fondement légal."},
             ]},
            {"id": "c1loc-mc", "type": "multiple-choice", "title": "Les Locutions Prépositives",
             "items": [
                {"id": "c1locm1", "prompt": "Quelle locution est la plus soutenue pour exprimer la concession ?", "options": ["en dépit de", "malgré", "au sein de"], "answerIndex": 0, "explanation": "En dépit de est plus littéraire que malgré, courant."},
                {"id": "c1locm2", "prompt": "Que signifie au sein de ?", "options": ["à l'intérieur d'un groupe", "envers quelqu'un", "en comparaison de"], "answerIndex": 0, "explanation": "C'est un équivalent formel de « dans »."},
                {"id": "c1locm3", "prompt": "Que signifie au regard de ?", "options": ["en fonction d'un critère de comparaison", "à l'intérieur de", "par fondement légal"], "answerIndex": 0, "explanation": "Au regard de introduit un point de comparaison ou d'évaluation."},
                {"id": "c1locm4", "prompt": "Que signifie en vertu de ?", "options": ["en fonction d'un fondement légal ou logique", "envers quelqu'un", "malgré quelque chose"], "answerIndex": 0, "explanation": "C'est le sens précis de en vertu de."},
             ]},
            {"id": "c1loc-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "c1locc1", "incorrect": "En vertu des résultats obtenus, la stratégie semble efficace.", "answer": ["Au regard des résultats obtenus, la stratégie semble efficace."], "explanation": "Au regard de introduit un critère de comparaison, pas un fondement légal."},
                {"id": "c1locc2", "incorrect": "Il a montré de la bienveillance au sein de ses collègues.", "answer": ["Il a montré de la bienveillance à l'égard de ses collègues."], "explanation": "À l'égard de exprime une attitude envers quelqu'un."},
                {"id": "c1locc3", "incorrect": "Des tensions existent à l'égard de l'entreprise.", "answer": ["Des tensions existent au sein de l'entreprise."], "explanation": "Au sein de exprime l'intériorité à un groupe."},
             ]},
        ],
        "summary": [
            "Malgré (courant) et en dépit de (soutenu) expriment tous deux la concession.",
            "Au sein de exprime l'appartenance à un groupe, à l'égard de une attitude envers quelqu'un.",
            "En vertu de introduit un fondement légal ou logique, au regard de un critère de comparaison.",
        ],
    },
    {
        "id": "c1-la-cohesion-et-la-progression-thematique",
        "level": "C1", "unit": "1", "order": 8, "skill": "writing", "strand": "cohesion-textuelle",
        "title": "La Cohésion et la Progression Thématique dans un Texte Argumentatif",
        "subtitle": "Construire un texte fluide qui progresse sans répétition, par reprise lexicale, pronominale et synonymique.",
        "objectives": [
            "Comprendre la progression thème/rhème d'un texte cohérent.",
            "Éviter la répétition lexicale par la reprise pronominale et la synonymie.",
            "Organiser un paragraphe argumentatif autour d'une idée qui progresse logiquement.",
        ],
        "content": {
            "intro": "Un texte bien écrit ne s'improvise pas phrase par phrase : chaque phrase reprend une information déjà connue (le thème) pour introduire une information nouvelle (le rhème), créant ainsi une progression logique et fluide.",
            "explanation": "<p>La <strong>progression thématique</strong> décrit comment l'information circule d'une phrase à l'autre : le <strong>thème</strong> est ce dont on parle (connu), le <strong>rhème</strong> est ce qu'on en dit (nouveau). Dans une progression simple, le rhème d'une phrase devient le thème de la suivante : <em>Le réchauffement climatique menace les écosystèmes. Ces écosystèmes, déjà fragilisés, peinent à s'adapter.</em></p><p>Pour éviter de répéter le même mot, le français utilise la <strong>reprise pronominale</strong> (<em>il, elle, celui-ci, ce dernier</em>), la <strong>reprise lexicale par synonyme</strong> (<em>le réchauffement → ce phénomène → cette évolution</em>), et la reprise par un <strong>terme générique</strong> (<em>le chêne → cet arbre</em>). Une bonne cohésion textuelle enchaîne aussi les idées avec des connecteurs adaptés, évitant les ruptures logiques entre les paragraphes.</p>",
            "rules": [
                {"heading": "a) Thème et rhème", "body": "<ul><li>Le thème (connu) précède le rhème (nouveau) ; le rhème d'une phrase devient souvent le thème de la suivante.</li></ul>"},
                {"heading": "b) Reprise pronominale", "body": "<ul><li><em>il, elle, celui-ci, ce dernier</em> — évitent de répéter le nom.</li></ul>"},
                {"heading": "c) Reprise par synonyme ou terme générique", "body": "<ul><li><em>le réchauffement → ce phénomène ; le chêne → cet arbre</em>.</li></ul>"},
                {"heading": "d) Connecteurs de cohésion", "body": "<ul><li>Enchaînent les idées sans rupture logique entre les phrases et les paragraphes.</li></ul>"},
            ],
            "examples": [
                "Le réchauffement climatique menace les écosystèmes. Ces derniers peinent déjà à s'adapter.",
                "L'auteur aborde ensuite un second argument, plus personnel celui-là.",
                "Cette réforme divise l'opinion. Ce phénomène s'observe dans tous les pays voisins.",
                "Le chêne est un arbre majestueux. Cet arbre peut vivre plusieurs siècles.",
                "L'entreprise a annoncé son plan. Ce dernier prévoit une restructuration complète.",
                "Ces deux hypothèses semblent contradictoires ; pourtant, elles se complètent.",
                "Le sujet mérite d'être approfondi ; c'est précisément l'objet de cette étude.",
            ],
            "commonMistakes": [
                {"wrong": "Le réchauffement climatique menace les écosystèmes. Le réchauffement climatique s'accélère chaque année.", "right": "Le réchauffement climatique menace les écosystèmes. Ce phénomène s'accélère chaque année.", "why": "Répéter le même groupe nominal alourdit le texte ; une reprise par synonyme ou pronom crée une meilleure cohésion."},
                {"wrong": "Écrire un paragraphe où chaque phrase introduit une idée sans lien avec la précédente.", "right": "Faire en sorte que le rhème d'une phrase devienne le thème de la phrase suivante.", "why": "Sans progression thématique claire, le texte perd en cohérence et devient difficile à suivre."},
                {"wrong": "Utiliser toujours le même pronom il/elle même quand le référent devient ambigu.", "right": "Utiliser ce dernier/celui-ci quand plusieurs référents possibles créent une ambiguïté.", "why": "Ce dernier lève l'ambiguïté en désignant clairement le référent le plus proche."},
            ],
        },
        "exercises": [
            {"id": "c1coh-fill", "type": "fill-blank", "title": "Complète avec la Reprise Correcte",
             "instructions": "Choisis la reprise qui évite la répétition.",
             "items": [
                {"id": "c1cohf1", "prompt": "Le réchauffement climatique menace les écosystèmes. ___ phénomène s'accélère chaque année.", "answers": [["Ce"]], "options": ["Ce", "Le", "Un"], "explanation": "Ce phénomène reprend le réchauffement climatique par synonymie."},
                {"id": "c1cohf2", "prompt": "L'entreprise a annoncé son plan. ___ dernier prévoit une restructuration.", "answers": [["Ce"]], "options": ["Ce", "Le", "Un"], "explanation": "Ce dernier reprend le plan pour éviter l'ambiguïté."},
                {"id": "c1cohf3", "prompt": "Le chêne est un arbre majestueux. Cet ___ peut vivre plusieurs siècles.", "answers": [["arbre"]], "options": ["arbre", "chêne", "bois"], "explanation": "Reprise par terme générique."},
                {"id": "c1cohf4", "prompt": "Dans une progression thématique simple, le ___ d'une phrase devient le thème de la suivante.", "answers": [["rhème"]], "options": ["rhème", "verbe", "sujet"], "explanation": "C'est la définition de la progression thématique simple."},
             ]},
            {"id": "c1coh-mc", "type": "multiple-choice", "title": "La Cohésion Textuelle",
             "items": [
                {"id": "c1cohm1", "prompt": "Qu'est-ce que le thème d'une phrase ?", "options": ["ce dont on parle, l'information connue", "l'information nouvelle", "le verbe principal"], "answerIndex": 0, "explanation": "C'est la définition du thème, par opposition au rhème."},
                {"id": "c1cohm2", "prompt": "Pourquoi éviter de répéter le même mot dans un texte cohérent ?", "options": ["cela alourdit le style, mieux vaut varier avec pronoms/synonymes", "c'est une règle sans justification", "cela change le sens du texte"], "answerIndex": 0, "explanation": "La variation améliore la fluidité et la cohésion."},
                {"id": "c1cohm3", "prompt": "Que reprend « ce dernier » dans un texte ?", "options": ["le référent le plus proche, pour lever une ambiguïté", "toujours le sujet de la première phrase", "rien, c'est une expression vide"], "answerIndex": 0, "explanation": "Ce dernier désigne le référent le plus récent."},
                {"id": "c1cohm4", "prompt": "Qu'est-ce qu'une progression thématique simple ?", "options": ["le rhème d'une phrase devient le thème de la suivante", "chaque phrase a un thème différent", "il n'y a pas de thème du tout"], "answerIndex": 0, "explanation": "C'est le type de progression le plus courant en français."},
             ]},
            {"id": "c1coh-ordering", "type": "ordering", "title": "Remets la Phrase en Ordre",
             "items": [
                {"id": "c1coho1", "prompt": "Remets les mots en ordre.", "words": ["Ce", "phénomène", "s'accélère", "chaque", "année"], "explanation": "Reprise par synonyme du thème précédent."},
                {"id": "c1coho2", "prompt": "Remets les mots en ordre.", "words": ["Ce", "dernier", "prévoit", "une", "restructuration"], "explanation": "Ce dernier reprend le référent le plus proche sans ambiguïté."},
             ]},
        ],
        "summary": [
            "La progression thématique fait circuler l'information : le rhème (nouveau) d'une phrase devient souvent le thème (connu) de la suivante.",
            "La reprise pronominale (celui-ci, ce dernier), lexicale par synonyme ou par terme générique évite la répétition.",
            "Une bonne cohésion textuelle enchaîne les idées sans rupture logique, à l'intérieur d'un paragraphe comme entre les paragraphes.",
        ],
    },
    {
        "id": "c1-les-registres-et-la-variation-stylistique",
        "level": "C1", "unit": "1", "order": 9, "skill": "vocabulary", "strand": "registres-ecrits",
        "title": "Les Registres et la Variation Stylistique à l'Écrit",
        "subtitle": "Distinguer littéraire, journalistique, administratif et courant, et choisir le registre adapté à chaque écrit.",
        "objectives": [
            "Distinguer quatre registres écrits : littéraire, journalistique, administratif, courant.",
            "Reconnaître les marqueurs lexicaux et syntaxiques propres à chacun.",
            "Reformuler un même contenu dans le registre approprié à une situation donnée.",
        ],
        "content": {
            "intro": "Un même contenu peut s'écrire de quatre façons très différentes selon le contexte : un roman, un article de presse, un courrier officiel et une note interne n'obéissent pas aux mêmes conventions stylistiques.",
            "explanation": "<p>Le registre <strong>littéraire</strong> privilégie les phrases longues, le vocabulaire recherché, les figures de style et parfois les temps du passé simple/subjonctif imparfait : <em>Le soleil déclinait lentement sur la vallée endormie.</em> Le registre <strong>journalistique</strong> vise la clarté et l'accroche : phrases courtes, chiffres, citations, conditionnel pour l'information non confirmée : <em>Le bilan s'alourdirait, selon les derniers chiffres.</em></p><p>Le registre <strong>administratif</strong> emploie des formules figées, la nominalisation, la troisième personne et des formules de politesse codifiées : <em>Nous vous prions de bien vouloir nous faire parvenir les documents requis.</em> Le registre <strong>courant</strong> (celui de ce cours) reste clair, correct, sans effet de style ni formule figée : <em>Merci de nous envoyer les documents.</em> Savoir passer de l'un à l'autre selon le contexte est une compétence-clé du niveau C1.</p>",
            "rules": [
                {"heading": "a) Registre littéraire", "body": "<ul><li>Phrases longues, figures de style, temps littéraires : <em>Le soleil déclinait sur la vallée.</em></li></ul>"},
                {"heading": "b) Registre journalistique", "body": "<ul><li>Phrases courtes, chiffres, conditionnel d'information non confirmée.</li></ul>"},
                {"heading": "c) Registre administratif", "body": "<ul><li>Formules figées, nominalisation, politesse codifiée : <em>Nous vous prions de bien vouloir…</em></li></ul>"},
                {"heading": "d) Registre courant", "body": "<ul><li>Clair, correct, sans effet de style : le registre par défaut de ce cours.</li></ul>"},
            ],
            "examples": [
                "Le soleil déclinait lentement sur la vallée endormie. (littéraire)",
                "Le bilan s'alourdirait, selon les derniers chiffres communiqués. (journalistique)",
                "Nous vous prions de bien vouloir nous faire parvenir les documents requis. (administratif)",
                "Merci de nous envoyer les documents dès que possible. (courant)",
                "Ainsi s'acheva cette longue et éprouvante journée. (littéraire)",
                "Le gouvernement annoncerait de nouvelles mesures dès la semaine prochaine. (journalistique)",
                "Veuillez trouver ci-joint le formulaire dûment complété. (administratif)",
            ],
            "commonMistakes": [
                {"wrong": "Écrire à un ami : « Nous vous prions de bien vouloir me répondre. »", "right": "Écrire à un ami : « Réponds-moi vite, s'il te plaît ! »", "why": "Le registre administratif est totalement déplacé dans une communication amicale et informelle."},
                {"wrong": "Rédiger un article de presse avec des phrases très longues et un vocabulaire littéraire recherché.", "right": "Rédiger un article de presse avec des phrases courtes, claires, et des informations chiffrées.", "why": "Le registre journalistique vise la clarté et l'efficacité, pas l'effet de style littéraire."},
                {"wrong": "Utiliser le passé simple dans une lettre administrative courante.", "right": "Utiliser le passé composé, temps normal du registre administratif et courant.", "why": "Le passé simple est réservé au registre littéraire ; l'administratif emploie le passé composé."},
            ],
        },
        "exercises": [
            {"id": "c1reg-fill", "type": "fill-blank", "title": "Identifie le Registre",
             "items": [
                {"id": "c1regf1", "prompt": "« Le soleil déclinait lentement sur la vallée » appartient au registre ___.", "answers": [["littéraire"]], "options": ["littéraire", "administratif", "journalistique"], "explanation": "Phrase longue, image poétique : registre littéraire."},
                {"id": "c1regf2", "prompt": "« Nous vous prions de bien vouloir… » appartient au registre ___.", "answers": [["administratif"]], "options": ["administratif", "littéraire", "courant"], "explanation": "Formule figée et polie : registre administratif."},
                {"id": "c1regf3", "prompt": "« Le bilan s'alourdirait, selon les derniers chiffres » appartient au registre ___.", "answers": [["journalistique"]], "options": ["journalistique", "littéraire", "administratif"], "explanation": "Conditionnel d'information non confirmée : registre journalistique."},
                {"id": "c1regf4", "prompt": "« Merci de nous envoyer les documents » appartient au registre ___.", "answers": [["courant"]], "options": ["courant", "littéraire", "administratif"], "explanation": "Clair, simple, sans formule figée : registre courant."},
             ]},
            {"id": "c1reg-mc", "type": "multiple-choice", "title": "Les Registres à l'Écrit",
             "items": [
                {"id": "c1regm1", "prompt": "Quel registre emploie le plus souvent des figures de style et le passé simple ?", "options": ["le littéraire", "l'administratif", "le journalistique"], "answerIndex": 0, "explanation": "Ce sont des marqueurs typiques du registre littéraire."},
                {"id": "c1regm2", "prompt": "Quel registre emploie souvent le conditionnel pour une information non confirmée ?", "options": ["le journalistique", "le courant", "le littéraire"], "answerIndex": 0, "explanation": "C'est un usage typique de la presse."},
                {"id": "c1regm3", "prompt": "Quel registre emploie des formules figées de politesse codifiée ?", "options": ["l'administratif", "le littéraire", "le courant"], "answerIndex": 0, "explanation": "« Nous vous prions de bien vouloir » est une formule administrative typique."},
                {"id": "c1regm4", "prompt": "Quel registre est le registre « par défaut », sans effet de style particulier ?", "options": ["le courant", "le littéraire", "l'administratif"], "answerIndex": 0, "explanation": "C'est le registre neutre de la communication quotidienne correcte."},
             ]},
            {"id": "c1reg-correction", "type": "correction", "title": "Corrige le Registre Inapproprié",
             "items": [
                {"id": "c1regc1", "incorrect": "Nous vous prions de bien vouloir me répondre (à un ami proche).", "answer": ["Réponds-moi vite, s'il te plaît !"], "explanation": "Le registre administratif est déplacé entre amis."},
                {"id": "c1regc2", "incorrect": "Le soleil déclinait lentement sur la vallée endormie (dans un article factuel bref).", "answer": ["Le soleil s'est couché à 19h30 aujourd'hui."], "explanation": "Le registre littéraire est déplacé dans un article factuel."},
                {"id": "c1regc3", "incorrect": "Le bilan s'alourdit, c'est confirmé (alors que l'information n'est pas vérifiée).", "answer": ["Le bilan s'alourdirait, selon les derniers chiffres."], "explanation": "Une information non confirmée demande le conditionnel journalistique."},
             ]},
        ],
        "summary": [
            "Le littéraire privilégie les figures de style et les temps littéraires ; le journalistique vise la clarté et l'accroche.",
            "L'administratif emploie des formules figées et la politesse codifiée ; le courant reste clair et sans effet de style.",
            "Choisir le registre adapté à la situation est une compétence-clé du niveau C1.",
        ],
    },
    {
        "id": "c1-lexpression-de-la-restriction-et-de-lexception",
        "level": "C1", "unit": "1", "order": 10, "skill": "grammar", "strand": "restriction-exception",
        "title": "L'Expression de la Restriction et de l'Exception",
        "subtitle": "Ne... que, sauf, hormis, excepté, à moins que : dire ce qui limite une affirmation, avec précision.",
        "objectives": [
            "Employer ne... que pour exprimer une restriction équivalente à seulement.",
            "Distinguer sauf, hormis et excepté, proches en sens mais différents en registre.",
            "Employer à moins que + subjonctif et sous réserve de + nom pour poser une condition restrictive.",
        ],
        "content": {
            "intro": "Exprimer une restriction ou une exception avec précision — ce qui limite une règle générale, ou ce qui y échappe — est une marque de maîtrise fine du français, avec plusieurs outils aux nuances de registre différentes.",
            "explanation": "<p><strong>Ne... que</strong> exprime une restriction équivalente à « seulement » : <em>Je n'ai que deux heures devant moi</em> (= seulement deux heures). <strong>Sauf</strong>, <strong>hormis</strong> et <strong>excepté</strong> introduisent une exception à une règle générale ; ils sont proches en sens, mais <em>sauf</em> est d'usage courant, tandis que <em>hormis</em> et <em>excepté</em> sont plus soutenus et plus fréquents à l'écrit : <em>Tout le monde est venu, sauf/hormis/excepté Marc.</em></p><p><strong>À moins que</strong> + subjonctif pose une condition restrictive qui empêcherait la réalisation de l'action principale : <em>Nous partirons à moins qu'il ne pleuve.</em> <strong>Sous réserve de</strong> + nom introduit une condition formelle, fréquente dans les contrats et les annonces officielles : <em>Le projet sera validé, sous réserve de l'accord du conseil.</em></p>",
            "rules": [
                {"heading": "a) Ne... que", "body": "<ul><li>Équivaut à « seulement » : <em>Il ne reste que trois places.</em></li></ul>"},
                {"heading": "b) Sauf / hormis / excepté", "body": "<ul><li>Introduisent une exception ; sauf est courant, hormis et excepté plus soutenus.</li></ul>"},
                {"heading": "c) À moins que + subjonctif", "body": "<ul><li>Condition restrictive qui empêcherait l'action principale : <em>à moins qu'il ne pleuve</em>.</li></ul>"},
                {"heading": "d) Sous réserve de + nom", "body": "<ul><li>Condition formelle, fréquente en contexte officiel/contractuel.</li></ul>"},
            ],
            "examples": [
                "Je n'ai que deux heures devant moi ce matin.",
                "Tout le monde est venu, sauf Marc, qui était malade.",
                "Hormis quelques détails, le rapport est complet.",
                "Excepté le prix, cette offre est parfaite.",
                "Nous partirons à moins qu'il ne pleuve.",
                "Le projet sera validé, sous réserve de l'accord du conseil.",
                "Il ne reste que trois places pour la conférence de demain.",
            ],
            "commonMistakes": [
                {"wrong": "Je n'ai pas que deux heures devant moi (pour dire « seulement deux heures »).", "right": "Je n'ai que deux heures devant moi.", "why": "Ne... que est déjà une restriction complète (= seulement) ; ajouter pas la transforme en négation d'une négation, un contresens."},
                {"wrong": "Nous partirons à moins qu'il pleut.", "right": "Nous partirons à moins qu'il ne pleuve.", "why": "À moins que impose le subjonctif, ici avec le ne explétif (facultatif mais fréquent à l'écrit soutenu)."},
                {"wrong": "Le projet sera validé, sous réserve que le conseil accepte (mélange de sous réserve de + nom et sous réserve que + phrase).", "right": "Le projet sera validé, sous réserve de l'accord du conseil. / Le projet sera validé, sous réserve que le conseil accepte.", "why": "Sous réserve de se construit avec un nom, sous réserve que avec une proposition — les deux existent, mais ne se mélangent pas dans une même construction."},
            ],
        },
        "exercises": [
            {"id": "c1rest-fill", "type": "fill-blank", "title": "Complète avec l'Expression de Restriction",
             "items": [
                {"id": "c1restf1", "prompt": "Je ___ que deux heures devant moi.", "answers": [["n'ai"]], "options": ["n'ai", "n'ai pas", "ai"], "explanation": "Ne... que exprime la restriction, sans pas."},
                {"id": "c1restf2", "prompt": "Tout le monde est venu, ___ Marc, qui était malade.", "answers": [["sauf"]], "options": ["sauf", "à moins que", "sous réserve de"], "explanation": "Sauf introduit une exception, ici en registre courant."},
                {"id": "c1restf3", "prompt": "Nous partirons à moins qu'il ne ___ (pleuvoir).", "answers": [["pleuve"]], "options": ["pleuve", "pleut", "pleuvra"], "explanation": "À moins que impose le subjonctif."},
                {"id": "c1restf4", "prompt": "Le projet sera validé, sous réserve ___ l'accord du conseil.", "answers": [["de"]], "options": ["de", "que", "à"], "explanation": "Sous réserve de se construit avec un nom."},
             ]},
            {"id": "c1rest-mc", "type": "multiple-choice", "title": "La Restriction et l'Exception",
             "items": [
                {"id": "c1restm1", "prompt": "À quoi équivaut ne... que ?", "options": ["seulement", "jamais", "toujours"], "answerIndex": 0, "explanation": "C'est une restriction équivalente à seulement."},
                {"id": "c1restm2", "prompt": "Quel mot d'exception est le plus courant à l'oral ?", "options": ["sauf", "hormis", "excepté"], "answerIndex": 0, "explanation": "Sauf est d'usage courant ; hormis et excepté sont plus soutenus."},
                {"id": "c1restm3", "prompt": "Quelle construction suit à moins que ?", "options": ["le subjonctif", "l'indicatif", "le conditionnel"], "answerIndex": 0, "explanation": "À moins que impose toujours le subjonctif."},
                {"id": "c1restm4", "prompt": "Avec quoi se construit sous réserve de ?", "options": ["un nom", "une proposition avec que", "un verbe à l'infinitif seul"], "answerIndex": 0, "explanation": "Sous réserve de est suivi d'un groupe nominal."},
             ]},
            {"id": "c1rest-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "c1restc1", "incorrect": "Je n'ai pas que deux heures devant moi.", "answer": ["Je n'ai que deux heures devant moi."], "explanation": "Ne... que est déjà une restriction complète, sans pas."},
                {"id": "c1restc2", "incorrect": "Nous partirons à moins qu'il pleut.", "answer": ["Nous partirons à moins qu'il ne pleuve."], "explanation": "À moins que impose le subjonctif."},
                {"id": "c1restc3", "incorrect": "Le projet sera validé, sous réserve l'accord du conseil.", "answer": ["Le projet sera validé, sous réserve de l'accord du conseil."], "explanation": "Sous réserve de exige la préposition de devant le nom."},
             ]},
        ],
        "summary": [
            "Ne... que équivaut à seulement ; sauf/hormis/excepté introduisent une exception, du plus courant (sauf) au plus soutenu (hormis, excepté).",
            "À moins que impose le subjonctif pour poser une condition restrictive à l'action principale.",
            "Sous réserve de + nom introduit une condition formelle, fréquente en contexte officiel et contractuel.",
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
    "c1-le-subjonctif-imparfait-et-plus-que-parfait": [
        {"id": "c1silx-reading", "type": "reading-comprehension", "title": "Lecture : Un Extrait Classique",
         "passage": "<p>Il fallait qu'il partît avant que le jour ne se levât, car le voyage serait long. Bien qu'elle fût inquiète, sa mère ne dit rien. Il eût fallu davantage de temps pour tout préparer, mais le destin en décida autrement. Quoiqu'il eût pris toutes les précautions, un orage éclata sur la route.</p>",
         "items": [
            {"id": "c1silxr1", "prompt": "Pourquoi fallait-il qu'il parte avant le lever du jour ?", "options": ["Le voyage serait long", "Il avait peur du soleil", "Le jour était férié"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "c1silxr2", "prompt": "Comment se sentait la mère ?", "options": ["Inquiète, mais elle ne dit rien", "Furieuse", "Indifférente"], "answerIndex": 0, "explanation": "Le texte le précise avec « bien qu'elle fût inquiète »."},
            {"id": "c1silxr3", "prompt": "Qu'est-ce qui aurait été nécessaire, selon le texte ?", "options": ["Davantage de temps pour tout préparer", "Moins de bagages", "Un autre chemin"], "answerIndex": 0, "explanation": "Le texte le dit avec « il eût fallu davantage de temps »."},
            {"id": "c1silxr4", "prompt": "Que se passa-t-il malgré toutes les précautions prises ?", "options": ["Un orage éclata sur la route", "Le voyage fut annulé", "Ils arrivèrent en avance"], "answerIndex": 0, "explanation": "Le texte se termine sur cet événement."},
         ]},
        {"id": "c1silx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1silxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "fallait", "qu'il", "partît", "avant", "l'aube"], "explanation": "Subjonctif imparfait littéraire après il fallait que."},
            {"id": "c1silxo2", "prompt": "Remets les mots en ordre.", "words": ["Bien", "qu'elle", "fût", "inquiète,", "elle", "se", "tut"], "explanation": "Bien que + subjonctif imparfait, accent circonflexe à fût."},
         ]},
    ],
    "c1-les-quatre-types-de-phrases-conditionnelles-complexes": [
        {"id": "c1condx-reading", "type": "reading-comprehension", "title": "Lecture : Regrets et Projets",
         "passage": "<p>Si j'avais choisi médecine, je travaillerais aujourd'hui dans un hôpital. Si j'avais économisé davantage pendant mes études, j'aurais moins de dettes maintenant. Si tout se passe bien demain, je signerai le contrat. Et si j'avais su plus tôt que ce poste existait, j'aurais postulé sans hésiter.</p>",
         "items": [
            {"id": "c1condxr1", "prompt": "Où la personne travaillerait-elle si elle avait choisi médecine ?", "options": ["Dans un hôpital", "Dans une école", "Dans une usine"], "answerIndex": 0, "explanation": "C'est une hypothèse mixte : cause passée, conséquence présente."},
            {"id": "c1condxr2", "prompt": "Qu'aurait-elle de moins si elle avait économisé davantage ?", "options": ["Des dettes", "Des amis", "Du temps libre"], "answerIndex": 0, "explanation": "Autre hypothèse mixte du texte."},
            {"id": "c1condxr3", "prompt": "Que fera-t-elle si tout se passe bien demain ?", "options": ["Elle signera le contrat", "Elle partira en voyage", "Elle changera de métier"], "answerIndex": 0, "explanation": "C'est le type réel : si + présent → futur."},
            {"id": "c1condxr4", "prompt": "Qu'aurait-elle fait si elle avait su plus tôt pour le poste ?", "options": ["Elle aurait postulé", "Elle aurait déménagé", "Elle aurait refusé"], "answerIndex": 0, "explanation": "C'est l'irréel du passé : plus-que-parfait → conditionnel passé."},
         ]},
        {"id": "c1condx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1condxo1", "prompt": "Remets les mots en ordre.", "words": ["Si", "j'avais", "choisi", "médecine,", "je", "travaillerais", "aujourd'hui"], "explanation": "Hypothèse mixte : cause passée, conséquence présente."},
            {"id": "c1condxo2", "prompt": "Remets les mots en ordre.", "words": ["Si", "tout", "se", "passe", "bien,", "je", "signerai"], "explanation": "Réel : si + présent → futur."},
         ]},
    ],
    "c1-les-nuances-du-subjonctif": [
        {"id": "c1nuanx-reading", "type": "reading-comprehension", "title": "Lecture : Une Décision Incertaine",
         "passage": "<p>Il est certain que ce projet coûtera cher. Il est cependant peu probable qu'il soit abandonné, tant les enjeux sont importants. Je ne pense pas que le conseil rejette cette proposition, mais il est possible que des modifications soient demandées. Il est évident que la décision finale reviendra à la direction.</p>",
         "items": [
            {"id": "c1nuanxr1", "prompt": "Que dit le texte avec certitude sur le coût du projet ?", "options": ["Il coûtera cher", "Il sera gratuit", "Il coûtera peu"], "answerIndex": 0, "explanation": "Il est certain que + indicatif exprime la certitude."},
            {"id": "c1nuanxr2", "prompt": "Le projet a-t-il de fortes chances d'être abandonné ?", "options": ["Non, c'est peu probable", "Oui, c'est certain", "Le texte ne le dit pas"], "answerIndex": 0, "explanation": "Il est peu probable que + subjonctif exprime une faible probabilité."},
            {"id": "c1nuanxr3", "prompt": "Que pense l'auteur du rejet de la proposition par le conseil ?", "options": ["Il ne pense pas que ce soit probable", "Il en est certain", "Il n'a pas d'avis"], "answerIndex": 0, "explanation": "Je ne pense pas que + subjonctif exprime le doute."},
            {"id": "c1nuanxr4", "prompt": "Qui prendra la décision finale, selon le texte ?", "options": ["La direction", "Le conseil seul", "Les employés"], "answerIndex": 0, "explanation": "Le texte se termine sur cette affirmation certaine."},
         ]},
        {"id": "c1nuanx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1nuanxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "est", "certain", "que", "cela", "coûtera", "cher"], "explanation": "Certitude totale : indicatif."},
            {"id": "c1nuanxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "est", "possible", "que", "cela", "change"], "explanation": "Simple possibilité : subjonctif."},
         ]},
    ],
    "c1-les-constructions-emphatiques-avancees": [
        {"id": "c1empx-reading", "type": "reading-comprehension", "title": "Lecture : Un Tournant Inattendu",
         "passage": "<p>Peut-être aurait-il pu éviter cette erreur. Sans doute regrette-t-il aujourd'hui sa décision. Ce projet, il y a consacré des années entières. Aussi décida-t-il, un beau matin, de tout recommencer à zéro. C'est précisément ce courage-là qui a fini par payer.</p>",
         "items": [
            {"id": "c1empxr1", "prompt": "Qu'aurait-il peut-être pu faire ?", "options": ["Éviter cette erreur", "Gagner plus d'argent", "Partir plus tôt"], "answerIndex": 0, "explanation": "Le texte le dit directement, avec inversion après peut-être."},
            {"id": "c1empxr2", "prompt": "À quoi a-t-il consacré des années entières ?", "options": ["À ce projet", "À ses études", "À sa famille"], "answerIndex": 0, "explanation": "Dislocation à gauche : « ce projet, il y a consacré... »."},
            {"id": "c1empxr3", "prompt": "Que décida-t-il un beau matin ?", "options": ["De tout recommencer à zéro", "D'abandonner", "De vendre son entreprise"], "answerIndex": 0, "explanation": "Le texte le dit directement, avec inversion après aussi."},
            {"id": "c1empxr4", "prompt": "Qu'est-ce qui a fini par payer, selon le texte ?", "options": ["Ce courage-là", "La chance", "L'argent"], "answerIndex": 0, "explanation": "Le texte se termine par cette mise en relief avec c'est... qui."},
         ]},
        {"id": "c1empx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1empxo1", "prompt": "Remets les mots en ordre.", "words": ["Sans", "doute", "regrette-t-il", "sa", "décision"], "explanation": "Inversion après sans doute en tête de phrase."},
            {"id": "c1empxo2", "prompt": "Remets les mots en ordre.", "words": ["Ce", "projet,", "il", "y", "a", "consacré", "des", "années"], "explanation": "Dislocation à gauche, reprise par y."},
         ]},
    ],
    "c1-la-nominalisation-et-le-style-academique": [
        {"id": "c1acadx-reading", "type": "reading-comprehension", "title": "Lecture : Extrait d'un Rapport",
         "passage": "<p>Il convient d'examiner cette question avec attention. L'analyse des données recueillies révèle une tendance préoccupante. Ce phénomène s'explique par une conjonction de facteurs économiques et sociaux. Dans un premier temps, il s'agit de définir précisément le cadre de cette étude. Il ressort de cette analyse que des mesures correctives sont nécessaires.</p>",
         "items": [
            {"id": "c1acadxr1", "prompt": "Que révèle l'analyse des données ?", "options": ["Une tendance préoccupante", "Une amélioration constante", "Aucun résultat clair"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "c1acadxr2", "prompt": "Par quoi s'explique ce phénomène ?", "options": ["Une conjonction de facteurs économiques et sociaux", "Le hasard", "Une erreur de calcul"], "answerIndex": 0, "explanation": "Le texte le précise avec le pronominal de sens passif."},
            {"id": "c1acadxr3", "prompt": "Que s'agit-il de faire dans un premier temps ?", "options": ["Définir le cadre de l'étude", "Publier les résultats", "Interroger le public"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "c1acadxr4", "prompt": "Que ressort-il de cette analyse ?", "options": ["Des mesures correctives sont nécessaires", "Aucune action n'est requise", "Le sujet est clos"], "answerIndex": 0, "explanation": "Le texte se termine sur cette conclusion."},
         ]},
        {"id": "c1acadx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1acadxo1", "prompt": "Remets les mots en ordre.", "words": ["L'analyse", "révèle", "une", "tendance", "préoccupante"], "explanation": "Nominalisation en tête de phrase, style académique."},
            {"id": "c1acadxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "convient", "d'examiner", "cette", "question"], "explanation": "Construction impersonnelle typique du style académique."},
         ]},
    ],
    "c1-le-discours-rapporte-et-la-concordance-des-temps-avancee": [
        {"id": "c1discx-reading", "type": "reading-comprehension", "title": "Lecture : Un Témoignage Rapporté",
         "passage": "<p>Elle a raconté qu'elle était née là-bas et qu'elle y avait vécu jusqu'à ses vingt ans. Elle a précisé qu'elle partirait le lendemain pour ne jamais revenir. Elle a ajouté qu'elle serait revenue plus tôt si elle avait pu. Elle a confié qu'elle regrettait cette décision, mais qu'elle referait sans doute le même choix.</p>",
         "items": [
            {"id": "c1discxr1", "prompt": "Où était-elle née, selon son témoignage ?", "options": ["Là-bas", "Ici", "On ne sait pas"], "answerIndex": 0, "explanation": "Le repère de lieu là reprend ici de l'énoncé original."},
            {"id": "c1discxr2", "prompt": "Jusqu'à quel âge y avait-elle vécu ?", "options": ["Vingt ans", "Dix ans", "Trente ans"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "c1discxr3", "prompt": "Quand allait-elle partir, selon son témoignage ?", "options": ["Le lendemain", "Dans un mois", "Immédiatement"], "answerIndex": 0, "explanation": "Demain devient le lendemain au discours rapporté passé."},
            {"id": "c1discxr4", "prompt": "Que regrettait-elle, selon le texte ?", "options": ["Cette décision", "Son enfance", "Son travail"], "answerIndex": 0, "explanation": "Le texte se termine sur ce regret exprimé."},
         ]},
        {"id": "c1discx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1discxo1", "prompt": "Remets les mots en ordre.", "words": ["Elle", "a", "précisé", "qu'elle", "partirait", "le", "lendemain"], "explanation": "Futur → conditionnel présent, demain → le lendemain."},
            {"id": "c1discxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "a", "raconté", "qu'elle", "était", "née", "là-bas"], "explanation": "Présent → imparfait, ici → là-bas."},
         ]},
    ],
    "c1-les-locutions-prepositives-nuancees": [
        {"id": "c1locx-reading", "type": "reading-comprehension", "title": "Lecture : Un Bilan d'Entreprise",
         "passage": "<p>En dépit de la crise économique, l'entreprise a maintenu ses effectifs. Des inquiétudes subsistent au sein de la direction quant à l'avenir du secteur. La politique de recrutement reste bienveillante à l'égard des jeunes diplômés. En vertu du nouvel accord signé, les salaires seront revalorisés. Au regard des résultats de l'année, la stratégie semble porter ses fruits.</p>",
         "items": [
            {"id": "c1locxr1", "prompt": "Qu'a fait l'entreprise en dépit de la crise ?", "options": ["Elle a maintenu ses effectifs", "Elle a licencié", "Elle a fermé"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "c1locxr2", "prompt": "Où subsistent des inquiétudes ?", "options": ["Au sein de la direction", "Chez les clients", "À l'étranger"], "answerIndex": 0, "explanation": "Au sein de exprime l'intériorité à un groupe."},
            {"id": "c1locxr3", "prompt": "Envers qui la politique de recrutement reste-t-elle bienveillante ?", "options": ["Les jeunes diplômés", "Les actionnaires", "Les concurrents"], "answerIndex": 0, "explanation": "À l'égard de exprime une attitude envers quelqu'un."},
            {"id": "c1locxr4", "prompt": "Que se passera-t-il en vertu du nouvel accord ?", "options": ["Les salaires seront revalorisés", "Les horaires changeront", "L'entreprise déménagera"], "answerIndex": 0, "explanation": "En vertu de introduit le fondement légal de cette mesure."},
         ]},
        {"id": "c1locx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1locxo1", "prompt": "Remets les mots en ordre.", "words": ["En", "dépit", "de", "la", "crise,", "elle", "résiste"], "explanation": "En dépit de exprime la concession, registre soutenu."},
            {"id": "c1locxo2", "prompt": "Remets les mots en ordre.", "words": ["Au", "sein", "de", "la", "direction,", "des", "doutes", "subsistent"], "explanation": "Au sein de exprime l'intériorité à un groupe."},
         ]},
    ],
    "c1-la-cohesion-et-la-progression-thematique": [
        {"id": "c1cohx-reading", "type": "reading-comprehension", "title": "Lecture : Un Paragraphe Bien Construit",
         "passage": "<p>La désertification menace de vastes régions du globe. Ce phénomène, déjà bien documenté, s'aggrave chaque année sous l'effet du réchauffement climatique. Ce dernier accélère l'évaporation des sols, rendant l'agriculture de plus en plus difficile. Cette situation pousse de nombreuses populations à migrer vers des zones plus fertiles.</p>",
         "items": [
            {"id": "c1cohxr1", "prompt": "Que menace la désertification ?", "options": ["De vastes régions du globe", "Uniquement les océans", "Les grandes villes"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "c1cohxr2", "prompt": "Comment le texte reprend-il « la désertification » dans la deuxième phrase ?", "options": ["Par « ce phénomène »", "En la répétant", "Il ne la reprend pas"], "answerIndex": 0, "explanation": "C'est une reprise par synonyme pour éviter la répétition."},
            {"id": "c1cohxr3", "prompt": "Que reprend « ce dernier » dans le texte ?", "options": ["Le réchauffement climatique", "La désertification", "L'agriculture"], "answerIndex": 0, "explanation": "Ce dernier désigne le référent le plus proche, le réchauffement climatique."},
            {"id": "c1cohxr4", "prompt": "Quelle est la conséquence finale décrite par le texte ?", "options": ["Des populations migrent vers des zones plus fertiles", "L'agriculture s'améliore", "Le climat se stabilise"], "answerIndex": 0, "explanation": "Le texte se termine sur cette conséquence."},
         ]},
        {"id": "c1cohx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1cohxo1", "prompt": "Remets les mots en ordre.", "words": ["Ce", "phénomène", "s'aggrave", "chaque", "année"], "explanation": "Reprise par synonyme du thème précédent."},
            {"id": "c1cohxo2", "prompt": "Remets les mots en ordre.", "words": ["Ce", "dernier", "accélère", "l'évaporation", "des", "sols"], "explanation": "Ce dernier reprend le référent le plus proche."},
         ]},
    ],
    "c1-les-registres-et-la-variation-stylistique": [
        {"id": "c1regx-reading", "type": "reading-comprehension", "title": "Lecture : Trois Messages, Trois Registres",
         "passage": "<p>Dans son roman, l'auteur écrit : « Le vent balayait la plaine, emportant avec lui les derniers échos du jour. » Dans le journal du soir, on lit : « Les vents violents pourraient s'intensifier dans la nuit, selon Météo-France. » Dans la lettre officielle reçue le matin même, il est écrit : « Nous vous prions de bien vouloir prendre vos dispositions en conséquence. »</p>",
         "items": [
            {"id": "c1regxr1", "prompt": "Quel registre utilise l'auteur du roman ?", "options": ["Littéraire", "Administratif", "Journalistique"], "answerIndex": 0, "explanation": "Image poétique et phrase longue : registre littéraire."},
            {"id": "c1regxr2", "prompt": "Que suggère le conditionnel « pourraient s'intensifier » dans le journal ?", "options": ["Une information non totalement confirmée", "Une certitude absolue", "Un événement passé"], "answerIndex": 0, "explanation": "C'est l'usage journalistique du conditionnel."},
            {"id": "c1regxr3", "prompt": "Quel registre utilise la lettre officielle ?", "options": ["Administratif", "Littéraire", "Familier"], "answerIndex": 0, "explanation": "Formule figée de politesse : registre administratif."},
            {"id": "c1regxr4", "prompt": "Combien de registres différents ce texte illustre-t-il ?", "options": ["Trois", "Un seul", "Cinq"], "answerIndex": 0, "explanation": "Littéraire, journalistique et administratif."},
         ]},
        {"id": "c1regx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1regxo1", "prompt": "Remets les mots en ordre.", "words": ["Le", "vent", "balayait", "la", "plaine"], "explanation": "Registre littéraire, imparfait descriptif."},
            {"id": "c1regxo2", "prompt": "Remets les mots en ordre.", "words": ["Les", "vents", "pourraient", "s'intensifier", "cette", "nuit"], "explanation": "Registre journalistique, conditionnel d'incertitude."},
         ]},
    ],
    "c1-lexpression-de-la-restriction-et-de-lexception": [
        {"id": "c1restx-reading", "type": "reading-comprehension", "title": "Lecture : Les Conditions de l'Offre",
         "passage": "<p>Cette offre est valable pour tous les clients, sauf ceux ayant déjà bénéficié d'une remise cette année. Il ne reste que quelques places disponibles. L'inscription sera validée, sous réserve du paiement intégral avant vendredi. Hormis les frais de dossier, aucun coût supplémentaire ne sera demandé, à moins que le client ne modifie sa réservation.</p>",
         "items": [
            {"id": "c1restxr1", "prompt": "Qui est exclu de cette offre ?", "options": ["Ceux ayant déjà bénéficié d'une remise cette année", "Les nouveaux clients", "Personne"], "answerIndex": 0, "explanation": "Sauf introduit cette exception."},
            {"id": "c1restxr2", "prompt": "Combien de places restent-ils, selon le texte ?", "options": ["Seulement quelques-unes", "Beaucoup", "Aucune"], "answerIndex": 0, "explanation": "Ne... que exprime la restriction, équivalent à seulement."},
            {"id": "c1restxr3", "prompt": "Sous quelle condition l'inscription sera-t-elle validée ?", "options": ["Le paiement intégral avant vendredi", "L'accord d'un parent", "Un examen médical"], "answerIndex": 0, "explanation": "Sous réserve de introduit cette condition formelle."},
            {"id": "c1restxr4", "prompt": "Dans quel cas un coût supplémentaire pourrait-il être demandé ?", "options": ["Si le client modifie sa réservation", "Jamais", "Toujours"], "answerIndex": 0, "explanation": "À moins que introduit cette exception au subjonctif."},
         ]},
        {"id": "c1restx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "c1restxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "ne", "reste", "que", "quelques", "places"], "explanation": "Ne... que exprime la restriction."},
            {"id": "c1restxo2", "prompt": "Remets les mots en ordre.", "words": ["Sous", "réserve", "du", "paiement", "intégral"], "explanation": "Sous réserve de + nom, condition formelle."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
