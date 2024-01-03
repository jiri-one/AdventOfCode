from puzzle_2_try import sort_ranges
from random import shuffle

RANGES = [range(0, 39), range(1, 20), range(3, 60), range(70, 120), range(150, 160)]

def test_sort_ranges():
    shuffle_ranges = RANGES[:]
    shuffle(shuffle_ranges)
    sorted_ranges = sort_ranges(shuffle_ranges)
    assert sorted_ranges == RANGES
