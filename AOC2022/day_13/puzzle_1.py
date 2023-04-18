from pathlib import Path
from sys import argv

# set input file
try:
    input_file = argv[1]
    input_file = Path(__file__).parent / argv[1]  
    # standard input files are "input.txt" and "test_input.txt"
    # # result of "input.txt" is XXX
    # # result of "test_input.txt" is 13
except IndexError:
    print("use format: python file.py some_input_file")
