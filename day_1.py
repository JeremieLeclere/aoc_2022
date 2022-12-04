#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aoc2022_common as common

# Load input data
_lines = common.load_input('input_day_1.txt')

# Parts 1 & 2
_sum = 0
_elves = []

for _line in _lines:

    if (len(_line.strip())) == 0:
        # List for current elf is over
        _elves.append(_sum)
        _sum = 0
    else:
        # Keep building current list
        _sum += int(_line.strip())

max_elf = max(_elves)
top_3_elves = sum(sorted(_elves)[-3:])

print('day 1 - part 1: Elf is carrying {} calories'.format(max_elf))
print('day 1 - part 2: Top 3 elves are carrying {} calories'.format(top_3_elves))
