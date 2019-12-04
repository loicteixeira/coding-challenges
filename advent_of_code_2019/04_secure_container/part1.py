from pathlib import Path
from typing import Callable, Iterable


def is_valid_password(password: int) -> bool:
    digits = map(int, str(password))

    previous_digit = 0
    has_same_adjacent_digits = False
    for digit in digits:
        # Equal adjacent digits
        if digit == previous_digit:
            has_same_adjacent_digits = True

        # Never decrease
        if digit < previous_digit:
            return False
        previous_digit = digit

    return has_same_adjacent_digits


def valid_passwords_in_range(
    inputs: str, validation: Callable = is_valid_password
) -> Iterable[int]:
    lower_bound, upper_bound = map(int, inputs.split("-"))
    password_candidates = range(lower_bound, upper_bound + 1)
    return filter(validation, password_candidates)


if __name__ == "__main__":
    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, "r") as fh:
        data = fh.readlines()

    valid_password = list(valid_passwords_in_range(data[0]))
    print(f"There are `{len(valid_password)}` valid password within the given range")
