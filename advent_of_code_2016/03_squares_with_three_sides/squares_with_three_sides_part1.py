import os
import re


def is_triangle_valid(triangle):
    sides = re.findall('\d+', triangle)
    if not sides or len(sides) != 3:
        return False

    # Instead of checking all three combinations (i.e. `a + b > c`, `b + c > a` and `c + a > b`),
    # with `a >= b >= c`, it is only needed to check `a + b > c`.
    sides = sorted(map(int, sides))
    return sides[0] + sides[1] > sides[2]


def valid_triangles(input_):

    count = sum(
        is_triangle_valid(triangle)
        for triangle in input_.splitlines()
    )

    return count

if __name__ == '__main__':

    directory = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(directory, 'input.txt')
    with open(file_path, 'r') as f:
        data = f.read()

    count = valid_triangles(data)
    if count:
        print('There are {} valid triangle(s).'.format(count))
    else:
        print('There is no valid triangles :(')
