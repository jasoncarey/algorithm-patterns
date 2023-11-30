# 643. Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/description/

class Solution:
    def find_max_average(self, nums: List[int], k: int) -> float:

        # Contiguous subarray -> Intuition: sliding window
        # Length = k -> Intuition: fixed sliding window

        if len(nums) < k: return
        max_sum, window_sum = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            if i < k:
                window_sum += nums[i]
                max_sum += nums[i]
            else:
                window_sum = window_sum - nums[i-k] + nums[i]
                max_sum = max(max_sum, window_sum)
        return max_sum / k
        
