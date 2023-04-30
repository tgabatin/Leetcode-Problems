"""
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

Each of the digits 1 - 9 must occur exactly once in each row.

Each of the digits 1 - 9 must occur exactly once in each column. 

Each of the digits 1 - 9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

The '.' character indicates empty cells.
"""

class Solution(object):
    def solveSudoku(self, board):

        def is_valid(pos, val):
            row, col = pos // 9, pos % 9
            box_row = (row // 3) * 3
            box_col = (col // 3) * 3
            return val not in board[row] and val not in [board[i][col] for i in range(9)] and \
                   val not in [board[i][j] for i in range(box_row, box_row + 3) for j in range(box_col, box_col + 3)]

        possible = [[set(str(i) for i in range(1, 10)) if board[row][col] == '.' else set() for col in range(9)] for row in range(9)]
        for pos in range(81):
            row, col = pos // 9, pos % 9
            if board[row][col] != '.':
                val = board[row][col]
                for i in range(9):
                    possible[row][i].discard(val)
                    possible[i][col].discard(val)
                box_row = (row // 3) * 3
                box_col = (col // 3) * 3
                for i in range(box_row, box_row + 3):
                    for j in range(box_col, box_col + 3):
                        possible[i][j].discard(val)

        def backtrack(pos):
            if pos == 81:
                return True

            row, col = pos // 9, pos % 9
            if board[row][col] != '.':
                return backtrack(pos + 1)

            for val in possible[row][col]:
                if is_valid(pos, val):
                    board[row][col] = val
                    if backtrack(pos + 1):
                        return True
                    board[row][col] = '.'

            return False

        backtrack(0)