import unittest
from Lab3.Task6.src.task_sum import sum_of_tenth


class TestSortProductSum(unittest.TestCase):
    def test_case_1(self):
        n, m = 4, 4
        A = [7, 1, 4, 9]
        B = [2, 7, 8, 11]
        self.assertEqual(sum_of_tenth(n, m, A, B), 51)

    def test_case_2(self):
        n, m = 2, 3
        A = [1, 2]
        B = [3, 4, 5]
        self.assertEqual(sum_of_tenth(n, m, A, B), 3)

    def test_case_3(self):
        n, m = 1, 1
        A = [5]
        B = [5]
        self.assertEqual(sum_of_tenth(n, m, A, B), 25)


if __name__ == "__main__":
    unittest.main()
