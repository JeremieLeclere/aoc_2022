# -*- coding: utf-8 -*-

import aoc2022_common as common

def get_priority(letter):
    """ Convert a letter to priority value:
            - [1..26] for lower case letters,
            - [27..52] for upper case letters
    """
    # Map lowered case letter to [1..26]
    priority = ord(letter.lower()) - 96

    # Add 26 if upper case
    if letter.isupper():
        priority += 26

    return priority


def find_common(data):
    """ Find common letter in a list of strings (/!\ expected to be unique)
    
        Ref: https://stackoverflow.com/questions/70480885/find-common-character-in-list-of-strings
    """
    # Use sorted() function to convert set to a list
    common = sorted(set.intersection(*map(set,data)))

    # Sure input data is correct, but just in case problem's not there ...
    assert len(common) == 1

    return common[0]


def inspect_rucksack(data):
    """ Search for common item in both halves of a given rursack, and return
        associated priority
    """
    # Search for the only letter that is in both halves of the list
    half = int(len(data)/2)
    common = find_common([data[0:half], data[half:]])

    # Return letter converted to priority
    return get_priority(common)


def inspect_group(data):
    """"" Search for common item in a rursack group, and return
        associated priority
    """
    # Search for common letter in group rursacks
    common = find_common(data)

    # Return letter converted to priority
    return get_priority(common)


# Load input data
_lines = common.load_input('input_day_3.txt')

# Part 1: Items priorities
single_priorities_sum = 0
for _line in _lines:
    single_priorities_sum += inspect_rucksack((_line.strip()))


print('day 3 - part 1: Sum of objects priorities: {}'.format(single_priorities_sum))

# Part 2: Group items priorities
_nb_groups = int(len(_lines) / 3)

group_priorities_sum = 0
for _i in range(_nb_groups):
    _group_data = [line.strip() for line in _lines[3*_i:3*(_i+1)]]
    group_priorities_sum += inspect_group(_group_data)

print('day 3 - part 2: Sum of objects priorities: {}'.format(group_priorities_sum))
