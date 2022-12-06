from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is FWSHSPJWM
test_input = Path(__file__).parent / "test_input.txt" # result of this file is CMZ

# helper variables
stacks: dict[int, list[str]] = {}
raw_lines: list[str]
move: list[dict[str, int]] = []

# read the initial file
with open(test_input, "r") as file:
    raw_lines = file.readlines()

# create stacks
for line_index, line in enumerate(raw_lines):
    if "[" not in line and "move" not in line: 
        line_in_list = [x for x in line.split() if x] # split line to list and remove empty elements
        try:
            for stack in line_in_list:
                stacks[int(stack)] = [] # all stacks are in dict with stack number key
            raw_lines.pop(line_index) # remove line with stacks
        except ValueError:
            pass

# create move commands
while line := raw_lines.pop(-1):
    if "move" not in line:
        raw_lines.append(line) # return the move line back to the end
        break
    line = line.strip()
    line_list = line.split()
    move.append({
        "crates_count": int(line_list[1]),
        "src_stack": int(line_list[3]),
        "dst_stack": int(line_list[5])
    })

# fill stacks
while raw_lines:
    line = raw_lines.pop(-1)
    start, stop = 0, 3
    stack = 1
    while stop < len(line):
        crate = line[start:stop]
        crate = crate.strip()
        if len(crate) != 0:
            crate = crate.replace("[", "").replace("]", "")
            stacks[stack].append(crate)
        stack += 1
        start += 4
        stop += 4


# move crates
for cmd in reversed(move):
    for _ in range(cmd["crates_count"]):
        stacks[cmd["dst_stack"]].append(stacks[cmd["src_stack"]].pop())

final_chars = ""
for stack in stacks.values():
    final_chars += stack[-1]
    
print(final_chars)
