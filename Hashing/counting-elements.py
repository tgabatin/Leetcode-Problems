"""
Given an integer array arr, count how many elements x there are,
such that x + 1 is also in arr. If there are duplicates in arr, count
them separately.
"""

class Solution(object):
    def countElements(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        count = 0
        hash_table = {}

        # Iterate through the values within the array and check for the key
        for x in arr:
            if x in hash_table:
                hash_table[x] += 1
            else:
                hash_table[x] = 1
        # Iterate through the values in the hash table created and count the 'x+1' elements
        for x in hash_table:
            if x+1 in hash_table:
                counnt += hash_table[x]
        # Return the count from the Hash Table
        return count