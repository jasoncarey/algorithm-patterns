"""
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/

Medium
"""


def search_matrix(matrix, target):

    ROWS, COLS = len(matrix), len(matrix[0])

    # find the correct row
    mid_row, top, bot = 0, 0, ROWS - 1
    while top <= bot:
        mid_row = (top + bot) // 2
        if target > matrix[mid_row][-1]:
            top = mid_row + 1
        elif target < matrix[mid_row][0]:
            bot = mid_row - 1
        else:
            break

    if not (top <= bot):  # target out of bounds
        return False

    # binary search in the correct row
    left, right = 0, COLS - 1
    while left <= right:
        mid = (left + right) // 2
        if matrix[mid_row][mid] == target:
            return True
        elif matrix[mid_row][mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False
