""" Selection-Sort

is NOT STABLE and INPLACE sort

Complexity:

Worst   |   Average   |   Best
----------------------------------
(N^2)/2 |  (N^2)/2    |  (N^2)/2

does N exchanges
"""

from . import exchange


def sort(a):
    for i in range(len(a)):
        low = i
        for j in range(i + 1, len(a)):
            if a[j] < a[low]:
                low = j
        if low != i:
            exchange(a, i, low)
