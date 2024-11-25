import unittest
from Lab2.Task5.src.five import solve, main
from utils import time_data, memory_data


class TestMajorityElement(unittest.TestCase):

    def test_example_1(self):
        a = [2, 3, 9, 2, 2]
        self.assertEqual(solve(a), 1)

    def test_example_2(self):
        a = [1, 2, 3, 4]
        self.assertEqual(solve(a), 0)

    def test_time_memory_data(self):
        print('Время работы: ', time_data(main), ' секунд')
        print('Память: ', memory_data(main), 'Мб')
