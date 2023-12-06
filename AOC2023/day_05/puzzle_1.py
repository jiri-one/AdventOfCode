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
    map: list[tuple[int, int, int]] = field(default_factory=list)


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
            print(src, dst)
            m = Map(src, dst)
            while src_to_dst_map_line := file.readline():
                if src_to_dst_map_line.strip() == "":
                    break
                m.map.append(tuple(int(nr) for nr in src_to_dst_map_line.split()))
            maps.append(m)

        

print(seeds)
print(maps)

print("__________________________")
