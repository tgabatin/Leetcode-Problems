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
    def longestZigZag(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node, direction, length, max_length):
            if not node:
                return max_length
            
            max_length = max(max_length, length)

            if direction == 'left':
                max_length = dfs(node.left, 'right', length + 1, max_length)
                max_length = dfs(node.right, 'left', 1, max_length)
            else:
                max_length = dfs(node.right, 'left', length + 1, max_length)
                max_length = dfs(node.left, 'right', 1, max_length)
            return max_length
        
        max_length = 0
        max_length = dfs(root, 'left', 0, max_length)
        max_length = dfs(root, 'right', 0, max_length)
        return max_length