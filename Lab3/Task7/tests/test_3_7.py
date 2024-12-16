import unittest
from Lab3.Task7.src.task_digital_sort import digit_sort


class TestDigitSort(unittest.TestCase):
    def test_case_1(self):
        expected_result = [2, 3, 1]
        n, m, k = 3, 3, 1
        lines = [
            "bab",
            "bba",
            "baa"
        ]

        result = digit_sort(n, m, k, lines)

        self.assertEqual(result, expected_result)

    def test_case_2(self):
        expected_result = [3, 2, 1]
        n, m, k = 3, 3, 2
        lines = [
            "bab",
            "bba",
            "baa"
        ]

        result = digit_sort(n, m, k, lines)

        self.assertEqual(result, expected_result)

    def test_case_3(self):
        expected_result = [2, 3, 1]
        n, m, k = 3, 3, 3
        lines = [
            "bab",
            "bba",
            "baa"
        ]

        result = digit_sort(n, m, k, lines)

        self.assertEqual(result, expected_result)
