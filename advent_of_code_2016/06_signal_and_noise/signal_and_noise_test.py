import unittest

from signal_and_noise_part1 import find_message as find_repetition_code_message
from signal_and_noise_part2 import find_message as find_modified_repetition_code_message


class Part1TestCase(unittest.TestCase):
    def test_find_message(self):
        input_ = (
            'eedadn\ndrvtee\neandsr\nraavrd\natevrs\ntsrnev\nsdttsa\nrasrtv\n'
            'nssdts\nntnada\nsvetve\ntesnvt\nvntsnd\nvrdear\ndvrsen\nenarar')
        msg = find_repetition_code_message(input_)

        self.assertEqual(msg, 'easter')


class Part2TestCase(unittest.TestCase):
    def test_find_message(self):
        input_ = (
            'eedadn\ndrvtee\neandsr\nraavrd\natevrs\ntsrnev\nsdttsa\nrasrtv\n'
            'nssdts\nntnada\nsvetve\ntesnvt\nvntsnd\nvrdear\ndvrsen\nenarar')
        msg = find_modified_repetition_code_message(input_)

        self.assertEqual(msg, 'advent')
