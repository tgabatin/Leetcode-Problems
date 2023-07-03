"""
Increasing Triplet Subsequence

Given an integer array nums, return true if there exists a triple of indices (i,j,k)
such that i < j < k and nums[i] < nums[k]. If no such indices exists, return false.
"""

class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) < 3:
            return False
        
        min_val = float('inf')
        mid_val = float('inf')

        for num in nums:
            if num <= min_val:
                min_val = num
            elif num <= mid_val:
                mid_val = num
            else:
                return True
            
        return False