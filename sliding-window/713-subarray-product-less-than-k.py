# 713. Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k
# Medium
# Sliding Window

# TC: O(n)
# SC: O(1)

from typing import List


def num_subarray_product_less_than_k(nums: List[int], k: int) -> int:

    product = 1
    result = 0
    left = 0

    for right in range(len(nums)):
        product *= nums[right]

        while product >= k and left <= right:
            product /= nums[left]
            left += 1

        result += right - left + 1

    return result


# --------------------------------- #

print("Expected: 8. " "Got: ", num_subarray_product_less_than_k([10, 5, 2, 6], 100))
print("Expected: 0. " "Got: ", num_subarray_product_less_than_k([1, 2, 3], 0))
