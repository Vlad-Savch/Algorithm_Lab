import unittest
from Lab6.Task8.src.task_hash_table import process_hash_table


class TestHashTable(unittest.TestCase):
    def test_case_1(self):
        n, x, a, b = 4, 0, 0, 0
        ac, bc, ad, bd = 1, 1, 0, 0
        expected_output = (3, 1, 1)

        result = process_hash_table(n, x, a, b, ac, bc, ad, bd)

        self.assertEqual(result, expected_output)

    def test_case_2(self):
        n, x, a, b = 5, 1, 1, 1
        ac, bc, ad, bd = 1, 2, 3, 4
        expected_output = (152757, 16, 21)

        result = process_hash_table(n, x, a, b, ac, bc, ad, bd)

        self.assertEqual(result, expected_output)

    def test_case_3(self):
        n, x, a, b = 3, 0, 0, 0
        ac, bc, ad, bd = 0, 0, 1, 1
        expected_output = (15, 3, 3)

        result = process_hash_table(n, x, a, b, ac, bc, ad, bd)

        self.assertEqual(result, expected_output)


if __name__ == "__main__":
    unittest.main()
