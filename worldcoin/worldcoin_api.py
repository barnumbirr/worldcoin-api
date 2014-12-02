#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib2
from worldcoin_utils import get_addr
from worldcoin_utils import exchange
from worldcoin_utils import gen_eckey
from worldcoin_utils import blockexplorer

__title__   = 'worldcoin'
__version__ = '1.0.1'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/worldcoin-api'
__license__ = 'Apache v2.0 License'


BROWSER_HEADER = {'User-Agent' : 'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/36.0'}


def about():
	"""Returns some information about the worldcoin module."""

	return '{} v.{} is maintained by {} and available at {}.'.format(__title__, __version__, __author__, __repo__)


def difficulty():
	"""Returns the current network difficulty."""

	d = urllib2.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'Difficulty']


def hashrate():
	"""Returns the current network hashrate."""
	
	d = urllib2.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'HashRate']


def block_count():
	"""Returns the number of blocks in the longest block chain.
	   Equivalent to Bitcoin's getblockcount.
	"""

	d = urllib2.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'Blocks']


def total_coins():
	"""Returns the number of Worldcoin mined."""
	
	d = urllib2.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'TotalCoins']

	
def reward():
	"""Returns the current block reward."""

	d = urllib2.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'Reward']


def block_hash(PARAMETER=None):
	"""Returns the block hash at a specific height.
	   [PARAMETER] is optional, should be a block hash or height.
	   [DEFAULT] equals to last block.
	"""

	if not PARAMETER:
		d = urllib2.urlopen(blockexplorer('block'))
		return json.loads(d.read())
	else:
		d = urllib2.urlopen(blockexplorer('block') + '/' + str(PARAMETER))
		return json.loads(d.read())
	

def transaction(PARAMETER):
	"""Returns details of a specific transaction.
	   [PARAMETER] is required and should be a transaction hash.
	"""

	d = urllib2.urlopen(blockexplorer('transaction') + '/' + str(PARAMETER))
	return json.loads(d.read())


def address(PARAMETER):
	"""Returns details of a specific address.
	   [PARAMETER] is required and should be an address hash.
	"""

	d = urllib2.urlopen(blockexplorer('address') + '/' + str(PARAMETER))
	return json.loads(d.read())


def generate_address():
	"""Returns a valid Worldcoin address and it's
	   matching private key.
	   On OSX run this in i386 mode.
	"""

	return get_addr(gen_eckey(compressed=True,version=73),version=73)


def to_btc():
	"""Returns array with trading pair object."""
	
	c = urllib2.Request(exchange('wdc_btc'), headers = BROWSER_HEADER)
	d = urllib2.urlopen(c)
	return json.loads(d.read())


def to_ltc():
	"""Returns array with trading pair object."""
	
	c = urllib2.Request(exchange('wdc_ltc'), headers = BROWSER_HEADER)
	d = urllib2.urlopen(c)
	return json.loads(d.read())


def to_usd():
	"""Returns array with trading pair object."""
	
	c = urllib2.Request(exchange('wdc_usd'), headers = BROWSER_HEADER)
	d = urllib2.urlopen(c)
	return json.loads(d.read())
