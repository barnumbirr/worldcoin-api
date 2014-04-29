#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
sys.path.insert(0, os.path.abspath('..'))
import unittest
import worldcoin

__title__   = 'worldcoin'
__version__ = '1.0.1'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/worldcoin-api'
__license__ = 'Apache v2.0 License'

class worldcointestsuite(unittest.TestCase):

	_multiprocess_can_split_ = True

	def test_difficulty(self):
		worldcoin.difficulty()
		assert type(worldcoin.difficulty()) is float
		
	def test_hashrate(self):
		worldcoin.hashrate()
		assert type(worldcoin.hashrate()) is int

	def test_block_count(self):
		worldcoin.block_count()
		assert type(worldcoin.block_count()) is int

	def test_total_coins(self):
		worldcoin.total_coins()
		assert type(worldcoin.total_coins()) is float
		
	def test_reward(self):
		worldcoin.reward()
		assert type(worldcoin.reward()) is float
	
	def test_block_hash(self):
		worldcoin.block_hash()
		assert type(worldcoin.block_hash()) is dict
		
	def test_transaction(self):
		worldcoin.transaction('0fc36e386282295512aa63d9f5047d9dc305c983394803474cfaa2f99d7e1bd0')
		assert type(worldcoin.transaction('0fc36e386282295512aa63d9f5047d9dc305c983394803474cfaa2f99d7e1bd0')) is dict

	def test_address(self):
		worldcoin.address('WYJ142WhSViiCJuUB2JbpbNiCFAuk9B47z')
		assert type(worldcoin.address('WYJ142WhSViiCJuUB2JbpbNiCFAuk9B47z')) is dict

	def test_generate_address(self):
		worldcoin.generate_address()
		assert type(worldcoin.generate_address()) is str
		
	def test_to_btc(self):
		worldcoin.to_btc()
		assert type(worldcoin.to_btc()) is dict
		
	def test_to_ltc(self):
		worldcoin.to_ltc()
		assert type(worldcoin.to_ltc()) is dict

	def test_to_usd(self):
		worldcoin.to_usd()
		assert type(worldcoin.to_usd()) is dict

if __name__ == '__main__':
    unittest.main()
