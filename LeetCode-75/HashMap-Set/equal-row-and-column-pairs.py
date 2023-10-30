"""
Equal Row and Column Pairs

Given a 0-indexed n*n integer matrix grid, return the number of pairs (r_i, c_j)
such that row r_i and c_j are equal. 

A row and column pair is considered equal if they contain the same elements in the same
order (i.e., an equal array).
"""

"""
# Incorrect Solution - Review
class Solution(object):
    def equalPairs(self, grid):
        
        #:type grid: List[int][int]
        #:rtype: int

        n = len(grid)
        count = 0

        grid_row = [{} for _ in range(n)]
        grid_col = [{} for _ in range(n)]

        for i in range(n):
            for j in range(n):
                element = grid[i][j]
                grid_row[i][element] = grid_row[i].get(element, 0) + 1
                grid_col[j][element] = grid_col[j].get(element, 0) + 1

        for i in range(n):
            for j in range(n):
                if grid_row[i] == grid_col[j]:
                    count += 1

        return count
"""

# Time Complexity: O(n^3)
# Space Complexity: O(1)
class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        count = 0

        for i in range(n):
            for j in range(n):
                if grid[i] == [grid[k][j] for k in range(n)]:
                    count += 1

        return count
