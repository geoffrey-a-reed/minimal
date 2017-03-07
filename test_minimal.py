# -*- coding: utf-8 -*-

'''Minimal test suite for minimal package.

Tests that addition functions as expected.
'''


import os
import sys
sys.path.insert(0, os.path.abspath('..'))

import minimal


def test_add_positive_integers():
	'''Adding positive integers functions as expected.'''
	assert minimal.add(1, 1) == 2


def test_add_negative_integers():
	'''Adding negative integers functions as expected.'''
	assert minimal.add(-1, -1) == -2