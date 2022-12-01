# result of test_input.txt file have to be 26397 and for input.txt it is 366027

incomplete = []
corrupted = []

with open("input.txt", "r") as file:
    while line:=file.readline().strip():
        while True:
            new_line = line
            new_line = new_line.replace("{}", "")
            new_line = new_line.replace("[]", "")
            new_line = new_line.replace("()", "")
            new_line = new_line.replace("<>", "")
            if new_line != line:
                line = new_line
            else:
                if (
                    "}" not in new_line and
                    ")" not in new_line and
                    ">" not in new_line and
                    "]" not in new_line
                    ):
                    incomplete.append(new_line)
                else:
                    corrupted.append(new_line)
                break

score = 0
for one_corrupted in corrupted:
    for char in one_corrupted:
        if char in "])}>":
            if char == "]":
                score += 57
            elif char == ")":
                score += 3
            elif char == "}":
                score += 1197
            elif char == ">":
                score += 25137
            break

print(score)