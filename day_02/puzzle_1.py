forward = 0
deep = 0
final = None

with open("input.txt", "r") as file:
    lines_list = file.read().splitlines()
    for line in lines_list:
        command, value = line.split()
        if command == "forward":
            forward += int(value)
        elif command == "up":
            deep -= int(value)
        elif command == "down":
            deep += int(value)
    final = forward * deep

print(final)
    
            