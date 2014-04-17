#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
from utils import blockexplorer

#                        __    __           _     
#   _      ______  _____/ /___/ /________  (_)___ 
#  | | /| / / __ \/ ___/ / __  / ___/ __ \/ / __ \
#  | |/ |/ / /_/ / /  / / /_/ / /__/ /_/ / / / / /
#  |__/|__/\____/_/  /_/\__,_/\___/\____/_/_/ /_/


__title__   = 'worldcoin'
__version__ = '0.2'
__author__  = "@c0ding"
__repo__    = "https://github.com/c0ding/worldcoin-api"
__license__ = "Apache v2.0 License"


def about():
	return "{} v.{} is maintained by {} and available at {}.".format(__title__, __version__, __author__, __repo__)

def get_difficulty():
	"""Returns the current network difficulty."""

	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'Difficulty']


def get_block_count():
	"""Returns the number of blocks in the longest block chain.
	   Equivalent to Bitcoin's getblockcount.
	"""

	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'Blocks']


def get_total_wdc():
	"""Returns the number of Worldcoin mined."""
	
	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'TotalCoins']


def get_block_hash(PARAMETER):
	"""Returns the block hash at a specific height.
	   [PARAMETER] is required and should be a block hash or height.
	"""

	d = urllib.urlopen(blockexplorer('block') + '/' + str(PARAMETER))
	d = json.loads(d.read())
	return json.dumps(d, indent=4)
	

def get_transaction(PARAMETER):
	"""Returns details of a specific transaction.
	   [PARAMETER] is required and should be a transaction hash.
	"""

	d = urllib.urlopen(blockexplorer('transaction') + '/' + str(PARAMETER))
	d = json.loads(d.read())
	return json.dumps(d, indent=4)


def get_address(PARAMETER):
	"""Returns details of a specific address.
	   [PARAMETER] is required and should be an address hash.
	"""

	d = urllib.urlopen(blockexplorer('address') + '/' + str(PARAMETER))
	d = json.loads(d.read())
	return json.dumps(d, indent=4)
