from django.core.exceptions import ImproperlyConfigured
from django.test.client import RequestFactory
from django.utils import unittest

# The code below is used with the test suite and is included in the
# documentation. If you change the code please make sure tests and
# documentation are still intact.

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
    template_name = 'navigation/first_child_tab.html'


class SecondChildTab(ChildNavigationBaseTab):
    _is_tab = True
    tab_id = 'second_child'
    tab_label = 'Second Child'
    template_name = 'navigation/second_child_tab.html'


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


class MultilevelTest(unittest.TestCase):
    rf = RequestFactory()

    def test_parent(self):
        """Tests the parent of a child navigation tab."""
        request = self.rf.get('/')
        response = FirstChildTab.as_view()(request)
        context = response.context_data
        self.assertIsInstance(context['parent_tabs'], list)
        self.assertEqual(len(context['parent_tabs']), 2)
        self.assertIsInstance(context['parent_tabs'][0], ParentTab)
        self.assertIsInstance(context['parent_tabs'][1], EmptyTab)
        self.assertEqual(context['parent_tab_id'], ParentTab.tab_id)

    def test_children(self):
        """Tests if a parent tab knows it's children."""
        request = self.rf.get('/')
        response = ParentTab.as_view()(request)
        context = response.context_data
        self.assertIsInstance(context['child_tabs'], list)
        self.assertEqual(len(context['child_tabs']), 2)
        self.assertIsInstance(context['child_tabs'][0], FirstChildTab)
        self.assertIsInstance(context['child_tabs'][1], SecondChildTab)

    def test_parent_none(self):
        """If tab_parent is not configured it is missing from context."""
        request = self.rf.get('/')
        response = ParentTab.as_view()(request)
        with self.assertRaises(KeyError):
            response.context_data['parent_tabs']

    def test_parent_not__is_tab(self):
        """Using a TabView as parent which has not _is_tab = True fails."""
        request = self.rf.get('/')
        with self.assertRaises(ImproperlyConfigured):
            BrokenChildTab.as_view()(request)
