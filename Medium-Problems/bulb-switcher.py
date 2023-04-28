"""
There are n bulbs that are initially off. You first turn on all the bulbs, then you
turn off every second bulb. 

On the third round, you toggle every third bulb (turning on if it's off or turning off
if it's on). For the ith round, you toggle every ith bulb. For the nth round, you toggle
only the last bulb.

Return the number of bulbs that are on after n rounds.
"""

"""
Time Complexity: O(sqrt(n))
Space Complexity: O(1)
"""
class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n**0.5)