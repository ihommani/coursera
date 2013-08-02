#! /usr/bin/env python
#-*- coding: ISO-8859-15 -*-

import unittest
import random
from divide_and_conquer_algorithm import MergeArray


class TestMergeSort(unittest.TestCase):
    
    def setUp(self):
        self.toSort = range(100)
        random.shuffle(self.toSort)

    def test_shuffle(self):
        sorter = MergeArray()
        self.assertEqual(sorter.sort(self.toSort), range(100))


if __name__ == "__main__":
    unittest.main()
