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

        potions.sort()

        pairs = []

        def binary_search_helper(spell):
            low, high = 0, len(potions) - 1
            count = 0

            while low <= high:
                mid = (low + high) // 2

                if spell * potions[mid] >= success:
                    count = len(potions) - 1
                    high = mid - 1
                else:
                    low = mid + 1

            return count
        
        for i in range(len(spells)):
            count = binary_search_helper(spells[i])
            pairs.append(count)

        return pairs

"""
Explanation Solution 1:


"""
