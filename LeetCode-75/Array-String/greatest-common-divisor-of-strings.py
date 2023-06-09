"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., is
concatenated with itself one or more times). 

Given two strings str1 and str2, return the largest string x such that x 
divides str1 and str2. 
"""

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        