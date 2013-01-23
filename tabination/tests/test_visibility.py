from django.contrib.auth.decorators import login_required
from django.test.client import RequestFactory
from django.utils import decorators, unittest
from django.utils.translation import ugettext as _

from tabination.views import TabView


class MainNavigationBaseTab(TabView):
    """Base class for all main navigation tabs."""
    tab_group = 'main_navigation'
    tab_classes = ['main-navigation-tab']

    def get_context_data(self, **kwargs):
        context = super(MainNavigationBaseTab, self).get_context_data(**kwargs)
        context['spam'] = 'ham'
        return context


class SpamTab(MainNavigationBaseTab):
    """A simple TabView."""
    _is_tab = True
    tab_id = 'spam'
    tab_label = _('Spam')
    template_name = 'spam_tab.html'


class HamTab(MainNavigationBaseTab):
    """TabView is only visible after authentication."""
    _is_tab = True
    tab_id = 'ham'
    tab_label = _('Ham')
    tab_rel = 'nofollow,noindex'
    template_name = 'ham_tab.html'

    @decorators.method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        """Make sure only authenticated users can access this tab."""
        return super(HamTab, self).dispatch(*args, **kwargs)

    @property
    def tab_visible(self):
        """Show tab only if current user is logged in."""
        return self.current_tab.request.user.is_authenticated()

    @property
    def tab_classes(self):
        """If user is logged in, set ``logged_in_only`` class."""
        classes = super(HamTab, self).tab_classes[:]
        if self.current_tab.request.user.is_authenticated():
            classes += ['logged_in_only']
        return classes


class HiddenTab(MainNavigationBaseTab):
    """A hidden TabView."""
    _is_tab = True
    tab_id = 'hidden'
    template_name = 'hidden_tab.html'


class AuthenticatedUserStub(object):
    def is_authenticated(self):
        return True


class AnonymousUserStub(object):
    def is_authenticated(self):
        return False


class UserTestCase(unittest.TestCase):
    """A TestCase with a RequestFactory."""
    rf = RequestFactory()

    def get(self, path, data={}, login=False, **extra):
        """Performs a GET request.

        Use the login argument to get a request with a authenticated user.
        """
        request = self.rf.get(path, data, **extra)
        if login:
            request.user = AuthenticatedUserStub()
        else:
            request.user = AnonymousUserStub()
        return request


class VisibilityTest(UserTestCase):
    def test_anonymous(self):
        """Test the group of tabs with an anonymous user."""
        request = self.get('/')
        response = SpamTab.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(1, len(response.context_data['tabs']))
        self.assertIsInstance(response.context_data['tabs'][0], SpamTab)

    def test_anonymous_redirect(self):
        """Accessing the protected HamTab results in a 302."""
        request = self.get('/')
        response = HamTab.as_view()(request)
        self.assertEqual(response.status_code, 302)

    def test_authenticated(self):
        """Test the group of tabs with an authenticated user."""
        request = self.get('/', login=True)
        response = HamTab.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(2, len(response.context_data['tabs']))
        self.assertIsInstance(response.context_data['tabs'][0], SpamTab)
        self.assertIsInstance(response.context_data['tabs'][1], HamTab)
