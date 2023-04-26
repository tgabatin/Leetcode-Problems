"""
Given an integer num, repeatedly add all its digits until the result has only
one digit, and return it.
"""


"""
Time Complexity: O(logn)
Space Complexity: O(1)
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num is None:
            return 0
        
        while num >= 10:
            digit_sum = 0
            for digit in str(num):
                digit_int = int(digit)
                digit_sum += digit_int
            num = digit_sum

        return num