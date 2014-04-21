#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
from worldcoin_utils import exchange
from worldcoin_utils import blockexplorer

__title__   = 'worldcoin'
__version__ = '0.5.1'
__author__  = "@c0ding"
__repo__    = "https://github.com/c0ding/worldcoin-api"
__license__ = "Apache v2.0 License"


def about():
	return "{} v.{} is maintained by {} and available at {}.".format(__title__, __version__, __author__, __repo__)


def difficulty():
	"""Returns the current network difficulty."""

	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'Difficulty']


def hashrate():
	"""Returns the current network hashrate."""
	
	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'HashRate']


def block_count():
	"""Returns the number of blocks in the longest block chain.
	   Equivalent to Bitcoin's getblockcount.
	"""

	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'Blocks']


def total_coins():
	"""Returns the number of Worldcoin mined."""
	
	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'TotalCoins']


def block_hash(PARAMETER=None):
	"""Returns the block hash at a specific height.
	   [PARAMETER] is optional, should be a block hash or height.
	   [DEFAULT] equals to last block.
	"""
	if not PARAMETER:
		d = urllib.urlopen(blockexplorer('block'))
		return json.loads(d.read())
	else:
		d = urllib.urlopen(blockexplorer('block') + '/' + str(PARAMETER))
		return json.loads(d.read())
	

def transaction(PARAMETER):
	"""Returns details of a specific transaction.
	   [PARAMETER] is required and should be a transaction hash.
	"""

	d = urllib.urlopen(blockexplorer('transaction') + '/' + str(PARAMETER))
	return json.loads(d.read())


def address(PARAMETER):
	"""Returns details of a specific address.
	   [PARAMETER] is required and should be an address hash.
	"""

	d = urllib.urlopen(blockexplorer('address') + '/' + str(PARAMETER))
	return json.loads(d.read())


def to_btc():
	"""Returns array with trading pair object."""
	
	d = urllib.urlopen(exchange('wdc_btc'))
	return json.loads(d.read())
	
	
def to_usd():
	"""Returns array with trading pair object."""
	
	d = urllib.urlopen(exchange('wdc_usd'))
	return json.loads(d.read())

