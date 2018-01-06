Breadcrumbs
==========

Breadcrumbs are a way to display one's location in a hierarchical  object model. Click on the appropriate crumb, and the browser will take you to
the page for that parent object. 

Github uses them at the top of each page, to let you know where you are.

This package displays bredcrumbs.

Many ZODB applications also use them. WHile github just has a
unix directory behind each breadcrumb, with the ZODB you can
have different views of the parent objects, typically the '/index' and the
'/manage' view.  So these breadcrumbs are a bit more sophisticated than
the typical github breadcrumbs.

The simplest way to use breadcrumbs is as follows:

```
from dolmen.breadcrumbs import defaultBreadCrumbs
print (defaultBreadCrumbs(item,request))
```

In practice you will want to use breadcrumbs in your
web pages, and so you add them to your Page subclasses

```
from dolmen.breadcrumbs import basicBreadCrumbs
class MyPage(Page):
    define breadcrumbs():
        return defaultBreadCrumbs(self.context,self.request)
```

Then in the Page Template just call them.
   ${view.breadcrumbs()}

And you should have breadcrumbs on your page. 

Of course if you want to customize it, you can.  Let us
explore how they work. 

Dolmen.Breadcrumbs assumes that there is a root object which
implements IPublicationRoot.  It gets the parents of an object,
using dolmen.location, and then genates a list of dictionaires with the
information for each item.  Finally it converst that list into html.

In [dolmen.breadcrumbs/src/dolmen/breadcrumbs/crumbs.py](./src/dolmen/breadcrumbs/crumbs.py])
There are two methods.

1.resolve_name() returns a (name, title) pair.  Some objects just have a name,
so they get back (name, name).  The root object IPublicationRoot,
may not even havea  name, so
it returns (none, none) or (none, title). 

2. breadcrumbs(item, request, resolver=resolve_name) is an iterator which
returns the data structures required to build breadcrumbs.  It gets the
items parents, up to IPublicatinRoot, reverses them, and yeilds a dictinary
with the name and url of the crumb. 

In [dolmen.breadcrumbs/src/dolmen/breadcrumbs/renderer.py](./src/dolmen/breadcrumbs/renderer.py) You will find two different methods. breadcrumbsrenderer() calls
render_breadcrums which calls the
[template](./src/dolmen/breadcrumbs/templates/breadcrumbs.pt)


Christopher Lozinski writes about these breadcrumbs: "They are
beautifully designed, whatever changes I needed to make just took 
a few lines of code. "


