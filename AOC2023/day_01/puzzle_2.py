from pathlib import Path
from sys import argv

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 53389
test_input = Path(__file__).parent / "test_input_2.txt"  # result of this file is 281

if len(argv) > 1 and argv[1] == "--test":
    main_input = test_input

# helper variables
digits = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
values = []

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if len(line) != 0:
            possible_digit_1 = ""
            for char in line:
                try:
                    value_1 = int(char)
                    break
                except ValueError:
                    possible_digit_1 += char
                    for digit, number in digits.items():
                        if digit in possible_digit_1:
                            value_1 = number
                            break
                    else:
                        continue
                    break

            possible_digit_2 = ""
            for char in reversed(line):
                try:
                    value_2 = int(char)
                    break
                except ValueError:
                    possible_digit_2 = char + possible_digit_2
                    for digit, number in digits.items():
                        if digit in possible_digit_2:
                            value_2 = number
                            break
                    else:
                        continue
                    break
            values.append(int(f"{value_1}{value_2}"))

print(sum(values))
