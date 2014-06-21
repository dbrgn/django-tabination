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

- Supported Django versions: 1.4, 1.5, 1.6
- Supported Python versions: 2.6, 2.7, 3.3, 3.4, pypy2


Docs
----

The docs can be found at http://django-tabination.readthedocs.org/.


Installing
----------

You can install *django-tabination* directly from pypi using pip::

    $ pip install django-tabination

Currently there is no further configuration needed. For more information about
setup and usage, please refer to `the docs`_.


Coding Guidelines
-----------------

`PEP8 <http://www.python.org/dev/peps/pep-0008/>`__ via `flake8
<https://pypi.python.org/pypi/flake8>`_ with max-line-width set to 99 and
E126-E128 ignored.


Testing
-------

Testing is implemented using tox_ and pytest_. Violations of the coding
guidelines will be counted as errors.

The easiest way to run the tests is by simply running ``tox``::

    $ pip install tox
    $ tox

This will run all tests in different virtualenvs with different configuration.
Currently there are around 6 different tox environments. They can be listed
with the ``-l`` switch::

    $ tox -l
    py26-django14
    py26-django15
    py27-django14
    py27-django15
    py34-django16
    pypy-django14
    pypy-django15

To run the tests only in specific environments, use the ``-e`` switch::

    $ tox -e py27-django14,py26-django15


License
-------

Copyright 2012 - 2014 Danilo Bargen (http://dbrgn.ch/) and contributors.

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
.. _tox: http://tox.readthedocs.org/
.. _pytest: http://pytest.org/
