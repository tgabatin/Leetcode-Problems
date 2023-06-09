"""
For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., is
concatenated with itself one or more times). 

Given two strings str1 and str2, return the largest string x such that x 
divides str1 and str2. 
"""

"""
Uses recursion to solve the problem
"""
class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        if len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)
        
        if not str2:
            return str1
        
        if str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):], str2)
        
        return ""
