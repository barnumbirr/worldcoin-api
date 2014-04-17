#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json
import urllib
from utils import blockexplorer

def get_difficulty():
	"""Returns the current network difficulty."""

	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'Difficulty']


def get_block_count():
	"""Returns the number of blocks in the longest block chain.
	Equivalent to Bitcoin's getblockcount."""

	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'Blocks']


def get_total_wdc():
	"""Returns the number of Worldcoin mined."""
	
	d = urllib.urlopen(blockexplorer('coindetails'))
	d = json.loads(d.read())
	return d[u'TotalCoins']
