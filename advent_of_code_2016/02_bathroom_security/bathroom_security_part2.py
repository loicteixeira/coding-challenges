import os

from bathroom_security_part1 import Keyboard as BaseKeyboard

KEYBOARD_SHAPE = (
    '  1  ',
    ' 234 ',
    '56789',
    ' ABC ',
    '  D  '
)
KEYBOARD_DEFAULT = (2, 0)
KEYBOARD_INVALID_VALUES = ' ',


class Keyboard(BaseKeyboard):

    def __init__(self, shape, starting_position, invalid_values):
        super().__init__(shape, starting_position)

        self.invalid_values = invalid_values

    def is_cursor_valid(self, cursor):
        in_bounds = super().is_cursor_valid(cursor)
        return in_bounds and self.shape[cursor.x][cursor.y] not in self.invalid_values


def find_code(instructions):

    keyboard = Keyboard(KEYBOARD_SHAPE, KEYBOARD_DEFAULT, KEYBOARD_INVALID_VALUES)
    code = ''

    for digit_instructions in instructions.splitlines():
        for move_direction in digit_instructions:
            keyboard.move(move_direction)

        code += keyboard.select()

    return code

if __name__ == '__main__':

    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.read()

    code = find_code(data)
    print('The code to the bathroom is `{}`'.format(code))
