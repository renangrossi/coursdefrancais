"""
French morphology for the reading library.

The English rules are a handful of suffixes because English barely inflects.
French does, so this is a real (if deliberately rough) conjugator: a glossary
entry reads "se lever" and the passage reads "je me leve a cinq heures", and
nothing but a paradigm gets from one to the other.

The same economics as English apply -- over-generation is free, a missing form
is a bug -- so the paradigms below are complete for the tenses these texts
actually use (present, imperfect, simple future, conditional, passe simple,
subjunctive present, participles) and do not try to be a reference grammar.
"""
import re

# French dictionary form carries an article on a noun and a reflexive pronoun
# on a verb; the infinitive itself needs no marker, unlike English "to V".
# The apostrophe forms (l', s', d') must be listed with the apostrophe because
# elision leaves no space after them.
# Longest alternative first, and a MANDATORY space after a word-article:
# with "un" before "une" and the space optional, "une grande maison" lost its
# first article's last letter and came out as "e grande maison", which then
# matched nothing. The apostrophe forms are a separate branch precisely
# because elision leaves no space for \s+ to require.
ARTICLE_RE = re.compile(
    r"^(?:"
    r"de\s+la\s+|de\s+l'|"
    r"(?:le|la|les|un|une|des|du|de|au|aux|se)\s+|"
    r"(?:l'|s'|d')"
    r")", re.I)

# In a French noun phrase the modifier AGREES with the head rather than the
# head's number migrating to the last word, so the English
# "a fitting room -> fitting rooms" rule is wrong here. Agreement is handled
# by tail_forms() below instead.
PLURALISES_LAST_WORD = False

