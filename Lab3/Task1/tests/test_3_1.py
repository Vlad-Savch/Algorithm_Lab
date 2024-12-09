import unittest
from Lab3.Task1.src.task_qs import randomized_quick_sort3


class TestQuickSortSimple(unittest.TestCase):
    def test_randomized_quick_sort3(self):
        array = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
        expected_result = sorted(array)

        randomized_quick_sort3(array, 0, len(array) - 1)

        self.assertEqual(array, expected_result)


if __name__ == "__main__":
    unittest.main()
