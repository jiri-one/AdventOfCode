from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 13131
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 12

# 1 for Rock, A, X
# 2 for Paper, B, Y
# 3 for Scissors, C, Z

# helper variables
points:dict[str, int] = {"A": 1, "B": 2, "C": 3}
convetrt_me_to_elf = {"X": "A", "Y": "B", "Z": "C"}
total_score = 0

# helper functions
def choose_winner_and_my_score(elf, me):
    if me == "A":
        my_score = 0
    elif me == "B":
        my_score = 3
    elif me == "C":
        my_score = 6
    # draw
    if my_score == 3:
        return points[elf] + my_score
    elif elf == "A" and my_score == 6:
        return my_score + points["B"]
    elif elf == "A" and my_score == 0:
        return my_score + points["C"]
    elif elf == "B" and my_score == 6:
        return my_score + points["C"]
    elif elf == "B" and my_score == 0:
        return my_score + points["A"]
    elif elf == "C" and my_score == 6:
        return my_score + points["A"]
    elif elf == "C" and my_score == 0:
        return my_score + points["B"]

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            elf, me = line.split()
            me = convetrt_me_to_elf[me]
            total_score += choose_winner_and_my_score(elf, me)

print(total_score)
