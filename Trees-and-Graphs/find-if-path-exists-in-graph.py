"""
There is a bi-directional graph with n vertices, where each vertex is 
labeled from 0 to n - 1 (inclusive). The edges in the graph are represented
as a 2D integer array edges, where each edges[i] = [u_i, v_i] denotes
a bi-directional edge between vertex u_i and vertex v_i. Every vertex
pair is connected by at most one edge, and no vertex has an edge to 
itself.

You want to determine if there is a valid path that exists from vertex
source to vertex destination. 

Given edges and integers n, source, and destination, return true if there
is a valid path from source to destination, or false otherwise.
"""

class Solution(object):
    def validPath(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        adj_list = {}
        for edge in edges:
            u,v = edge
            if u not in adj_list:
                adj_list[u] = []
            adj_list[u].append(v)
            if v not in adj_list:
                adj_list[v] = []
            adj_list[v].append(u)
        visited_node = set()
        def dfs(node):
            if node == destination:
                return True
            visited_node.add(node)
            for neighbor in adj_list[node]:
                if neighbor not in visited_node:
                    if dfs(neighbor):
                        return True
            return False
        return dfs(source)