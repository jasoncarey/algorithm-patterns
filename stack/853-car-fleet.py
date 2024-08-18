"""
853. Car Fleet
https://leetcode.com/problems/car-fleet

Medium
"""

from typing import List


def car_fleet(target: int, position: List[int], speed: List[int]) -> int:

    cars = sorted(zip(position, speed), reverse=True)
    stack = []

    for car in cars:
        time = (target - car[0]) / car[1]

        if not stack or stack[-1] < time:
            stack.append(time)

    return len(stack)


# --------------------------------- #
print("Expected: 3, Got: ", car_fleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3]))
print("Expected: 1, Got: ", car_fleet(10, [3], [3]))
print("Expected: 1, Got: ", car_fleet(100, [0, 2, 4], [4, 2, 1]))
print("Expected: 2, Got: ", car_fleet(10, [6, 8], [3, 2]))
