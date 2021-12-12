# result of test_input.txt file have to be 26984457539 and for input.txt it is XXX
with open("test_input.txt", "r") as file:
    lines_list = file.read().splitlines()

lanternfish_list = [int(item) for item in lines_list[0].split(",")]

total_days = 256

class Counter(object):
    def __init__(self):
        self.counter = 0
    
    def __call__(self):
        self.counter += 1

counter = Counter()

def finish_fish(fish, start_day):
    counter()
    for day in range(start_day,total_days+1):
        fish -= 1
        if fish == -1:
            finish_fish(8, day+1)
            fish = 6

for lanternfish in set(lanternfish_list):
    number_of_repeated = lanternfish_list.count(lanternfish)
    if number_of_repeated > 1:
        counter_start_value = counter.counter
        finish_fish(lanternfish, 1)
        counter_end_value = counter.counter
        counter.counter += (number_of_repeated - 1) * (counter_end_value - counter_start_value)
    else: # number_of_repeated > 1:
        finish_fish(lanternfish, 1)
          
print(counter.counter)
