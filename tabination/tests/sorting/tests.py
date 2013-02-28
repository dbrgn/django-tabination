from django.test.client import RequestFactory
from django.utils import unittest

from .views import FirstTab, SecondTab, ThirdTab, FourthTab, FifthTab


class SortingTest(unittest.TestCase):
    rf = RequestFactory()

    def test_sorting(self):
        """Tests if the sorting order is correct."""
        request = self.rf.get('/')
        response = FirstTab.as_view()(request)
        context = response.context_data
        self.assertEqual(len(context['tabs']), 5)
        self.assertIsInstance(context['tabs'][0], FirstTab)
        self.assertIsInstance(context['tabs'][1], SecondTab)
        self.assertIsInstance(context['tabs'][2], ThirdTab)
        self.assertIsInstance(context['tabs'][3], FourthTab)
        self.assertIsInstance(context['tabs'][4], FifthTab)
