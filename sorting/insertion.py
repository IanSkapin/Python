""" Insertion Sort

INPLACE and STABLE

  Worst   |   Average   |   Best
  N^2/4       N^2/4         N

Good for:
 - small N
 - partially ordered

"""

from . import exchange


def sort(a: list, lo: int = None, hi: int = None):
    lo = lo or 0
    size = hi + 1 or len(a)
    for i in range(size):
        for j in range(i, lo, -1):
            if a[j] < a[j - 1]:
                exchange(a, j, j - 1)
            else:
                break
