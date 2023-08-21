"""
Maximum Depth of Binary Tree

Given the root of a binary tree, return its maximum depth. 

A binary tree's maximum depth is the number of nodes along the longest path from 
the root node down to the farthest leaf node. 
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self,root):
        """
        :type root: TreeNode
        :rtype: int
        """