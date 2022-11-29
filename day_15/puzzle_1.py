import numpy as np
from pathlib import Path
import copy

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is XXXX
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 40

# helper variables

# helper functions

# read the initial file
with open(test_input, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            try:
                arr = np.vstack((arr, np.array([int(x) for x in line], dtype=int)))
            except NameError:
                arr = np.array([int(x) for x in line], dtype=int)

coor = (0, 0)
while coor != arr.shape:
    
