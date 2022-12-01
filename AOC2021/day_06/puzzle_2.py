import numpy as np

# result of test_input.txt file have to be 26984457539 and for input.txt it is 1710166656900
with open("input.txt", "r") as file:
    lines_list = file.read().splitlines()

lanternfish_list = [int(item) for item in lines_list[0].split(",")]

lanternfish_array = np.zeros(9, dtype=int)

number_of_days = 256

# count initial values
for item in lanternfish_list:
    lanternfish_array[item] += 1

for _ in range(number_of_days):
    zeroes = lanternfish_array[0]
    for index in range(8):
        lanternfish_array[index] = lanternfish_array[index+1]
    lanternfish_array[6] += zeroes
    lanternfish_array[8] = zeroes

print(np.sum(lanternfish_array))
