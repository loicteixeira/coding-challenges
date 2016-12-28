import unittest

from internet_protocol_v7_part1 import count_ips_with_tls_support


class Part1TestCase(unittest.TestCase):
    def test_count_ips_with_tls_support(self):
        input_ = 'abba[mnop]qrst\nabcd[bddb]xyyx\naaaa[qwer]tyui\nioxxoj[asdfgh]zxcvbn'
        count = count_ips_with_tls_support(input_)

        self.assertEqual(count, 2)
