from binary_search import BinarySearch


def smallest_missing_positive_nonzero(array):
    """find the smallest missing positive and nonzero element in the given array"""
    bs = BinarySearch(array)
    lo = None
    for i in range(1, bs[-1] + 2):
        if (x := bs.has(i, start=lo)) is False:
            return i
        else:
            lo = x
