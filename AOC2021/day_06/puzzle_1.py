import numpy as np

# result of test_input.txt file have to be 5934 and for input.txt it is 380612
with open("input.txt", "r") as file:
    lines_list = file.read().splitlines()

lanternfish_list = lines_list[0].split(",")
lanternfish_array = np.array(lanternfish_list, dtype=int)

for day in range(80):
    lanternfish_array = lanternfish_array - 1
    minus_one_indexes = np.where(lanternfish_array==-1)
    if np.size(minus_one_indexes):
        for minus_one_index in np.nditer(minus_one_indexes):
            lanternfish_array[minus_one_index] = 6
            lanternfish_array = np.append(lanternfish_array, 8)

print(lanternfish_array.size)
