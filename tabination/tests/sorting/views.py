from tabination.views import TabView


class SortedBaseTab(TabView):
    tab_group = 'sorted_navigation'


class ThirdTab(SortedBaseTab):
    _is_tab = True
    tab_id = 'third'
    tab_label = 'Third Tab'
    template_name = 'third_tab.html'
    weight = 50


class FifthTab(SortedBaseTab):
    _is_tab = True
    tab_id = 'fifth'
    tab_label = 'Fifth Tab'
    template_name = 'fifth_tab.html'
    weight = 80


class SecondTab(SortedBaseTab):
    _is_tab = True
    tab_id = 'second'
    tab_label = 'Second Tab'
    template_name = 'second_tab.html'


class FourthTab(SortedBaseTab):
    _is_tab = True
    tab_id = 'fourth'
    tab_label = 'Fourth Tab'
    template_name = 'fourth_tab.html'
    weight = 50


class FirstTab(SortedBaseTab):
    _is_tab = True
    tab_id = 'first'
    tab_label = 'First Tab'
    template_name = 'first_tab.html'
    weight = -20
