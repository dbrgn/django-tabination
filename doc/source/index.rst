django-tabination
=================

*django-tabination* is a library that enables you to easily build your own tab
navigation based on class based views.

The main idea behind this library is that the properties of the tabs are defined
inside the view and aren't stored in the database. The database based approach
(which is used for example by `django-sitetree`_ or `django-treenav`_, often
based on `django-mptt`_) is great for CMS-like projects with users editing the
pages directly via the admin, but it causes many problems when the pages are
mainly coded directly in the views because the navigation is then not tracked by
your version control system and can be off-sync / inconsistent between different
versions or systems.

There are also projects that provide a set of template tags to mark a page as
active, which can then be used to render the navigation template accordingly
(e.g. `django-tabs`_). But that solution is very limited and not as flexible as
*django-tabination*.

*django-tabination* allows you to create tabs directly in your class based views
by settings some specific attributes. This can be simplified even further by
creating a common base class for all your tab views that handles all the logic
necessary to build a dynamically configured tab navigation.

Features include conditional displaying/hiding of a tab, translation of the tab
labels, tab hierarchies to build multi-level navigations and more.

Table of Contents
-----------------

.. toctree::
   :maxdepth: 1

   installation
   usage
   The TabView Class <tabview>
   testing


Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. _django-sitetree: https://github.com/idlesign/django-sitetree
.. _django-treenav: https://github.com/caktus/django-treenav
.. _django-tabs: http://code.google.com/p/django-tabs/ 
.. _django-mptt: https://github.com/django-mptt/django-mptt
