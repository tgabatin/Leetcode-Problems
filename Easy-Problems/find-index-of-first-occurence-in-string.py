"""
Given two strings needle and haystack, return the index of the first occurence of
needle in haystack, or -1 if needle is not a part of haystack.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

from collections import deque
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        return haystack.find(needle)
    
"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution2(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        queue = deque(maxlen=len(needle))

        for i, char in enumerate(haystack):
            queue.append(char)
            if len(queue) == len(needle) and ''.join(queue) == needle:
                return i - len(needle) + 1
        
        return -1