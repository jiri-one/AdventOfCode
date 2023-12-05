from pathlib import Path
import numpy as np
from sys import argv

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 72553319
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 467835

if len(argv) > 1 and argv[1] == "--test":
    main_input = test_input

# helper variables

# read the initial file
with open(main_input, "r") as file:
    while line := file.readline():
        line = line.strip()
        new_line = []
        for char in line:
            if char == ".":
                char = None
            else:
                try:
                    char = int(char)
                except ValueError:
                    pass
            new_line.append(char)
        try:
            arr = np.vstack((arr, np.array([x for x in new_line], dtype=object)))
        except NameError:
            arr = np.array([x for x in new_line], dtype=object)

size = np.shape(arr.T)
print(size)

print(arr)
x_indexes = []
number = ""
y_index = None
engine_parts: dict[tuple[int, int], list] = dict() # dict where key is asterisk coordinates and value is the list of part numbers
with np.nditer(arr.T, flags=["multi_index", "refs_ok"]) as ar:
    for elm in ar:
        x, y = ar.multi_index
        element = arr.T[x][y]
        if isinstance(element, int):
            x_indexes.append(x)
            y_index = y
            number += str(element)
        if x_indexes and not isinstance(element, int):
            # try surroundings of number (x_indexes) and reset indexes (x and y)
            check_this_coor: set[tuple[int, int]] = set()
            # create coordinates to check
            for x_index in x_indexes:
                if x_index != 0:
                    check_this_coor.add((x_index-1, y))
                if x_index != 0 and y_index != 0:
                    check_this_coor.add((x_index-1, y-1))
                if x_index != 0 and y_index < size[1]-1:
                    check_this_coor.add((x_index-1, y+1))
                if y_index != 0:
                    check_this_coor.add((x_index, y-1))
                if y_index < size[1]-1:
                    check_this_coor.add((x_index, y+1))
                if x_index < size[0]-1:
                    check_this_coor.add((x_index+1, y))
                if x_index < size[0]-1 and y_index != 0:
                    check_this_coor.add((x_index+1, y-1))
                if x_index < size[0]-1 and y_index < size[1]-1:
                    check_this_coor.add((x_index+1, y+1))
            # check the coordinates, which are surrounding one part of number
            for coor in check_this_coor:
                x, y = coor
                if isinstance(arr.T[x][y], str) and arr.T[x][y] == "*":
                    if engine_parts.get(coor, None):
                        engine_parts[coor].append(int(number))
                    else:
                        engine_parts[coor] = [int(number)]
            x_indexes = list()
            number = ""
            y_index = None

parts = []
for coor, part_list in engine_parts.items():
    if len(part_list) == 2:
        parts.append(part_list[0] * part_list[1])

print(sum(parts))
