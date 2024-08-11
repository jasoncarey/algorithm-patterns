"""
2. Add Two Numbers
https://leetcode.com/problems/add-two-numbers
Medium
Linked List

Example: [2,4,3], [5,6,4] -> [7,0,8]
"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: ListNode, l2: ListNode) -> ListNode:

    result = ListNode(0)
    pointer = result
    carry = 0

    while l1 or l2 or carry:
        first_num = l1.val if l1 else 0
        second_num = l2.val if l2 else 0

        node_sum = first_num + second_num + carry
        node = node_sum % 10
        carry = node_sum // 10

        pointer.next = ListNode(node)
        pointer = pointer.next

        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return result.next
