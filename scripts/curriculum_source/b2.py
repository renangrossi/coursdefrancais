# -*- coding: utf-8 -*-
"""B2 — Données du curriculum de niveau intermédiaire avancé. Voir
curriculum/SCHEMA.md pour la forme exacte du JSON vers lequel ceci est
compilé (scripts/generate_curriculum.py fait la compilation). Écrit en
Python plutôt qu'en JSON à la main pour que le HTML en ligne (rules[].body,
content.explanation) et les guillemets dans le texte puissent s'écrire
naturellement."""

OVERVIEW = (
    "Le niveau B2 complète le système du subjonctif avec le subjonctif passé "
    "et un éventail plus large de déclencheurs (opinion, doute, but, "
    "concession), puis explore les pronoms relatifs composés, l'usage du "
    "conditionnel pour une information non confirmée, et la nominalisation "
    "propre à l'écrit formel. Tu apprendras aussi à distinguer les registres "
    "de langue, à construire une argumentation avec des connecteurs "
    "sophistiqués, à maîtriser les cas complexes d'accord du participe "
    "passé, à utiliser les tournures emphatiques, et à former le futur "
    "antérieur. À la fin de ce niveau, tu pourras t'exprimer avec aisance "
    "et nuance, à l'oral comme à l'écrit, dans un registre adapté à chaque "
    "situation."
)

