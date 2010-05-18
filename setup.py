#! /usr/bin/env python

from distutils.core import setup

import rarfile

ldesc = rarfile.__doc__.strip()
sdesc = ldesc.split('\n')[0]

setup(
    name = "rarfile",
    version = rarfile.__version__,
    description = sdesc,
    long_description = ldesc,
    author = "Marko Kreen",
    license = "ISC",
    author_email = "markokr@gmail.com",
    url = "http://rarfile.berlios.de/",
    py_modules = ['rarfile'],
    keywords = ['rar', 'archive'],
    classifiers = [
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: ISC License (ISCL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: System :: Archiving :: Compression",
    ]
)

