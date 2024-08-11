"""
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number

Medium

Linked List problem where the 'next' pointer is the value of nums

Floyd's algorithm to determine the beginning of a cycle:
    -> find the intersection of fast and slow pointers
    -> then make a new slow pointer at the beginning
    -> iterate until slow1 = slow2 

TC: O(n)
SC: O(1)
"""


def find_duplicate(nums) -> int:

    slow1, slow2, fast = 0, 0, 0

    while True:
        slow1 = nums[slow1]
        fast = nums[nums[fast]]

        if slow1 == fast:
            break

    while True:
        slow1 = nums[slow1]
        slow2 = nums[slow2]

        if slow1 == slow2:
            return slow1
