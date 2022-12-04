from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 562
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 2

# helper functions

# helper variables
overlaps: int = 0

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            elf1, elf2 = line.split(",")
            elf1_start, elf1_end = [int(nr) for nr in elf1.split("-")]
            elf2_start, elf2_end = [int(nr) for nr in elf2.split("-")]
            elf1_range = range(elf1_start, elf1_end + 1)
            elf2_range = range(elf2_start, elf2_end + 1)
            if elf1_start in elf2_range and elf1_end in elf2_range:
                overlaps += 1
            elif elf2_start in elf1_range and elf2_end in elf1_range:
                overlaps += 1
            

print(overlaps)
