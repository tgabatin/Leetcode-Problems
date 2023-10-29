"""
Equal Row and Column Pairs

Given a 0-indexed n*n integer matrix grid, return the number of pairs (r_i, c_j)
such that row r_i and c_j are equal. 

A row and column pair is considered equal if they contain the same elements in the same
order (i.e., an equal array).
"""

class Solution(object):
    def equalPairs(self, grid):
        """
        :type grid: List[int][int]
        :rtype: int
        """