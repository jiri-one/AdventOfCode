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

def test_reduce_ranges_which_dont_need_to_reduce():
    some_ranges = [range(0, 1), range(45, 56), range(93, 93), range(97, 100)]
    reduced_ranges = reduce_ranges(some_ranges)
    assert some_ranges == reduced_ranges
