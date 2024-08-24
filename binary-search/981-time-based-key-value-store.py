"""
981. Time Based Key-Value Store
https://leetcode.com/problems/time-based-key-value-store/

Medium

TC: O(1), O(log(n))
SC: O(n)
"""


class TimeMap:
    def __init__(self):
        self.dict = {}  # key: list of [val, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res, values = "", self.dict.get(key, [])

        # m is the index of the current pair
        # [m][0] is the value, [m][1] is the timestamp
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] <= timestamp:
                # we might not find an exact match so hold the closest so far
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
