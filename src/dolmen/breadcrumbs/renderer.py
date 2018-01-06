# -*- coding: utf-8 -*-

from os import path
from cromlech.browser import IRenderable
from cromlech.i18n import ILanguage
from dolmen.breadcrumbs import breadcrumbs
from dolmen.template import TALTemplate
from zope.interface import implementer


TEMPLATES_DIR = path.join(path.dirname(__file__), 'templates')
template = TALTemplate(path.join(TEMPLATES_DIR, 'breadcrumbs.pt'))


def render_breadcrumbs(renderer, crumbs, viewName='', separator="&rarr;"):
    namespace = dict(
        breadcrumbs=crumbs,
        viewName=viewName,
        target_language='en',
        separator=separator)
    return template.render(renderer, **namespace)
    #    target_language=ILanguage(renderer.request, None),
        #WHAT SHOULD I HAVE DONE HERE?


@implementer(IRenderable)
class BreadcrumbsRenderer(object):

    resolver = None
    
    def __init__(self, context, request, viewName=''):
        self.context = context
        self.request = request
        self.viewName = viewName

    def update(self):
        self.breadcrumbs = list(
            breadcrumbs(self.context, self.request, self.viewName, self.resolver))

    def render(self):
        return render_breadcrumbs(self, self.breadcrumbs)
