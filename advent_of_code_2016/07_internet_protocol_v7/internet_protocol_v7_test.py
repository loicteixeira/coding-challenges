import unittest

from internet_protocol_v7_part1 import count_ips_with_tls_support
from internet_protocol_v7_part2 import count_ips_with_ssl_support


class Part1TestCase(unittest.TestCase):
    def test_count_ips_with_tls_support(self):
        input_ = 'abba[mnop]qrst\nabcd[bddb]xyyx\naaaa[qwer]tyui\nioxxoj[asdfgh]zxcvbn'
        count = count_ips_with_tls_support(input_)

        self.assertEqual(count, 2)


class Part2TestCase(unittest.TestCase):
    def test_count_ips_with_ssl_support(self):
        input_ = 'aba[bab]xyz\nxyx[xyx]xyx\naaa[kek]eke\nzazbz[bzb]cdb'
        count = count_ips_with_ssl_support(input_)

        self.assertEqual(count, 3)
