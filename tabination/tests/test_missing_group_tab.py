from __future__ import with_statement

from django.core.exceptions import ImproperlyConfigured
from django.test.client import RequestFactory
from django.utils import unittest

from tabination.views import TabView


class IncompleteTab(TabView):
    """TabView with a missing tab_group attribute."""
    _is_tab = True
    tab_id = 'incomplete'
    tab_label = 'Incomplete'
    template_name = 'spam_tab.html'


class MissingTabGroupTest(unittest.TestCase):
    def test_missing_tab_group(self):
        """Tests a TabView with a missing tab_group attribute."""
        request = RequestFactory().get('/')
        with self.assertRaises(ImproperlyConfigured):
            IncompleteTab.as_view()(request)
