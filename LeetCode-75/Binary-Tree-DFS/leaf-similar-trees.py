"""
Leaf Similar Trees

Consider all the leaves of a binary tree, from left to right order, the values of 
those leaves form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).

Two binary trees are considered leaf-similar if their leaf value sequence is the same.

Return true if and only if the two given trees with head nodes root1 and root2 are
leaf-similar. 
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.right = right
        self.left = left

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def get_leaf_values(node, leaf_values):
            if not node:
                return
            if not node.left and not node.right:  # Check if the node is a leaf
                leaf_values.append(node.val)
            get_leaf_values(node.left, leaf_values)
            get_leaf_values(node.right, leaf_values)

        leaf_values1 = []
        leaf_values2 = []

        get_leaf_values(root1, leaf_values1)
        get_leaf_values(root2, leaf_values2)

        return leaf_values1 == leaf_values2

        