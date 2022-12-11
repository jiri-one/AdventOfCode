from pathlib import Path
from dataclasses import dataclass

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 50616
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 10605

# helper variables and classes
@dataclass
class Monkey:
    """Class for keeping monkey and it's (or my :-D) items in inventory."""
    nr: int # the monkey number
    items: list[int] # the items which monkey holds
    raiser: int | str = None # by how much or how many times it should be increased worry level
    mark: str = None # plus or multiplier
    divisible: int = None # Test: divisible by this value
    true_monkey: int = None # if test True
    false_monkey: int = None # if test False
    inspected_items: int = 0


    def operation(self, item):
        self.inspected_items += 1
        if self.raiser == "old":
            elm = item
        else:
            elm = int(self.raiser)
        if self.mark == "*":
            return int((item * elm) / 3)
        else: # self.mark == "+"
            return int((item + elm) / 3)
        
    
    def test(self, new_item):
        if new_item % self.divisible == 0:
            return self.true_monkey
        else:
            return self.false_monkey


monkeys: dict[int, Monkey] = {}
inspected_items: list[int] = []


# read the initial file
with open(main_input, "r") as file:
    while line:= file.readline():
        line = line.strip()
        match line.split():
            case ["Monkey", nr]:
                monkey = Monkey(int(nr[:-1]), []) # new monkey with empty item list
            case ["Operation:", "new", "=", "old", mark, raiser]:
                monkey.mark = mark
                monkey.raiser = raiser
            case ["Test:", "divisible", "by", divisible]:
                monkey.divisible = int(divisible)
            case ["If", "true:", "throw", "to", "monkey", true_monkey]:
                monkey.true_monkey = int(true_monkey)
            case ["If", "false:", "throw", "to", "monkey", false_monkey]:
                monkey.false_monkey = int(false_monkey)
            case ["Starting", "items:", *items]:
                for item in items:
                    monkey.items.append(int(item.strip(",")))
        monkeys[monkey.nr] = monkey


for _ in range(20):
    # I can do "for monkey in monkey.values()" and it will work in this case, but I don't like to iterate over changing values
    for nr in range(len(monkeys)): 
        monkey = monkeys[nr]
        while monkey.items:
            item = monkey.items.pop(0)
            new_item = monkey.operation(item)
            new_monkey = monkey.test(new_item)
            monkeys[new_monkey].items.append(new_item)

   
for monkey in monkeys.values():
    inspected_items.append(monkey.inspected_items)

inspected_items = sorted(inspected_items)
print(inspected_items[-1] * inspected_items[-2])
