from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 3120

# read the initial file
with open(main_input, "r") as file:
    line = file.readline().strip()

start, stop = 0, 14
while True:
    string =line[start:stop]
    unique = sum([string.count(x) for x in string])
    if unique == 14:
        print(stop)
        break
    start += 1
    stop += 1
