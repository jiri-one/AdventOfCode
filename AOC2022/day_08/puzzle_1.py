from pathlib import Path
import numpy as np

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 1703
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 21

# helper variables
visible: int = 0

# read the initial file
with open(main_input, "r") as file:
    while line := file.readline():
        line = line.strip()
        try:
            arr = np.vstack((arr, np.array([int(x) for x in line], dtype=int)))
        except NameError:
            arr = np.array([int(x) for x in line], dtype=int)

size = np.shape(arr.T)
with np.nditer(arr.T, flags=["multi_index"]) as ar:
    for elm in ar:
        x, y = ar.multi_index
        if x == 0 or y == 0 or x == size[0] - 1 or y == size[1] - 1:
            visible += 1
        else:
            col = arr.T[x]
            row = arr[y]
            if (
                np.all(col[:y] < elm)
                or np.all(col[y + 1 :] < elm)
                or np.all(row[:x] < elm)
                or np.all(row[x + 1 :] < elm)
            ):
                visible += 1

print(visible)
