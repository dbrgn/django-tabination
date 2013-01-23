Installation and Configuration
==============================

There are several ways to install *django-tabination*, either by using a
package manager like pip_ or by manually downloading and installing a
copy of the library.

.. _pip: http://www.pip-installer.org/


Automatic installation via a package manager
--------------------------------------------

You can install *django-tabination* directly from pypi_ using pip::

    pip install django-tabination

.. _pypi: https://pypi.python.org/pypi/django-tabination


Manual installation from a downloaded package
---------------------------------------------

If you prefer not to use an automated package installer, you can
download_ a copy of *django-tabination* and install it manually.

.. _download: https://pypi.python.org/pypi/django-tabination

To install it, navigate to the directory containing :file:`setup.py` on
your console and type::

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


Sourcecode
----------

The sourcecode of *django-tabination* can be forked on GitHub_.

.. _GitHub: https://github.com/dbrgn/django-tabination
