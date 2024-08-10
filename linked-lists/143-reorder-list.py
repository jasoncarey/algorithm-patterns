"""
143. Reorder List
https://leetcode.com/problems/reorder-list/
Medium
Linked List

TC: O(n)
SC: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reorder_list(head: ListNode) -> None:

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    first, second = head, reverse(slow)

    while second.next:
        next_temp = first.next
        first.next = second
        first = next_temp

        next_temp = second.next
        second.next = first
        second = next_temp


def reverse(head: ListNode) -> ListNode:

    prev, curr = None, head

    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    return prev
