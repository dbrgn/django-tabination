"""The views are used with the test suite and documentation.

If you change the code please make sure tests and documentation are
still intact.
"""
from tabination.views import TabView


# First navigation level

class ParentNavigationBaseTab(TabView):
    """Base class for all parent navigation tabs."""
    tab_group = 'parent_navigation'
    tab_classes = ['parent-navigation-tab']


class ParentTab(ParentNavigationBaseTab):
    _is_tab = True
    tab_id = 'parent'
    tab_label = 'Parent'
    template_name = 'parent_tab.html'


class EmptyTab(ParentNavigationBaseTab):
    _is_tab = True
    tab_id = 'empty'
    tab_label = 'Empty'
    template_name = 'empty_tab.html'


# Second navigation level

class ChildNavigationBaseTab(TabView):
    """Base class for all child navigation tabs."""
    tab_group = 'child_navigation'
    tab_classes = ['child-navigation-tab']
    tab_parent = ParentTab


class FirstChildTab(ChildNavigationBaseTab):
    _is_tab = True
    tab_id = 'first_child'
    tab_label = 'First Child'
    template_name = 'first_child_tab.html'


class SecondChildTab(ChildNavigationBaseTab):
    _is_tab = True
    tab_id = 'second_child'
    tab_label = 'Second Child'
    template_name = 'second_child_tab.html'


class HiddenChildTab(ChildNavigationBaseTab):
    """This class has ``tab_visible`` set to ``False``."""
    _is_tab = True
    tab_id = 'hidden_child'
    tab_label = 'Hidden Child'
    template_name = 'hidden_child_tab.html'
    tab_visible = False


class BrokenChildNavigationBaseTab(TabView):
    """This class has a wrong tab_parent class."""
    tab_group = 'child_navigation'
    tab_classes = ['child-navigation-tab']
    tab_parent = ParentNavigationBaseTab


class BrokenChildTab(BrokenChildNavigationBaseTab):
    _is_tab = True
    tab_id = 'broken'
    tab_label = 'Broken'
    template_name = 'broken_tab.html'
