from puzzle_2_try import sort_ranges, reduce_ranges
from random import shuffle

RANGES = [range(0, 39), range(1, 20), range(3, 60), range(70, 120), range(120, 130), range(150, 160)]
REDUCED_RANGES = [range(0, 60), range(70, 130), range(150, 160)]

def test_sort_ranges():
    shuffle_ranges = RANGES[:]
    shuffle(shuffle_ranges)
    sorted_ranges = sort_ranges(shuffle_ranges)
    assert sorted_ranges == RANGES

def test_reduce_ranges():
    origin_ranges = RANGES[:]
    reduced_ranges = reduce_ranges(origin_ranges)
    assert reduced_ranges == REDUCED_RANGES
