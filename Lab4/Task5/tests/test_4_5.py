import unittest
from Lab4.Task5.src.task_max_stack import MaxStack


class TestMaxStack(unittest.TestCase):
    def test_push_max(self):
        stack = MaxStack()

        stack.push(1)
        stack.push(2)

        self.assertEqual(stack.get_max(), 2)

    def test_push_pop_max(self):
        stack = MaxStack()

        stack.push(1)
        stack.push(2)

        stack.pop()
        self.assertEqual(stack.get_max(), 1)

    def test_multiple_push_pop(self):
        stack = MaxStack()

        stack.push(3)
        stack.push(1)
        stack.push(5)
        stack.push(2)

        self.assertEqual(stack.get_max(), 5)
        stack.pop()
        self.assertEqual(stack.get_max(), 5)
        stack.pop()
        self.assertEqual(stack.get_max(), 3)

    def test_single_element(self):
        stack = MaxStack()

        stack.push(10)

        self.assertEqual(stack.get_max(), 10)
        stack.pop()
        self.assertEqual(stack.get_max(), None)


if __name__ == "__main__":
    unittest.main()
