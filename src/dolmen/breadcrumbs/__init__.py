# -*- coding: utf-8 -*-

from dolmen.breadcrumbs.crumbs import breadcrumbs
from dolmen.breadcrumbs.renderer import BreadcrumbsRenderer

def defaultBreadcrumbs(item,request):
       #import pdb; pdb.set_trace()
       crumbs=BreadcrumbsRenderer(item,request,viewName='',separator='/')
       crumbs.update()
       return crumbs.render()


