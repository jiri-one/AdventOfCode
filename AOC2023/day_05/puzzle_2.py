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

for init_r in initial_ranges:
    for src_val in init_r:
        current = src_val
        for m in maps:
            for r in m.ranges:
                src_range = range(r[0], r[0]+r[2])
                if current in src_range:

                    src_index = src_range.index(current)
                    dst_range = range(r[1], r[1]+r[2])
                    dst_nr = dst_range[src_index]

                    break
            else:
                dst_nr = current

            current = dst_nr

        if current < lowest_location:
            lowest_location = current

print(lowest_location)


print("__________________________")
