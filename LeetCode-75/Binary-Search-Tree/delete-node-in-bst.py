"""
Delete Node in a BST

Given a root node reference of a BST and a key, delete the node with the given
key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:
1. Search for a node to remove
2. If the node is found, delete the node. 
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Find the minimum node in the right subtree
            min_node = root.right
            while min_node.left:
                min_node = min_node.left
            
            # Copy the value of the minimum node to the current node
            root.val = min_node.val
            
            # Delete the minimum node from the right subtree
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root
