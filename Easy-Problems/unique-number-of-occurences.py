"""
Given an array of integers arr, return true if the number of occurences of each
value in the array is unique, or false otherwise.
"""

"""
Time Complexity: O(n)
Space Complexity: O(n)
"""
class Solution(object):
    def uniqueOccurences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        is_unique = True
        hash_map = {}

        for i in arr:
            if i not in arr:
                hash_map[i] = 1
            else:
                hash_map[i] += 1

        val = set(hash_map.values())

        if len(val) != len(hash_map):
            is_unique = False

        return is_unique