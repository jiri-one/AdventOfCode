from pathlib import Path
from sys import argv

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 2286

if len(argv) > 1 and argv[1] == "--test":
    main_input = test_input

# helper variables
cubes = {"red": 12, "green": 13, "blue": 14}
powers = []


# read the initial file
with open(main_input, "r") as file:
    for line in file:
        line = line.strip()
        print(line)
        if len(line) != 0:
            game_nr = int(line.split(":")[0].removeprefix("Game "))
            raw_game = [r.strip() for r in line.split(":")[1].strip().split(";")]
            highest_cubes = {"red": 1, "green": 1, "blue": 1}
            for raw_round in raw_game:
                cubes_in_round = raw_round.strip().split(", ")
                for one_color in cubes_in_round:
                    nr_of_cubes, color_of_cubes = one_color.split()
                    nr_of_cubes = int(nr_of_cubes)
                    if nr_of_cubes > highest_cubes[color_of_cubes]:
                        highest_cubes[color_of_cubes] = nr_of_cubes
            game_power = highest_cubes["red"] * highest_cubes["green"] * highest_cubes["blue"]
            powers.append(game_power)

print(sum(powers))
