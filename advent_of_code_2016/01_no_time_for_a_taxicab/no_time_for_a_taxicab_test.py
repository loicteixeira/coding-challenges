import unittest

from no_time_for_a_taxicab_part1 import distance
from no_time_for_a_taxicab_part2 import distance_to_first_intersection


class Part1TestCase(unittest.TestCase):

    def test_distance(self):
        values = (
            ('R2, L3', 5),
            ('R2, L12', 14),
            ('R2, R2, R2', 2),
            ('R5, L5, R5, R3', 12),
        )

        for input_, expected in values:
            self.assertEqual(distance(input_), expected)


class Part2TestCase(unittest.TestCase):

    def test_distance_to_first_intersection(self):
        self.assertEqual(distance_to_first_intersection('R8, R4, R4, R8'), 4)
