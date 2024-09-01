"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/

Medium
"""


# TC: O(n)
# SC: O(h) -> O(n) worst case, O(log(n)) best case
def is_valid_bst(root):
    def valid(node, left, right):
        if not node:
            return True

        if not (left < node.val < right):
            return False

        return valid(node.left, left, node.val) and valid(node.right, node.val, right)

    return valid(root, float("-inf"), float("inf"))


# Inorder traversal then parse the array
# TC: O(n)
# SC: O(n)
def is_valid_bst(root):

    def dfs(node):
        nonlocal res
        if not node:
            return

        dfs(node.left)
        res.append(node.val)
        dfs(node.right)

    res = []
    dfs(root)
    if not res:
        return False
    for i in range(len(res) - 1):
        if res[i] >= res[i + 1]:
            return False
    return True
