"""
Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates
in-place such that each unique element appears only once. The relative order of the
elements should be kept the same. Then return the number of unique elements in nums. 

Consier the number of unique elements of nums to be k, to get accepted, you need to
do the following things:

* Change the array nums such that the first k elements of nums contain the unique 
elements in the order they were present in nums initially. The remaining elements
of nums are not important as well as the size of nums
* Return k
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
    
        i = 0 
        
        while i < len(nums) - 1:
            if nums[i] == nums[i + 1]:
                del nums[i]
            else:
                i += 1
        
        return len(nums)

