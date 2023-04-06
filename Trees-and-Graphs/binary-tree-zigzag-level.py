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
        if not root:
            return []
        
        queue = deque([root])
        result = []
        left_to_right = False

        while queue:
            level = deque()
            level_size = len(queue)

            for i in range(level_size):
                node = queue.popleft()

                if left_to_right:
                    level.append(node.val)
                else:
                    level.appendleft(node.val)

                if node.left:
                    queue.append(node.left)

                if node.right:
                    queue.append(node.right)

            result.append(list(level))
            left_to_right = not left_to_right

        return result