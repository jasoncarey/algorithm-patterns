"""
875. Koko Eating Bananas
https://leetcode.com/problems/koko-eating-bananas/

Medium
"""

import math


# TC: O(n * log(max(piles)))
# SC: O(1)
def min_eating_speed(piles, h):

    # binary search the range of k
    left, right, res = 1, max(piles), max(piles)
    while left <= right:
        k = (left + right) // 2
        time = 0
        for bananas in piles:
            time += math.ceil(bananas / k)

        if time <= h:
            res = min(res, k)
            right = k - 1
        else:
            left = k + 1

    return res


# Brute force
# TC: O(max(piles) * len(piles))
# SC: O(1)
def min_eating_speed_force(piles, h):

    k = 1
    while k <= max(piles):
        time = 0
        for bananas in piles:
            time += math.ceil(bananas / k)

        if time <= h:
            return k

        k += 1


# --------------------------------- #

print("Expected: 4. " "Got: ", min_eating_speed([3, 6, 7, 11], 8))
print("Expected: 30. " "Got: ", min_eating_speed([30, 11, 23, 4, 20], 5))
print("Expected: 23. " "Got: ", min_eating_speed([30, 11, 23, 4, 20], 6))
