"""
973. K Closest Points to Origin
https://leetcode.com/problems/k-closest-points-to-origin/description/

Medium

TC: O(nlog(k))
SC: O(k)
"""

from typing import List
import heapq
import math


def k_closest(points: List[List[int]], k: int) -> List[List[int]]:
    heap = []

    for point in points:
        d = distance_origin(point)
        if len(heap) >= k:
            heapq.heappushpop(heap, [-d, point])
        else:
            heapq.heappush(heap, [-d, point])

    return [point for _, point in heap]


def distance_origin(point):
    return math.sqrt(point[0] ** 2 + point[1] ** 2)
