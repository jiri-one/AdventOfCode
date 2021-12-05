import numpy as np

arrays_list = []

with open("test_input.txt", "r") as file:
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

def is_there_a_winner(arrays):
	for array_nr, array in enumerate(arrays):
		print(array_nr)
		for row in array:
			print("řádek", row)
		for row in array.T:
			print("sloupec", row)		
	
is_there_a_winner(arrays_list)
