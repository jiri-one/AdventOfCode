# result of test_input.txt file have to be 26 and for input.txt it is 272
with open("input.txt", "r") as file:
	lines_list = file.read().splitlines()

easy_digits_counter = 0

for line in lines_list:
	for digital_output in line.split(" | ")[1].split():
		if (
			len(digital_output) == 2 or
			len(digital_output) == 4 or
			len(digital_output) == 3 or
			len(digital_output) == 7
			):
			easy_digits_counter += 1

print(easy_digits_counter)