LESSONS = [
    {
        "id": "b2-le-subjonctif-passe",
        "level": "B2", "unit": "1", "order": 1, "skill": "grammar", "strand": "subjonctif-passe",
        "title": "Le Subjonctif Passé",
        "subtitle": "Comment former le subjonctif passé, pour une action subjective antérieure au moment de la principale.",
        "objectives": [
            "Former le subjonctif passé avec le subjonctif présent de avoir/être + participe passé.",
            "Employer le subjonctif passé quand l'action subjective est antérieure à celle de la principale.",
            "Distinguer le subjonctif présent du subjonctif passé selon la chronologie des deux actions.",
        ],
        "content": {
            "intro": "Le subjonctif présent situe une action incertaine, souhaitée ou ressentie en même temps ou après la principale ; quand cette action est déjà terminée avant, il faut passer au subjonctif passé.",
            "explanation": "<p>Le subjonctif passé se forme avec le <strong>subjonctif présent</strong> de <em>avoir</em> ou <em>être</em> + le participe passé, avec les mêmes règles d'auxiliaire et d'accord que le passé composé : <em>que j'aie fini, qu'elle soit partie, qu'ils se soient levés</em>.</p><p>Il s'emploie quand l'action introduite par <em>que</em> est <strong>antérieure</strong> à celle de la principale : <em>Je suis content que tu aies réussi ton examen</em> (la réussite précède la satisfaction). Si les deux actions sont simultanées ou que l'action subordonnée suit la principale, on garde le subjonctif présent : <em>Je suis content que tu viennes ce soir.</em></p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>Subjonctif présent de avoir/être + participe passé : <em>que j'aie parlé, que tu sois parti(e)</em>.</li></ul>"},
                {"heading": "b) Emploi", "body": "<ul><li>Action subjective antérieure à celle de la principale : <em>Je doute qu'il ait compris.</em></li></ul>"},
                {"heading": "c) Contraste avec le subjonctif présent", "body": "<ul><li>Simultanéité ou postériorité → subjonctif présent : <em>Je doute qu'il comprenne.</em></li></ul>"},
                {"heading": "d) Même accord que le passé composé", "body": "<ul><li>Les verbes pronominaux et les verbes de mouvement suivent les mêmes règles d'auxiliaire qu'ailleurs.</li></ul>"},
            ],
            "examples": [
                "Je suis content que tu aies réussi ton examen.",
                "Je doute qu'il ait compris la consigne.",
                "C'est dommage qu'elle soit partie si tôt.",
                "Il est possible qu'ils aient déjà mangé.",
                "Je regrette que nous nous soyons disputés.",
                "Je ne pense pas qu'elle ait fini le rapport.",
                "Il est étonnant que vous ayez tout terminé si vite.",
            ],
            "commonMistakes": [
                {"wrong": "Je suis content que tu réussisses ton examen (déjà passé).", "right": "Je suis content que tu aies réussi ton examen.", "why": "L'action est déjà terminée : il faut le subjonctif passé, pas le présent."},
                {"wrong": "Je doute qu'il a compris.", "right": "Je doute qu'il ait compris.", "why": "Le doute déclenche le subjonctif, ici au passé car l'action est antérieure."},
                {"wrong": "C'est dommage qu'elle soit parti si tôt.", "right": "C'est dommage qu'elle soit partie si tôt.", "why": "Le participe passé s'accorde avec le sujet féminin, elle : partie."},
            ],
        },
        "exercises": [
            {"id": "b2sbp-fill", "type": "fill-blank", "title": "Conjugue au Subjonctif Passé",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b2sbpf1", "prompt": "Je suis content que tu ___ (réussir) ton examen.", "answers": [["aies réussi"]], "options": ["aies réussi", "réussisses", "as réussi"], "explanation": "Action antérieure à la satisfaction : subjonctif passé."},
                {"id": "b2sbpf2", "prompt": "Je doute qu'il ___ (comprendre) la consigne.", "answers": [["ait compris"]], "options": ["ait compris", "comprenne", "a compris"], "explanation": "Doute + action déjà terminée : subjonctif passé."},
                {"id": "b2sbpf3", "prompt": "C'est dommage qu'elle ___ (partir) si tôt.", "answers": [["soit partie"]], "options": ["soit partie", "soit parti", "parte"], "explanation": "Partir se conjugue avec être, accord au féminin : soit partie."},
                {"id": "b2sbpf4", "prompt": "Je regrette que nous nous ___ (disputer).", "answers": [["soyons disputés"]], "options": ["soyons disputés", "disputions", "sommes disputés"], "explanation": "Verbe pronominal au subjonctif passé : avec être."},
             ]},
            {"id": "b2sbp-mc", "type": "multiple-choice", "title": "Le Subjonctif Passé",
             "items": [
                {"id": "b2sbpm1", "prompt": "Comment forme-t-on le subjonctif passé ?", "options": ["subjonctif présent de avoir/être + participe passé", "imparfait de avoir/être + participe passé", "présent de avoir/être + participe passé"], "answerIndex": 0, "explanation": "L'auxiliaire est au subjonctif présent."},
                {"id": "b2sbpm2", "prompt": "Quand utilise-t-on le subjonctif passé plutôt que le présent ?", "options": ["quand l'action subordonnée est antérieure à la principale", "quand l'action est future", "jamais, ils sont interchangeables"], "answerIndex": 0, "explanation": "L'antériorité déclenche le subjonctif passé."},
                {"id": "b2sbpm3", "prompt": "Dans « je doute qu'il ait compris », quelle action est antérieure ?", "options": ["comprendre", "douter", "aucune des deux"], "answerIndex": 0, "explanation": "Comprendre a déjà eu lieu avant le doute exprimé."},
                {"id": "b2sbpm4", "prompt": "Quel accord suit les mêmes règles qu'au subjonctif passé qu'au passé composé ?", "options": ["l'accord du participe passé", "l'accord de l'adjectif", "aucun accord"], "answerIndex": 0, "explanation": "Les mêmes règles d'auxiliaire et d'accord s'appliquent."},
             ]},
            {"id": "b2sbp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b2sbpc1", "incorrect": "Je suis content que tu réussisses ton examen (déjà passé).", "answer": ["Je suis content que tu aies réussi ton examen."], "explanation": "Action déjà terminée : subjonctif passé."},
                {"id": "b2sbpc2", "incorrect": "Je doute qu'il a compris.", "answer": ["Je doute qu'il ait compris."], "explanation": "Le doute déclenche le subjonctif, ici au passé."},
                {"id": "b2sbpc3", "incorrect": "C'est dommage qu'elle soit parti si tôt.", "answer": ["C'est dommage qu'elle soit partie si tôt."], "explanation": "Accord avec le sujet féminin."},
             ]},
        ],
        "summary": [
            "Le subjonctif passé se forme avec le subjonctif présent de avoir/être + participe passé.",
            "Il exprime une action subjective antérieure à celle de la principale ; sinon, on garde le subjonctif présent.",
            "Les mêmes règles d'auxiliaire et d'accord qu'au passé composé s'appliquent.",
        ],
    },
    {
        "id": "b2-le-subjonctif-apres-opinion-doute-but-concession",
        "level": "B2", "unit": "1", "order": 2, "skill": "grammar", "strand": "subjonctif-declencheurs-avances",
        "title": "Le Subjonctif Après l'Opinion, le Doute, le But et la Concession",
        "subtitle": "Un répertoire plus large de déclencheurs du subjonctif : bien que, pour que, à moins que, avant que.",
        "objectives": [
            "Élargir le répertoire des déclencheurs du subjonctif au-delà de il faut que et vouloir que.",
            "Employer bien que/quoique pour la concession et pour que/afin que pour le but.",
            "Reconnaître les expressions d'opinion qui basculent au subjonctif à la forme négative ou interrogative.",
        ],
        "content": {
            "intro": "Au-delà des déclencheurs de base vus au niveau B1, le français utilise le subjonctif dans un ensemble beaucoup plus large de structures — la concession, le but, la restriction — indispensables pour un discours nuancé.",
            "explanation": "<p>La <strong>concession</strong> (« malgré tout ») s'exprime avec <em>bien que</em> ou <em>quoique</em> + subjonctif : <em>Bien qu'il soit fatigué, il continue à travailler.</em> Le <strong>but</strong> s'exprime avec <em>pour que</em> ou <em>afin que</em> + subjonctif quand le sujet change entre les deux propositions : <em>Je lui explique pour qu'il comprenne.</em> La <strong>restriction</strong> s'exprime avec <em>à moins que</em> : <em>Nous partirons à moins qu'il ne pleuve.</em> L'antériorité temporelle stricte s'exprime avec <em>avant que</em> + subjonctif.</p><p>Les verbes d'opinion (<em>penser, croire, trouver</em>) restent à l'indicatif à la forme affirmative, mais basculent souvent au subjonctif à la forme négative ou interrogative, car la certitude disparaît : <em>Je trouve que c'est une bonne idée</em> (indicatif) → <em>Trouves-tu que ce soit une bonne idée ?</em> (subjonctif, incertitude).</p>",
            "rules": [
                {"heading": "a) Concession", "body": "<ul><li><em>bien que, quoique</em> + subjonctif : <em>Bien qu'il pleuve, nous sortons.</em></li></ul>"},
                {"heading": "b) But", "body": "<ul><li><em>pour que, afin que</em> + subjonctif (sujets différents) : <em>Je parle fort pour qu'il m'entende.</em></li></ul>"},
                {"heading": "c) Restriction et antériorité", "body": "<ul><li><em>à moins que, avant que</em> + subjonctif.</li></ul>"},
                {"heading": "d) Opinion à la forme négative/interrogative", "body": "<ul><li><em>penser, croire, trouver</em> négatif ou interrogatif → souvent subjonctif.</li></ul>"},
            ],
            "examples": [
                "Bien qu'il soit fatigué, il continue à travailler.",
                "Je lui explique pour qu'il comprenne.",
                "Nous partirons à moins qu'il ne pleuve.",
                "Appelle-moi avant que je parte.",
                "Trouves-tu que ce soit une bonne idée ?",
                "Quoiqu'elle soit jeune, elle a beaucoup d'expérience.",
                "Je ne crois pas qu'il vienne ce soir.",
            ],
            "commonMistakes": [
                {"wrong": "Bien qu'il est fatigué, il continue.", "right": "Bien qu'il soit fatigué, il continue.", "why": "Bien que impose toujours le subjonctif."},
                {"wrong": "Je parle fort pour qu'il m'entend.", "right": "Je parle fort pour qu'il m'entende.", "why": "Pour que impose le subjonctif quand le sujet change de proposition."},
                {"wrong": "Je trouve que c'est une bonne idée (au subjonctif).", "right": "Je trouve que c'est une bonne idée.", "why": "Trouver que à la forme affirmative reste à l'indicatif, la certitude est présente."},
            ],
        },
        "exercises": [
            {"id": "b2sbo-fill", "type": "fill-blank", "title": "Complète avec le Subjonctif",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b2sbof1", "prompt": "Bien qu'il ___ (être) fatigué, il continue.", "answers": [["soit"]], "options": ["soit", "est", "sera"], "explanation": "Bien que impose le subjonctif."},
                {"id": "b2sbof2", "prompt": "Je lui explique pour qu'il ___ (comprendre).", "answers": [["comprenne"]], "options": ["comprenne", "comprend", "comprendra"], "explanation": "Pour que + sujets différents → subjonctif."},
                {"id": "b2sbof3", "prompt": "Nous partirons à moins qu'il ne ___ (pleuvoir).", "answers": [["pleuve"]], "options": ["pleuve", "pleut", "pleuvra"], "explanation": "À moins que impose le subjonctif."},
                {"id": "b2sbof4", "prompt": "Appelle-moi avant que je ne ___ (partir).", "answers": [["parte"]], "options": ["parte", "pars", "partirai"], "explanation": "Avant que impose le subjonctif."},
             ]},
            {"id": "b2sbo-mc", "type": "multiple-choice", "title": "Subjonctif : Opinion, Doute, But, Concession",
             "items": [
                {"id": "b2sbom1", "prompt": "Quelle conjonction exprime la concession ?", "options": ["bien que", "pour que", "parce que"], "answerIndex": 0, "explanation": "Bien que/quoique expriment la concession."},
                {"id": "b2sbom2", "prompt": "Quelle conjonction exprime le but ?", "options": ["pour que", "bien que", "à moins que"], "answerIndex": 0, "explanation": "Pour que/afin que expriment le but."},
                {"id": "b2sbom3", "prompt": "« Je trouve que c'est une bonne idée » est-il à l'indicatif ou au subjonctif ?", "options": ["indicatif, car affirmatif", "subjonctif, toujours", "cela dépend du sujet"], "answerIndex": 0, "explanation": "Trouver que affirmatif reste à l'indicatif."},
                {"id": "b2sbom4", "prompt": "Que se passe-t-il souvent avec « penser que » à la forme interrogative ?", "options": ["le verbe passe au subjonctif", "rien ne change", "le verbe passe au conditionnel"], "answerIndex": 0, "explanation": "La forme interrogative introduit une incertitude."},
             ]},
            {"id": "b2sbo-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b2sboc1", "incorrect": "Bien qu'il est fatigué, il continue.", "answer": ["Bien qu'il soit fatigué, il continue."], "explanation": "Bien que impose le subjonctif."},
                {"id": "b2sboc2", "incorrect": "Je parle fort pour qu'il m'entend.", "answer": ["Je parle fort pour qu'il m'entende."], "explanation": "Pour que impose le subjonctif."},
                {"id": "b2sboc3", "incorrect": "Nous partirons à moins qu'il ne pleut.", "answer": ["Nous partirons à moins qu'il ne pleuve."], "explanation": "À moins que impose le subjonctif."},
             ]},
        ],
        "summary": [
            "Bien que/quoique (concession) et pour que/afin que (but, sujets différents) imposent le subjonctif.",
            "À moins que (restriction) et avant que (antériorité) imposent aussi le subjonctif.",
            "Penser/croire/trouver restent à l'indicatif à la forme affirmative, mais basculent souvent au subjonctif à la forme négative ou interrogative.",
        ],
    },
    {
        "id": "b2-les-pronoms-relatifs-composes",
        "level": "B2", "unit": "1", "order": 3, "skill": "grammar", "strand": "relatifs-composes",
        "title": "Les Pronoms Relatifs Composés",
        "subtitle": "Lequel, auquel, duquel : les pronoms relatifs utilisés après une préposition.",
        "objectives": [
            "Utiliser lequel/laquelle/lesquels/lesquelles après une préposition.",
            "Contracter lequel avec à et de (auquel, duquel) et leurs formes plurielles.",
            "Distinguer l'emploi des relatifs composés de celui de qui, que, où, dont vus au niveau B1.",
        ],
        "content": {
            "intro": "Après une préposition autre que de, le français n'utilise pas qui pour les choses : il faut un pronom relatif composé, qui s'accorde en genre et en nombre avec son antécédent.",
            "explanation": "<p><strong>Lequel, laquelle, lesquels, lesquelles</strong> remplacent un nom (généralement une chose) après une préposition : <em>le stylo avec lequel j'écris, la raison pour laquelle il est parti</em>. Avec <em>à</em>, ils se contractent : <em>à + lequel → auquel, à + lesquels → auxquels, à + lesquelles → auxquelles</em> (laquelle ne se contracte pas : <em>à laquelle</em>).</p><p>Avec <em>de</em>, ils se contractent aussi : <em>de + lequel → duquel, de + lesquels → desquels, de + lesquelles → desquelles</em> (laquelle ne se contracte pas : <em>de laquelle</em>). Pour une <strong>personne</strong> après une préposition, on préfère généralement <em>qui</em> : <em>la personne à qui je parle</em>, plutôt que <em>à laquelle</em>, sauf après <em>parmi</em> et <em>entre</em>, où lequel reste obligatoire même pour des personnes.</p>",
            "rules": [
                {"heading": "a) Forme de base", "body": "<ul><li><em>lequel, laquelle, lesquels, lesquelles</em>, accordés avec l'antécédent.</li></ul>"},
                {"heading": "b) Contraction avec à", "body": "<ul><li><em>auquel, à laquelle, auxquels, auxquelles</em>.</li></ul>"},
                {"heading": "c) Contraction avec de", "body": "<ul><li><em>duquel, de laquelle, desquels, desquelles</em>.</li></ul>"},
                {"heading": "d) Personnes", "body": "<ul><li>On préfère <em>qui</em> pour les personnes après une préposition simple : <em>l'ami à qui j'écris</em>.</li></ul>"},
            ],
            "examples": [
                "Le stylo avec lequel j'écris est cassé.",
                "La raison pour laquelle il est parti reste inconnue.",
                "Le projet auquel je pense est ambitieux.",
                "La ville dans laquelle j'habite est petite.",
                "Les amis parmi lesquels je vis sont formidables.",
                "L'entreprise pour laquelle elle travaille est jeune.",
                "L'ami à qui j'écris habite loin.",
            ],
            "commonMistakes": [
                {"wrong": "Le projet à lequel je pense est ambitieux.", "right": "Le projet auquel je pense est ambitieux.", "why": "À + lequel se contracte obligatoirement en auquel."},
                {"wrong": "La ville dans lequel j'habite est petite.", "right": "La ville dans laquelle j'habite est petite.", "why": "Laquelle s'accorde au féminin avec ville."},
                {"wrong": "L'ami auquel j'écris habite loin.", "right": "L'ami à qui j'écris habite loin.", "why": "Pour une personne après une préposition simple, on préfère qui à lequel."},
            ],
        },
        "exercises": [
            {"id": "b2rc-fill", "type": "fill-blank", "title": "Complète avec le Pronom Relatif Composé",
             "instructions": "Choisis la forme correcte.",
             "items": [
                {"id": "b2rcf1", "prompt": "Le projet ___ je pense est ambitieux.", "answers": [["auquel"]], "options": ["auquel", "à lequel", "duquel"], "explanation": "À + lequel se contracte en auquel."},
                {"id": "b2rcf2", "prompt": "La ville dans ___ j'habite est petite.", "answers": [["laquelle"]], "options": ["laquelle", "lequel", "lesquelles"], "explanation": "Laquelle s'accorde au féminin avec ville."},
                {"id": "b2rcf3", "prompt": "Les amis parmi ___ je vis sont formidables.", "answers": [["lesquels"]], "options": ["lesquels", "qui", "dont"], "explanation": "Après parmi, on utilise lesquels même pour des personnes."},
                {"id": "b2rcf4", "prompt": "L'ami à ___ j'écris habite loin.", "answers": [["qui"]], "options": ["qui", "auquel", "lequel"], "explanation": "Pour une personne après une préposition simple, on préfère qui."},
             ]},
            {"id": "b2rc-mc", "type": "multiple-choice", "title": "Les Pronoms Relatifs Composés",
             "items": [
                {"id": "b2rcm1", "prompt": "Comment se contracte à + lequel ?", "options": ["auquel", "alequel", "à lequel"], "answerIndex": 0, "explanation": "La contraction obligatoire donne auquel."},
                {"id": "b2rcm2", "prompt": "Comment se contracte de + lesquels ?", "options": ["desquels", "de lesquels", "duxquels"], "answerIndex": 0, "explanation": "La contraction obligatoire donne desquels."},
                {"id": "b2rcm3", "prompt": "Laquelle se contracte-t-elle avec à ?", "options": ["non, elle reste à laquelle", "oui, en alaquelle", "oui, en auquelle"], "answerIndex": 0, "explanation": "Laquelle ne se contracte jamais."},
                {"id": "b2rcm4", "prompt": "Quel pronom préfère-t-on pour une personne après une préposition simple ?", "options": ["qui", "lequel", "dont"], "answerIndex": 0, "explanation": "Qui est préféré pour les personnes, sauf après parmi/entre."},
             ]},
            {"id": "b2rc-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b2rcc1", "incorrect": "Le projet à lequel je pense est ambitieux.", "answer": ["Le projet auquel je pense est ambitieux."], "explanation": "Contraction obligatoire : auquel."},
                {"id": "b2rcc2", "incorrect": "La ville dans lequel j'habite est petite.", "answer": ["La ville dans laquelle j'habite est petite."], "explanation": "Accord au féminin avec ville."},
                {"id": "b2rcc3", "incorrect": "L'ami auquel j'écris habite loin.", "answer": ["L'ami à qui j'écris habite loin."], "explanation": "Qui est préféré pour une personne."},
             ]},
        ],
        "summary": [
            "Lequel/laquelle/lesquels/lesquelles remplacent un nom après une préposition.",
            "Ils se contractent avec à (auquel, auxquels, auxquelles) et avec de (duquel, desquels, desquelles), sauf laquelle.",
            "Pour une personne après une préposition simple, on préfère qui à lequel, sauf après parmi/entre.",
        ],
    },
    {
        "id": "b2-le-conditionnel-information-non-confirmee",
        "level": "B2", "unit": "1", "order": 4, "skill": "grammar", "strand": "conditionnel-non-confirme",
        "title": "Le Conditionnel pour une Information Non Confirmée",
        "subtitle": "Comment le français utilise le conditionnel dans la presse pour signaler une information qui n'est pas encore certaine.",
        "objectives": [
            "Reconnaître l'usage journalistique du conditionnel pour une information non confirmée.",
            "Distinguer cet usage du conditionnel de politesse et du conditionnel hypothétique déjà connus.",
            "Reformuler une information certaine (indicatif) en information non confirmée (conditionnel).",
        ],
        "content": {
            "intro": "Dans la presse et les communiqués officiels, le conditionnel a un troisième emploi, différent de la politesse ou de l'hypothèse : il signale qu'une information circule sans être encore vérifiée.",
            "explanation": "<p>Au lieu d'affirmer un fait avec l'indicatif, un journaliste utilise le <strong>conditionnel</strong> pour présenter une information dont la source n'est pas garantie : <em>Le ministre aurait démissionné ce matin</em> (on ne l'affirme pas comme un fait certain, seulement rapporté). C'est un usage très fréquent dans les titres de presse, les dépêches et les communiqués de police.</p><p>Cet emploi est distinct des deux autres usages du conditionnel déjà connus : la politesse (<em>je voudrais</em>) et l'hypothèse (<em>si j'avais le temps, je viendrais</em>). Ici, il n'y a ni condition ni politesse : seulement une réserve sur la véracité de l'information, souvent renforcée par <em>selon, d'après</em>.</p>",
            "rules": [
                {"heading": "a) Usage journalistique", "body": "<ul><li>Conditionnel présent ou passé pour une information non confirmée : <em>Il y aurait eu un accident.</em></li></ul>"},
                {"heading": "b) Marqueurs fréquents", "body": "<ul><li><em>selon, d'après, il semblerait que</em> accompagnent souvent cet emploi.</li></ul>"},
                {"heading": "c) Distinction", "body": "<ul><li>Différent du conditionnel de politesse et du conditionnel hypothétique : ici, aucune condition n'est exprimée.</li></ul>"},
                {"heading": "d) Contexte", "body": "<ul><li>Très fréquent en presse écrite, à la radio et dans les communiqués officiels.</li></ul>"},
            ],
            "examples": [
                "Le ministre aurait démissionné ce matin.",
                "Il y aurait eu un accident sur l'autoroute.",
                "Selon des sources proches du dossier, l'accord serait signé demain.",
                "Le nombre de victimes serait plus élevé que prévu.",
                "L'entreprise aurait licencié cent employés, d'après nos informations.",
                "Il semblerait que la réunion ait été annulée.",
                "Les négociations auraient repris hier soir.",
            ],
            "commonMistakes": [
                {"wrong": "Le ministre a démissionné ce matin (information non vérifiée).", "right": "Le ministre aurait démissionné ce matin.", "why": "Une information non confirmée s'annonce au conditionnel, pas à l'indicatif."},
                {"wrong": "Il y aura eu un accident sur l'autoroute.", "right": "Il y aurait eu un accident sur l'autoroute.", "why": "C'est le conditionnel, pas le futur antérieur, qui marque l'information non confirmée."},
                {"wrong": "Si l'accord serait signé, ce serait une bonne nouvelle (usage journalistique confondu avec l'hypothèse).", "right": "Si l'accord est signé, ce sera une bonne nouvelle.", "why": "Après si, on n'utilise jamais le conditionnel ; cette phrase est une hypothèse réelle, pas une information non confirmée."},
            ],
        },
        "exercises": [
            {"id": "b2cnc-fill", "type": "fill-blank", "title": "Complète avec le Conditionnel Journalistique",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b2cncf1", "prompt": "Le ministre ___ (démissionner) ce matin, selon nos informations.", "answers": [["aurait démissionné"]], "options": ["aurait démissionné", "a démissionné", "démissionnerait"], "explanation": "Information non confirmée : conditionnel passé."},
                {"id": "b2cncf2", "prompt": "Il y ___ (avoir) un accident sur l'autoroute.", "answers": [["aurait eu"]], "options": ["aurait eu", "aura eu", "a eu"], "explanation": "Conditionnel passé pour une information non vérifiée."},
                {"id": "b2cncf3", "prompt": "L'accord ___ (être) signé demain, d'après des sources proches.", "answers": [["serait"]], "options": ["serait", "sera", "est"], "explanation": "Conditionnel présent pour une information rapportée."},
                {"id": "b2cncf4", "prompt": "Les négociations ___ (reprendre) hier soir.", "answers": [["auraient repris"]], "options": ["auraient repris", "ont repris", "reprendraient"], "explanation": "Conditionnel passé, information rapportée au passé."},
             ]},
            {"id": "b2cnc-mc", "type": "multiple-choice", "title": "Le Conditionnel Journalistique",
             "items": [
                {"id": "b2cncm1", "prompt": "Pourquoi la presse utilise-t-elle le conditionnel ?", "options": ["pour signaler une information non confirmée", "par politesse", "pour exprimer une hypothèse"], "answerIndex": 0, "explanation": "C'est l'usage journalistique du conditionnel."},
                {"id": "b2cncm2", "prompt": "Quels mots accompagnent souvent cet emploi ?", "options": ["selon, d'après", "si, à condition que", "bien que, quoique"], "answerIndex": 0, "explanation": "Ces marqueurs signalent la source de l'information."},
                {"id": "b2cncm3", "prompt": "Cet emploi du conditionnel exprime-t-il une condition ?", "options": ["non, aucune condition", "oui, toujours", "seulement au passé"], "answerIndex": 0, "explanation": "Il n'y a ni condition ni politesse, seulement une réserve sur la véracité."},
                {"id": "b2cncm4", "prompt": "Où rencontre-t-on le plus souvent cet emploi ?", "options": ["dans la presse et les communiqués officiels", "dans les recettes de cuisine", "dans les lettres d'amour"], "answerIndex": 0, "explanation": "C'est un usage typique du style journalistique."},
             ]},
            {"id": "b2cnc-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b2cncc1", "incorrect": "Le ministre a démissionné ce matin (information non vérifiée).", "answer": ["Le ministre aurait démissionné ce matin."], "explanation": "Information non confirmée : conditionnel."},
                {"id": "b2cncc2", "incorrect": "Il y aura eu un accident sur l'autoroute.", "answer": ["Il y aurait eu un accident sur l'autoroute."], "explanation": "Le conditionnel marque l'information non confirmée, pas le futur antérieur."},
                {"id": "b2cncc3", "incorrect": "Si l'accord serait signé, ce serait une bonne nouvelle.", "answer": ["Si l'accord est signé, ce sera une bonne nouvelle."], "explanation": "Jamais de conditionnel juste après si."},
             ]},
        ],
        "summary": [
            "Le conditionnel signale, dans la presse et les communiqués officiels, une information non encore confirmée.",
            "Il est souvent accompagné de selon, d'après, il semblerait que.",
            "Cet emploi est distinct du conditionnel de politesse et du conditionnel hypothétique après si.",
        ],
    },
    {
        "id": "b2-la-nominalisation",
        "level": "B2", "unit": "1", "order": 5, "skill": "grammar", "strand": "nominalisation",
        "title": "La Nominalisation",
        "subtitle": "Comment transformer un verbe ou un adjectif en nom, pour un style plus formel et plus condensé.",
        "objectives": [
            "Former des noms à partir de verbes fréquents à l'aide des suffixes les plus courants.",
            "Former des noms à partir d'adjectifs fréquents.",
            "Reformuler une phrase verbale en phrase nominale pour un registre plus soutenu.",
        ],
        "content": {
            "intro": "L'écrit formel français préfère souvent une construction nominale à une construction verbale — un style plus condensé et plus abstrait, fréquent dans la presse, les rapports et les textes administratifs.",
            "explanation": "<p>La <strong>nominalisation</strong> transforme un verbe en nom, le plus souvent avec les suffixes <em>-tion/-sion</em> (<em>décider → la décision, informer → l'information</em>), <em>-ment</em> (<em>changer → le changement</em>), <em>-age</em> (<em>arrêter → l'arrêtage</em>, rare) ou une forme propre à mémoriser (<em>arriver → l'arrivée, choisir → le choix</em>). Elle transforme aussi des <strong>adjectifs</strong> en noms, avec <em>-té/-ité</em> (<em>possible → la possibilité, réel → la réalité</em>) ou <em>-esse</em> (<em>faible → la faiblesse</em>).</p><p>La nominalisation permet de condenser une phrase verbale en une expression plus courte et plus formelle : <em>Le gouvernement a décidé d'augmenter les impôts</em> devient <em>La décision du gouvernement d'augmenter les impôts…</em>. Ce procédé est très fréquent dans les titres de presse et les rapports officiels.</p>",
            "rules": [
                {"heading": "a) Suffixe -tion/-sion", "body": "<ul><li><em>décider → la décision, informer → l'information, produire → la production</em>.</li></ul>"},
                {"heading": "b) Suffixe -ment", "body": "<ul><li><em>changer → le changement, développer → le développement</em>.</li></ul>"},
                {"heading": "c) Formes à mémoriser", "body": "<ul><li><em>arriver → l'arrivée, choisir → le choix, partir → le départ</em>.</li></ul>"},
                {"heading": "d) Adjectifs → noms", "body": "<ul><li><em>-té/-ité : possible → la possibilité</em>. <em>-esse : faible → la faiblesse</em>.</li></ul>"},
            ],
            "examples": [
                "La décision du gouvernement a surpris tout le monde.",
                "L'information a été diffusée ce matin.",
                "Le changement climatique inquiète les scientifiques.",
                "Son arrivée a été retardée par la neige.",
                "La possibilité d'un accord reste ouverte.",
                "Le développement de la ville s'accélère.",
                "La faiblesse de l'économie explique cette crise.",
            ],
            "commonMistakes": [
                {"wrong": "La décidement du gouvernement a surpris tout le monde.", "right": "La décision du gouvernement a surpris tout le monde.", "why": "Décider se nominalise en décision, pas en décidement."},
                {"wrong": "Son arrivement a été retardé.", "right": "Son arrivée a été retardée.", "why": "Arriver se nominalise en arrivée, une forme irrégulière à mémoriser."},
                {"wrong": "La possibleté d'un accord reste ouverte.", "right": "La possibilité d'un accord reste ouverte.", "why": "Possible se nominalise en possibilité, avec le suffixe -ité."},
            ],
        },
        "exercises": [
            {"id": "b2nom-fill", "type": "fill-blank", "title": "Nominalise le Verbe ou l'Adjectif",
             "instructions": "Écris la forme nominale correcte.",
             "items": [
                {"id": "b2nomf1", "prompt": "décider → la ___", "answers": [["décision"]], "options": ["décision", "décidement", "décidage"], "explanation": "Décider se nominalise en décision."},
                {"id": "b2nomf2", "prompt": "arriver → l'___", "answers": [["arrivée"]], "options": ["arrivée", "arrivement", "arrivation"], "explanation": "Arriver se nominalise en arrivée, forme irrégulière."},
                {"id": "b2nomf3", "prompt": "possible → la ___", "answers": [["possibilité"]], "options": ["possibilité", "possibleté", "possibilage"], "explanation": "Possible se nominalise en possibilité."},
                {"id": "b2nomf4", "prompt": "changer → le ___", "answers": [["changement"]], "options": ["changement", "changision", "changerie"], "explanation": "Changer se nominalise en changement."},
             ]},
            {"id": "b2nom-mc", "type": "multiple-choice", "title": "La Nominalisation",
             "items": [
                {"id": "b2nomm1", "prompt": "Quel suffixe transforme souvent un verbe en nom ?", "options": ["-tion/-sion", "-ard", "-ette"], "answerIndex": 0, "explanation": "C'est le suffixe le plus productif pour la nominalisation verbale."},
                {"id": "b2nomm2", "prompt": "Comment se nominalise choisir ?", "options": ["le choix", "le choisement", "la choisition"], "answerIndex": 0, "explanation": "Choisir a une nominalisation irrégulière : le choix."},
                {"id": "b2nomm3", "prompt": "Quel suffixe transforme souvent un adjectif en nom ?", "options": ["-té/-ité", "-eur", "-oir"], "answerIndex": 0, "explanation": "C'est le suffixe le plus courant pour cette transformation."},
                {"id": "b2nomm4", "prompt": "Pourquoi utilise-t-on la nominalisation à l'écrit formel ?", "options": ["pour un style plus condensé et abstrait", "pour simplifier le vocabulaire", "pour éviter les accords"], "answerIndex": 0, "explanation": "C'est un procédé stylistique propre au registre formel."},
             ]},
            {"id": "b2nom-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b2nomc1", "incorrect": "La décidement du gouvernement a surpris tout le monde.", "answer": ["La décision du gouvernement a surpris tout le monde."], "explanation": "Nominalisation correcte : décision."},
                {"id": "b2nomc2", "incorrect": "Son arrivement a été retardé.", "answer": ["Son arrivée a été retardée."], "explanation": "Nominalisation irrégulière : arrivée."},
                {"id": "b2nomc3", "incorrect": "La possibleté d'un accord reste ouverte.", "answer": ["La possibilité d'un accord reste ouverte."], "explanation": "Nominalisation correcte : possibilité."},
             ]},
        ],
        "summary": [
            "La nominalisation transforme un verbe (souvent -tion/-sion, -ment) ou un adjectif (-té/-ité, -esse) en nom.",
            "Certaines formes sont irrégulières à mémoriser : arriver → l'arrivée, choisir → le choix.",
            "Ce procédé condense une phrase verbale en expression nominale, fréquent en presse et à l'écrit formel.",
        ],
    },
    {
        "id": "b2-le-registre-soutenu-et-familier",
        "level": "B2", "unit": "1", "order": 6, "skill": "vocabulary", "strand": "registres",
        "title": "Le Registre Soutenu, le Registre Familier et les Figures de Style",
        "subtitle": "Reconnaître et adapter son niveau de langue selon la situation, du familier au soutenu.",
        "objectives": [
            "Distinguer le vocabulaire et les structures du registre familier, courant et soutenu.",
            "Reconnaître l'inversion du sujet dans les questions au registre soutenu.",
            "Identifier les figures de style les plus courantes : métaphore, comparaison, hyperbole.",
        ],
        "content": {
            "intro": "Un même message peut se dire très différemment selon la situation : entre amis, on simplifie et on relâche la grammaire ; à l'écrit formel ou devant un public, on choisit des structures plus soignées.",
            "explanation": "<p>Le <strong>registre familier</strong> (oral, entre proches) laisse souvent tomber le <em>ne</em> de la négation (<em>je sais pas</em> pour <em>je ne sais pas</em>) et utilise un vocabulaire relâché (<em>bouffer, un mec, un truc</em>). Le <strong>registre courant</strong> est le français standard, celui qu'on apprend en cours. Le <strong>registre soutenu</strong> (écrit formel, discours) utilise un vocabulaire plus précis, des phrases plus longues, et l'<strong>inversion du sujet</strong> dans les questions (<em>Que pensez-vous ?</em> plutôt que <em>Qu'est-ce que vous pensez ?</em>).</p><p>Les <strong>figures de style</strong> enrichissent l'expression : la <strong>métaphore</strong> compare sans mot de comparaison (<em>le temps est un voleur</em>), la <strong>comparaison</strong> utilise <em>comme</em> ou <em>tel que</em> (<em>rapide comme l'éclair</em>), et l'<strong>hyperbole</strong> exagère volontairement (<em>je meurs de faim, il pleut des cordes</em>).</p>",
            "rules": [
                {"heading": "a) Registre familier", "body": "<ul><li>Chute du ne, vocabulaire relâché : <em>je sais pas, un mec, un truc</em>.</li></ul>"},
                {"heading": "b) Registre soutenu", "body": "<ul><li>Inversion du sujet dans les questions : <em>Que pensez-vous de ce projet ?</em></li></ul>"},
                {"heading": "c) Métaphore et comparaison", "body": "<ul><li>Métaphore : sans mot de comparaison. Comparaison : avec comme/tel que.</li></ul>"},
                {"heading": "d) Hyperbole", "body": "<ul><li>Exagération volontaire : <em>je meurs de faim, il pleut des cordes</em>.</li></ul>"},
            ],
            "examples": [
                "Je sais pas si je viendrai. (familier)",
                "Je ne sais pas si je viendrai. (courant)",
                "Que pensez-vous de cette proposition ? (soutenu)",
                "Le temps est un voleur silencieux. (métaphore)",
                "Elle court comme le vent. (comparaison)",
                "J'ai une faim de loup ! (hyperbole)",
                "Un mec sympa m'a filé un coup de main. (familier)",
            ],
            "commonMistakes": [
                {"wrong": "Utiliser « je sais pas » dans une lettre officielle.", "right": "Utiliser « je ne sais pas » ou une formulation soutenue.", "why": "Le registre familier est réservé à l'oral entre proches, jamais à l'écrit formel."},
                {"wrong": "Qu'est-ce que vous pensez ? (dans un discours officiel)", "right": "Que pensez-vous ? (avec inversion, registre soutenu)", "why": "Le registre soutenu privilégie l'inversion du sujet dans les questions."},
                {"wrong": "Confondre métaphore et comparaison.", "right": "La métaphore ne contient pas de mot de comparaison ; la comparaison en contient un (comme, tel que).", "why": "C'est la présence ou l'absence du mot de comparaison qui distingue les deux figures."},
            ],
        },
        "exercises": [
            {"id": "b2reg-fill", "type": "fill-blank", "title": "Identifie le Registre ou la Figure",
             "instructions": "Choisis la réponse correcte.",
             "items": [
                {"id": "b2regf1", "prompt": "« Je sais pas » appartient au registre ___.", "answers": [["familier"]], "options": ["familier", "soutenu", "courant"], "explanation": "La chute du ne est typique du registre familier oral."},
                {"id": "b2regf2", "prompt": "« Que pensez-vous ? » appartient au registre ___.", "answers": [["soutenu"]], "options": ["soutenu", "familier", "courant"], "explanation": "L'inversion du sujet est typique du registre soutenu."},
                {"id": "b2regf3", "prompt": "« Le temps est un voleur » est une ___.", "answers": [["métaphore"]], "options": ["métaphore", "comparaison", "hyperbole"], "explanation": "Aucun mot de comparaison : c'est une métaphore."},
                {"id": "b2regf4", "prompt": "« Rapide comme l'éclair » est une ___.", "answers": [["comparaison"]], "options": ["comparaison", "métaphore", "hyperbole"], "explanation": "Le mot comme introduit une comparaison."},
             ]},
            {"id": "b2reg-mc", "type": "multiple-choice", "title": "Registres et Figures de Style",
             "items": [
                {"id": "b2regm1", "prompt": "Que perd souvent la négation au registre familier ?", "options": ["le ne", "le pas", "le verbe"], "answerIndex": 0, "explanation": "« Je sais pas » pour « je ne sais pas »."},
                {"id": "b2regm2", "prompt": "Qu'est-ce qui caractérise une question au registre soutenu ?", "options": ["l'inversion du sujet", "l'usage de est-ce que", "l'intonation seule"], "answerIndex": 0, "explanation": "L'inversion est typique du registre soutenu."},
                {"id": "b2regm3", "prompt": "Quelle figure de style exagère volontairement ?", "options": ["l'hyperbole", "la métaphore", "la comparaison"], "answerIndex": 0, "explanation": "L'hyperbole exagère pour marquer l'effet."},
                {"id": "b2regm4", "prompt": "Quelle figure compare sans mot de comparaison ?", "options": ["la métaphore", "la comparaison", "l'hyperbole"], "answerIndex": 0, "explanation": "La métaphore fait une comparaison implicite."},
             ]},
            {"id": "b2reg-correction", "type": "correction", "title": "Corrige le Registre",
             "items": [
                {"id": "b2regc1", "incorrect": "Je sais pas (dans une lettre formelle).", "answer": ["Je ne sais pas."], "explanation": "Le registre familier est réservé à l'oral entre proches."},
                {"id": "b2regc2", "incorrect": "Qu'est-ce que vous pensez ? (dans un discours officiel)", "answer": ["Que pensez-vous ?"], "explanation": "Le registre soutenu privilégie l'inversion."},
                {"id": "b2regc3", "incorrect": "Le temps est comme un voleur (pour désigner une métaphore).", "answer": ["Le temps est un voleur."], "explanation": "La métaphore ne contient pas de mot de comparaison."},
             ]},
        ],
        "summary": [
            "Le registre familier relâche la grammaire (chute du ne) et le vocabulaire ; le registre soutenu privilégie l'inversion du sujet et un vocabulaire précis.",
            "La métaphore compare sans mot de comparaison, la comparaison utilise comme/tel que, l'hyperbole exagère volontairement.",
            "Adapter son registre à la situation est une compétence essentielle du niveau B2.",
        ],
    },
    {
        "id": "b2-les-connecteurs-argumentatifs-avances",
        "level": "B2", "unit": "1", "order": 7, "skill": "writing", "strand": "connecteurs-avances",
        "title": "Les Connecteurs Argumentatifs Avancés",
        "subtitle": "Structurer une argumentation écrite avec d'une part/d'autre part, en revanche, néanmoins, par conséquent.",
        "objectives": [
            "Structurer une argumentation en deux temps avec d'une part/d'autre part.",
            "Nuancer une opposition avec en revanche, néanmoins, cependant.",
            "Enchaîner une conséquence avec par conséquent, en outre, ceci dit.",
        ],
        "content": {
            "intro": "Un texte argumentatif bien construit ne s'appuie pas seulement sur des idées solides, mais aussi sur des connecteurs qui organisent clairement leur enchaînement pour le lecteur.",
            "explanation": "<p>Pour présenter deux aspects d'une même question, le français utilise <strong>d'une part… d'autre part</strong> : <em>D'une part, ce projet coûte cher ; d'autre part, il crée des emplois.</em> Pour marquer une opposition nuancée, on utilise <strong>en revanche, néanmoins, cependant</strong> (plus soutenus que <em>mais</em>) : <em>Le projet est coûteux ; néanmoins, il reste rentable à long terme.</em></p><p>Pour enchaîner une conséquence à l'écrit formel, on utilise <strong>par conséquent, de ce fait</strong> ; pour ajouter un argument supplémentaire, <strong>en outre, de plus</strong> ; et pour conclure ou nuancer en fin de paragraphe, <strong>ceci dit, cela étant</strong> introduit une réserve après une affirmation.</p>",
            "rules": [
                {"heading": "a) Structuration en deux temps", "body": "<ul><li><em>d'une part… d'autre part</em>.</li></ul>"},
                {"heading": "b) Opposition nuancée", "body": "<ul><li><em>en revanche, néanmoins, cependant</em> — plus soutenus que mais.</li></ul>"},
                {"heading": "c) Conséquence et ajout", "body": "<ul><li><em>par conséquent, de ce fait</em> (conséquence) ; <em>en outre, de plus</em> (ajout).</li></ul>"},
                {"heading": "d) Réserve finale", "body": "<ul><li><em>ceci dit, cela étant</em> — nuance une affirmation précédente.</li></ul>"},
            ],
            "examples": [
                "D'une part, ce projet coûte cher ; d'autre part, il crée des emplois.",
                "Le projet est coûteux ; néanmoins, il reste rentable à long terme.",
                "Il pleut ; par conséquent, la sortie est annulée.",
                "Ce candidat est compétent ; en outre, il parle trois langues.",
                "Le prix a augmenté ; en revanche, la qualité s'est améliorée.",
                "Ceci dit, il reste des points à clarifier.",
                "De ce fait, nous avons dû reporter la réunion.",
            ],
            "commonMistakes": [
                {"wrong": "D'une part, ce projet coûte cher. Et d'autre part, il crée des emplois (répété sans lien).", "right": "D'une part, ce projet coûte cher ; d'autre part, il crée des emplois.", "why": "D'une part appelle toujours d'autre part dans la même argumentation, formant une paire liée."},
                {"wrong": "Il pleut ; néanmoins, la sortie est annulée.", "right": "Il pleut ; par conséquent, la sortie est annulée.", "why": "Néanmoins marque une opposition, pas une conséquence : ici il faut par conséquent."},
                {"wrong": "Le projet est coûteux ; par conséquent, il reste rentable.", "right": "Le projet est coûteux ; néanmoins, il reste rentable.", "why": "Il y a une opposition (coûteux mais rentable), pas une conséquence logique directe."},
            ],
        },
        "exercises": [
            {"id": "b2con-fill", "type": "fill-blank", "title": "Complète avec le Bon Connecteur",
             "instructions": "Choisis le connecteur qui convient.",
             "items": [
                {"id": "b2conf1", "prompt": "Il pleut ; ___, la sortie est annulée.", "answers": [["par conséquent"]], "options": ["par conséquent", "néanmoins", "d'une part"], "explanation": "C'est une conséquence logique."},
                {"id": "b2conf2", "prompt": "Le projet est coûteux ; ___, il reste rentable.", "answers": [["néanmoins"]], "options": ["néanmoins", "par conséquent", "en outre"], "explanation": "C'est une opposition nuancée."},
                {"id": "b2conf3", "prompt": "___, ce projet coûte cher ; d'autre part, il crée des emplois.", "answers": [["D'une part"]], "options": ["D'une part", "En revanche", "Ceci dit"], "explanation": "D'une part appelle d'autre part."},
                {"id": "b2conf4", "prompt": "Ce candidat est compétent ; ___, il parle trois langues.", "answers": [["en outre"]], "options": ["en outre", "cependant", "par conséquent"], "explanation": "C'est un argument supplémentaire, pas une opposition."},
             ]},
            {"id": "b2con-mc", "type": "multiple-choice", "title": "Les Connecteurs Argumentatifs",
             "items": [
                {"id": "b2conm1", "prompt": "Quel connecteur appelle toujours d'autre part ?", "options": ["d'une part", "en outre", "néanmoins"], "answerIndex": 0, "explanation": "Ils forment toujours une paire liée."},
                {"id": "b2conm2", "prompt": "Quel connecteur marque une conséquence à l'écrit formel ?", "options": ["par conséquent", "en revanche", "d'une part"], "answerIndex": 0, "explanation": "Par conséquent introduit une conséquence logique."},
                {"id": "b2conm3", "prompt": "Quel connecteur introduit une réserve après une affirmation ?", "options": ["ceci dit", "en outre", "par conséquent"], "answerIndex": 0, "explanation": "Ceci dit nuance ce qui vient d'être dit."},
                {"id": "b2conm4", "prompt": "Quel connecteur ajoute un argument supplémentaire ?", "options": ["en outre", "néanmoins", "par conséquent"], "answerIndex": 0, "explanation": "En outre/de plus ajoutent un argument."},
             ]},
            {"id": "b2con-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b2conc1", "incorrect": "Il pleut ; néanmoins, la sortie est annulée.", "answer": ["Il pleut ; par conséquent, la sortie est annulée."], "explanation": "C'est une conséquence, pas une opposition."},
                {"id": "b2conc2", "incorrect": "Le projet est coûteux ; par conséquent, il reste rentable.", "answer": ["Le projet est coûteux ; néanmoins, il reste rentable."], "explanation": "C'est une opposition, pas une conséquence."},
                {"id": "b2conc3", "incorrect": "D'une part, ce projet coûte cher. Et d'autre part, il crée des emplois.", "answer": ["D'une part, ce projet coûte cher ; d'autre part, il crée des emplois."], "explanation": "Les deux membres forment une seule phrase liée."},
             ]},
        ],
        "summary": [
            "D'une part… d'autre part structure une argumentation en deux temps liés.",
            "En revanche, néanmoins, cependant marquent une opposition nuancée ; par conséquent, de ce fait marquent une conséquence.",
            "En outre/de plus ajoutent un argument ; ceci dit/cela étant introduisent une réserve finale.",
        ],
    },
    {
        "id": "b2-laccord-du-participe-passe-cas-complexes",
        "level": "B2", "unit": "1", "order": 8, "skill": "grammar", "strand": "accord-participe-passe-complexe",
        "title": "L'Accord du Participe Passé — Cas Complexes",
        "subtitle": "Au-delà des règles de base : l'accord avec avoir et un COD antéposé, et les verbes pronominaux.",
        "objectives": [
            "Accorder le participe passé avec avoir quand le complément d'objet direct précède le verbe.",
            "Accorder le participe passé des verbes pronominaux selon la fonction du pronom réfléchi.",
            "Reconnaître les cas où le participe passé reste invariable.",
        ],
        "content": {
            "intro": "L'accord du participe passé de base (avec être : toujours ; avec avoir : jamais avec le sujet) cache des cas plus subtils, fréquents à l'écrit soigné, qui demandent une analyse précise de la phrase.",
            "explanation": "<p>Avec <strong>avoir</strong>, le participe passé s'accorde avec le complément d'objet direct (COD) seulement quand celui-ci est placé <strong>avant</strong> le verbe : <em>J'ai vu les photos</em> (pas d'accord, COD après) mais <em>Les photos que j'ai vues</em> (accord, COD « que » avant, représentant <em>les photos</em>, féminin pluriel). C'est le cas le plus fréquent avec un pronom relatif <em>que</em> ou un pronom COD (<em>le, la, les</em>) placé avant le verbe.</p><p>Pour les <strong>verbes pronominaux</strong>, l'accord se fait avec le sujet seulement si le pronom réfléchi (<em>se</em>) fonctionne comme un COD : <em>Elle s'est lavée</em> (elle a lavé qui ? elle-même → accord). Mais si le pronom réfléchi est un complément d'objet indirect, le participe reste invariable : <em>Elle s'est lavé les mains</em> (elle a lavé quoi ? les mains, COD placé après → pas d'accord avec le sujet ; « les mains » n'est pas non plus avant le verbe ici).</p>",
            "rules": [
                {"heading": "a) Avoir + COD antéposé", "body": "<ul><li>Accord seulement si le COD précède le verbe : <em>Les photos que j'ai vues.</em></li></ul>"},
                {"heading": "b) Avoir + COD postposé", "body": "<ul><li>Pas d'accord si le COD suit le verbe : <em>J'ai vu les photos.</em></li></ul>"},
                {"heading": "c) Pronominaux, pronom = COD", "body": "<ul><li>Accord avec le sujet : <em>Elle s'est lavée.</em></li></ul>"},
                {"heading": "d) Pronominaux, pronom = COI", "body": "<ul><li>Pas d'accord : <em>Elle s'est lavé les mains.</em></li></ul>"},
            ],
            "examples": [
                "Les photos que j'ai vues sont magnifiques.",
                "J'ai vu les photos hier soir.",
                "Elle s'est lavée avant de sortir.",
                "Elle s'est lavé les mains avant de manger.",
                "La lettre que tu as écrite est très touchante.",
                "Ils se sont parlé pendant des heures. (se = COI, invariable)",
                "Ils se sont regardés en silence. (se = COD, accord)",
            ],
            "commonMistakes": [
                {"wrong": "Les photos que j'ai vu sont magnifiques.", "right": "Les photos que j'ai vues sont magnifiques.", "why": "Le COD que (représentant les photos) précède le verbe : accord obligatoire."},
                {"wrong": "Elle s'est lavé (sans complément, sens : elle-même).", "right": "Elle s'est lavée.", "why": "Sans complément d'objet direct après, se représente le COD : accord avec le sujet."},
                {"wrong": "Elle s'est lavée les mains.", "right": "Elle s'est lavé les mains.", "why": "Les mains est le COD, placé après le verbe ; se est ici un COI (elle a lavé les mains à elle-même) : pas d'accord."},
            ],
        },
        "exercises": [
            {"id": "b2acc-fill", "type": "fill-blank", "title": "Accorde le Participe Passé",
             "instructions": "Écris la forme correcte du participe passé.",
             "items": [
                {"id": "b2accf1", "prompt": "Les photos que j'ai ___ (voir) sont magnifiques.", "answers": [["vues"]], "options": ["vues", "vu", "vues."], "explanation": "COD que (les photos) antéposé : accord au féminin pluriel."},
                {"id": "b2accf2", "prompt": "J'ai ___ (voir) les photos hier soir.", "answers": [["vu"]], "options": ["vu", "vues", "vus"], "explanation": "COD les photos postposé : pas d'accord."},
                {"id": "b2accf3", "prompt": "Elle s'est ___ (laver) avant de sortir.", "answers": [["lavée"]], "options": ["lavée", "lavé", "lavés"], "explanation": "Se = COD ici : accord avec le sujet féminin."},
                {"id": "b2accf4", "prompt": "Elle s'est ___ (laver) les mains.", "answers": [["lavé"]], "options": ["lavé", "lavée", "lavées"], "explanation": "Se = COI ici, les mains est le COD postposé : pas d'accord."},
             ]},
            {"id": "b2acc-mc", "type": "multiple-choice", "title": "L'Accord du Participe Passé",
             "items": [
                {"id": "b2accm1", "prompt": "Quand le participe passé avec avoir s'accorde-t-il avec le COD ?", "options": ["quand le COD précède le verbe", "toujours", "jamais"], "answerIndex": 0, "explanation": "L'accord ne se fait qu'avec un COD antéposé."},
                {"id": "b2accm2", "prompt": "Dans « elle s'est lavée », que représente se ?", "options": ["le COD", "le COI", "rien"], "answerIndex": 0, "explanation": "Sans complément après, se est le COD : accord."},
                {"id": "b2accm3", "prompt": "Dans « elle s'est lavé les mains », que représente se ?", "options": ["le COI", "le COD", "le sujet"], "answerIndex": 0, "explanation": "Les mains est le COD ; se est ici le COI : pas d'accord."},
                {"id": "b2accm4", "prompt": "« J'ai vu les photos » s'accorde-t-il ?", "options": ["non, le COD suit le verbe", "oui, toujours avec avoir", "oui, car le sujet est féminin"], "answerIndex": 0, "explanation": "Le COD postposé ne déclenche jamais l'accord."},
             ]},
            {"id": "b2acc-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b2accc1", "incorrect": "Les photos que j'ai vu sont magnifiques.", "answer": ["Les photos que j'ai vues sont magnifiques."], "explanation": "COD antéposé : accord obligatoire."},
                {"id": "b2accc2", "incorrect": "Elle s'est lavé (sans complément).", "answer": ["Elle s'est lavée."], "explanation": "Se = COD ici : accord avec le sujet."},
                {"id": "b2accc3", "incorrect": "Elle s'est lavée les mains.", "answer": ["Elle s'est lavé les mains."], "explanation": "Se = COI ici, les mains est le COD postposé : pas d'accord."},
             ]},
        ],
        "summary": [
            "Avec avoir, le participe passé s'accorde avec le COD seulement si celui-ci précède le verbe.",
            "Pour les verbes pronominaux, l'accord se fait avec le sujet seulement si se est un COD.",
            "Si se est un COI (souvent parce qu'un autre COD suit, postposé), le participe passé reste invariable.",
        ],
    },
    {
        "id": "b2-les-tournures-emphatiques-et-la-mise-en-relief",
        "level": "B2", "unit": "1", "order": 9, "skill": "grammar", "strand": "emphase",
        "title": "Les Tournures Emphatiques et la Mise en Relief",
        "subtitle": "C'est… qui/que, ce qui/ce que… c'est : comment insister sur un élément de la phrase.",
        "objectives": [
            "Utiliser c'est… qui pour mettre en relief le sujet d'une phrase.",
            "Utiliser c'est… que pour mettre en relief un complément.",
            "Utiliser ce qui/ce que… c'est pour mettre en relief le début d'une phrase.",
        ],
        "content": {
            "intro": "Pour insister sur un élément précis d'une phrase — sans changer l'intonation, impossible à l'écrit — le français dispose de constructions syntaxiques dédiées, très fréquentes à l'oral comme à l'écrit soigné.",
            "explanation": "<p>La construction <strong>c'est… qui</strong> met en relief le <strong>sujet</strong> : <em>C'est Marie qui a gagné</em> (et pas quelqu'un d'autre). La construction <strong>c'est… que</strong> met en relief un <strong>complément</strong> (objet, lieu, temps) : <em>C'est ce livre que je préfère. C'est demain que nous partons.</em></p><p>Pour mettre en relief le début de la phrase de façon encore plus marquée, on utilise <strong>ce qui/ce que… c'est</strong> : <em>Ce qui m'intéresse, c'est la musique. Ce que je veux, c'est partir en vacances.</em> <em>Ce qui</em> reprend un sujet, <em>ce que</em> reprend un complément d'objet direct.</p>",
            "rules": [
                {"heading": "a) C'est… qui (sujet)", "body": "<ul><li><em>C'est Marie qui a gagné.</em></li></ul>"},
                {"heading": "b) C'est… que (complément)", "body": "<ul><li><em>C'est ce livre que je préfère.</em></li></ul>"},
                {"heading": "c) Ce qui… c'est (sujet, emphase forte)", "body": "<ul><li><em>Ce qui m'intéresse, c'est la musique.</em></li></ul>"},
                {"heading": "d) Ce que… c'est (complément, emphase forte)", "body": "<ul><li><em>Ce que je veux, c'est partir en vacances.</em></li></ul>"},
            ],
            "examples": [
                "C'est Marie qui a gagné le concours.",
                "C'est ce livre que je préfère.",
                "C'est demain que nous partons.",
                "Ce qui m'intéresse, c'est la musique classique.",
                "Ce que je veux, c'est partir en vacances.",
                "C'est toi qui as raison.",
                "Ce dont j'ai besoin, c'est de calme.",
            ],
            "commonMistakes": [
                {"wrong": "C'est Marie que a gagné.", "right": "C'est Marie qui a gagné.", "why": "Marie est le sujet du verbe gagner : il faut qui, pas que."},
                {"wrong": "C'est ce livre qui je préfère.", "right": "C'est ce livre que je préfère.", "why": "Ce livre est le complément d'objet direct de préférer : il faut que, pas qui."},
                {"wrong": "Ce que m'intéresse, c'est la musique.", "right": "Ce qui m'intéresse, c'est la musique.", "why": "M'intéresse a pour sujet ce qui précède : il faut ce qui, pas ce que."},
            ],
        },
        "exercises": [
            {"id": "b2emp-fill", "type": "fill-blank", "title": "Complète la Mise en Relief",
             "instructions": "Choisis qui, que ou ce qui/ce que.",
             "items": [
                {"id": "b2empf1", "prompt": "C'est Marie ___ a gagné le concours.", "answers": [["qui"]], "options": ["qui", "que", "ce qui"], "explanation": "Marie est le sujet : qui."},
                {"id": "b2empf2", "prompt": "C'est ce livre ___ je préfère.", "answers": [["que"]], "options": ["que", "qui", "ce que"], "explanation": "Ce livre est le complément : que."},
                {"id": "b2empf3", "prompt": "___ m'intéresse, c'est la musique.", "answers": [["Ce qui"]], "options": ["Ce qui", "Ce que", "Qui"], "explanation": "M'intéresse a pour sujet ce qui précède."},
                {"id": "b2empf4", "prompt": "___ je veux, c'est partir en vacances.", "answers": [["Ce que"]], "options": ["Ce que", "Ce qui", "Que"], "explanation": "Je veux a pour complément d'objet ce que je veux."},
             ]},
            {"id": "b2emp-mc", "type": "multiple-choice", "title": "Les Tournures Emphatiques",
             "items": [
                {"id": "b2empm1", "prompt": "Que met en relief c'est… qui ?", "options": ["le sujet", "le complément", "le verbe"], "answerIndex": 0, "explanation": "C'est… qui isole le sujet."},
                {"id": "b2empm2", "prompt": "Que met en relief c'est… que ?", "options": ["un complément", "le sujet", "le verbe"], "answerIndex": 0, "explanation": "C'est… que isole un complément."},
                {"id": "b2empm3", "prompt": "Quand utilise-t-on ce qui plutôt que ce que ?", "options": ["quand l'élément mis en relief est un sujet", "quand c'est un complément", "toujours indifféremment"], "answerIndex": 0, "explanation": "Ce qui reprend un sujet, ce que un COD."},
                {"id": "b2empm4", "prompt": "Quelle construction met le plus fortement en relief le début de la phrase ?", "options": ["ce qui/ce que… c'est", "c'est… qui/que", "l'ordre normal"], "answerIndex": 0, "explanation": "Ce qui/ce que… c'est place l'élément mis en relief en tête absolue."},
             ]},
            {"id": "b2emp-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b2empc1", "incorrect": "C'est Marie que a gagné.", "answer": ["C'est Marie qui a gagné."], "explanation": "Marie est le sujet : qui."},
                {"id": "b2empc2", "incorrect": "C'est ce livre qui je préfère.", "answer": ["C'est ce livre que je préfère."], "explanation": "Ce livre est le complément : que."},
                {"id": "b2empc3", "incorrect": "Ce que m'intéresse, c'est la musique.", "answer": ["Ce qui m'intéresse, c'est la musique."], "explanation": "Sujet du verbe intéresser : ce qui."},
             ]},
        ],
        "summary": [
            "C'est… qui met en relief le sujet ; c'est… que met en relief un complément.",
            "Ce qui/ce que… c'est place l'élément mis en relief en tête de phrase, pour une emphase encore plus forte.",
            "Ce qui reprend toujours un sujet, ce que un complément d'objet direct.",
        ],
    },
    {
        "id": "b2-le-futur-anterieur",
        "level": "B2", "unit": "1", "order": 10, "skill": "grammar", "strand": "futur-anterieur",
        "title": "Le Futur Antérieur",
        "subtitle": "Comment former le futur antérieur, pour exprimer une action terminée avant un autre moment du futur.",
        "objectives": [
            "Former le futur antérieur avec le futur simple de avoir/être + participe passé.",
            "Employer le futur antérieur après quand, dès que, lorsque pour une action antérieure à une autre action future.",
            "Distinguer le futur antérieur du futur simple selon la chronologie des deux actions.",
        ],
        "content": {
            "intro": "Quand deux actions se situent dans le futur mais que l'une doit être terminée avant que l'autre commence, le français utilise le futur antérieur pour marquer clairement cette antériorité.",
            "explanation": "<p>Le futur antérieur se forme avec le <strong>futur simple</strong> de <em>avoir</em> ou <em>être</em> + le participe passé, avec les mêmes règles d'auxiliaire et d'accord que le passé composé : <em>j'aurai fini, elle sera partie, nous nous serons levés</em>.</p><p>Il s'emploie pour une action qui sera <strong>déjà terminée</strong> au moment où une autre action future se produira, très souvent après <em>quand, dès que, lorsque, aussitôt que</em> : <em>Quand tu arriveras, j'aurai déjà fini de préparer le dîner.</em> Contrairement à l'anglais, le français utilise le futur (simple ou antérieur) après ces conjonctions, jamais le présent.</p>",
            "rules": [
                {"heading": "a) Formation", "body": "<ul><li>Futur simple de avoir/être + participe passé : <em>j'aurai parlé, tu seras parti(e)</em>.</li></ul>"},
                {"heading": "b) Emploi", "body": "<ul><li>Action antérieure à un autre fait futur : <em>Dès que tu auras fini, appelle-moi.</em></li></ul>"},
                {"heading": "c) Après quand/dès que/lorsque", "body": "<ul><li>Le français utilise le futur (simple ou antérieur), jamais le présent, contrairement à l'anglais.</li></ul>"},
                {"heading": "d) Même accord que le passé composé", "body": "<ul><li>Les mêmes règles d'auxiliaire et d'accord s'appliquent.</li></ul>"},
            ],
            "examples": [
                "Quand tu arriveras, j'aurai déjà fini de préparer le dîner.",
                "Dès que tu auras fini, appelle-moi.",
                "Elle sera partie avant notre arrivée.",
                "Lorsque nous aurons terminé, nous sortirons fêter ça.",
                "Aussitôt qu'il aura reçu la réponse, il nous préviendra.",
                "Ils se seront couchés avant minuit, sans doute.",
                "Tu auras compris la leçon d'ici la fin de la semaine.",
            ],
            "commonMistakes": [
                {"wrong": "Quand tu arrives, j'aurai fini.", "right": "Quand tu arriveras, j'aurai fini.", "why": "Après quand annonçant un fait futur, on utilise le futur, jamais le présent, en français."},
                {"wrong": "Dès que tu as fini, appelle-moi.", "right": "Dès que tu auras fini, appelle-moi.", "why": "L'action future antérieure demande le futur antérieur, pas le passé composé."},
                {"wrong": "Elle aura parti avant notre arrivée.", "right": "Elle sera partie avant notre arrivée.", "why": "Partir se conjugue avec être, même au futur antérieur, avec accord au féminin."},
            ],
        },
        "exercises": [
            {"id": "b2fa-fill", "type": "fill-blank", "title": "Conjugue au Futur Antérieur",
             "instructions": "Écris la forme correcte du verbe entre parenthèses.",
             "items": [
                {"id": "b2faf1", "prompt": "Quand tu arriveras, j'___ (finir) de préparer le dîner.", "answers": [["aurai fini"]], "options": ["aurai fini", "ai fini", "aurais fini"], "explanation": "Futur simple de avoir + participe passé."},
                {"id": "b2faf2", "prompt": "Dès que tu ___ (finir), appelle-moi.", "answers": [["auras fini"]], "options": ["auras fini", "as fini", "finiras"], "explanation": "Futur antérieur après dès que."},
                {"id": "b2faf3", "prompt": "Elle ___ (partir) avant notre arrivée.", "answers": [["sera partie"]], "options": ["sera partie", "aura parti", "était partie"], "explanation": "Partir se conjugue avec être, accord au féminin."},
                {"id": "b2faf4", "prompt": "Lorsque nous ___ (terminer), nous sortirons fêter ça.", "answers": [["aurons terminé"]], "options": ["aurons terminé", "terminons", "avons terminé"], "explanation": "Futur antérieur après lorsque, pour une action future antérieure."},
             ]},
            {"id": "b2fa-mc", "type": "multiple-choice", "title": "Le Futur Antérieur",
             "items": [
                {"id": "b2fam1", "prompt": "Comment forme-t-on le futur antérieur ?", "options": ["futur simple de avoir/être + participe passé", "imparfait de avoir/être + participe passé", "présent de avoir/être + participe passé"], "answerIndex": 0, "explanation": "L'auxiliaire est au futur simple."},
                {"id": "b2fam2", "prompt": "Quel temps utilise le français après quand/dès que pour un fait futur ?", "options": ["le futur, jamais le présent", "toujours le présent", "toujours le subjonctif"], "answerIndex": 0, "explanation": "Contrairement à l'anglais, le français exige le futur."},
                {"id": "b2fam3", "prompt": "À quoi sert le futur antérieur ?", "options": ["exprimer une action terminée avant un autre fait futur", "décrire une habitude passée", "exprimer un regret"], "answerIndex": 0, "explanation": "Il marque toujours l'antériorité entre deux faits futurs."},
                {"id": "b2fam4", "prompt": "Dans « quand tu arriveras, j'aurai fini », quelle action se termine en premier ?", "options": ["j'aurai fini", "tu arriveras", "aucune des deux"], "answerIndex": 0, "explanation": "Le futur antérieur marque toujours l'action la plus ancienne des deux."},
             ]},
            {"id": "b2fa-correction", "type": "correction", "title": "Corrige les Erreurs",
             "items": [
                {"id": "b2fac1", "incorrect": "Quand tu arrives, j'aurai fini.", "answer": ["Quand tu arriveras, j'aurai fini."], "explanation": "Le futur, jamais le présent, après quand pour un fait futur."},
                {"id": "b2fac2", "incorrect": "Dès que tu as fini, appelle-moi.", "answer": ["Dès que tu auras fini, appelle-moi."], "explanation": "Futur antérieur pour l'action future antérieure."},
                {"id": "b2fac3", "incorrect": "Elle aura parti avant notre arrivée.", "answer": ["Elle sera partie avant notre arrivée."], "explanation": "Partir se conjugue avec être."},
             ]},
        ],
        "summary": [
            "Le futur antérieur se forme avec le futur simple de avoir/être + participe passé.",
            "Il exprime une action terminée avant un autre fait futur, souvent après quand, dès que, lorsque.",
            "Contrairement à l'anglais, le français utilise toujours le futur (simple ou antérieur) après ces conjonctions, jamais le présent.",
        ],
    },
]

