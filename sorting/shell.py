""" Shell-Sort

is NOT STABLE and INPLACE sort

Complexity:

Worst   |   Average   |   Best
----------------------------------
 ?      |  ? ( < N^2) |    N


Move entries more than one position at a time
"""
from . import exchange


def sort(array):
    h = 1
    while h < len(array) / 3:
        h = 3 * h + 1

    while h >= 1:
        for i in range(h, len(array)):
            for j in range(i, 0, -h):
                if array[j] < array[j - h]:
                    exchange(array, j, j - h)
                else:
                    break
        h = int(h / 3)


