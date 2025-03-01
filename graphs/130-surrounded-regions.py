"""
130. Surrounded Regions
https://leetcode.com/problems/surrounded-regions

Medium

TC: 
SC: 
"""


def solve(board):

    if not board or not board[0]:
        return

    ROWS, COLS = len(board), len(board[0])
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    def dfs(r, c):
        if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] != "O":
            return

        board[r][c] = "S"  # mark border connected cells as safe (we only dfs from these cells)

        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # dfs only on border connected cells
    for r in range(ROWS):
        if board[r][0] == "O":
            dfs(r, 0)
        if board[r][COLS - 1] == "O":
            dfs(r, COLS - 1)

    for c in range(COLS):
        if board[0][c] == "O":
            dfs(0, c)
        if board[ROWS - 1][c] == "O":
            dfs(ROWS - 1, c)

    for r in range(ROWS):
        for c in range(COLS):
            if board[r][c] == "O":
                board[r][c] = "X"
            elif board[r][c] == "S":
                board[r][c] = "O"
