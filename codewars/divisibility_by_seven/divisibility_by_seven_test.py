import unittest

from divisibility_by_seven import seven


class DivisibilityBySevenTestCase(unittest.TestCase):

    def test_with_small_inputs(self):
        self.assertEqual(seven(35), (35, 0))

    def test_with_medium_inputs(self):
        self.assertEqual(seven(371), (35, 1))
        self.assertEqual(seven(1603), (7, 2))

    def test_with_large_inputs(self):
        self.assertEqual(seven(477557101), (28, 7))
