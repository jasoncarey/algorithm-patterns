"""
1584. Min Cost to Connect All Points
https://leetcode.com/problems/min-cost-to-connect-all-points/description/

Medium

TC: O(n^2 * log(n))
SC: O(n)
"""

import heapq


def prim_mst(graph, start):
    visited = set()
    heap = [(0, start, None)]
    total_cost = 0
    mst_edges = []

    while heap:
        weight, node, parent = heapq.heappop(heap)
        if node in visited:
            continue
        visited.add(node)
        total_cost += weight
        if parent is not None:
            mst_edges.append((parent, node, weight))

        for neighbour, edge_weight in graph.get(node, []):
            if neighbour not in visited:
                heapq.heappush(heap, (edge_weight, neighbour, node))

    return total_cost, mst_edges


def manhattan_distance(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])


def min_cost_connect_points(points):
    graph = defaultdict(list)
    n = len(points)

    # build graph with custom weight function
    for i in range(n):
        for j in range(i + 1, n):
            w = manhattan_distance(points[i], points[j])
            graph[i].append((j, w))
            graph[j].append((i, w))

    cost, _ = prim_mst(graph, 0)
    return cost


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
            return False
        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1
        return True


def kruskal_mst(nodes, edges):
    uf = UnionFind()
    total_cost = 0
    mst_edges = []

    edges.sort()

    for w, u, v in edges:
        if uf.union(u, v):
            total_cost += w
            mst_edges.append((u, v, w))
            if len(mst_edges) == len(nodes) - 1:
                break

    return total_cost, mst_edges


def kruskal_min_cost_connect_points(points):
    n = len(points)
    nodes = list(range(n))
    edges = []

    for i in range(n):
        for j in range(i + 1, n):
            dist = manhattan_distance(points[i], points[j])
            edges.append((dist, i, j))

    cost, _ = kruskal_mst(nodes, edges)
    return cost
