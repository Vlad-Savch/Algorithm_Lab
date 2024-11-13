import unittest
import random
from Lab2.one import merge_sort


class TestMergeSortWithFiles(unittest.TestCase):

    def test_sorted_array(self):
        sorted_array = list(range(1, 1001))
        self.assertEqual(merge_sort(sorted_array), sorted(sorted_array))

    def test_reversed_array(self):
        reversed_array = list(range(1000, 0, -1))
        self.assertEqual(merge_sort(reversed_array), sorted(reversed_array))

    def test_random_array(self):
        random_array = random.sample(range(1, 1001), 200)
        expected_result = sorted(random_array)
        self.assertEqual(merge_sort(random_array), expected_result)