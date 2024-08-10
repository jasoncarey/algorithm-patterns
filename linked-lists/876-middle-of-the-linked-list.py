"""
876. Middle of the Linked List
https://leetcode.com/problems/middle-of-the-linked-list/

Easy
Linked List

TC: O(n)
SC: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def middle_node(head: ListNode) -> ListNode:

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if not fast.next:
        return slow
    else:
        return slow.next
