import unittest
from Lab4.Task13.src.task_stack_and_queue import Stack, Queue


class TestStackAndQueue(unittest.TestCase):
    def test_stack_operations(self):
        stack = Stack()
        self.assertTrue(stack.isEmpty())
        stack.push(10)
        stack.push(20)
        stack.push(30)
        self.assertEqual(stack.display(), [30, 20, 10])
        self.assertEqual(stack.pop(), 30)
        self.assertEqual(stack.display(), [20, 10])
        self.assertEqual(stack.pop(), 20)
        self.assertEqual(stack.pop(), 10)
        self.assertTrue(stack.isEmpty())

    def test_queue_operations(self):
        queue = Queue()
        self.assertTrue(queue.isEmpty())
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        self.assertEqual(queue.display(), [1, 2, 3])
        self.assertEqual(queue.dequeue(), 1)
        self.assertEqual(queue.display(), [2, 3])
        self.assertEqual(queue.dequeue(), 2)
        self.assertEqual(queue.dequeue(), 3)
        self.assertTrue(queue.isEmpty())


if __name__ == "__main__":
    unittest.main()
