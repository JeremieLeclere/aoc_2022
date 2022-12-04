# -*- coding: utf-8 -*-

import aoc2022_common as common

def parse_line(line):
    """ Parse provided line
    """
    ranges = []
    for pair in line.split(','):
        ranges.append([int(x) for x in pair.split('-')])
    return ranges

def check_contained(line):
    """ Check if a range is contained in the other
    """
    r = parse_line(line)
    return (r[0][0] >= r[1][0] and r[0][1] <= r[1][1]) \
        or (r[1][0] >= r[0][0] and r[1][1] <= r[0][1])

def check_overlap(line):
    """ Check if ranges overlap
    """
    r = parse_line(line)
    return (r[0][1] >= r[1][0] and r[0][0] <= r[1][0]) \
        or (r[1][1] >= r[0][0] and r[1][0] <= r[0][0])

# Load input data
_lines = common.load_input('input_day_4.txt')

# Parts 1 & 2
contained_ranges = 0
overlap_ranges = 0
for _line in _lines:

    # Check if a range if contained in the other
    if check_contained(_line):
        contained_ranges += 1

    # Check if ranges overlap
    if check_overlap(_line):
        overlap_ranges += 1

print('day 4 - part 1: Number of pairs in which one contains the other: {}'.format(contained_ranges))
print('day 4 - part 2: Number of pairs which overlaps: {}'.format(overlap_ranges))