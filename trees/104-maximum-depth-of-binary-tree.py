"""
104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/

Easy

TC: O(n)
SC: O(n)
"""


def max_depth(root):

    if not root:
        return 0

    return 1 + max(max_depth(root.left), max_depth(root.right))
