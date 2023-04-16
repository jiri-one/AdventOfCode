from pathlib import Path
from string import ascii_lowercase, ascii_uppercase, punctuation
from dataclasses import dataclass, replace
from functools import lru_cache
import math

# input files
main_input = (
    Path(__file__).parent / "input.txt"
)  # result of this file is 851 for part 1 a 12160 for part 2
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 33

# helper variables
unwanted_chars = ascii_lowercase + ascii_uppercase + punctuation
total_minutes: int = 24


@dataclass(frozen=True)
class State(object):
    nr: int  # blueprint number
    mins: int  # minutes
    # All types are tuple: ore, clay, obsidian, geode
    ore_price: tuple
    clay_price: tuple
    obs_price: tuple
    geo_price: tuple
    max_price: tuple
    mats: tuple = (0, 0, 0, 0)  # initial state of material
    robs: tuple = (1, 0, 0, 0)  # initial state of robots

    @property
    @lru_cache
    def optimistic_estimate(self):
        # A number that's bigger (or same) as the best
        # score achievable from this node.
        mr = self.mins
        return self.score + self.robs[-1] * mr + (mr + 1) * mr // 2

    @property
    def score(self):
        return self.mats[-1]

    def __repr__(self):
        def f(resources):
            return "(" + ",".join(f"{n:2}" for n in resources) + ")"

        return f"<{self.mins:2}: m={f(self.mats)} r={f(self.robs)}>"

    def get_states(self):
        built_robot = False
        rob_prices = self.ore_price, self.clay_price, self.obs_price, self.geo_price
        for rob_i, (rob_price, current_robot_count, max_price) in enumerate(
            zip(rob_prices, self.robs, self.max_price)
        ):
            if any(p > 0 and r == 0 for p, r in zip(rob_price, self.robs)):
                continue
            if current_robot_count >= max_price:
                continue
            mats = self.mats
            mins = self.mins
            while mins:
                if all(  # All current mats are higher (or same) then robot prices, so I can afford this current robot
                    mat >= price for mat, price in zip(mats, rob_price)
                ):
                    break  # if Yes!
                mins -= 1
                # All robots continue to gather material
                mats = tuple(m + r for m, r in zip(mats, self.robs))
            if mins:  # don't buy robot on last minute
                # I'll spend the material for the robot
                mats = tuple(m - p for m, p in zip(mats, rob_price))
                mins -= 1  # time is still ticking
                # All robots continue to gather material
                mats = tuple(m + r for m, r in zip(mats, self.robs))
                # and increase the number of robots
                robs = tuple(
                    r + (1 if rob_i == i else 0) for i, r in enumerate(self.robs)
                )
                yield replace(
                    self,
                    mins=mins,
                    mats=tuple(
                        min(m, mp + (mp - r) * mins)
                        for m, mp, r in zip(
                            mats,
                            self.max_price,
                            robs,
                        )
                    ),
                    robs=robs,
                )
                built_robot = True

        if not built_robot and self.mins:
            # I will only wait, so only gather material
            mats = tuple(m + r * self.mins for m, r in zip(self.mats, self.robs))
            yield replace(
                self,
                mins=0,
                mats=mats,
            )


initial_states = []

# read the initial file
with open(main_input, "r") as file:
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
        prices = (
            (ore_rob, 0, 0, 0),
            (clay_rob, 0, 0, 0),
            (obsidian_rob_ore, obsidian_rob_clay, 0, 0),
            (geode_rob_ore, 0, geode_rob_obs, 0),
        )
        state = State(
            nr=blueprint,
            mins=total_minutes,
            ore_price=(ore_rob, 0, 0, 0),
            clay_price=(clay_rob, 0, 0, 0),
            obs_price=(obsidian_rob_ore, obsidian_rob_clay, 0, 0),
            geo_price=(geode_rob_ore, 0, geode_rob_obs, 0),
            max_price=(
                *[max(c) for c in zip(*prices)][:-1],
                float("inf"),
            ),
        )
        initial_states.append(state)


def get_answer(init_states, part):
    results = []
    for init_state in init_states:
        best_score = -1
        n = 0
        visited = set()
        to_visit = [init_state]
        while to_visit:
            state = to_visit.pop()
            if state.optimistic_estimate < best_score:
                continue
            if state in visited:
                continue
            visited.add(state)
            # n += 1
            # if n % 10_00 == 0:
            # print(n, state)
            # if n == 10:
            #     print(best_score)
            #     exit()
            if state.score > best_score:
                # print(f'best score:', state.score)
                best_score = state.score
            for new_state in state.get_states():
                to_visit.append(new_state)
        if part == 1:
            results.append(best_score * state.nr)
        else:
            results.append(best_score)
    if part == 1:
        return sum(results)
    else:
        return math.prod(results)


# answer for part 1
answer_part1 = get_answer(initial_states, 1)  # 1 like part 1
print(f"{answer_part1=}")

# answer for part 2 (change first states to 32 minutes)
states_for_part_2 = []
for state in initial_states[:3]:
    state = replace(state, mins=32)
    states_for_part_2.append(state)
answer_part2 = get_answer(states_for_part_2, 2)  # 2 like part 2
print(f"{answer_part2=}")
