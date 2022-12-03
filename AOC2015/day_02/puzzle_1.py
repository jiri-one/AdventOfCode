from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 1606483

# read the initial file
with open(main_input, "r") as file:
    paper: int = 0
    for line in file:
        line = line.strip()
        if line:
            l, w, h  = [int(x) for x in line.split("x")]
            lwh = sorted([l, w, h]) # smallest part is product of two lowest numbers
            paper += (2*l*w + 2*w*h + 2*h*l + lwh[0]*lwh[1])

print(paper)
