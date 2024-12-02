import unittest
import random
import tempfile
import os
from Lab2.Task1.src.one import merge_sort, main, sort_file
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
        with tempfile.TemporaryDirectory() as temp_dir:
            input_file = os.path.join(temp_dir, "input.txt")
            output_file = os.path.join(temp_dir, "output.txt")

            with open(input_file, "w") as f:
                f.write("5\n4 3 2 1 5")

            def temp_main():
                sort_file(input_file, output_file)

            execution_time = time_data(temp_main)
            memory_usage = memory_data(temp_main)

            with open(output_file, "r") as f:
                sorted_result = f.read().strip()

            self.assertEqual(sorted_result, "1 2 3 4 5")

            print('Время работы:', execution_time, 'секунд')
            print('Использование памяти:', memory_usage, 'Мб')

    if __name__ == "__main__":
        unittest.main()

