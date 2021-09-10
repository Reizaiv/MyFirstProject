import unittest
import TicTacToe as ttt

class MyTestCase(unittest.TestCase):
    def test_something(self):
        val = 'X'
        result = ttt.player_turn(val)
        self.assertEqual(result, 'O')  # add assertion here


if __name__ == '__main__':
    unittest.main()