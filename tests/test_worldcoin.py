#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import unittest
import worldcoin

class worldcointestsuite(unittest.TestCase):

	_multiprocess_can_split_ = True

	def test_get_difficulty(self):
		assert type(worldcoin.get_difficulty()) is float

	def test_get_block_count(self):
		assert type(worldcoin.get_block_count()) is int

	def test_get_total_wdc(self):
		assert type(worldcoin.get_total_wdc()) is float
	
	def test_get_block_hash(self):
		assert type(worldcoin.get_block_hash(1)) is str
		
	def test_get_transaction(self):
		assert type(worldcoin.get_transaction('0fc36e386282295512aa63d9f5047d9dc305c983394803474cfaa2f99d7e1bd0')) is str

	def test_get_address(self):
		assert type(worldcoin.get_address('WYJ142WhSViiCJuUB2JbpbNiCFAuk9B47z')) is str
		
	def test_to_btc(self):
		assert type(worldcoin.to_btc()) is str

	def test_to_usd(self):
		assert type(worldcoin.to_usd()) is str

if __name__ == '__main__':
    unittest.main()