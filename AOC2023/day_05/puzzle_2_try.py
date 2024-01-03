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
    ranges: list[tuple[range, range]] = field(default_factory=list) # tuple is src int, dst int, range int

inputs = list()
maps: list[Map] = list()

# read the initial file
with open(main_input, "r") as file:
    while line := file.readline():
        line = line.strip()
        if "seeds: " in line:
            line = line.removeprefix("seeds: ")
            raw_inputs = [int(s) for s in line.split()]
            it = iter(raw_inputs)
            for inp in it:
                inputs.append(range(inp, inp+next(it)))
                
        elif " map:" in line:
            src, dst = line.removesuffix(" map:").split("-to-")
            m = Map(src, dst)
            while src_to_dst_map_line := file.readline():
                if src_to_dst_map_line.strip() == "":
                    break
                r0, r1, r2 = [int(nr) for nr in src_to_dst_map_line.split()]
                dst_range = range(r0, r0+r2)
                src_range = range(r1, r1+r2)
                m.ranges.append((src_range, dst_range))
            maps.append(m)

def sort_ranges(ranges: list[range]):
    new_ranges = sorted(ranges, key=lambda r: r.start)
    return new_ranges


lowest_location = 1000000000000
for m in maps:
    print("MAPS:", m.src, "to", m.dst)
    print("==============================")
    for rng in m.ranges:
        src_range, dst_range = rng
        move = dst_range[0] - src_range[0]
        print("src_range", src_range, "dst_range", dst_range)
        print("move", move)
        new_inputs = []
        try:
            while inp:= inputs.pop(0):
                print("input range", inp)
                if inp.start in src_range and inp[-1] in src_range:
                    print("completely in")
                    new_range = range(inp.start+move, inp.stop+move)
                    new_inputs.append(new_range)
                
                elif (
                    inp.start not in src_range
                    and inp[-1] not in src_range
                    and src_range.start not in inp
                    and src_range[-1] not in inp
                    ):
                    print("comletely out")
                    new_inputs.append(inp)
                
                elif inp.start in src_range and inp[-1] not in src_range:
                    print("start is in src_range, end is not")
                    new_range = range(inp.start+move, src_range.stop+move)
                    rest_of_range = range(src_range.stop, inp.stop)
                    
                    new_inputs.append(new_range)
                    inputs.append(rest_of_range)
                    print(len(new_range), len(rest_of_range), len(inp))
                    print(new_range, rest_of_range, inp)
                    assert len(new_range) + len(rest_of_range) == len(inp)
                
                elif inp.start not in src_range and inp[-1] in src_range:
                    print("start is not in src_range, end is")
                    new_range = range(src_range.start+move, inp.stop+move)
                    rest_of_range = range(inp.start, src_range.start)
                    print("rest_of_range[-1]", rest_of_range[-1], "new_range[0]", new_range[0])
                    
                    new_inputs.append(new_range)
                    inputs.append(rest_of_range)
                    print(len(new_range), len(rest_of_range), len(inp))
                    print(f"{new_range=}, {rest_of_range=}, {inp=}")
                    assert len(new_range) + len(rest_of_range) == len(inp)
        except IndexError:
            print("new_inputs", new_inputs)
            inputs = new_inputs
    
    
print(min([x[0] for x in new_inputs]))
    

#print(inputs)
#print(maps)
