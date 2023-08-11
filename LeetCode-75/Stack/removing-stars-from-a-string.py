"""
Remove Stars From a String

You are given a string s, which contains stars *.

In one operation, you can:
- Choose a star in s
- Remove the closest non-star characters to its left, as well as remove the 
star itself

Return the string after all stars have been removed. 

Note:
- The input will be generated such that the operation is always possible
- It can be shown that the resulting string will always be unique. 
"""

class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        result = ""

        for char in s:
            if char == '*':
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        result = ''.join(stack)

        return result