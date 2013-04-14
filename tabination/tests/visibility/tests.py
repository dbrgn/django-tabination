from django.test.client import RequestFactory
from django.utils import unittest

from .views import SpamTab, HamTab


class AuthenticatedUserStub(object):
    def is_authenticated(self):
        return True


class AnonymousUserStub(object):
    def is_authenticated(self):
        return False


class FakeAuthRequestFactory(RequestFactory):
    """A RequestFactory with fake authentication."""
    def get(self, path, data={}, login=False, **extra):
        """Performs a GET request.

        Use the login argument to get a request with a authenticated user.
        """
        request = super(FakeAuthRequestFactory, self).get(path, data, **extra)
        if login:
            request.user = AuthenticatedUserStub()
        else:
            request.user = AnonymousUserStub()
        return request


class VisibilityTest(unittest.TestCase):
    rf = FakeAuthRequestFactory()

    def test_anonymous(self):
        """Test the group of tabs with an anonymous user."""
        request = self.rf.get('/')
        response = SpamTab.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(response.context_data['tabs']))
        self.assertIsInstance(response.context_data['tabs'][0], SpamTab)
        self.assertNotIn('logged_in_only', response.context_data['tabs'][0].tab_classes)

    def test_anonymous_redirect(self):
        """Accessing the protected HamTab results in a 302."""
        request = self.rf.get('/')
        response = HamTab.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_authenticated(self):
        """Test the group of tabs with an authenticated user."""
        request = self.rf.get('/', login=True)
        response = HamTab.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, len(response.context_data['tabs']))
        self.assertIsInstance(response.context_data['tabs'][0], SpamTab)
        self.assertIsInstance(response.context_data['tabs'][1], HamTab)
        self.assertIn('logged_in_only', response.context_data['tabs'][1].tab_classes)
