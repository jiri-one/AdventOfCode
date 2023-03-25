from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 74


# read the initial file
with open(main_input, "r") as file:
    line = file.readline().strip()
    counter: int = 0
    for bratchet in line:
        if bratchet == "(":
            counter += 1
        else:
            counter -= 1

print(counter)
