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

    def test_latest_hash(self):
        assert type(worldcoin.get_total_wdc()) is float

if __name__ == '__main__':
    unittest.main()