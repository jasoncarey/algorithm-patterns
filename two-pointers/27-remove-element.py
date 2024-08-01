# 27. Remove Element
# https://leetcode.com/problems/remove-element
# Two pointers

from typing import List


def remove_element(nums: List[int], val: int) -> int:

    i, k = 0, len(nums)

    while i < k:
        if nums[i] != val:
            i += 1
        else:
            nums[i] = nums[k - 1]
            k -= 1

    return k


# --------------------------------- #

print("Expected: 2")
print("Got: ", remove_element([3, 2, 2, 3], 3))

print("Expected: 5")
print("Got: ", remove_element([0, 1, 2, 2, 3, 0, 4, 2], 2))