# Verbs whose stem or endings do not follow a regular class. Values are the
# full set of surface forms worth matching; the shared code adds nothing to
# them beyond what surface_forms() returns.
IRREGULAR = {
    "etre": ["suis", "es", "est", "sommes", "etes", "sont", "etais", "etait",
             "etions", "etiez", "etaient", "fus", "fut", "fumes", "futes",
             "furent", "serai", "seras", "sera", "serons", "serez", "seront",
             "serais", "serait", "serions", "seriez", "seraient", "ete",
             "etant", "soit", "soient", "sois", "soyons", "soyez"],
    "avoir": ["ai", "as", "a", "avons", "avez", "ont", "avais", "avait",
              "avions", "aviez", "avaient", "eus", "eut", "eumes", "eutes",
              "eurent", "aurai", "auras", "aura", "aurons", "aurez", "auront",
              "aurais", "aurait", "aurions", "auriez", "auraient", "eu", "eue",
              "eus", "eues", "ayant", "aie", "ait", "aient", "ayons", "ayez"],
    "aller": ["vais", "vas", "va", "allons", "allez", "vont", "allais",
              "allait", "allions", "alliez", "allaient", "irai", "iras",
              "ira", "irons", "irez", "iront", "irais", "irait", "irions",
              "iriez", "iraient", "alle", "allee", "alles", "allees",
              "allant", "aille", "aillent"],
    "faire": ["fais", "fait", "faisons", "faites", "font", "faisais",
              "faisait", "faisions", "faisiez", "faisaient", "fis", "fit",
              "fimes", "fites", "firent", "ferai", "feras", "fera", "ferons",
              "ferez", "feront", "ferais", "ferait", "ferions", "feriez",
              "feraient", "faite", "faits", "faites", "faisant", "fasse",
              "fassent"],
    "pouvoir": ["peux", "peut", "pouvons", "pouvez", "peuvent", "pouvais",
                "pouvait", "pouvions", "pouviez", "pouvaient", "pus", "put",
                "purent", "pourrai", "pourras", "pourra", "pourrons",
                "pourrez", "pourront", "pourrais", "pourrait", "pourrions",
                "pourriez", "pourraient", "pu", "pouvant", "puisse",
                "puissent"],
    "vouloir": ["veux", "veut", "voulons", "voulez", "veulent", "voulais",
                "voulait", "voulions", "vouliez", "voulaient", "voulus",
                "voulut", "voulurent", "voudrai", "voudras", "voudra",
                "voudrons", "voudrez", "voudront", "voudrais", "voudrait",
                "voudrions", "voudriez", "voudraient", "voulu", "voulue",
                "voulant", "veuille", "veuillent", "veuillez"],
    "devoir": ["dois", "doit", "devons", "devez", "doivent", "devais",
               "devait", "devions", "deviez", "devaient", "dus", "dut",
               "durent", "devrai", "devras", "devra", "devrons", "devrez",
               "devront", "devrais", "devrait", "devrions", "devriez",
               "devraient", "du", "due", "dus", "dues", "devant", "doive",
               "doivent"],
    "savoir": ["sais", "sait", "savons", "savez", "savent", "savais",
               "savait", "savions", "saviez", "savaient", "sus", "sut",
               "surent", "saurai", "sauras", "saura", "saurons", "saurez",
               "sauront", "saurais", "saurait", "saurions", "sauriez",
               "sauraient", "su", "sue", "sachant", "sache", "sachent",
               "sachez"],
    "venir": ["viens", "vient", "venons", "venez", "viennent", "venais",
              "venait", "venions", "veniez", "venaient", "vins", "vint",
              "vinrent", "viendrai", "viendras", "viendra", "viendrons",
              "viendrez", "viendront", "viendrais", "viendrait", "viendrions",
              "viendriez", "viendraient", "venu", "venue", "venus", "venues",
              "venant", "vienne", "viennent"],
    "tenir": ["tiens", "tient", "tenons", "tenez", "tiennent", "tenais",
              "tenait", "tenions", "teniez", "tenaient", "tins", "tint",
              "tinrent", "tiendrai", "tiendra", "tiendrons", "tiendront",
              "tiendrais", "tiendrait", "tenu", "tenue", "tenus", "tenues",
              "tenant", "tienne", "tiennent"],
    "prendre": ["prends", "prend", "prenons", "prenez", "prennent", "prenais",
                "prenait", "prenions", "preniez", "prenaient", "pris", "prit",
                "prirent", "prendrai", "prendras", "prendra", "prendrons",
                "prendrez", "prendront", "prendrais", "prendrait",
                "prendrions", "prendriez", "prendraient", "prise", "prises",
                "prenant", "prenne", "prennent"],
    "mettre": ["mets", "met", "mettons", "mettez", "mettent", "mettais",
               "mettait", "mettions", "mettiez", "mettaient", "mis", "mit",
               "mirent", "mettrai", "mettra", "mettrons", "mettront",
               "mettrais", "mettrait", "mise", "mises", "mettant", "mette",
               "mettent"],
    "dire": ["dis", "dit", "disons", "dites", "disent", "disais", "disait",
             "disions", "disiez", "disaient", "dis", "dit", "dirent",
             "dirai", "diras", "dira", "dirons", "direz", "diront", "dirais",
             "dirait", "dirions", "diriez", "diraient", "dite", "dites",
             "disant", "dise", "disent"],
    "voir": ["vois", "voit", "voyons", "voyez", "voient", "voyais", "voyait",
             "voyions", "voyiez", "voyaient", "vis", "vit", "virent",
             "verrai", "verras", "verra", "verrons", "verrez", "verront",
             "verrais", "verrait", "verrions", "verriez", "verraient", "vu",
             "vue", "vus", "vues", "voyant", "voie", "voient"],
    "croire": ["crois", "croit", "croyons", "croyez", "croient", "croyais",
               "croyait", "croyions", "croyiez", "croyaient", "crus", "crut",
               "crurent", "croirai", "croira", "croirons", "croiront",
               "croirais", "croirait", "cru", "crue", "crus", "crues",
               "croyant", "croie", "croient"],
    "boire": ["bois", "boit", "buvons", "buvez", "boivent", "buvais",
              "buvait", "buvions", "buviez", "buvaient", "bus", "but",
              "burent", "boirai", "boira", "boirons", "boiront", "boirais",
              "boirait", "bu", "bue", "bus", "bues", "buvant", "boive",
              "boivent"],
    "ecrire": ["ecris", "ecrit", "ecrivons", "ecrivez", "ecrivent",
               "ecrivais", "ecrivait", "ecrivions", "ecriviez", "ecrivaient",
               "ecrivis", "ecrivit", "ecrivirent", "ecrirai", "ecrira",
               "ecrirons", "ecriront", "ecrirais", "ecrirait", "ecrite",
               "ecrites", "ecrivant", "ecrive", "ecrivent"],
    "lire": ["lis", "lit", "lisons", "lisez", "lisent", "lisais", "lisait",
             "lisions", "lisiez", "lisaient", "lus", "lut", "lurent",
             "lirai", "lira", "lirons", "liront", "lirais", "lirait", "lu",
             "lue", "lus", "lues", "lisant", "lise", "lisent"],
    "vivre": ["vis", "vit", "vivons", "vivez", "vivent", "vivais", "vivait",
              "vivions", "viviez", "vivaient", "vecus", "vecut", "vecurent",
              "vivrai", "vivra", "vivrons", "vivront", "vivrais", "vivrait",
              "vecu", "vecue", "vivant", "vive", "vivent"],
    "suivre": ["suis", "suit", "suivons", "suivez", "suivent", "suivais",
               "suivait", "suivions", "suiviez", "suivaient", "suivis",
               "suivit", "suivirent", "suivrai", "suivra", "suivrons",
               "suivront", "suivrais", "suivrait", "suivi", "suivie",
               "suivis", "suivies", "suivant", "suive", "suivent"],
    "connaitre": ["connais", "connait", "connaissons", "connaissez",
                  "connaissent", "connaissais", "connaissait",
                  "connaissions", "connaissiez", "connaissaient", "connus",
                  "connut", "connurent", "connaitrai", "connaitra",
                  "connaitrons", "connaitront", "connaitrais", "connaitrait",
                  "connu", "connue", "connus", "connues", "connaissant",
                  "connaisse", "connaissent"],
    "naitre": ["nais", "nait", "naissons", "naissez", "naissent", "naissais",
               "naissait", "naquis", "naquit", "naquirent", "naitrai",
               "naitra", "ne", "nee", "nes", "nees", "naissant", "naisse"],
    "mourir": ["meurs", "meurt", "mourons", "mourez", "meurent", "mourais",
               "mourait", "mourions", "mouriez", "mouraient", "mourus",
               "mourut", "mourupent", "moururent", "mourrai", "mourra",
               "mourrons", "mourront", "mourrais", "mourrait", "mort",
               "morte", "morts", "mortes", "mourant", "meure", "meurent"],
    "ouvrir": ["ouvre", "ouvres", "ouvrons", "ouvrez", "ouvrent", "ouvrais",
               "ouvrait", "ouvrions", "ouvriez", "ouvraient", "ouvris",
               "ouvrit", "ouvrirent", "ouvrirai", "ouvrira", "ouvrirons",
               "ouvriront", "ouvrirais", "ouvrirait", "ouvert", "ouverte",
               "ouverts", "ouvertes", "ouvrant", "ouvre", "ouvrent"],
    "courir": ["cours", "court", "courons", "courez", "courent", "courais",
               "courait", "courions", "couriez", "couraient", "courus",
               "courut", "courureent", "coururent", "courrai", "courra",
               "courrons", "courront", "courrais", "courrait", "couru",
               "courue", "courant", "coure", "courent"],
    "recevoir": ["recois", "recoit", "recevons", "recevez", "recoivent",
                 "recevais", "recevait", "recevions", "receviez",
                 "recevaient", "recus", "recut", "recurent", "recevrai",
                 "recevra", "recevrons", "recevront", "recevrais",
                 "recevrait", "recu", "recue", "recus", "recues",
                 "recevant", "recoive", "recoivent"],
    "falloir": ["faut", "fallait", "fallut", "faudra", "faudrait", "fallu"],
    "valoir": ["vaux", "vaut", "valons", "valez", "valent", "valais",
               "valait", "valut", "vaudra", "vaudrait", "valu", "valant",
               "vaille"],
    "asseoir": ["assieds", "assied", "asseyons", "asseyez", "asseyent",
                  "asseyais", "asseyait", "assis", "assit", "assirent",
                  "assierai", "assiera", "assis", "assise", "assises",
                  "asseyant"],
    # Common irregular nouns and adjectives.
    "oeil": ["yeux"], "ciel": ["cieux"], "aieul": ["aieux"],
    "monsieur": ["messieurs"], "madame": ["mesdames"],
    "mademoiselle": ["mesdemoiselles"],
    "bon": ["bonne", "bons", "bonnes", "meilleur", "meilleure", "meilleurs",
            "meilleures"],
    "mauvais": ["mauvaise", "mauvaises", "pire", "pires"],
    "vieux": ["vieil", "vieille", "vieilles"],
    "beau": ["bel", "belle", "beaux", "belles"],
    "nouveau": ["nouvel", "nouvelle", "nouveaux", "nouvelles"],
    "tout": ["toute", "tous", "toutes"],
    "celui": ["celle", "ceux", "celles"],
}

