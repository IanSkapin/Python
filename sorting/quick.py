""" Quick sort and Quick-select
### Quick sort

Algorithm:
    Repeat until i and j pointers cross.
    ・ Scan i from left to right so long as (a[i] < a[lo]) .
    ・ Scan j from right to left so long as (a[j] > a[lo]) .
    ・ Exchange a[i] with a[j] .

    When pointers cross.
    ・ Exchange a[lo] with a[j] .

### Quick-select
Get the N-th item by size from the randomized list

Algorithm:
    Partition array so that:
    ・ Entry a[j] is in place.
    ・ No larger entry to the left of j.
    ・ No smaller entry to the right of j.

    Repeat in one subarray, depending on j; finished when j equals k.

Complexity:
    average: linear time
    worst: ~(N^2)/2

"""
import random

from . import exchange, median_of_3
from . import insertion


def partition(a: list, lo: int, hi: int):
    i = lo
    j = hi + 1
    while True:
        while a[(i := i + 1)] < a[lo]:
            if i == hi:
                break

        while a[lo] < a[(j := j - 1)]:
            pass

        if i >= j:
            break
        exchange(a, i, j)

    exchange(a, lo, j)
    return j


def sort(a: list, cutoff=None):
    random.shuffle(a)
    __sort__(a, 0, len(a) - 1, cutoff)


def __sort__(a: list, lo: int, hi: int, cutoff=None):
    if cutoff:
        if hi <= lo + cutoff - 1:
            insertion.sort(a, lo, hi)
            return
    else:
        if hi <= lo:
            return

    # try getting the partition closer to the middle
    m = median_of_3(a, lo, lo + (hi - lo) / 2, hi)
    exchange(a, lo, m)

    j = partition(a, lo, hi)
    __sort__(a, lo, j - 1, cutoff)
    __sort__(a, j + 1, hi, cutoff)




### Quick-select
def select(a: list, k: int):
    random.shuffle(a)
    lo = 0
    hi = len(a) - 1
    while hi > lo:
        j = partition(a, lo, hi)
        if j < k:
            lo = j + 1
        elif j > k:
            hi = j - 1
        else:
            return a[k]
    return a[k]
