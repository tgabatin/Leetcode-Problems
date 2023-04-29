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
        """
        No return type, modification of board is in-place.
        """
        # Define helper functions for positional index of values

        # Initialization of all possible values

        # Recursion to backtrack through the function