# The three regular classes, by infinitive ending. Endings are appended to the
# stem (the infinitive minus its ending).
_PARADIGMS = {
    "er": ["e", "es", "e", "ons", "ez", "ent",            # present
           "ais", "ait", "ions", "iez", "aient",          # imperfect
           "ai", "as", "a", "ames", "ates", "erent",      # passe simple
           "erai", "eras", "era", "erons", "erez", "eront",       # future
           "erais", "erait", "erions", "eriez", "eraient",        # conditional
           "e", "ee", "es", "ees",                        # past participle
           "ant"],                                        # present participle
    # finir-type: the -iss- infix is what distinguishes it from partir-type.
    "ir_iss": ["is", "is", "it", "issons", "issez", "issent",
               "issais", "issait", "issions", "issiez", "issaient",
               "is", "it", "imes", "ites", "irent",
               "irai", "iras", "ira", "irons", "irez", "iront",
               "irais", "irait", "irions", "iriez", "iraient",
               "i", "ie", "is", "ies",
               "issant"],
    # partir/dormir/sortir-type: no infix, and the stem loses its final
    # consonant in the singular (pars/part, dors/dort) -- handled below.
    "ir_bare": ["is", "is", "it", "ons", "ez", "ent",
                "ais", "ait", "ions", "iez", "aient",
                "is", "it", "imes", "ites", "irent",
                "irai", "iras", "ira", "irons", "irez", "iront",
                "irais", "irait", "irions", "iriez", "iraient",
                "i", "ie", "is", "ies",
                "ant"],
    "re": ["s", "s", "", "ons", "ez", "ent",
           "ais", "ait", "ions", "iez", "aient",
           "is", "it", "imes", "ites", "irent",
           "rai", "ras", "ra", "rons", "rez", "ront",
           "rais", "rait", "rions", "riez", "raient",
           "u", "ue", "us", "ues",
           "ant"],
}

