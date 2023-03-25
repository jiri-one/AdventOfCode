import numpy as np
from pathlib import Path
import copy

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 2849
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 315

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if line:
            try:
                arr_risk = np.vstack(
                    (arr_risk, np.array([int(x) for x in line], dtype=int))
                )
            except NameError:
                arr_risk = np.array([int(x) for x in line], dtype=int)

# smaller array 4x4 for test purposes
# with open(test_input, "r") as file:
#     counter = 4
#     for line in file:
#         line = line.strip()
#         if line:
#             try:
#                 arr_risk = np.vstack((arr_risk, np.array([int(x) for x in line][:4], dtype=int)))
#             except NameError:
#                 arr_risk = np.array([int(x) for x in line][:4], dtype=int)
#         counter -= 1
#         if counter < 1:
#             break


def increase_arr(index, arr):
    increased_arr = np.copy(arr)
    for _ in range(index):
        increased_arr = increased_arr + 1
        ten_indexes = np.where(increased_arr.T == 10)
        if np.size(ten_indexes) > 0:
            for ten_index in np.nditer(ten_indexes):
                increased_arr.T[ten_index] = 1
    return increased_arr


# create big array
risk_arr_big_column = np.copy(arr_risk)
for index in range(1, 5):
    risk_arr_big_column = np.concatenate(
        (risk_arr_big_column, increase_arr(index, arr_risk)), axis=0
    )

risk_arr_big = np.copy(risk_arr_big_column)
for index in range(1, 5):
    risk_arr_big = np.concatenate(
        (risk_arr_big, increase_arr(index, risk_arr_big_column)), axis=1
    )

arr_risk = risk_arr_big
arr_check = np.ones(np.shape(arr_risk), dtype=bool)
arr_way = np.zeros(np.shape(arr_risk), dtype=int)


# helper functions
def mark_surrounding_to_check(x, y, lowest_risk, better_way):
    """Mark surrondings elemnts to have to be checked, except the one, which was the entry.
    better_way: it is current way[...] minus current risk[...]
    """
    if lowest_risk[0] != "left":
        if x != 0:
            if arr_way.T[x - 1][y] - arr_risk.T[x - 1][y] > better_way:
                arr_check.T[x - 1][y] = True
    if lowest_risk[0] != "right":
        if x <= arr_check.T.shape[0] - 2:
            if arr_way.T[x + 1][y] - arr_risk.T[x + 1][y] > better_way:
                arr_check.T[x + 1][y] = True
    if lowest_risk[0] != "up":
        if y != 0:
            if arr_way.T[x][y - 1] - arr_risk.T[x][y - 1] > better_way:
                arr_check.T[x][y - 1] = True
    if lowest_risk[0] != "down":
        if y <= arr_check.T.shape[1] - 2:
            if arr_way.T[x][y + 1] - arr_risk.T[x][y + 1] > better_way:
                arr_check.T[x][y + 1] = True


# initial settings for tree elements at the beginning
arr_check.T[0][0] = False  # no need to check top, left element
arr_way.T[0][1] = arr_risk.T[0][1]  # top, left + 1 element -> it's risk = way
arr_check.T[0][1] = False  # no need to check top, left + 1 element
arr_way.T[1][0] = arr_risk.T[1][0]  # top + 1, left element -> it's risk = way
arr_check.T[1][0] = False  # no need to check top + 1, left element


while True in arr_check:
    with np.nditer(
        [arr_risk, arr_check, arr_way], flags=["multi_index"], op_flags=["readwrite"]
    ) as ar:
        for risk, check, way in ar:  # risk is from arr_risk, check is from... etc
            y, x = ar.multi_index
            if check == True:
                left_risk = right_risk = up_risk = down_risk = None

                if x != 0 and arr_way.T[x - 1][y] != 0:
                    left_risk = arr_way.T[x - 1][y] + risk[...]

                if x <= arr_way.T.shape[0] - 2 and arr_way.T[x + 1][y] != 0:
                    right_risk = arr_way.T[x + 1][y] + risk[...]

                if y != 0 and arr_way.T[x][y - 1] != 0:
                    up_risk = arr_way.T[x][y - 1] + risk[...]

                if y <= arr_way.T.shape[1] - 2 and arr_way.T[x][y + 1] != 0:
                    down_risk = arr_way.T[x][y + 1] + risk[...]

                risk_list = [
                    ("left", left_risk),
                    ("right", right_risk),
                    ("up", up_risk),
                    ("down", down_risk),
                ]
                surrounding_risks = [risk for risk in risk_list if risk[1] is not None]
                if len(surrounding_risks) > 0:
                    lowest_risk = sorted(surrounding_risks, key=lambda x: x[1])[0]
                    if way[...] == 0 or lowest_risk[1] <= way[...]:
                        way[...] = lowest_risk[1]
                        check[...] = False
                        mark_surrounding_to_check(
                            x, y, lowest_risk, way[...] - risk[...]
                        )


print(arr_way.T[arr_check.T.shape[0] - 1][arr_check.T.shape[1] - 1])
