#!/usr/bin/env python

from setuptools import setup
import tabination

setup(name='django-tabination',
      version=tabination.__VERSION__,
      description='A library that enables you to easily build your own tab navigation based on class based views.',
      author=tabination.__AUTHOR__,
      author_email=tabination.__AUTHOR_EMAIL__,
      maintainer=tabination.__MAINTAINER__,
      maintainer_email=tabination.__MAINTAINER_EMAIL__,
      url='https://github.com/FactorAG/django-tabination',
      license='LGPLv3',
      keywords='django tabs tabination',
      packages=['tabination'],
      platforms=['any'],
      classifiers=[
          'Development Status :: 4 - Beta',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
    )
