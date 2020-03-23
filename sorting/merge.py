from . import insertion


def merge(a: list, aux: list, lo: int, mid: int, hi: int):
    # assert isSorted(a, lo, mid); // precondition: a[lo..mid] sorted
    # assert isSorted(a, mid+1, hi); // precondition: a[mid+1..hi] sorted
    aux[lo:hi+1] = a[lo:hi+1]

    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        if i > mid:
            a[k] = aux[j]
            j += 1
        elif j > hi:
            a[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            a[k] = aux[j]
            j += 1
        else:
            a[k] = aux[i]
            i += 1

    # assert isSorted(a, lo, hi); // postcondition: a[lo..hi] sorted


def __sort__(a: list, aux: list, lo: int, hi: int, cutoff=None):
    if cutoff:
        # switch to insertion sort for arrays smaller than cutoff
        if hi <= lo + cutoff - 1:
            insertion.sort(a[lo:hi+1])
            return
    else:
        if hi <= lo:
            return

    mid = int(lo + (hi - lo) / 2)
    __sort__(a, aux, lo,      mid, cutoff)
    __sort__(a, aux, mid + 1, hi,  cutoff)

    # skip merge if the biggest item in first half is smaller or equal to the smallest in the second half
    if a[mid] <= a[mid+1]:
        return
    merge(a, aux, lo, mid, hi)


def sort(a: list):
    aux = [0 for _ in range(len(a))]
    __sort__(a, aux, 0, len(a) - 1, cutoff=20)


# ## Time optimized
# Eliminate the copy to the auxiliary array. Save time (but not space)
# by switching the role of the input and auxiliary array in each recursive call.
def sort_no_copy(a: list):
    aux = a[:]
    sort_aux_to_a(aux, a, 0, len(a) - 1)


def merge_a_to_aux(a: list, aux: list, lo: int, mid: int, hi: int):
    i = lo
    j = mid + 1
    for k in range(lo, hi + 1):
        # merge from a[] to aux[]
        if i > mid:
            aux[k] = a[j]
            j += 1
        elif j > hi:
            aux[k] = a[i]
            i += 1
        elif a[j] < a[i]:
            aux[k] = a[j]
            j += 1
        else:
            aux[k] = a[i]
            i += 1


def sort_aux_to_a(a: list, aux: list, lo: int, hi: int):
    if hi <= lo:
        return
    mid = int(lo + (hi - lo) / 2)
    # Note: sort(a) initializes aux[] and sets
    # aux[i] = a[i] for each i.
    sort_aux_to_a(aux, a, lo,    mid)
    sort_aux_to_a(aux, a, mid+1, hi)
    # switch roles of aux[] and a[]
    merge_a_to_aux(a, aux, lo, mid, hi)


# ## Bottom Up Merge Sort
# 10% slower than the recursive
def sort_bottom_up(a: list):
    aux = [0 for _ in range(len(a))]
    sz = 1
    while sz < len(a):
        lo = 0
        while lo < len(a) - sz:
            merge(a, aux, lo, lo + sz - 1, min(lo + sz + sz - 1, len(a) - 1))
            lo += sz + sz
        sz += sz

