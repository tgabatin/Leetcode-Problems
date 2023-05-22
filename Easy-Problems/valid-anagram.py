"""
242. Valid Anagram

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word
or phrase, typically using all the original letters exactly once.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :rtype t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        
        char_count = {}

        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        for char in t:
            if char in char_count:
                char_count[char] -= 1
                if char_count[char] < 0:
                    return False
            else:
                return False
            
        return True