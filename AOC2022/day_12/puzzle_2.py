import numpy as np
from pathlib import Path
from string import ascii_lowercase
from sys import maxsize, argv

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 386
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 29

# helper variables
height: dict[str, int] = {}


# helper functions
def char_to_num_dict():
    height_range = range(1, len(ascii_lowercase) + 1)
    for current_height, char in zip(height_range, ascii_lowercase):
        height[char] = current_height
    height["S"] = 0
    height["E"] = 99


char_to_num_dict()  # and run it to fullfill height dict


# read the initial file
with open(argv[1], "r") as file:
    for line in file:
        line = line.strip()
        if line:
            try:
                arr_height = np.vstack(
                    (arr_height, np.array([height[x] for x in line], dtype=int))
                )
                arr_check = np.vstack(
                    (arr_check, np.array([True for x in line], dtype=bool))
                )
                arr_way = np.vstack((arr_way, np.array([0 for x in line], dtype=int)))

            except NameError:
                arr_height = np.array([height[x] for x in line], dtype=int)
                arr_check = np.array([True for x in line], dtype=bool)
                arr_way = np.array([0 for x in line], dtype=int)

S = np.where(arr_height.T == 0)  # coordinates of start in array
E = np.where(arr_height.T == 99)  # coordinates of end in array
arr_height.T[S] = 1  # give a start a right heights
arr_height.T[E] = 26  # give a end a right heights
Sx, Sy = int(S[0]), int(S[1])  # coordinates of start in int
Ex, Ey = int(E[0]), int(E[1])  # coordinates of end in int

np.set_printoptions(threshold=maxsize, linewidth=1000)


# helper functions
def mark_surrounding_to_check(x, y, shortest_way):
    """Mark surrondings elements to have to be checked, except the one, which was the shortest entry.
    better_way: it is current way[...] minus current risk[...]
    """
    if shortest_way[0] != "left":
        if x != 0:
            if arr_way.T[x - 1][y] > shortest_way[1] - 1:
                arr_check.T[x - 1][y] = True
    if shortest_way[0] != "right":
        if x <= arr_check.T.shape[0] - 2:
            if arr_way.T[x + 1][y] > shortest_way[1] - 1:
                arr_check.T[x + 1][y] = True
    if shortest_way[0] != "up":
        if y != 0:
            if arr_way.T[x][y - 1] > shortest_way[1] - 1:
                arr_check.T[x][y - 1] = True
    if shortest_way[0] != "down":
        if y <= arr_check.T.shape[1] - 2:
            if arr_way.T[x][y + 1] > shortest_way[1] - 1:
                arr_check.T[x][y + 1] = True


# initial settings for neighbouring start elements
arr_check.T[E] = False  # no need to check Start (Start is End (E) now)
# if left element is same or lower -1, you can go there so +1 step
if Ex != 0 and arr_height.T[Ex - 1][Ey] >= 25:
    arr_way.T[Ex - 1][Ey] += 1
    arr_check.T[Ex - 1][Ey] = False
# if right element is same or lower -1, you can go there so +1 step
if Ex <= arr_way.T.shape[0] - 2 and arr_height.T[Ex + 1][Ey] >= 25:
    arr_way.T[Ex + 1][Ey] += 1
    arr_check.T[Ex + 1][Ey] = False
# if up element is same or lower -1, you can go there so +1 step
if Ey != 0 and arr_height.T[Ex][Ey - 1] >= 25:
    arr_way.T[Ex][Ey - 1] += 1
    arr_check.T[Ex][Ey - 1] = False
# if down element is same or lower -1, you can go there so +1 step
if Ey <= arr_way.T.shape[1] - 2 and arr_height.T[Ex][Ey + 1] >= 25:
    arr_way.T[Ex][Ey + 1] += 1
    arr_check.T[Ex][Ey + 1] = False


while True in arr_check:
    arr_way_copy = np.copy(arr_way)
    with np.nditer(
        [arr_height, arr_check, arr_way], flags=["multi_index"], op_flags=["readwrite"]
    ) as ar:
        for height, check, way in ar:  # height is from arr_height, check is from... etc
            y, x = ar.multi_index
            if check == True:
                left_way = right_way = up_way = down_way = None
                # print("x, y", x, y)
                if (
                    x != 0
                    and arr_way.T[x - 1][y] != 0
                    and height[...] - arr_height.T[x - 1][y] >= -1
                ):
                    left_way = arr_way.T[x - 1][y] + 1

                if (
                    x <= arr_way.T.shape[0] - 2
                    and arr_way.T[x + 1][y] != 0
                    and height[...] - arr_height.T[x + 1][y] >= -1
                ):
                    right_way = arr_way.T[x + 1][y] + 1

                if (
                    y != 0
                    and arr_way.T[x][y - 1] != 0
                    and height[...] - arr_height.T[x][y - 1] >= -1
                ):
                    up_way = arr_way.T[x][y - 1] + 1

                if (
                    y <= arr_way.T.shape[1] - 2
                    and arr_way.T[x][y + 1] != 0
                    and height[...] - arr_height.T[x][y + 1] >= -1
                ):
                    down_way = arr_way.T[x][y + 1] + 1

                way_list = [
                    ("left", left_way),
                    ("right", right_way),
                    ("up", up_way),
                    ("down", down_way),
                ]
                surrounding_way = [w for w in way_list if w[1] is not None]
                #print("surrounding_way", surrounding_way)
                if len(surrounding_way) > 0:
                    shortest_way = sorted(surrounding_way, key=lambda x: x[1])[0]
                    if way[...] == 0 or shortest_way[1] <= way[...]:
                        way[...] = shortest_way[1]
                        check[...] = False
                        mark_surrounding_to_check(x, y, shortest_way)
    if np.array_equal(arr_way_copy, arr_way):
        break
            
    print(arr_way)
    print(arr_height)
    print("")

one_with_lowest_steps = 100000
with np.nditer(
    [arr_height, arr_way]) as ar:
    for height, way in ar:
        if height[...] == 1 and 0 < way[...] < one_with_lowest_steps:
            one_with_lowest_steps = way[...]

print(one_with_lowest_steps)
