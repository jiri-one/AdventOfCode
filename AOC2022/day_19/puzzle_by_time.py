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
    mats: tuple = (0, 0, 0, 0)  # initial state of material
    robs: tuple = (1, 0, 0, 0)  # initial state of robots

    def get_geodes(self):
        minutes = 24
        minute = 1
        while minute != minutes+1:
            print(f"{minute} MINUTE")
            robs = self.robs
            mats = self.mats
            cur_rob = 3 # current robot
            build_robot = None
            for rob_price in (self.geo_price, self.obs_price, self.clay_price, self.ore_price):
                # buy robot if I can (but only if I don't have enough robots, or do not build more robots than needed to build another robot)
                new_mats = []
                if all(  # All current mats are higher (or same) then robot prices
                    mat >= price for mat, price in zip(mats, rob_price)
                ): # I can afford robot
                    print(f"I can afford robot {cur_rob}")
                    build_robot = cur_rob
                    for p, m in zip(rob_price, mats):
                        print("p, m", p, m)
                        if p <= m:
                            m = m-p
                        new_mats.append(m)
                    new_mats = tuple(new_mats)
                    print("new_mats", new_mats)
                    self.mats = new_mats
                    break # But only one robot by one round
                cur_rob -= 1
            # All robots continue to gather material
            self.mats = tuple(m+r for m, r in zip(self.mats, self.robs))
            print("mats", self.mats)
            # and increase the number of robots
            print(f"a tady checkuju {build_robot}")
            if build_robot:
                print("jsem zde")
                self.robs = tuple(r+(1 if i == build_robot else 0) for i, r in enumerate(robs))
                print("robs", self.robs)
            minute += 1
            if minute == 10:
                print("current mats", self.mats)
                print("current robs", self.robs)
                break
                

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
            ore_price=(ore_rob, 0, 0, 0),
            clay_price=(clay_rob, 0, 0, 0),
            obs_price=(obsidian_rob_ore, obsidian_rob_clay, 0, 0),
            geo_price=(geode_rob_ore, 0, geode_rob_obs, 0),
        )
        state.get_geodes()
        #print("XXXXXXXXXXx", state.mats)
        #print(states)
        break


def reload_runner():
    reloader = hupper.start_reloader("puzzle_by_time.reload_runner")


if __name__ == "__main__":
    reload_runner()
