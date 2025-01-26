"""
79. Word Search
https://leetcode.com/problems/word-search/description/

Medium

TC: O(m * n * 4^L)
SC: O(L) 
where L is length of the word
4^L comes from the 4 directions we can move in
"""


def exist(board, word):

    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    ROWS, COLS = len(board), len(board[0])

    def backtrack(x, y, position, seen):
        if len(word) == position:
            return True

        if x < 0 or x >= ROWS or y < 0 or y >= COLS or board[x][y] != word[position] or (x, y) in seen:
            return False

        seen.add((x, y))

        for dx, dy in directions:
            if backtrack(x + dx, y + dy, position + 1, seen):
                return True

        seen.remove((x, y))
        return False

    # word can start on anywhere on the board
    for i in range(ROWS):
        for j in range(COLS):
            if backtrack(i, j, 0, set()):
                return True

    return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    res = exist(board, word)
    print(f"res: {res}, ans: True")

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "SEE"
    res = exist(board, word)
    print(f"res: {res}, ans: True")

    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCB"
    res = exist(board, word)
    print(f"res: {res}, ans: False")
