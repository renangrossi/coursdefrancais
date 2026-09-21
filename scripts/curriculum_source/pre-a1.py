# -*- coding: utf-8 -*-
"""Pre-A1 — Données du curriculum de survie totale. Voir curriculum/SCHEMA.md
pour la forme exacte du JSON vers lequel ceci est compilé (scripts/generate_curriculum.py
fait la compilation). Écrit en Python plutôt qu'en JSON à la main pour que le
HTML en ligne (rules[].body, content.explanation) et les guillemets dans le
texte puissent s'écrire naturellement."""

OVERVIEW = ("Pre-A1 est le point de départ absolu : l'alphabet et les sons du français, "
            "les salutations et les présentations, les nombres, l'heure et la date, le "
            "vocabulaire essentiel pour survivre en classe, les mots les plus courants pour "
            "les personnes et les objets du quotidien, et les premiers verbes et pronoms pour "
            "construire tes premières phrases. À la fin de ce niveau, tu pourras te présenter, "
            "demander des choses simples et comprendre de très courts dialogues de la vie "
            "quotidienne, sans avoir besoin d'aucune connaissance préalable du français.")

LESSONS = [
    {
        "id": "pre-a1-alphabet-et-sons-du-francais",
        "level": "Pre-A1", "unit": "1", "order": 1, "skill": "pronunciation", "strand": "alphabet",
        "title": "L'Alphabet et les Sons du Français",
        "subtitle": "Les lettres du français, les accents, la cédille, les voyelles nasales et pourquoi tant de lettres finales sont muettes.",
        "objectives": [
            "Reconnaître les 26 lettres de l'alphabet français et ses signes diacritiques.",
            "Distinguer les voyelles nasales (an, in, on, un) des voyelles orales.",
            "Repérer les consonnes finales muettes et un premier cas de liaison.",
        ],
        "content": {
            "intro": "Le français utilise le même alphabet que l'anglais, mais ses accents et ses sons changent tout — apprendre ces bases est le premier pas pour lire, écrire et prononcer avec confiance.",
            "explanation": "<p>L'alphabet français a <strong>26 lettres</strong>, comme l'anglais, mais plusieurs voyelles portent un <strong>accent</strong> qui change leur prononciation, et parfois le sens du mot : <em>a</em> (verbe avoir) et <em>à</em> (préposition) ne se prononcent pas pareil. La <strong>cédille</strong> (<em>ç</em>) transforme le son dur du c en son doux, comme dans <em>français</em> ou <em>garçon</em>.</p><p>Le français a aussi des <strong>voyelles nasales</strong> — des sons qui n'existent pas en anglais ni en portugais standard, où l'air passe par le nez : <em>an/en</em>, <em>in/im</em>, <em>on</em>, <em>un</em>. Autre trait essentiel : beaucoup de <strong>consonnes finales sont muettes</strong> (<em>petit</em> se prononce sans le t final), mais elles peuvent réapparaître devant une voyelle grâce à la <strong>liaison</strong> — <em>les amis</em> se prononce comme «&nbsp;lezami&nbsp;».</p>",
            "rules": [
                {"heading": "a) Les accents", "body": "<ul><li><strong>é</strong> (accent aigu) — un son fermé, comme dans <em>café</em>.</li><li><strong>è / ê</strong> (accent grave / circonflexe) — un son ouvert, comme dans <em>mère, fête</em>.</li><li><strong>à / ù</strong> — ne changent pas le son, mais distinguent des mots : <em>a</em> (il a) vs <em>à</em> (préposition), <em>ou</em> (ou bien) vs <em>où</em> (lieu).</li><li>Le <strong>tréma</strong> (ë, ï) sépare deux voyelles qu'on prononcerait sinon ensemble, comme dans <em>Noël</em>.</li></ul>"},
                {"heading": "b) La cédille (ç)", "body": "<ul><li>Se met uniquement sous un c suivi de a, o ou u : <em>ça, garçon, reçu</em>.</li><li>Elle transforme le son dur du c (comme dans <em>café</em>) en son doux, comme un s : <em>français</em> se prononce «&nbsp;fransé&nbsp;».</li><li>Devant e ou i, le c est déjà doux tout seul — pas besoin de cédille : <em>ceci, cinéma</em>.</li></ul>"},
                {"heading": "c) Les voyelles nasales", "body": "<ul><li><strong>an / en</strong> — comme dans <em>France, enfant</em>.</li><li><strong>in / im / ain</strong> — comme dans <em>vin, important, pain</em>.</li><li><strong>on</strong> — comme dans <em>bonjour, maison</em>.</li><li><strong>un</strong> — comme dans <em>un, lundi</em>.</li></ul>"},
                {"heading": "d) Consonnes finales muettes et liaison", "body": "<ul><li>Beaucoup de consonnes finales ne se prononcent pas : <em>petit, beaucoup, nez</em>.</li><li>Les consonnes <strong>c, r, f, l</strong> se prononcent souvent en fin de mot (astuce : le mot anglais «&nbsp;careful&nbsp;»).</li><li>La <strong>liaison</strong> : une consonne finale muette se prononce devant une voyelle qui suit — <em>les amis</em> («&nbsp;lezami&nbsp;»), <em>vous avez</em> («&nbsp;vouzavez&nbsp;»).</li></ul>"},
            ],
            "examples": [
                "Bonjour, je m'appelle Léa.",
                "Le garçon mange un croissant.",
                "Mon frère habite en France.",
                "Un, deux, trois, quatre, cinq.",
                "Les amis arrivent à midi.",
                "Il fait beaucoup de bruit.",
                "Où est la gare, s'il vous plaît ?",
            ],
            "commonMistakes": [
                {"wrong": "Prononcer le t final de petit.", "right": "Dire petit sans prononcer le t final.", "why": "La plupart des consonnes finales sont muettes en français, sauf devant une voyelle (liaison) ou pour les lettres c, r, f, l."},
                {"wrong": "Prononcer an/en comme le an anglais.", "right": "Prononcer an/en comme une voyelle nasale, l'air passant par le nez.", "why": "Les voyelles nasales françaises n'ont pas d'équivalent exact en anglais ; c'est un son entièrement nouveau à apprendre."},
                {"wrong": "Ignorer la cédille et prononcer garçon avec un son dur.", "right": "Prononcer garçon avec le son doux indiqué par la cédille.", "why": "La cédille change la prononciation du c devant a, o, u ; l'oublier change le son du mot."},
            ],
        },
        "exercises": [
            {"id": "pa1-mc", "type": "multiple-choice", "title": "Quelle Lettre ou Quel Son Est-ce ?",
             "items": [
                {"id": "pa1mc1", "prompt": "Quel signe transforme le son dur du c en son doux ?", "options": ["l'accent aigu", "la cédille", "le tréma"], "answerIndex": 1, "explanation": "La cédille (ç) adoucit le son du c devant a, o, u."},
                {"id": "pa1mc2", "prompt": "Comment se prononce le t final du mot petit ?", "options": ["Il ne se prononce pas", "Il se prononce comme un d", "Il se prononce fort"], "answerIndex": 0, "explanation": "Le t final est muet en français, comme la plupart des consonnes finales."},
                {"id": "pa1mc3", "prompt": "Quel mot contient une voyelle nasale ?", "options": ["ami", "bonjour", "école"], "answerIndex": 1, "explanation": "Bonjour contient le son nasal on."},
                {"id": "pa1mc4", "prompt": "Que se passe-t-il dans les amis à l'oral ?", "options": ["Rien de spécial", "Une liaison : le s final se prononce z", "Le a disparaît"], "answerIndex": 1, "explanation": "Devant une voyelle, le s final de les se prononce comme un z : liaison."},
             ]},
            {"id": "pa1-tf", "type": "true-false", "title": "Vrai ou Faux",
             "items": [
                {"id": "pa1tf1", "statement": "La cédille peut se mettre sous un c suivi de e ou de i.", "answer": False, "explanation": "Devant e ou i, le c est déjà doux sans cédille ; elle ne s'utilise que devant a, o, u."},
                {"id": "pa1tf2", "statement": "Les voyelles nasales du français n'existent pas en anglais.", "answer": True, "explanation": "Ce sont des sons propres au français (et à quelques autres langues), sans équivalent exact en anglais."},
                {"id": "pa1tf3", "statement": "Toutes les consonnes finales françaises sont toujours muettes.", "answer": False, "explanation": "Les lettres c, r, f, l se prononcent souvent en fin de mot ; et la liaison réactive une consonne muette devant une voyelle."},
                {"id": "pa1tf4", "statement": "à et a se prononcent exactement pareil.", "answer": True, "explanation": "L'accent grave sur à ne change pas le son ; il sert seulement à distinguer ce mot du verbe avoir (il a)."},
             ]},
            {"id": "pa1-match", "type": "matching", "title": "Associe la Lettre ou le Son à sa Description",
             "items": [
                {"id": "pa1match1", "pairs": [
                    {"left": "ç", "right": "adoucit le son du c devant a, o, u"},
                    {"left": "an/on/in/un", "right": "voyelles nasales"},
                    {"left": "t final de petit", "right": "consonne muette"},
                    {"left": "s de les amis", "right": "se prononce grâce à la liaison"},
                ], "explanation": "Chacun de ces éléments a un comportement propre dans la prononciation du français."},
             ]},
            {"id": "pa1-fill", "type": "fill-blank", "title": "Complète avec la Bonne Lettre",
             "instructions": "Choisis le mot correctement écrit pour chaque espace.",
             "items": [
                {"id": "pa1f1", "prompt": "Le ___ mange un croissant.", "answers": [["garçon"]], "options": ["garçon", "garcon", "garson"], "explanation": "Garçon s'écrit avec une cédille pour garder le son doux du c."},
                {"id": "pa1f2", "prompt": "___, comment ça va ?", "answers": [["Bonjour"]], "options": ["Bonjour", "Bonjor", "Bomjour"], "explanation": "Bonjour s'écrit avec on, la voyelle nasale, pas avec m."},
                {"id": "pa1f3", "prompt": "___ est la gare, s'il vous plaît ?", "answers": [["Où"]], "options": ["Où", "Ou", "Oú"], "explanation": "Où (lieu) prend un accent grave pour se distinguer de ou (ou bien)."},
                {"id": "pa1f4", "prompt": "Mon frère habite en ___.", "answers": [["France"]], "options": ["France", "Frence", "Fronce"], "explanation": "France s'écrit avec an, la voyelle nasale correspondante."},
             ]},
        ],
        "summary": [
            "L'alphabet français a 26 lettres, mais les accents (é, è, ê, à) et la cédille (ç) changent la prononciation et parfois le sens.",
            "Les voyelles nasales (an/en, in, on, un) sont des sons propres au français, sans équivalent exact en anglais.",
            "Beaucoup de consonnes finales sont muettes, sauf c, r, f, l, et sauf en cas de liaison devant une voyelle.",
        ],
    },
    {
        "id": "pre-a1-salutations-et-presentations",
        "level": "Pre-A1", "unit": "1", "order": 2, "skill": "functional", "strand": "salutations",
        "title": "Salutations et Présentations",
        "subtitle": "Comment saluer, prendre congé et te présenter en français — et quand utiliser tu ou vous.",
        "objectives": [
            "Saluer et prendre congé selon le moment de la journée.",
            "Demander et dire le nom d'une personne.",
            "Choisir entre tu et vous dans une première conversation.",
        ],
        "content": {
            "intro": "Toute conversation en français commence par une salutation, et cette salutation en dit déjà long sur le niveau de familiarité entre les deux personnes.",
            "explanation": "<p>En français, <strong>bonjour</strong> fonctionne du matin jusqu'au soir, dans des situations formelles comme informelles. <strong>Bonsoir</strong> le remplace le soir, et <strong>salut</strong> est une salutation informelle qui sert aussi bien à dire bonjour qu'au revoir entre amis.</p><p>Le français a aussi deux façons de dire «&nbsp;tu&nbsp;» : <strong>tu</strong> (informel) et <strong>vous</strong> (formel, ou pluriel). On utilise <em>tu</em> avec les amis, la famille et les enfants ; on utilise <em>vous</em> avec des personnes inconnues, plus âgées, ou dans un contexte professionnel, jusqu'à ce que l'autre personne propose de se tutoyer.</p>",
            "rules": [
                {"heading": "a) Salutations selon le moment de la journée", "body": "<ul><li><strong>Bonjour</strong> — du matin jusqu'au soir, formel et informel.</li><li><strong>Bonsoir</strong> — le soir, pour saluer en arrivant.</li><li><strong>Bonne nuit</strong> — seulement au moment de se coucher, jamais pour saluer en arrivant.</li><li><strong>Salut</strong> 👋 — informel, entre amis, pour dire bonjour ou au revoir.</li></ul>"},
                {"heading": "b) Demander et dire son nom", "body": "<ul><li>Informel : <em>Comment tu t'appelles ?</em> → <em>Je m'appelle Marie.</em></li><li>Formel : <em>Comment vous appelez-vous ?</em> → <em>Je m'appelle Marie.</em> (la réponse ne change pas)</li><li><em>Enchanté(e)</em> — se dit en rencontrant quelqu'un pour la première fois.</li></ul>"},
                {"heading": "c) Tu face à vous", "body": "<ul><li><strong>Tu</strong> — amis, famille, enfants, personnes de ton âge. <em>Tu viens d'où ?</em></li><li><strong>Vous</strong> — inconnus, personnes plus âgées, contextes formels. <em>Vous venez d'où ?</em></li><li>En cas de doute, commence par <em>vous</em> : c'est l'option la plus sûre.</li></ul>"},
                {"heading": "d) Prendre congé", "body": "<ul><li><strong>Au revoir</strong> — façon générale de se quitter, à tout moment.</li><li><strong>À bientôt</strong> — quand tu vas revoir la personne prochainement.</li><li><strong>À demain</strong> — quand tu vas la revoir le lendemain.</li></ul>"},
            ],
            "examples": [
                "Bonjour, comment allez-vous ?",
                "Salut ! Ça va ?",
                "Je m'appelle Thomas. Et toi, comment tu t'appelles ?",
                "Enchantée de faire votre connaissance.",
                "Bonsoir, monsieur Dubois.",
                "Je vais très bien, merci. Et vous ?",
                "Au revoir, à bientôt !",
                "Bonne nuit, dors bien.",
            ],
            "commonMistakes": [
                {"wrong": "Salut, comment allez-vous ?", "right": "Salut, ça va ? / Bonjour, comment allez-vous ?", "why": "Salut est informel, donc il se combine mieux avec ça va ; si tu utilises vous, il est plus naturel de commencer par une salutation formelle."},
                {"wrong": "Bonne nuit (en arrivant le matin)", "right": "Bonjour (en arrivant le matin)", "why": "Bonne nuit ne s'utilise que pour se coucher, jamais comme salutation du matin."},
                {"wrong": "Comment tu s'appelles ?", "right": "Comment tu t'appelles ? / Comment vous appelez-vous ?", "why": "Tu t'appelles est la forme correcte avec tu ; s'appelles mélange tu avec une forme de il/elle."},
            ],
        },
        "exercises": [
            {"id": "pa2-mc", "type": "multiple-choice", "title": "Choisis la Bonne Salutation",
             "items": [
                {"id": "pa2mc1", "prompt": "Il est neuf heures du matin. Que dis-tu ?", "options": ["Bonne nuit", "Bonjour", "Bonsoir"], "answerIndex": 1, "explanation": "Bonjour s'utilise du matin jusqu'au soir."},
                {"id": "pa2mc2", "prompt": "Tu rencontres un professeur pour la première fois. Quel pronom utilises-tu ?", "options": ["tu", "vous", "on"], "answerIndex": 1, "explanation": "Avec une personne inconnue, dans un contexte formel, on utilise vous."},
                {"id": "pa2mc3", "prompt": "Tu dis au revoir à un ami que tu vas voir demain. Que dis-tu ?", "options": ["À demain", "Bonne nuit", "Enchanté"], "answerIndex": 0, "explanation": "À demain s'utilise quand tu vas revoir la personne le lendemain."},
                {"id": "pa2mc4", "prompt": "Quelle salutation informelle sert aussi à dire au revoir ?", "options": ["Bonsoir", "Salut", "Bonne nuit"], "answerIndex": 1, "explanation": "Salut est une salutation informelle qui fonctionne dans les deux sens."},
             ]},
            {"id": "pa2-tf", "type": "true-false", "title": "Vrai ou Faux",
             "items": [
                {"id": "pa2tf1", "statement": "On utilise tu avec une personne inconnue lors d'un entretien d'embauche.", "answer": False, "explanation": "Lors d'un entretien d'embauche, l'usage normal est vous."},
                {"id": "pa2tf2", "statement": "Enchanté(e) se dit en rencontrant quelqu'un pour la première fois.", "answer": True, "explanation": "Enchanté(e) est l'expression typique en se présentant."},
                {"id": "pa2tf3", "statement": "La réponse à comment tu t'appelles ? et à comment vous appelez-vous ? est différente.", "answer": False, "explanation": "La réponse est toujours je m'appelle... ; la question change, mais pas la réponse."},
                {"id": "pa2tf4", "statement": "Bonne nuit ne s'utilise que pour se coucher.", "answer": True, "explanation": "Bonne nuit est réservée au moment de se coucher, jamais comme salutation d'arrivée."},
             ]},
            {"id": "pa2-match", "type": "matching", "title": "Associe la Situation à la Salutation",
             "items": [
                {"id": "pa2match1", "pairs": [
                    {"left": "Tu arrives au bureau à huit heures du matin", "right": "Bonjour"},
                    {"left": "Tu te couches", "right": "Bonne nuit"},
                    {"left": "Tu salues un ami dans la rue", "right": "Salut !"},
                    {"left": "Tu rencontres quelqu'un pour la première fois", "right": "Enchanté(e)"},
                ], "explanation": "Chaque situation a une salutation naturelle en français ; choisir la bonne montre courtoisie et sens du contexte."},
             ]},
            {"id": "pa2-fill", "type": "fill-blank", "title": "Complète le Dialogue",
             "items": [
                {"id": "pa2f1", "prompt": "— Comment ___-tu ? — Je m'appelle Julie.", "answers": [["t'appelles"]], "options": ["t'appelles", "s'appelle", "m'appelle"], "explanation": "T'appelles est la forme informelle avec tu."},
                {"id": "pa2f2", "prompt": "— Bonsoir, comment ___-vous ? — Très bien, merci.", "answers": [["allez"]], "options": ["allez", "vas", "va"], "explanation": "Avec vous, on utilise la forme allez, pas vas."},
                {"id": "pa2f3", "prompt": "— Bonjour, ___. — Enchanté également.", "answers": [["enchanté"]], "options": ["enchanté", "beaucoup", "merci"], "explanation": "L'expression fixe pour se présenter est enchanté(e)."},
                {"id": "pa2f4", "prompt": "— Au revoir, à ___ ! — Au revoir !", "answers": [["bientôt"]], "options": ["bientôt", "depuis", "pour"], "explanation": "À bientôt indique que tu vas revoir la personne prochainement."},
             ]},
        ],
        "summary": [
            "Bonjour fonctionne toute la journée, bonsoir le remplace le soir, et bonne nuit sert uniquement à se coucher.",
            "Comment tu t'appelles ? (informel) et Comment vous appelez-vous ? (formel) ont la même réponse : je m'appelle...",
            "Utilise tu avec les proches et vous avec les inconnus ou en contexte formel ; en cas de doute, vous est l'option sûre.",
        ],
    },
    {
        "id": "pre-a1-nombres-heure-et-date",
        "level": "Pre-A1", "unit": "1", "order": 3, "skill": "vocabulary", "strand": "nombres-temps",
        "title": "Les Nombres, l'Heure et la Date",
        "subtitle": "Les nombres de 0 à 100 (avec leurs curiosités !), comment demander et dire l'heure, les jours de la semaine et les mois.",
        "objectives": [
            "Compter et utiliser les nombres de 0 à 100 dans des situations quotidiennes.",
            "Demander et dire l'heure en français.",
            "Nommer les jours de la semaine et les mois de l'année.",
        ],
        "content": {
            "intro": "Les nombres, l'heure et la date apparaissent tous les jours — dans un magasin, à un rendez-vous, dans une conversation — c'est donc du vocabulaire de toute première priorité.",
            "explanation": "<p>Les nombres de 0 à 69 suivent une logique assez régulière, mais à partir de <strong>70</strong>, le français devient célèbre pour ses curiosités : <em>soixante-dix</em> (70) est littéralement «&nbsp;soixante-dix&nbsp;», <em>quatre-vingts</em> (80) est «&nbsp;quatre fois vingt&nbsp;», et <em>quatre-vingt-dix</em> (90) combine les deux. Ce système, hérité d'un ancien comptage en base vingt, demande un peu de pratique.</p><p>Pour demander l'heure, on dit <strong>Quelle heure est-il ?</strong>, et pour répondre on utilise <em>il est</em> pour toutes les heures : <em>Il est une heure</em> (singulier, sans s) mais <em>Il est deux heures, il est trois heures...</em> (avec s). La date s'organise avec le jour d'abord, puis le mois : <em>le 15 mars</em>.</p>",
            "rules": [
                {"heading": "a) Nombres de 0 à 30", "body": "<ul><li>0 zéro, 1 un, 2 deux, 3 trois, 4 quatre, 5 cinq</li><li>6 six, 7 sept, 8 huit, 9 neuf, 10 dix</li><li>11 onze, 12 douze, 13 treize, 14 quatorze, 15 quinze</li><li>16 seize... 19 dix-neuf, 20 vingt</li><li>21 vingt et un... 29 vingt-neuf, 30 trente</li></ul>"},
                {"heading": "b) Nombres de 31 à 100 (les curiosités)", "body": "<ul><li>De 31 à 69 : trente et un, trente-deux... soixante-neuf (logique régulière).</li><li><strong>70 soixante-dix</strong> (60+10), <strong>80 quatre-vingts</strong> (4×20), <strong>90 quatre-vingt-dix</strong> (4×20+10).</li><li>71 soixante et onze, 81 quatre-vingt-un, 91 quatre-vingt-onze.</li><li>100 cent (mais <em>cent un, cent deux...</em> à partir de 101, sans et).</li></ul>"},
                {"heading": "c) Dire l'heure", "body": "<ul><li><strong>Quelle heure est-il ?</strong> — question générale pour savoir l'heure.</li><li><em>Il est une heure</em> — seulement pour 1h00 (singulier).</li><li><em>Il est deux heures, il est dix heures...</em> — pour toutes les autres heures (pluriel).</li><li><em>Il est quatre heures et demie</em> (4h30) ; <em>il est cinq heures moins le quart</em> (4h45).</li></ul>"},
                {"heading": "d) Jours et mois", "body": "<ul><li>Jours : lundi, mardi, mercredi, jeudi, vendredi, samedi, dimanche.</li><li>Mois : janvier, février, mars, avril, mai, juin, juillet, août, septembre, octobre, novembre, décembre.</li><li>Les jours et les mois s'écrivent en minuscule en français.</li></ul>"},
            ],
            "examples": [
                "J'ai vingt-cinq ans.",
                "Il est trois heures et demie de l'après-midi.",
                "Aujourd'hui, c'est lundi 3 mars.",
                "Mon anniversaire est le 20 juillet.",
                "Il est une heure pile.",
                "J'ai besoin de quatre-vingt-dix-neuf euros.",
                "Le dimanche, je ne travaille pas.",
                "Décembre est le dernier mois de l'année.",
            ],
            "commonMistakes": [
                {"wrong": "Il est une heures de l'après-midi.", "right": "Il est une heure de l'après-midi.", "why": "Seule une heure reste au singulier ; toutes les autres heures prennent un s (deux heures, trois heures...)."},
                {"wrong": "Aujourd'hui, c'est Lundi, 3 Mars.", "right": "Aujourd'hui, c'est lundi, 3 mars.", "why": "En français, les jours de la semaine et les mois s'écrivent toujours avec une minuscule initiale."},
                {"wrong": "quatre-vingt-dix se dit \"neuf-dix\"", "right": "quatre-vingt-dix", "why": "Le français compte 90 comme 4×20+10, pas comme un mot indépendant ; c'est une des difficultés classiques du système numérique français."},
            ],
        },
        "exercises": [
            {"id": "pa3-mc", "type": "multiple-choice", "title": "Nombres, Heure et Date",
             "items": [
                {"id": "pa3mc1", "prompt": "Comment dit-on 80 en français ?", "options": ["huit-dix", "quatre-vingts", "octante"], "answerIndex": 1, "explanation": "Quatre-vingts signifie littéralement « quatre fois vingt »."},
                {"id": "pa3mc2", "prompt": "Que dit-on pour 1h00 ?", "options": ["Il est une heures", "Il est une heure", "Il est un heure"], "answerIndex": 1, "explanation": "Seule une heure reste au singulier ; toutes les autres heures utilisent le pluriel."},
                {"id": "pa3mc3", "prompt": "Quel est le premier jour de la semaine dans le calendrier français ?", "options": ["dimanche", "lundi", "samedi"], "answerIndex": 1, "explanation": "En France, la semaine commence traditionnellement le lundi."},
                {"id": "pa3mc4", "prompt": "Quel mois vient après juin ?", "options": ["mai", "juillet", "août"], "answerIndex": 1, "explanation": "L'ordre des mois est ...mai, juin, juillet, août..."},
                {"id": "pa3mc5", "prompt": "Comment s'écrit 70 ?", "options": ["septante", "soixante-dix", "sept-dix"], "answerIndex": 1, "explanation": "Soixante-dix est la forme standard en français de France (septante s'utilise en Belgique et en Suisse)."},
             ]},
            {"id": "pa3-tf", "type": "true-false", "title": "Vrai ou Faux",
             "items": [
                {"id": "pa3tf1", "statement": "Les jours de la semaine s'écrivent avec une majuscule en français.", "answer": False, "explanation": "Ils s'écrivent en minuscule : lundi, mardi, mercredi..."},
                {"id": "pa3tf2", "statement": "Il est deux heures s'utilise pour 2h00.", "answer": True, "explanation": "À partir de deux heures, on utilise toujours le pluriel."},
                {"id": "pa3tf3", "statement": "90 se dit quatre-vingt-dix, littéralement 4×20+10.", "answer": True, "explanation": "Oui — c'est l'une des curiosités les plus connues du système numérique français."},
                {"id": "pa3tf4", "statement": "Vingt et un s'écrit tout attaché, sans espace : vingtetun.", "answer": False, "explanation": "Il s'écrit en trois mots séparés (avec des traits d'union à l'écrit courant) : vingt et un."},
             ]},
            {"id": "pa3-match", "type": "matching", "title": "Associe le Nombre à sa Forme Écrite",
             "items": [
                {"id": "pa3match1", "pairs": [
                    {"left": "15", "right": "quinze"},
                    {"left": "21", "right": "vingt et un"},
                    {"left": "70", "right": "soixante-dix"},
                    {"left": "80", "right": "quatre-vingts"},
                    {"left": "99", "right": "quatre-vingt-dix-neuf"},
                ], "explanation": "À partir de 70, le français compte par blocs de vingt hérités d'un ancien système vigésimal."},
             ]},
            {"id": "pa3-fill", "type": "fill-blank", "title": "Complète l'Heure et la Date",
             "items": [
                {"id": "pa3f1", "prompt": "— Quelle heure est-il ? — Il ___ cinq heures.", "answers": [["est"]], "options": ["est", "sont", "a"], "explanation": "On utilise toujours il est pour donner l'heure, jamais ils sont."},
                {"id": "pa3f2", "prompt": "Le premier mois de l'année est ___.", "answers": [["janvier"]], "options": ["janvier", "décembre", "mars"], "explanation": "Janvier est le premier mois du calendrier, suivi de février."},
                {"id": "pa3f3", "prompt": "Le dernier jour de la semaine (dans le calendrier français) est ___.", "answers": [["dimanche"]], "options": ["dimanche", "samedi", "lundi"], "explanation": "La semaine se termine le dimanche."},
                {"id": "pa3f4", "prompt": "J'ai trente-___ ans (35).", "answers": [["cinq"]], "options": ["cinq", "six", "quatre"], "explanation": "Trente-cinq, c'est 35."},
             ]},
        ],
        "summary": [
            "Les nombres de 0 à 69 suivent une logique régulière ; à partir de 70, le français compte par blocs de vingt (soixante-dix, quatre-vingts, quatre-vingt-dix).",
            "Il est une heure est la seule heure au singulier ; toutes les autres utilisent le pluriel (il est deux heures, il est trois heures...).",
            "Les jours de la semaine et les mois de l'année s'écrivent en minuscule et la semaine commence le lundi.",
        ],
    },
    {
        "id": "pre-a1-vocabulaire-de-classe-et-etude",
        "level": "Pre-A1", "unit": "1", "order": 4, "skill": "vocabulary", "strand": "classe",
        "title": "Vocabulaire de Classe et d'Étude",
        "subtitle": "Les mots et phrases essentiels pour survivre — et apprendre — dans un cours de français.",
        "objectives": [
            "Utiliser des phrases de base pour demander de l'aide ou une répétition en classe.",
            "Nommer les objets les plus courants d'un étudiant.",
            "Comprendre des consignes simples données par un professeur de français.",
        ],
        "content": {
            "intro": "Avant de parler du monde, il faut survivre dans la salle de classe : demander de répéter, dire que tu ne comprends pas, et nommer ce que tu as sur ta table.",
            "explanation": "<p>Dans un cours de français, tu vas entendre et avoir besoin des mêmes phrases très souvent : <strong>répétez, s'il vous plaît</strong> 🔁, <strong>je ne comprends pas</strong>, <strong>comment dit-on... ?</strong> Ces phrases sont ton outil le plus utile en tant que débutant — elles te permettent de suivre le cours sans frustration.</p><p>Il te faut aussi les noms des objets que tu utilises chaque jour pour étudier : le <strong>cahier</strong> 📓, le <strong>crayon</strong> ✏️, le <strong>livre</strong> 📖, le <strong>stylo</strong>. Les apprendre maintenant t'aide à comprendre des consignes simples comme <em>ouvrez le livre</em> ou <em>écrivez dans le cahier</em>.</p>",
            "rules": [
                {"heading": "a) Phrases pour demander de l'aide", "body": "<ul><li><strong>Répétez, s'il vous plaît</strong> — quand tu n'as pas bien entendu.</li><li><strong>Je ne comprends pas</strong> — quand tu ne comprends pas quelque chose.</li><li><strong>Comment dit-on... en français ?</strong> — pour demander un mot nouveau.</li><li><strong>Pouvez-vous parler plus lentement, s'il vous plaît ?</strong> — quand la personne parle trop vite.</li></ul>"},
                {"heading": "b) Objets de l'étudiant", "body": "<ul><li>le cahier 📓, le crayon ✏️, le stylo, la gomme</li><li>le livre 📖, le sac à dos, la feuille de papier</li><li>la table, la chaise, le tableau</li></ul>"},
                {"heading": "c) Consignes typiques du professeur", "body": "<ul><li><strong>Ouvrez le livre</strong> — ouvre ton livre.</li><li><strong>Écrivez dans le cahier</strong> — utilise le cahier pour écrire.</li><li><strong>Écoutez attentivement</strong> — fais attention à l'audio ou à la voix.</li><li><strong>Travaillez avec votre camarade</strong> — fais l'exercice avec une autre personne.</li></ul>"},
            ],
            "examples": [
                "Pardon, je ne comprends pas. Pouvez-vous répéter, s'il vous plaît ?",
                "Comment dit-on ce mot encore une fois, s'il vous plaît ?",
                "J'ai besoin d'un crayon et d'une feuille de papier.",
                "Ouvrez le livre à la page dix.",
                "Écrivez votre nom dans le cahier.",
                "Pouvez-vous parler plus lentement, s'il vous plaît ?",
                "Mon sac à dos contient deux cahiers et un stylo.",
                "Écoutez attentivement le dialogue.",
            ],
            "commonMistakes": [
                {"wrong": "Rester silencieux quand tu ne comprends pas quelque chose.", "right": "Je ne comprends pas. Pouvez-vous répéter, s'il vous plaît ?", "why": "Demander de l'aide avec une phrase simple est normal et attendu en classe — c'est mieux que de rester muet."},
                {"wrong": "Je comprends pas non.", "right": "Je ne comprends pas.", "why": "La négation française se construit avec ne...pas autour du verbe, pas avec non après."},
                {"wrong": "Comment dit-on en français ce mot ?", "right": "Comment dit-on ce mot en français ?", "why": "L'ordre naturel place le mot en question avant en français."},
            ],
        },
        "exercises": [
            {"id": "pa4-mc", "type": "multiple-choice", "title": "Phrases et Objets de Classe",
             "items": [
                {"id": "pa4mc1", "prompt": "Tu n'as pas bien entendu ce qu'a dit le professeur. Que dis-tu ?", "options": ["Je ne comprends pas", "Répétez, s'il vous plaît", "Enchanté"], "answerIndex": 1, "explanation": "Répétez, s'il vous plaît sert à demander de redire quelque chose."},
                {"id": "pa4mc2", "prompt": "Tu ne comprends pas un mot. Que dis-tu ?", "options": ["Je ne comprends pas", "Bonjour", "Au revoir"], "answerIndex": 0, "explanation": "Je ne comprends pas exprime que tu ne comprends pas quelque chose."},
                {"id": "pa4mc3", "prompt": "Quel objet utilises-tu pour écrire à l'encre ?", "options": ["le crayon", "le stylo", "la gomme"], "answerIndex": 1, "explanation": "Le stylo écrit à l'encre ; le crayon utilise du graphite et s'efface avec la gomme."},
                {"id": "pa4mc4", "prompt": "Le professeur parle très vite. Que lui demandes-tu ?", "options": ["Pouvez-vous parler plus lentement, s'il vous plaît ?", "Comment vous appelez-vous ?", "Enchanté"], "answerIndex": 0, "explanation": "Cette phrase demande spécifiquement de parler plus lentement."},
                {"id": "pa4mc5", "prompt": "Où ranges-tu tes cahiers et tes livres pour aller en cours ?", "options": ["dans le tableau", "dans le sac à dos", "dans la chaise"], "answerIndex": 1, "explanation": "Le sac à dos est l'endroit où tu transportes tes affaires de classe."},
             ]},
            {"id": "pa4-tf", "type": "true-false", "title": "Vrai ou Faux",
             "items": [
                {"id": "pa4tf1", "statement": "Je ne comprends pas est une phrase utile quand tu ne comprends pas quelque chose en classe.", "answer": True, "explanation": "C'est exactement la phrase correcte pour exprimer un manque de compréhension."},
                {"id": "pa4tf2", "statement": "La gomme sert à écrire à l'encre.", "answer": False, "explanation": "La gomme sert à effacer ce qui est écrit au crayon ; le stylo écrit à l'encre."},
                {"id": "pa4tf3", "statement": "Répétez, s'il vous plaît s'utilise quand tu veux réentendre quelque chose.", "answer": True, "explanation": "Exactement — tu demandes à l'autre personne de redire la même chose."},
                {"id": "pa4tf4", "statement": "Le tableau est un objet qu'un étudiant transporte dans son sac à dos.", "answer": False, "explanation": "Le tableau est fixé dans la salle de classe ; les étudiants ne le transportent pas dans leur sac."},
             ]},
            {"id": "pa4-match", "type": "matching", "title": "Associe l'Objet à sa Description",
             "items": [
                {"id": "pa4match1", "pairs": [
                    {"left": "le cahier", "right": "où tu écris tes notes de cours"},
                    {"left": "le crayon", "right": "peut s'effacer avec la gomme"},
                    {"left": "le sac à dos", "right": "où tu transportes tes affaires"},
                    {"left": "le tableau", "right": "où le professeur écrit pour toute la classe"},
                ], "explanation": "Reconnaître ces objets t'aide à suivre des consignes simples dès le premier jour de cours."},
             ]},
            {"id": "pa4-fill", "type": "fill-blank", "title": "Complète la Phrase de Survie",
             "items": [
                {"id": "pa4f1", "prompt": "Pardon, je ne ___ pas. Pouvez-vous répéter ?", "answers": [["comprends"]], "options": ["comprends", "comprend", "comprenez"], "explanation": "Comprends est la forme je, la personne qui parle."},
                {"id": "pa4f2", "prompt": "Comment ___-on ce mot en français ?", "answers": [["dit"]], "options": ["dit", "dites", "dis"], "explanation": "Dit-on est la forme impersonnelle utilisée pour demander le nom de quelque chose."},
                {"id": "pa4f3", "prompt": "___ le livre à la page dix, s'il vous plaît.", "answers": [["Ouvrez"]], "options": ["Ouvrez", "Ouvre", "Ouvrir"], "explanation": "Ouvrez est la forme de consigne (impératif avec vous) que donne le professeur."},
                {"id": "pa4f4", "prompt": "J'ai besoin d'un ___ pour écrire à l'encre.", "answers": [["stylo"]], "options": ["stylo", "crayon", "gomme"], "explanation": "Le stylo est l'objet qui écrit à l'encre."},
             ]},
        ],
        "summary": [
            "Répétez, s'il vous plaît ; je ne comprends pas ; et comment dit-on... ? sont les trois phrases les plus utiles pour survivre dans un cours de français.",
            "Le cahier, le crayon, le stylo et le livre sont les objets de base de tout étudiant.",
            "Reconnaître des consignes simples comme ouvrez le livre ou écoutez attentivement te permet de suivre le cours sans dépendre de traductions.",
        ],
    },
    {
        "id": "pre-a1-personnes-et-objets-du-quotidien",
        "level": "Pre-A1", "unit": "1", "order": 5, "skill": "vocabulary", "strand": "personnes-objets",
        "title": "Personnes et Objets du Quotidien — le Genre",
        "subtitle": "Vocabulaire de base pour parler des personnes (homme, femme, enfant) et des choses que tu vois chaque jour — et le genre grammatical dès le départ.",
        "objectives": [
            "Nommer les personnes les plus courantes de ton entourage quotidien.",
            "Identifier des objets courants de la maison et de la rue.",
            "Utiliser correctement le, la, l' et un, une selon le genre de chaque mot.",
        ],
        "content": {
            "intro": "Avant de former des phrases longues, il te faut les mots les plus fréquents pour parler des personnes et des objets qui t'entourent chaque jour — et, en français, cela veut dire apprendre le genre dès le premier mot.",
            "explanation": "<p>En français, <strong>tous les noms ont un genre</strong> : ils sont masculins ou féminins, et portent un article — <strong>le</strong> (masculin), <strong>la</strong> (féminin), ou <strong>l'</strong> devant une voyelle — devant eux. Contrairement à l'espagnol ou l'italien, la terminaison du mot ne donne pas toujours d'indice fiable sur son genre : il faut apprendre chaque mot avec son article.</p><p>Pour parler des personnes, on utilise des mots comme <strong>l'homme</strong>, <strong>la femme</strong>, <strong>le garçon</strong>, <strong>la fille</strong>. Pour parler des objets de tous les jours, on utilise des mots comme <strong>la table</strong>, <strong>la chaise</strong>, <strong>le téléphone</strong> 📱, <strong>la maison</strong> 🏠. Au pluriel, un/une deviennent <strong>des</strong>, et le/la deviennent <strong>les</strong>.</p>",
            "rules": [
                {"heading": "a) Personnes", "body": "<ul><li><strong>l'homme</strong> / <strong>la femme</strong></li><li><strong>le garçon</strong> / <strong>la fille</strong></li><li><strong>l'ami</strong> / <strong>l'amie</strong></li><li><strong>la personne</strong> — toujours féminin, même pour parler d'un homme.</li></ul>"},
                {"heading": "b) Objets de la maison", "body": "<ul><li><strong>la table</strong>, <strong>la chaise</strong>, <strong>la porte</strong>, <strong>la fenêtre</strong></li><li><strong>le téléphone</strong> 📱, <strong>le canapé</strong>, <strong>le livre</strong> 📖</li><li><strong>la maison</strong> 🏠 — l'endroit où tu habites.</li></ul>"},
                {"heading": "c) Le, la, l' et un, une : le genre de l'article", "body": "<ul><li>Devant une consonne : <em>le livre</em> (masc.), <em>la table</em> (fém.).</li><li>Devant une voyelle ou un h muet, le/la deviennent <strong>l'</strong> : <em>l'homme, l'amie</em>.</li><li>Au singulier indéfini : <strong>un</strong> livre, <strong>une</strong> table ; au pluriel, les deux deviennent <strong>des</strong> : <em>des livres, des tables</em>.</li></ul>"},
            ],
            "examples": [
                "L'homme parle avec la femme.",
                "La fille a un nouveau livre.",
                "Mon téléphone est sur la table.",
                "La maison a quatre chaises.",
                "Le garçon ouvre la porte.",
                "Mon amie habite près de ma maison.",
                "La fenêtre de la maison est grande.",
            ],
            "commonMistakes": [
                {"wrong": "Le table", "right": "La table", "why": "Table est un mot féminin ; son article correct est la, même si aucune règle de terminaison ne le prédit ici."},
                {"wrong": "La téléphone", "right": "Le téléphone", "why": "Téléphone est un mot masculin ; l'article correct est le."},
                {"wrong": "Le personne (pour parler d'un homme)", "right": "La personne (toujours, même pour parler d'un homme)", "why": "Personne est toujours féminin en français, quel que soit le genre de la personne décrite."},
            ],
        },
        "exercises": [
            {"id": "pa5-mc", "type": "multiple-choice", "title": "Personnes et Objets",
             "items": [
                {"id": "pa5mc1", "prompt": "Quel est l'article correct pour table ?", "options": ["le", "la"], "answerIndex": 1, "explanation": "Table est un mot féminin : la table."},
                {"id": "pa5mc2", "prompt": "Quel est l'article correct pour téléphone ?", "options": ["le", "la"], "answerIndex": 0, "explanation": "Téléphone est masculin : le téléphone."},
                {"id": "pa5mc3", "prompt": "Comment dit-on la personne adulte de sexe féminin ?", "options": ["l'homme", "la femme", "la fille"], "answerIndex": 1, "explanation": "La femme est la personne adulte de genre féminin."},
                {"id": "pa5mc4", "prompt": "Quel mot utilise-t-on toujours au féminin, même pour parler d'un homme ?", "options": ["la personne", "l'homme", "la maison"], "answerIndex": 0, "explanation": "Personne est toujours féminin en français, indépendamment de qui elle décrit."},
                {"id": "pa5mc5", "prompt": "Où habites-tu ?", "options": ["dans la maison", "dans le maison", "dans la table"], "answerIndex": 0, "explanation": "Maison est féminin : la maison ; avec la préposition dans on dit dans la maison."},
             ]},
            {"id": "pa5-tf", "type": "true-false", "title": "Vrai ou Faux",
             "items": [
                {"id": "pa5tf1", "statement": "La terminaison d'un mot français permet toujours de deviner son genre.", "answer": False, "explanation": "Contrairement à d'autres langues romanes, il n'y a pas de règle fiable pour tous les mots ; il faut apprendre chaque mot avec son article."},
                {"id": "pa5tf2", "statement": "Le garçon et la fille utilisent des articles différents.", "answer": True, "explanation": "Le garçon est masculin et la fille est féminin, chacun avec son propre article."},
                {"id": "pa5tf3", "statement": "Le mot personne prend toujours l'article la.", "answer": True, "explanation": "Personne est un mot féminin fixe, quel que soit le genre de la personne décrite."},
                {"id": "pa5tf4", "statement": "Le téléphone est un mot féminin.", "answer": False, "explanation": "Téléphone est masculin : le téléphone."},
             ]},
            {"id": "pa5-match", "type": "matching", "title": "Associe le Mot à son Article",
             "items": [
                {"id": "pa5match1", "pairs": [
                    {"left": "table", "right": "la table"},
                    {"left": "téléphone", "right": "le téléphone"},
                    {"left": "maison", "right": "la maison"},
                    {"left": "homme", "right": "l'homme"},
                    {"left": "fille", "right": "la fille"},
                ], "explanation": "Apprendre chaque mot avec son article (le, la ou l') est la meilleure façon de mémoriser correctement le genre."},
             ]},
            {"id": "pa5-fill", "type": "fill-blank", "title": "Complète avec Le, La ou L'",
             "items": [
                {"id": "pa5f1", "prompt": "___ femme parle avec ___ homme.", "answers": [["la"], ["l'"]], "explanation": "Femme est féminin (la) et homme est masculin mais commence par une voyelle (l')."},
                {"id": "pa5f2", "prompt": "J'ai besoin d'utiliser ___ nouveau téléphone.", "answers": [["le"]], "options": ["le", "la", "l'"], "explanation": "Téléphone est masculin et commence par une consonne : le téléphone."},
                {"id": "pa5f3", "prompt": "___ maison a quatre chaises.", "answers": [["La"]], "options": ["La", "Le", "L'"], "explanation": "Maison est féminin : la maison."},
                {"id": "pa5f4", "prompt": "___ garçon ouvre la porte.", "answers": [["Le"]], "options": ["Le", "La", "L'"], "explanation": "Garçon est masculin : le garçon."},
             ]},
        ],
        "summary": [
            "En français, chaque nom a un genre (masculin ou féminin) et porte un article : le, la, ou l' devant une voyelle.",
            "Les mots les plus fréquents pour les personnes sont l'homme, la femme, le garçon et la fille ; personne est toujours féminin.",
            "La terminaison d'un mot n'indique pas toujours son genre de façon fiable : mieux vaut apprendre chaque mot avec son article.",
        ],
    },
    {
        "id": "pre-a1-verbes-de-base-etre-avoir-vouloir-aimer",
        "level": "Pre-A1", "unit": "1", "order": 6, "skill": "grammar", "strand": "verbes-de-base",
        "title": "Verbes de Base : Être, Avoir, Vouloir, Aimer",
        "subtitle": "Un premier contact avec quatre verbes essentiels, dans des phrases très simples avec je, tu et il/elle.",
        "objectives": [
            "Utiliser le verbe être pour dire qui tu es et comment tu es.",
            "Utiliser le verbe avoir pour dire ce que tu as ou quel âge tu as.",
            "Utiliser vouloir et aimer dans des phrases simples pour exprimer des souhaits et des préférences.",
        ],
        "content": {
            "intro": "Avec seulement quatre verbes — être, avoir, vouloir et aimer — tu peux déjà former des dizaines de phrases utiles sur toi-même et sur les personnes que tu connais.",
            "explanation": "<p>Le verbe <strong>être</strong> sert à dire qui tu es, d'où tu viens ou comment tu es : <em>Je suis Anna. Je suis française. Je suis grande.</em> Le verbe <strong>avoir</strong> sert à parler de possession et aussi de l'âge : <em>J'ai un chien. J'ai vingt ans.</em> (Jamais <em>je suis vingt ans</em> — c'est une des erreurs les plus fréquentes des débutants.)</p><p>Le verbe <strong>vouloir</strong> exprime un souhait : <em>Je veux un café.</em> Le verbe <strong>aimer</strong> exprime une préférence ou un sentiment : <em>J'aime la musique.</em> Ces quatre verbes sont tous irréguliers, donc leurs formes doivent simplement être mémorisées.</p>",
            "rules": [
                {"heading": "a) Être (je/tu/il-elle)", "body": "<ul><li>je <strong>suis</strong> — <em>Je suis professeur.</em></li><li>tu <strong>es</strong> — <em>Tu es très gentil.</em></li><li>il/elle <strong>est</strong> — <em>Elle est du Pérou.</em></li></ul>"},
                {"heading": "b) Avoir (je/tu/il-elle)", "body": "<ul><li>j'<strong>ai</strong> — <em>J'ai deux frères.</em></li><li>tu <strong>as</strong> — <em>Tu as le temps ?</em></li><li>il/elle <strong>a</strong> — <em>Il a trente ans.</em></li></ul>"},
                {"heading": "c) Vouloir (je/tu/il-elle)", "body": "<ul><li>je <strong>veux</strong> — <em>Je veux de l'eau, s'il vous plaît.</em></li><li>tu <strong>veux</strong> — <em>Qu'est-ce que tu veux manger ?</em></li><li>il/elle <strong>veut</strong> — <em>Elle veut se reposer.</em></li></ul>"},
                {"heading": "d) Aimer (je/tu/il-elle)", "body": "<ul><li>j'<strong>aime</strong> le café. (goût, préférence)</li><li>tu <strong>aimes</strong> la musique ?</li><li>il/elle <strong>aime</strong> le chocolat.</li><li>Le sujet est toujours la personne, pas la chose — contrairement à l'espagnol gustar.</li></ul>"},
            ],
            "examples": [
                "Je suis Marc et je suis du Canada.",
                "J'ai vingt-huit ans.",
                "Tu as des frères et sœurs ?",
                "Je veux un café au lait, s'il vous plaît.",
                "J'aime beaucoup la musique.",
                "Tu aimes le chocolat ?",
                "Elle est très sympathique.",
                "Il a un petit chien.",
            ],
            "commonMistakes": [
                {"wrong": "Je suis vingt ans.", "right": "J'ai vingt ans.", "why": "L'âge se dit toujours avec avoir en français, jamais avec être."},
                {"wrong": "Elle a sympathique.", "right": "Elle est sympathique.", "why": "Les qualités et les caractéristiques s'expriment avec être, pas avec avoir."},
                {"wrong": "Je aime le café.", "right": "J'aime le café.", "why": "Je s'élide en j' devant une voyelle ; on ne dit jamais je aime."},
            ],
        },
        "exercises": [
            {"id": "pa6-mc", "type": "multiple-choice", "title": "Choisis le Bon Verbe",
             "items": [
                {"id": "pa6mc1", "prompt": "Comment dit-on ton âge en français ?", "options": ["Je suis vingt ans", "J'ai vingt ans", "Je veux vingt ans"], "answerIndex": 1, "explanation": "L'âge s'exprime avec avoir, pas avec être."},
                {"id": "pa6mc2", "prompt": "Comment dis-tu que tu aimes le café ?", "options": ["Je suis le café", "J'aime le café", "J'ai le café"], "answerIndex": 1, "explanation": "Aimer exprime une préférence, avec la personne comme sujet."},
                {"id": "pa6mc3", "prompt": "Tu veux dire d'où tu viens. Quel verbe utilises-tu ?", "options": ["avoir", "être", "vouloir"], "answerIndex": 1, "explanation": "L'origine s'exprime avec être : je suis de..."},
                {"id": "pa6mc4", "prompt": "Comment demandes-tu quelque chose que tu désires dans un café ?", "options": ["Je suis un café, s'il vous plaît", "Je veux un café, s'il vous plaît", "J'ai un café, s'il vous plaît"], "answerIndex": 1, "explanation": "Vouloir exprime un souhait direct : je veux un café."},
                {"id": "pa6mc5", "prompt": "Quelle est la forme tu du verbe avoir ?", "options": ["as", "ai", "a"], "answerIndex": 0, "explanation": "As est la forme tu : tu as des frères et sœurs ?"},
             ]},
            {"id": "pa6-tf", "type": "true-false", "title": "Vrai ou Faux",
             "items": [
                {"id": "pa6tf1", "statement": "En français, l'âge s'exprime avec le verbe être.", "answer": False, "explanation": "L'âge s'exprime avec avoir : j'ai vingt ans."},
                {"id": "pa6tf2", "statement": "J'aime le café est correct pour dire que tu aimes le café.", "answer": True, "explanation": "C'est exactement la forme correcte avec le verbe aimer."},
                {"id": "pa6tf3", "statement": "Es est la forme correcte de je avec le verbe être.", "answer": False, "explanation": "La forme correcte de je est suis ; es est la forme de tu."},
                {"id": "pa6tf4", "statement": "Veux sert à exprimer un souhait.", "answer": True, "explanation": "Veux exprime un souhait ou une demande directe."},
             ]},
            {"id": "pa6-match", "type": "matching", "title": "Associe le Pronom à la Forme du Verbe",
             "items": [
                {"id": "pa6match1", "pairs": [
                    {"left": "je (être)", "right": "suis"},
                    {"left": "tu (avoir)", "right": "as"},
                    {"left": "il/elle (vouloir)", "right": "veut"},
                    {"left": "j' (aimer)", "right": "aime"},
                    {"left": "j' (avoir)", "right": "ai"},
                ], "explanation": "Chaque pronom a sa propre forme du verbe ; je s'élide en j' devant une voyelle."},
             ]},
            {"id": "pa6-fill", "type": "fill-blank", "title": "Complète avec le Bon Verbe",
             "items": [
                {"id": "pa6f1", "prompt": "Je ___ professeur de français.", "answers": [["suis"]], "options": ["suis", "es", "est"], "explanation": "Suis est la forme je du verbe être."},
                {"id": "pa6f2", "prompt": "Quel âge ___-tu ?", "answers": [["as"]], "options": ["as", "ai", "a"], "explanation": "As est la forme tu du verbe avoir."},
                {"id": "pa6f3", "prompt": "Elle ___ se reposer un peu.", "answers": [["veut"]], "options": ["veut", "veux", "voulons"], "explanation": "Veut est la forme il/elle du verbe vouloir."},
                {"id": "pa6f4", "prompt": "J'___ beaucoup la musique.", "answers": [["aime"]], "options": ["aime", "aimes", "aiment"], "explanation": "Aime est la forme j' du verbe aimer."},
             ]},
        ],
        "summary": [
            "Être exprime l'identité, l'origine et les caractéristiques (je suis, tu es, il/elle est) ; avoir exprime la possession et l'âge (j'ai, tu as, il/elle a).",
            "Vouloir exprime un souhait direct (je veux, tu veux, il/elle veut), utile pour demander des choses simplement et poliment.",
            "Aimer garde la personne comme sujet (j'aime, tu aimes, il/elle aime) — contrairement au gustar espagnol, la chose aimée n'est jamais le sujet.",
        ],
    },
    {
        "id": "pre-a1-pronoms-sujets-et-etre-avoir",
        "level": "Pre-A1", "unit": "1", "order": 7, "skill": "grammar", "strand": "pronoms",
        "title": "Pronoms Sujets et un Premier Aperçu de Être et Avoir",
        "subtitle": "Je, tu, il/elle, nous, ils/elles ; et la différence simple entre je suis de... (origine) et je suis à... (lieu).",
        "objectives": [
            "Reconnaître et utiliser les pronoms sujets je, tu, il/elle, nous et ils/elles.",
            "Utiliser je suis de... pour dire d'où tu viens.",
            "Utiliser je suis à/en/au... pour dire où tu te trouves en ce moment.",
        ],
        "content": {
            "intro": "Les pronoms sujets identifient qui fait l'action, et une seule paire de prépositions — de pour l'origine, à/en/au pour le lieu — te permet de parler de ton origine et de ta position dès le premier jour.",
            "explanation": "<p>Les pronoms sujets les plus utilisés sont <strong>je</strong>, <strong>tu</strong>, <strong>il</strong>/<strong>elle</strong>, <strong>nous</strong> et <strong>ils</strong>/<strong>elles</strong>. Contrairement à l'espagnol ou à l'italien, le français ne peut presque jamais omettre le pronom sujet : la terminaison du verbe seule ne suffit pas à identifier qui parle, donc le pronom est toujours présent.</p><p>Le français utilise <strong>être</strong> aussi bien pour l'origine que pour le lieu, mais avec des prépositions différentes : <em>Je suis de Lyon</em> (origine, avec <strong>de</strong>) contre <em>Je suis à Lyon</em> (lieu actuel, avec <strong>à</strong>). Pour les pays, la préposition de lieu change selon le genre : <strong>à</strong> + ville, <strong>en</strong> + pays féminin (<em>en France</em>), <strong>au</strong> + pays masculin (<em>au Canada</em>), <strong>aux</strong> + pays pluriel (<em>aux États-Unis</em>).</p>",
            "rules": [
                {"heading": "a) Les pronoms sujets", "body": "<ul><li><strong>je</strong> — la personne qui parle.</li><li><strong>tu</strong> — la personne à qui tu parles (informel).</li><li><strong>il / elle</strong> — une autre personne (masculin/féminin).</li><li><strong>nous</strong> — toi (qui parles) et d'autres personnes.</li><li><strong>ils / elles</strong> — plusieurs personnes dont tu parles.</li></ul>"},
                {"heading": "b) Je suis de... pour l'origine", "body": "<ul><li><em>Je suis de Marseille.</em></li><li><em>Tu es d'où ?</em></li><li><em>Elle est du Japon.</em> (de + le = du)</li></ul>"},
                {"heading": "c) Je suis à/en/au... pour le lieu", "body": "<ul><li><em>Je suis à la maison.</em></li><li><em>Où es-tu maintenant ?</em></li><li><em>Elle est au travail.</em> (à + le = au)</li></ul>"},
                {"heading": "d) Un contraste simple", "body": "<ul><li><strong>Je suis du Chili</strong> — d'où je viens (origine, avec de/du).</li><li><strong>Je suis au Chili</strong> — où je me trouve maintenant (lieu, avec à/au).</li><li>Une personne peut venir d'un pays et se trouver dans un autre en même temps.</li></ul>"},
            ],
            "examples": [
                "Je suis du Brésil.",
                "Tu es à l'université maintenant.",
                "Elle est du Portugal, mais elle est en France.",
                "Nous sommes de la même ville.",
                "Ils sont au parc.",
                "Tu es d'où ?",
                "Où es-tu en ce moment ?",
            ],
            "commonMistakes": [
                {"wrong": "Je suis en Espagne (pour dire mon origine).", "right": "Je suis d'Espagne.", "why": "L'origine s'exprime avec de (je suis de/d'...), pas avec en, qui indique un lieu actuel."},
                {"wrong": "Elle est de l'école (pour dire où elle est maintenant).", "right": "Elle est à l'école.", "why": "Le lieu où quelqu'un se trouve s'exprime avec à/en/au, pas avec de, qui indique l'origine."},
                {"wrong": "Ils est du Pérou.", "right": "Ils sont du Pérou.", "why": "Avec le pronom ils, le verbe être prend la forme sont, pas est."},
            ],
        },
        "exercises": [
            {"id": "pa7-mc", "type": "multiple-choice", "title": "Pronoms, Origine et Lieu",
             "items": [
                {"id": "pa7mc1", "prompt": "Quel pronom utilises-tu pour parler de toi-même ?", "options": ["tu", "je", "il"], "answerIndex": 1, "explanation": "Je est le pronom de la première personne, celle qui parle."},
                {"id": "pa7mc2", "prompt": "Comment dis-tu d'où tu viens ?", "options": ["Je suis à...", "Je suis de...", "J'ai de..."], "answerIndex": 1, "explanation": "L'origine s'exprime avec je suis de..."},
                {"id": "pa7mc3", "prompt": "Comment dis-tu où tu te trouves maintenant ?", "options": ["Je suis de...", "Je suis à...", "Je veux à..."], "answerIndex": 1, "explanation": "Le lieu actuel s'exprime avec je suis à..."},
                {"id": "pa7mc4", "prompt": "Quel pronom utilises-tu pour parler d'un groupe qui t'inclut ?", "options": ["ils", "nous", "tu"], "answerIndex": 1, "explanation": "Nous inclut la personne qui parle avec d'autres."},
                {"id": "pa7mc5", "prompt": "Anna et Léo sont à la plage. Quel pronom les représente ?", "options": ["nous", "ils", "elle"], "answerIndex": 1, "explanation": "Ils s'utilise pour parler de plusieurs personnes, ici Anna et Léo."},
             ]},
            {"id": "pa7-tf", "type": "true-false", "title": "Vrai ou Faux",
             "items": [
                {"id": "pa7tf1", "statement": "Je suis de... s'utilise pour parler de l'origine d'une personne.", "answer": True, "explanation": "Exactement — je suis de indique d'où vient quelqu'un."},
                {"id": "pa7tf2", "statement": "Je suis à... s'utilise pour parler de l'origine d'une personne.", "answer": False, "explanation": "Je suis à... indique le lieu où quelqu'un se trouve maintenant, pas son origine."},
                {"id": "pa7tf3", "statement": "Une personne peut venir d'un pays et se trouver dans un autre en même temps.", "answer": True, "explanation": "Oui — l'origine (de) et le lieu actuel (à/en/au) sont deux choses distinctes."},
                {"id": "pa7tf4", "statement": "Nous et ils se réfèrent toujours à la même personne.", "answer": False, "explanation": "Nous inclut celui qui parle ; ils se réfère à d'autres personnes, sans inclure celui qui parle."},
             ]},
            {"id": "pa7-match", "type": "matching", "title": "Associe le Pronom à la Situation",
             "items": [
                {"id": "pa7match1", "pairs": [
                    {"left": "je", "right": "la personne qui parle"},
                    {"left": "tu", "right": "la personne à qui tu parles"},
                    {"left": "nous", "right": "toi (qui parles) et d'autres personnes"},
                    {"left": "ils", "right": "plusieurs personnes dont tu parles"},
                ], "explanation": "Chaque pronom sujet identifie clairement qui réalise l'action dans la phrase."},
             ]},
            {"id": "pa7-fill", "type": "fill-blank", "title": "Complète avec Suis... De ou Suis... À",
             "items": [
                {"id": "pa7f1", "prompt": "Je ___ de Colombie.", "answers": [["suis"]], "options": ["suis", "es", "est"], "explanation": "Suis est la forme je du verbe être, utilisée ici avec de pour l'origine."},
                {"id": "pa7f2", "prompt": "Maintenant, je suis ___ travail.", "answers": [["au"]], "options": ["au", "de", "du"], "explanation": "Au (à + le) introduit le lieu actuel."},
                {"id": "pa7f3", "prompt": "Tu ___ d'où ?", "answers": [["es"]], "options": ["es", "êtes", "suis"], "explanation": "Es est la forme tu du verbe être, utilisée pour demander l'origine."},
                {"id": "pa7f4", "prompt": "Où ___-tu maintenant ?", "answers": [["es"]], "options": ["es", "suis", "est"], "explanation": "Es est la forme tu du verbe être, utilisée pour demander le lieu."},
             ]},
        ],
        "summary": [
            "Les pronoms sujets (je, tu, il/elle, nous, ils/elles) identifient qui réalise l'action, et sont toujours obligatoires en français.",
            "Je suis de... exprime l'origine d'une personne ; je suis à/en/au... exprime où elle se trouve en ce moment.",
            "Une personne peut venir d'un endroit et se trouver dans un autre au même moment — origine et lieu sont deux choses différentes.",
        ],
    },
    {
        "id": "pre-a1-lecture-et-ecoute-de-survie",
        "level": "Pre-A1", "unit": "1", "order": 8, "skill": "reading", "strand": "survie",
        "title": "Lecture et Écoute de Survie",
        "subtitle": "Lis et écoute de courts dialogues de situations de base : te présenter et demander quelque chose dans un magasin.",
        "objectives": [
            "Lire un court dialogue de présentation et comprendre l'information principale.",
            "Lire un court dialogue dans un magasin et comprendre ce que chaque personne demande.",
            "Reconnaître des mots et des phrases de survie dans un texte simple.",
        ],
        "content": {
            "intro": "Avec le vocabulaire et les phrases des leçons précédentes, tu peux déjà lire et comprendre de courts dialogues de la vie réelle — l'objectif final de tout débutant.",
            "explanation": "<p>Lire de vrais dialogues, même très simples, est différent d'apprendre des mots isolés : il faut reconnaître le vocabulaire que tu connais déjà dans une conversation complète, avec des questions, des réponses et un peu de contexte.</p><p>Cette leçon rassemble tout ce que tu as appris — salutations, noms, nombres, objets — dans deux situations très courantes pour un débutant : <strong>se présenter</strong> à quelqu'un et <strong>demander quelque chose dans un magasin</strong>.</p>",
            "rules": [
                {"heading": "a) Stratégie de lecture", "body": "<ul><li>Tu n'as pas besoin de comprendre chaque mot — cherche les mots que tu connais déjà.</li><li>Utilise le contexte (qui parle, où ils sont) pour deviner les mots nouveaux.</li><li>Lis le dialogue deux fois : la première pour avoir une idée générale, la deuxième pour les détails.</li></ul>"},
                {"heading": "b) Dialogue 1 — Se présenter", "body": "<p><strong>Sara :</strong> Bonjour, comment tu t'appelles ?<br><strong>Léo :</strong> Je m'appelle Léo. Et toi ?<br><strong>Sara :</strong> Je m'appelle Sara. Enchantée.<br><strong>Léo :</strong> Enchanté, Sara. Tu es d'où ?<br><strong>Sara :</strong> Je suis du Portugal. Et toi ?<br><strong>Léo :</strong> Moi, je suis de Belgique.</p>"},
                {"heading": "c) Dialogue 2 — Dans un magasin", "body": "<p><strong>Vendeuse :</strong> Bonjour, qu'est-ce qu'il vous faut ?<br><strong>Client :</strong> Bonjour. Je voudrais un cahier et un crayon, s'il vous plaît.<br><strong>Vendeuse :</strong> Voilà. Autre chose ?<br><strong>Client :</strong> Non, merci. C'est combien ?<br><strong>Vendeuse :</strong> C'est cinq euros.<br><strong>Client :</strong> Voilà. Merci, au revoir.</p>"},
            ],
            "examples": [
                "Bonjour, comment tu t'appelles ?",
                "Je m'appelle Léo. Enchanté.",
                "Tu es d'où ?",
                "Bonjour, qu'est-ce qu'il vous faut ?",
                "Je voudrais un cahier et un crayon, s'il vous plaît.",
                "C'est combien ? — C'est cinq euros.",
            ],
            "commonMistakes": [
                {"wrong": "Traduire chaque mot du dialogue avant de le comprendre.", "right": "Chercher d'abord les mots et phrases que tu connais déjà.", "why": "Chercher le sens général avec le vocabulaire connu est plus rapide et plus utile que traduire mot à mot."},
                {"wrong": "Répondre à C'est combien ? par C'est cinq euros, s'il vous plaît.", "right": "C'est combien ? — C'est cinq euros.", "why": "La réponse au prix n'a pas besoin de s'il vous plaît ; cette formule s'utilise pour demander quelque chose, pas pour donner une information."},
                {"wrong": "Ne rien comprendre et abandonner la lecture.", "right": "Lire le dialogue deux fois : d'abord pour l'idée générale, ensuite pour les détails.", "why": "Une deuxième lecture, avec l'idée générale déjà claire, aide à repérer plus de détails et de mots nouveaux."},
            ],
        },
        "exercises": [
            {"id": "pa8-tf", "type": "true-false", "title": "Compréhension : Vrai ou Faux ?",
             "items": [
                {"id": "pa8tf1", "statement": "Dans le Dialogue 1, Sara est du Portugal.", "answer": True, "explanation": "Sara dit : Je suis du Portugal."},
                {"id": "pa8tf2", "statement": "Dans le Dialogue 1, Léo est du Portugal.", "answer": False, "explanation": "Léo dit qu'il est de Belgique, pas du Portugal."},
                {"id": "pa8tf3", "statement": "Dans le Dialogue 2, le client veut un cahier et un crayon.", "answer": True, "explanation": "Le client dit : Je voudrais un cahier et un crayon, s'il vous plaît."},
                {"id": "pa8tf4", "statement": "Dans le Dialogue 2, le prix total est cinq euros.", "answer": True, "explanation": "La vendeuse dit : C'est cinq euros."},
                {"id": "pa8tf5", "statement": "Dans le Dialogue 2, le client demande aussi un livre.", "answer": False, "explanation": "Le client demande seulement un cahier et un crayon ; quand on lui demande autre chose ?, il dit non."},
             ]},
            {"id": "pa8-mc", "type": "multiple-choice", "title": "Questions sur les Dialogues",
             "items": [
                {"id": "pa8mc1", "prompt": "Qui parle en premier dans le Dialogue 1 ?", "options": ["Léo", "Sara", "La vendeuse"], "answerIndex": 1, "explanation": "Sara est celle qui salue en premier : Bonjour, comment tu t'appelles ?"},
                {"id": "pa8mc2", "prompt": "D'où est Léo ?", "options": ["Portugal", "Espagne", "Belgique"], "answerIndex": 2, "explanation": "Léo dit : Moi, je suis de Belgique."},
                {"id": "pa8mc3", "prompt": "Que demande le client dans le magasin ?", "options": ["Un cahier et un crayon", "Un livre et une gomme", "Un téléphone"], "answerIndex": 0, "explanation": "Le client dit : Je voudrais un cahier et un crayon, s'il vous plaît."},
                {"id": "pa8mc4", "prompt": "Combien coûte l'achat du client ?", "options": ["Cinq euros", "Dix euros", "Deux euros"], "answerIndex": 0, "explanation": "La vendeuse répond : C'est cinq euros."},
             ]},
            {"id": "pa8-order", "type": "ordering", "title": "Ordonne les Phrases du Dialogue",
             "instructions": "Place les lignes ou les mots dans le bon ordre.",
             "items": [
                {"id": "pa8order1", "prompt": "Remets les lignes du Dialogue 1 dans le bon ordre.", "words": ["Bonjour, comment tu t'appelles ?", "Je m'appelle Léo. Et toi ?", "Je m'appelle Sara. Enchantée.", "Enchanté, Sara. Tu es d'où ?", "Je suis du Portugal. Et toi ?", "Moi, je suis de Belgique."], "explanation": "Le dialogue suit un ordre logique : d'abord la salutation et les noms, ensuite la question sur l'origine et les réponses."},
                {"id": "pa8order2", "prompt": "Remets les lignes du Dialogue 2 dans le bon ordre.", "words": ["Bonjour, qu'est-ce qu'il vous faut ?", "Bonjour. Je voudrais un cahier et un crayon, s'il vous plaît.", "Voilà. Autre chose ?", "Non, merci. C'est combien ?", "C'est cinq euros.", "Voilà. Merci, au revoir."], "explanation": "La conversation dans le magasin suit l'ordre : salutation, demande, remise, question sur le prix, paiement et au revoir."},
                {"id": "pa8order3", "prompt": "Remets les mots dans le bon ordre pour former une phrase correcte.", "words": ["Je", "voudrais", "un", "cahier", "et", "un", "crayon"], "explanation": "L'ordre correct place je voudrais avant le premier objet, et, puis le second objet — voudrais commence toujours la demande."},
             ]},
        ],
        "summary": [
            "Lire un dialogue simple est plus facile si tu cherches d'abord les mots que tu connais déjà, plutôt que de tout traduire.",
            "Le Dialogue 1 (se présenter) combine salutations, noms et origine ; le Dialogue 2 (dans un magasin) combine salutations, objets et nombres.",
            "Avec le vocabulaire des leçons précédentes, tu peux déjà suivre de courtes conversations de la vie réelle en français.",
        ],
    },
]

