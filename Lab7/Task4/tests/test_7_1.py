import unittest
from Lab7.Task4.src.task_two_sequences import longest_common_subsequence


class TestLongestCommonSubsequence(unittest.TestCase):
    def test_example_case(self):
        a = [2, 7, 5]
        b = [2, 5]
        result = longest_common_subsequence(a, b)
        self.assertEqual(result, 2)

    def test_empty_sequence(self):
        a = []
        b = [1, 2, 3]
        result = longest_common_subsequence(a, b)
        self.assertEqual(result, 0)

    def test_no_common_elements(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        result = longest_common_subsequence(a, b)
        self.assertEqual(result, 0)

    def test_identical(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        result = longest_common_subsequence(a, b)
        self.assertEqual(result, 3)

    def test_large_overlap(self):
        a = [1, 2, 3, 4, 5]
        b = [2, 3, 4]
        result = longest_common_subsequence(a, b)
        self.assertEqual(result, 3)

    def test_single_element(self):
        a = [1, 3, 5, 7]
        b = [7]
        result = longest_common_subsequence(a, b)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()
