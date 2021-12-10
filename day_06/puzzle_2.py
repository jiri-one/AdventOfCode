import numpy as np

# result of test_input.txt file have to be 26984457539 and for input.txt it is XXX
with open("test_input.txt", "r") as file:
    lines_list = file.read().splitlines()

lanternfish_list = lines_list[0].split(",")
lanternfish_array = np.array(lanternfish_list, dtype=np.int8)

for day in range(256):
    lanternfish_array = lanternfish_array - np.int8(1)
    how_many_minus_one = np.size(lanternfish_array[lanternfish_array == np.int8(-1)])
    if how_many_minus_one:
        lanternfish_array[lanternfish_array == np.int8(-1)] = np.int8(6)
        lanternfish_array = np.append(lanternfish_array, [np.int8(8) for _ in range(how_many_minus_one)])

print(lanternfish_array.size)
