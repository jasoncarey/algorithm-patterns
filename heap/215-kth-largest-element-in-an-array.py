"""
1046. Kth Largest Element in an Array
https://leetcode.com/problems/kth-largest-element-in-an-array

Medium

TC: O(nlog(k))
SC: O(k)
"""

import heapq


def find_kth_largest(nums, k):
    heap = []

    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        else:
            heapq.heappushpop(heap, num)

        return heap[0]
