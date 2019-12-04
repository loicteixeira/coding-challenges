from collections import defaultdict
from pathlib import Path

from part1 import valid_passwords_in_range


def is_valid_password(password: int) -> bool:
    digits = map(int, str(password))

    previous_digit = 0
    same_adjacent_digits = defaultdict(lambda: 1)
    for digit in digits:
        # Equal adjacent digits
        if digit == previous_digit:
            same_adjacent_digits[digit] += 1

        # Never decrease
        if digit < previous_digit:
            return False
        previous_digit = digit

    doubles = [digit for digit, count in same_adjacent_digits.items() if count == 2]
    return len(doubles) > 0


if __name__ == "__main__":
    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, "r") as fh:
        data = fh.readlines()

    valid_password = list(valid_passwords_in_range(data[0], is_valid_password))
    print(f"There are `{len(valid_password)}` valid password within the given range")
