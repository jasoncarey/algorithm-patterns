"""
739. Daily Temperatures
https://leetcode.com/problems/daily-temperatures

Medium

TC: O(n)
SC: O(n)
"""


def daily_temperatures(temperatures):

    res = [0] * len(temperatures)
    stack = []  # monotonically decreasing stack stores indexes

    for i in range(len(temperatures)):
        while stack and temperatures[stack[-1]] < temperatures[i]:
            prev_day = stack.pop()
            res[prev_day] = i - prev_day
        stack.append(i)

    return res
