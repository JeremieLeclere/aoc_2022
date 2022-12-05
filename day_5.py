#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from queue import LifoQueue

class Stack:
    """ Simple wrapper around LIFO queue
    """
    def __init__(self):
        """ Initialize self as a LIFO queue
        """
        self.queue = LifoQueue()

    def put(self, value):
        """ Add a value to the top of the stack
        """
        self.queue.put(value)

    def put_multiple(self, values):
        """ Add a list of values to the top of the stack
        """
        for value in values:
            self.queue.put(value)

    def get(self):
        """ Get first value of the stack
        """
        return self.queue.get()

    def get_multiple(self, nb_values):
        """ Get first nb_values of the stack without changing their order
        """
        values = []
        for i in range(nb_values):
            values.append(self.queue.get())
        values.reverse()
        return values

    def show_top(self):
        """ Return element at top of stck without removing it
        """
        return self.queue.queue[-1]

    def __repr__(self):
        """ Debug: print representation
        """
        return 'Stack({})'.format(self.queue.queue)


def load_stacks(lines):
    """ Load stacks initial states from input data
    """
    # Extract stacks description section
    stack_lines = []
    for line in lines:
        if len(line) == 0:
            break
        stack_lines.append(line)

    # We do not want stacks IDs, AND input data is provided in
    # a non convenient way ...
    stack_lines = stack_lines[:-1]
    stack_lines.reverse()

    # Initialize Stacks array
    nb_stacks = int((len(stack_lines[0]) + 1) / 4)
    stacks = [None] * nb_stacks
    for i in range(nb_stacks):
        stacks[i] = Stack()

    # Parse stacks
    for line in stack_lines:
        line += ' '
        for i in range(nb_stacks):
            elt = line[4*i:4*(i+1)].strip().replace('[','').replace(']','')
            if len(elt) > 0:
                stacks[i].put(elt)

    return stacks


def parse_line(line):
    """ Parse a move instruction
    """
    line = line.strip().split()
    nb = int(line[1])
    src = int(line[3]) - 1
    dst = int(line[5]) - 1
    return nb, src, dst


# Load input data (do not use aoc2022_common method here, we want
# to keep everything, included spaces)
fd = open('input_day_5.txt')
_input_data = [line.replace('\n','') for line in fd.readlines()]
fd.close()

# Part 1 - CrateMover 9000
# Get stacks initial status
_stacks = load_stacks(_input_data)

# Proceed to moves
for _line in _input_data:
    if 'move' not in _line:
        continue
    _nb, _src, _dst = parse_line(_line)
    for i in range(_nb):
        _stacks[_dst].put(_stacks[_src].get())

# Show stacks top items
CrateMover9000 = []
for _stack in _stacks:
    CrateMover9000.append(_stack.show_top())
print('Day 5 - part 1 : CrateMover 9000 results in \'{}\''.format(''.join(CrateMover9000)))


# Part 2 - CrateMover 9001
# Get stacks initial status
_stacks = load_stacks(_input_data)

# Proceed to moves
for _line in _input_data:
    if 'move' not in _line:
        continue

    _nb, _src, _dst = parse_line(_line)
    _stacks[_dst].put_multiple(_stacks[_src].get_multiple(_nb))

# Show stacks top items
CrateMover9001 = []
for _stack in _stacks:
    CrateMover9001.append(_stack.show_top())
print('Day 5 - part 2 : CrateMover 9001 results in \'{}\''.format(''.join(CrateMover9001)))
