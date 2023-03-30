"""
The next greater element of some element x in an array is the first greater element
that is to the right of x in the same array. 

You are given two distinct 0-indexed integer array nums1 and nums2, where nums1 is a subset of nums2.

For each 0 <= i <= nums1.length, find the index j such that nums1[i] == nums2[j] and determine the next
greater element of nums2[j] in nums2. If there is no next greater element, then the answer for this query is -1. 

Return an array ans of length nums1.length such that ans[i] is the next greater element as described above. 
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""

from ast import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        map = {}

        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                map[stack.pop()] = nums2[i]
            stack.append(nums2[i])

        while stack:
            map[stack.pop()] = -1

        res = [0] * len(nums1)
        for i in range(len(nums1)):
            res[i] = map.get(nums1[i])

        return res



