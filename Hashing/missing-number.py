"""
Given an array nums containing n distinct numbers in the range [0,n],
return the only number in the range that is missing from the array.
"""

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_dict = {}
        for num in nums:
            num_dict[num] = True
        n = len(nums)
        for i in range(n+1):
            if i not in num_dict:
                return i
        

