import unittest

from integer_to_currency import to_currency


class IntegerToCurrencyTestCase(unittest.TestCase):

    def test_to_currency(self):
        self.assertEqual(to_currency(123), "123")
        self.assertEqual(to_currency(1234), "1,234")
        self.assertEqual(to_currency(123456), "123,456")
        self.assertEqual(to_currency(12345678), "12,345,678")
        self.assertEqual(to_currency(123456789), "123,456,789")
