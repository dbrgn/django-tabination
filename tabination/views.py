"""
.. moduleauthor:: Danilo Bargen <gezuru@gmail.com>

"""

from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView


class _TabTracker(type):
    """Metaclass that tracks all subclasses with an _is_tab attribute.

    All tracked classes are stored inside self._registry.

    If multilevel navigation is used all relationships between a parent
    and it's children are stored in the self._children dictionary.
    """
    def __init__(cls, name, bases, attrs):
        if hasattr(cls, '_is_tab'):
            TabView._registry.append(cls)
            if cls.tab_parent is not None:
                if cls.tab_parent.tab_id not in TabView._children:
                    TabView._children[cls.tab_parent.tab_id] = []
                TabView._children[cls.tab_parent.tab_id].append(cls)


class TabView(TemplateView):
    """This is a tab view that sets different tab properties and handles the
    tab groups.

    All attributes can be overridden with a Python property, e.g.::

        @property
        def tab_visible(self):
           return self.object.is_active

    Internally, the tabs are tracked using the :class:`_TabTracker`
    `metaclass <http://stackoverflow.com/a/6581949/284318>`_.
    All subclasses that have set the ``_is_tab`` attribute are added to the
    ``self._registry`` list.

    """

    __metaclass__ = _TabTracker
    _registry = []
    """In here, references to all tabs are stored."""
    _children = {}
    """Stores all parent -> child relationships."""
    tab_id = None
    """ID of the tab, can be used for URL, CSS classes and more."""
    tab_label = None
    """Label for the tab. If label is ``None``, tab should be hidden."""
    tab_group = None
    """All tabs with the same group string will be contained in ``{{ tabs }}``."""
    tab_counter = None
    """A string or callable with a count that can be shown on the tab."""
    tab_classes = []
    """A list of CSS classes that can be added to the tab."""
    tab_rel = ''
    """String that can be set as the HTML rel element."""
    tab_parent = None
    """Name of the parent tab class."""

    def get_group_tabs(self):
        """Return instances of all other tabs that are members of the
        tab's tab group."""
        if self.tab_group is None:
            raise ImproperlyConfigured(
                "%s requires a definition of 'tab_group'" %
                self.__class__.__name__)
        group_members = [t for t in self._registry if t.tab_group == self.tab_group]
        return [t() for t in group_members]

    @property
    def tab_visible(self):
        """Whether or not this tab is shown in the tab group. Or to be more exact,
        whether or not this tab is contained in ``{{ tabs }}``.

        The default behavior is to set the tab as visible if it has a label.

        """
        return self.tab_label is not None

    def get_visible_tabs(self):
        """Returns instances of all visible tabs of the tab's group.

        It's important that the tab are instanciated so that the
        instance methods can be used.
        """
        # Get all group tabs
        tabs = [t for t in self.get_group_tabs()]

        # Add reference to current tab to all other tabs
        for t in tabs:
            t.current_tab = self

        # Remove all tabs that shouldn't be visible
        tabs = filter(lambda t: t.tab_visible, tabs)

        return tabs

    def get_context_data(self, **kwargs):
        """Adds tab information to context.

        To retrieve a list of all group tab instances, use
        ``{{ tabs }}`` in your template.

        The id of the current tab is added as ``current_tab_id`` to the
        template context.

        If the current tab has a parent tab the parent's id is added to
        the template context as ``parent_tab_id``. Instances of all tabs
        of the parent level are added as ``parent_tabs`` to the context.

        If the current tab has children they are added to the template
        context as ``child_tabs``.
        """
        context = super(TabView, self).get_context_data()

        # Update the context with kwargs, TemplateView doesn't do this.
        context.update(kwargs)

        context['current_tab_id'] = self.tab_id
        context['tabs'] = self.get_visible_tabs()

        if self.tab_parent is not None:
            if self.tab_parent not in self._registry:
                msg = '%s has no attribute _is_tab' % self.tab_parent.__class__.__name__
                raise ImproperlyConfigured(msg)
            context['parent_tab_id'] = self.tab_parent().tab_id
            context['parent_tabs'] = self.tab_parent().get_visible_tabs()

        if self.tab_id in self._children:
            context['child_tabs'] = [t() for t in self._children[self.tab_id]]

        return context
