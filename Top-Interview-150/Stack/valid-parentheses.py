"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

1. Open brackets must be closed by the same type of brackets.
2. Open brackets must be closed in the correct order.
3. Every close bracket has a corresponding open bracket of the same type. 
"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        stack = []

        for c in s:
            if c in '([{}':
                stack.append(c)
            else:
                if not stack or \
                    (c == ')' and stack[-1] != ')') \
                    (c == ']' and stack[-1] != ']') \
                    (c == '}' and stack[-1] != '}'):
                    return False
                stack.pop()

        return not stack
                    


