"""
Find the Index of the First Occurence in a String

Given two strings needle and haystack, return the index of the first occurence of
needle in haystack, or -1 if needle is not part of haystack.
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        index = None

        if not needle:
            return 0
        
        for i in range(len(haystack)- len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                index = i
                break

        return index if index is not None else -1
    
"""
Explanation Solution:

"""

class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    
"""
Explanation Solution2:
"""
    

        
