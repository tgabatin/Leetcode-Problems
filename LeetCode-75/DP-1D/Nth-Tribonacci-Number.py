"""
N-th Tribonacci Number

The Tribonacci squence, T_n is defined as follows:

T_0 = 0, T_1 = 1, T_2 = 1 
and
T_n+3 = T_n + T_n+1 + T_n+2 for n >= 0.

Given n, return the value of T_n.
"""

class Solution(object):
    def tribonaci(self, n):
        """
        :type n: int
        :rtype: int
        """