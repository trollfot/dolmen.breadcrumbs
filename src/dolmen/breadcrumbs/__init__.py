# -*- coding: utf-8 -*-

from dolmen.breadcrumbs.crumbs import breadcrumbs
from dolmen.breadcrumbs.renderer import BreadcrumbsRenderer

def BasicBreadCrumbs(item,request):
       crumbs=BreadCrynbsRender()
       crumbs.breadcrums=breadcrumbs(item,request)
       return crumbs.render()

   
