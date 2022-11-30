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
                arr_risk = np.vstack((arr_risk, np.array([int(x) for x in line], dtype=int)))
                arr_check = np.vstack((arr_check, np.array([True for x in line], dtype=bool)))
                arr_way = np.vstack((arr_way, np.array([0 for x in line], dtype=int)))
                
            except NameError:
                arr_risk = np.array([int(x) for x in line], dtype=int)
                arr_check = np.array([True for x in line], dtype=bool)
                arr_way = np.array([0 for x in line], dtype=int)
                

print(arr_risk)
print(arr_check)
print(arr_way)

arr_check[0][0] = False # no need to check top left element


with np.nditer([arr_risk, arr_check, arr_way], flags=['multi_index'], op_flags=['readwrite']) as ar:
    while True in arr_check:
        for risk, check, way in ar: # from is from arr_risk, check is from... etc
            x, y = ar.multi_index
            print(x, y)
            # if y[...] == "#":
            #     x[...] = "#"
