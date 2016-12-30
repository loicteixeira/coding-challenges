import itertools
import os
import re

SCREEN_WIDTH = 50
SCREEN_HEIGHT = 6


class Screen:

    PIXEL_OFF, PIXEL_ON = 0, 1
    VALID_COMMANDS = ('rect', 'rotate')
    RECT_CMD_ARGS_PATTERN = re.compile(r'(?P<width>\d+)x(?P<height>\d+)')
    ROTATE_CMD_ARGS_PATTERN = re.compile(
        r'(?P<axis>(?:row|column))'
        r'\s[xy]='
        r'(?P<idx>\d+)'
        r'\sby\s'
        r'(?P<amount>\d+)'
    )

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[self.PIXEL_OFF for _ in range(width)] for _ in range(height)]

    def rect(self, args):
        match = self.RECT_CMD_ARGS_PATTERN.match(args)
        if not match:
            raise ValueError('Invalid arguments `{}`'.format(args))

        width, height = map(int, match.group('width', 'height'))
        pixels_to_lit = itertools.product(range(height), range(width))
        for x, y in pixels_to_lit:
            self.pixels[x][y] = self.PIXEL_ON

    def rotate(self, args):
        match = self.ROTATE_CMD_ARGS_PATTERN.match(args)
        if not match:
            raise ValueError('Invalid arguments `{}`'.format(args))

        axis = match.group('axis')
        idx, amount = map(int, match.group('idx', 'amount'))

        if axis == 'row':
            self.pixels[idx] = self.pixels[idx][-amount:] + self.pixels[idx][:-amount]

        elif axis == 'column':
            # Extract column values, shift and apply.
            column_values = [self.pixels[x][idx] for x in range(self.height)]
            column_values = column_values[-amount:] + column_values[:-amount]
            for x in range(self.height):
                self.pixels[x][idx] = column_values[x]

    def get_lit_pixels_count(self):
        pixels = itertools.chain.from_iterable(self.pixels)
        count = sum(pixels)

        return count


def count_lit_pixels(instructions):
    screen = Screen(SCREEN_WIDTH, SCREEN_HEIGHT)

    for instruction in instructions.splitlines():
        cmd, args = instruction.split(' ', 1)

        if cmd not in Screen.VALID_COMMANDS:
            raise ValueError('Invalid Command `{}`'.format(cmd))

        method = getattr(screen, cmd)
        method(args)

    return screen.get_lit_pixels_count()

if __name__ == '__main__':
    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.read()

    count = count_lit_pixels(data)
    print('There are {} lit pixels on the screen'.format(count))
