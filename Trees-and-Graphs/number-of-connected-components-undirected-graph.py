"""
You have a graph of n nodes. You are given an integer n and an array
edges where edges[i] = [a_i, b_i] indicates that there is an edge
between a_i and b_i in the graph.

Return the number of connected components in the graph
"""

"""
Time Complexity: O(n+m)
Space Complexity: O(n+m)
"""

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        adj_list = [[] for _ in range(n)]
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        def dfs(node, visited):
            visited.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited:
                    dfs(neighbor, visited)

        visited = set()
        count = 0

        for node in range(n):
            if node not in visited:
                dfs(node, visited)
                count += 1

        return count