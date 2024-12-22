import unittest
from Lab5.Task2.src.task_tree_height import calculate_tree_height


class TestTreeHeight(unittest.TestCase):
    def test_example_1(self):
        n = 5
        parents = [4, -1, 4, 1, 1]

        result = calculate_tree_height(n, parents)

        self.assertEqual(result, 3)

    def test_single_node(self):
        n = 1
        parents = [-1]

        result = calculate_tree_height(n, parents)

        self.assertEqual(result, 1)

    def test_linear_tree(self):
        n = 5
        parents = [-1, 0, 1, 2, 3]

        result = calculate_tree_height(n, parents)

        self.assertEqual(result, 5)

    def test_star_tree(self):
        n = 5
        parents = [-1, 0, 0, 0, 0]

        result = calculate_tree_height(n, parents)

        self.assertEqual(result, 2)

    def test_balanced_tree(self):
        n = 7
        parents = [-1, 0, 0, 1, 1, 2, 2]

        result = calculate_tree_height(n, parents)

        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
