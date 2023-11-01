"""
Maximum Level Sum of a Binary Tree

Given the root of a binary tree, the level of the root is 1, the level of its children
is 2, and so on. 

Return the smallest level x such that the sum of all the values of nodes at level
x is maximal. 
"""

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxLevelSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        max_level = 1
        max_sum = root.val
        current_level = 1

        queue = deque([root])

        while queue:
            level_sum = 0
            level_size = len(queue)  # Number of nodes at the current level

            for _ in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level_sum > max_sum:
                max_sum = level_sum
                max_level = current_level

            current_level += 1

        return max_level
