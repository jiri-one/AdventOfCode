from pathlib import Path
from string import ascii_lowercase, ascii_uppercase

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 7872
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 157


# helper functions
def create_priority_dict():
    priority: dict[str, int] = {}
    priority_level_range = range(1, len(ascii_lowercase + ascii_uppercase) + 1)
    for prior, char in zip(priority_level_range, ascii_lowercase + ascii_uppercase):
        priority[char] = prior
    return priority


# helper variables
priority: dict[str, int] = create_priority_dict()
total_score: int = 0

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            half_len = int(len(line) / 2)
            one_half, sec_half = line[:half_len], line[half_len:]
            for char in one_half:
                if char in sec_half:
                    total_score += priority[char]
                    break  # there is more occurrences

print(total_score)
