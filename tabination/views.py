"""
.. moduleauthor:: Danilo Bargen <gezuru@gmail.com>

"""

from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView


class _TabTracker(type):
    """Metaclass that tracks all subclasses that have set the _is_tab
    attribute. The classes are stored inside self._registry."""
    def __init__(cls, name, bases, attrs):
        if hasattr(cls, '_is_tab'):
            TabView._registry.append(cls)


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

    def get_group_tabs(self):
        """Return instances of all other tabs that are members of the
        tab's tab group."""
        if self.tab_group is None:
            raise ImproperlyConfigured(
                "%s requires a definition of 'tab_group'" \
                    % self.__class__.__name__)
        group_members = [t for t in self._registry if t.tab_group == self.tab_group]
        return [t() for t in group_members]

    @property
    def tab_visible(self):
        """Whether or not this tab is shown in the tab group. Or to be more exact,
        whether or not this tab is contained in ``{{ tabs }}``.

        The default behavior is to set the tab as visible if it has a label.

        """
        return self.tab_label is not None

    def get_context_data(self, **kwargs):
        """Add tab information to context. To retrieve list of all group tab
        instances, use ``{{ tabs }}`` in your template."""

        # Get base context
        context = super(TabView, self).get_context_data()

        # Update the context with kwargs, as TemplateView doesn't do this
        context.update(kwargs)

        # Get all group tabs
        tabs = [t for t in self.get_group_tabs()]

        # Add reference to current tab to all other tabs
        for t in tabs:
            t.current_tab = self

        # Add current tab id to context
        context['current_tab_id'] = self.tab_id

        # Remove all tabs that shouldn't be visible
        tabs = filter(lambda t: t.tab_visible, tabs)

        # We need tab instances of all tab group members in order to
        # be able to use instance methods.
        context['tabs'] = tabs

        return context
