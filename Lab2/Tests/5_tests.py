import unittest
from Lab2.five import solve


class TestMajorityElement(unittest.TestCase):

    def test_example_1(self):
        a = [2, 3, 9, 2, 2]
        self.assertEqual(solve(a), 1)

    def test_example_2(self):
        a = [1, 2, 3, 4]
        self.assertEqual(solve(a), 0)

