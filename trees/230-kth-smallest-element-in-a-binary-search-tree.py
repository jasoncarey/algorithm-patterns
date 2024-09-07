"""
230. Kth Smallest Element in a Binary Search Tree
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Medium

TC: O(n)
SC: O(n)
"""


def kth_smallest(root):

    res = []

    def inorder(root):
        nonlocal res
        if not root:
            return

        inorder(root.left)
        res.append(root.val)
        inorder(root.right)

    inorder(root)
    return res[k - 1]
