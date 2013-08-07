from django.core.exceptions import ImproperlyConfigured
from django.test.client import RequestFactory
from django.utils import unittest

from .views import (ParentTab, EmptyTab, FirstChildTab, SecondChildTab, BrokenChildTab)


class MultilevelTest(unittest.TestCase):
    rf = RequestFactory()

    def test_parent(self):
        """Tests the parent of a child navigation tab."""
        request = self.rf.get('/')
        response = FirstChildTab.as_view()(request)
        context = response.context_data

        # Check list of parent tabs
        self.assertIsInstance(context['parent_tabs'], list)
        self.assertEqual(len(context['parent_tabs']), 2)
        self.assertIsInstance(context['parent_tabs'][0], ParentTab)
        self.assertIsInstance(context['parent_tabs'][1], EmptyTab)

        # Check important tab IDs
        self.assertEqual(context['parent_tab_id'], ParentTab.tab_id)
        self.assertEqual(context['current_tab_id'], FirstChildTab.tab_id)

        # Check references to current tab
        self.assertEqual(context['tabs'][1].group_current_tab.tab_id, FirstChildTab.tab_id)
        self.assertEqual(context['parent_tabs'][1].group_current_tab.tab_id, ParentTab.tab_id)

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
