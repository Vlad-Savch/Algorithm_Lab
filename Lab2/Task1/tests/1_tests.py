import unittest
import random
from Lab2.Task1.src.one import merge_sort, main
from utils import time_data, memory_data


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

    def test_time_memory_data(self):
        print('Время работы: ', time_data(main), ' секунд')
        print('Память: ', memory_data(main), 'Мб')

