from itertools import chain
from functools import reduce
from math import log10


def split_merge(ls, digit):
    buf = [[] for _ in range(10)]
    divisor = 10 ** digit
    for n in ls:
        buf[(n // divisor) % 10].append(n)
    return chain(*buf)


def sort(ls, fn=split_merge):
    return list(reduce(fn, range(int(log10(max(abs(val) for val in ls)) + 1)), ls))
