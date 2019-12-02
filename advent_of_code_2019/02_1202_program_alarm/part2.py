from itertools import combinations
from pathlib import Path

from part1 import IntcodeInterpreter


if __name__ == "__main__":
    input_file_path = Path(__file__).parent / "input.txt"
    with open(input_file_path, "r") as fh:
        data = fh.readline()

    data = list(map(int, data.split(",")))

    for noun, verb in combinations(range(100), 2):
        program_data = data.copy()
        program_data[1] = noun
        program_data[2] = verb
        interpreter = IntcodeInterpreter(program_data)
        program_result = interpreter.run()

        if program_result[0] == 19690720:
            print(f"The pair of inputs produces the output `19690720` are `{noun}` and `{verb}`.")
            result = 100 * noun + verb
            print(f"The final value is `{result}`.")
            break
