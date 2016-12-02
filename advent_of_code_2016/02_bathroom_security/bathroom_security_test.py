import unittest

from bathroom_security_part1 import find_code as find_code_simple_keyboard
from bathroom_security_part2 import find_code as find_code_complex_keyboard


class Part1TestCase(unittest.TestCase):

    def test_find_code(self):
        instructions = 'ULL\nRRDDD\nLURDL\nUUUUD'
        expected = '1985'
        code = find_code_simple_keyboard(instructions)

        self.assertEqual(code, expected)


class Part2TestCase(unittest.TestCase):

    def test_find_code(self):
        instructions = 'ULL\nRRDDD\nLURDL\nUUUUD'
        expected = '5DB3'
        code = find_code_complex_keyboard(instructions)

        self.assertEqual(code, expected)
