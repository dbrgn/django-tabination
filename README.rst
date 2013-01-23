django-tabination
=================


*django-tabination* is a lightweight library that enables you to easily build
your own tab navigation based on class based views.


Docs
----

The docs can be found at http://django-tabination.readthedocs.org/.


Installing
----------

You can install *django-tabination* directly from pypi using pip::

    $ pip install django-tabination


Changelog
---------

v0.1.1 (2012-05-04)

- [add] Added `current_tab_id` to context by default

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

    $ make coverage

To see a HTML version of the coverage report, there's ::

    $ make coverage-html

Finally, to check conformance to the PEP8 coding standard, use ::

    $ make flake8

The flake8 configuration ignores E128 (*continuation line under-indented for
visual indent*) errors and allows a max line length of 99 characters per line.


License
-------

Copyright 2012 - 2013 Danilo Bargen (http://dbrgn.ch/).

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU Lesser General Public License as published by the Free
Software Foundation, either version 3 of the License, or any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE. See the GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License along
with this program.  If not, see http://www.gnu.org/licenses/lgpl.html.
