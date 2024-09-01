"""
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree

Medium

TC: O(n)
SC: O(n)
"""


def good_nodes(root):

    def dfs(node, highest):
        nonlocal res
        if not node:
            return

        if node.val >= highest:
            res += 1
            highest = node.val

        dfs(node.left, highest)
        dfs(node.right, highest)

        return

    res = 0
    dfs(root, root.val)
    return res
