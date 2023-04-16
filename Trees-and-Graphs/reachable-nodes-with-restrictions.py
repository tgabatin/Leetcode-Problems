"""
There is an undidrected tree with n nodes labeled from 0 to n - 1 and
n - 1 edges.

You are given a 2D integer array edges of length n - 1 where edges[i]
= [a_i, b_i] indicates that there is an edge between nodes a_i and b_i
in the tree. You are also given an integer array restricted which 
represents restricted nodes.

Return the maximum number of nodes you can reach from node 0 without
visiting a restricted node. 

Note that node 0 will not be a restricted node.
"""

"""
Time Complexity: O(n^2)
Space Complexity: O(n^2)
"""

class Solution(object):
    def reachableNodes(self, n, edges, restricted):
        """
        :type n: int
        :type edges: List[List[int]]
        :type restricted: List[int]
        :rtype: int
        """
        stack = [0]
        adj = [[] for _ in range(n)]
        for i, j in edges:
            adj[i].append(j)
            adj[j].append(i)
        visited = [0] * n
        visited[0] = -1
        for i in restricted:
            visited[i] = -1
        count = 0
        while stack:
            curr_node = stack.pop(0)
            count += 1
            for i in adj[curr_node]:
                if visited[i] == 0:
                    stack.append(i)
                    visited[i] = 1
        return count
