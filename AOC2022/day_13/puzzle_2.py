from pathlib import Path
from re import findall
from sys import argv

# set input file with data
try:
    input_file = argv[1]
    input_file = Path(__file__).parent / argv[1]
    if not input_file.exists():
        raise FileNotFoundError() 
    # standard input files are "input.txt" and "test_input.txt"
    # # result of "input.txt" is 27648
    # # result of "test_input.txt" is 140
except IndexError:
    print("use format: python file.py some_input_file")
except FileNotFoundError:
    print("Input file has to exist and the path has to be correct.")

packets = [[2], [6]] # initial packets with divider packets too
with open(input_file, "r") as file:
    for line in file:
        line = line.strip()
        line = line.replace("[]", "[0]")
        if line:
            numbers = findall("\d+", line)
            if numbers:
                packets.append([int(x) for x in numbers])
            else:
                packets.append([0])

print(packets)
packets.sort()
print(packets)
index_if_divider1 = packets.index([2]) + 1
index_if_divider2 = packets.index([6]) + 1

print("Answer of part2 is", index_if_divider1*index_if_divider2)
