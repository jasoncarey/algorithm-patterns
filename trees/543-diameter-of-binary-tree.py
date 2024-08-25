"""
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/

Easy

TC: O(n)
SC: O(h) -> O(log(n)) for balanced, otherwise O(n)

Diameter = max_height(left) + max_height(right)
"""


def diameter_of_binary_tree(root):

    res = 0

    def dfs(root):
        nonlocal res
        if not root:
            return 0

        left = dfs(root.left)
        right = dfs(root.right)
        res = max(res, left + right)  # calculate the diameter of this tree

        return 1 + max(left, right)  # but only return the height

    dfs(root)
    return res
