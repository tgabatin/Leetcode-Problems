"""
Majority Element

Given an array nums of size n, return the majority element. 

The majority element is the element that appears more than floor(n/2) times. You may
assume that the majority element always exists in the array.
"""
import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        majority_element = {}

        for i in range(len(nums)):
            current_element = nums[i]

            if current_element not in majority_element:
                majority_element[current_element] = 1
            else:
                majority_element[current_element] += 1
            
            if majority_element[current_element] > math.floor(len(nums / 2)):
                break

        return current_element

