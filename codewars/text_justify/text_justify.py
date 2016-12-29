import functools
import math
import re

NEW_LINE = '\n'
SPACE = ' '


def justify(text, width):
    # Would use r'(?<=\s|^).{1,%i}(?=\s|$)'
    # if python's positive lookahead was supporting non-fixed-width patterns.
    pattern = r'[\s^]?(.{1,%i})(?=\s|$)' % width
    lines = re.findall(pattern, text)

    # Justify all but last line.
    func = functools.partial(justify_line, width=width)
    lines[:-1] = map(func, lines[:-1])

    return NEW_LINE.join(lines)


def justify_line(raw_line, width):
    line = ''
    words = raw_line.split(' ')
    missing_spaces = width - len(raw_line.replace(' ', ''))

    for i, word in enumerate(words):
        line += word

        words_left = len(words) - i - 1
        if words_left != 0:
            spaces_to_add = int(math.ceil(float(missing_spaces) / words_left))
            missing_spaces -= spaces_to_add
            line += SPACE * spaces_to_add

    return line
