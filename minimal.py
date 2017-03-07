# -*- coding: utf-8 -*-

'''Minimal Python package.

Contains one function which adds its two parameters.
'''


from codecs import open
from os import path

root = path.abspath(path.dirname(__file__))

with open(path.join(root, 'VERSION.txt'), encoding='utf-8') as f:
    version = f.read().strip()


__version__ = version

__all__ = ['add']


def add(x, y):
	'''Adds x and y.'''
	return x + y