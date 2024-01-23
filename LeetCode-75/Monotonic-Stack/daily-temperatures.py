"""
Daily Temperatures

Given an array of integers temperatures represents the daily temperatures, return an
array answer such that answer[i] is the number of days you have to wait after the ith
day to get a warmer temperature. If there is no future day for which this is possible,
keep answer[i] == 0 instead.
"""

class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperature: List[int]
        :rtype: List[int]
        """
        n = len(stack)
        result = [0] * n
        stack = []

        for i in range(len(n)):
            while stack and temperatures[i] < temperatures[stack[-1]]:
                prev = stack.pop()
                result[prev] = i - prev
            stack.append(i)

        return result