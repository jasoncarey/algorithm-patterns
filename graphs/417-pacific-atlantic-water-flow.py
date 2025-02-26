"""
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow

Medium

TC: O(n)
SC: O(n)
"""


def pacific_atlantic(heights):
    ROWS, COLS = len(heights), len(heights[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    pacific = set()
    atlantic = set()

    def dfs(r, c, visited):
        if (r, c) in visited:
            return
        visited.add((r, c))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < ROWS and 0 <= nc < COLS and heights[r][c] <= heights[nr][nc]:
                dfs(nr, nc, visited)

    # initialize dfs at border cells
    for i in range(ROWS):
        dfs(i, 0, pacific)
        dfs(i, COLS - 1, atlantic)

    for j in range(COLS):
        dfs(0, j, pacific)
        dfs(ROWS - 1, j, atlantic)

    return [[r, c] for r, c in pacific.intersection(atlantic)]  # find the intersection
