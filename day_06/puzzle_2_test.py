with open("test_input.txt", "r") as file:
	lines_list = file.read().splitlines()

lanternfish_list = lines_list[0].split(",")

days = list(range(1,81))

while days:
	
