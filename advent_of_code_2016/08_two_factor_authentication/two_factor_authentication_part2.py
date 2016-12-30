import os

from two_factor_authentication_part1 import Screen as BaseScreen
from two_factor_authentication_part1 import SCREEN_WIDTH, SCREEN_HEIGHT


class Screen(BaseScreen):

    PIXEL_OFF, PIXEL_ON = ' ', '█'

    def show(self):
        rows = (''.join(row) for row in self.pixels)
        return '\n'.join(rows)


def show_message(instructions):
    screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

    for instruction in instructions.splitlines():
        cmd, args = instruction.split(' ', 1)

        if cmd not in Screen.VALID_COMMANDS:
            raise ValueError('Invalid Command `{}`'.format(cmd))

        method = getattr(screen, cmd)
        method(args)

    return screen.show()

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.read()

    message = show_message(data)
    print('The screen reads:\n{}'.format(message))
