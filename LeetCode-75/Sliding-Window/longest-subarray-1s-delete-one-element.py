"""
Longest Subarray of 1's After Deleting One Element

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's in the resulting
array. Return 0 if there is no such subarray.
"""

class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = 0
        max_ones = 0

        for num in nums:
            if num == 1:
                right += 1
            else:
                max_ones = max(max_ones, left + right)
                left = right
                right = 0

            max_ones = max(max_ones, left + right)

            return max_ones - 1 if max_ones == len(nums) else max_ones

