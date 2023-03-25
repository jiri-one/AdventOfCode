from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 1795


# read the initial file
with open(main_input, "r") as file:
    line = file.readline().strip()
    counter: int = 0
    for position, bratchet in enumerate(line, start=1):
        if bratchet == "(":
            counter += 1
        else:
            counter -= 1
        if counter == -1:
            print(position)
            break
