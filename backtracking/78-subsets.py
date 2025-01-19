"""
78. Subsets
https://leetcode.com/problems/subsets/description/

Medium

TC: O(n * 2^n)
SC: O(n * 2^n)
"""


def subsets(nums):
    res = []

    def backtrack(path, start):
        res.append(path[:])

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(path, i + 1)
            path.pop()

    backtrack([], 0)
    return res
