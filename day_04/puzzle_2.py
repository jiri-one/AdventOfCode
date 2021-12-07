import numpy as np

arrays_list = []

# result of test_input.txt file have to be 1924 and for input.txt it is 8112
with open("input.txt", "r") as file:
    lines_list = file.read().splitlines()
    numbers = lines_list.pop(0).split(",")
    array_in_list = []
    while lines_list:
        for line in list(lines_list):
            lines_list.pop(0)
            if line != "":
                one_row = [(int(nr), False) for nr in line.split()]
                array_in_list.append(one_row)
                if len(array_in_list) == 5:
                    array = np.array(array_in_list, dtype="i,bool").reshape(5,5)
                    arrays_list.append(array)
                    array_in_list = []

def is_this_array_a_winner(array):
    # firstly check for winner row
    for row_nr, row in enumerate(array):
        true_elements = []
        for element in row:
            if element[1] == True:
                true_elements.append(True)
        if len(true_elements) == 5:
            return True
    # then check for winner column
    for column_nr, column in enumerate(array.T):
        true_elements = []
        for element in column:
            if element[1] == True:
                true_elements.append(True)
        if len(true_elements) == 5:
            return True

def mark_numbers_as_true_in_arrays(nums, arrays):
    win_arrays = []
    win_number = None
    while nums:
        if win_arrays:
            if len(arrays) > 1:
                for array_to_delete in sorted(win_arrays, reverse=True):
                    arrays.pop(array_to_delete)
                win_arrays = []
            else:
                return arrays[0], win_number
        number = nums.pop(0)
        for array_nr, array in enumerate(arrays):
            for row_nr, row in enumerate(array):
                for element_nr, element in enumerate(row):
                    if element[0] == int(number):
                        arrays[array_nr][row_nr][element_nr][1] = True
            if is_this_array_a_winner(array) == True:
                win_arrays.append(array_nr)
                win_number = int(number)

this_array_is_last_winner, win_number = mark_numbers_as_true_in_arrays(numbers, arrays_list)

elements_sum = 0
for row in this_array_is_last_winner:
    for element in row:
        if element[1] == False:
            elements_sum += element[0]

print(elements_sum * win_number)
