from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 13221
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 15

# 1 for Rock, A, X
# 2 for Paper, B, Y
# 3 for Scissors, C, Z

# helper variables
points:dict[str, int] = {"A": 1, "B": 2, "C": 3}
convetrt_me_to_elf = {"X": "A", "Y": "B", "Z": "C"}
total_score = 0

# helper functions
def choose_winner_and_my_score(elf, me):
    # draw
    if elf == me:
        return points[me] + 3
    elif elf == "A" and me == "B":
        return points[me] + 6
    elif elf == "A" and me == "C":
        return points[me]
    elif elf == "B" and me == "A":
        return points[me]
    elif elf == "B" and me == "C":
        return points[me] + 6
    elif elf == "C" and me == "A":
        return points[me] + 6
    elif elf == "C" and me == "B":
        return points[me]

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            elf, me = line.split()
            me = convetrt_me_to_elf[me]
            total_score += choose_winner_and_my_score(elf, me)

print(total_score)
