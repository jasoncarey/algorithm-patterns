# 15. 3Sum
# https://leetcode.com/problems/3sum/
# Medium
# Two Pointers

# TC: O(n^2)
# SC: O(n)

from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:

    nums.sort()
    n = len(nums)
    results = []

    for i in range(n - 2):
        if i > 0 and nums[i - 1] == nums[i]:
            continue

        j, k = i + 1, n - 1

        while j < k:
            curr_sum = nums[i] + nums[j] + nums[k]
            if curr_sum == 0:
                results.append((nums[i], nums[j], nums[k]))
                j += 1
                while j < k and nums[j - 1] == nums[j]:
                    j += 1

                k -= 1
                while j < k and nums[k + 1] == nums[k]:
                    k -= 1
            elif curr_sum < 0:
                j += 1
            else:
                k -= 1

    return results


# --------------------------------- #

print("Expected: [[-1,-1,2],[-1,0,1]]. " "Got: ", three_sum([-1, 0, 1, 2, -1, 4]))
print("Expected: [[0,0,0]]. " "Got: ", three_sum([0, 0, 0, 0]))
print("Expected: [[-1,0,1]]. " "Got: ", three_sum([1, -1, -1, 0]))
print("Expected: [[-2,0,2], [-2,1,1]]. " "Got: ", three_sum([-2, 0, 1, 1, 2]))
