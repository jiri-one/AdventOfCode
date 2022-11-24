import numpy as np
from pathlib import Path
main_input = Path(__file__).parent / "input.txt"
test_input = Path(__file__).parent / "test_input.txt"

fold = {}
highest_x = 0
highest_y = 0
sharps = []
with open(test_input, "r") as file:
    fold_counter = 1
    for line in file:
        line = line.strip()
        if line: # remove empty line
            if "fold" in line:
                axis, fold_value = line.split("=")
                fold[fold_counter] = (axis[-1], int(fold_value))
                fold_counter += 1
            else:
                x, y = line.split(",")
                x, y = int(x), int(y)
                sharps.append((x, y))
                if x > highest_x: highest_x = x
                if y > highest_y: highest_y = y

array = np.full((highest_y+1,highest_x+1), ".", dtype=str)
for sharp in sharps:
    array[sharp[1]][sharp[0]] = "X"
print(array)
