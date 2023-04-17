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
Time Complexity: O(mn)
Space Complexity: O(mn)
"""

from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        m, n = len(maze), len(maze[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        queue = deque([entrance[0], entrance[1], 0])
        visited = set([(entrance[0], entrance[1])])

        while queue:
            front = queue.popleft()
            row = front[0]
            col = front[1]
            distance = front[2]

            if (row == 0 or row == m-1 or col == 0 or col == n-1) and (row, col) != tuple(entrance):
                return distance
            
            for d in directions:
                r, c = row + d[0], col + d[1]
                if 0 <= r < m and 0 <= c < n and maze[r][c] == '.' and (r,c) not in visited:
                    visited.add((r,c))
                    queue.append((r,c, distance + 1))

        return -1
