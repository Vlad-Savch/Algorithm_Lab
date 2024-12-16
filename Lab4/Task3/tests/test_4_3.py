import unittest
from Lab4.Task3.src.task_bracket_sequence import bracket_sequence


class TestBracketSequence(unittest.TestCase):
    def test_valid_sequences(self):
        self.assertTrue(bracket_sequence("()"))
        self.assertTrue(bracket_sequence("[]"))
        self.assertTrue(bracket_sequence("()[]"))
        self.assertTrue(bracket_sequence("(())"))
        self.assertTrue(bracket_sequence("([])"))

    def test_invalid_sequences(self):
        self.assertFalse(bracket_sequence("("))
        self.assertFalse(bracket_sequence(")"))
        self.assertFalse(bracket_sequence("([)]"))
        self.assertFalse(bracket_sequence("((]]"))
        self.assertFalse(bracket_sequence(")("))

    def test_mixed_sequences(self):
        self.assertTrue(bracket_sequence("()[]([])"))
        self.assertFalse(bracket_sequence("()[(])"))
        self.assertTrue(bracket_sequence("(([]))"))
        self.assertFalse(bracket_sequence("(([])"))


if __name__ == "__main__":
    unittest.main()
