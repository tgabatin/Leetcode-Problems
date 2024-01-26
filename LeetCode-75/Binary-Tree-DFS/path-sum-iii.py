"""
Path Sum III

Given the root of a binary tree and an integer targetSum, return the number of paths
where the sum of the values along the path euqals targetSum. 

The path does not need to start or end at the root or a leaf, but it must go
downwards (i.e., traveling only from parent nodes to child nodes).
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def pathSum(self, root, targetSum):
        """
        
        :type root: TreeNode
        :type targetSum: int
        :rtype: int
        """
        def dfs(node, current_sum, path_sums):
            if not node:
                return 0
            
            current_sum += node.val

            count = path_sums.get(current_sum - targetSum, 0)

            path_sums[current_sum] = path_sums.get(current_sum, 0) + 1

            count += dfs(node.left, current_sum, path_sums)
            count += dfs(node.right, current_sum, path_sums)

            return count
        
        path_sums = {0:1}

        return dfs(root, 0, path_sums)
    
"""
Explanation
Utilization of recursive DFS for solution.
"""