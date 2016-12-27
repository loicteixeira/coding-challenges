import hashlib
import itertools
import random

from how_about_a_nice_game_of_chess_part1 import get_hash, PASSWORD_LENGTH

FAKE_CHARS = '0123456789abcdef'
VALID_HASH_PREFIX = '00000'
PASSWORD_POSITION_INDEX = 5
PASSWORD_CHARACTER_INDEX = 6


def print_progress(characters):
    password = ''.join(
        c if c else random.choice(FAKE_CHARS)
        for c in characters
    )
    found = PASSWORD_LENGTH - characters.count(None)

    progress = '[{found}/{length}] {password}\r'.format(
        found=found, length=PASSWORD_LENGTH, password=password
    )
    print(progress, end='')


def is_valid_hash(hash_):
    if not hash_.startswith(VALID_HASH_PREFIX):
        return False

    try:
        position = int(hash_[PASSWORD_POSITION_INDEX])
    except ValueError:
        return False

    return position < PASSWORD_LENGTH


def find_password(door_id, show_progress=False):
    characters = [None] * PASSWORD_LENGTH

    for i in itertools.count():
        # Do not show progress on each loop to not overload the console.
        if show_progress and i % 5000 == 0:
            print_progress(characters)

        h = get_hash(door_id, i)

        if not is_valid_hash(h):
            continue

        position = int(h[PASSWORD_POSITION_INDEX])
        if characters[position]:
            continue  # Position has already been filled.

        characters[position] = h[PASSWORD_CHARACTER_INDEX]

        # Update progress as a new character is found.
        if show_progress:
            print_progress(characters)

        if all(characters):  # All characters have been found (no None left).
            password = ''.join(characters)
            return password

if __name__ == '__main__':
    door_id = 'ojvtpuvg'
    password = find_password(door_id, show_progress=True)
    print('The password to the door `{}` is `{}`'.format(door_id, password))
