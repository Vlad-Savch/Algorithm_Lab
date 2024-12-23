import unittest
from Lab7.Task5.src.task_three_sequences import longest_common_subsequence_three


class TestLongestCommonSubsequenceThree(unittest.TestCase):
    def test_basic_case(self):
        a = [1, 2, 3]
        b = [2, 1, 3]
        c = [1, 3, 5]
        result = longest_common_subsequence_three(a, b, c)
        self.assertEqual(result, 2)

    def test_empty_sequence(self):
        a = []
        b = [1, 2, 3]
        c = [1, 3]
        result = longest_common_subsequence_three(a, b, c)
        self.assertEqual(result, 0)

    def test_no_common_elements(self):
        a = [1, 2, 3]
        b = [4, 5, 6]
        c = [7, 8, 9]
        result = longest_common_subsequence_three(a, b, c)
        self.assertEqual(result, 0)

    def test_full_overlap(self):
        a = [1, 2, 3]
        b = [1, 2, 3]
        c = [1, 2, 3]
        result = longest_common_subsequence_three(a, b, c)
        self.assertEqual(result, 3)

    def test_partial_overlap(self):
        a = [1, 2, 3, 4]
        b = [2, 3, 5]
        c = [3, 4, 6]
        result = longest_common_subsequence_three(a, b, c)
        self.assertEqual(result, 1)

    def test_large_case(self):
        a = [1, 2, 3, 4, 5]
        b = [2, 3, 4, 5]
        c = [3, 4, 5, 6]
        result = longest_common_subsequence_three(a, b, c)
        self.assertEqual(result, 3)

if __name__ == '__main__':
    unittest.main()
