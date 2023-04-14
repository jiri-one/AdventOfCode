from pathlib import Path
import hupper
from string import ascii_lowercase, ascii_uppercase, punctuation
from dataclasses import dataclass, replace

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is XXX
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 33

# helper variables
unwanted_chars = ascii_lowercase + ascii_uppercase + punctuation
total_minutes: int = 24


@dataclass
class State(object):
    # All types are tuple: ore, clay, obsidian, geode
    ore_price: tuple
    clay_price: tuple
    obs_price: tuple
    geo_price: tuple
    mats: tuple = (0, 0, 0, 0)  # initial state of material
    robs: tuple = (1, 0, 0, 0)  # initial state of robots
    mins: int = 0 # minutes
    
    @property
    def score(self):
        return self.mats[-1]
    
    def __repr__(self):
        def f(resources):
            return '(' + ','.join(f'{n:2}' for n in resources) + ')'
        return f'<{self.mins:2}: m={f(self.mats)} r={f(self.robs)}>'

    def get_geodes(self):
        robs = self.robs
        mats = self.mats
        mins = self.mins
        while mins != total_minutes:
            build_robot = None
            for rob_i, rob_price in enumerate((self.ore_price, self.clay_price, self.obs_price, self.geo_price)):
                # buy robot if I can (but only if I don't have enough robots, or do not build more robots than needed to build another robot)
                new_mats = []
                if all(  # All current mats are higher (or same) then robot prices
                    mat >= price for mat, price in zip(mats, rob_price)
                ): # I can afford robot
                    #print(f"I can afford robot {cur_rob}")
                    build_robot = rob_i
                    for p, m in zip(rob_price, mats):
                        #print("p, m", p, m)
                        if p <= m:
                            m = m-p
                        new_mats.append(m)
                    new_mats = tuple(new_mats)
                    #print("new_mats", new_mats)
                    self.mats = new_mats
                    continue # But only one robot by one round
            # All robots continue to gather material
            mats = tuple(m+r for m, r in zip(mats, robs))
            #print("mats", self.mats)
            # and increase the number of robots
            #print(f"a tady checkuju {build_robot}")
            mins += 1
            if build_robot:
                robs = tuple(r+(1 if i == build_robot else 0) for i, r in enumerate(robs))
                yield replace(
                    self,
                    mins=mins,
                    mats=mats,
                    robs=robs
                )
        if not mins:
            yield replace(
                self,
                mins=mins,
                mats=mats,
            )
        
answer = 0
states = set()

best_score = -1
n = 0

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
        to_visit = [state]
        try:
            while state := to_visit.pop():
                n += 1
                if n % 10_000 == 0:
                    print(n, state)
                # print(state)
                if state.score > best_score:
                    best_score = state.score
                for new_state in state.get_geodes():
                    to_visit.append(new_state)
        except IndexError:
            print("BEST SCORE:", best_score)
        #print("XXXXXXXXXXx", state.mats)
        #print(states)
        break


def reload_runner():
    reloader = hupper.start_reloader("puzzle_by_time.reload_runner")


if __name__ == "__main__":
    reload_runner()
