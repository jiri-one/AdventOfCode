from pathlib import Path
import numpy as np

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 496650
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 8

# helper variables
best_view: int = 0

# read the initial file
with open(main_input, "r") as file:
    while line:= file.readline():
        line = line.strip()
        try:
            arr = np.vstack((arr, np.array([int(x) for x in line], dtype=int)))
        except NameError:
            arr = np.array([int(x) for x in line], dtype=int)

size = np.shape(arr.T)
with np.nditer(arr.T, flags=['multi_index']) as ar:
    for elm in ar:
        x, y = ar.multi_index
        col = arr.T[x]
        row = arr[y]
        up = (col[:y])[::-1] # it have to be reversed with [::-1]
        down = col[y+1:]
        left = (row[:x])[::-1] # it have to be reversed with [::-1]
        right = row[x+1:]
        up_view: int = 0
        down_view: int = 0
        left_view: int = 0
        right_view: int = 0
        for tree in up:
            if tree < elm:
                up_view += 1
            elif tree >= elm:
                up_view += 1
                break
        for tree in down:
            if tree < elm:
                down_view += 1
            elif tree >= elm:
                down_view += 1
                break
        for tree in left:
            if tree < elm:
                left_view += 1
            elif tree >= elm:
                left_view += 1
                break
        for tree in right:
            if tree < elm:
                right_view += 1
            elif tree >= elm:
                right_view += 1
                break
        current_view: int = up_view * down_view * left_view * right_view
        if current_view > best_view:
            best_view = current_view
            

print(best_view)
