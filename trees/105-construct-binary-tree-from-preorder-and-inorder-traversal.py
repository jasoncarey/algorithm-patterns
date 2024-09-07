"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

Medium

TC: O(n)
SC: O(n)
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(preorder, inorder):
    if not preorder or not inorder:
        return None

    # root of preorder is the 0 index
    root = TreeNode(preorder[0])
    # this is the root found previously but inorder
    mid = inorder.index(preorder[0])
    # left subtree is everything left of the root in inorder
    root.left = self.build_tree(preorder[1 : mid + 1], inorder[:mid])
    # right subtree is everything right of the root in inorder
    root.right = self.build_tree(preorder[mid + 1 :], inorder[mid + 1 :])

    return root
