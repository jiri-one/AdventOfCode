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

# print(maps)
src_vals = list(range(seeds[0], seeds[0]+seeds[1])) + list(range(seeds[2], seeds[2]+seeds[3]))
output = []
for map_nr, m in enumerate(maps):
    # print(m)
    for src_val in src_vals:
        for r in m.ranges:
            src_range = range(r[0], r[0]+r[2])
            if src_val in src_range:
                #breakpoint()
                src_index = src_range.index(src_val)
                dst_range = range(r[1], r[1]+r[2])
                dst_nr = dst_range[src_index]
                #print("seed_nr", in_val, "src_range", src_range, "dst_range", dst_range, "seed_index", seed_index, "soil_nr", soil_nr)
                output.append(dst_nr)
                break
        else:
            dst_nr = src_val
            output.append(dst_nr)
    src_vals = output
    output = []
    # if map_nr == 1:
    #     break

print(min(src_vals))

print("__________________________")
