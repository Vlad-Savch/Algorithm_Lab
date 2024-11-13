import unittest
from Lab2.three import count_inversions


class TestCountInversions(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(count_inversions(arr), 0)

    def test_reversed_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(count_inversions(arr), 10)

    def test_single_element(self):
        arr = [1]
        self.assertEqual(count_inversions(arr), 0)

    def test_elements_sorted(self):
        arr = [1, 2]
        self.assertEqual(count_inversions(arr), 0)

    def test_elements_unsorted(self):
        arr = [2, 1]
        self.assertEqual(count_inversions(arr), 1)

    def test_example_case(self):
        arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        self.assertEqual(count_inversions(arr), 17)
