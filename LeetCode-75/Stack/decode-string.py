"""
Given an encoded string, return its decoded string.

Th encoding rule is: k[encoded_string], where the encoded_string inside the squared
brackets is being repeated exactly k times. Note that k is guaranteed to be a positiev
integer.

You may assume that the input string is always valid; there are no extra white
spaces, square brackets are well-formed, etc. Furthermore, you may assume that the
original data does not contain any digits and that digits are only for those repeat
numbers, k. For example, there will not be input like 3a or 2[4].

The test cases are generated so that the length of the output will never exceed
10^5.
"""

class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        current_num = 0
        current_str = ""

        for char in s:
            if char.isdigit():
                current_num = current_num * 10 + int(char)
            elif char == '[':
                stack.append(current_str)
                stack.append(current_num)
                current_str = ""
                current_num = 0
            elif char == ']':
                num = stack.pop()
                prev_str = stack.pop()
                current_str = prev_str + num * current_str
            else:
                current_str += char

        return current_str