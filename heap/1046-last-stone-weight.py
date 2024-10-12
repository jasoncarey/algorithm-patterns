"""
1046. Last Stone Weight
https://leetcode.com/problems/last-stone-weight/description/

Easy

TC: O(n*log(n))
SC: O(n)
"""

from typing import List
import heapq


def last_stone_weight(stones: List[int]) -> int:
    maxHeap = [-stone for stone in stones]
    heapq.heapify(maxHeap)

    while len(maxHeap) > 1:
        first, second = heapq.heappop(maxHeap), heapq.heappop(maxHeap)
        if first != second:
            heapq.heappush(maxHeap, first - second)

    return -maxHeap[0] if maxHeap else 0
