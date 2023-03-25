import numpy as np

# result of test_input.txt file have to be 195 and for input.txt it is 324
with open("input.txt", "r") as file:
    while line := file.readline().strip():
        try:
            arr = np.vstack((arr, np.array([int(x) for x in line], dtype=int)))
        except NameError:
            arr = np.array([int(x) for x in line], dtype=int)

steps = 0
while True:
    steps += 1
    arr += 1
    arr[arr == 10] = 0
    zeroes_to_check = set()
    for row_nr, row in enumerate(arr):
        for elm_nr, elm in enumerate(row):
            if elm == 0:
                zeroes_to_check.add((row_nr, elm_nr))

    while zeroes_to_check:
        row_nr, elm_nr = zeroes_to_check.pop()
        neighbours = [
            (row_nr + 1, elm_nr - 1),
            (row_nr + 1, elm_nr),
            (row_nr + 1, elm_nr + 1),
            (row_nr, elm_nr - 1),
            (row_nr, elm_nr + 1),
            (row_nr - 1, elm_nr - 1),
            (row_nr - 1, elm_nr),
            (row_nr - 1, elm_nr + 1),
        ]

        for neighbour in neighbours:
            if (
                neighbour[0] >= 0
                and neighbour[1] >= 0
                and neighbour[0] < 10
                and neighbour[1] < 10
            ):
                if arr[neighbour[0]][neighbour[1]] != 0:
                    arr[neighbour[0]][neighbour[1]] += 1
                    if arr[neighbour[0]][neighbour[1]] == 10:
                        arr[neighbour[0]][neighbour[1]] = 0
                        zeroes_to_check.add(neighbour)
    if np.all((arr == 0)):
        break

print(steps)
