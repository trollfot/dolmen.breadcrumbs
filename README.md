Breadcrumbs
==========

Breadcrumbs are a way to display one's location in a hierarchical  object model.

Github uses them at the top of each page, to let you know where you are. 

Many ZODB applications also use them.

This package displays them.

Dolmen.Breadcrumbs assumes that there is a root object which
implements IPublicationRoot.

In

dolmen.breadcrumbs/src/dolmen/breadcrumbs/crumbs.py

There are two methods.

1.resolve_name() returns the __name__ of the object twice,or it throws an exception.
Of course for IPulicationRoot, if there is no __name__, it can return None.
You could also write a resolver which returns (__name__, title)

2. breadcrumbs(item, request, resolver=resolve_name) is an iterator which
returns the data structures required to build breadcrumbs.  It gets the
items parents, up to IPublicatinRoot, reverses them, and yeilds a dictinary with
the name and url of the crumb. 

In

dolmen.breadcrumbs/src/dolmen/breadcrumbs/renderer.py

You will find two different methods. breadcrumbsrenderer() calls
render_breadcrums which calls the
[template](./src/dolmen/breadcrumbs/templates/breadcrumbs.pt)

So I think what we want to do is something like

```
from dolmen.breadcrumbs. import breadcrumbs
from dolmen.breadcrumbs. import BreadcrumbsRenderer
class MyPage(Page):
    define breadcrumbs():
       crumbs=BreadCrynbsRender*(
       crumbs.breadcrums=breadcrums
       return crumbs.render()
```

Then in the Page Template add in
   ${view.breadcrumbs()}

And you should have breadcrums on your page. 

By tomorrow I should have tested this. 

Christopher Lozinski Writes about these breadcrumbs:"  They are
beautifully designed, but not that heavily used, not that many features.
In contast the breadcrums I wrote and have been using have a lot
more features, but are less well designed, so I am migrating to dolmen.breadcrumbs
and adding features. It should be quite easy to do."
