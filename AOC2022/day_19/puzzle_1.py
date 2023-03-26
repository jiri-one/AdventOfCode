from pathlib import Path
import hupper
from string import ascii_lowercase, ascii_uppercase, punctuation
from dataclasses import dataclass
from pprint import pprint
from copy import deepcopy
from collections import namedtuple

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 33

# helper variables
unwanted_chars = ascii_lowercase + ascii_uppercase + punctuation

# helper functions and classes
Price = namedtuple("Price", ["ore", "clay", "obsidian", "geode"])
Materials = namedtuple("Materials", ["ore", "clay", "obsidian", "geode"])
Robots = namedtuple("Robots", ["ore", "clay", "obsidian", "geode"])


@dataclass
class BluePrint:
    nr: int
    prices: dict[str, Price[int, int, int]]  # robot are: ore, clay, obsidian, geode


# current blueprint state
state: dict = {
    "mats": Materials(0, 0, 0, 0),  # materials: ore, clay, obsidian
    "robs": Robots(1, 0, 0, 0),  # robots: ore, clay, obsidian, geode
    "bp": None,  # BluePrint
    "mins": 24,  # minutest to the end
}

blueprints = []
answer = 0


def cretate_states(state):
    bp_prices = state["bp"].prices
    for robot, prices in bp_prices.items():
        minutes_to_end = state["mins"]
        mats = state["mats"]
        robs = state["robs"]
        # if I don't have material, I can't buy robot
        if any(price > 0 and rob == 0 for price, rob in zip(prices, robs)):
            continue
        # if I have material, let's go buy robotm but check that first
        while minutes_to_end:
            # Can I buy robot?
            if all(  # All mats are higher then prices
                mat >= price for mat, price in zip(mats, prices)
            ):
                # Yes, I can buy this robot!
                break
            # I don't have mats, so only mining
            minutes_to_end -= 1
            mats = Materials(
                mats.ore + robs.ore,
                mats.clay + robs.clay,
                mats.obsidian + robs.obsidian,
                mats.geode + robs.geode,
            )
            print(minutes_to_end, mats)
        if minutes_to_end:
            # Buy a robot (remove material)
            mats = Materials(
                mats.ore - prices.ore,
                mats.clay - prices.clay,
                mats.obsidian - prices.obsidian,
                mats.geode - prices.geode,
            )
            minutes_to_end -= 1
            # And the robots continue to mine
            mats = Materials(
                mats.ore + robs.ore,
                mats.clay + robs.clay,
                mats.obsidian + robs.obsidian,
                mats.geode + robs.geode,
            )
            # And increase the number of current robot
            robs = Robots(
                robs.ore + int(robot == "ore_rob"),
                robs.clay + int(robot == "clay_rob"),
                robs.obsidian + int(robot == "obsidian_rob"),
                robs.geode + int(robot == "geode_rob"),
            )
            # At the end crate new state
            new_state = deepcopy(state)
            new_state["mins"] = minutes_to_end
            new_state["mats"] = mats
            new_state["robs"] = robs
            yield new_state

    # if I don't have material, wait


def get_best_score(blueprint, minutes):
    global state
    init = deepcopy(state)
    init["bp"] = blueprint
    init["mins"] = minutes
    print(init)
    to_visit = [init]
    best_score = -1
    best_state = None
    while to_visit:
        state = to_visit.pop()
        if state["mats"].geode > best_score:
            best_score = state["mats"].geode
            best_state = deepcopy(state)
        for new_state in cretate_states(state):
            print("------------------")
            print(new_state)
            to_visit.append(new_state)
    return best_score


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
        blueprint = BluePrint(
            nr=blueprint,
            prices={
                "ore_rob": Price(ore_rob, 0, 0, 0),
                "clay_rob": Price(clay_rob, 0, 0, 0),
                "obsidian_rob": Price(obsidian_rob_ore, obsidian_rob_clay, 0, 0),
                "geode_rob": Price(geode_rob_ore, 0, geode_rob_obs, 0),
            },
        )
        blueprints.append(blueprint)
        # pprint(blueprints)


for blueprint in blueprints:
    geodes = get_best_score(blueprint, 24)
    print(f"{blueprint} \n___ {geodes=}")
    answer += geodes * blueprint.nr
    break

print(f"{answer=}")


def reload_runner():
    reloader = hupper.start_reloader("puzzle_1.reload_runner")


if __name__ == "__main__":
    reload_runner()
