from pathlib import Path
from sys import argv, exit

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 54338
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 142

if len(argv) > 1 and argv[1] == "--test":
    main_input = test_input

# helper variables
values = []

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if len(line) != 0:
            for char in line:
                try:
                    value_1 = int(char)
                    break
                except ValueError:
                    pass
            for char in reversed(line):
                try:
                    value_2 = int(char)
                    break
                except ValueError:
                    pass
            values.append(int(f"{value_1}{value_2}"))

print(sum(values))
