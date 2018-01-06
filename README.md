Breadcrumbs
==========

Breadcrumbs are a way to display one's location in a hierarchical  object model.

Github uses them at the top of each page, to let you know where you are. 

Many ZODB applications also use them.

This package displays them.

The simplest way to use breadcrumbs is as follows:

```
from dolmen.breadcrumbs import basicBreadCrumbs
print (basicBreadCrumbs(item,request))
```

In practice you will want to use breadcrumbs in your
web pages, and so you add them to your Page subclasses

```
from dolmen.breadcrumbs import basicBreadCrumbs
class MyPage(Page):
    define breadcrumbs():
        return basicBreadCrumbs(self.context,self.request)
```

Then in the Page Template just call them.
   ${view.breadcrumbs()}

And you should have breadcrumbs on your page. 

Of course if you want to customize it, you can.  Let us
explore how they work. 

Dolmen.Breadcrumbs assumes that there is a root object which
implements IPublicationRoot.  It gets the paretns of an object (kin),
using dolmen.location, and then genates a list of dictionaires with the
information for each item.  Finally it converst that list into html.

In [dolmen.breadcrumbs/src/dolmen/breadcrumbs/crumbs.py](./src/dolmen/breadcrumbs/crumbs.py])
There are two methods.

1.resolve_name() returns the __name__ of the object twice,or it throws an exception.
Of course for IPulicationRoot, if there is no __name__, it can return None.
You could also write a resolver which returns (__name__, title)

2. breadcrumbs(item, request, resolver=resolve_name) is an iterator which
returns the data structures required to build breadcrumbs.  It gets the
items parents, up to IPublicatinRoot, reverses them, and yeilds a dictinary with
the name and url of the crumb. 

In [dolmen.breadcrumbs/src/dolmen/breadcrumbs/renderer.py](./src/dolmen/breadcrumbs/renderer.py) You will find two different methods. breadcrumbsrenderer() calls
render_breadcrums which calls the
[template](./src/dolmen/breadcrumbs/templates/breadcrumbs.pt)


Christopher Lozinski writes about these breadcrumbs: "They are
beautifully designed, whatever changes I needed to make just took 
a few lines of code. "