EXTRA_EXERCISES = {
    "b2-le-subjonctif-passe": [
        {"id": "b2sbpx-reading", "type": "reading-comprehension", "title": "Lecture : Une Bonne Nouvelle",
         "passage": "<p>Marc vient d'apprendre que sa sœur a eu son diplôme. Il est très content qu'elle ait réussi, surtout qu'elle ait travaillé si dur toute l'année. Il doute seulement qu'elle ait eu le temps de fêter ça, tant elle était fatiguée après l'examen. Il espère qu'elle se soit reposée depuis.</p>",
         "items": [
            {"id": "b2sbpxr1", "prompt": "Qu'a appris Marc ?", "options": ["Que sa sœur a eu son diplôme", "Que sa sœur a échoué", "Que sa sœur part en voyage"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2sbpxr2", "prompt": "Pourquoi est-il particulièrement content ?", "options": ["Parce qu'elle a travaillé dur toute l'année", "Parce qu'il a eu son diplôme aussi", "Parce qu'elle part en vacances"], "answerIndex": 0, "explanation": "Le texte dit : « surtout qu'elle ait travaillé si dur »."},
            {"id": "b2sbpxr3", "prompt": "De quoi doute-t-il ?", "options": ["Qu'elle ait eu le temps de fêter ça", "Qu'elle ait réussi", "Qu'elle soit sa sœur"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2sbpxr4", "prompt": "Qu'espère-t-il ?", "options": ["Qu'elle se soit reposée depuis", "Qu'elle recommence l'examen", "Qu'elle change d'études"], "answerIndex": 0, "explanation": "Le texte se termine par cette phrase."},
         ]},
        {"id": "b2sbpx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2sbpxo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "est", "content", "qu'elle", "ait", "réussi"], "explanation": "Subjonctif passé après une émotion, action antérieure."},
            {"id": "b2sbpxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "doute", "qu'elle", "ait", "eu", "le", "temps"], "explanation": "Subjonctif passé après le doute."},
         ]},
    ],
    "b2-le-subjonctif-apres-opinion-doute-but-concession": [
        {"id": "b2sbox-reading", "type": "reading-comprehension", "title": "Lecture : Un Projet Difficile",
         "passage": "<p>Bien que le projet soit compliqué, l'équipe continue à y travailler. Le chef explique chaque étape pour que tout le monde comprenne. Ils termineront à temps, à moins qu'un problème imprévu ne survienne. Personne ne pense que le projet échoue, mais tous restent prudents avant que la présentation finale n'arrive.</p>",
         "items": [
            {"id": "b2sboxr1", "prompt": "Que fait l'équipe bien que le projet soit compliqué ?", "options": ["Elle continue à y travailler", "Elle abandonne", "Elle change de projet"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2sboxr2", "prompt": "Pourquoi le chef explique-t-il chaque étape ?", "options": ["Pour que tout le monde comprenne", "Pour impressionner l'équipe", "Parce qu'il s'ennuie"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2sboxr3", "prompt": "Dans quel cas l'équipe ne terminerait-elle pas à temps ?", "options": ["À moins qu'un problème imprévu ne survienne", "Si le chef part", "Si le projet est trop facile"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2sboxr4", "prompt": "Que pense l'équipe du risque d'échec ?", "options": ["Personne ne pense que le projet échoue", "Tout le monde pense qu'il échouera", "Le chef seul y croit"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
         ]},
        {"id": "b2sbox-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2sboxo1", "prompt": "Remets les mots en ordre.", "words": ["Bien", "que", "ce", "soit", "compliqué", "elle", "continue"], "explanation": "Bien que + subjonctif exprime la concession."},
            {"id": "b2sboxo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "explique", "pour", "que", "tout", "le", "monde", "comprenne"], "explanation": "Pour que + subjonctif exprime le but."},
         ]},
    ],
    "b2-les-pronoms-relatifs-composes": [
        {"id": "b2rcx-reading", "type": "reading-comprehension", "title": "Lecture : Le Bureau de Sarah",
         "passage": "<p>Sarah travaille dans une entreprise pour laquelle elle a beaucoup d'admiration. Le bureau dans lequel elle passe ses journées donne sur un joli parc. Les collègues avec lesquels elle déjeune sont devenus de vrais amis. C'est un projet auquel elle pense sans cesse : créer sa propre équipe l'année prochaine.</p>",
         "items": [
            {"id": "b2rcxr1", "prompt": "Que ressent Sarah pour son entreprise ?", "options": ["Beaucoup d'admiration", "De l'indifférence", "De la déception"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2rcxr2", "prompt": "Sur quoi donne son bureau ?", "options": ["Un joli parc", "Une rue bruyante", "Un parking"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2rcxr3", "prompt": "Que sont devenus ses collègues ?", "options": ["De vrais amis", "Des rivaux", "Des inconnus"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2rcxr4", "prompt": "À quel projet pense-t-elle sans cesse ?", "options": ["Créer sa propre équipe l'année prochaine", "Changer d'entreprise", "Déménager"], "answerIndex": 0, "explanation": "Le texte se termine par cette phrase."},
         ]},
        {"id": "b2rcx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2rcxo1", "prompt": "Remets les mots en ordre.", "words": ["Le", "bureau", "dans", "lequel", "elle", "travaille"], "explanation": "Pronom relatif composé après une préposition de lieu."},
            {"id": "b2rcxo2", "prompt": "Remets les mots en ordre.", "words": ["C'est", "un", "projet", "auquel", "elle", "pense"], "explanation": "À + lequel se contracte en auquel."},
         ]},
    ],
    "b2-le-conditionnel-information-non-confirmee": [
        {"id": "b2cncx-reading", "type": "reading-comprehension", "title": "Lecture : Une Dépêche de Presse",
         "passage": "<p>Selon des sources proches du dossier, l'entreprise aurait licencié une centaine d'employés ce mois-ci. La direction n'a pas encore confirmé cette information. Le nouveau contrat avec l'étranger serait signé la semaine prochaine, ce qui, d'après les analystes, pourrait sauver plusieurs emplois. Aucune déclaration officielle n'a été faite pour l'instant.</p>",
         "items": [
            {"id": "b2cncxr1", "prompt": "Qu'aurait fait l'entreprise selon des sources proches du dossier ?", "options": ["Licencié une centaine d'employés", "Embauché cent employés", "Fermé ses portes"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2cncxr2", "prompt": "La direction a-t-elle confirmé l'information ?", "options": ["Non, pas encore", "Oui, totalement", "Oui, en partie"], "answerIndex": 0, "explanation": "Le texte dit : « n'a pas encore confirmé »."},
            {"id": "b2cncxr3", "prompt": "Quand le nouveau contrat serait-il signé ?", "options": ["La semaine prochaine", "Ce soir", "Dans un an"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2cncxr4", "prompt": "Une déclaration officielle a-t-elle été faite ?", "options": ["Non, aucune pour l'instant", "Oui, ce matin", "Oui, hier"], "answerIndex": 0, "explanation": "Le texte se termine par cette phrase."},
         ]},
        {"id": "b2cncx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2cncxo1", "prompt": "Remets les mots en ordre.", "words": ["L'entreprise", "aurait", "licencié", "une", "centaine", "d'employés"], "explanation": "Conditionnel passé, information non confirmée."},
            {"id": "b2cncxo2", "prompt": "Remets les mots en ordre.", "words": ["Le", "contrat", "serait", "signé", "la", "semaine", "prochaine"], "explanation": "Conditionnel présent passif, information non confirmée."},
         ]},
    ],
    "b2-la-nominalisation": [
        {"id": "b2nomx-reading", "type": "reading-comprehension", "title": "Lecture : Un Rapport Officiel",
         "passage": "<p>La décision du conseil municipal a surpris de nombreux habitants. L'annonce du projet de rénovation a été faite ce matin. Le développement du quartier est prévu sur cinq ans. La possibilité d'un financement européen reste à confirmer, mais la faiblesse du budget actuel inquiète déjà les élus.</p>",
         "items": [
            {"id": "b2nomxr1", "prompt": "Qu'est-ce qui a surpris de nombreux habitants ?", "options": ["La décision du conseil municipal", "Une élection", "Un incendie"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2nomxr2", "prompt": "Quand l'annonce a-t-elle été faite ?", "options": ["Ce matin", "Hier soir", "La semaine dernière"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2nomxr3", "prompt": "Sur combien d'années le développement est-il prévu ?", "options": ["Cinq ans", "Un an", "Dix ans"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2nomxr4", "prompt": "Qu'est-ce qui inquiète les élus ?", "options": ["La faiblesse du budget actuel", "Le nombre d'habitants", "La météo"], "answerIndex": 0, "explanation": "Le texte se termine par cette phrase."},
         ]},
        {"id": "b2nomx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2nomxo1", "prompt": "Remets les mots en ordre.", "words": ["La", "décision", "a", "surpris", "les", "habitants"], "explanation": "Nominalisation du verbe décider."},
            {"id": "b2nomxo2", "prompt": "Remets les mots en ordre.", "words": ["La", "possibilité", "reste", "à", "confirmer"], "explanation": "Nominalisation de l'adjectif possible."},
         ]},
    ],
    "b2-le-registre-soutenu-et-familier": [
        {"id": "b2regx-reading", "type": "reading-comprehension", "title": "Lecture : Deux Messages, Deux Registres",
         "passage": "<p>Dans un message à son ami, Paul écrit : « Salut, j'sais pas si je viens ce soir, j'suis crevé. » Dans sa lettre de motivation, il écrit : « Je vous prie de bien vouloir considérer ma candidature avec la plus grande attention. » Le contraste entre les deux textes illustre à quel point le registre change selon la situation et le destinataire.</p>",
         "items": [
            {"id": "b2regxr1", "prompt": "Quel registre utilise Paul avec son ami ?", "options": ["Familier", "Soutenu", "Administratif"], "answerIndex": 0, "explanation": "Le texte le dit directement (chute du ne, vocabulaire relâché)."},
            {"id": "b2regxr2", "prompt": "Que signifie « j'suis crevé » ?", "options": ["Je suis très fatigué", "Je suis content", "Je suis en retard"], "answerIndex": 0, "explanation": "Crevé est un mot familier pour fatigué."},
            {"id": "b2regxr3", "prompt": "Quel registre utilise Paul dans sa lettre de motivation ?", "options": ["Soutenu", "Familier", "Vulgaire"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2regxr4", "prompt": "Que montre le contraste entre les deux textes ?", "options": ["Que le registre change selon la situation", "Que Paul écrit toujours pareil", "Que Paul ne sait pas écrire"], "answerIndex": 0, "explanation": "Le texte se termine par cette conclusion."},
         ]},
        {"id": "b2regx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2regxo1", "prompt": "Remets les mots en ordre.", "words": ["Je", "ne", "sais", "pas", "si", "je", "viens"], "explanation": "Version au registre courant, avec le ne."},
            {"id": "b2regxo2", "prompt": "Remets les mots en ordre.", "words": ["Que", "pensez-vous", "de", "ce", "projet", "?"], "explanation": "Inversion du sujet, registre soutenu."},
         ]},
    ],
    "b2-les-connecteurs-argumentatifs-avances": [
        {"id": "b2conx-reading", "type": "reading-comprehension", "title": "Lecture : Pour ou Contre le Télétravail",
         "passage": "<p>D'une part, le télétravail réduit le temps de trajet des salariés ; d'autre part, il isole parfois les équipes. En revanche, il permet une meilleure organisation personnelle. Par conséquent, de nombreuses entreprises l'adoptent. Ceci dit, un encadrement clair reste nécessaire pour éviter les dérives.</p>",
         "items": [
            {"id": "b2conxr1", "prompt": "Que réduit le télétravail, selon le texte ?", "options": ["Le temps de trajet des salariés", "Le salaire", "Les vacances"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2conxr2", "prompt": "Quel est l'inconvénient mentionné ?", "options": ["Il isole parfois les équipes", "Il coûte plus cher", "Il est interdit"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2conxr3", "prompt": "Pourquoi de nombreuses entreprises adoptent-elles le télétravail ?", "options": ["Par conséquent de la meilleure organisation personnelle qu'il permet", "Par obligation légale", "Par hasard"], "answerIndex": 0, "explanation": "Le texte enchaîne cette conséquence."},
            {"id": "b2conxr4", "prompt": "Que reste-t-il nécessaire, selon le texte ?", "options": ["Un encadrement clair", "Plus de réunions", "Moins de salariés"], "answerIndex": 0, "explanation": "Le texte se termine par cette réserve, introduite par « ceci dit »."},
         ]},
        {"id": "b2conx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2conxo1", "prompt": "Remets les mots en ordre.", "words": ["D'une", "part,", "il", "réduit", "le", "trajet"], "explanation": "D'une part structure le premier argument."},
            {"id": "b2conxo2", "prompt": "Remets les mots en ordre.", "words": ["Par", "conséquent,", "les", "entreprises", "l'adoptent"], "explanation": "Par conséquent marque la conséquence logique."},
         ]},
    ],
    "b2-laccord-du-participe-passe-cas-complexes": [
        {"id": "b2accx-reading", "type": "reading-comprehension", "title": "Lecture : Une Matinée Chargée",
         "passage": "<p>Ce matin, Léa s'est levée tôt. Elle s'est lavé les mains avant de préparer le petit-déjeuner. Les tartines qu'elle a préparées ont plu à toute la famille. Ensuite, elle s'est brossé les dents et s'est habillée rapidement avant de partir au travail.</p>",
         "items": [
            {"id": "b2accxr1", "prompt": "Que fait Léa juste après s'être levée ?", "options": ["Elle se lave les mains", "Elle part au travail", "Elle appelle une amie"], "answerIndex": 0, "explanation": "Le texte suit cet ordre."},
            {"id": "b2accxr2", "prompt": "Qu'a-t-elle préparé pour la famille ?", "options": ["Des tartines", "Un gâteau", "Une soupe"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2accxr3", "prompt": "Pourquoi « préparées » s'accorde-t-il au féminin pluriel ?", "options": ["Le COD que (les tartines) précède le verbe", "Léa est féminin", "C'est une règle sans raison"], "answerIndex": 0, "explanation": "Le pronom relatif que, représentant les tartines, précède le verbe."},
            {"id": "b2accxr4", "prompt": "Pourquoi « brossé » ne s'accorde-t-il pas dans « elle s'est brossé les dents » ?", "options": ["Se est un COI ici, les dents est le COD postposé", "C'est une erreur du texte", "Brossé ne s'accorde jamais"], "answerIndex": 0, "explanation": "Les dents est le COD placé après le verbe ; se est le COI."},
         ]},
        {"id": "b2accx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2accxo1", "prompt": "Remets les mots en ordre.", "words": ["Léa", "s'est", "levée", "tôt", "ce", "matin"], "explanation": "Se = COD ici : accord avec le sujet féminin."},
            {"id": "b2accxo2", "prompt": "Remets les mots en ordre.", "words": ["Elle", "s'est", "lavé", "les", "mains"], "explanation": "Se = COI ici, les mains est le COD postposé : pas d'accord."},
         ]},
    ],
    "b2-les-tournures-emphatiques-et-la-mise-en-relief": [
        {"id": "b2empx-reading", "type": "reading-comprehension", "title": "Lecture : Le Concours de Cuisine",
         "passage": "<p>C'est Léo qui a remporté le concours de cuisine cette année. Ce qui a impressionné le jury, c'est l'originalité de son dessert. C'est surtout la présentation qu'ils ont saluée. Ce que Léo retient de cette expérience, c'est l'importance de la créativité.</p>",
         "items": [
            {"id": "b2empxr1", "prompt": "Qui a remporté le concours ?", "options": ["Léo", "Le jury", "Un autre candidat"], "answerIndex": 0, "explanation": "Le texte le dit directement, avec c'est... qui."},
            {"id": "b2empxr2", "prompt": "Qu'est-ce qui a impressionné le jury ?", "options": ["L'originalité de son dessert", "Le prix du plat", "La rapidité de Léo"], "answerIndex": 0, "explanation": "Le texte le dit directement, avec ce qui... c'est."},
            {"id": "b2empxr3", "prompt": "Qu'ont surtout salué les juges ?", "options": ["La présentation", "Le goût", "La rapidité"], "answerIndex": 0, "explanation": "Le texte le dit directement, avec c'est... que."},
            {"id": "b2empxr4", "prompt": "Que retient Léo de cette expérience ?", "options": ["L'importance de la créativité", "L'importance de la rapidité", "Rien de particulier"], "answerIndex": 0, "explanation": "Le texte se termine par cette phrase, avec ce que... c'est."},
         ]},
        {"id": "b2empx-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2empxo1", "prompt": "Remets les mots en ordre.", "words": ["C'est", "Léo", "qui", "a", "gagné"], "explanation": "C'est... qui met en relief le sujet."},
            {"id": "b2empxo2", "prompt": "Remets les mots en ordre.", "words": ["Ce", "qui", "compte,", "c'est", "la", "créativité"], "explanation": "Ce qui... c'est met en relief le sujet avec une emphase forte."},
         ]},
    ],
    "b2-le-futur-anterieur": [
        {"id": "b2fax-reading", "type": "reading-comprehension", "title": "Lecture : Les Plans du Week-end",
         "passage": "<p>Dès que nous aurons fini nos devoirs, nous irons au cinéma. Quand ma sœur sera rentrée, nous mangerons tous ensemble. Lorsque j'aurai terminé mon livre, je le prêterai à mon frère. Aussitôt que le film aura commencé, éteignez vos téléphones, s'il vous plaît.</p>",
         "items": [
            {"id": "b2faxr1", "prompt": "Que feront-ils dès qu'ils auront fini leurs devoirs ?", "options": ["Ils iront au cinéma", "Ils dormiront", "Ils partiront en voyage"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2faxr2", "prompt": "Quand mangeront-ils tous ensemble ?", "options": ["Quand la sœur sera rentrée", "Demain matin", "Après le film"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2faxr3", "prompt": "Que fera la personne de son livre ?", "options": ["Elle le prêtera à son frère", "Elle le vendra", "Elle le jettera"], "answerIndex": 0, "explanation": "Le texte le dit directement."},
            {"id": "b2faxr4", "prompt": "Que faut-il faire aussitôt que le film aura commencé ?", "options": ["Éteindre son téléphone", "Applaudir", "Sortir de la salle"], "answerIndex": 0, "explanation": "Le texte se termine par cette demande."},
         ]},
        {"id": "b2fax-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "b2faxo1", "prompt": "Remets les mots en ordre.", "words": ["Dès", "que", "nous", "aurons", "fini,", "nous", "irons"], "explanation": "Futur antérieur après dès que, futur simple dans la principale."},
            {"id": "b2faxo2", "prompt": "Remets les mots en ordre.", "words": ["Quand", "ma", "sœur", "sera", "rentrée,", "nous", "mangerons"], "explanation": "Futur antérieur (être) après quand pour l'action antérieure."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))
