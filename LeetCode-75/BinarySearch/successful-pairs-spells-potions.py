"""
Successful Pairs of Spells and Potions

You are given two positive integer arrays spells and potions, of length n and m 
respectively, where spells[i] represents the strength of the ith spell and potions[i]
represents the strength of the jth potion. 

You are also given an integer success. A spell and potion pair is considered successful
if the product of their strengths is at least success.

Return an integer array pairs of length n where pairs[i] is the number of potions that
will form a successful pair with the ith spell. 
"""

class Solution(object):
    def successfulPairs(self, spells, potions, success):
        """
        :type spells: List[int]
        :type potions: List[int]
        :type success: int
        :rtype: List[int]
        """