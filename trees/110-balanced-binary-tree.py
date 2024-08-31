"""
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/description/

Easy
"""


# Height-Balanced: depth of each nodes subtrees differs by <= 1
def is_balanced(root):

    def dfs(root):
        if not root:
            return [True, 0]

        left, right = dfs(root.left), dfs(root.right)

        balanced = left[0] and right[0] and (abs(left[1] - right[1]) <= 1)
        return [balanced, 1 + max(left[1], right[1])]

    return dfs(root)[0]
