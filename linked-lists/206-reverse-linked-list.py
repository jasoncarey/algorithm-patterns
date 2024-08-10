# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list
# Linked List

# TC: O(n)
# SC: O(1)


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:

    prev, curr = None, head

    while curr:
        curr.next, prev, curr = prev, curr, curr.next

    return prev
