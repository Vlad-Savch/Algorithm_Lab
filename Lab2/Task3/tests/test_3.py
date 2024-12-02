import unittest
import os
import tempfile
from Lab2.Task3.src.three import count_inversions, main, process_file
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

    def test_inversion_count(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file = os.path.join(temp_dir, "input.txt")
            output_file = os.path.join(temp_dir, "output.txt")

            with open(input_file, "w") as f:
                f.write("5\n4 3 2 1 5")

            def temp_main():
                process_file(input_file, output_file)

            execution_time = time_data(temp_main)
            memory_usage = memory_data(temp_main)

            with open(output_file, "r") as f:
                result = f.read().strip()

            self.assertEqual(result, "6")

            print('Время работы:', execution_time, 'секунд')
            print('Использование памяти:', memory_usage, 'Мб')
