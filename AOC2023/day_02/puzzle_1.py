from pathlib import Path
from sys import argv
from dataclasses import dataclass

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 2348
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 8

if len(argv) > 1 and argv[1] == "--test":
    main_input = test_input

# helper variables
cubes = {"red": 12, "green": 13, "blue": 14}
games = []

impossible_games = set()

# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        print(line)
        if len(line) != 0:
            game_nr = int(line.split(":")[0].removeprefix("Game "))
            games.append(game_nr)
            raw_game = [r.strip() for r in line.split(":")[1].strip().split(";")]
            rounds = []
            game = []
            for raw_round in raw_game:
                cubes_in_round = raw_round.strip().split(", ")
                for one_color in cubes_in_round:
                    nr_of_cubes, color_of_cubes = one_color.split()
                    real_cubes_in_this_color = cubes.get(color_of_cubes)
                    if real_cubes_in_this_color < int(nr_of_cubes):
                        impossible_games.add(game_nr)


possible_games = [game for game in games if game not in impossible_games]
print(sum(possible_games))
