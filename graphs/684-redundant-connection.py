"""
684. Redundant Connection
https://leetcode.com/problems/redundant-connection/description/

Medium

TC: O(n)
SC: O(n)
"""


class UnionFind:
    def __init__(self):
        self.parent = {}
        self.rank = {}

    def find(self, x):
        if x not in self.parent:
            self.parent[x] = x
            self.rank[x] = 0
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # cycle
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


def find_redundant_connection(edges):
    union_find = UnionFind()
    last_redundant = []

    for edge in edges:
        if not union_find.union(edge[0], edge[1]):
            last_redundant = edge

    return last_redundant
