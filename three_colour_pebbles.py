"""
Given an array of n buckets, each containing a red, white, or blue pebble, sort them by color. The allowed operations
are:

    swap(i,j): swap the pebble in bucket i with the pebble in bucket j.
    color(i): determine the color of the pebble in bucket i.

The performance requirements are as follows:

    At most n calls to color().
    At most n calls to swap().
    Constant extra space.
"""

from random import randint
from sorting import quick3way, merge
from zero_length_compression import compress
from functools import total_ordering


def random_array_of(size, elements):
    return [elements[randint(0, len(elements) - 1)] for _ in range(size)]


@total_ordering
class Pebble:
    def __init__(self, colour):
        self.colour = colour

    def __lt__(self, other):
        return self.colour < other.colour

    def __eq__(self, other):
        return self.colour == other.colour

    def __call__(self):
        return self.colour

    def __str__(self):
        return self.colour

    def __repr__(self):
        return self.__str__()


# quick solution
elements = [Pebble('read'), Pebble('white'), Pebble('blue')]
array = random_array_of(50000, elements)
array2 = array[:]
quick3way.sort(array)
print(compress(array))

# TODO double check it  merge is respecting the limitations:
#  max N compares and max N swaps

merge.sort_no_copy(array)
print(compress(array))
