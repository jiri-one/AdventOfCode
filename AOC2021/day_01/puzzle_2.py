index1 = 0
index2 = 1
index3 = 2
prev_sum = None
larger = 0

# result of test_input.txt file have to be 5
with open("input.txt", "r") as file:
    lines_list = file.read().splitlines()
    while True:
        if prev_sum == None:
            prev_sum = (
                int(lines_list[index1])
                + int(lines_list[index2])
                + int(lines_list[index3])
            )
        else:
            try:
                index1 += 1
                index2 += 1
                index3 += 1
                next_sum = (
                    int(lines_list[index1])
                    + int(lines_list[index2])
                    + int(lines_list[index3])
                )
                if next_sum > prev_sum:
                    larger += 1
                prev_sum = next_sum
            except IndexError:
                break
print(larger)
