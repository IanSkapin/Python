"""
Given a social network containing N members and a log file containing M timestamps at which times pairs of members
formed friendships, design an algorithm to determine the earliest time at which all members are connected (i.e., every
member is a friend of a friend of a friend ... of a friend). Assume that the log file is sorted by timestamp and that
friendship is an equivalence relation. The running time of your algorithm should be M log N or better and
use extra space proportional to N.
"""

import UnionFind

N = 10



class SoNet(UnionFind.WeightedQuickUnion):
    def all_connected(self):
        return len(self.connections) == self.connections.count(self.connections[0])

sn = SoNet(N)

for entry in UnionFind.random_time_union_genrator(N, N * N):
    t, a, b = entry
    sn.union(a, b)
    # print(f'{a} <=> {b} : {sn.connections}')
    if sn.all_connected():
        print(f'They all became friends at {t}')
        break
