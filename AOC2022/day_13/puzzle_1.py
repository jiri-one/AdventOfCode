from pathlib import Path
from itertools import zip_longest
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
                r_packets.append(eval(line))
            else:
                l_packets.append(eval(line)) 

# print(l_packets)
# print(r_packets)

# helper functions and variables
# def same_type(first, second):
#     return type(first) 
def compare_packets(l_packet, r_packet):
    if isinstance(l_packet, int):
        print("prevest levou stranu na seznam:", l_packet)
        l_packet = [l_packet] # convert l_packet to list
    if isinstance(r_packet, int):
        print("prevest pravou stranu na seznam:", r_packet)
        r_packet = [r_packet] # convert r_packet to list
    for l_elm, r_elm in zip_longest(l_packet, r_packet):
        if l_elm is None: # Left side ran out of items
            print("tady dosly prvky leve strane", l_elm, r_elm)
            return True
        if r_elm is None: # Right side ran out of items
            print("tady dosly prvky prave strane", l_elm, r_elm)
            return False
        if type(l_elm) == type(r_elm): # both sides are same type
            if isinstance(l_elm, int): # both sides are integer
                print("POROVNAVAM", l_elm, r_elm)
                if l_elm < r_elm:
                    print("leva je mensi nez prava", l_elm, r_elm)
                    return True
                if l_elm > r_elm:
                    print("prava je mensi nez leva", l_elm, r_elm)
                    return False
            elif isinstance(l_elm, list): # both sides are list
                print("tady dva seznamy", l_elm, r_elm)
                result = compare_packets(l_elm, r_elm)
                if result is not None:
                    return result
        else: # mixed types
            if isinstance(l_elm, int):
                l_elm = [l_elm] # convert l_elm to list
                print("prevest levou stranu na seznam:", l_elm)
            if isinstance(r_elm, int):
                r_elm = [r_elm] # convert r_elm to list
                print("prevest pravou stranu na seznam:", r_elm)
            print("tady dva seznamy taky", l_elm, r_elm)
            result = compare_packets(l_elm, r_elm)
            if result is not None:
                return result

# result = None
# def compare_packets(l_packet, r_packet):
#     if type(l_packet) == type(r_packet) and isinstance(r_packet, int): # both sides are integer
#         print("POROVNAVAM", l_packet, r_packet)
#         if l_packet < r_packet:
#             print("leva je mensi nez prava", l_packet, r_packet)
#             return True
#         if l_packet > r_packet:
#             print("prava je mensi nez leva", l_packet, r_packet)
#             return False
    
#     # mixed types or two lists
#     if isinstance(l_packet, int):
#         l_packet = [l_packet] # convert l_packet to list
#         print("prevest levou stranu na seznam:", l_packet)
#     if isinstance(r_packet, int):
#         r_packet = [r_packet] # convert r_packet to list
#         print("prevest pravou stranu na seznam:", r_packet)
#     print("tady dva seznamy", l_packet, r_packet)
#     while True:
#         try:
#             l_elm = l_packet.pop(0)
#         except IndexError:
#             return True # Left side ran out of items
#         try:
#             r_elm = r_packet.pop(0)
#         except IndexError:
#             return False # Right side ran out of items
#         print("HMMMMMM", l_elm, r_elm)
#         if compare_packets(l_elm, r_elm):
#             return True

        
            
ne = 1 # number of elements
right_order = []
for packet_index, (l_packet, r_packet) in enumerate(zip(l_packets, r_packets), start=1):
    print(packet_index, (l_packet, r_packet))
    print(compare_packets(l_packet, r_packet))
    if compare_packets(l_packet, r_packet):
        right_order.append(packet_index)

print("right_order", right_order)
print("answer part1:", sum(right_order))
