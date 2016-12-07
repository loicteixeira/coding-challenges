import itertools
import re
import os


# From https://docs.python.org/3/library/itertools.html#itertools-recipes
def grouper(iterable, n, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    args = [iter(iterable)] * n
    return itertools.zip_longest(*args, fillvalue=fillvalue)


def is_triangle_valid(sides):
    # Instead of checking all three combinations (i.e. `a + b > c`, `b + c > a` and `c + a > b`),
    # with `a >= b >= c`, it is only needed to check `a + b > c`.
    sides = sorted(map(int, sides))
    return sides[0] + sides[1] > sides[2]


def valid_triangles(input_):

    count = 0

    # Group lines by 3.
    lines = input_.splitlines()
    groups = grouper(lines, 3)

    for group in groups:
        # Extract numbers for each line and transpose the list.
        group_sides = map(lambda g: re.findall('\d+', g), group)
        transposed_group = zip(*group_sides)

        # Check validity.
        for triangle in transposed_group:
            if is_triangle_valid(triangle):
                count += 1

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
