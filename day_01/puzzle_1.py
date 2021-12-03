prev_deep = None
larger = 0

# result of test_input.txt file have to be 7
with open("input.txt", "r") as file:
    for line in file.readlines():
        try:
            if prev_deep == None:
                prev_deep = int(line)
            else:
                next_deep = int(line)
                if next_deep > prev_deep:
                    larger += 1
                prev_deep = next_deep
        except ValueError:
            pass

print(larger)