"""
Given two strings needle and haystack, return the index of the first occurence of
needle in haystack, or -1 if needle is not a part of haystack.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)