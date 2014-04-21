#!/usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup

setup(
    name = 'worldcoin',
    version = "0.5.1",
    url = "https://github.com/c0ding/worldcoin-api",
    download_url = "https://github.com/c0ding/worldcoin-api/archive/master.zip",
    author = 'c0ding',
    author_email = 'me@martinsimon.me',
    license = 'Apache v2.0 License',
    packages = ['worldcoin'],
    description = 'Python API for the Worldcoin cryptocurrency.',
    long_description = file('README.md','r').read(),
    keywords = ['WDC', 'Worldcoin', 'LTC', 'Litecoin', 'BTC', 'Bitcoin', 'DOGE', 'Dogecoin', 'cryptocurrency', 'API'],
)
