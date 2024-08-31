"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/

Easy
"""


def is_subtree(self, root, subRoot):
    if not root:
        return False
    if not subRoot:
        return True

    if self.same_tree(root, subRoot):
        return True

    return self.is_subtree(root.left, subRoot) or self.is_subtree(root.right, subRoot)


def same_tree(self, s, t):
    if not s and not t:
        return True
    if s and t and s.val == t.val:
        return self.same_tree(s.left, t.left) and self.same_tree(s.right, t.right)

    return False
