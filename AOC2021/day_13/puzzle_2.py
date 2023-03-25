import numpy as np
from pathlib import Path

# input files
# result of this file is "LRGPRECB" in file puzzle2_output.txt
main_input = Path(__file__).parent / "input.txt"
# result of this file is "O" in file puzzle2_test_output.txt
test_input = Path(__file__).parent / "test_input.txt"

# helper variables
fold: dict[int, tuple[str, int]] = {}  # fold dict
highest_x: int = 0
highest_y: int = 0
sharps: list[tuple[int, int]] = []  # list of sharps coordinates

with open(main_input, "r") as file:
    fold_counter = 1
    for line in file:
        line = line.strip()
        if line:  # ignore empty lines
            if "fold" in line:
                axis, fold_value = line.split("=")
                fold[fold_counter] = (axis[-1], int(fold_value))
                fold_counter += 1
            else:
                x, y = line.split(",")
                x, y = int(x), int(y)
                sharps.append((x, y))
                if x > highest_x:
                    highest_x = x
                if y > highest_y:
                    highest_y = y
# create array of dots
array = np.full((highest_y + 1, highest_x + 1), ".", dtype=str)
# populate array with #
for sharp in sharps:
    array[sharp[1]][sharp[0]] = "#"

for x in range(1, len(fold) + 1):  # handle all folds
    axis, value = fold[x]
    if axis == "y":
        cut_axis = 0
        split = np.vsplit
        flip = np.flipud
    else:
        cut_axis = 1
        split = np.hsplit
        flip = np.fliplr
    array = np.delete(array, value, cut_axis)  # delete folded row/column
    # this will split arrays to 3 sliced arrays: :value, value:value (empty array), value:
    arrays = split(array, np.array([value, value]))
    # remove empty array
    array1, array2 = [array for array in arrays if np.size(array) != 0]
    array2 = flip(array2)  # mirror/flip second array
    with np.nditer([array1, array2], op_flags=["readwrite"]) as ar:
        for x, y in ar:  # x is from array1, y is from array2
            if y[...] == "#":
                x[...] = "#"
    array = array1

print(array)
