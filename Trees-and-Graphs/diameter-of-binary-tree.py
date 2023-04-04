"""
Given the root of a binary tree, return the length of the diameter 
of the tree.

The diameter of a binary tree is the length of the longest path between
any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number
of edges between them.
"""

"""
Time Complexity: O(n)
Space Complexity
Depends - O(H) -> Ranging from O(log(n)) to O(n)
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.diameter = 0

        def getHeight(node):
            if not node:
                return 0
            
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        getHeight(root)
        return self.diameter