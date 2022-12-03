from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 2497
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 70

# helper functions
def create_priority_dict():
    priority: dict[str, int] = {}
    priority_level_range = range(1,len(ascii_lowercase+ascii_uppercase)+1)
    for prior, char in zip(priority_level_range,
                           ascii_lowercase+ascii_uppercase):
        priority[char] = prior
    return priority

# helper variables
priority: dict[str, int] = create_priority_dict()
total_score: int = 0

# read the initial file
with open(main_input, "r") as file:
    line_counter: int = 0
    three_lines: dict[int, str] = {}
    for line in file:
        line = line.strip()
        if line:
            line_counter += 1
            three_lines[line_counter] = line
            if len(three_lines) == 3:
                for char in three_lines[1]:
                    if char in three_lines[2] and char in three_lines[3]:
                        total_score += priority[char]
                        break
                three_lines = dict()
                line_counter = 0

print(total_score)
