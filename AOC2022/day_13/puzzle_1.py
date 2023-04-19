from pathlib import Path
from sys import argv

# set input file with data
try:
    input_file = argv[1]
    input_file = Path(__file__).parent / argv[1]
    if not input_file.exists():
        raise FileNotFoundError() 
    # standard input files are "input.txt" and "test_input.txt"
    # # result of "input.txt" is XXX
    # # result of "test_input.txt" is 13
except IndexError:
    print("use format: python file.py some_input_file")
except FileNotFoundError:
    print("Input file has to exist and the path has to be correct.")

l_packets = []
r_packets = []
line_counter = 0
with open(input_file, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            line_counter +=1
            if line_counter % 2 == 0:
                r_packets.append(line)
            else:
                l_packets.append(line) 

print(l_packets)
print(r_packets)
