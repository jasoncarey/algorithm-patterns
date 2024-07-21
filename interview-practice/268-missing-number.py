# 268. Missing Number
# https://leetcode.com/problems/missing-number/

# TC: O(n)
# SC: O(n)

from typing import List

class Solution:
    def missing_number(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            seen[num] = True
        for i in range(len(nums)+1):
            if i not in seen:
                return i
        return

if __name__ == "__main__":
    s = Solution()

    i_1 = [3, 0, 1]
    print(s.missing_number(i_1))

    i_2 = [0, 1]
    print(s.missing_number(i_2))

    i_3 = [9,6,4,2,3,5,7,0,1]
    print(s.missing_number(i_3))

    i_4 = []
    print(s.missing_number(i_4))

    i_5 = [1]
    print(s.missing_number(i_5))
