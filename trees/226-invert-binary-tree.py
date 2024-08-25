"""
226. Invert Binary Tree
https://leetcode.com/problems/invert-binary-tree/

Easy

TC: O(n)
SC: O(n)
"""


def invert_tree(root):

    if not root:
        return

    root.left, root.right = root.right, root.left
    invert_tree(root.left)
    invert_tree(root.right)

    return root
