"""
743. Network Delay Time
https://leetcode.com/problems/network-delay-time/description/

Medium

TC: O((V + E) * log(V))
SC: O(V + E)
"""

import heapq
from collections import defaultdict


def dijkstra(graph, source):
    dist = {}
    heap = [(0, source)]  # distance, node

    while heap:
        cost, node = heapq.heappop(heap)
        if node in dist:
            continue  # already visited with shorter path

        dist[node] = cost

        for neighbour, weight in graph.get(node, []):
            if neighbour not in dist:
                heapq.heappush(heap, (cost + weight, neighbour))

    return dist


def network_delay_time(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    dist = dijkstra(graph, source=k)
    if len(dist) == n:
        return max(dist.values())
    else:
        return -1
