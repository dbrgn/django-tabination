#!/usr/bin/env python

from setuptools import setup
import tabination

readme = open('README.rst').read()

setup(name='django-tabination',
      version=tabination.__VERSION__,
      description='A library that enables you to easily build your own tab navigation based on class based views.',
      long_description=readme,
      author=tabination.__AUTHOR__,
      author_email=tabination.__AUTHOR_EMAIL__,
      url='https://github.com/dbrgn/django-tabination',
      license='LGPLv3',
      keywords='django tabs tabination',
      packages=['tabination'],
      platforms=['any'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: Web Environment',
          'Framework :: Django',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
          'Operating System :: OS Independent',
          'Programming Language :: Python :: 2',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Programming Language :: Python :: Implementation :: CPython',
          'Programming Language :: Python :: Implementation :: PyPy',
          'Topic :: Internet :: WWW/HTTP',
          'Topic :: Software Development :: Libraries :: Python Modules',
          ],
    )
