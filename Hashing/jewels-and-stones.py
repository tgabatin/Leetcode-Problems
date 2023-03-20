"""
You're given strings jewels representing the types of stones that are jewels,
and stones representing the stones you have. Each charcter in stones is a type of stone you have.
You want to know how many of the stones you have are also jewels. 

Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        result = {}
        count = 0
        for char in stones:
            if char in stones[char]:
                result[char] += 1
            else:
                result[char] =  1

        for jewel in jewels:
            if jewel in result:
                count += result[jewel]

        return count

