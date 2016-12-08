import unittest

from how_about_a_nice_game_of_chess_part1 import find_password


class Part1TestCase(unittest.TestCase):
    def test_find_password(self):
        self.assertEqual(find_password('abc'), '18f47a30')
