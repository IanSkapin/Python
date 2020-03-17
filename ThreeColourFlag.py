"""
Given an array of nnn buckets, each containing a red, white, or blue pebble, sort them by color. The allowed operations
are:

    swap(i,j): swap the pebble in bucket i with the pebble in bucket j.
    color(i): determine the color of the pebble in bucket i.

The performance requirements are as follows:

    At most n calls to color().
    At most n calls to swap().
    Constant extra space.
"""

from random import randint


def random_arrey_of(size, elements):
    return [elements[randint(0, len(elements) - 1)] for i in range(size)]


class Pebble:
    def __init__(self, colour):
        self.colour = colour

    def __cmp__(self, other):
        if self.colour < other.colour:
            return -1
        if self.colour > other.colour:
            return 1
        return 0

    def