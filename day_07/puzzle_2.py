import numpy as np

# result of test_input.txt file have to be 168 and for input.txt it is 87640209
with open("input.txt", "r") as file:
	lines_list = file.read().splitlines()

crabs = np.sort(np.array([int(crab) for crab in lines_list[0].split(",")]))

best_position = None
least_fuel = None

for crab_position in range(crabs[-1]+1):
	possibly_least_fuel = 0
	for crab in crabs:
		fuel = sum(range(1,abs(crab_position - crab)+1))
		possibly_least_fuel += fuel
	else:
		if least_fuel == None:
			least_fuel = possibly_least_fuel
		elif possibly_least_fuel < least_fuel:
			least_fuel = possibly_least_fuel

print(least_fuel)