"""
Calling a site's own scripts/site_chrome.py, whatever shape it is.

The family's sites forked from each other at different times, so their chrome
helpers have drifted apart:

    curso-ingles       head(rel, title, description, page_path=, og_type=)
                       header(rel, level, breadcrumb, body_class="")
    coursdefrancais    head(rel, title, description, extra_css=None)
                       header(rel, level, breadcrumb_html=None, active_top=None)

Rather than edit seven sites' chrome to one signature -- which would mean
touching files the reading library has no business owning -- this adapter
inspects what the site actually accepts and passes only that. A site that
grows a `body_class` or `page_path` parameter later starts receiving it with
no change here.

body_class is the one argument the reading library cannot do without: the
print stylesheet is scoped to body.reading-page. Where the site's header()
cannot take it, it is patched into the returned markup instead.
"""
import inspect
import re


class Chrome:
    def __init__(self, module):
        self.m = module
        self._head_params = self._params(module.head)
        self._header_params = self._params(module.header)
        self._footer_params = self._params(module.footer)

    @staticmethod
    def _params(fn):
        try:
            return set(inspect.signature(fn).parameters)
        except (TypeError, ValueError):       # a C function or similar
            return set()

    def head(self, rel, title, description, page_path=None, extra_css=None):
        kw = {}
        # Only curso-ingles builds social meta, and only it knows the page's
        # own path; elsewhere the argument does not exist.
        if "page_path" in self._head_params and page_path:
            kw["page_path"] = page_path
        if "og_type" in self._head_params:
            kw["og_type"] = "article"
        takes_css = "extra_css" in self._head_params
        if takes_css and extra_css:
            kw["extra_css"] = list(extra_css)
        out = self.m.head(rel, title, description, **kw)
        if extra_css and not takes_css:
            # The site's head() has no extra_css parameter, so the reading
            # stylesheet is spliced in before </head> instead. Editing the
            # site's chrome to grow a parameter it has no other use for would
            # be the bigger change, and a <link> in <body> is not valid HTML
            # even though browsers tolerate it.
            out = _add_stylesheets(out, rel, extra_css)
        return out

    def header(self, rel, level, breadcrumb, body_class="reading-page"):
        kw = {}
        if "body_class" in self._header_params:
            kw["body_class"] = body_class
        out = self.m.header(rel, level, breadcrumb, **kw)
        if "body_class" not in self._header_params and body_class:
            out = _add_body_class(out, body_class)
        return out

    def footer(self, rel):
        return self.m.footer(rel)

    def extra_css_supported(self):
        return "extra_css" in self._head_params


BODY_RE = re.compile(r"<body(?![\w-])([^>]*)>", re.I)


def _add_body_class(markup, cls):
    """Add a class to the <body> tag of generated chrome.

    Textual, because the alternative is making every site's header() grow a
    parameter it has no other use for. It is a narrow edit -- one tag, one
    attribute -- and it fails loudly rather than silently: if the chrome ever
    stops emitting a <body> here, the print stylesheet would quietly stop
    applying, so this raises instead.
    """
    m = BODY_RE.search(markup)
    if not m:
        raise RuntimeError(
            "site_chrome.header() emitted no <body> tag, so body_class could "
            f"not be set to {cls!r}. The reading print stylesheet is scoped to "
            "body.reading-page and would silently stop applying.")
    attrs = m.group(1)
    cm = re.search(r'class\s*=\s*"([^"]*)"', attrs, re.I)
    if cm:
        if cls in cm.group(1).split():
            return markup
        new_attrs = attrs[:cm.start(1)] + (cm.group(1) + " " + cls).strip() + attrs[cm.end(1):]
    else:
        new_attrs = attrs.rstrip() + f' class="{cls}"'
    return markup[:m.start()] + f"<body{new_attrs}>" + markup[m.end():]


HEAD_CLOSE_RE = re.compile(r"</head\s*>", re.I)


def _add_stylesheets(markup, rel, names):
    """Link extra stylesheets into generated <head> markup.

    `names` are bare stylesheet names without the .css extension, matching the
    convention each site's head(extra_css=...) already uses.
    """
    links = "".join(
        f'<link rel="stylesheet" href="{rel}assets/css/{n}.css">' for n in names)
    m = HEAD_CLOSE_RE.search(markup)
    if not m:
        raise RuntimeError(
            "site_chrome.head() emitted no </head>, so the reading stylesheets "
            f"{list(names)} could not be linked. The page would render with no "
            "reading styles at all, so this fails rather than shipping it.")
    return markup[:m.start()] + links + markup[m.start():]
