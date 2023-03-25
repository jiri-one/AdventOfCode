from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 3842356

# read the initial file
with open(main_input, "r") as file:
    bow: int = 0
    for line in file:
        line = line.strip()
        if line:
            l, w, h = [int(x) for x in line.split("x")]
            lwh = sorted([l, w, h])
            bow += lwh[0] * 2 + lwh[1] * 2 + l * w * h

print(bow)
