aim = 0
depth = 0
horizontal_position = 0
final = None

# result of test_input.txt file have to be 900
with open("input.txt", "r") as file:
    lines_list = file.read().splitlines()
    for line in lines_list:
        command, value = line.split()
        if command == "forward":
            horizontal_position += int(value)
            depth += aim * int(value)
        elif command == "up":
            aim -= int(value)
        elif command == "down":
            aim += int(value)
    final = depth * horizontal_position

print(final)
    
