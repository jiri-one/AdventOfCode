from pathlib import Path
from sys import argv
from dataclasses import dataclass, field

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 46

if len(argv) > 1 and argv[1] == "--test":
    main_input = test_input

# helper variables
@dataclass
class Map:
    src: str
    dst: str
    ranges: list[tuple[int, int, int]] = field(default_factory=list) # tuple is src int, dst int, range int

seeds = list()
maps: list[Map] = list()

# read the initial file
with open(main_input, "r") as file:
    while line := file.readline():
        line = line.strip()
        if "seeds: " in line:
            line = line.removeprefix("seeds: ")
            seeds = [int(s) for s in line.split()]
        elif " map:" in line:
            src, dst = line.removesuffix(" map:").split("-to-")
            m = Map(src, dst)
            while src_to_dst_map_line := file.readline():
                if src_to_dst_map_line.strip() == "":
                    break
                ranges = [int(nr) for nr in src_to_dst_map_line.split()]
                m.ranges.append(tuple([ranges[1], ranges[0], ranges[2]]))
            maps.append(m)

initial_ranges = []
start, stop = 0, 1

for _ in range(int(len(seeds)/2)):
    current_range = range(seeds[start], seeds[start]+seeds[stop])
    initial_ranges.append(range(seeds[start], seeds[start]+seeds[stop]))
    start += 2
    stop += 2

lowest_location = 1000000000000
#initial_ranges = [[82]]

def range_to_output(m: Map, ini_range: range):
    first_len_of_ini_range = len(ini_range)
    print("ini_range", ini_range)
    output_ranges = []
    for i, r in enumerate(m.ranges):
        src_range = range(r[0], r[0]+r[2])
        dst_range = range(r[1], r[1]+r[2])
        print("src", src_range, "dst", dst_range)
        if ini_range[0] in src_range and ini_range[-1] in src_range:
            print("is in range")
            src_index_start = src_range.index(ini_range[0])
            src_index_end = src_range.index(ini_range[-1])
            dst_start = dst_range[src_index_start]
            dst_stop = dst_range[src_index_end]
            if i == len(m.ranges)-1:
                if not output_ranges:
                    print("it is last map range and no output ranges, so return one complete new range")
                    return range(dst_start, dst_stop+1)
            else:
                print("added range to output ranges")
                output_ranges.append(range(dst_start, dst_stop+1))
            break
        
        elif ini_range[0] not in src_range and ini_range[-1] not in src_range and src_range[0] not in ini_range and src_range[-1] not in ini_range:
            print("is completely out of range")
            if i == len(m.ranges)-1:
                if not output_ranges:
                    print("it is last map range and no output ranges, so return it as is")
                    return ini_range
                else:
                    print("it is last map range, so add ini_range to output_ranges")
                    output_ranges.append(ini_range)
            else:
                print("let it like it is and continue")
                continue
        
        elif ini_range[0] in src_range and ini_range[-1] not in src_range:
            print("beginning is in range, end not")
            src_index_start = src_range.index(ini_range[0])
            src_index_end = len(src_range)-1
            dst1_start = dst_range[src_index_start]
            dst1_stop = dst_range[src_index_end]
            dst1_range = range(dst1_start, dst1_stop+1)
            output_ranges.append(dst1_range)
            print("current ini_range", ini_range)
            print("ZDEEEEEEEEEE", src_range[-1])
            ini_range = range(src_range[-1]+1, ini_range[-1])
            print(f"added to output ranges {dst1_range} and rest of ini_range is {ini_range}")
            if i == len(m.ranges)-1:
                print("it is last src_range so added ini_range to output ranges too")
                output_ranges.append(ini_range)
        
        elif ini_range[0] not in src_range and ini_range[-1] in src_range:
            print("beginning is not in range, end is")
            src_index_end = src_range.index(ini_range[-1])
            dst1_start = dst_range[0]
            dst1_stop = dst_range[src_index_end]
            dst1_range = range(dst1_start, dst1_stop+1)
            output_ranges.append(dst1_range)
            ini_range = range(ini_range[0], src_range[0])
            print(f"added to output ranges {dst1_range} and rest of ini_range is {ini_range}")
            if i == len(m.ranges)-1:
                print("it is last src_range so added ini_range to output ranges too")
                output_ranges.append(ini_range)
        
    final_len_ranges = sum([len(l) for l in output_ranges])
    #assert final_len_ranges == first_len_of_ini_range
    return output_ranges
            
def get_lowest(i):
    global lowest_location
    if isinstance(i, range):
        if i[0] < lowest_location:
            lowest_location = i[0]
        return
    else:
        for l in i:
            get_lowest(l)


for ini_range in initial_ranges:
    output = None
    for m in maps:
        if output:
            if isinstance(output, list):
                next_output = []
                for r in output:               
                    next_output.append(range_to_output(m, r))
                output = next_output
            else:
                output = range_to_output(m, output)
        else:
            output = range_to_output(m, ini_range)
    
        

    get_lowest(output)


print("__________________________")
print(lowest_location)
print("__________________________")
