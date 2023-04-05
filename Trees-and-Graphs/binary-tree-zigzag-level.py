"""
Given the root of a binary tree, return the zigzag level order traversal
of its nodes' values. (i.e., from left to right, then right to left for 
the next level and alternatve between).
"""

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        