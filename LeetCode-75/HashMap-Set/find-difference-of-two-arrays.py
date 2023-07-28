"""
Find the Difference of Two Arrays

Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2
where:

* answer[0] is a list of all distinct integers in nums1 which are not present in nums2
* answer[1] is a list of all distinct integers in nums2 which are not present in nums1

Note that the integers in the lists may be returned in any order.
"""

class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        set_nums1 = set(nums1)
        set_nums2 = set(nums2)

        answer1 = []
        answer2 = []

        for num in set_nums1:
            if num not in set_nums2:
                answer1.append(num)

        for num in set_nums2:
            if num not in set_nums1:
                answer2.append(num)

        return [answer1, answer2]

