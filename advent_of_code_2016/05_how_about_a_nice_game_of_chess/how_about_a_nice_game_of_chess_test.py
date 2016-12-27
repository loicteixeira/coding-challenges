import unittest

from how_about_a_nice_game_of_chess_part1 import find_password
from how_about_a_nice_game_of_chess_part2 import find_password as find_complex_password


class Part1TestCase(unittest.TestCase):
    def test_find_password(self):
        self.assertEqual(find_password('abc'), '18f47a30')


class Part2TestCase(unittest.TestCase):
    def test_find_password(self):
        self.assertEqual(find_complex_password('abc'), '05ace8e3')
