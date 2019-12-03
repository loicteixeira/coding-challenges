from dataclasses import dataclass
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "wires_inputs,expected_distance",
    [
        (["R75,D30,R83,U83,L12,D49,R71,U7,L72", "U62,R66,U55,R34,D71,R55,D58,R83"], 159),
        (
            ["R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51", "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7"],
            135,
        ),
    ],
)
def test_distance__to_closest_intersection(wires_inputs, expected_distance):
    assert distance_to_closest_intersection(wires_inputs) == expected_distance


@dataclass(frozen=True)
class Vector:
    x: int = 0
    y: int = 0

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


DIRECTION_VECTORS = {
    "R": Vector(1, 0),
    "L": Vector(-1, 0),
    "U": Vector(0, 1),
    "D": Vector(0, -1),
}


def distance_to_closest_intersection(inputs):
    visited_by_first_wire, visited_by_second_wire = map(get_visited, inputs)
    intersections = visited_by_first_wire & visited_by_second_wire
    return min(abs(point.x) + abs(point.y) for point in intersections)


def get_visited(commands):
    position = Vector(0, 0)
    visited = set()

    for command in commands.split(","):
        direction = DIRECTION_VECTORS[command[0]]
        distance = int(command[1:])

        for step in range(distance):
            position = position + direction
            visited.add(position)

    return visited


if __name__ == "__main__":
    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, "r") as fh:
        data = fh.readlines()

    closest_distance = distance_to_closest_intersection(data)
    print(
        "The Manhattan distance from the central port "
        f"to the closest intersection is `{closest_distance}`."
    )
