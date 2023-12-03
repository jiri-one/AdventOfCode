from pathlib import Path
import numpy as np
from sys import argv

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 1703
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 21

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

print(arr)

with np.nditer(arr.T, flags=["multi_index", "refs_ok"]) as ar:
    for elm in ar:
        x, y = ar.multi_index




#         if x == 0 or y == 0 or x == size[0] - 1 or y == size[1] - 1:
#             visible += 1
#         else:
#             col = arr.T[x]
#             row = arr[y]
#             if (
#                 np.all(col[:y] < elm)
#                 or np.all(col[y + 1 :] < elm)
#                 or np.all(row[:x] < elm)
#                 or np.all(row[x + 1 :] < elm)
#             ):
#                 visible += 1

# print(visible)
