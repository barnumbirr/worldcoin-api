#!/usr/bin/env python
# -*- coding: utf-8 -*-

OFFICIAL_BLOCKEXPLORER = 'http://www.worldcoinexplorer.com/api/'

def blockexplorer(*suffix):
	"""Returns the entrypoint URL for the Worldcoin API.
	   All data provided by the official Worldcoin Blockexplorer.
	   http://www.worldcoinexplorer.com
	"""
	
	return OFFICIAL_BLOCKEXPLORER + '/'.join(suffix)
