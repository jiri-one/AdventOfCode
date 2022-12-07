from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 95437

folders: dict[Path, int] = {}
root: Path = Path("/")

# helper variables
def update_parents(dir, size):
    for parent in dir.parents:
        folders[parent] += size
    

# read the initial file
with open(main_input, "r") as file:
    while line:= file.readline():
        line = line.strip()
        if line[0:4] == "$ cd":
            if line[5:] == "/":
                dir = root
                folders[dir] = 0
            elif line[5:] == "..":
                dir = dir.parent
            else:
                dir = dir / line[5:]
                folders[dir] = 0
        elif line == "$ ls":
            pass
        elif line[0:3] == "dir":
            pass
        else:
            size, name = line.split()
            size = int(size)
            folders[dir] += size
            update_parents(dir, size)

result = sum([size for size in folders.values() if size < 100000])
print(result)
