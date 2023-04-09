"""
Given the root of a binary search tree and a target value, return the
value in the BST that is closest to the target. If there are multiple
answers, print the smallest
"""

"""
Runtime Complexity: O(h) -> Best Case O(n) -> Worst Case
Space Complexit: O(1)
"""

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        closest_val = root.val
        while root:
            if abs(root.val - target) < abs(closest_val - target) or \
                    (abs(root.val - target) == abs(closest_val - target) and root.val < closest_val):
                closest_val = root.val
            root = root.left if target < root.val else root.right
        return closest_val