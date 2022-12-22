from pathlib import Path
from string import ascii_lowercase, ascii_uppercase, punctuation

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 33

# helper variables
unwanted_chars = ascii_lowercase + ascii_uppercase + punctuation

# helper functions

# read the initial file
with open(main_input, "r") as file:
    while line:= file.readline():
        for char in unwanted_chars: line = line.replace(char, "")
        line_list = line.split()
        blueprint = line_list[0]
        ore_robot = line_list[1]
        clay_robot = line_list[2]
        obsidian_robot = (line_list[3], line_list[4]) # ore and clay
        geode_robot = (line_list[5], line_list[6]) # ore and obsidian
        print(blueprint, ore_robot, clay_robot, obsidian_robot, geode_robot)
