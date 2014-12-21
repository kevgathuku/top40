#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

setup(
    name='top40',
    version='0.2.0',
    py_modules=['top40'],
    author = "Kevin Ndung'u",
    author_email = 'kevgathuku@gmail.com',
    description = ("A simple command line tool to display songs in the "
                    "UK Top 40 Charts"),
    url='https://github.com/kevgathuku/top40',
    license = "MIT",
    install_requires=[
        'Click>=3.3',
        'requests>=2.4.3',
        'requests-cache==0.4.6',
        'google-api-python-client==1.3.1',
    ],
    entry_points='''
        [console_scripts]
        top40=top40:top40
    ''',
)
