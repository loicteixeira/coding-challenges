import unittest

from squares_with_three_sides_part1 import valid_triangles


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
