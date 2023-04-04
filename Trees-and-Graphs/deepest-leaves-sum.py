"""
Given the root of a binary tree, return the sum of values of its
deepest leaves.
"""

"""
Time Complexity: O(n)
Space Complexity: O(w) (w = width of binary tree)
"""

from collections import deque

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0

        queue = deque([root])
        level_sum = 0

        while queue:
            level_size = len(queue)
            level_sum = 0

            for i in range(level_size):
                node = queue.popleft()
                level_sum += node.val

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)

        return level_sum