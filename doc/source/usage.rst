Usage
=====

.. |TabView| replace:: :class:`views.TabView`

*django-tabination* is a library that enables you to easily build your own tab
navigation templates by extending the |TabView| base class.

The library is strongly based on the
`class based views <https://docs.djangoproject.com/en/dev/topics/class-based-views/>`_
that Django has introduced with version 1.3. You cannot use this library if
your project is using function based views.


Creating tab views
------------------

For a working custom tab view, the following things are requried:

* You need to extend the |TabView| base class
* You need to add the class attribute ``_is_tab = True`` to your view
* You need to specify the ``tab_group``.
* Each tab needs a ``tab_id``.
* In order for the tab to be visible in your navigation, you need to
  set a ``tab_label``.
* You need to define a ``template_name``.

.. note::

    The ``_is_tab`` attribute is needed for the class to be tracked by a
    tracking metaclass. Therefore it needs to be present when the classes are
    parsed by the python interpreter and cannot be added later,
    e.g. with a decorator.

Getting started
+++++++++++++++

The base class resides in ``tabination.views``. Import it like this::

    from tabination.views import TabView

This is a very simple example tab::

    class SpamTab(TabView):
        _is_tab = True
        tab_id = 'spam'
        tab_group = 'main_navigation'
        tab_label = 'Spam'
        template_name = 'tabs/spam_tab.html'

Now your page will be rendered using the template `tabs/spam_tab.html`, because
|TabView| extends Django's generic `TemplateView`.

If you want, you can also use other `generic view mixins
<https://docs.djangoproject.com/en/dev/ref/class-based-views/#mixins>`_ (or any
other custom mixins) to provide additional functionality. A good example would
be the `SingleObjectMixin`::

    from django.views.generic.detail import SingleObjectMixin

    class SpamTab(SingleObjectMixin, TabView):
        _is_tab = True
        tab_id = 'spam'
        tab_group = 'main_navigation'
        tab_label = 'Spam'
        template_name = 'tabs/spam_tab.html'
        model = models.SpamCan

Now the `SpamCan` object with a primary key provided from your URL definition
will be passed on to your template as ``object`` (see
`<https://docs.djangoproject.com/en/dev/ref/class-based-views/#singleobjectmixin>`_).

.. warning::

    As of Django 1.4, above example does not work due to a bug in the class
    based views implementation (``get_context_data`` in the generic mixins does
    not call ``super()``). This is fixed in the current development version
    (see `Ticket #16074 <https://code.djangoproject.com/ticket/16074>`_) and
    will most probably be included in the next Django release. In the meantime,
    you can either use generic mixins that don't affect ``get_context_data``,
    manually call ``TabView.get_context_data(self, **kwargs)`` from your tab
    code or create your own mixins. See the next section for an example.

You can do everything with your TabView that you can do with normal class
based views. The only things that you need to bear in mind is that 
|TabView| always needs to be the base class (on the right side of the
parentheses). It may be overloaded using mixins but cannot be combined with
other views that override ``get_context_data``.

Customizing your tab view
+++++++++++++++++++++++++

You can further customize your tab view by overloading the |TabView|'s class
attributes with your own class- or instance attributes or
`properties <http://docs.python.org/library/functions.html#property>`_
(if logic is required).

For available attributes, see |TabView| documentation. You can also create your
own attributes, as long as they're used in your template.

Keep in mind that if the tab you're working with is not the currently loaded
tab, it is just an instance of the tab that has not passed through the
dispatching functions. In case you need some variables that you get only by
dispatching the request (e.g. ``self.kwargs``), you can use the special
attribute ``self.current_tab`` to gain access to the currently loaded tab.
See also section :ref:`accessing-request-data`.

