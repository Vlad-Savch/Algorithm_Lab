import unittest
from Lab7.Task1.src.task_coins import min_coins


class TestMinCoins(unittest.TestCase):
    def test_case_1(self):
        money = 2
        coins = [1, 3, 4]
        result = min_coins(money, coins)
        self.assertEqual(result, 2)

    def test_case_2(self):
        money = 5
        coins = [1, 3, 4]
        result = min_coins(money, coins)
        self.assertEqual(result, 2)

    def test_case_3(self):
        money = 10
        coins = [1, 3, 4]
        result = min_coins(money, coins)
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
