import os

from security_through_obscurity_part1 import is_room_valid, ROOM_PATTERN

ORD_FIRST_LOWERCASE_LETTER = 97
ORD_DASH = 45
ORD_SPACE = 32
ALPHABET_LENGTH = 26
STORAGE_ROOM_NAME = 'northpole object storage'


def decrypt_room_name(name, shift):

    ords = (ord(letter) for letter in name)
    shifted_ords = (
        # Basically `(ord + shift) % alphabet_length`
        # with -/+ first ord letter to start at 0.
        (o - ORD_FIRST_LOWERCASE_LETTER + shift) % ALPHABET_LENGTH + ORD_FIRST_LOWERCASE_LETTER

        # Dashes do not get shifted but replaced with spaces.
        if o != ORD_DASH else ORD_SPACE

        for o in ords
    )
    shifted_letters = (chr(so) for so in shifted_ords)

    return ''.join(shifted_letters).strip()


def valid_rooms(rooms):
    for room in rooms.splitlines():
        matches = ROOM_PATTERN.search(room)
        if not matches:
            continue

        name, id_, checksum = matches.groups()
        if not is_room_valid(name, checksum):
            continue

        yield name, int(id_), checksum


def storage_room_id(rooms, storage_room_name=STORAGE_ROOM_NAME):

    for room_name, room_id, _ in valid_rooms(rooms):
        decrypted_name = decrypt_room_name(room_name, room_id)

        if decrypted_name == storage_room_name:
            return room_id

if __name__ == '__main__':

    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.read()

    room_id = storage_room_id(data)
    if room_id:
        print('The storage room ID is {}.'.format(room_id))
    else:
        print("Couldn't find the `{}` room".format(STORAGE_ROOM_NAME))
