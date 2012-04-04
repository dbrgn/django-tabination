Installation and Configuration
==============================

There are several ways to install *django-tabination*, either by using a package
manager like `pip <http://pip.openplans.org/>`_ or by manually downloading and
installing a copy of the library.

Automatic installation via a package manager
--------------------------------------------

You can easily install *django-tabination* using pip::

    pip install -e git://github.com/FactorAG/django-tabination.git#egg=tabination


Manual installation from a downloaded package
---------------------------------------------

If you prefer not to use an automated package installer, you can download a
copy of *django-tabination* and install it manually.

To install it, navigate to the directory containing setup.py on your console
and type::

    python setup.py install


Configuration
-------------

Currently there is no further configuration needed to use *django-tabination*.

..
    To enable *django-tabination*, add ``tabination`` it to the ``INSTALLED_APPS`` setting of
    your project.

    Your Django settings file might look like this::

        INSTALLED_APPS = (
            'django.contrib.auth',
            'django.contrib.sites',
            'tabination',
            # other apps...
        )
