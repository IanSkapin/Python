"""
Design an algorithm for the 3-SUM problem that takes time proportional to n^2 in the worst case. You may assume that you
can sort the n integers in time proportional to n^2 or better.
"""


from binary_search import BinarySearch


def find(integer_array, count=1, find_all=False):
    """

    Args:
        integer_array:
        count:
        find_all:

    Returns:

    """
    array = BinarySearch(integer_array)
    matches = []
    for i, x in enumerate(array):
        for j, y in enumerate(array[i + 1:]):
            # print(f'x[i]: {x}[{i}]  y[j]: {y}[{j}]')
            if match := array.has(integer=-(x + y), start=i + j + 1):
                # print(f'match at {match}')
                matches.append((x, y, array[match]))
                count -= 1
            if not find_all and count <= 0:
                return matches
    return matches


"""
import sum_of_3

sum_of_3.find([100, 80, 60, 40, 20, 0, -10, -30, -50, -70, -90])


"""