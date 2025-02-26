"""
994. Rotting Oranges
https://leetcode.com/problems/rotting-oranges

Medium

TC: 
SC: 
"""

from collections import deque


def oranges_rotting(grid):
    ROWS, COLS = len(grid), len(grid[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    q = deque()
    fresh = 0

    # add all the initial rotten oranges to the queue and get fresh count
    for i in range(ROWS):
        for j in range(COLS):
            if grid[i][j] == 2:
                q.append((i, j))
            elif grid[i][j] == 1:
                fresh += 1

    # if not fresh oranges exist intially, return 0 immediately
    if fresh == 0:
        return 0

    time = 0
    while q:
        new_rotted = False  # bfs runs 1 cycle after everything processed, so time is falsely incremented

        for _ in range(len(q)):  # process at level
            r, c = q.popleft()
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1:
                    grid[nr][nc] = 2
                    q.append((nr, nc))
                    fresh -= 1
                    new_rotted = True

        if new_rotted:
            time += 1

    return time if fresh == 0 else -1
