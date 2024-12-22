import unittest
from Lab5.Task4.src.task_pyramid import build_min_heap


class TestHeapBuilder(unittest.TestCase):
    def test_example_1(self):
        arr = [5, 4, 3, 2, 1]

        swaps = build_min_heap(arr)

        self.assertEqual(len(swaps), 3)
        self.assertEqual(arr, [1, 2, 3, 5, 4])

    def test_single_element(self):
        arr = [1]

        swaps = build_min_heap(arr)

        self.assertEqual(len(swaps), 0)
        self.assertEqual(arr, [1])

    def test_already_heap(self):
        arr = [1, 2, 3, 4, 5]

        swaps = build_min_heap(arr)

        self.assertEqual(len(swaps), 0)
        self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_reverse_order(self):
        arr = [6, 5, 4, 3, 2, 1]

        swaps = build_min_heap(arr)

        self.assertEqual(len(swaps), 4)
        self.assertEqual(arr, [1, 2, 4, 3, 5, 6])


if __name__ == "__main__":
    unittest.main()
