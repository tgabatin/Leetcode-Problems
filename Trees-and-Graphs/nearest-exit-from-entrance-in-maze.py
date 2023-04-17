"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented
as '.') and walls (represented as '+'). You are also given the entrace of
the maze, where entrace = [entrace_row, entrace_col] denotes the row and
column of the cell you are initially standing at. 

In one step, you can move one cell up, down, left, or right. You cannot
step into a cell with a wall, and you cannot step outside the maze. Your
goal is to find the nearest exit from the entrace. An exit is defined as
an empty cell that is at the border of the maze. The entrace does not
count as an exit.

Return the number of steps in the shortest path from the entrace to the
nearest exit, or -1 if no such path exists.
"""

"""
Time Complexity:
Space Complexity:
"""

class Solution(object):
    def nearestExit(self, maze, entrace):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """