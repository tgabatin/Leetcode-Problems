"""
Kids With the Greatest Number of Candies

There are n kids with candies. You are given an integer array candies, where each 
candies[i] represents the number of candies the ith kid has, and an integer
extraCandies, denoting the number of extra candies you have. 

Return a boolean array result of length n, where result[i] is true, if, after
giving the ith kid all the extraCandies, they will have the greatest number of candies
among all the kids, or false otherwise. 

Note that multiple kids can ahve the greatest number of candies. 
"""

class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        