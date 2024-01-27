"""
Longest ZigZag Path in a Binary Tree

You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follows:

* Choose any node in the binary tree and a direction (right or left).
* If the current direction is right, move to the right child of the current node;
otherwise, move to the left child
* Change the direction from right to left or from left to right
* Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has
a length of 0).

Return the longest ZigZag path contained in that tree. 
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def longestZigZag(self, root, targetSum):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count = 0
        self.prefix_sum = {0 : 1}
        self.dfs(root,targetSum, 0)
        return self.count
    
    def dfs(self, node, targetSum, curr_sum):
        if not node:
            return 
        
        curr_sum += node.val

        self.count += self.prefix_sum.get(curr_sum - targetSum, 0)
        self.prefix_sum[curr_sum] = self.prefix_sum.get(curr_sum, 0) + 1

        self.dfs(node.left, targetSum, curr_sum)
        self.dfs(node.right, targetSum, curr_sum)

        self.prefix_sum[curr_sum] -= 1
    
