#!/usr/bin/env python
# -*- coding: utf-8 -*-

#                        __    __           _     
#   _      ______  _____/ /___/ /________  (_)___ 
#  | | /| / / __ \/ ___/ / __  / ___/ __ \/ / __ \
#  | |/ |/ / /_/ / /  / / /_/ / /__/ /_/ / / / / /
#  |__/|__/\____/_/  /_/\__,_/\___/\____/_/_/ /_/

__title__   = 'worldcoin'
__version__ = '1.0.1'
__author__  = '@c0ding'
__repo__    = 'https://github.com/c0ding/worldcoin-api'
__license__ = 'Apache v2.0 License'

import worldcoin_utils
from worldcoin_api import (
	about, difficulty, hashrate, block_count, total_coins, reward,
	block_hash, transaction, address, generate_address, to_btc,
	to_ltc, to_usd
)
