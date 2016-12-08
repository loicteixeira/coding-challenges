import hashlib
import itertools

PASSWORD_LENGTH = 8


def print_progress(characters):
    progress = '[{found}/{length}] {password}\r'.format(
        found=len(characters), length=PASSWORD_LENGTH, password=''.join(characters).ljust(PASSWORD_LENGTH, '*')
    )
    print(progress, end='')


def get_hash(door_id, index):
    s = '{door_id}{index}'.format(door_id=door_id, index=index).encode('utf-8')
    h = hashlib.md5(s).hexdigest()

    return h


def find_password(door_id, show_progress=False):
    characters = []

    if show_progress:
        print_progress(characters)

    for i in itertools.count():
        h = get_hash(door_id, i)

        if h.startswith('00000'):
            next_character = h[5]
            characters.append(next_character)

            if show_progress:
                print_progress(characters)

            if len(characters) == PASSWORD_LENGTH:
                password = ''.join(characters)
                return password

if __name__ == '__main__':
    door_id = 'ojvtpuvg'
    password = find_password(door_id, show_progress=True)
    print('The password to the door `{}` is `{}`'.format(door_id, password))
