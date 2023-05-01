"""
You have a long flowerbed in which some of the plots are planted, and some are not.
However, flowers cannot be planted in adjacent plots. 

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 
meas not empty, and an integer n, return true if n new flowers can be planted in
the flowerbed without violating the no-adjacent-flowers rule and false otherwise.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """
        count = 0
        i = 0
        while i < len(flowerbed) and count < n:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i==len(flowerbed) - 1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
                i += 1
            i += 1
        return count >= n

