from pathlib import Path
import hupper
from string import ascii_lowercase, ascii_uppercase, punctuation
from dataclasses import dataclass
from pprint import pprint
from copy import deepcopy

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 33

# helper variables
unwanted_chars = ascii_lowercase + ascii_uppercase + punctuation

# helper functions and classes
@dataclass
class BluePrint:
    nr: int
    prices: dict[str, tuple[int,int,int]] # material prices are: ore, clay, obsidian

# current blueprint state
state: dict = {"materials": (0, 0, 0), # ore, clay, obsidian
               "robots": (1, 0, 0, 0), # ore, clay, obsidian, geode robot; one ore robot for start
               "blueprint": None,
               "minutes_to_end": 24}

blueprints = []
answer = 0

def cretate_states(state):
    # if I have material, buy robot
    for index, price in state["blueprint"].prices.values():
         minutes_to_end = state["minutest_to_end"]
         materials = state["materials"]
         robots = state["robots"]
         while minutes_to_end:
             minutes_to_end -= 1
             materials = (
                 materials[index] + robots[index], 
             )
    
    # if I don't have material, wait

# read the initial file
with open(test_input, "r") as file:
    while line:= file.readline():
        for char in unwanted_chars: line = line.replace(char, "")
        line_list = [int(x) for x in line.split()]
        blueprint, ore_rob, clay_rob, obsidian_rob_ore, obsidian_rob_clay, geode_rob_ore, geode_rob_obs = line_list
        blueprint = BluePrint(
            nr = blueprint,
            prices = {"ore_rob": (ore_rob, 0, 0),
                      "clay_rob": (clay_rob, 0, 0),
                      "obsidian_rob": (obsidian_rob_ore, obsidian_rob_clay, 0),
                      "geode_rob": (geode_rob_ore, 0, geode_rob_obs)})
        blueprints.append(blueprint)
        pprint(blueprints)

def get_best_score(blueprint, minutes):
    init = deepcopy(state)
    init["blueprint"] = blueprint
    init["minutes_to_end"] = minutes
    to_visit = [init]
    while to_visit:
        state = to_visit.pop()
        cretate_states(init)

for blueprint in blueprints:
    geodes = get_best_score(blueprint, 24)
    print(f'{blueprint=}', f'{geodes=}')
    answer += geodes * blueprint.nr

print(f'{answer=}')

def reload_runner():
    reloader = hupper.start_reloader('puzzle_1.reload_runner')

if __name__ == "__main__":
    reload_runner()
