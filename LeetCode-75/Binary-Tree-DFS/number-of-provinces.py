"""
Number of Provinces

There are n cities. Some of them are connected, while some are not. If city a is
connected directly with city b, and city b is connected directly with city c, then
city a is connected indirectly with city c. 

A province is a group of directly or indirectly connected cities and no other cities
outside of the group.

You are given an n * n matrix isConnected where isConnected[i][j] = 1 if the ith city
and the jth city are directly connected, and isConnected[i][j] = 0 otherwise. 

Return the total number of provinces. 
"""

class Solution(object):
    def findCircleNum(self, isConnected):
        """
        :type isConnected: List[List[int]]
        :rtype: int
        """

        def dfs(city, visited):
            visited[city] = True

            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor, visited)

        n = len(isConnected)
        provinces = 0
        visited = [False] * n

        for city in range(n):
            if not visited[city]:
                dfs(city, visited)
                provinces += 1

        return provinces