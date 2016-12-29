import unittest

from hello_world import greet


class HelloWorldTestCase(unittest.TestCase):

    def test_with_empty_name(self):
        greeting = greet()
        self.assertEqual(greeting, 'Hello World!')

    def test_with_given_name(self):
        greeting = greet('Guido')
        self.assertEqual(greeting, 'Hello Guido!')
