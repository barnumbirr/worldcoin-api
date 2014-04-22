#!/usr/bin/env python
# -*- coding: utf-8 -*-

import worldcoin

def estimated_wdc(hashrate):
	"""Returns an estimated amount of Worldcoins a given
	   hashrate will yield at a given difficulty and reward.
	   This profit is NOT guaranteed.
	"""
	
	difficulty = worldcoin.difficulty()
	reward = worldcoin.reward()
	estimated = float(hashrate) * float(1000) * float(86400) * float(reward) / (float(4294967296) * float(difficulty))
	estimated = '%.2f' % estimated
	print 'A hashrate of {} khash/s and a difficulty of {} will yield {}WDC per day.'.format(hashrate, difficulty, estimated)

if __name__ == '__main__':
	estimated_wdc(hashrate)
