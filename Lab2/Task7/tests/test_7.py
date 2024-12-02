import unittest
import os
import tempfile
from Lab2.Task7.src.seven import max_subarray_sum, main, process_file
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

    def test_main_function(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file = os.path.join(temp_dir, "input.txt")
            output_file = os.path.join(temp_dir, "output.txt")

            with open(input_file, "w") as f:
                f.write("5\n-1 -2 -3 4 5")

            def temp_main():
                process_file(input_file, output_file)

            execution_time = time_data(temp_main)
            memory_usage = memory_data(temp_main)

            with open(output_file, "r") as f:
                result = f.read().strip()

            self.assertEqual(result, '9')

            print('\nВремя работы:', execution_time, 'секунд')
            print('Память:', memory_usage, 'Мб')
