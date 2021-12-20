import numpy as np

# result of test_input.txt file have to be 15 and for input.txt it is XXX
with open("test_input.txt", "r") as file:
	while line:=file.readline():
		try:
			arr = np.vstack((arr, np.array([int(x) for x in line.strip()], dtype=int)))
		except NameError:
			arr = np.array([int(x) for x in line.strip()], dtype=int)

for row_nr, row in enumerate(arr):
	if row_nr == 0:
		column_neighbors = (1)
	elif row_nr == len(arr)-1:
		column_neighbors = (len(arr)-2)
	for elm_nr, elm in enumerate(row):
		