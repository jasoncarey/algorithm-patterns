# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# TC: O(n)
# SC: O(1)


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy/sell is a subarray -> Intuition: sliding window
        # Remember the lowest price we found so far
        # It's more like a shifting window, jumping to the lowest buy price

        buy = 0
        profit = 0
        for sell in range(1, len(prices)):
            if prices[sell] > prices[buy]:
                profit = max(profit, prices[sell] - prices[buy])
            else:
                buy = sell

        return profit
