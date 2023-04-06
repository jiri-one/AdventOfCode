from pathlib import Path
import hupper
from string import ascii_lowercase, ascii_uppercase, punctuation
from dataclasses import dataclass

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 33

# helper variables
unwanted_chars = ascii_lowercase + ascii_uppercase + punctuation

@dataclass
class State(object):
    # All types are tuple: ore, clay, obsidian, geode
    ore_price: tuple
    clay_price: tuple
    obs_price: tuple
    geo_price: tuple
    materials: tuple = (0, 0, 0, 0) # initial state
    robots: tuple = (1, 0, 0, 0) # initial state of robots
    
    def get_states(self, ore_price, clay_price, obs_price, geo_price):
        pass

answer = 0
states = set()

# read the initial file
with open(test_input, "r") as file:
    while line := file.readline():
        for char in unwanted_chars:
            line = line.replace(char, "")
        line_list = [int(x) for x in line.split()]
        (
            blueprint,
            ore_rob,
            clay_rob,
            obsidian_rob_ore,
            obsidian_rob_clay,
            geode_rob_ore,
            geode_rob_obs,
        ) = line_list
        state = State(
        ore_price = (ore_rob, 0, 0, 0),
        clay_price = (clay_rob, 0, 0, 0),
        obs_price = (obsidian_rob_ore, obsidian_rob_clay, 0, 0),
        geo_price = (geode_rob_ore, 0, geode_rob_obs, 0),
        )
        print(states)
        exit()
        
def reload_runner():
    reloader = hupper.start_reloader("puzzle_test.reload_runner")


if __name__ == "__main__":
    reload_runner()        
