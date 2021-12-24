import numpy as np

# result of test_input.txt file have to be 1134 and for input.txt it is 1048128
with open("input.txt", "r") as file:
	while line:=file.readline():
		try:
			arr = np.vstack((arr, np.array([int(x) for x in line.strip()], dtype=int)))
		except NameError:
			arr = np.array([int(x) for x in line.strip()], dtype=int)

lowest_points = np.array([], dtype=int)

basins = []

def detect_its_basin(row_nr: int, elm_nr: int):
	basins_coordinates = {(row_nr, elm_nr)} # it is set, so any element of set is unique
	while True: # repeat until break is called
		last_basin_len = len(basins_coordinates) # We need to check if new elements have added in main for cycle or it is done
		for coordinate in set(basins_coordinates): # main iteration of set (it is actual copy of set, bacause original set we will modify)
			row_index, elm_index = coordinate
			for try_row_i, try_elm_i in [(row_index+1, elm_index),
										 (row_index-1, elm_index), 
										 (row_index, elm_index+1), 
										 (row_index, elm_index-1)]: # iteration of "cross adjacent locations"
				if try_row_i < 0 or try_elm_i < 0: # we can not have minus indexes
					pass
				else:
					try: # we need to eliminate indexes, which are out of array
						if arr[try_row_i][try_elm_i] < 9:
							basins_coordinates.add((try_row_i, try_elm_i)) # add coordinates to the set
					except IndexError:
						pass
		else: # after whole main iteration it is done ... (or after iteration of all elements)
			if len(basins_coordinates) == last_basin_len: # check if any new element is in set, and if not ...
				return last_basin_len # we can return number of elemnts in basin

for row_nr, row in enumerate(arr):
	if row_nr == 0:
		row_neighbors = [1]
	elif row_nr == len(arr)-1:
		row_neighbors = [len(arr)-2]
	else: 
		row_neighbors = [row_nr-1, row_nr+1]
	for elm_nr, elm in enumerate(row):
		neighbors_values = np.array([], dtype=int)
		if elm_nr == 0:
			neighbors_values = np.append(neighbors_values, row[1])
		elif elm_nr == len(row)-1:
			neighbors_values = np.append(neighbors_values, row[elm_nr-1])
		else: 
			neighbors_values = np.append(neighbors_values, [row[elm_nr-1], row[elm_nr+1]])
		
		for row_index in row_neighbors:
			neighbors_values = np.append(neighbors_values, arr[row_index][elm_nr])
		
		neighbors_values.sort()
		if elm < sorted(neighbors_values)[0]:
			lowest_points = np.append(lowest_points, elm)
			basins.append(detect_its_basin(row_nr, elm_nr))

three_bigest_basins = sorted(basins)[-3:]

print(three_bigest_basins[0] * three_bigest_basins[1] * three_bigest_basins[2])
