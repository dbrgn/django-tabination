"""
.. moduleauthor:: Danilo Bargen <mail@dbrgn.ch>

"""
# -*- coding: utf-8 -*-
from __future__ import print_function, division, absolute_import, unicode_literals

from django.core.exceptions import ImproperlyConfigured
from django.views.generic import TemplateView

from six import with_metaclass


class _TabTracker(type):
    """
    Metaclass that tracks all subclasses with an _is_tab attribute.

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


class TabView(with_metaclass(_TabTracker, TemplateView)):
    """
    This is a tab view that sets different tab properties and handles the tab
    groups.

    All attributes can be overridden with a Python property, e.g.::

        @property
        def tab_visible(self):
           return self.object.is_active

    Internally, the tabs are tracked using the :class:`_TabTracker`
    `metaclass <http://stackoverflow.com/a/6581949/284318>`_.
    All subclasses that have set the ``_is_tab`` attribute are added to the
    ``self._registry`` list.

    """
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
    weight = 0
    """Weight of the tab, used for sorting the tabs."""

    def get_group_tabs(self):
        """
        Return instances of all other tabs that are members of the tab's
        tab group.
        """
        if self.tab_group is None:
            raise ImproperlyConfigured(
                "%s requires a definition of 'tab_group'" %
                self.__class__.__name__)
        group_members = [t for t in self._registry if t.tab_group == self.tab_group]
        return [t() for t in group_members]

    @property
    def tab_visible(self):
        """
        Whether or not this tab is shown in the tab group. Or to be more exact,
        whether or not this tab is contained in ``{{ tabs }}``.

        The default behavior is to set the tab as visible if it has a label.

        """
        return self.tab_label is not None

    def _process_tabs(self, tabs, current_tab, group_current_tab):
        """
        Process and prepare tabs.

        This includes steps like updating references to the current tab,
        filtering out hidden tabs, sorting tabs etc...

        Args:
            tabs:
                The list of tabs to process.
            current_tab:
                The reference to the currently loaded tab.
            group_current_tab:
                The reference to the active tab in the current tab group. For
                parent tabs, this is different than for the current tab group.

        Returns:
            Processed list of tabs. Note that the method may have side effects.

        """
        # Update references to the current tab
        for t in tabs:
            t.current_tab = current_tab
            t.group_current_tab = group_current_tab

        # Filter out hidden tabs
        tabs = list(filter(lambda t: t.tab_visible, tabs))

        # Sort remaining tabs in-place
        tabs.sort(key=lambda t: t.weight)

        return tabs

    def get_context_data(self, **kwargs):
        """
        Adds tab information to context.

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
        context = super(TabView, self).get_context_data(**kwargs)

        # Update the context with kwargs, TemplateView doesn't do this.
        context.update(kwargs)

        # Add tabs and "current" references to context
        process_tabs_kwargs = {
            'tabs': self.get_group_tabs(),
            'current_tab': self,
            'group_current_tab': self,
        }
        context['tabs'] = self._process_tabs(**process_tabs_kwargs)
        context['current_tab_id'] = self.tab_id

        # Handle parent tabs
        if self.tab_parent is not None:
            # Verify that tab parent is valid
            if self.tab_parent not in self._registry:
                msg = '%s has no attribute _is_tab' % self.tab_parent.__class__.__name__
                raise ImproperlyConfigured(msg)

            # Get parent tab instance
            parent = self.tab_parent()

            # Add parent tabs to context
            process_parents_kwargs = {
                'tabs': parent.get_group_tabs(),
                'current_tab': self,
                'group_current_tab': parent,
            }
            context['parent_tabs'] = self._process_tabs(**process_parents_kwargs)
            context['parent_tab_id'] = parent.tab_id

        # Handle child tabs
        if self.tab_id in self._children:
            process_children_kwargs = {
                'tabs': [t() for t in self._children[self.tab_id]],
                'current_tab': self,
                'group_current_tab': None,
            }
            context['child_tabs'] = self._process_tabs(**process_children_kwargs)

        return context
