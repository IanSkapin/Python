""" Priority Queue
implementation  |   insert   |   del max   |   max
------------------------------------------------------
unordered array |   1        |   N         |   N
ordered array   |   N        |   1         |   1
goal            |   log N    |   log N     |   log N

"""
from . import exchange


MAX = 'maximum'


class UnorderedPQ:
    __slots__ = 'queue', 'mode'

    def __init__(self, mode=MAX):
        self.queue = []
        self.mode = mode
        self.compare = (lambda best, current: self.queue[best] < self.queue[current]) if self.mode == MAX else \
            (lambda best, current: self.queue[best] > self.queue[current])

    def is_empty(self):
        return len(self.queue) == 0

    def insert(self, x):
        self.queue.append(x)

    def pop(self):
        best = 0
        for i in range(len(self.queue)):
            if self.compare(best, i):
                best = i
        exchange(self.queue, best, len(self.queue) - 1)
        return self.queue.pop()


class OrderedPQ:
    pass


class BinaryHeapList(list):
    def __getitem__(self, item):
        return super().__getitem__(item - 1)

    def __setitem__(self, key, value):
        super().__setitem__(key - 1, value)


class BinaryHeap:
    def __init__(self, mode=MAX):
        self.queue = BinaryHeapList()
        self.mode = mode
        self.compare = (lambda best, current: self.queue[best] < self.queue[current]) if self.mode == MAX else \
            (lambda best, current: self.queue[best] > self.queue[current])

    def swim(self, k):
        while k > 1 and self.compare((half_k := k//2),  k):
            exchange(self.queue, k, half_k)
            k = half_k

    def insert(self, x):
        self.queue.append(x)
        self.swim(len(self.queue))

    def sink(self, k):
        while 2 * k <= len(self.queue):
            j = 2 * k
            if j < len(self.queue) and self.compare(j, j + 1):
                j += 1
            if not self.compare(k, j):
                break
            exchange(self.queue, k, j)
            k = j

    def pop(self):
        exchange(self.queue, 1, len(self.queue))
        self.sink(1)
        return self.queue.pop()

    def is_empty(self):
        return len(self.queue) == 0

