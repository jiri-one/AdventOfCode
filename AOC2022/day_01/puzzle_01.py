from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is XXXX
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 24000

# helper variables
most_calories = 0
actual_calories = 0

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if len(line) != 0:
            actual_calories += int(line)
        else:
            if actual_calories > most_calories:
                most_calories = actual_calories
            actual_calories = 0

if actual_calories > most_calories:
    most_calories = actual_calories

print(most_calories)
