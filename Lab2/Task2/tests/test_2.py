import unittest
import tempfile
import os
from Lab2.Task2.src.two import merge_sort, process_file, main
from utils import time_data, memory_data


class TestMergeSort(unittest.TestCase):
    def test_merge_sort(self):
        arr = [5, 2, 8, 1, 3]
        expected = [1, 2, 3, 5, 8]
        with tempfile.NamedTemporaryFile() as temp_output_file:
            temp_output_file.close()
            with open(temp_output_file.name, 'w') as output_file:
                merge_sort(arr, 0, len(arr) - 1, output_file)
                self.assertEqual(arr, expected)

    def test_time_and_memory(self):
        elapsed_time = time_data(main)
        memory_usage = memory_data(main)

        print(f"\nВремя работы: {elapsed_time} секунд")
        print(f"Память: {memory_usage} Мб")
