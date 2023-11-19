"""
Count Good Nodes in Binary Tree

Given a binary tree root, a node X in the tree is named good if in the path from
root to X there are no nodes with a value greater than X. 

Return the number of good nodes in the binary tree.
"""

from platform import node


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def goodNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, prev):
            if not node:
                return 0
            elif node.val >= prev:
                return 1 + dfs(node.left, node.val) + dfs(node..right, node.val)
            else:
                return dfs(node.left, prev) + dfs(node.right, prev)
            
        return dfs(root, root.val)
    
    
"""
Explanation:


"""