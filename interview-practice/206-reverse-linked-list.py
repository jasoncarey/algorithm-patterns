# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list

# TC:
# SC:

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # TC: O(n)
    # SC: O(n)
    def reverse_list_recursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # eg: [1, 2, 3, 4, 5]
        # when head = 4:
        #   new_head = reverse_list_recursive(5)
        #   5 -> head (4) -> None

        # Handle the empty list or single-node list case
        if not head or not head.next:
            return head

        new_head = self.reverse_list_recursive(head.next)
        head.next.next = head
        head.next = None

        return new_head

    # TC: O(n)
    # SC: O(1)
    def reverse_list_iterative(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 3 pointers solution [prev, curr, temp] in this order
        # reverse curr (curr.next = prev)
        # move each pointer right (curr = temp so we don't go through our new reversed path)

        if self.has_cycle(head):
            return None

        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev

    def has_cycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
        return False
