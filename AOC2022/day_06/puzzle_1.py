from pathlib import Path
from queue import LifoQueue

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 1198
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 7

# read the initial file
with open(main_input, "r") as file:
    line = file.readline().strip()

start, stop = 0, 4
while True:
    string =line[start:stop]
    unique = sum([string.count(x) for x in string])
    if unique == 4:
        print(stop)
        break
    start += 1
    stop += 1
