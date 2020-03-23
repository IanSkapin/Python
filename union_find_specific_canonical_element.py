"""
Add a method find() to the union-find data type so that find(i) returns the largest element in the connected component
containing i. The operations, union(), connected(), and find() should all take logarithmic time or better.

For example, if one of the connected components is {1, 2, 6, 9}, then the find() method should
return 9 for each of the four elements in the connected components.
"""

import union_find



class CanonicalUnionFind(union_find.WeightedQuickUnion):
    def __init__(self, size):
        super().__init__(size)
        self.group_leader = {}

    def union(self, p, q):
        new_root, del_root = super().union(p, q)
        del_group_leader = self.group_leader.pop(str(del_root), 0)
        self.group_leader[str(new_root)] = max([p, q,
                                                self.group_leader.get(str(new_root), 0),
                                                del_group_leader])
        # print(f'{self.connections} <- union({p}, {q}): {self.group_leader}')

    def find(self, i):
        root = self.root(i)
        return self.group_leader.get(str(root), i)


if __name__ == '__main__':
    N = 10
    cuf = CanonicalUnionFind(N)

    for t, a, b in union_find.random_time_union_generator(N, N):
        cuf.union(a, b)

    print(' 0  1  2  3  4  5  6  7  8  9')
    print(f'{cuf.connections}')
    for e in range(N):
        canonical_element = cuf.find(e)
        print(f'for element {e}, {canonical_element} is the biggest in the group')
