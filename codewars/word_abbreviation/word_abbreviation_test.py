import unittest

from word_abbreviation import abbreviate


class WordAbbreviationTestCase(unittest.TestCase):

    def test_does_not_abbreviate_short_words(self):
        self.assertEqual(abbreviate('You'), 'You')

    def test_abbreviate_long_words(self):
        self.assertEqual(abbreviate('banana'), 'b4a')

    def test_abbreviate_sentences(self):
        self.assertEqual(abbreviate('double-barrel'), 'd4e-b4l')
        self.assertEqual(abbreviate('You, and I, should speak.'), 'You, and I, s4d s3k.')
