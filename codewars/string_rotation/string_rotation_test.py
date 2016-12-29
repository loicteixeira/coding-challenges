import unittest

from string_rotation import shifted_diff


class StringRotationTestCase(unittest.TestCase):
    def test_valid_rotation(self):
        rotation = shifted_diff("coffee", "eecoff")
        self.assertEqual(rotation, 2)

        rotation = shifted_diff("eecoff", "coffee")
        self.assertEqual(rotation, 4)

    def test_valid_rotation_with_special_characters(self):
        rotation = shifted_diff("isn't", "'tisn")
        self.assertEqual(rotation, 2)

    def test_with_no_rotation(self):
        rotation = shifted_diff("Esham", "Esham")
        self.assertEqual(rotation, 0)

    def test_invalid_rotation(self):
        rotation = shifted_diff("Moose", "moose")
        self.assertEqual(rotation, -1)
