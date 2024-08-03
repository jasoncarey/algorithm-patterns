# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water
# Medium
# Two Pointers, Greedy

# TC: O(n)
# SC: O(1)

from typing import List


def max_area(height: List[int]) -> int:

    max_area = 0

    left, right = 0, len(height) - 1

    while left < right:
        curr_area = min(height[left], height[right]) * (right - left)
        max_area = max(max_area, curr_area)

        if height[right] < height[left]:
            right -= 1
        else:
            left += 1

    return max_area


# --------------------------------- #

print("Expected: 49. " "Got: ", max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))
print("Expected: 1. " "Got: ", max_area([1, 1]))
print("Expected: 0. " "Got: ", max_area([0, 0]))
