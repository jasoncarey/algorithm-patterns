# Trees

- DFS: stack or recursive (stack)
- BFS: queue

- Diameter = max_height(left) + max_height(right)


```python
# General BFS
def bfs(root):
    if not root:
        return []

    q = deque([root])
    result = []

    while q:
        level_size = len(q)
        level = []

        for i in range(level_size):
            node = q.popleft()

            # process current node based on specific problem
            level.append(node.val) 

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        # perform level operations here
        result.append(level)

    return result
```