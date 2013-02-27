"""The views are used with the test suite and documentation.

If you change the code please make sure tests and documentation are
still intact.
"""
from django.contrib.auth.decorators import login_required
from django.utils import decorators
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

    @property
    def tab_classes(self):
        """If user is logged in, set ``logged_in_only`` class."""
        classes = super(MainNavigationBaseTab, self).tab_classes[:]
        if self.current_tab.request.user.is_authenticated():
            classes += ['logged_in_only']
        return classes


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


class HiddenTab(MainNavigationBaseTab):
    """A hidden TabView."""
    _is_tab = True
    tab_id = 'hidden'
    template_name = 'hidden_tab.html'
