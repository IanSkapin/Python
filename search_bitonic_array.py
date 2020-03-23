"""
An array is bitonic if it is comprised of an increasing sequence of integers followed immediately by a decreasing
sequence of integers. Write a program that, given a bitonic array of n distinct integer values, determines whether a
given integer is in the array.

    Standard version: Use ∼3 lg n compares in the worst case.

    Signing bonus:  Use ∼2 lg n compares in the worst case (and prove that no algorithm can guarantee to perform fewer
                    than ∼2 lg n compares in the worst case).

Hints:
    Standard version. First, find the maximum integer using ∼1lg⁡n compares—this divides the array into the increasing and decreasing pieces.

    Signing bonus. Do it without finding the maximum integer.
"""
from random import randint
from collections import deque
import binary_search


def generate_bitonic_array(length, max_step=10):
    length = length if length > 2 else 3
    array = [randint(-length, length)]
    for i in range(length - 1):
        array.append(randint(array[-1] + 1, array[-1] + max_step))
    array.reverse()
    bitonic = deque()
    for i in array:
        if randint(0, 1):
            bitonic.append(i)
        else:
            bitonic.appendleft(i)

    return bitonic


def is_in_bitonic_array(integer, array, debug=False):
    def get_mid(low, high):
        return round((low + high) / 2)

    def search(low, high, descending=False):
        return binary_search.search(array, integer, low, high, descending, debug)

    def max(low, high, local_max=0):
        if low > high:
            return local_max
        mid = get_mid(low, high)
        if debug:
            print(f'{low}:{mid}:{high} local max: array[{local_max}]={array[local_max]} # {array[low]}:{array[mid]}:{array[high]}')

        if array[low] <= array[mid] <= array[high]:
            if array[local_max] <= array[high]:
                return max(mid, high, local_max=high) if low < mid < high else high
            else:
                return local_max
        elif array[low] >= array[mid] >= array[high]:
            if array[local_max] <= array[low]:
                return max(low, mid, local_max=low) if low < mid < high else low
            else:
                return local_max
        if array[local_max] < array[(new_max := max(low, mid, local_max=local_max))]:
            local_max = new_max
        if array[local_max] < array[(new_max := max(mid + 1, high, local_max=local_max))]:
            local_max = new_max
        return local_max

    array_max = max(0, len(array) - 1)
    if debug:
        print(f'max is {array[array_max]} at {array_max}')
    if (match := search(0, array_max)) is not False:
        return match
    if (match := search(array_max + 1, len(array) - 1, descending=True)) is not False:
        return match
    return False


if __name__ == '__main__':
   if True:
        import time
        min_e = 1
        max_e = 1
        for N in [2, 4, 8, 16, 32, 64]:
            N = N * 100000
            a = generate_bitonic_array(N)
            var = max(a)
            start = time.time()
            rc = is_in_bitonic_array(var, a)
            elapsed = time.time() - start
            x = elapsed/min_e
            min_e = elapsed if elapsed > 0 else 1
            print(f'N: {N} Time: {elapsed} rc: {rc} val: {a[rc]}, ratio: {x}')
            a = generate_bitonic_array(N)
            var = min(a) - 1
            start = time.time()
            rc = is_in_bitonic_array(var, a)
            elapsed = time.time() - start
            x = elapsed/max_e
            max_e = elapsed if elapsed > 0 else 1
            print(f'N: {N} Time: {elapsed} rc: {rc} ratio:{x}')
        exit()
   else:
        N = 100
        a = generate_bitonic_array(N)
        #a = [4, 83, 139, 146, 230, 304, 371, 314, 265, 257]
        #a = [-6, -1, 7, 11, 15, 18, 26, 34, 23, 21]
        #a = [72, 82, 91, 95, 103, 125, 158, 178, 185, 188, 193, 195, 220, 222, 239, 251, 255, 266, 274, 277, 287, 292, 307, 312, 334, 339, 349, 356, 358, 368, 370, 384, 392, 397, 407, 424, 434, 448, 469, 500, 510, 517, 533, 554, 585, 589, 580, 573, 564, 549, 547, 542, 531, 522, 519, 494, 486, 481, 474, 462, 459, 457, 451, 439, 437, 435, 418, 417, 375, 366, 363, 326, 322, 299, 281, 267, 260, 247, 240, 236, 231, 224, 212, 206, 205, 203, 183, 175, 166, 165, 152, 142, 140, 139, 130, 116, 107, 80, 68, 65]
        print(a)
        for i in a:
            print(i)
            if is_in_bitonic_array(i, a) is False:
                print(f'Error failed to find {i}, running with debug')
                print(is_in_bitonic_array(i, a, True))
            i += 1
            if i not in a:
                if is_in_bitonic_array(i, a) is not False:
                    print(f'Error found {i}, running with debug')
                    print(is_in_bitonic_array(i, a, True))
