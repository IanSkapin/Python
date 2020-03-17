
def exchange(a, i, j):
    tmp = a[i]
    a[i] = a[j]
    a[j] = tmp


def median_of_3(a: list, lo: int, mid: int, hi: int):
    l = a[lo]
    m = a[mid]
    h = a[hi]
    if l <= m:
        if m <= h:
            return mid
        else:
            if l < h:
                return hi
            else:
                return lo
    else:
        if l <= h:
            return lo
        else:
            if m < h:
                return hi
            else:
                return mid


def ninther(a: list):
    """ Tukey's ninther
    Median of the median of 3 samples, each of 3 entries.
    ・ Approximates the median of 9.
    ・ Uses at most 12 compares.
    """
    k = int(len(a) / 9)
    k0, k1, k2, k3, k4, k5, k6, k7, k8 = list(range(0, 9 * k, k))

    mid1 = median_of_3(a, k0, k1, k2)
    mid2 = median_of_3(a, k3, k4, k5)
    mid3 = median_of_3(a, k6, k7, k8)
    return median_of_3(a, mid1, mid2, mid3)
