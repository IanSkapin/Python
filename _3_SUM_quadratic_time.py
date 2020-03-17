"""
Design an algorithm for the 3-SUM problem that takes time proportional to n^2 in the worst case. You may assume that you
can sort the n integers in time proportional to n^2 or better.
"""


from BinarySearch import BinarySearch


class Find3Sum:
    def __init__(self, integer_array):
        self.array = BinarySearch(integer_array)

    def find(self, count=1, find_all=False):
        matches = []
        for i, x in enumerate(self.array):
            for j, y in enumerate(self.array[i + 1:]):
                # print(f'x[i]: {x}[{i}]  y[j]: {y}[{j}]')
                if match := self.array.has(integer=-(x + y),
                                           start=i + j + 1):
                    # print(f'match at {match}')
                    matches.append((x, y, self.array[match]))
                    count -= 1
                if not find_all and count <= 0:
                    return matches
        return matches


"""
from _3_SUM_quadratic_time import Find3Sum

o = Find3Sum([100, 80, 60, 40, 20, 0, -10, -30, -50, -70, -90])
o.find()

"""