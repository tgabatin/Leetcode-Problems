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
        self.longest_path = 0

        def dfs(node, left, right):
            self.longest_path = max(self.longest_path, left, right)

            if node.left:
                dfs(node.left, right + 1, 0)
            
            if node.right:
                dfs(node.right, 0, left + 1)

        dfs(root, 0, 0)

        return self.longest_path

    
