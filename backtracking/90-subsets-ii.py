"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/description/

Medium

nums[i] == nums[i-1] checks for duplicates
i > start ensures only duplicates within the same recursive level are skipped

TC: O(n * 2^n)
SC: O(n * 2^n)
"""


def subsets_with_dupe(nums):

    result = []
    nums.sort()

    def backtrack(path, start):
        result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue
            path.append(nums[i])
            backtrack(path, i + 1)
            path.pop()

    backtrack([], 0)
    return result
