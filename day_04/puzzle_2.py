import numpy as np

arrays_list = []

# result of test_input.txt file have to be 1924
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

def is_there_a_winner():
    for array_nr, array in enumerate(arrays_list):
        # firstly check for winner row
        for row_nr, row in enumerate(array):
            true_elements = []
            for element in row:
                if element[1] == True:
                    true_elements.append(True)
            if len(true_elements) == 5:
                return array_nr
        # then check for winner column
        for column_nr, column in enumerate(array.T):
            true_elements = []
            for element in column:
                if element[1] == True:
                    true_elements.append(True)
            if len(true_elements) == 5:
                return array_nr

def mark_numbers_as_true_in_arrays():
    for number in numbers:
        for array_nr, array in enumerate(arrays_list):
            for row_nr, row in enumerate(array):
                for element_nr, element in enumerate(row):
                    if element[0] == int(number):
                        arrays_list[array_nr][row_nr][element_nr][1] = True
            result = is_there_a_winner()
            if result is not None:
                return result, int(number)

while len(arrays_list) > 1:
    print(len(arrays_list))
    winner_is_array_nr, win_number = mark_numbers_as_true_in_arrays()
    removed_array = arrays_list.pop(winner_is_array_nr)

winner_is_array_nr, win_number = mark_numbers_as_true_in_arrays()

elements_sum = 0
for row in arrays_list[0]:
    for element in row:
        if element[1] == False:
            elements_sum += element[0]

print(elements_sum * win_number)
