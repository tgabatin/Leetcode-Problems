"""
Given an integer array nums and an integer val, remove all occurences of val in nums
in-place. The order of the elements may be changed. Then return the number of elements
in nums which are not equal to val. 

Consider the number of elements in nums which are not equal to val to be k, to get
acepted, you need to do the following things:

- Change the array nums such that the first k elements of nums contain the elements 
which are not equal to val. The remaining elements of nums are not important a well
as the size of nums.
- Return k
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k