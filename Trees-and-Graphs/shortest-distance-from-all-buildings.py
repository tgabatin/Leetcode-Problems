"""
You are given an m x n grid of values of 0, 1, or 2 where:

- each 0 marks an empty land that you can pass by freely
- each 1 marks a building that you cannot pass through, and
- each 2 marks an obstacle that you cannot pass through

You want to build a house on empty land that reaches all buildings in the 
shortest total travel distane. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build
such a house according to the above rules, return -1. 

The total travel distance is the sum of the distances between the houses of the 
friends and the meeting point.

The distance is calculated using Manhattan Distance, where
distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.
"""

"""
Time Complexity: O(mn)
Space Complexity: O(mn)
"""
class Solution(object):
    def shortestDistance(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        if not grid or not grid[0]:
            return -1
        
        rows, cols = len(grid), len(grid[0])
        building_count = sum(grid[r][c] == 1 for r in range(rows) for c in range(cols))
        distances = [[0] * cols for _ in range(rows)] # total distance to all buildings for each empty land
        reach_counts = [[0] * cols for _ in range(rows)] # number of buildings reached by each empty land
        
        # bfs from each building
        def bfs(r, c):
            visited = [[False] * cols for _ in range(rows)]
            visited[r][c] = True
            queue = [(r, c, 0)]
            while queue:
                row, col, d = queue.pop(0)
                for r_, c_ in ((row-1,col),(row+1,col),(row,col-1),(row,col+1)):
                    if 0 <= r_ < rows and 0 <= c_ < cols and not visited[r_][c_] and grid[r_][c_] != 2:
                        visited[r_][c_] = True
                        if grid[r_][c_] == 0: # empty land
                            distances[r_][c_] += d+1
                            reach_counts[r_][c_] += 1
                            queue.append((r_, c_, d+1))
                        elif grid[r_][c_] == 1: # building
                            continue
        
        # bfs from each building
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    bfs(r, c)
        
        # find the empty land with minimum total distance to all buildings
        ans = float('inf')
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0 and reach_counts[r][c] == building_count:
                    ans = min(ans, distances[r][c])
        
        return ans if ans != float('inf') else -1

