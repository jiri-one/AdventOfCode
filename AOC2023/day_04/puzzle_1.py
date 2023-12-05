from pathlib import Path
import numpy as np
from sys import argv

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 13

if len(argv) > 1 and argv[1] == "--test":
    main_input = test_input

# helper variables
total_points = 0
# read the initial file
with open(main_input, "r") as file:
    while line := file.readline():
        line = line.strip()
        card = int(line.split(":")[0].removeprefix("Card "))
        part1, part2 = line.split(":")[1].split("|")
        win_numbers: set = set(int(n) for n in part1.strip().split())
        my_numbers: set = set(int(n) for n in part2.strip().split())
        common_numbers: set = win_numbers.intersection(my_numbers)
        if len(common_numbers) == 1:
            points = 1
        elif len(common_numbers) > 1:
            points = 2 ** (len(common_numbers)-1)
        else:
            points = 0
        total_points += points

print(total_points)
print("__________________________")
