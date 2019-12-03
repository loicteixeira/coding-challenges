from pathlib import Path

import pytest

from part1 import get_visited


@pytest.mark.parametrize(
    "wires_inputs,expected_distance",
    [
        (["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"], 610),
        (
            ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"],
            410,
        ),
    ],
)
def test_steps_to_closest_intersection(wires_inputs, expected_distance):
    assert steps_to_closest_intersection(wires_inputs) == expected_distance


def steps_to_closest_intersection(inputs):
    visited_by_first_wire, visited_by_second_wire = map(get_visited, inputs)
    intersections = visited_by_first_wire.keys() & visited_by_second_wire.keys()

    return min(
        visited_by_first_wire[point] + visited_by_second_wire[point] for point in intersections
    )


if __name__ == "__main__":
    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, "r") as fh:
        data = fh.readlines()

    closest_steps = steps_to_closest_intersection(data)
    print(
        f"The fewest combined steps the wires must take to reach an intersection `{closest_steps}`."
    )
