from pathlib import Path
import hupper
from string import ascii_lowercase, ascii_uppercase, punctuation
from dataclasses import dataclass
from pprint import pprint
from copy import deepcopy
from collections import namedtuple

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 33

# helper variables
unwanted_chars = ascii_lowercase + ascii_uppercase + punctuation

# helper functions and classes
Price = namedtuple('Price', ['ore', 'clay', 'obsidian'])

@dataclass
class BluePrint:
    nr: int
    prices: dict[str, Price[int,int,int]] # material prices are: ore, clay, obsidian


Materials = namedtuple('Materials', ['ore', 'clay', 'obsidian', 'geode'])
Robots = namedtuple('Robots', ['ore', 'clay', 'obsidian', 'geode'])

# current blueprint state
state: dict = {"mats": Materials(0, 0, 0, 0), # materials: ore, clay, obsidian
               "robs": Robots(1, 0, 0, 0), # robots: ore, clay, obsidian, geode
               "bp": None, # BluePrint
               "mins": 24} # minutest to the end

blueprints = []
answer = 0

def cretate_states(state):
    # if I have material, buy robot
    for price in enumerate(state["bp"].prices.values()):
         minutes_to_end = state["mins"]
         mats = state["mats"]
         robs = state["robs"]
         while minutes_to_end:
             if 
             minutes_to_end -= 1
             mats = Materials(  mats.ore + robs.ore,
                                mats.clay + robs.clay,
                                mats.obsidian + robs.obsidian,
                                mats.geode + robs.geode)
             print(minutes_to_end, mats)
    
    # if I don't have material, wait


def get_best_score(blueprint, minutes):
    global state
    init = deepcopy(state)
    init["bp"] = blueprint
    init["mins"] = minutes
    to_visit = [init]
    while to_visit:
        state = to_visit.pop()
        cretate_states(init)
    return 42


# read the initial file
with open(test_input, "r") as file:
    while line:= file.readline():
        for char in unwanted_chars: line = line.replace(char, "")
        line_list = [int(x) for x in line.split()]
        blueprint, ore_rob, clay_rob, obsidian_rob_ore, obsidian_rob_clay, geode_rob_ore, geode_rob_obs = line_list
        blueprint = BluePrint(
            nr = blueprint,
            prices = {"ore_rob": Price(ore_rob, 0, 0),
                      "clay_rob": Price(clay_rob, 0, 0),
                      "obsidian_rob": Price(obsidian_rob_ore, obsidian_rob_clay, 0),
                      "geode_rob": Price(geode_rob_ore, 0, geode_rob_obs)})
        blueprints.append(blueprint)
        pprint(blueprints)


for blueprint in blueprints:
    geodes = get_best_score(blueprint, 24)
    print(f'{blueprint=}', f'{geodes=}')
    answer += geodes * blueprint.nr

print(f'{answer=}')

def reload_runner():
    reloader = hupper.start_reloader('puzzle_1.reload_runner')

if __name__ == "__main__":
    reload_runner()
