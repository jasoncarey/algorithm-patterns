# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Easy
# Linked List

# TC: O(n)
# SC: O(1)


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def has_cycle(head: ListNode) -> bool:

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow is fast:
            return True

    return False
