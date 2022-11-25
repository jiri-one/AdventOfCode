from pathlib import Path
import copy

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 2188189693529

# helper variables
null_count_rules: dict[str, dict[str, str | int]] = {}
letter_count: dict[str, int] = {}

# helper functions
def letter_counter(char, count = 1):
    try:
        letter_count[char] += count
    except KeyError:
        letter_count[char] = count

# read the initial file
with open(main_input, "r") as file:
    formula = next(file).strip() # first line of file
    for line in file:
        line = line.strip()
        if line:
            pair, added_char = line.split(" -> ")
            null_count_rules[pair] = {"added_char": added_char, "count": 0}

# initial count for letters
for char in formula:
    letter_counter(char)

# initial operation for new_rules
rules = copy.deepcopy(null_count_rules)
start, end = 0, 2
while True:
    pair = formula[start:end]
    if len(pair) < 2:
        break
    try:
        rules[pair]["count"] += 1
    except KeyError:
        pass
    start += 1
    end += 1

for _ in range(40):
    next_rules = copy.deepcopy(null_count_rules)
    for key in rules:
        if rules[key]["count"] != 0:
            next_key1 = key[0] + rules[key]["added_char"] # first letter in key+added_char
            next_key2 = rules[key]["added_char"] + key[1] # added_char + second letter in key
            # it's import here to use += because we need to do it more time
            next_rules[next_key1]["count"] += rules[key]["count"]
            next_rules[next_key2]["count"] += rules[key]["count"]
            letter_counter(rules[key]["added_char"], rules[key]["count"])

    rules = copy.deepcopy(next_rules)

print(letter_count)
sorted_letter_count = sorted(letter_count.items(), key=lambda x:x[1])
print("The result is:", sorted_letter_count[-1][1] - sorted_letter_count[0][1])
