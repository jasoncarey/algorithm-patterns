"""
33. Search in Rotated Sorted Array
https://leetcode.com/problems/search-in-rotated-sorted-array/

Medium

TC: O(log(n))
SC: O(1)
"""


def search(nums, target):

    # find pivot
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m

    pivot = l

    # determine which side of pivot target is in
    if nums[pivot] == target:
        return pivot
    elif nums[pivot] < target <= nums[-1]:
        l, r = pivot + 1, len(nums) - 1
    else:
        l, r = 0, pivot - 1

    # normal binary search for target
    while l <= r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        elif nums[m] < target:
            l = m + 1
        else:
            r = m - 1

    return -1


# --------------------------------- #

print("Expected: 4. " "Got: ", search([4, 5, 6, 7, 0, 1, 2], 0))
print("Expected: -1. " "Got: ", search([1], 0))
print("Expected: 1. " "Got: ", search([1, 3], 3))
