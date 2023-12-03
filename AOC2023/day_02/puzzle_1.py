from pathlib import Path
from sys import argv
from dataclasses import dataclass

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 8

if len(argv) > 1 and argv[1] == "--test":
    main_input = test_input

# helper variables
@dataclass
class Round:
    red: int = 0
    green: int = 0
    blue: int = 0

    def __gt__(self, other):
        return self.red > other.red and self.green > other.green and self.blue > other.blue
    
    def __lt__(self, other):
        return self.red < other.red and self.green < other.green and self.blue < other.blue

cubes = Round(**{"red": 12, "green": 13, "blue": 14})

impossible_games = set()

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        if len(line) != 0:
            game_nr = int(line.split(":")[0].removeprefix("Game "))
            raw_game = [r.strip() for r in line.split(":")[1].strip().split(";")]
            rounds = []
            for raw_round in raw_game:
                round = Round()
                cobes_in_round = raw_round.strip().split(", ")
                for one_color in cobes_in_round:
                    nr_of_cubes, color_of_cubes = one_color.split()
                    setattr(round, color_of_cubes, int(nr_of_cubes))
                if cubes > round:
                    continue
                else:
                    impossible_games.add(game_nr)

possible_games = [game for game in range(1, game_nr+1) if game not in impossible_games]
print(sum(possible_games))
print("--------------------------------")
