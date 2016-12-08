import unittest

from security_through_obscurity_part1 import is_room_valid, valid_rooms_sum


class Part1TestCase(unittest.TestCase):
    def test_is_room_valid_returns_true_for_valid_rooms(self):
        values = (
            ('aaaaa-bbb-z-y-x', 'abxyz'),  # aaaaa-bbb-z-y-x-123[abxyz]
            ('a-b-c-d-e-f-g-h', 'abcde'),  # a-b-c-d-e-f-g-h-987[abcde]
            ('not-a-real-room', 'oarel'),  # not-a-real-room-404[oarel]
        )

        for room_name, checksum in values:
            self.assertTrue(
                is_room_valid(room_name, checksum))

    def test_is_room_valid_returns_false_for_invalid_rooms(self):
        values = (
            ('aaaaa-bbb-z-y-x', 'axyzb'),  # aaaaa-bbb-z-y-x-123[axyzb], same as first valid example but bad checksum
            ('totally-real-room', 'decoy'),  # totally-real-room-200[decoy]
        )

        for room_name, checksum in values:
            self.assertFalse(
                is_room_valid(room_name, checksum))

    def test_valid_rooms_sum(self):
        input_ = 'aaaaa-bbb-z-y-x-123[abxyz]\ntotally-real-room-200[decoy]'

        self.assertEqual(valid_rooms_sum(input_), 123)
