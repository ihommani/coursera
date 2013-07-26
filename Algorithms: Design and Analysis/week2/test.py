#! /usr/bin/env python
#-*- coding: ISO-8859-15 -*-

import unittest
import random
from quick_sort import QuickSortArray


class TestMergeSort(unittest.TestCase):
    
    def setUp(self):
        self.toSort = range(100)
        random.shuffle(self.toSort)

    def test_shuffle_first(self):
        sorter = QuickSortArray(1)
        self.assertEqual(sorter.sort(self.toSort), range(100))

    def test_shuffle_last(self):
        sorter = QuickSortArray(2)
        self.assertEqual(sorter.sort(self.toSort), range(100))

    def test_shuffle_middle(self):
        sorter = QuickSortArray(3)
        self.assertEqual(sorter.sort(self.toSort), range(100))

    def test_shuffle_uniform(self):
        sorter = QuickSortArray(4)
        self.assertEqual(sorter.sort(self.toSort), range(100))

    @unittest.expectedFailure
    def test_shuffle_middle(self):
        sorter = QuickSortArray(3)
        self.assertEqual(sorter.sort(self.toSort), range(101))


if __name__ == "__main__":
    unittest.main()

