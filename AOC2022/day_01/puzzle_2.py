from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 199628
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 45000

# helper variables
calories = []
actual_calories = 0

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if len(line) != 0:
            actual_calories += int(line)
        else:
            calories.append(actual_calories)
            actual_calories = 0

# for last elf, which is not ended by empty line
calories.append(actual_calories)

total_calories = 0
for cal in sorted(calories)[-3:]:
    total_calories += cal

print(total_calories)
