#!/usr/bin/env python
# -*- coding: utf-8 -*-

BLOCKEXPLORER_URL = 'http://www.worldcoinexplorer.com/api/'

def blockexplorer(*suffix):
	"""Returns url for BLOCKEXPLORER resource."""
	return BLOCKEXPLORER_URL + '/'.join(suffix)
