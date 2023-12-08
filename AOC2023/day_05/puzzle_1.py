from pathlib import Path
from sys import argv
from dataclasses import dataclass, field

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 20117
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 13

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

# get soil number
print(maps)
soil_numbers = []
for m in maps:
    print(m)
    for seed_nr in seeds:
        for r in m.ranges:
            src_range = range(r[0], r[0]+r[2])
            if seed_nr in src_range:
                seed_index = src_range.index(seed_nr)
                dst_range = range(r[1], r[1]+r[2])
                soil_nr = dst_range[seed_index]
                print("seed_nr", seed_nr, "src_range", src_range, "dst_range", dst_range, "seed_index", seed_index, "soil_nr", soil_nr)
                soil_numbers.append(soil_nr)
                break
        else:
            soil_nr = seed_nr
            soil_numbers.append(soil_nr)
    break

print(soil_numbers)



        

# print(seeds)
# print(maps)

print("__________________________")