# -ir verbs that take the bare paradigm rather than the -iss- one. The list is
# short and closed enough to enumerate; anything else -ir is assumed -iss-.
_BARE_IR = {
    "partir", "sortir", "dormir", "servir", "sentir", "mentir", "repartir",
    "ressortir", "endormir", "desservir", "consentir", "ressentir", "bouillir",
    "repentir", "pressentir",
}


_FOLD = str.maketrans({
    "à": "a", "â": "a", "ä": "a", "ç": "c", "é": "e", "è": "e", "ê": "e",
    "ë": "e", "î": "i", "ï": "i", "ô": "o", "ö": "o", "ù": "u", "û": "u",
    "ü": "u", "ÿ": "y", "œ": "oe", "æ": "ae",
})


def _fold(s):
    """Accents off, for looking a headword up in the tables below.

    The paradigms and the irregular table are written without accents because
    a conjugation table is unreadable with them. That is only safe if every
    lookup folds too: "etre" is in IRREGULAR and "être" is not, and without
    this the commonest verb in the language was being run through the regular
    -re paradigm and yielding "êtaient".
    """
    return s.lower().translate(_FOLD)


def _verb_forms(inf):
    """Every conjugated form of a regular infinitive, or () if it is not one."""
    low = _fold(inf)
    out = set()
    if low.endswith("er") and len(low) > 2:
        stem, key = low[:-2], "er"
        # -ger/-cer keep their soft consonant before a back vowel: nous
        # mangeons, nous commencons. Generating both spellings is harmless.
        if stem.endswith("g"):
            out |= {stem + "eons", stem + "eais", stem + "eait", stem + "eant"}
        if stem.endswith("c"):
            out |= {stem[:-1] + "cons", stem[:-1] + "cais", stem[:-1] + "cait"}
        # appeler -> appelle, jeter -> jette; acheter -> achete.
        if stem.endswith("el") or stem.endswith("et"):
            out |= {stem + stem[-1] + "e", stem + stem[-1] + "es",
                    stem + stem[-1] + "ent"}
    elif low.endswith("ir") and len(low) > 2:
        stem = low[:-2]
        key = "ir_bare" if low in _BARE_IR else "ir_iss"
        if key == "ir_bare":
            # pars/part from part-, dors/dort from dorm-: the singular drops
            # the stem's final consonant.
            short = stem[:-1] if stem and stem[-1].isalpha() else stem
            out |= {short + "s", short + "t"}
    elif low.endswith("re") and len(low) > 2:
        stem, key = low[:-2], "re"
    else:
        return out
    for end in _PARADIGMS[key]:
        out.add(stem + end)
    out.add(low)
    return out


