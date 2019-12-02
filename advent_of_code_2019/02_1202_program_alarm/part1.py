from operator import add, mul
from pathlib import Path

import pytest


@pytest.mark.parametrize(
    "input_data,expected_output",
    [
        ([1, 0, 0, 0, 99], [2, 0, 0, 0, 99]),
        ([2, 3, 0, 3, 99], [2, 3, 0, 6, 99]),
        ([2, 4, 4, 5, 99, 0], [2, 4, 4, 5, 99, 9801]),
        ([1, 1, 1, 4, 99, 5, 6, 0, 99], [30, 1, 1, 4, 2, 5, 6, 0, 99]),
    ],
)
def test_single_instruction(input_data, expected_output):
    interpreter = IntcodeInterpreter(input_data)
    assert interpreter.run() == expected_output


@pytest.mark.parametrize(
    "input_data,expected_output",
    [([1, 9, 10, 3, 2, 3, 11, 0, 99, 30, 40, 50], [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50])],
)
def test_multiple_instructions(input_data, expected_output):
    interpreter = IntcodeInterpreter(input_data)
    assert interpreter.run() == expected_output


class IntcodeInterpreter:
    opcode_map = {
        1: add,
        2: mul,
        99: None,
    }

    def __init__(self, program):
        self.program = program
        self.cursor = 0
        self.instruction_size = 4

    def current_operation(self):
        opcode = self.program[self.cursor]

        return self.opcode_map[opcode]

    def instructions_set(self):
        while (operation := self.current_operation()) is not None:
            first_operand_index = self.program[self.cursor + 1]
            second_operand_index = self.program[self.cursor + 2]
            output_index = self.program[self.cursor + 3]

            yield operation, self.program[first_operand_index], self.program[
                second_operand_index
            ], output_index

            self.step()

    def step(self):
        self.cursor += self.instruction_size

    def run(self):
        for operation, first_operand, second_operand, output_index in self.instructions_set():
            self.program[output_index] = operation(first_operand, second_operand)

        return self.program


if __name__ == "__main__":
    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, "r") as fh:
        data = fh.readline()

    data = list(map(int, data.split(",")))
    data[1] = 12
    data[2] = 2
    interpreter = IntcodeInterpreter(data)
    result = interpreter.run()

    print(f"After the program halts, the value left at position `0` is: `{result[0]}`")
