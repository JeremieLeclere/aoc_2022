# -*- coding: utf-8 -*-

def load_input(filename):
    """ Load input data as a list of lines, stripped from return symbol
    """
    with open(filename) as fd:
        lines = fd.readlines()

    return [line.strip() for line in lines]