def _noun_adj_forms(w):
    """Gender and number of a noun or adjective."""
    low = _fold(w)
    out = {low}
    # Plural.
    if low.endswith(("s", "x", "z")):
        out.add(low)                       # already plural or invariable
    elif low.endswith(("eau", "eu")):
        out.add(low + "x")                 # bateau -> bateaux, jeu -> jeux
    elif low.endswith("al"):
        out.add(low[:-2] + "aux")          # journal -> journaux
    elif low.endswith("ail"):
        out.add(low[:-3] + "aux")          # travail -> travaux
    else:
        out.add(low + "s")
    # Feminine.
    if low.endswith("e"):
        out.add(low)
    elif low.endswith("eur"):
        out |= {low[:-3] + "euse", low[:-3] + "rice", low + "e"}
    elif low.endswith("eux"):
        out.add(low[:-1] + "se")           # heureux -> heureuse
    elif low.endswith("f"):
        out.add(low[:-1] + "ve")           # actif -> active
    elif low.endswith("er"):
        out.add(low[:-2] + "ere")          # premier -> premiere
    elif low.endswith(("en", "on")):
        out.add(low + low[-1] + "e")       # bon -> bonne, ancien -> ancienne
    elif low.endswith("el"):
        out.add(low + "le")                # nouvel -> nouvelle
    else:
        out.add(low + "e")
    # Feminine plural, from each feminine form generated above.
    for f in list(out):
        if f.endswith("e"):
            out.add(f + "s")
    return out


def surface_forms(head):
    """Every surface form the first word of a headword might appear as.

    A French headword is either a verb in the infinitive or a noun/adjective,
    and there is no reliable way to tell which from the string alone --
    "ferme" is both. So both paradigms run and the union is returned, which
    is exactly the over-generation the English rules rely on too.
    """
    low = _fold(head)
    out = {head, head.lower(), low}
    out |= _verb_forms(low)
    out |= _noun_adj_forms(low)
    out |= set(IRREGULAR.get(low, []))
    # Elision: a headword beginning with a vowel appears as l'ami, d'ami,
    # and a reflexive as s'habille. The shared matcher strips the article, so
    # what is needed here is the bare form -- already present. Nothing to add.
    return {f for f in out if f}


def tail_forms(word):
    """Agreement forms for a word AFTER the head of a noun phrase.

    French modifiers agree with their head ("une grande maison" ->
    "de grandes maisons"), which the English rules have no equivalent of.
    """
    return _noun_adj_forms(word)


# Accent folding, for MATCHING ONLY.
#
# The paradigms above are written without accents ("etre", "parlames") because
# a conjugation table is unreadable with them and easy to get wrong. Real
# French text of course carries them, so the shared matcher expands each base
# letter into a character class when it builds a pattern. The passage itself is
# never altered: this changes what a pattern MATCHES, not what a reader sees,
# and it is deliberately not the same thing as the accent-stripping that
# grading must never do -- an exercise answer still has to be accented
# correctly.
CHAR_CLASSES = {
    "a": "aàâä", "c": "cç", "e": "eéèêë", "i": "iîï",
    "o": "oôö", "u": "uùûü", "y": "yÿ",
}
