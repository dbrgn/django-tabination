from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView


class TabTracker(type):
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
    
    Attributes:
    tab_id -- ID of the tab, can be used for URL and more.
    tab_label -- Text on the tab. If label is None, tab will be hidden.
    tab_group -- All tabs with the same group string will be listed.
    tab_counter -- A string or callable with a count that will be shown
                   on the tab.
    tab_classes -- A list of CSS classes that will be added to the tab.
    tab_rel -- String that will be added to the HTML rel element.
    tab_visible -- Whether or not this tab is shown in the tab group.

    """

    __metaclass__ = TabTracker
    _registry = []
    tab_id = None
    tab_label = None
    tab_group = None
    tab_counter = None
    tab_classes = []
    tab_rel = u''
    tab_visible = True

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
        return self.tab_label is not None
    
    def get_context_data(self, **kwargs):
        """Add tab information to context."""

        # Get base context
        context = super(TabView, self).get_context_data()

        # Update the context with kwargs, as TemplateView doesn't do this
        context.update(kwargs)

        # Get all group tabs
        tabs = [t for t in self.get_group_tabs() if t.tab_visible]

        # We need tab instances of all tab group members in order to
        # be able to use instance methods.
        context['tabs'] = tabs

        return context
