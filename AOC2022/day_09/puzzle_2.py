from pathlib import Path

# input files
main_input = Path(__file__).parent / "input.txt"  # result of this file is 2793
test_input = Path(__file__).parent / "test_input.txt"  # result of this file is 1


class SnakePiece:
    def __init__(self, follow=None):
        self.follow = follow
        x: int = 0
        y: int = 0
        coor: tuple[x, y] = (x, y)
        self.cur_head: coor = (x, y)
        self.cur_tail: coor = (x, y)
        self.coor_tail_trail: set[coor] = {(x, y)}  # initial coor of tail to the set

    def get_surround_coor_set(self):
        """
        Return the set of 9 coordinates, which are around given coor and the coor itself.
        If the head is in this set, the tail does not need to move.
        """
        x = self.cur_tail[0]
        y = self.cur_tail[1]
        return {
            (x, y),  # overlap of head and tail
            (x - 1, y),  # left
            (x + 1, y),  # right
            (x, y + 1),  # up
            (x, y - 1),  # down
            (x - 1, y + 1),  # left-up
            (x - 1, y - 1),  # left-down
            (x + 1, y + 1),  # right-up
            (x + 1, y - 1),
        }  # right-down

    def move_tail(self):
        if self.cur_head not in self.get_surround_coor_set():
            xt, yt, xh, yh = (
                self.cur_tail[0],
                self.cur_tail[1],
                self.cur_head[0],
                self.cur_head[1],
            )
            if yt == yh and xt != xh:
                if xh > xt:
                    self.cur_tail = (xt + 1, yt)  # move tail right
                else:
                    self.cur_tail = (xt - 1, yt)  # move tail left
            elif yt != yh and xt == xh:
                if yh > yt:
                    self.cur_tail = (xt, yt + 1)  # move tail up
                else:
                    self.cur_tail = (xt, yt - 1)  # move tail down
            else:  # diagonal shifting of head
                if xh == xt + 1 and yh == yt + 2:  # diagonally up right (x+1,y+2)
                    self.cur_tail = (xt + 1, yt + 1)
                elif xh == xt - 1 and yh == yt + 2:  # diagonally up left (x-1,y+2)
                    self.cur_tail = (xt - 1, yt + 1)
                elif xh == xt + 1 and yh == yt - 2:  # diagonally down right (x+1,y-2)
                    self.cur_tail = (xt + 1, yt - 1)
                elif xh == xt - 1 and yh == yt - 2:  # diagonally down left (x-1,y-2)
                    self.cur_tail = (xt - 1, yt - 1)
                elif xh == xt + 2 and yh == yt + 1:  # diagonally right up (x+2,y+1)
                    self.cur_tail = (xt + 1, yt + 1)
                elif xh == xt + 2 and yh == yt - 1:  # diagonally left up (x+2,y-1)
                    self.cur_tail = (xt + 1, yt - 1)
                elif xh == xt - 2 and yh == yt + 1:  # diagonally right down (x-2,y+1)
                    self.cur_tail = (xt - 1, yt + 1)
                elif xh == xt - 2 and yh == yt - 1:  # diagonally left down (x-2,y-1)
                    self.cur_tail = (xt - 1, yt - 1)
                elif xh == xt + 2 and yh == yt + 2:  # # diagonally right up (x+2,y+2)
                    self.cur_tail = (xt + 1, yt + 1)
                elif xh == xt - 2 and yh == yt - 2:  # diagonally left down (x-2,y-2)
                    self.cur_tail = (xt - 1, yt - 1)
                elif xh == xt + 2 and yh == yt - 2:  # diagonally right down (x+2,y-2)
                    self.cur_tail = (xt + 1, yt - 1)
                elif xh == xt - 2 and yh == yt + 2:  # diagonally right down (x-2,y-2)
                    self.cur_tail = (xt - 1, yt + 1)
                else:  # this is here only for debug purposes, this shouldn't happen
                    print("I dont know what to do.")
                    print(self.cur_tail, self.cur_head)
                    exit()

            self.coor_tail_trail.add(self.cur_tail)

            # this is important part, where are other knots updated
            if self.follow:
                self.follow.cur_head = self.cur_tail
                self.follow.move_tail()

    def move_head(self, cmd, steps):
        x, y = self.cur_head[0], self.cur_head[1]
        for _ in range(steps):
            if cmd == "U":  # we are going UP
                y += 1
            elif cmd == "D":  # we are going DOWN
                y -= 1
            elif cmd == "L":  # we are going LEFT
                x -= 1
            elif cmd == "R":  # we are going RIGHT
                x += 1
            self.cur_head = (x, y)
            self.move_tail()

    def __call__(self, cmd, step):
        self.move_head(cmd, step)


# 9 knots/pieces and 10th is tail
tail_8 = SnakePiece()
tail_7 = SnakePiece(tail_8)
tail_6 = SnakePiece(tail_7)
tail_5 = SnakePiece(tail_6)
tail_4 = SnakePiece(tail_5)
tail_3 = SnakePiece(tail_4)
tail_2 = SnakePiece(tail_3)
tail_1 = SnakePiece(tail_2)
head = SnakePiece(tail_1)


# read the initial file
with open(main_input, "r") as file:
    while line := file.readline():
        line = line.strip()
        cmd, steps = line.split()
        head(cmd, int(steps))


print(len(tail_8.coor_tail_trail))
