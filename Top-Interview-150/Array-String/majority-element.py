"""
Majority Element

Given an array nums of size n, return the majority element. 

The majority element is the element that appears more than floor(n/2) times. You may
assume that the majority element always exists in the array.
"""

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_element = 0

        