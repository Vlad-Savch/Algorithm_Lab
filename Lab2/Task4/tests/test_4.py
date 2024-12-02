import unittest
import os
import tempfile
from Lab2.Task4.src.four import binary_search, main, process_file
from utils import time_data, memory_data


class TestMainFunction(unittest.TestCase):
    def test_main_function(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file = os.path.join(temp_dir, "input.txt")
            output_file = os.path.join(temp_dir, "output.txt")

            def main_with_temp_files():
                input_path = input_file
                output_path = output_file

            with open(input_file, "w") as f:
                f.write("5\n1 5 8 12 13\n5\n8 1 23 1 11")

            process_file(input_file, output_file)

            with open(output_file, "r") as f:
                result = f.read().strip()

            self.assertEqual(result, "2 0 -1 0 -1")

            execution_time = time_data(main)
            memory_usage = memory_data(main)

            print('\nВремя работы:', execution_time, 'секунд')
            print('Использование памяти:', memory_usage, 'Мб')
