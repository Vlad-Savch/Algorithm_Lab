import unittest
from Lab4.Task2.src.task_queue import queue_commands


class TestQueueOperations(unittest.TestCase):
    def test_single_add_and_remove(self):
        commands = ["+ 10", "-"]
        expected = [10]

        result = queue_commands(commands)

        self.assertEqual(result, expected)

    def test_multiple_adds_and_removes(self):
        commands = ["+ 5", "+ 15", "-", "-", "+ 20", "-"]
        expected = [5, 15, 20]

        result = queue_commands(commands)

        self.assertEqual(result, expected)

    def test_no_remove(self):
        commands = ["+ 1", "+ 2"]
        expected = []

        result = queue_commands(commands)

        self.assertEqual(result, expected)

    def test_empty(self):
        commands = []
        expected = []

        result = queue_commands(commands)

        self.assertEqual(result, expected)

    def test_only_remove(self):
        commands = ["-"]
        expected = []

        result = queue_commands(commands)

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
