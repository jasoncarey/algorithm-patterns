"""
39. Combination Sum
https://leetcode.com/problems/combination-sum/description/

Medium

TC: O(2^n)
SC: O(n)
"""


class Solution:
    def combination_sum(self, candidates, target):
        res = []

        def backtrack(path, start, sum):
            if sum > target:
                return
            if sum == target:
                res.append(path[:])
                return

            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(path, i, sum + candidates[i])  # not i + 1 because we can reuse elements
                path.pop()

        backtrack([], 0, 0)
        return res


if __name__ == "__main__":
    solution = Solution()
    candidates = [2, 3, 6, 7]
    target = 7
    result = solution.combination_sum(candidates, target)
    print(f"Result: {result}")
