#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='top40',
    version='0.1',
    py_modules=['top40'],
    author = 'kevgathuku',
    author_email = 'kevgathuku@gmail.com',
    description = ("Print and optionally download songs in the "
                    "UK Top 40 Charts"),
    url='https://github.com/kevgathuku/top40',
    license = "MIT",
    install_requires=[
        'Click>=3.3',
        'requests',
        'requests-cache',
        'google-api-python-client',
    ],
    entry_points='''
        [console_scripts]
        top40=top40:cli
    ''',
)
