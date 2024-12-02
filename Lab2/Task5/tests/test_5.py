import unittest
import tempfile
import os
from Lab2.Task5.src.five import solve, main, process_file
from utils import time_data, memory_data


class TestMajorityElement(unittest.TestCase):

    def test_example_1(self):
        a = [2, 3, 9, 2, 2]
        self.assertEqual(solve(a), 1)

    def test_example_2(self):
        a = [1, 2, 3, 4]
        self.assertEqual(solve(a), 0)

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

            self.assertEqual(result, "0")

            print('\nВремя работы:', execution_time, 'секунд')
            print('Использование памяти:', memory_usage, 'Мб')
