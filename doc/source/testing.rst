Testing
=======

Current build status:

.. image:: https://secure.travis-ci.org/dbrgn/django-tabination.png?branch=master
    :alt: Build status
    :target: http://travis-ci.org/dbrgn/django-tabination

To set up a testing environment, you need to install Django and some additional
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

.. note::

    The flake8 configuration ignores E128 (*continuation line under-indented for
    visual indent*) errors and allows a max line length of 99 characters per
    line.
