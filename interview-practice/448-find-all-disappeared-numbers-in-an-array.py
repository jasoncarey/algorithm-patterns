# 448. Find All Disappeared Numbers in an Array
# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array

# TC: O(n)
# SC: O(n)

from typing import List


class Solution:
    def find_disappeared_numbers(self, nums: List[int]) -> List[int]:
        n = len(nums) + 1
        seen = [False] * n

        for num in nums:
            seen[num] = True

        print(seen)
        disappeared_numbers = [i for i in range(1, n) if seen[i] == False]
        return disappeared_numbers


class OptimalSolution:
    # TC: O(n)
    # SC: O(1)
    def missing_number(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = -abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]


if __name__ == "__main__":
    s = Solution()

    input_1 = [4, 3, 2, 7, 8, 2, 3, 1]
    print(s.find_disappeared_numbers(input_1))
    # Expect [5, 6]

    input_2 = [1, 1]
    print(s.find_disappeared_numbers(input_2))
    # Expect [2]
