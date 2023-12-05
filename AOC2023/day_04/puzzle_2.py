from pathlib import Path
from sys import argv
from dataclasses import dataclass

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 13768818
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 30

if len(argv) > 1 and argv[1] == "--test":
    main_input = test_input

# helper variables
@dataclass
class Card:
    card: int
    count: int
    matching_numbers: int

    def increase_count(self):
        self.count += 1

    
total_cards:  dict[int, Card] = dict() # dict with key of card number and value is Card instance

# read the initial file
with open(main_input, "r") as file:
    while line := file.readline():
        line = line.strip()
        card = int(line.split(":")[0].removeprefix("Card "))
        part1, part2 = line.split(":")[1].split("|")
        win_numbers: set = set(int(n) for n in part1.strip().split())
        my_numbers: set = set(int(n) for n in part2.strip().split())
        common_numbers: set = win_numbers.intersection(my_numbers)
        matching_numbers: int = len(common_numbers)
        # initial cards, for now we have only 1 card from all card numbers
        total_cards[card] = Card(card, 1, matching_numbers)

for nr in range(1, len(total_cards)+1):
    card = total_cards[nr]
    matching_numbers = card.matching_numbers
    for _ in range(card.count):
        for card_copy_nr in range(nr+1, nr+matching_numbers+1):
            one_of_next_cards = total_cards[card_copy_nr]
            one_of_next_cards.increase_count()

cards_count = 0
for card in total_cards.values():
    cards_count += card.count

print(cards_count)
print("__________________________")
