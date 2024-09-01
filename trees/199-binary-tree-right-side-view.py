"""
199. Binary tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/description/

Medium

# We can see the right-most left in every level -> try BFS
"""


def right_side_view(root):
    if not root:
        return

    q = deque([root])
    result = []

    while q:
        level_size = len(q)

        for i in range(len(q)):
            node = q.popleft()

            # this is the right-most node
            if i == level_size - 1:
                result.append(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

    return result
