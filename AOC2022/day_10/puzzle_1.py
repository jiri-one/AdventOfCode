from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 11780
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 13140

# helper variables
X: int = 1
cycle: int = 0
cycles: tuple[int] = (20, 60, 100, 140, 180, 220)
signal_strength: list[int] = []

# helper functions
def comp_signal_strength():
    global cycle
    cycle += 1
    if cycle in cycles:
        signal_strength.append(X * cycle)


# read the initial file
with open(main_input, "r") as file:
    while line:= file.readline():
        line = line.strip()
        line_list = line.split()
        if line_list[0] == "noop":
            comp_signal_strength()
        else: # addx command
            comp_signal_strength()
            comp_signal_strength()
            X += int(line_list[1])

print(sum(signal_strength))
            


        
        
