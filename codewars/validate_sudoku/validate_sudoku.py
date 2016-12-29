import itertools

VALID_NUMBERS = set(range(1, 10))


def valid_row(row):
    diff = VALID_NUMBERS - set(row)
    return len(diff) == 0


def valid_solution(grid):

    # Rows
    rows = grid
    if not all(map(valid_row, rows)):
        return False

    # Columns
    cols = zip(*rows)
    if not all(map(valid_row, cols)):
        return False

    # 3x3 Blocks
    # Where i and j are the starting position of each 3x3 block in the 9x9 grid,
    # and r, c the row and column index within that 3x3 block.
    for i, j in itertools.product(range(0, 9, 3), repeat=2):
        block = (
            grid[i + r][j + c]
            for r, c in itertools.product(range(3), repeat=2)
        )

        if not valid_row(block):
            return False

    return True
