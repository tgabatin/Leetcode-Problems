"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place
such that each unique element appears only once. The relative order of the elements
should be kept the same. Then return the number of unique elemnts in nums. 

Consider the number of unique elements of nums to be k, to get accepted, to you need
to do the following things:

- Change the array nums such that the first k elements of nums contain the unique
elements in the order they were present in nums initially. The remaining elements
of nums are not important as well as the size of nums.
- Return k
"""
"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Check whether there are items in nums
        if not nums:
            return 0
        
        k = 1
        prev_num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != prev_num:
                nums[k] = nums[i]
                k += 1
                prev_num = nums[i]

        return k
    


        
