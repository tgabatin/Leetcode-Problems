"""
N-th Tribonacci Number

The Tribonacci squence, T_n is defined as follows:

T_0 = 0, T_1 = 1, T_2 = 1 
and
T_n+3 = T_n + T_n+1 + T_n+2 for n >= 0.

Given n, return the value of T_n.
"""

class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1 or n == 2:
            return 1
        
        tribonacci_nums = [0] * (n + 1)
        tribonacci_nums[1] = 1
        tribonacci_nums[2] = 1

        for i in range(3, n + 1):
            tribonacci_nums[i] = tribonacci_nums[i-1] + tribonacci_nums[i-2] + tribonacci_nums[i-3]

        return tribonacci_nums[n]