# =======================================================================
# EXTRA_EXERCISES — blocs de pratique supplémentaires (lecture et
# remise en ordre) fusionnés dans chaque leçon par id, pour enrichir la
# collection d'exercices sans toucher au contenu pédagogique déjà écrit
# ci-dessus. Voir la boucle de fusion à la fin de ce fichier.
# =======================================================================
EXTRA_EXERCISES = {
    "pre-a1-alphabet-et-sons-du-francais": [
        {"id": "pa1x-reading", "type": "reading-comprehension", "title": "Lecture : Un Message de Léa",
         "passage": "<p>Salut ! Je m'appelle Léa. Mon prénom a un accent : L-É-A, avec un accent aigu sur le é. Mon nom de famille aussi a un accent : François, avec une cédille sous le c. Mon chat s'appelle Mimi et il vit avec moi en France. J'habite dans une rue avec beaucoup de sons nasaux : rue des Champs.</p>",
         "items": [
            {"id": "pa1xr1", "prompt": "Quel signe a le prénom de Léa ?", "options": ["un accent aigu", "une cédille", "un tréma"], "answerIndex": 0, "explanation": "Le texte dit : « Mon prénom a un accent : L-É-A, avec un accent aigu sur le é »."},
            {"id": "pa1xr2", "prompt": "Comment s'appelle le chat de Léa ?", "options": ["Léa", "Mimi", "François"], "answerIndex": 1, "explanation": "Le texte dit : « Mon chat s'appelle Mimi »."},
            {"id": "pa1xr3", "prompt": "Quel signe a le nom de famille de Léa ?", "options": ["un accent aigu", "une cédille", "aucun signe"], "answerIndex": 1, "explanation": "François a une cédille sous le c, mentionnée explicitement dans le texte."},
            {"id": "pa1xr4", "prompt": "Le mot \"Champs\" contient-il un son nasal ?", "options": ["Oui", "Non"], "answerIndex": 0, "explanation": "Champs contient le son nasal an, comme le mentionne le texte."},
         ]},
        {"id": "pa1x-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "pa1xo1", "prompt": "Remets les mots en ordre.", "words": ["La", "cédille", "adoucit", "le", "son", "du", "c"], "explanation": "Sujet (La cédille), verbe (adoucit), et le reste décrit ce qu'elle fait."},
            {"id": "pa1xo2", "prompt": "Remets les mots en ordre.", "words": ["Le", "chat", "s'appelle", "Mimi"], "explanation": "Structure typique pour nommer un animal : sujet + s'appelle + nom."},
         ]},
    ],
    "pre-a1-salutations-et-presentations": [
        {"id": "pa2x-reading", "type": "reading-comprehension", "title": "Lecture : À la Fête",
         "passage": "<p>— Bonsoir ! Je m'appelle Marc. Comment tu t'appelles ?<br>— Bonsoir, Marc. Je m'appelle Élise. Enchantée.<br>— Enchanté, Élise. Tu es d'où ?<br>— Je suis du Sénégal. Et toi ?<br>— Moi, je suis de Suisse. Bienvenue à la fête !</p>",
         "items": [
            {"id": "pa2xr1", "prompt": "Comment s'appelle la personne qui vient du Sénégal ?", "options": ["Marc", "Élise", "Aucun des deux"], "answerIndex": 1, "explanation": "Élise dit : « Je suis du Sénégal »."},
            {"id": "pa2xr2", "prompt": "D'où est Marc ?", "options": ["Du Sénégal", "De Suisse", "Il ne le dit pas"], "answerIndex": 1, "explanation": "Marc dit : « Moi, je suis de Suisse »."},
            {"id": "pa2xr3", "prompt": "À quel moment de la journée a lieu cette rencontre ?", "options": ["Le matin", "Le soir", "L'après-midi"], "answerIndex": 1, "explanation": "Le dialogue commence par « Bonsoir »."},
            {"id": "pa2xr4", "prompt": "Le dialogue se termine-t-il par une bienvenue ?", "options": ["Oui", "Non"], "answerIndex": 0, "explanation": "La dernière ligne est « Bienvenue à la fête ! »."},
         ]},
        {"id": "pa2x-order", "type": "ordering", "title": "Remets le Dialogue en Ordre",
         "items": [
            {"id": "pa2xo1", "prompt": "Remets les mots en ordre.", "words": ["Comment", "tu", "t'appelles"], "explanation": "La question commence par le mot interrogatif Comment."},
            {"id": "pa2xo2", "prompt": "Remets les mots en ordre.", "words": ["Enchanté", "de", "faire", "ta", "connaissance"], "explanation": "Expression fixe de politesse en rencontrant quelqu'un."},
         ]},
    ],
    "pre-a1-nombres-heure-et-date": [
        {"id": "pa3x-reading", "type": "reading-comprehension", "title": "Lecture : L'Emploi du Temps de Marion",
         "passage": "<p>Marion se lève à sept heures du matin. Elle prend son petit-déjeuner à sept heures et demie. Ses cours commencent à neuf heures et finissent à une heure de l'après-midi. Aujourd'hui, c'est mardi trois mars. L'anniversaire de Marion est le vingt mai.</p>",
         "items": [
            {"id": "pa3xr1", "prompt": "À quelle heure Marion se lève-t-elle ?", "options": ["À sept heures", "À sept heures et demie", "À neuf heures"], "answerIndex": 0, "explanation": "Le texte dit : « Marion se lève à sept heures du matin »."},
            {"id": "pa3xr2", "prompt": "À quelle heure finissent les cours de Marion ?", "options": ["À une heure de l'après-midi", "À neuf heures", "À sept heures et demie"], "answerIndex": 0, "explanation": "Le texte dit : « finissent à une heure de l'après-midi »."},
            {"id": "pa3xr3", "prompt": "Quel jour sommes-nous dans le texte ?", "options": ["Lundi", "Mardi", "Mercredi"], "answerIndex": 1, "explanation": "Le texte dit : « Aujourd'hui, c'est mardi trois mars »."},
            {"id": "pa3xr4", "prompt": "En quel mois est l'anniversaire de Marion ?", "options": ["Mars", "Avril", "Mai"], "answerIndex": 2, "explanation": "Le texte dit : « L'anniversaire de Marion est le vingt mai »."},
         ]},
        {"id": "pa3x-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "pa3xo1", "prompt": "Remets les mots en ordre.", "words": ["Il", "est", "neuf", "heures", "du", "matin"], "explanation": "Pour donner l'heure au pluriel on utilise il est + nombre + heures."},
            {"id": "pa3xo2", "prompt": "Remets les mots en ordre.", "words": ["Aujourd'hui", "c'est", "le", "trois", "mars"], "explanation": "Pour la date : aujourd'hui c'est le + nombre + mois."},
         ]},
    ],
    "pre-a1-vocabulaire-de-classe-et-etude": [
        {"id": "pa4x-reading", "type": "reading-comprehension", "title": "Lecture : Le Sac à Dos de Paul",
         "passage": "<p>Paul apporte son sac à dos en cours tous les jours. À l'intérieur, il a deux cahiers, trois crayons, un livre et une gomme. Sa professeure écrit au tableau et les élèves écoutent attentivement. Après le cours, Paul range tout dans son sac à dos à nouveau.</p>",
         "items": [
            {"id": "pa4xr1", "prompt": "Combien de cahiers Paul a-t-il dans son sac à dos ?", "options": ["Un", "Deux", "Trois"], "answerIndex": 1, "explanation": "Le texte dit : « il a deux cahiers »."},
            {"id": "pa4xr2", "prompt": "Où écrit la professeure ?", "options": ["Dans un cahier", "Au tableau", "Dans un livre"], "answerIndex": 1, "explanation": "Le texte dit : « Sa professeure écrit au tableau »."},
            {"id": "pa4xr3", "prompt": "Que font les élèves pendant le cours ?", "options": ["Ils dorment", "Ils écoutent attentivement", "Ils mangent"], "answerIndex": 1, "explanation": "Le texte dit : « les élèves écoutent attentivement »."},
            {"id": "pa4xr4", "prompt": "Paul apporte-t-il son sac à dos seulement certains jours ?", "options": ["Oui, seulement le lundi", "Non, tous les jours", "Ce n'est pas précisé"], "answerIndex": 1, "explanation": "Le texte dit que Paul apporte son sac à dos « tous les jours »."},
         ]},
        {"id": "pa4x-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "pa4xo1", "prompt": "Remets les mots en ordre.", "words": ["J'ai", "besoin", "d'un", "crayon", "et", "d'une", "gomme"], "explanation": "J'ai besoin de + objet + et + de + autre objet, avec les articles corrects selon le genre."},
            {"id": "pa4xo2", "prompt": "Remets les mots en ordre.", "words": ["La", "professeure", "écrit", "au", "tableau"], "explanation": "Sujet + verbe + complément de lieu."},
         ]},
    ],
    "pre-a1-personnes-et-objets-du-quotidien": [
        {"id": "pa5x-reading", "type": "reading-comprehension", "title": "Lecture : La Famille de Louis",
         "passage": "<p>Voici la famille de Louis. Sa mère s'appelle Rose et elle est grande. Son père s'appelle Thomas et il est sympathique. Louis a un petit frère qui s'appelle Yvan. Dans le salon de leur maison, il y a une table, deux chaises et une nouvelle télévision.</p>",
         "items": [
            {"id": "pa5xr1", "prompt": "Comment s'appelle la mère de Louis ?", "options": ["Rose", "Thomas", "Yvan"], "answerIndex": 0, "explanation": "Le texte dit : « Sa mère s'appelle Rose »."},
            {"id": "pa5xr2", "prompt": "Comment est le père de Louis, d'après le texte ?", "options": ["Grand", "Sympathique", "Petit"], "answerIndex": 1, "explanation": "Le texte dit : « Son père s'appelle Thomas et il est sympathique »."},
            {"id": "pa5xr3", "prompt": "Qu'y a-t-il dans le salon de la maison ?", "options": ["Un lit et une armoire", "Une table, deux chaises et une télévision", "Un chien et un chat"], "answerIndex": 1, "explanation": "Le texte décrit le salon avec ces trois objets."},
            {"id": "pa5xr4", "prompt": "Yvan est-il le grand frère de Louis ?", "options": ["Oui", "Non, c'est le petit frère"], "answerIndex": 1, "explanation": "Le texte dit : « un petit frère qui s'appelle Yvan »."},
         ]},
        {"id": "pa5x-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "pa5xo1", "prompt": "Remets les mots en ordre.", "words": ["Mon", "père", "est", "très", "sympathique"], "explanation": "Possessif + nom + verbe être + adverbe + adjectif."},
            {"id": "pa5xo2", "prompt": "Remets les mots en ordre.", "words": ["Il", "y", "a", "une", "table", "dans", "le", "salon"], "explanation": "Il y a (existence) + objet + complément de lieu."},
         ]},
    ],
    "pre-a1-verbes-de-base-etre-avoir-vouloir-aimer": [
        {"id": "pa6x-reading", "type": "reading-comprehension", "title": "Lecture : Sofia se Présente",
         "passage": "<p>Je m'appelle Sofia et je suis étudiante. J'ai vingt ans et j'ai deux sœurs. Je veux très bien apprendre le français. J'aime la musique et j'aime aussi le café le matin. Je n'aime pas me lever tôt le dimanche.</p>",
         "items": [
            {"id": "pa6xr1", "prompt": "Quel âge a Sofia ?", "options": ["Dix-huit ans", "Vingt ans", "Vingt-cinq ans"], "answerIndex": 1, "explanation": "Le texte dit : « J'ai vingt ans »."},
            {"id": "pa6xr2", "prompt": "Que veut apprendre Sofia ?", "options": ["La musique", "L'anglais", "Le français"], "answerIndex": 2, "explanation": "Le texte dit : « Je veux très bien apprendre le français »."},
            {"id": "pa6xr3", "prompt": "Sofia aime-t-elle se lever tôt le dimanche ?", "options": ["Oui, beaucoup", "Non, elle n'aime pas"], "answerIndex": 1, "explanation": "Le texte dit : « Je n'aime pas me lever tôt le dimanche »."},
            {"id": "pa6xr4", "prompt": "Combien de sœurs a Sofia ?", "options": ["Une", "Deux", "Trois"], "answerIndex": 1, "explanation": "Le texte dit : « j'ai deux sœurs »."},
         ]},
        {"id": "pa6x-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "pa6xo1", "prompt": "Remets les mots en ordre.", "words": ["J'aime", "beaucoup", "le", "café"], "explanation": "Sujet + aimer + adverbe + nom avec article."},
            {"id": "pa6xo2", "prompt": "Remets les mots en ordre.", "words": ["Je", "veux", "apprendre", "le", "français"], "explanation": "Je veux + infinitif + complément."},
         ]},
    ],
    "pre-a1-pronoms-sujets-et-etre-avoir": [
        {"id": "pa7x-reading", "type": "reading-comprehension", "title": "Lecture : Nous Sommes Étudiants",
         "passage": "<p>Nous sommes étudiants de français. Je suis du Brésil et elle est de France. Il est fatigué aujourd'hui parce qu'il travaille beaucoup. Ils sont à la bibliothèque maintenant, en train d'étudier pour l'examen de la semaine prochaine.</p>",
         "items": [
            {"id": "pa7xr1", "prompt": "D'où est la personne qui parle (je) ?", "options": ["De France", "Du Brésil", "Ce n'est pas précisé"], "answerIndex": 1, "explanation": "Le texte dit : « Je suis du Brésil »."},
            {"id": "pa7xr2", "prompt": "Pourquoi il est fatigué ?", "options": ["Parce qu'il étudie beaucoup", "Parce qu'il travaille beaucoup", "Parce qu'il ne dort pas"], "answerIndex": 1, "explanation": "Le texte dit : « Il est fatigué aujourd'hui parce qu'il travaille beaucoup »."},
            {"id": "pa7xr3", "prompt": "Où sont-ils maintenant ?", "options": ["À la maison", "À la bibliothèque", "Au travail"], "answerIndex": 1, "explanation": "Le texte dit : « Ils sont à la bibliothèque maintenant »."},
            {"id": "pa7xr4", "prompt": "Pour quoi étudient-ils à la bibliothèque ?", "options": ["Pour un examen", "Pour une fête", "Pour un voyage"], "answerIndex": 0, "explanation": "Le texte dit qu'ils étudient « pour l'examen de la semaine prochaine »."},
         ]},
        {"id": "pa7x-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "pa7xo1", "prompt": "Remets les mots en ordre.", "words": ["Nous", "sommes", "étudiants", "de", "français"], "explanation": "Pronom pluriel + être (nous) + nom + complément."},
            {"id": "pa7xo2", "prompt": "Remets les mots en ordre.", "words": ["Ils", "sont", "à", "la", "bibliothèque"], "explanation": "Pronom + être (ils) + complément de lieu."},
         ]},
    ],
    "pre-a1-lecture-et-ecoute-de-survie": [
        {"id": "pa8x-reading", "type": "reading-comprehension", "title": "Lecture : Demander de l'Aide dans la Rue",
         "passage": "<p>— Excusez-moi, où est la gare, s'il vous plaît ?<br>— C'est tout près, à deux rues d'ici, sur votre droite.<br>— Merci beaucoup. Une autre question : y a-t-il une banque près d'ici aussi ?<br>— Oui, il y en a une en face de la gare.<br>— Parfait, merci beaucoup pour votre aide.</p>",
         "items": [
            {"id": "pa8xr1", "prompt": "Que cherche la personne qui pose la question ?", "options": ["Une banque", "La gare", "Un restaurant"], "answerIndex": 1, "explanation": "La première question est : « où est la gare, s'il vous plaît ? »."},
            {"id": "pa8xr2", "prompt": "Dans quelle direction est la gare ?", "options": ["À gauche", "À droite", "Tout droit"], "answerIndex": 1, "explanation": "La réponse dit : « à deux rues d'ici, sur votre droite »."},
            {"id": "pa8xr3", "prompt": "Où est la banque ?", "options": ["En face de la gare", "À l'intérieur de la gare", "Loin de la gare"], "answerIndex": 0, "explanation": "La réponse dit : « il y en a une en face de la gare »."},
            {"id": "pa8xr4", "prompt": "La personne remercie-t-elle plus d'une fois ?", "options": ["Oui", "Non"], "answerIndex": 0, "explanation": "Elle dit « Merci beaucoup » puis « merci beaucoup pour votre aide »."},
         ]},
        {"id": "pa8x-order", "type": "ordering", "title": "Remets la Phrase en Ordre",
         "items": [
            {"id": "pa8xo1", "prompt": "Remets les mots en ordre.", "words": ["Excusez-moi", "où", "est", "la", "gare"], "explanation": "Formule de politesse + question de localisation."},
            {"id": "pa8xo2", "prompt": "Remets les mots en ordre.", "words": ["C'est", "à", "deux", "rues", "d'ici"], "explanation": "Être (localisation) + distance + référence."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES.get(_lesson["id"], []))

# =======================================================================
# EXTRA_EXERCISES_2 — deuxième série de blocs supplémentaires (correction
# et production écrite courte) fusionnée dans chaque leçon par id.
# =======================================================================
EXTRA_EXERCISES_2 = {
    "pre-a1-alphabet-et-sons-du-francais": [
        {"id": "pa1y-correction", "type": "correction", "title": "Corrige les Erreurs",
         "items": [
            {"id": "pa1yc1", "incorrect": "Le son du h dans \"hôtel\" est fort.", "answer": ["Le son du h dans \"hôtel\" n'existe pas. / Le h dans \"hôtel\" est muet."], "explanation": "Le h ne se prononce jamais en français, dans aucun mot."},
            {"id": "pa1yc2", "incorrect": "Le mot \"garçon\" se prononce avec un son de c dur.", "answer": ["Le mot \"garçon\" se prononce avec un son doux, grâce à la cédille."], "explanation": "La cédille adoucit toujours le son du c devant a, o, u."},
         ]},
        {"id": "pa1y-typing", "type": "typing", "title": "Pratique",
         "items": [
            {"id": "pa1yt1", "prompt": "Écris un mot français qui contient une voyelle nasale (an, en, in, on ou un).", "answer": [["bonjour", "maison", "enfant", "pain", "lundi", "français"]], "explanation": "N'importe quel mot avec une voyelle nasale est correct ; bonjour, maison et enfant sont des exemples très courants."},
         ]},
    ],
    "pre-a1-salutations-et-presentations": [
        {"id": "pa2y-correction", "type": "correction", "title": "Corrige les Erreurs",
         "items": [
            {"id": "pa2yc1", "incorrect": "Je appelle Marie.", "answer": ["Je m'appelle Marie."], "explanation": "S'appeler est un verbe pronominal ; il a toujours besoin du pronom me/te/se."},
            {"id": "pa2yc2", "incorrect": "Enchanté de te rencontrer toi.", "answer": ["Enchanté de te rencontrer."], "explanation": "Le pronom toi est inutile après te rencontrer, qui inclut déjà le pronom te."},
         ]},
        {"id": "pa2y-typing", "type": "typing", "title": "Pratique",
         "items": [
            {"id": "pa2yt1", "prompt": "Écris comment tu te présentes à quelqu'un de nouveau, en utilisant « je m'appelle ».", "explanation": "Gardé pour ta propre révision — compare ta phrase avec : « Bonjour, je m'appelle... Enchanté(e). »"},
         ]},
    ],
    "pre-a1-nombres-heure-et-date": [
        {"id": "pa3y-correction", "type": "correction", "title": "Corrige les Erreurs",
         "items": [
            {"id": "pa3yc1", "incorrect": "Il est trois heure de l'après-midi.", "answer": ["Il est trois heures de l'après-midi."], "explanation": "À partir de deux, heure prend toujours un s au pluriel."},
            {"id": "pa3yc2", "incorrect": "Aujourd'hui c'est en mardi.", "answer": ["Aujourd'hui c'est mardi."], "explanation": "Pour dire le jour de la semaine, on n'utilise pas la préposition en avec le verbe être."},
         ]},
        {"id": "pa3y-typing", "type": "typing", "title": "Pratique",
         "items": [
            {"id": "pa3yt1", "prompt": "Écris la date d'aujourd'hui en français (jour, mois).", "explanation": "Gardé pour ta propre révision — souviens-toi du format : aujourd'hui c'est le [nombre] [mois]."},
         ]},
    ],
    "pre-a1-vocabulaire-de-classe-et-etude": [
        {"id": "pa4y-correction", "type": "correction", "title": "Corrige les Erreurs",
         "items": [
            {"id": "pa4yc1", "incorrect": "J'ai besoin d'un gomme pour effacer.", "answer": ["J'ai besoin d'une gomme pour effacer."], "explanation": "Gomme est féminin : une gomme, pas un gomme."},
            {"id": "pa4yc2", "incorrect": "La professeure écrit dans le tableau.", "answer": ["La professeure écrit au tableau."], "explanation": "On écrit au tableau (à + le tableau), pas dans le tableau."},
         ]},
        {"id": "pa4y-typing", "type": "typing", "title": "Pratique",
         "items": [
            {"id": "pa4yt1", "prompt": "Écris trois objets que tu as dans ton sac à dos.", "explanation": "Gardé pour ta propre révision — utilise le vocabulaire de cette leçon : cahier, crayon, livre, gomme..."},
         ]},
    ],
    "pre-a1-personnes-et-objets-du-quotidien": [
        {"id": "pa5y-correction", "type": "correction", "title": "Corrige les Erreurs",
         "items": [
            {"id": "pa5yc1", "incorrect": "Ma mère est grand.", "answer": ["Ma mère est grande."], "explanation": "L'adjectif doit s'accorder en genre avec mère (féminin) : grande, pas grand."},
            {"id": "pa5yc2", "incorrect": "Dans le salon il y a un table.", "answer": ["Dans le salon il y a une table."], "explanation": "Table est féminin : une table, pas un table."},
         ]},
        {"id": "pa5y-typing", "type": "typing", "title": "Pratique",
         "items": [
            {"id": "pa5yt1", "prompt": "Décris une personne de ta famille en une phrase courte.", "explanation": "Gardé pour ta propre révision — pense à accorder l'adjectif avec le genre de la personne."},
         ]},
    ],
    "pre-a1-verbes-de-base-etre-avoir-vouloir-aimer": [
        {"id": "pa6y-correction", "type": "correction", "title": "Corrige les Erreurs",
         "items": [
            {"id": "pa6yc1", "incorrect": "Je a vingt ans.", "answer": ["J'ai vingt ans."], "explanation": "Je + avoir = j'ai, pas je a ; devant une voyelle, je s'élide toujours en j'."},
            {"id": "pa6yc2", "incorrect": "Je aime le café.", "answer": ["J'aime le café."], "explanation": "Je s'élide en j' devant une voyelle ; on ne dit jamais je aime."},
         ]},
        {"id": "pa6y-typing", "type": "typing", "title": "Pratique",
         "items": [
            {"id": "pa6yt1", "prompt": "Écris une phrase avec « j'aime » sur quelque chose que tu aimes.", "explanation": "Gardé pour ta propre révision — souviens-toi de la structure : j'aime + nom (la chose aimée n'est jamais le sujet)."},
         ]},
    ],
    "pre-a1-pronoms-sujets-et-etre-avoir": [
        {"id": "pa7y-correction", "type": "correction", "title": "Corrige les Erreurs",
         "items": [
            {"id": "pa7yc1", "incorrect": "Nous est étudiants.", "answer": ["Nous sommes étudiants."], "explanation": "Nous + être = sommes, pas est (qui est la forme de il/elle)."},
            {"id": "pa7yc2", "incorrect": "Elle a professeure.", "answer": ["Elle est professeure."], "explanation": "La profession décrit une identité, pas une possession : on utilise être, pas avoir."},
         ]},
        {"id": "pa7y-typing", "type": "typing", "title": "Pratique",
         "items": [
            {"id": "pa7yt1", "prompt": "Écris une phrase avec « je suis » sur comment tu te sens aujourd'hui.", "explanation": "Gardé pour ta propre révision — je suis + adjectif décrit un état ou une caractéristique."},
         ]},
    ],
    "pre-a1-lecture-et-ecoute-de-survie": [
        {"id": "pa8y-correction", "type": "correction", "title": "Corrige les Erreurs",
         "items": [
            {"id": "pa8yc1", "incorrect": "Où est-ce les toilettes ?", "answer": ["Où sont les toilettes ?"], "explanation": "Toilettes est toujours pluriel en français ; le verbe s'accorde donc au pluriel : sont, pas est."},
            {"id": "pa8yc2", "incorrect": "Merci beaucoup pour ton aide à toi.", "answer": ["Merci beaucoup pour ton aide."], "explanation": "À toi est inutile après ton, qui exprime déjà la possession."},
         ]},
        {"id": "pa8y-typing", "type": "typing", "title": "Pratique",
         "items": [
            {"id": "pa8yt1", "prompt": "Écris comment tu demanderais de l'aide pour trouver les toilettes dans la rue.", "explanation": "Gardé pour ta propre révision — compare avec : « Excusez-moi, où sont les toilettes ? »"},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES_2.get(_lesson["id"], []))

# =======================================================================
# EXTRA_EXERCISES_3 — troisième série (associer et vocabulaire) fusionnée
# dans chaque leçon par id.
# =======================================================================
EXTRA_EXERCISES_3 = {
    "pre-a1-alphabet-et-sons-du-francais": [
        {"id": "pa1z-match", "type": "matching", "title": "Associe",
         "items": [
            {"id": "pa1zm1", "prompt": "Associe la lettre ou le signe à un mot qui le contient.", "pairs": [{"left": "ç", "right": "garçon"}, {"left": "an/en", "right": "enfant"}, {"left": "h", "right": "hôtel"}, {"left": "on", "right": "bonjour"}], "explanation": "Chaque signe ou son spécial apparaît dans un mot très courant du français."},
         ]},
        {"id": "pa1z-vocab", "type": "vocabulary", "title": "Vocabulaire",
         "items": [
            {"id": "pa1zv1", "prompt": "Comment s'appelle le signe au-dessus de certaines voyelles ?", "options": ["Un accent", "Un point", "Une virgule"], "answerIndex": 0, "explanation": "Un accent change la prononciation ou distingue des mots identiques par ailleurs."},
            {"id": "pa1zv2", "prompt": "Combien de lettres a l'alphabet français ?", "options": ["24", "26", "28"], "answerIndex": 1, "explanation": "L'alphabet français a 26 lettres, comme l'alphabet anglais."},
            {"id": "pa1zv3", "prompt": "Quel phénomène fait réapparaître une consonne finale muette devant une voyelle ?", "options": ["La cédille", "La liaison", "Le tréma"], "answerIndex": 1, "explanation": "La liaison relie une consonne finale muette à la voyelle qui suit."},
         ]},
    ],
    "pre-a1-salutations-et-presentations": [
        {"id": "pa2z-match", "type": "matching", "title": "Associe",
         "items": [
            {"id": "pa2zm1", "prompt": "Associe la salutation au moment de la journée.", "pairs": [{"left": "bonjour", "right": "toute la journée"}, {"left": "bonsoir", "right": "le soir"}, {"left": "bonne nuit", "right": "au coucher"}, {"left": "salut", "right": "n'importe quel moment (informel)"}], "explanation": "Chaque salutation correspond à un moment précis, sauf bonjour qui fonctionne toute la journée."},
         ]},
        {"id": "pa2z-vocab", "type": "vocabulary", "title": "Vocabulaire",
         "items": [
            {"id": "pa2zv1", "prompt": "Que signifie « enchanté(e) » ?", "options": ["Au revoir", "En rencontrant quelqu'un", "Bonne nuit"], "answerIndex": 1, "explanation": "Enchanté(e) se dit en rencontrant quelqu'un pour la première fois."},
            {"id": "pa2zv2", "prompt": "Que réponds-tu à « merci » ?", "options": ["De rien", "Bonjour", "Au revoir"], "answerIndex": 0, "explanation": "De rien est la réponse habituelle à un remerciement."},
            {"id": "pa2zv3", "prompt": "Comment quelqu'un prend-il congé ?", "options": ["Bonjour", "Au revoir", "Merci"], "answerIndex": 1, "explanation": "Au revoir est la formule de départ la plus courante."},
         ]},
    ],
    "pre-a1-nombres-heure-et-date": [
        {"id": "pa3z-match", "type": "matching", "title": "Associe",
         "items": [
            {"id": "pa3zm1", "prompt": "Associe le nombre à sa forme écrite.", "pairs": [{"left": "5", "right": "cinq"}, {"left": "10", "right": "dix"}, {"left": "20", "right": "vingt"}, {"left": "100", "right": "cent"}], "explanation": "Chaque nombre correspond à sa forme écrite en français."},
         ]},
        {"id": "pa3z-vocab", "type": "vocabulary", "title": "Vocabulaire",
         "items": [
            {"id": "pa3zv1", "prompt": "Quel mot signifie « day » (unité de temps) ?", "options": ["semaine", "jour", "mois"], "answerIndex": 1, "explanation": "Jour est l'unité de temps de base de 24 heures."},
            {"id": "pa3zv2", "prompt": "Combien de jours a une semaine ?", "options": ["Cinq", "Sept", "Dix"], "answerIndex": 1, "explanation": "Une semaine a sept jours."},
            {"id": "pa3zv3", "prompt": "Quel mot signifie « month » ?", "options": ["Année", "Mois", "Heure"], "answerIndex": 1, "explanation": "Mois est l'unité de temps d'environ trente jours."},
         ]},
    ],
    "pre-a1-vocabulaire-de-classe-et-etude": [
        {"id": "pa4z-match", "type": "matching", "title": "Associe",
         "items": [
            {"id": "pa4zm1", "prompt": "Associe l'objet à son usage.", "pairs": [{"left": "crayon", "right": "écrire"}, {"left": "gomme", "right": "effacer"}, {"left": "livre", "right": "lire"}, {"left": "sac à dos", "right": "transporter des affaires"}], "explanation": "Chaque objet de classe a une fonction précise."},
         ]},
        {"id": "pa4z-vocab", "type": "vocabulary", "title": "Vocabulaire",
         "items": [
            {"id": "pa4zv1", "prompt": "Qu'utilises-tu pour écrire au tableau ?", "options": ["Un crayon", "Un marqueur/de la craie", "Une gomme"], "answerIndex": 1, "explanation": "On écrit au tableau avec un marqueur ou de la craie, pas avec un crayon."},
            {"id": "pa4zv2", "prompt": "Où transportes-tu tes livres pour aller en cours ?", "options": ["Dans le sac à dos", "Dans le cahier", "Dans la gomme"], "answerIndex": 0, "explanation": "Le sac à dos est l'endroit où l'on transporte le matériel scolaire."},
            {"id": "pa4zv3", "prompt": "Que signifie « effacer » ?", "options": ["Écrire", "Supprimer ce qui est écrit", "Lire"], "answerIndex": 1, "explanation": "Effacer signifie supprimer quelque chose d'écrit, normalement avec une gomme."},
         ]},
    ],
    "pre-a1-personnes-et-objets-du-quotidien": [
        {"id": "pa5z-match", "type": "matching", "title": "Associe",
         "items": [
            {"id": "pa5zm1", "prompt": "Associe le membre de la famille à sa description.", "pairs": [{"left": "mère", "right": "femme qui a donné naissance"}, {"left": "frère", "right": "mêmes parents"}, {"left": "grand-père", "right": "père du père ou de la mère"}, {"left": "fils", "right": "descendant"}], "explanation": "Chaque mot de famille décrit un lien de parenté différent."},
         ]},
        {"id": "pa5z-vocab", "type": "vocabulary", "title": "Vocabulaire",
         "items": [
            {"id": "pa5zv1", "prompt": "Quel mot signifie « chair » ?", "options": ["Table", "Chaise", "Lit"], "answerIndex": 1, "explanation": "Chaise est le meuble sur lequel on s'assoit."},
            {"id": "pa5zv2", "prompt": "Quel mot signifie « table » ?", "options": ["Chaise", "Table", "Fenêtre"], "answerIndex": 1, "explanation": "Table est le meuble de travail ou de repas."},
            {"id": "pa5zv3", "prompt": "Comment appelle-t-on le père de ton père ?", "options": ["Oncle", "Grand-père", "Cousin"], "answerIndex": 1, "explanation": "Le père de ton père est ton grand-père."},
         ]},
    ],
    "pre-a1-verbes-de-base-etre-avoir-vouloir-aimer": [
        {"id": "pa6z-match", "type": "matching", "title": "Associe",
         "items": [
            {"id": "pa6zm1", "prompt": "Associe le verbe à son sens.", "pairs": [{"left": "être", "right": "identité permanente"}, {"left": "avoir", "right": "posséder"}, {"left": "vouloir", "right": "désirer"}, {"left": "aimer", "right": "apprécier"}], "explanation": "Chaque verbe de base a un sens distinct et essentiel."},
         ]},
        {"id": "pa6z-vocab", "type": "vocabulary", "title": "Vocabulaire",
         "items": [
            {"id": "pa6zv1", "prompt": "Quel verbe utiliserais-tu pour dire ton âge ?", "options": ["Être", "Avoir", "Vouloir"], "answerIndex": 1, "explanation": "L'âge s'exprime avec avoir : j'ai vingt ans."},
            {"id": "pa6zv2", "prompt": "Quel verbe exprime un souhait ?", "options": ["Être", "Vouloir", "Aimer"], "answerIndex": 1, "explanation": "Vouloir exprime un souhait direct : je veux un café."},
            {"id": "pa6zv3", "prompt": "Quel verbe garde toujours la personne comme sujet pour exprimer une préférence ?", "options": ["Avoir", "Être", "Aimer"], "answerIndex": 2, "explanation": "Aimer garde la personne comme sujet : j'aime le café."},
         ]},
    ],
    "pre-a1-pronoms-sujets-et-etre-avoir": [
        {"id": "pa7z-match", "type": "matching", "title": "Associe",
         "items": [
            {"id": "pa7zm1", "prompt": "Associe le pronom à sa forme du verbe être.", "pairs": [{"left": "je", "right": "suis"}, {"left": "tu", "right": "es"}, {"left": "nous", "right": "sommes"}, {"left": "ils", "right": "sont"}], "explanation": "Chaque pronom a sa propre forme du verbe être au présent."},
         ]},
        {"id": "pa7z-vocab", "type": "vocabulary", "title": "Vocabulaire",
         "items": [
            {"id": "pa7zv1", "prompt": "Quel pronom utiliserais-tu pour parler de toi-même ?", "options": ["Tu", "Je", "Il"], "answerIndex": 1, "explanation": "Je est le pronom de la première personne du singulier."},
            {"id": "pa7zv2", "prompt": "Quel pronom correspond à un groupe qui inclut celui qui parle ?", "options": ["Nous", "Ils", "Vous"], "answerIndex": 0, "explanation": "Nous inclut celui qui parle au sein d'un groupe."},
            {"id": "pa7zv3", "prompt": "Quelle forme de avoir correspond à « je » ?", "options": ["as", "ai", "a"], "answerIndex": 1, "explanation": "Je + avoir = j'ai."},
         ]},
    ],
    "pre-a1-lecture-et-ecoute-de-survie": [
        {"id": "pa8z-match", "type": "matching", "title": "Associe",
         "items": [
            {"id": "pa8zm1", "prompt": "Associe la question à sa réponse logique.", "pairs": [{"left": "Où sont les toilettes ?", "right": "Au fond à droite."}, {"left": "C'est combien ?", "right": "C'est cinq euros."}, {"left": "Comment tu t'appelles ?", "right": "Je m'appelle Anna."}, {"left": "Tu parles anglais ?", "right": "Un peu."}], "explanation": "Chaque question de survie a une réponse naturelle typique."},
         ]},
        {"id": "pa8z-vocab", "type": "vocabulary", "title": "Vocabulaire",
         "items": [
            {"id": "pa8zv1", "prompt": "Que dis-tu pour demander de l'aide poliment ?", "options": ["Excusez-moi", "Au revoir", "Merci"], "answerIndex": 0, "explanation": "Excusez-moi est une façon polie d'attirer l'attention de quelqu'un."},
            {"id": "pa8zv2", "prompt": "Que signifie « perdu(e) » ?", "options": ["Qui ne sait pas où il/elle est", "Qui a faim", "Qui est content(e)"], "answerIndex": 0, "explanation": "Être perdu(e) signifie ne pas savoir où l'on est ni comment arriver quelque part."},
            {"id": "pa8zv3", "prompt": "Quel mot utiliserais-tu pour demander le prix ?", "options": ["Combien ?", "Quand ?", "Où ?"], "answerIndex": 0, "explanation": "C'est combien ? s'utilise pour demander le prix."},
         ]},
    ],
}

for _lesson in LESSONS:
    _lesson["exercises"].extend(EXTRA_EXERCISES_3.get(_lesson["id"], []))
