import unittest
from Lab2.Task3.src.three import count_inversions, main
from utils import time_data, memory_data


class TestCountInversions(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual(count_inversions(arr), 0)

    def test_reversed_array(self):
        arr = [5, 4, 3, 2, 1]
        self.assertEqual(count_inversions(arr), 10)

    def test_example_case(self):
        arr = [1, 8, 2, 1, 4, 7, 3, 2, 3, 6]
        self.assertEqual(count_inversions(arr), 17)

    def test_time_memory_data(self):
        print('Время работы: ', time_data(main), ' секунд')
        print('Память: ', memory_data(main), 'Мб')