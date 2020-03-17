
from random import randint

class QuickFind:
    """ complexity:
    initialize  -> N
    union       -> N
    find        -> 1
    Union is too expensive. It takes N 2 array accesses to process a sequence of N union commands on N objects.
    """
    def __init__(self, size):
        self.connections = [i for i in range(size)]

    def connected(self, p, q):
        return self.connections[p] == self.connections[q]

    def union(self, p, q):
        p_group = self.connections[p]
        q_group = self.connections[q]
        for idx, group in enumerate(self.connections):
            print(f'{idx}[{group}]')
            if group == p_group:
                self.connections[idx] = q_group
                print(f'New Union: {idx}[{q_group}]')


class QuickUnion:
    """ complexity
    initialize  -> N
    union       -> N (worst case)
    find        -> N (Worst case)
    Is faster than QuickFind but still to slow for huge numbers of elements and connections.
    """
    def __init__(self, size):
        self.connections = [i for i in range(size)]

    def root(self, idx):
        while idx != self.connections[idx]:
            idx = self.connections[idx]
        return idx

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        self.connections[p_root] = q_root


class WeightedQuickUnion:
    """ complexity:
    initialize  -> N
    union       -> lg N (worst case)
    find        -> lg N (Worst case)

    Is faster than QuickFind but still to slow for huge numbers of elements and connections.

    We can further improve this using path compression. In our case we make each examined point point to its grandfather.
    complexity then becomes:
    N + M lg* N (close to linear)
    """
    def __init__(self, size, path_compression=True):
        self.path_compression = path_compression
        self.connections = [i for i in range(size)]
        self.weights = [1 for i in range(size)]

    def root(self, idx):
        while idx != self.connections[idx]:
            if self.path_compression:
                self.connections[idx] = self.connections[self.connections[idx]]
            idx = self.connections[idx]

        return idx

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        p_root = self.root(p)
        q_root = self.root(q)
        if self.weights[q_root] <= self.weights[p_root]:
            self.connections[q_root] = p_root
            self.weights[p_root] += self.weights[q_root]
            return p_root, q_root
        else:
            self.connections[p_root] = q_root
            self.weights[q_root] += self.weights[p_root]
            return q_root, p_root


def random_time_union_generator(elements, max_entries=10000):
    for time in range(int(max_entries)):
        yield time, randint(0, elements - 1), randint(0, elements - 1)
