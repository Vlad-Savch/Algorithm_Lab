import unittest
from Lab3.Task2.src.task_anti_qs import generate_anti_quicksort
from utils import time_data, memory_data


class TestAntiQuickSort(unittest.TestCase):
    def test1_anti_quicksort(self):
        test_value = 3
        expected_result = [2, 3, 1]

        actual_result = generate_anti_quicksort(test_value)
        self.assertEqual(actual_result, expected_result)

    def test2_anti_quicksort(self):
        test_value = 4
        expected_result = [2, 4, 3, 1]

        actual_result = generate_anti_quicksort(test_value)
        self.assertEqual(actual_result, expected_result)


if __name__ == "__main__":
    unittest.main()
