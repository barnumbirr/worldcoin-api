#!/usr/bin/env python
# -*- coding: utf-8 -*-

OFFICIAL_BLOCKEXPLORER = 'http://www.worldcoinexplorer.com/api/'
CRYPTOCOIN_API = 'http://www.cryptocoincharts.info/v2/api/tradingPair/'

def blockexplorer(*suffix):
	"""Returns the entrypoint URL for the Worldcoin block API.
	   All data provided by the official Worldcoin Blockexplorer.
	   http://www.worldcoinexplorer.com
	"""
	
	return OFFICIAL_BLOCKEXPLORER + '/'.join(suffix)

def exchange(*suffix):
	"""Returns the entrypoint URL for the Worldcoin price API.
	   All data provided by CryptoCoin.
	   http://www.cryptocoincharts.info
	"""
	
	return CRYPTOCOIN_API + '/'.join(suffix)
