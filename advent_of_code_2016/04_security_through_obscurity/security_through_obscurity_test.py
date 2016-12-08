import unittest

from security_through_obscurity_part1 import is_room_valid, valid_rooms_sum
from security_through_obscurity_part2 import decrypt_room_name, storage_room_id


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


class Part2TestCase(unittest.TestCase):
    def test_decrypt_room_name(self):
        encrypted_name = 'qzmt-zixmtkozy-ivhz'
        shift = 343
        expected_name = 'very encrypted name'

        self.assertEqual(decrypt_room_name(encrypted_name, shift), expected_name)

    def test_storage_room_id_with_existing_room(self):
        input_ = (
            'qzchnzbshud-cxd-trdq-sdrshmf-105[jqexn]\n'  # => radioactive dye user testing
            'molgbzqfib-bdd-mrozexpfkd-289[bdfmo]'  # => projectile egg purchasing
        )
        room_to_find = 'projectile egg purchasing'

        self.assertEqual(storage_room_id(input_, room_to_find), 289)

    def test_storage_room_id_with_non_existing_room(self):
        input_ = (
            'qzchnzbshud-cxd-trdq-sdrshmf-105[jqexn]\n'  # => radioactive dye user testing
            'molgbzqfib-bdd-mrozexpfkd-289[bdfmo]'  # => projectile egg purchasing
        )
        room_to_find = 'laundry'

        self.assertIsNone(storage_room_id(input_, room_to_find))
