"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/

Medium

TC: O(log(n))
SC: O(1)
"""


def find_min(nums):

    l, r = 0, len(nums) - 1

    while l < r:
        m = (l + r) // 2

        # the minimum element is in the unsorted half
        if nums[m] > nums[r]:
            l = m + 1
        elif nums[m] <= nums[r]:
            r = m

    return nums[l]


# --------------------------------- #

print("Expected: 1. " "Got: ", find_min([3, 4, 5, 1, 2]))
print("Expected: 0. " "Got: ", find_min([4, 5, 6, 7, 0, 1, 2]))
print("Expected: 11. " "Got: ", find_min([11, 13, 15, 17]))
