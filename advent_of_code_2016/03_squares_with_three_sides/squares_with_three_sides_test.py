import unittest

from squares_with_three_sides_part1 import valid_triangles
from squares_with_three_sides_part2 import valid_triangles as valid_vertical_triangles


class Part1TestCase(unittest.TestCase):

    def test_with_valid_triangles(self):
        count = valid_triangles('16  10  25')
        self.assertEqual(count, 1)

    def test_with_invalid_triangles(self):
        count = valid_triangles('5  10  25')
        self.assertEqual(count, 0)

    def test_with_mixed_triangles(self):
        valid_triangle = '16  10  25'
        invalid_triangle = '5  10  25'
        input_ = '{}\n{}'.format(valid_triangle, invalid_triangle)

        count = valid_triangles(input_)
        self.assertEqual(count, 1)


class Part2TestCase(unittest.TestCase):

    def test_with_valid_triangles(self):
        input_ = '101 301 501\n102 302 502\n103 303 503'

        count = valid_vertical_triangles(input_)
        self.assertEqual(count, 3)

    def test_with_invalid_triangles(self):
        input_ = '5 12 100\n10 50 105\n25 20 503'

        count = valid_vertical_triangles(input_)
        self.assertEqual(count, 0)

    def test_with_mixed_triangles(self):
        input_ = '101 12 100\n102 50 105\n103 20 503'

        count = valid_vertical_triangles(input_)
        self.assertEqual(count, 1)
