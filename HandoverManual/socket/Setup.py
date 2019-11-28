#!/usr/bin/env python
# coding: utf-8

'''
@Author: Senkita
'''

from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize('application_entry.pyx'))