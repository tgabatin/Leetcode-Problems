"""
Single Number

Given a non-empty array of integers nums, every element appears twice except for one.
Find that single one.

You must implement a solution with a linear runtime complexity and use only constant
extra space.
"""


"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def singleNumer(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hash_map = {}
        for num in nums:
            if num in hash_map:
                hash_map[num] += 1
            else:
                hash_map[num] = 1

        for key, value in hash_map.items():
            if value == 1:
                return key
