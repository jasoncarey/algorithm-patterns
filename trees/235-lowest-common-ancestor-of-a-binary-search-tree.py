"""
235. Lowest Common Ancestor of a Binary Search Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

Medium

TC: O(log(n))
SC: O(1)

This is just using the invariant of a binary search tree
"""


def lowest_common_ancestor(root, p, q):

    while root:
        if root.val < p.val and root.val < q.val:
            root = root.right
        elif root.val > p.val and root.val > q.val:
            root = root.left
        else:
            return root
