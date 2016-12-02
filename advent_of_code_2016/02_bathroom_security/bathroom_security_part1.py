import os

KEYBOARD_SHAPE = (
    '123',
    '456',
    '789'
)
KEYBOARD_DEFAULT = (1, 1)


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def __str__(self):
        return '({x}, {y})'.format(x=self.x, y=self.y)


class Keyboard:

    MOVES = {
        'U': Point(-1, 0),
        'D': Point(1, 0),
        'L': Point(0, -1),
        'R': Point(0, 1)
    }

    def __init__(self, shape, starting_position):
        self.shape = shape
        self.cursor = Point(*starting_position)

    def is_cursor_valid(self, cursor):
        valid_line = 0 <= cursor.x < len(self.shape)
        if not valid_line:
            return False

        valid_column = 0 <= cursor.y < len(self.shape[cursor.x])
        if not valid_column:
            return False

        return True

    def move(self, direction):
        if direction not in Keyboard.MOVES:
            raise ValueError('Invalid move `{}`'.format(direction))

        new_cursor = self.cursor + Keyboard.MOVES[direction]
        if self.is_cursor_valid(new_cursor):
            self.cursor = new_cursor

    def select(self):
        return self.shape[self.cursor.x][self.cursor.y]


def find_code(instructions):

    keyboard = Keyboard(KEYBOARD_SHAPE, KEYBOARD_DEFAULT)
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
