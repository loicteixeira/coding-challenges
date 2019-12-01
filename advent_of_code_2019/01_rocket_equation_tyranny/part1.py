from pathlib import Path
from typing import Iterator

import pytest


@pytest.mark.parametrize(
    "mass,expected_required_fuel", [(12, 2), (14, 2), (1969, 654), (100756, 33583)]
)
def test_mass_to_fuel(mass, expected_required_fuel):
    assert mass_to_fuel(mass) == expected_required_fuel


@pytest.mark.parametrize(
    "module_masses,expected_required_fuel", [([12, 14], 2 + 2), ([1969, 100756], 654 + 33583)]
)
def test_fuel_for_modules(module_masses, expected_required_fuel):
    assert fuel_for_modules(module_masses) == expected_required_fuel


def mass_to_fuel(mass: int) -> int:
    return mass // 3 - 2


def fuel_for_modules(masses: Iterator[int]) -> int:
    return sum(map(mass_to_fuel, masses))


if __name__ == "__main__":
    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, "r") as fh:
        data = fh.readlines()

    total_fuel = fuel_for_modules(map(int, data))
    print(
        f"The sum of the fuel requirements for all of the modules on the spacecraft is: {total_fuel}"
    )
