"""
703. Kth Largest Element in a Stream
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Easy

TC: O(n*log(k)), O(log(k))
SC: O(k)
"""

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.h = []
        self.k = k
        for i, num in enumerate(nums):
            if i < k:
                heapq.heappush(self.h, num)
            else:
                heapq.heappushpop(self.h, num)

    def add(self, val: int) -> int:
        if len(self.h) < self.k:
            heapq.heappush(self.h, val)
        else:
            heapq.heappushpop(self.h, val)

        return self.h[0]
