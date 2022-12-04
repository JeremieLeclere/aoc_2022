#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import aoc2022_common as common

# Defines with associated base score
ROCK     = 1
PAPER    = 2
SCISSORS = 3

# Defines with associated weight
LOOSE    = 0
DRAW     = 3
WIN      = 6

# Dictionary to map letter to a shape
code_2_shape = {
                'A' : ROCK,
                'B' : PAPER,
                'C' : SCISSORS,
                'X' : ROCK,
                'Y' : PAPER,
                'Z' : SCISSORS
               }

# Dictionary to map strategy requirement to a score
code_2_score = {
                'X' : 0,
                'Y' : 3,
                'Z' : 6
               }

def rps_round_1(line):
    """ Compute round score according to first draft of rules:
            - First letter is the shape played by the opponent
            - Second letter is the shape played by us

        Score is equal to the sum of values associated to result and shape
        we played.
    """
    # Get elve shape
    opponent = code_2_shape[line.strip().split()[0]]

    # Get self shape
    me = code_2_shape[line.strip().split()[1]]

    # Get score from shapes
    if me == opponent:
        score = DRAW
    else:
        if me == ROCK:
            if opponent == PAPER:
                score = LOOSE
            else:
                score = WIN
        elif me == PAPER:
            if opponent == ROCK:
                score = WIN
            else:
                score = LOOSE
        else:
            if opponent == ROCK:
                score = LOOSE
            else:
                score = WIN

    score += me

    return score

def rps_round_2(line):
    """ Compute round score according to first draft of rules:
            - First letter is the shape played by the opponent
            - Second letter is the result we're expected to reach

        Score is equal to the sum of values associated to result and shape
        we played.
    """
    # Get elve shape
    opponent = code_2_shape[line.strip().split()[0]]

    # Get expected result (directly as score)
    score = code_2_score[line.strip().split()[1]]

    if score == LOOSE:
        if opponent == ROCK:
            score += SCISSORS
        elif opponent == PAPER:
            score += ROCK
        else:
            score += PAPER
    elif score == DRAW:
        score += opponent
    else:
        if opponent == ROCK:
            score += PAPER
        elif opponent == PAPER:
            score += SCISSORS
        else:
                score += ROCK

    return score

# Load input data
_lines = common.load_input('input_day_2.txt')

# Parts 1 & 2
score_1 = 0
score_2 = 0
for _line in _lines:
    score_1 += rps_round_1(_line)
    score_2 += rps_round_2(_line)

print('day 2 - part 1: Expected score: {}'.format(score_1))
print('day 2 - part 2: Expected score: {}'.format(score_2))