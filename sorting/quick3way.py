"""
private static void sort(Comparable[] a, int lo, int hi)
{
    if (hi <= lo) return;
    int lt = lo, gt = hi;
    Comparable v = a[lo];
    int i = lo;
    while (i <= gt)
    {
        int cmp = a[i].compareTo(v);
        if (cmp < 0) exch(a, lt++, i++);
        else if (cmp > 0) exch(a, i, gt--);
        else i++;
    }
    sort(a, lo, lt - 1);
    sort(a, gt + 1, hi);
}
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
