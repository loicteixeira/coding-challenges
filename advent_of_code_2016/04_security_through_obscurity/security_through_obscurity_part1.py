import collections
import os


def is_room_valid(room_name, checksum):

    room_name = room_name.replace('-', '')

    letters_count = collections.Counter(room_name).items()
    ordered_letters_count = sorted(
        letters_count,
        key=lambda l_c: (-l_c[1], l_c[0])  # Order by count DESC and letter ASC
    )

    ordered_letters = [letter for letter, _ in ordered_letters_count][:len(checksum)]
    calculated_checksum = ''.join(ordered_letters)

    return calculated_checksum == checksum


def valid_rooms_sum(data):
    pass


if __name__ == '__main__':

    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.read()

    sum_ = valid_rooms_sum(data)
    print('The sum of the sector IDs of the real rooms is {}.'.format(sum_))
