from pathlib import Path
import numpy as np

# input files
main_input = Path(__file__).parent / "input.txt" # result of this file is 6745
test_input = Path(__file__).parent / "test_input.txt" # result of this file is 13

# helper variables
x: int = 0
y: int = 0
coor: tuple[x, y] = (x, y)
cur_head: coor = (x, y)
cur_tail: coor = (x, y)
coor_tail_trail: set[coor] = {(0, 0)}

# helper functions
def get_surround_coor_set():
    """
    Return the set of 9 coordinates, which are around given coor and the coor itself.
    If the head is in this set, the tail does not need to move.
    """
    x = cur_tail[0]
    y = cur_tail[1]
    return {(x, y), # overlap head and tail
            (x-1, y), # left
            (x+1, y), # right
            (x, y+1), # up
            (x, y-1), # down
            (x-1, y+1), # left-up
            (x-1, y-1), # left-down
            (x+1, y+1), # right-up
            (x+1, y-1)} # right-down


def move_tail():
    global cur_tail
    if cur_head not in get_surround_coor_set():
        xt, yt, xh, yh = cur_tail[0], cur_tail[1], cur_head[0], cur_head[1]
        if yt == yh and xt != xh:
            if xh > xt: cur_tail = (xt + 1, yt) # move tail right
            else: cur_tail = (xt-1, yt) # move tail left
        elif yt != yh and xt == xh:
            if yh > yt: cur_tail = (xt, yt + 1) # move tail up
            else: cur_tail = (xt, yt - 1) # move tail down
        else: # diagonal shifting of head
            if xh == xt+1 and yh == yt+2: # diagonally up right (y+2)
                cur_tail = (xt+1, yt+1)
            elif xh == xt-1 and yh == yt+2: # diagonally up left (y+2)
                cur_tail = (xt-1, yt+1)
            elif xh == xt+1 and yh == yt-2: # diagonally down right (y-2)
                cur_tail = (xt+1, yt-1)
            elif xh == xt-1 and yh == yt-2: # diagonally down left (y-2)
                cur_tail = (xt-1, yt-1)
            elif xh == xt+2 and yh == yt+1: # diagonally right up (x+2)
                cur_tail = (xt+1, yt+1)
            elif xh == xt+2 and yh == yt-1: # diagonally left up (x+2)
                cur_tail = (xt+1, yt-1)
            elif xh == xt-2 and yh == yt+1: # diagonally right down (x-2)
                cur_tail = (xt-1, yt+1)
            elif xh == xt-2 and yh == yt-1: # diagonally left down (x-2)
                cur_tail = (xt-1, yt-1)
        
        coor_tail_trail.add(cur_tail)

     
def move_head(cmd, steps):
    global cur_head
    x, y = cur_head[0], cur_head[1]
    for _ in range(steps):
        if cmd == "U": # we are going UP
            y += 1
        elif cmd == "D": # we are going DOWN
            y -= 1
        elif cmd == "L": # we are going LEFT
            x -= 1
        elif cmd == "R": # we are going RIGHT
            x += 1
        cur_head = (x, y)
        move_tail()


# read the initial file
with open(main_input, "r") as file:
    while line:= file.readline():
        line = line.strip()
        cmd, steps = line.split()
        move_head(cmd, int(steps))


print(len(coor_tail_trail))
        
        
