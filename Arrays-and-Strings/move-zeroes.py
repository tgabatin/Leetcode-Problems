"""
Given an integer array nums, move all the 0's to the end of it
while maintaining the relative order of the non-zero elements.

Note: You must do this in place without making a copy of the array.
"""

"""
Runtime Complexity: O(n)
Spacetime Complexity: O(n)
"""
class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead
        """

        # Check the condition in which the list is empty
        if len(nums) == 0:
            print("List empty - Exit")

        # Remove all the 0's from the list
        num_zeroes = nums.count(0)
        nums[:] = [num for num in nums if num != 0]
        # Extend the list with just 0's that were counted
        nums.extend([0] * num_zeroes)

        