"""
Move Zeroes

Given an integer array nums, move all 0's to the end of it while maintaining the
relative order of the non-zero elements. 

Note that you must do this in-place without making a copy of the array.
"""

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in place
        """
        if not nums:
            return
        
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1