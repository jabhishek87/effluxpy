# -*- coding: utf-8 -*-
"""
effluxpy
========

Advanced Browser and Streamer Python with directory gzipped tarball download, file upload,
removal and plugins.

More details on project's README and
`github page <https://github.com/jkabhishek/effluxpy/>`_.


Development Version
-------------------

The effluxpy development version can be installed by cloning the git
repository from `github`_::

    git clone git@github.com:jkabhishek/effluxpy.git

.. _github: https://github.com/jkabhishek/effluxpy

License
-------
MIT (see LICENSE file).
"""

import os
import os.path
import sys
import shutil

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys_path = sys.path[:]
sys.path[:] = (os.path.abspath('effluxpy'),)
__import__('__meta__')
meta = sys.modules['__meta__']
sys.path[:] = sys_path

with open('README.rst') as f:
    meta_doc = f.read()

extra_requires = []
bdist = 'bdist' in sys.argv or any(a.startswith('bdist_') for a in sys.argv)
if bdist or not hasattr(os, 'scandir'):
    extra_requires.append('scandir')

if bdist or not hasattr(shutil, 'get_terminal_size'):
    extra_requires.append('backports.shutil_get_terminal_size')

for debugger in ('ipdb', 'pudb', 'pdb'):
    opt = '--debug=%s' % debugger
    if opt in sys.argv:
        os.environ['UNITTEST_DEBUG'] = debugger
        sys.argv.remove(opt)

setup(
    name=meta.app,
    version=meta.version,
    url=meta.url,
    download_url=meta.tarball,
    license=meta.license,
    author=meta.author_name,
    author_email=meta.author_mail,
    description=meta.description,
    long_description=meta_doc,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        ],
    keywords=['web', 'file', 'browser'],
    packages=[
        'effluxpy',
        'effluxpy.tests',
        'effluxpy.tests.deprecated',
        'effluxpy.tests.deprecated.plugin',
        'effluxpy.transform',
        'effluxpy.plugin',
        'effluxpy.plugin.player',
        ],
    entry_points={
        'console_scripts': (
            'effluxpy=effluxpy.__main__:main'
            )
        },
    package_data={  # ignored by sdist (see MANIFEST.in), used by bdist_wheel
        'effluxpy': [
            'templates/*',
            'static/fonts/*',
            'static/*.*',  # do not capture directories
        ],
        'effluxpy.plugin.player': [
            'templates/*',
            'static/*/*',
        ]},
    install_requires=['flask', 'unicategories'] + extra_requires,
    test_suite='effluxpy.tests',
    test_runner='effluxpy.tests.runner:DebuggerTextTestRunner',
    zip_safe=False,
    platforms='any'
)
