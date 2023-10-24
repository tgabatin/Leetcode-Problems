"""
Max Number of K-Sum Pairs

You are given an integer array nums and an integer k. 

In one operation, you can pick two numbers from the array whose sum equals k and 
remove them from the array. 

Return the maximum number of operations you can perform on the array.
"""

class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        