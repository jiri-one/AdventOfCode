from pathlib import Path
import numpy as np

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is PZULBAUA

# helper variables
X: int = 1
X_coor: tuple[int, int, int] = (X-1, X, X+1)
cycle: int = 0
arr = np.array(["." for x in range(240)], dtype=str)
arr = arr.reshape(6, 40) # and directly reshape the array
row_nr = 0
row = arr[row_nr]


# helper functions
def cycler():
    global cycle, row_nr, row
    cycle += 1
    if cycle % 40 == 0:
        row_nr += 1
        if row_nr < 6: # it is here because of last cmd
            row = arr[row_nr]
    col = (cycle - 1) % 40
    if col in X_coor:
        row[col] = "X"  


# read the initial file
with open(main_input, "r") as file:
    while line:= file.readline():
        line = line.strip()
        line_list = line.split()
        print(line_list)
        if line_list[0] == "noop":
            cycler()
        else: # addx command
            cycler()
            cycler()
            X += int(line_list[1])
            X_coor = (X-1, X, X+1)


print(arr)
            


        
        
