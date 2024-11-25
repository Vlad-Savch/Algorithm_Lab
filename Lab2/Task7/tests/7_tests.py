import unittest
from Lab2.Task7.src.seven import max_subarray_sum, main
from utils import time_data, memory_data


class TestMaxSubarraySum(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(max_subarray_sum([1, 2, 3, 4, 5]), 15)

    def test_negative_numbers(self):
        self.assertEqual(max_subarray_sum([-1, -2, -3, -4]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(max_subarray_sum([-2, 1, -3, 4, -1, 2, 1, -5, 4]), 6)

    def test_large_array(self):
        arr = [i for i in range(-1000, 1001)]
        self.assertEqual(max_subarray_sum(arr), sum(arr[1000:2001]))

    def test_time_memory_data(self):
        print('Время работы: ', time_data(main), ' секунд')
        print('Память: ', memory_data(main), 'Мб')
