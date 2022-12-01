# result of test_input.txt file have to be 288957 and for input.txt it is 1118645287

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

total_scores = []
for one_incomplete in incomplete:
    score = 0
    one_incomplete = list(one_incomplete)
    one_incomplete.reverse() # I dont need to replace it for closing variant )}]>, its same with opening variant, reversed
    for char in one_incomplete:
        if char == "[":
            score = score * 5 + 2
        elif char == "(":
            score = score * 5 + 1
        elif char == "{":
            score = score * 5 + 3
        elif char == "<":
            score = score * 5 + 4
    total_scores.append(score)

print(sorted(total_scores)[int(len(total_scores)/2)])
