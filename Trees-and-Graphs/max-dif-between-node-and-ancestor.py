"""
Given the root of a binary tree, find the maximum value v for which
there exist different nodes a and b where v = |a.val - b.val| and a 
is an ancestor of b.

A node a is an ancestor of b if either: any child of a is equal to b 
or any child of a is an ancestor of b. 
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

class TreeNode:
    def __init__(self, val = 0, left=None, right = None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def helperFunction(node, curr_max, curr_min):
            if not node:
                return curr_max - curr_min
            
            curr_max = max(curr_max, node.val)
            curr_min = min(curr_min, node.val)

            left_diff = helperFunction(node.left, curr_max, curr_min)
            right_diff = helperFunction(node.right, curr_max, curr_min)

            return max(left_diff, right_diff)

        return helperFunction(root, root.val, root.val)    