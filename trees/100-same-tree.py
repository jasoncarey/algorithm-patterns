"""
100. Same Tree
https://leetcode.com/problems/same-tree/

Easy

TC: O(n)
SC: O(h) -> O(n) worst case, O(log(n)) best case
"""


def same_tree(p, q):
    # DFS
    stack = [(p, q)]

    while stack:
        node1, node2 = stack.pop()

        if not node1 and not node2:
            continue
        if not node1 or not node2 or node1.val != node2.val:
            return False

        stack.append((node1.right, node2.right))
        stack.append((node1.left, node2.left))

    return True
