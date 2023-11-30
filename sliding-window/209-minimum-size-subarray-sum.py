# 209. Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution:
    def min_subarray_len(self, target: int, nums: List[int]) -> int:
        
        # Subarray -> Intuition: sliding window
        # Mininun length -> Intuition: dynamic version

        if not nums: return 0
        if nums[0] >= target: return 1
    
        min_window = len(nums)+1
        window_start = 0
        window_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Grow to sum >= target
            window_sum += nums[i]

            # If condition is satisfied,
            # Shrink until it's not
            while window_sum >= target and window_start <= i:
                min_window = min(min_window, i - window_start + 1)
                window_sum -= nums[window_start]
                window_start += 1
        
        if min_window == len(nums) + 1: return 0
        else: return min_window
