import unittest
import random
import tempfile
import os
from Lab2.Task1.src.one import merge_sort, main, sort_file
from utils import time_data, memory_data


class TestMergeSortWithFiles(unittest.TestCase):

    def test_sorted_array(self):
        sorted_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        expected = sorted(sorted_array)

        result = merge_sort(sorted_array)

        self.assertEqual(result, expected)

    def test_reversed_array(self):
        reversed_array = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        expected = sorted(reversed_array)

        result = merge_sort(reversed_array)

        self.assertEqual(result, expected)

    def test_random_array(self):
        random_array = random.sample(range(1, 1001), 200)
        expected_result = sorted(random_array)

        result = merge_sort(random_array)

        self.assertEqual(result, expected_result)


if __name__ == "__main__":
    unittest.main()