Here is an example of a more sophisticated tab view hierarchy::

    from tabination.views import TabView
    from django.views.generic.base import TemplateResponseMixin
    from django.utils.translation import ugettext as _


    class MainNavigationBaseTab(TemplateResponseMixin, TabView):
        """Base class for all main navigation tabs."""
        tab_group = 'main_navigation'
        tab_classes = ['main-navigation-tab']

        def get_context_data(self, **kwargs):
            context = super(MainNavigationBaseTab, self).get_context_data(**kwargs)
            context['spam'] = 'ham'
            return context


    class SpamTab(MainNavigationBaseTab):
        _is_tab = True
        tab_id = 'spam'
        tab_label = _('Spam')
        template_name = 'tabs/spam_tab.html'


    class HamTab(MainNavigationBaseTab):
        _is_tab = True
        tab_id = 'ham'
        tab_label = _('Ham')
        tab_rel = 'nofollow,noindex'
        template_name = 'tabs/ham_tab.html'

        @property
        def tab_visible(self):
            """Show tab only if current user is logged in."""
            return self.request.user.is_authenticated()

        @property
        def tab_classes(self):
            """If user is logged in, set ``logged_in_only`` class."""
            classes = super(HamTab, self).tab_classes
            if self.request.user.is_authenticated():
                classes += ['logged_in_only']
            return classes


    class HiddenTab(MainNavigationBaseTab):
        _is_tab = True
        tab_id = 'hidden'
        template_name = 'tabs/hidden_tab.html'


In this example, a base tab class was created. Because it does not contain the
``_is_tab`` class attribute, it is not listed as a tab itself (which wouldn't
be possible anyway, as it has no ``tab_id``). The three classes
:class:`SpamTab`, :class:`HamTab` and :class:`HiddenTab` extend the
:class:`MainNavigationBaseTab`. The base class predefines a tab group, so each
extending tab doesn't have to define it again, therefore following the DRY
principle. It also adds a new context variable called ``spam`` to the context
of each tab.

The second tab, :class:`HamTab`, overrides some more attributes. In this
example, the tab is only visible in the template if the current user is logged
in.  Additionally, if the user is logged in, a new CSS class `logged_in_only`
gets added to the ``tab_classes`` list, in order to be able to show the user
that this is a "secret" tab that guest users aren't able to see.

The third tab, :class:`HiddenTab`, doesn't define a ``tab_label`` and is
therefore not shown at all (see default behavior of
:func:`views.TabView.tab_visible`).

.. warning::

    Keep in mind that if you're overriding ``get_context_data(self, **kwargs)``,
    you need to call the superclasses' versions of the method first (like in
    the example above). Otherwise, you'll override the ``tabs`` context
    variable.

.. _accessing-request-data:

Accessing request data
++++++++++++++++++++++

If you want to access ``self.request`` in a function used to render the tab
item in your template, you may notice that it is not available. This is
because the tab instances other than your current tab don't pass through the
request dispatching functions.

If you need access to your current request information, you can access it via
the ``self.current_tab`` attribute, e.g.::

    class SpamTab(TabView):
        # (...)
        def username(self):
            current_tab = self.current_tab
            user = current_tab.request.user
            return user.username


Tab navigation template
-----------------------

In order to display the tabs in your templates, you need to create a tab list
using the ``{{ tabs }}`` context variable. You can also use
``{{ current_tab_id }}`` to access the id of the currently active tab. Here is
an example template:

.. code-block:: guess

    <div id="tab_navigation">
        <ul>
            {% for tab in tabs %}
                <li class="{{ tab.tab_classes|join:" " }}{% if tab.tab_id == current_tab_id %} active{% endif %}">
                    <a href="/tabs/{{ tab.id }}.html" {%if tab.tab_rel %}rel="{{ tab.tab_rel }}"{% endif %}>
                    {% if tab.tab_counter %}<em>{{ tab.tab_counter }}</em>{% endif %}
                    {{ tab.tab_label }}
                    </a>
                </li>
            {% endfor %}
        </ul>
    </div>

Each item in the ``{{ tabs }}`` list is an instance of a tab in the same tab
group as the current tab. Therefore you can use all class- and instance
variables as well as all functions without arguments that are defined in the
|TabView| base class or in the extending class.

It's a good idea to put this template code in a file called e.g.
``blocks/tabination.html`` and to include it everywhere you want the
navigation to be displayed:

.. code-block:: guess

    ...
    {% include 'blocks/tabination.html %}
    ...
