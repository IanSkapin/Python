"""
Given two arrays a[] and b[], each containing n distinct 2D points in the plane, design a subquadratic algorithm to
count the number of points that are contained both in array a[] and array b[].
"""
from sorting.shell import sort
from binary_search import search
from functools import total_ordering


@total_ordering
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x or self.x == other.x and self.y < other.y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f'P({self.x}, {self.y})'


a = [Point2D(3, 4),
     Point2D(1, 1),
     Point2D(5, 9),
     Point2D(7, 2),
     Point2D(9, 1),
     Point2D(5, 5),
     Point2D(7, 8),
     Point2D(6, 4)]

b = [Point2D(0, 0),
     Point2D(5, 9),
     Point2D(6, 6),
     Point2D(7, 2),
     Point2D(4, 3),
     Point2D(7, 8),
     Point2D(9, 9)]


def count_common_points(array1, array2):
    sort(array2)
    count = 0
    for p1 in array1:
        if match := search(array2, p1, 0, len(array2)):
            print(f'{p1} == {array2[match]}')
            count += 1
    return count


print(count_common_points(a, b))

