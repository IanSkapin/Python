""" Quick-3way-Sort
Is a quick sort alternative for sorting arrays with multiple duplicate keys.

Partition array into 3 parts so that:
・ Entries between lt and gt equal to partition item v.
・ No larger entries to left of lt.
・ No smaller entries to right of gt.

Implementation:
・ Let v be partitioning item a[lo] .
・ Scan i from left to right.
    – (a[i] < v) : exchange a[lt] with a[i] ; increment both lt and i
    – (a[i] > v) : exchange a[gt] with a[i] ; decrement gt
    – (a[i] == v) : increment i


"""
import random
from . import exchange


def sort(a: list):
    random.shuffle(a)
    __sort__(a, 0, len(a) - 1)


def __sort__(a: list, lo: int, hi: int):
    if hi <= lo:
        return
    lt = lo
    gt = hi
    v = a[lo]
    i = lo
    while i <= gt:
        if a[i] < v:
            exchange(a, lt, i)
            lt += 1
            i += 1
        elif a[i] > v:
            exchange(a, i, gt)
            gt -= 1
        else:
            i += 1

    __sort__(a, lo, lt - 1)
    __sort__(a, gt + 1, hi)
