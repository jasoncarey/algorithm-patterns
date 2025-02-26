"""
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/description/

Medium

TC: 
SC: 
"""


def max_area_island(grid):

    ROWS, COLS = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    max_area = 0

    def dfs(r, c):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == 0:
            return 0

        grid[r][c] = 0  # mark as seen
        area = 1  # start with current cell
        for dr, dc in directions:
            area += dfs(r + dr, c + dc)

        return area

    # dfs starting from every land grid point
    for r in range(ROWS):
        for c in range(COLS):
            if grid[r][c] == 1:
                max_area = max(dfs(r, c), max_area)

    return max_area
