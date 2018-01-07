# -*- coding: utf-8 -*-

from cromlech.browser import IPublicationRoot
from dolmen.location import lineage_chain
from dolmen.location import resolve_url
from dolmen.location import get_absolute_url


try:
        from urllib import quote  # Python 2.X
except ImportError:
        from urllib.parse import quote  # Python 3+

_safe = '@+'  # Characters that we don't want to have quoted


def resolve_name(item):
    """Choose a display name for the current context.
    This method has been splitted out for convenient overriding.
    """
    name = getattr(item, '__name__', None)
    title= getattr(item, 'title', None)

    if name is None and not IPublicationRoot.providedBy(item):
        raise KeyError('Object name (%r) could not be resolved.' % item)

    if (title != None):
        return name, title
    return name, name


def breadcrumbs(item, request, viewName='', resolver=resolve_name):
    #IF YOU WANT A SPECFIC VIEWNAME, THEN PREPEND A SLASH
    if viewName != '':
       viewName ='/' + viewName
    if resolver is None:
        resolver = resolve_name
    parents = lineage_chain(item)
    if parents:
        parents.reverse()
        root = parents.pop(0)
        #base_url = get_absolute_url(root, request)
        base_url = resolve_url(root, request)        
        name, title = resolver(root)
        yield {'name': title, 'url': base_url + viewName}

        for ancestor in parents:
            name, title = resolver(ancestor)
            base_url += '/' + quote(name.encode('utf-8'), _safe)
            yield {'name': title, 'url': base_url+ viewName}
