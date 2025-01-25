"""
40. Combination Sum
https://leetcode.com/problems/combination-sum-ii/description/

Medium

TC: O(2^n)
SC: O(n)
"""


def combination_sum_ii(candidates, target):
    result = []
    candidates.sort()

    def backtrack(path, start, sum):
        if sum > target:
            return
        if sum == target:
            result.append(path[:])
            return

        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            path.append(candidates[i])
            backtrack(path, i + 1, sum + candidates[i])
            path.pop()

    backtrack([], 0, 0)
    return results
