from pathlib import Path
from typing import Iterator

import pytest

from part1 import mass_to_fuel


@pytest.mark.parametrize(
    "fuel_mass,expected_additional_fuel_requirement", [(2, 0), (654, 312), (33583, 16763)]
)
def test_fuel_for_added_fuel(fuel_mass, expected_additional_fuel_requirement):
    assert fuel_for_added_fuel(fuel_mass) == expected_additional_fuel_requirement


@pytest.mark.parametrize(
    "modules_mass,expected_fuel_requirement", [(12, 2), (14, 2), (1969, 966), (100756, 50346)]
)
def test_total_fuel_required(modules_mass, expected_fuel_requirement):
    assert total_fuel_required([modules_mass]) == expected_fuel_requirement


def fuel_for_added_fuel(fuel_mass: int) -> int:
    total = 0
    while (fuel_mass := mass_to_fuel(fuel_mass)) > 0:
        total += fuel_mass
    return total


def total_fuel_required(masses: Iterator[int]) -> int:
    total = 0
    for mass in masses:
        module_fuel = mass_to_fuel(int(mass))
        total += module_fuel
        fuel_fuel = fuel_for_added_fuel(module_fuel)
        total += fuel_fuel
    return total


if __name__ == "__main__":
    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, "r") as fh:
        data = fh.readlines()

    total_fuel = total_fuel_required(map(int, data))

    print(
        "The sum of the fuel requirements for all of the modules on the spacecraft"
        f"when also taking into account the mass of the added fuel is: {total_fuel}"
    )
