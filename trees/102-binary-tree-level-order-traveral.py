"""
102. Binary Tree Level Order Traversel
https://leetcode.com/problems/binary-tree-level-order-traversal/

Medium

TC: O(n)
SC: O(w) ~> O(n/2) -> O(n)
"""


def level_order(root):
    # BFS
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        level = []

        for i in range(level_size):
            node = q.popleft()
            level.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        result.append(level)

    return result
