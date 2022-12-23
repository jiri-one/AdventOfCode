from collections import namedtuple

Robots = namedtuple('Robots', ['ore', 'clay', 'obsidian', 'geode'])
robots = Robots(1,0,0,1)
print(robots+1)
