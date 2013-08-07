django-tabination
=================

.. image:: https://secure.travis-ci.org/dbrgn/django-tabination.png?branch=master
    :alt: Build status
    :target: http://travis-ci.org/dbrgn/django-tabination

.. image:: https://coveralls.io/repos/dbrgn/django-tabination/badge.png?branch=master
    :alt: Coverage
    :target: https://coveralls.io/r/dbrgn/django-tabination

.. image:: https://pypip.in/d/django-tabination/badge.png
    :alt: PyPI download stats
    :target: https://crate.io/packages/django-tabination

*django-tabination* is a lightweight (~70 SLOC) Django 1.4+ library that enables
you to easily build your own tab navigation based on class based views.

It supports code based creation of tabs directly in your views, conditional
displaying/hiding of a tab, translation of the tab labels, tab sorting,
multi-level tab navigations and more.


Docs
----

The docs can be found at http://django-tabination.readthedocs.org/.


Installing
----------

You can install *django-tabination* directly from pypi using pip::

    $ pip install django-tabination

Currently there is no further configuration needed. For more information about
setup and usage, please refer to `the docs`_.


Changelog
---------

*django-tabination* uses `Semantic Versioning`_ 2.0.0-rc.1.

v0.3.1 (2013-08-07)

- [bug] Fixed bug #10 related to multilevel navigation

v0.3.0 (2013-02-28)

- [add] Sorting of tabs

v0.2.0 (2013-02-18)

- [add] Multilevel navigation

v0.1.1 (2012-05-04)

- [add] Added ``current_tab_id`` to context by default

v0.1.0 (2012-04-04)

- [add] Initial version


Testing
-------

To setup a testing environment, you need to install Django and some additional
dependencies::

    $ pip install Django
    $ make install

To run the test suite, use ::

    $ make test

If you want to generate a coverage report, use ::

    $ make report

To see a HTML version of the coverage report, there's ::

    $ make report-html

Finally, to check conformance to the PEP8 coding standard, use ::

    $ make flake8

The flake8 configuration ignores E128 (*continuation line under-indented for
visual indent*) errors and allows a max line length of 99 characters per line.


License
-------

Copyright 2012 - 2013 Danilo Bargen (http://dbrgn.ch/) and contributors.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with this program. If not, see http://www.gnu.org/licenses/lgpl.html.


.. _the docs: http://django-tabination.readthedocs.org/en/latest/installation.html
.. _semantic versioning: http://semver.org/
