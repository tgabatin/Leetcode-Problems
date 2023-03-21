"""
Given a string 's', find the length of the longest substring without repeating characters.
"""

class Solution(object):
    def lengthOfLongestSubstring(self,s):
        """
        :type s: str
        :rtype: int
        """
        chars = {}
        maxLength = 0
        leftPointer = 0
        for rightPointer in range(len(s)):
            if s[rightPointer] in chars and chars[s[rightPointer]] >= leftPointer:
                leftPointer = chars[s[rightPointer]] + 1
            chars[s[rightPointer]] = rightPointer
            maxLength = max(maxLength, rightPointer - leftPointer + 1)
        return maxLength
