from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 7268994
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 24933642

# helper variables
folders: dict[Path, int] = {}
root: Path = Path("/")


# helper functions
def update_parents(dir, size):
    for parent in dir.parents:
        folders[parent] += size


# read the initial file
with open(main_input, "r") as file:
    while line := file.readline():
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
            pass  # skip that line
        elif line[0:3] == "dir":
            pass  # skip that line
        else:
            size, name = line.split()
            size = int(size)
            folders[dir] += size
            update_parents(dir, size)

free_space = 70000000 - folders[root]
needed_space = 30000000 - free_space
result = sorted([size for size in folders.values() if size >= needed_space])[0]
print(result)
