"""
46. Permutations
https://leetcode.com/problems/permutations/description/

Medium

TC: O(n!)
SC: O(n)
"""


def permute(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if used[i] == True:
                continue
            path.append(nums[i])
            used[i] = True
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return result
