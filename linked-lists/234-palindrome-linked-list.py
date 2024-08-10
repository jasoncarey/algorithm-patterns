"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/

Medium
Linked List

Algorithm:
1. find middle
2. reverse second half
3. compare
4. reverse back

TC: O(n)
SC: O(1)
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome(head: ListNode) -> bool:

    slow = fast = head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    second_half = reverse(slow)

    while head and second_half:
        if head.val != second_half.val:
            return False

        head = head.next
        second_half = second_half.next

    return True


def reverse(head: ListNode) -> ListNode:

    prev, curr = None, head
    while curr:
        pnext = curr.next
        curr.next = prev
        prev = curr
        curr = pnext

    return prev
