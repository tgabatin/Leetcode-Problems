"""
43. Multiply Strings

Given two non-negative integers num1 and num2 represented as strings, return the product
of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to 
integer directly.
"""

"""
Time Complexity: O(m*n)
Space Complexity: O(m+n)
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        
        if num1 == '0' or num2 == '0':
            return '0'

        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                pos1, pos2 = i + j, i + j + 1
                total = mul + result[pos2]
                
                result[pos2] = total % 10
                result[pos1] += total // 10
        
        while result[0] == 0:
            result.pop(0)
        
        return ''.join(map(str, result))