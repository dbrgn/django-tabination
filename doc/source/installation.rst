Installation and Configuration
==============================

There are several ways to install *django-tabination*, either by using a
package manager like pip_ or by manually downloading and installing a
copy of the library.


Installing
----------

The recommended way to install *django-tabination* is directly from pypi_ using
pip::

    pip install django-tabination

If you prefer not to use an automated package installer, you can download_ a
copy of *django-tabination* and install it manually. To install it, navigate to
the directory containing :file:`setup.py` on your console and type::

    python setup.py install


Configuration
-------------

Currently there is no further configuration needed to use *django-tabination*.
Take a look at the :doc:`usage` docs to see how to implement your tabs.

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


Source Code
-----------

The source code of *django-tabination* is licensed under the LGPLv3 license and
can be forked on GitHub_.


.. _pip: http://www.pip-installer.org/
.. _pypi: https://pypi.python.org/pypi/django-tabination
.. _download: https://pypi.python.org/pypi/django-tabination
.. _github: https://github.com/dbrgn/django-tabination
