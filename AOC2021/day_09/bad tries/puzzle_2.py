import numpy as np

# result of test_input.txt file have to be 15 and for input.txt it is 494
with open("test_input.txt", "r") as file:
	while line:=file.readline():
		try:
			arr = np.vstack((arr, np.array([int(x) for x in line.strip()], dtype=int)))
		except NameError:
			arr = np.array([int(x) for x in line.strip()], dtype=int)

lowest_points = np.array([], dtype=int)

basins = []

def determine_elemnt_to_the_edges(row_nr: int, elm_nr: int):
	first_basin_row = [elm_nr]
	counter = 1
	while True:
		try:
			current_value = arr[row_nr][elm_nr+counter]
			if current_value != 9:
				first_basin_row.append(elm_nr+counter)
				counter += 1
			elif current_value == 9:
				break
		except IndexError:
			break
	
	counter = 1
	while True:
		try:
			if (elm_nr - counter) >= 0:
				current_value = arr[row_nr][elm_nr-counter]
				if current_value != 9:
					first_basin_row.append(elm_nr-counter)
					counter += 1
				elif current_value == 9:
					break
			else:
				break
		except IndexError:
			break
	return first_basin_row

def detect_its_basin(row_nr: int, elm_nr: int):
	first_basin_row = determine_elemnt_to_the_edges(row_nr, elm_nr)
	basin = (len(first_basin_row))

	for basin_elm_index in first_basin_row:
		try:
			if arr[row_nr+1][basin_elm_index] < 9:
				return basin + detect_its_basin(row_nr+1, basin_elm_index)
		except IndexError:
			pass
	else:
		return(basin)
	
	#for basin_elm_index in basin_in_row:
		#try:
			#if arr[row_nr-1][basin_elm_index] < 9:
				#return basin + detect_its_basin(row_nr-1, basin_elm_index)
		#except IndexError:
			#pass	
	
	
	
		

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

print(basins)
#print(np.sum(lowest_points+1))