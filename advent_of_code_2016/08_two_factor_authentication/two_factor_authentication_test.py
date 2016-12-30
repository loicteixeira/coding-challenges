import unittest

from two_factor_authentication_part1 import count_lit_pixels


class Part1TestCase(unittest.TestCase):
    def test_count_lit_pixels(self):
        input_ = (
            'rect 3x2\n'
            'rotate column x=1 by 1\n'
            'rotate row y=0 by 4\n'
            'rotate column x=1 by 1'
        )
        count = count_lit_pixels(input_)

        self.assertEqual(count, 6)
