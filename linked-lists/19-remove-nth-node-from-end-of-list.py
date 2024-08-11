"""
19. Remove Nth Node From End of List
https://leetcode.com/problems/remove-nth-node-from-end-of-list/
Medium
Linked List

TC: O(n)
SC: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def remove_nth_from_end(head: ListNode, n: int) -> ListNode:

    dummy = head
    length = 0

    while head:
        head = head.next
        length += 1

    head = dummy

    for i in range(length - n):
        head = head.next

    if length == n:
        head = head.next
        return head

    if head.next and head.next.next:
        head.next = head.next.next
    else:
        head.next = None

    return dummy
