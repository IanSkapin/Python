"""
Given a set of nnn integers S={0,1,...,n−1} and a sequence of requests of the following form:

    Remove x from S
    Find the successor of x: the smallest y in S such that y ≥ x.

design a data type so that all operations (except construction) take logarithmic time or better in the worst case.
"""
from union_find_specific_canonical_element import CanonicalUnionFind
from union_find import random_time_union_generator


class Successor(CanonicalUnionFind):
    def __init__(self, size):
        super().__init__(size + 1)

    def remove(self, x):
        if x == self.connections[x]:
            self.union(x + 1, x)

    def find(self, x):
        group_max = super().find(x)
        if group_max == self.root(group_max):
            return group_max
        return self.find(group_max + 1)


N = 10
s = Successor(N)
print('removing:')
for _, e, _ in random_time_union_generator(N-1, 5):
    s.remove(e)
    print(f'{e}')

print(' 0  1  2  3  4  5  6  7  8  9')
print(f'{s.connections}')

for e in range(len(s.connections)):
    successor = s.find(e)
    print(f'{successor} is successor of {e}')

